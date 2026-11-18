# Framework Scaffolding example

This fragment targets .NET Framework 4.8.1. Apply it within the existing project and verify the surrounding configuration.

```text
MSBuild.exe Inventory.sln /restore /p:RestorePackagesConfig=true
```

Verify a clean checkout builds on Windows.
