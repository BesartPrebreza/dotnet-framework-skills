---
name: windows-incident-triage
description: Use when triaging a production incident in a Framework application in a classic .NET Framework 4.8.1 solution.
---

# Windows Incident Triage

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Establish scope and operating authority. Capture timestamps, application logs and approved Windows/IIS evidence. Keep changes under incident procedures and redact handoffs.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Reconcile the timeline and identify the evidence supporting each conclusion. Record the checks that ran and identify prerequisites for any outstanding checks.
