# Iis Observability example

This fragment targets .NET Framework 4.8. Apply it within the existing project and verify the surrounding configuration.

```text
GET /health/ready
```

Simulate database unavailability and verify the application reports readiness correctly.
