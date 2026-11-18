---
name: aspnet-mvc5
description: Use when changing MVC 5 controllers, Razor views or model binding in a classic .NET Framework 4.8 solution.
---

# Aspnet Mvc5

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Keep view models explicit, preserve route and validation conventions and use anti-forgery on cookie-authenticated form writes. Follow post-redirect-get after successful writes where appropriate.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Verify invalid submissions preserve user input and validation messages. Record the checks that ran and identify prerequisites for any outstanding checks.
