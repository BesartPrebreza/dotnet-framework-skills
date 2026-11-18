# Winforms Maintenance example

This fragment targets .NET Framework 4.8. Apply it within the existing project and verify the surrounding configuration.

```text
if (InvokeRequired) { BeginInvoke(updateUi); return; }
```

Close the form while data loads and check for disposed-control callbacks.
