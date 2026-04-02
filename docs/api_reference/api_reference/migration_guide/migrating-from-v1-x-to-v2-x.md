# Migration Guide

This guide describes the breaking changes and required updates to migrate from 1.x to 2.x.

## 🔴 Breaking Changes

### 1. Removed Methods

#### `BaseDocument`

The following methods have been removed in favor of direct property access:

| ❌ Removed Method  | ✅ Replacement        |
| ----------------- | -------------------- |
| `get_metadata()`  | `document.metadata`  |
| `get_embedding()` | `document.embedding` |

---

#### `DocumentWithScore`

The following methods have been removed:

| ❌ Removed Method | ✅ Replacement                                                         |
| ---------------- | --------------------------------------------------------------------- |
| `get_score()`    | `document_with_score.normalized_score`                                |
| `get_content()`  | `document_with_score.content`                                         |
| `get_metadata()` | `document_with_score.metadata`                                        |

---

### 2. Embeddings API Change

#### `embed_text`

* Now **always returns a list** of embeddings.

**Before:**

```python
embedding = embed_text("hello world")  # could return a single vector
```

**After:**

```python
embeddings = embed_text("hello world")  # always returns a list
embedding = embeddings[0]
```

⚠️ **Important:** Update any code that assumes a single embedding vector is returned.

---

### 3. watsonx Observability Changes

#### Removed

* ❌ `WatsonxLocalMetric`

---

#### Renamed

| ❌ Old Name      | ✅ New Name          |
| --------------- | ------------------- |
| `WatsonxMetric` | `WatsonxMetricSpec` |

---

### 4. Import Path Changes

Module paths have been updated to reflect the new naming conventions.

| ❌ Old Import         | ✅ New Import              |
| -------------------- | ------------------------- |
| `beekeeper.readers`  | `beekeeper.loaders`       |
| `beekeeper.monitors` | `beekeeper.observability` |


## 🔍 Quick Find & Replace Suggestions

You can use these patterns to accelerate migration:

| Find                  | Replace                         |
| --------------------- | ------------------------------- |
| `.get_metadata()`     | `.metadata`                     |
| `.get_embedding()`    | `.embedding`                    |
| `.get_score()`        | `.score` or `.normalized_score` |
| `.get_content()`      | `.content`                      |
| `WatsonxMetric`       | `WatsonxMetricSpec`             |
| `WatsonxLocalMetric`  | *(remove usage)*                |
