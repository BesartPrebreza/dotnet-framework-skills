# Async Request Pipelines example

This fragment targets .NET Framework 4.8.1. Apply it within the existing project and verify the surrounding configuration.

```text
await query.ToListAsync(cancellationToken)
```

Test disconnected requests and bounded execution under load.
