
CREATE PROC [demo].[Northwind_Invoices_Pull_MyName]

     @CompanyName VARCHAR(100)
    ,@ContactName NVARCHAR(100)
    ,@CustomerID VARCHAR(500) = ''
    ,@IncludePaid VARCHAR(5) = 0
    ,@Interject_RequestContext NVARCHAR(MAX)

AS
BEGIN

SET NOCOUNT ON  -- helps reduce conflicts with ADO

DECLARE @Interject_LoginName VARCHAR(200)
DECLARE @UtcOffset	DECIMAL(6,4)

-- Dataset has very old dates
-- To give a static date to compare to we hard coded the date.
DECLARE @DateCompare VARCHAR(20) = '1997-09-15'
DECLARE @ErrorMessage VARCHAR(100)

IF LEN(@CompanyName)>40
BEGIN
    SET @ErrorMessage = 'Usernotice:The company search text must not be more than 40 characters.'
    RAISERROR (@ErrorMessage, 18, 1)
    RETURN		
END

-- This is another SP that parses the xml in request context to get the needed system data
EXEC [demo].[RequestContext_Parse]
    @Interject_RequestContext		= @Interject_RequestContext	
    ,@Interject_LoginName			= @Interject_LoginName	OUTPUT
    ,@UtcOffset = @UtcOffset OUTPUT

-- @IncludePaid is default 0.
-- if set to Yes, change it to 1
IF @IncludePaid = 'Yes'
    SET @IncludePaid = 1

-----------------------------------------------
--	REMAINDER OF DATA QUERY
-----------------------------------------------
--Create CTE that sorts data by InvoiceDate's difference from the hardcoded DateCompare
;WITH Invoice_CTE
AS
(
    SELECT 
            [CustomerID]
        ,[InvoiceID]
        ,[InvoiceNum]
        ,[InvoiceTotal]
        ,[Current]
        ,[30Days]
        ,[60Days]
        ,[90Days]
        ,[IsPaid]
    FROM 
    (
        SELECT 
                i.[CustomerID]
            ,i.[InvoiceID]
            ,i.[InvoiceNum]
            ,i.[InvoiceDate]
            ,i.[InvoiceTotal]
            ,CASE WHEN DATEDIFF(dd,InvoiceDate,@DateCompare) < 30 THEN (i.[InvoiceTotal]) ELSE 0 END AS [Current]
            ,CASE WHEN DATEDIFF(dd,InvoiceDate,@DateCompare) BETWEEN 30 AND 59 THEN (i.[InvoiceTotal]) ELSE 0 END AS [30Days]
            ,CASE WHEN DATEDIFF(dd,InvoiceDate,@DateCompare) BETWEEN 60 AND 89 THEN (i.[InvoiceTotal]) ELSE 0 END AS [60Days]
            ,CASE WHEN DATEDIFF(dd,InvoiceDate,@DateCompare) > 90 THEN (i.[InvoiceTotal]) ELSE 0 END AS [90Days]
            ,@IncludePaid AS IsPaid
        FROM [demo].[Northwind_Invoices] i
    ) t
    WHERE [IsPaid] = @IncludePaid
    GROUP BY [CustomerID]
            ,[InvoiceID] 
            ,[InvoiceNum]
            ,[InvoiceTotal]
            ,[Current]
            ,[30Days]
            ,[60Days]
            ,[90Days]
            ,[IsPaid]
)
-- Final Select statement
SELECT
        c.[CustomerID]
    ,c.[CompanyName]
    ,c.[ContactName]
    ,c.[ContactTitle]
    ,c.[Country]
    ,i.[InvoiceID]
    ,i.[InvoiceNum]
    ,i.[InvoiceDate]
    ,i.[OrderTotal]
    ,i.[Freight]
    ,i.[InvoiceTotal]
    ,i.[BillName]
    ,i.[BillAddress]
    ,i.[BillCity]
    ,i.[BillCountry]
    ,i.[IsPaid]
    ,o.[OrderID]
    ,cte.[IsPaid]
    ,cte.[Current]
    ,cte.[30Days]
    ,cte.[60Days]
    ,cte.[90Days]
    ,p.[PaidAmount]
    ,n.[KeyValue] AS Note
    ,d.[KeyValue] AS ExpectedDate
FROM [demo].[Northwind_Invoices] i
LEFT JOIN [demo].[Northwind_Customers] c
    ON i.[CustomerID] = c.[CustomerID]
LEFT JOIN Invoice_CTE cte
    ON cte.[InvoiceID] = i.[InvoiceID]
LEFT JOIN demo.Northwind_Payments p
    ON i.[InvoiceID] = p.[InvoiceID]
LEFT JOIN demo.Northwind_Orders o
    ON o.[CustomerID] = i.[CustomerID]
    AND o.[Freight] = i.[Freight]
LEFT JOIN demo.Northwind_InvoiceExternal n
    ON n.[InvoiceID] = i.[InvoiceID]
    AND n.[KeyName] = 'NOTE'
LEFT JOIN demo.Northwind_InvoiceExternal d
    ON d.[InvoiceID] = i.[InvoiceID]
    AND d.[KeyName] = 'ExpectedDate'
WHERE 
    i.IsPaid = @IncludePaid
    AND
    (@CompanyName='' OR c.[CompanyName] LIKE '%' + @CompanyName + '%')
    AND
    (@ContactName='' OR c.[ContactName] LIKE '%' + @ContactName + '%')
    AND
    (@CustomerID='' OR c.[CustomerID] = @CustomerID)
ORDER BY c.[CompanyName]
        ,i.[InvoiceDate]
        ,i.[InvoiceID]

END