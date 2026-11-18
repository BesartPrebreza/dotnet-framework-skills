# Ef6 Data Access example

This fragment targets .NET Framework 4.8.1. Apply it within the existing project and verify the surrounding configuration.

```text
query.AsNoTracking().Select(x => new StockRow { Quantity = x.Quantity })
```

Inspect generated SQL for server-side predicates and stable ordering.
