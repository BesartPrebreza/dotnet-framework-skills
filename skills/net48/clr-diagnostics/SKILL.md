---
name: clr-diagnostics
description: Use when investigating CLR CPU, memory, hangs or thread starvation in a classic .NET Framework 4.8 solution.
---

# Clr Diagnostics

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Capture a baseline and correlate counters with incident timestamps. Use scoped PerfView or ETW collection under host policy. Redact paths and customer data before sharing evidence.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Compare CPU, working set and elapsed time across samples. Record the checks that ran and identify prerequisites for any outstanding checks.
