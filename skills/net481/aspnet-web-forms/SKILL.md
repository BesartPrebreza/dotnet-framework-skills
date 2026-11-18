---
name: aspnet-web-forms
description: Use when changing Web Forms pages, postbacks or controls in a classic .NET Framework 4.8.1 solution.
---

# Aspnet Web Forms

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Respect page lifecycle ordering and recreate dynamic controls early with stable IDs. Rebind initial data on first load when state should survive postbacks.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Verify selection, validators and control events survive a postback. Record the checks that ran and identify prerequisites for any outstanding checks.
