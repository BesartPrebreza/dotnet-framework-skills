# Ef6 Transactions example

This fragment targets .NET Framework 4.8. Apply it within the existing project and verify the surrounding configuration.

```text
using (var transaction = db.Database.BeginTransaction()) { db.SaveChanges(); transaction.Commit(); }
```

Force the second write to fail and verify atomic rollback.
