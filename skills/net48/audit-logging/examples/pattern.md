# Audit Logging example

This fragment targets .NET Framework 4.8. Apply it within the existing project and verify the surrounding configuration.

```text
AuditEvent(actorId, "Stock.Adjusted", warehouseId, correlationId)
```

Verify failed and successful actions emit appropriately redacted events.
