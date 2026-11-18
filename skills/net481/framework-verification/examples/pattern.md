# Framework Verification example

This fragment targets .NET Framework 4.8.1. Apply it within the existing project and verify the surrounding configuration.

```text
MSBuild.exe Inventory.sln /t:Rebuild /p:Configuration=Release
```

Confirm the Release build uses the expected target framework.
