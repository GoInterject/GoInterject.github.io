CREATE PROC [demo].[Northwind_Customers_Pull_MyName]

     @CompanyName					VARCHAR(100)
    ,@ContactName					VARCHAR(100)
    ,@CustomerID					VARCHAR(500) = ''
    ,@Interject_NTLogin				VARCHAR(50) 
    ,@Interject_LocalTimeZoneOffset MONEY

AS
BEGIN

SET NOCOUNT ON  -- helps reduce conflicts with ADO

DECLARE @DateCompare VARCHAR(20) = '1997-09-15'
DECLARE @ErrorMessage VARCHAR(100)

IF LEN(@CompanyName)>40
BEGIN
    SET @ErrorMessage = 'Usernotice:The company search text must not be more than 40 characters.'
    RAISERROR (@ErrorMessage, 18, 1)
    RETURN		
END

--CREATE CTE to consolidate the invoice data into seperate categories based on date
;WITH Invoice_CTE
AS
(
    SELECT 
         CustomerID
        ,SUM(InvoiceTotal)	AS InvoiceTotal
        ,SUM([Current])		AS [Current]
        ,SUM([30Days])		AS [30Days]
        ,SUM([60Days])		AS [60Days]
        ,SUM([90Days])		AS [90Days]
        ,IsPaid
    FROM 
    (
    SELECT 
         i.CustomerID
        ,i.InvoiceDate
        ,i.InvoiceTotal
        ,CASE WHEN DATEDIFF(dd,i.InvoiceDate,@DateCompare) < 30	THEN (i.InvoiceTotal) ELSE 0 END AS [Current]
        ,CASE WHEN DATEDIFF(dd,i.InvoiceDate,@DateCompare) between 30 and 59 THEN (i.InvoiceTotal) ELSE 0 END AS [30Days]
        ,CASE WHEN DATEDIFF(dd,i.InvoiceDate,@DateCompare) between 60 and 89 THEN (i.InvoiceTotal) ELSE 0 END AS [60Days]
        ,CASE WHEN DATEDIFF(dd,i.InvoiceDate,@DateCompare) > 90	THEN (i.InvoiceTotal) ELSE 0 END AS [90Days]
        ,IsPaid
    FROM [demo].[Northwind_Invoices] i
    WHERE IsPaid = 0 --This line selects the invoices that have not been paid 
    ) t
    GROUP BY CustomerID, IsPaid
)

SELECT 
     c.[CustomerID]
    ,c.[CompanyName]
    ,c.[ContactName]
    ,c.[ContactTitle]
    ,ISNULL(c.[Address],'') AS [Address]
    ,c.[City]
    ,c.[Region]
    ,c.[PostalCode]
    ,c.[Country]
    ,c.[Phone]
    ,cte.[Current]
    ,cte.[30Days]
    ,cte.[60Days]
    ,cte.[90Days]
    ,cte.IsPaid
    ,ISNULL(c.PostalCode,'') + ',' + ISNULL(c.Country,'') AS TestValueList
FROM [demo].[Northwind_Customers] c
    LEFT JOIN Invoice_CTE cte
        ON c.CustomerID = cte.CustomerID
WHERE 
    (@CompanyName='' OR c.CompanyName LIKE '%' + @CompanyName + '%')
    AND
    (@ContactName='' OR c.ContactName LIKE '%' + @ContactName + '%')
    AND
    (@CustomerID='' OR c.CustomerID = @CustomerID)
ORDER BY c.[CompanyName] 
    
END