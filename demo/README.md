# Inventory fixture

The executable models the stock report boundary with synthetic in-memory data. It verifies that warehouse authorization runs before the read, that stock from another warehouse stays excluded, and that two historical receipts would inflate an incorrect report. The fixture checks a current-stock result of 225.00.

On Windows with the matching Developer Packs and .NET SDK, run both targets.

```powershell
dotnet run --project demo/InventoryDemo.csproj --framework net48 --configuration Release
dotnet run --project demo/InventoryDemo.csproj --framework net481 --configuration Release
```
