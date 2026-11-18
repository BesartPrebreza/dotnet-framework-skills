# Durable Messaging example

This fragment targets .NET Framework 4.8.1. Apply it within the existing project and verify the surrounding configuration.

```text
UNIQUE (ConsumerName, MessageId)
```

Redeliver after commit and verify the handler applies the effect once.
