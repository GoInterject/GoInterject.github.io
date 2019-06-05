---
title: "Lab Developer: jDropdown Stored Procedures"
layout: custom
keywords: [jDropdown, function]
description: Walks through how to create the stored procedures for the jDropdowns built in the customer aging create report
---

## Overview

This lab walks you through how to build the stored procedure for the jDropdowns built in the [Customer Aging report](/wGetStarted/L-Create-Dropdowns.html). It is required that you have access to build stored procedures in your database to complete this lab.

### Creating the Stored Procedure

A dropdown formula often requires a seperate stored procedure from the one used in the pull or save. This stored procedure is designed to filter down on the specific options for a parameter.


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
