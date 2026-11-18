# Restartable Batch Imports example

This fragment targets .NET Framework 4.8.1. Apply it within the existing project and verify the surrounding configuration.

```text
UNIQUE (ImportId, SourceRowNumber)
```

Stop after a committed chunk and restart without duplicating records.
