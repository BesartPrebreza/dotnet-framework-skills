# Ef6 Migrations example

This fragment targets .NET Framework 4.8.1. Apply it within the existing project and verify the surrounding configuration.

```text
Update-Database -Script -SourceMigration:Previous -TargetMigration:Next
```

Apply the script to a restored database and verify persisted data.
