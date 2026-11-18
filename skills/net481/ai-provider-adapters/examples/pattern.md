# Ai Provider Adapters example

This fragment targets .NET Framework 4.8.1. Apply it within the existing project and verify the surrounding configuration.

```text
Task<Classification> ClassifyAsync(string text, CancellationToken token);
```

Test malformed output, provider outage and cancellation.
