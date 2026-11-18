# Web Api 2 Conventions example

This fragment targets .NET Framework 4.8. Apply it within the existing project and verify the surrounding configuration.

```text
if (!ModelState.IsValid) return BadRequest(ModelState);
```

Assert response status, media type and Location.
