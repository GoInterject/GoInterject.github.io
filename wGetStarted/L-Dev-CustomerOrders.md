---
title: "Lab Developer: Customer Orders"
layout: custom
keywords: [developer, example, customer orders, walkthrough, SQL]
description: In this example, you will how to create a second report, Customer Orders, that will be drilled to from the Customer Aging Report you built in the last lab. This uses a report range.
---
* * *

##  **Overview**

In this example, you will how to create a second report, Customer Orders, that will be drilled to from the Customer Aging Report you built in the [last lab](/wGetStarted/L-Dev-CustomerAging.html). You should have already seen the Customer Orders report while reviewing the business use case in the lab. Continue to build the INTERJECT configuration and database objects to support the report. 

###  Verifying the Data Connection 

Because this report uses the same database as the previous example, you do not need to create another data connection. The same connection can be used for this report. The connection created in the example text was named **NorthwindExampleDB_MyName** and  you should use the same naming conventions for your connection  . 

###  Copy the Data Portal 

**Step 1:** Navigate to the data portal, **NorthwindCustomers_MyName** , and click the green clone button on the top right corner of the page. 

![](/images/L-DevCustOrders/01.png)
<br>
  


**Step 2:** A new data portal named, **NorthwindCustomers_MyName_copy** , generates. Change this data portal name to **NorthwindOrders_MyName** . Since each Data Portal must have a unique code, please use your name instead of **_MyName** . Then click Save Changes 

![](/images/L-DevCustOrders/02.png)
<br>
  


**Step 3:** Change the procedure name to run **[Demo].[Northwind_CustomerOrders_Pull_MyName]** , which you will create next. Then click **Save Changes**. 

![](/images/L-DevCustOrders/03.jpg)
<br>

###  Creating the Stored Procedure 

A stored procedure or data API servers as a middle tier for an INTERJECT report. In this example, you are using a stored procedure. INTERJECT can retrieve one or more result sets from the stored procedure into the spreadsheet report. 

The INTERJECT Website Portal allows you to create and manage data portals and reference stored procedures you create. Data portals are stored locally in your Excel session when you log into INTERJECT. When requesting data, INTERJECT creates a point-to-point connection with the intended data source. 

The steps below assume you are proficient with SQL Management Studio for Microsoft SQL Server and in creating stored procedures. If you need additional training in this area, please contact us at [ info@gointerject.com ](mailto:info@gointerject.com) . 

**Step 1:** Create a stored procedure called [demo].[Northwind_CustomerOrders_Pull_MyName] using the following code: 

<button class="collapsible">\[demo\].\[Northwind_CustomerOrders_Pull_MyName\]</button>
<div markdown="1" class="panel">

