# Framework Testing example

This fragment targets .NET Framework 4.8.1. Apply it within the existing project and verify the surrounding configuration.

```text
vstest.console.exe Inventory.Tests.dll
```

Run tests twice and verify they do not depend on execution order.
