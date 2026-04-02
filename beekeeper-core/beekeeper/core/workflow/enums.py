from enum import Enum


class DocStrategy(Enum):
    """
    Document de-duplication strategies work by comparing the hashes in the vector store.
    They require a vector store to be set.
    """

    DUPLICATE_ONLY = "duplicate_only"
    DUPLICATE_AND_DELETE = "duplicate_and_delete"
    DEDUPLICATE_OFF = "deduplicate_off"
