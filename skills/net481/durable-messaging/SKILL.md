---
name: durable-messaging
description: Use when integrating queues, retries, dead letters or outbox processing in a classic .NET Framework 4.8.1 solution.
---

# Durable Messaging

1. Inspect the affected project, its host, current packages and integration boundaries. Confirm the effective target framework, C# compiler settings and Windows deployment baseline before changing dependencies.
2. Check client package compatibility, preserve message schema and acknowledge after durable effect. Deduplicate by message ID with a database uniqueness constraint. Bound retry delays and retain actionable dead letter metadata.
3. Consult [the example](examples/pattern.md) for a pattern to adapt to the repository. Preserve existing callers and record any contract changes in the implementation summary.
4. Redeliver after commit and verify the handler applies the effect once. Record the checks that ran and identify prerequisites for any outstanding checks.
