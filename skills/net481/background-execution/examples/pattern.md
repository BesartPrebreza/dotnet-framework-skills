# Background Execution example

This fragment targets .NET Framework 4.8.1. Apply it within the existing project and verify the surrounding configuration.

```text
await handler.ProcessAsync(job, stoppingToken)
```

Restart the worker between claim and completion and verify recovery.
