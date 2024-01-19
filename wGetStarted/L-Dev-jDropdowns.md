---
title: "Develop: jDropdown"
filename: "L-Dev-jDropdowns.md"
layout: custom
keywords: [jDropdown, function, develop, build, walkthrough]
headings: ["Overview", "Setting up the Data Connection", "Setting up the Data Portal", "Creating the Stored Procedure", "Testing the Stored Procedure"]
links: ["/wGetStarted/L-Create-Dropdowns.html", "https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/downloading-sample-databases", "https://portal.gointerject.com", "/wPortal/L-Database-Connection.html#testing-the-connection-string-from-within-excel", "https://portal.gointerject.com", "https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-2017", "/wGetStarted/L-Create-Dropdowns.html"]
description: Walks through how to create the stored procedures for the jDropdowns built in the customer aging create report.
---
* * *

## Overview

 If you are looking to build custom jDropdown stored procedures for your reports, then this example will walk you through just that. But first, remember that a jDropdown formula often requires a separate stored procedure from the one used by a data pull or save. You will walk through how to build the Data Connection, Data Portal, and stored procedure for the [jDropdown example](/wGetStarted/L-Create-Dropdowns.html) built on the Customer Aging report. This stored procedure is designed to filter down on the specific options for a parameter. Include all the columns that can be used as filter values in the report.

<blockquote class=highlight_note>
<b>Note:</b> It is required that you have access to build stored procedures in your database to complete this example. This example uses Microsoft's Northwind Database. You can download this database <a href="https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/downloading-sample-databases">here</a> or you can use this example as a guide for your own data source.
</blockquote>

### Setting up the Data Connection

