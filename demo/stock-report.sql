-- Run in SQL Server. The primary key declares current stock grain.
SET NOCOUNT ON;

CREATE TABLE #CurrentStock (
    WarehouseId int NOT NULL,
    ArticleCode int NOT NULL,
    Barcode varchar(20) NOT NULL,
    Quantity int NOT NULL,
    UnitPrice decimal(19,4) NOT NULL,
    PRIMARY KEY (WarehouseId, ArticleCode, Barcode)
);

CREATE TABLE #ReceiptHistory (ArticleCode int NOT NULL);
INSERT INTO #CurrentStock VALUES (3, 40, '00040', 5, 45), (23, 5789, '05789', 1, 122);
INSERT INTO #ReceiptHistory VALUES (40), (40), (5789);

-- @WarehouseId comes from the application after resource authorization.
DECLARE @WarehouseId int = 3;
DECLARE @ReportTotal decimal(38,4);
DECLARE @Rows int;

SELECT @ReportTotal = SUM(Quantity * UnitPrice), @Rows = COUNT(*)
FROM #CurrentStock
WHERE WarehouseId = @WarehouseId;

IF @Rows <> 1 OR @ReportTotal IS NULL OR @ReportTotal <> 225
    THROW 50001, 'Warehouse report returned unexpected totals or row count.', 1;

SELECT ArticleCode, Barcode, Quantity, UnitPrice, Quantity * UnitPrice AS Total
FROM #CurrentStock
WHERE WarehouseId = @WarehouseId
ORDER BY ArticleCode, Barcode;

DROP TABLE #ReceiptHistory, #CurrentStock;
