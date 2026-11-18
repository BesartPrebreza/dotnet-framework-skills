# Framework Configuration example

This fragment targets .NET Framework 4.8.1. Apply it within the existing project and verify the surrounding configuration.

```text
ConfigurationManager.AppSettings["TimeoutSeconds"]
```

Reject zero, negative and malformed timeout values.
