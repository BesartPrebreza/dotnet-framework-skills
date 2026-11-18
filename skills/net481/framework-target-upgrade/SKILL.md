---
name: framework-target-upgrade
description: Use when retargeting an existing solution to .NET Framework 4.8 or 4.8.1 in a classic .NET Framework 4.8.1 solution.
---

# Framework Target Upgrade

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Inventory OS support, project targets, vendor libraries, COM, TLS behavior and binding redirects. Upgrade in small steps and test each host, bitness and deployment transform.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Clean-install the package on a supported Windows test host. Record the checks that ran and identify prerequisites for any outstanding checks.
