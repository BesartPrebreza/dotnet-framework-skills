# Csharp Nullability example

This fragment targets .NET Framework 4.8. Apply it within the existing project and verify the surrounding configuration.

```text
if (request == null) throw new ArgumentNullException(nameof(request));
```

Test omitted JSON fields, database nulls and empty collections.
