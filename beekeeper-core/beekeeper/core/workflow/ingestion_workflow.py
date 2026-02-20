from beekeeper.core.document import Document
from beekeeper.core.loaders import BaseLoader
from beekeeper.core.schema import TransformerComponent
from beekeeper.core.vector_stores import BaseVectorStore
from beekeeper.core.workflow.enums import DocStrategy


class IngestionWorkflow:
    """
    An ingestion workflow for processing and storing data.

    Attributes:
        transformers (list[TransformerComponent]): A list of transformer components applied to the input documents.
        doc_strategy (DocStrategy): The strategy used for handling document duplicates.
            Defaults to `DocStrategy.DUPLICATE_ONLY`.
        post_transformer (bool): Whether document de-duplication should be applied after transformation step.
            Defaults to `False`.
        readers (BaseLoader, optional): List of loaders for loading or fetching documents.
        vector_store (BaseVectorStore, optional): Vector store for saving processed documents

    Example:
        ```python
        from beekeeper.core.workflows import IngestionWorkflow
        from beekeeper.core.text_chunkers import TokenTextChunker
        from beekeeper.embeddings.huggingface import HuggingFaceEmbedding

        ingestion_workflow = IngestionWorkflow(
            transformers=[
                TokenTextChunker(),
                HuggingFaceEmbedding(model_name="intfloat/multilingual-e5-small"),
            ]
        )
        ```
    """

    def __init__(
        self,
        transformers: list[TransformerComponent],
        doc_strategy: DocStrategy = DocStrategy.DUPLICATE_ONLY,
        post_transformer: bool = False,
        readers: list[BaseLoader] | None = None,
        vector_store: BaseVectorStore | None = None,
    ) -> None:
        self.doc_strategy = doc_strategy
        self.post_transformer = post_transformer
        self.transformers = transformers
        self.readers = readers
        self.vector_store = vector_store

    def _read_documents(self, documents: list[Document] | None):
        input_documents = []

        if documents is not None:
            input_documents.extend(documents)

        if self.readers is not None:
            for reader in self.readers:
                input_documents.extend(reader.load_data())

        return input_documents

    def _handle_duplicates(self, documents) -> list[Document]:
        ids, existing_hashes, existing_ref_hashes = (
            self.vector_store.get_all_document_hashes()
        )

        if self.post_transformer:
            # Use own document hash (chunks level) for de-duplication
            hashes_fallback = existing_hashes
        else:
            # Use parent document hash `ref_doc_hash`
            # Fallback to document own hash if `ref_doc_hash` (parent level) is missing for de-duplication
            hashes_fallback = [
                existing_ref_hashes[i]
                if existing_ref_hashes[i] is not None
                else existing_hashes[i]
                for i in range(len(existing_ref_hashes))
            ]

        current_hashes = []
        current_unique_hashes = []
        dedup_documents_to_run = []

        for doc in documents:
            current_hashes.append(doc.hash)

            if (
                doc.hash not in hashes_fallback
                and doc.hash not in current_unique_hashes
                and doc.get_content() != ""
            ):
                dedup_documents_to_run.append(doc)
                current_unique_hashes.append(
                    doc.hash,
                )  # Prevent duplicating same document hash in same batch workflow execution.

        if self.doc_strategy == DocStrategy.DUPLICATE_AND_DELETE:
            ids_to_remove = [
                ids[i]
                for i in range(len(hashes_fallback))
                if hashes_fallback[i] not in current_hashes
            ]

            if self.vector_store is not None:
                self.vector_store.delete_documents(ids_to_remove)

        return dedup_documents_to_run

    def _run_transformers(
        self,
        documents: list[Document],
        transformers: list[TransformerComponent],
    ) -> list[Document]:
        _documents = documents.copy()

        for transformer in transformers:
            _documents = transformer(_documents)

        return _documents

    def run(self, documents: list[Document] = None) -> list[Document]:
        """
        Run an ingestion workflow.

        Args:
            documents: Set of documents to be transformed.

        Example:
            ```python
            ingestion_workflow.run(documents: list[Document])
            ```
        """
        documents_processed = []
        input_documents = self._read_documents(documents)

        if (
            self.vector_store is not None
            and self.doc_strategy != DocStrategy.DEDUPLICATE_OFF
            and not self.post_transformer
        ):
            # Apply transformers before de-dup (parent level)

            documents_to_run = self._handle_duplicates(input_documents)
        else:
            # Apply transformers after de-dup (chunk level)
            documents_to_run = input_documents

        if documents_to_run:
            documents_processed = self._run_transformers(
                documents_to_run,
                self.transformers,
            )

            # Apply transformers after de-dup (chunk level)
            if (
                self.vector_store is not None
                and self.doc_strategy != DocStrategy.DEDUPLICATE_OFF
                and self.post_transformer
            ):
                documents_processed = self._handle_duplicates(documents_processed)

            if self.vector_store is not None and documents_processed:
                self.vector_store.add_documents(documents_processed)

        return documents_processed
