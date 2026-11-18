---
name: scheduled-jobs
description: Use when scheduling recurring Framework jobs in a classic .NET Framework 4.8 solution.
---

# Scheduled Jobs

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Use an existing durable scheduler or Windows Task Scheduler. Track last processed cursor and prevent concurrent sweeps with a durable claim. Specify the time zone and DST policy.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Verify overlap, host restart and daylight-saving transitions. Record the checks that ran and identify prerequisites for any outstanding checks.
