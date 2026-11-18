# Multi Tenancy example

This fragment targets .NET Framework 4.8.1. Apply it within the existing project and verify the surrounding configuration.

```text
Where(x => x.TenantId == tenantId)
```

Test two tenants with overlapping local IDs in reads, writes and exports.
