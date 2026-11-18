---
name: web-api-2-conventions
description: Use when creating or changing System.Web HTTP endpoints and DTOs in a classic .NET Framework 4.8 solution.
---

# Web Api 2 Conventions

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Use Web API 2 ApiController conventions and preserve existing routes. Validate ModelState, bind DTOs and return 201 with a resolvable Location if a resource is created.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Assert response status, media type and Location. Record the checks that ran and identify prerequisites for any outstanding checks.
