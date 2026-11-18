---
name: iis-windows-deployment
description: Use when deploying System.Web or WCF to IIS or Windows containers in a classic .NET Framework 4.8 solution.
---

# Iis Windows Deployment

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Confirm Windows base image and host compatibility. Match app-pool bitness and identity, apply transforms per environment and sanity-check permissions. Stage health checks and validate rollback artifacts before rollout.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Test startup under the deployed service identity and configured virtual path. Record the checks that ran and identify prerequisites for any outstanding checks.
