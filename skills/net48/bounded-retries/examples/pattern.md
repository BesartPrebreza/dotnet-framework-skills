# Bounded Retries example

This fragment targets .NET Framework 4.8. Apply it within the existing project and verify the surrounding configuration.

```text
await Task.Delay(backoff, cancellationToken)
```

Test exhausted retries and cancellation during delay.