```sql
    CREATE PROC [demo].[Northwind_CustomerOrders_Pull_MyName]
    
    	 @CompanyName						VARCHAR(100)
    	,@ContactName						VARCHAR(100)
    	,@CustomerID						VARCHAR(500) = ''
    	,@Interject_NTLogin					VARCHAR(10)
    	,@Interject_LocalTimeZoneOffset		MONEY
    
    AS
    BEGIN
    
    SET NOCOUNT ON  -- helps reduce conflicts with ADO
    
    DECLARE @ErrorMessage VARCHAR(100)
    
    IF LEN(@CompanyName)>40
    BEGIN
    	SET @ErrorMessage = 'Usernotice:The company search text must not be more than 40 characters.'
    	RAISERROR (@ErrorMessage, 18, 1)
    	RETURN		
    END
    
    SELECT 
    	 c.[CustomerID]
    	,c.[CompanyName]
    	,c.[ContactName]
    	,c.[Country]
    	,o.[OrderID]
    	,o.[OrderDate]
    	,o.[ShipCity]
    	,o.[ShipCountry]
    	,s.[CompanyName] AS ShipVia
    	,o.[ShippedDate]
    	,SUM(d.[UnitPrice] * cast(d.[Quantity] AS MONEY) * (cast(1 AS MONEY) -d.[Discount])) AS OrderAmount
    	,o.[Freight]
    	,SUM(d.[UnitPrice] * cast(d.[Quantity] AS MONEY) * (cast(1 AS MONEY) -d.[Discount])) + o.[Freight] AS TotalAmount
    FROM [demo].[Northwind_Orders] o
    	INNER JOIN [demo].[Northwind_Customers] c
    		ON o.[CustomerID] = c.[CustomerID]
    	INNER JOIN [demo].[Northwind_Shippers] s
    		ON o.[ShipVia] = s.[ShipperID]
    	INNER JOIN [demo].[Northwind_Order Details] d
    		ON o.[OrderID] = d.[OrderID]
    WHERE 
    	(@CompanyName='' OR c.CompanyName LIKE '%' + @CompanyName + '%')
    	and
    	(@ContactName='' OR c.ContactName LIKE '%' + @ContactName + '%')
    	and
    	(@CustomerID='' OR c.[CustomerID] = @CustomerID)
    GROUP BY
    	 c.[CustomerID]
    	,c.[CompanyName]
    	,c.[ContactName]
    	,c.[Country]
    	,o.[OrderID]
    	,o.[OrderDate]
    	,o.[ShipName]
    	,o.[ShipCity]
    	,o.[ShipCountry]
    	,s.[CompanyName]
    	,o.[ShippedDate]
    	,o.[Freight]
    ORDER BY c.[CompanyName], o.[OrderID]  DESC
    
    END
```

</div>

**Step 2:** INTERJECT supports stored procedures natively. Here are a few key areas to note in the code above that help illustrate INTERJECT features. 

  * Parameters: The parameters included in the stored procedure are the same parameters added to the data portal in a previous step. For each request, INTERJECT passes the formula parameter values from the spreadsheet configuration, along with system parameters, to the stored procedure. Output parameters are supported and can populate values in the spreadsheet, but they are not included in this example. 



![](/images/L-DevCustOrders/04.png)
<br>

  * Validation: The code above includes an example of validating the input from the formula parameter, **@CustomerName** . It limits the search text to 40 characters and displays an error when the length is exceeded. This error has a prefix, **UserNotice:** which tells INTERJECT to provide a message box with the text to the user as a response. Without the prefix, INTERJECT interprets the error as a generic error. 



![](/images/L-DevCustOrders/05.png)
<br>

  * Select statements: Returning data to INTERJECT simply uses a select statement as shown below. More than one select statement can be returned at a time to reduce the connections needed to fully populate a complex report. You only have one select statement in this example. 



![](/images/L-DevCustOrders/06.png)
<br>

**Step 3:** It is important to test the stored procedure in the database before testing through the INTERJECT platform. The code below is an example that includes a test SQL statement. 

<button class="collapsible">Example Test Script</button>
<div markdown="1" class="panel">

```sql 
    Execute [demo].[Northwind_CustomerOrders_Pull_MyName]
    	@CompanyName = 'market'
    	,@ContactName = ''
    	,@CustomerID = ''
    	,@Interject_NTLogin = 'MaryM'
    	,@Interject_LocalTimeZoneOffset = -7
```

</div>
When this code is executed, it returns the following result set. 

![](/images/L-DevCustOrders/07.png)
<br>

 

###  Create The Report: 

At this point you have a tested stored procedure that uses parameters to filter the results. An INTERJECT Data Connection is setup to go to your example database and you added an INTERJECT Data Portal to use that connection and is mapped to the stored procedure that was just created. You are ready to build the spreadsheet report. 

Fortunately, the documentation to build this report has already been presented in **Create: Customer Orders** and you likely have already completed it. The end result should look like the below screenshot. 

![](/images/L-DevCustOrders/08.png)
<br>
  


It is recommended to go to [Lab Create: Customer Orders](/wGetStarted/L-Create-CustomerOrders.html) to complete those steps again to reinforce the process. However, this time you can use your own Data Portal for the report. 

 
