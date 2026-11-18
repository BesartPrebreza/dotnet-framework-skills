# Api Versioning example

This fragment targets .NET Framework 4.8.1. Apply it within the existing project and verify the surrounding configuration.

```text
[Route("api/v2/warehouses/{id:int}")]
```

Run both versions with the same resource and verify their contracts independently.
