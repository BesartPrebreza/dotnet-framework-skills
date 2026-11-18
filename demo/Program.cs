using System;
using System.Collections.Generic;
using System.Linq;

internal sealed class Stock
{
    public Stock(int warehouseId, int articleCode, string barcode, int quantity, decimal unitPrice)
    {
        WarehouseId = warehouseId;
        ArticleCode = articleCode;
        Barcode = barcode;
        Quantity = quantity;
        UnitPrice = unitPrice;
    }

    public int WarehouseId { get; }
    public int ArticleCode { get; }
    public string Barcode { get; }
    public int Quantity { get; }
    public decimal UnitPrice { get; }
    public decimal Total => Quantity * UnitPrice;
}

internal sealed class StockReport
{
    private readonly Func<IEnumerable<Stock>> readCurrentStock;

    public StockReport(Func<IEnumerable<Stock>> readCurrentStock)
    {
        this.readCurrentStock = readCurrentStock;
    }

    public IReadOnlyList<Stock> Read(int warehouseId, ISet<int> allowedWarehouses)
    {
        if (!allowedWarehouses.Contains(warehouseId))
        {
            throw new UnauthorizedAccessException("Warehouse access denied.");
        }

        return readCurrentStock()
            .Where(row => row.WarehouseId == warehouseId)
            .OrderBy(row => row.ArticleCode)
            .ThenBy(row => row.Barcode, StringComparer.Ordinal)
            .ToList();
    }
}

internal static class Program
{
    private static int Main()
    {
        var stock = new[]
        {
            new Stock(3, 40, "00040", 5, 45m),
            new Stock(23, 5789, "05789", 1, 122m)
        };
        var historicalReceiptArticles = new[] { 40, 40, 5789 };
        var reads = 0;
        var report = new StockReport(() => { reads++; return stock; });
        var allowed = new HashSet<int> { 3 };
        var results = report.Read(3, allowed);
        var row = results.Single();
        Require(row.ArticleCode == 40 && row.Barcode == "00040", "Unexpected report identity.");
        Require(row.Quantity == 5 && row.UnitPrice == 45m && row.Total == 225m, "Incorrect stock totals.");
        var duplicatedValue = historicalReceiptArticles.Where(article => article == row.ArticleCode)
            .Sum(article => row.Total);
        Require(duplicatedValue == 450m, "Fixture must reproduce duplicate receipt inflation.");
        Require(report.Read(99, new HashSet<int> { 99 }).Count == 0, "Unknown allowed warehouse should be empty.");

        try
        {
            report.Read(23, allowed);
        }
        catch (UnauthorizedAccessException)
        {
            Require(reads == 2, "Denied access attempted to read stock.");
            Console.WriteLine("Verified warehouse isolation, report grain and exact stock totals.");
            return 0;
        }

        throw new InvalidOperationException("Warehouse access was not denied.");
    }

    private static void Require(bool condition, string message)
    {
        if (!condition)
        {
            throw new InvalidOperationException(message);
        }
    }
}
