---
title: "Lab Developer: jDropdown Stored Procedures"
layout: custom
keywords: [jDropdown, function]
description: Walks through how to create the stored procedures for the jDropdowns built in the customer aging create report
---

## Overview

 A dropdown formula often requires a seperate stored procedure from the one used by the pull or save. This lab walks you through how to build the data connection, dataportal, and stored procedure for the [jDropdown example](/wGetStarted/L-Create-Dropdowns.html) built on the Customer Aging report. This stored procedure is designed to filter down on the specific options for a parameter and include all the columns that can be used as filter values in the report.

> **IMPORTANT:**  It is required that you have access to build stored procedures in your database to complete this lab. 

###  Setting Up The Data Connection

**Step 1:** Navigate to [ https://portal.gointerject.com ](https://portal.gointerject.com) and log in. Set up a data connection by clicking the **Data Connections** icon. 

![](/images/L-Dev-CustAging/01.jpg)
<br>

**Step 2:** On the Data Connections page, click the **New Connection** button. 

![](/images/L-Dev-CustAging/02.jpg)
<br>

**Step 3:** In the Connection Type field, verify that **Database** is selected. 

![](/images/L-Dev-CustAging/03.jpg)
<br>

**Step 4:** The Connection Details page needs to contain the following information for the new connection: Type **NorthwindExampleDB_MyName** in Connection Name, but include your own name in the suffix. Each connection name must be unique. For the connection string, type **Server=myServerAddress;Database=myDataBase;Trusted_Connection=True;**. This example is using Windows authentication, so username and password are not required. Make sure the server name and database name match the ones you are using for this walkthrough.

![](/images/L-Dev-CustAging/04.jpg)
<br>
  
**Step 5:** In the Description field, include details about how the data connection will be used. 

![](/images/L-Dev-CustAging/05.jpg)
<br>

**Step 6:** Click the Save button to create the new data connection.

![](/images/L-Dev-CustAging/06.jpg)
<br>

The Database Data Connection is now ready to be used in a Data Portal. You should always test a new connection with your security context. Follow the steps in the [ Data Connections ](/wPortal/Data-Connections.html) walkthrough to test your connection string. 

### Setting up the Data Portal

**Step 1:** To add a new data portal, return to [ https://portal.gointerject.com  ](https://portal.gointerject.com) and select Data Portals from the sidebar menu. 

![](/images/L-Dev-CustAging/07.jpg)
<br>

**Step 2:** Select New Data Portal. 

![](/images/L-Dev-CustAging/08.jpg)
<br>

**Step 3:** Type **NorthwindCustomersDropdown_MyName** for the Data Portal Code. Since this field must be unique, add your name to the suffix. Select the connection that was made in the previous step, **NorthwindExampleDB_MyName**. Also enter a name for the stored procedure **\[demo\].\[Northwind_CustomerDropdown\]**, which will be created later. 

![](/images/L-Dev-Dropdowns/01.png)
<br>

**Step 4:** Click **Create Data Portal** to save the new data portal. Additional options for adding parameters will show after selecting the Create Data Portal button. 

![](/images/L-Dev-Dropdowns/02.png)
<br>

**Step 5:** To add your first formula parameter, click **Click here to add a Formula Parameter**. For this parameter, enter **Filter** for Name, **varchar** for Type, and **input** for Direction to input, as shown below. 

![](/images/L-Dev-Dropdowns/03.png)

<br>

### Creating the Stored Procedure

**Step 1:** Create a stored procedure called [demo].[Northwind_CustomerDropdown] using the following code example. 

<button class = "collapsible"> \[demo\].\[Northwind_CustomerDropdown\] </button>

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

```

</div>

**Step 2:** Stored procedures are natively supported by INTERJECT. There are a few key areas to note in the code example that help illustrate INTERJECT features. 

  * Parameters: The parameters included in the stored procedure are the same as those added to the Data Portal in a previous walkthrough. On each request, INTERJECT passes the Formula Parameters values from the spreadsheet configuration to the stored procedure along with System Parameters. Output parameters that can populate values in the spreadsheet are supported, but they are not included in this example. In this case, there is only one formula parameter.

![](/images/L-Create-Dropdowns/01.png)
<br>

  * Select statements: Returning data to INTERJECT uses a select statement, as shown below. More than one can be returned at a time to reduce the connections needed to fully populate a complex report. There are two select statements in this example. 

![](/images/L-Create-Dropdowns/02.png)
<br>

**Step 3:** It is important to test the stored procedure in the database before testing through the INTERJECT platform. The example code includes a test SQL statement that can be executed in a new query, as shown below. Be sure to change the procedure name to match your own. 


<button class="collapsible">Example Test Script</button>
<div markdown="1" class="panel">

```sql
	EXEC [demo].[Northwind_CustomerDropdown]
		@Filter = 'Market'
```

</div>

When executed, you should see the following result sets. Notice there are two different result sets. Each of them returns only values that contained the word **Market**

![](/images/L-Create-Dropdowns/03.png)
<br>