**Step 1:** Navigate to [https://portal.gointerject.com](https://portal.gointerject.com) and log in. Set up a data connection by clicking the **Data Connections** icon.

![](/images/L-Dev-Dropdowns/01.jpg)
<br>

**Step 2:** On the Data Connections page, click the **New Connection** button.

![](/images/L-Dev-Dropdowns/02.jpg)
<br>

**Step 3:** In the Connection Type field, verify that **Database** is selected.

![](/images/L-Dev-Dropdowns/03.jpg)
<br>

**Step 4:** The Connection Details page needs to contain the following information for the new connection: Type **NorthwindExampleDB_MyName** in Connection Name, but include your own name in the suffix. Each connection name must be unique. For the connection string, type **Server=myServerAddress;Database=myDataBase;Trusted_Connection=True;**. This example is using Windows authentication, so username and password are not required. Make sure the server name and database name match the ones you are using for this walkthrough.

![](/images/L-Dev-Dropdowns/04.jpg)
<br>

**Step 5:** In the Description field, include details about how the data connection will be used.

![](/images/L-Dev-Dropdowns/05.jpg)
<br>

**Step 6:** Click the Save button to create the new data connection.

![](/images/L-Dev-Dropdowns/06.jpg)
<br>

The Database Data Connection is now ready to be used in a Data Portal. You should always test a new connection with your security context. Follow the steps in the [Data Connections](/wPortal/L-Database-Connection.html#testing-the-connection-string-from-within-excel) walkthrough to test your connection string.

### Setting up the Data Portal

**Step 1:** To add a new Data Portal, return to [https://portal.gointerject.com](https://portal.gointerject.com) and select **Data Portals** from the sidebar menu.

![](/images/L-Dev-Dropdowns/07.jpg)
<br>

**Step 2:** Click **New Data Portal**.

![](/images/L-Dev-Dropdowns/08.jpg)
<br>

**Step 3:** Type **NorthwindCustomersDropdown_MyName** for the Data Portal Code. Since this field must be unique, add your name to the suffix. Select the connection that was made in the previous step, **NorthwindExampleDB_MyName**. Also enter a name for the stored procedure **\[demo\].\[Northwind_CustomerDropdown\]**, which will be created later.

![](/images/L-Dev-Dropdowns/01.png)
<br>

**Step 4:** Click **Create Data Portal** to save the new data portal. Additional options for adding parameters will show after selecting the Create Data Portal button.

![](/images/L-Dev-Dropdowns/02.png)
<br>

**Step 5:** To add your first formula parameter, click **Click here to add a Formula Parameter**. For this parameter, enter **Filter** for Name, **varchar** for Type, and **input** for Direction to input, as shown below. This parameter will be set up in the Stored Procedure to receive a word that will filter the data returned.

![](/images/L-Dev-Dropdowns/03.png)
<br>

### Creating the Stored Procedure

Open up a text editor of your choice. This example will use [SSMS](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-2017){:target="_blank"}{:rel="noopener noreferrer"} to execute the code, but again, you can use whichever you prefer. You will be creating this stored procedure in the database you created for the [data connection](#setting-up-the-data-connection).

Create a stored procedure called [demo].[Northwind_CustomerDropdown] using the following code example:

<button class = "collapsible"> Northwind_CustomerDropdown </button>
<div markdown="1" class="panel">

```sql
CREATE PROCEDURE [demo].[Northwind_CustomerDropdown]

	@Filter varchar(255) = ''

AS

-- Customer Search
SELECT
	 [CustomerID]
	,[CompanyName]
	,([CustomerID]+' - '+[CompanyName]) AS [DisplayText]
FROM [demo].[Northwind_Customers]
WHERE
	(@Filter = '' OR CompanyName LIKE '%' + @Filter + '%')
	OR
	(@Filter = '' OR CustomerID LIKE '%' + @Filter + '%')
ORDER BY [DisplayText]

-- Contact Search
SELECT
	 [ContactName]	
	,[ContactTitle]
	,([ContactName]+' - '+[ContactTitle]) AS [DisplayText]
FROM [Demo].[Northwind_Customers]
WHERE
	(@Filter = '' OR ContactName LIKE '%' + @Filter + '%')
	OR
	(@Filter = '' OR ContactTitle LIKE '%' + @Filter + '%')
ORDER BY [DisplayText]

-- Customer ID
SELECT
	 [CustomerID]	
	,[CompanyName]
	,([CustomerID]+' - '+[CompanyName]) AS [DisplayText]
FROM [Demo].[Northwind_Customers]
WHERE
	(@Filter = '' OR ContactName LIKE '%' + @Filter + '%')
	OR
	(@Filter = '' OR CustomerID LIKE '%' + @Filter + '%')
ORDER BY [DisplayText]
GO
```

</div>

Stored procedures are natively supported by Interject. There are a few key areas to note in the code example above that help illustrate Interject features:

* **Parameters:** The parameters included in the Stored Procedure are the same as those added to the Data Portal. On each request, Interject passes the Formula Parameters values from the spreadsheet configuration to the Stored Procedure along with System Parameters. Output parameters that can populate values in the spreadsheet are supported, but they are not included in this example. In this example, there is only one formula parameter: "filter".

* **Select statements:** Returning data to Interject uses a select statement. More than one can be returned at a time to reduce the connections needed to fully populate a complex report. Notice the procedure returns 3 select statements, each representing a different data set return to Interject.

### Testing the Stored Procedure

It is important to test the Stored Procedure in the database before testing through the Interject platform. The example code includes a test SQL statement that can be executed in a new query, as shown below. Be sure to change the procedure name to match your own.

<button class="collapsible">Example Test Script</button>
<div markdown="1" class="panel">

```sql
	EXEC [demo].[Northwind_CustomerDropdown]
		@Filter = 'Market'
```

</div>

When executed, you should see the following result sets. Notice there are three different result sets. Each of them returns only values that contained the word **Market**.

![](/images/L-Dev-Dropdowns/TestStoreProcedureResult.png)
<br>

To see an example of how to set up a jDropdown within Excel, see [Create: Building jDropdowns](/wGetStarted/L-Create-Dropdowns.html).
