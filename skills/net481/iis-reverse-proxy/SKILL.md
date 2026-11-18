---
name: iis-reverse-proxy
description: Use when maintaining an existing IIS ARR reverse proxy or API edge in a classic .NET Framework 4.8.1 solution.
---

# Iis Reverse Proxy

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Keep backend targets explicit, set bounded timeouts, and apply forwarded header trust at the proxy boundary. Scope retries to replay-safe traffic and validate health routes.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Check trusted proxy routing and client URL generation. Record the checks that ran and identify prerequisites for any outstanding checks.
