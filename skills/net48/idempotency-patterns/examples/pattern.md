# Idempotency Patterns example

This fragment targets .NET Framework 4.8. Apply it within the existing project and verify the surrounding configuration.

```text
UNIQUE (CallerId, OperationName, RequestKey)
```

Send two concurrent requests and assert one business effect.
