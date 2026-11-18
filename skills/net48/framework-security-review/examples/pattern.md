# Framework Security Review example

This fragment targets .NET Framework 4.8. Apply it within the existing project and verify the surrounding configuration.

```text
[ValidateAntiForgeryToken]
```

Verify a protected state change rejects a request without a valid anti-forgery token.
