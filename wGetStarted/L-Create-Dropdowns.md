---
title: "Lab Create Parameter Dropdowns"
layout: custom
keywords: [jDropdown, function]
description: The jDropdown formula is used for filtering on multiple parameters at once.
---

### Overview

The jDropdown formula helps developers simplify the use of parameters in a data pull or save. It can reduce the rows of data in a report, speeding the report process, sparing server resources, and pulling data more efficiently. 

### Creating the Stored Procedure

A dropdown formula often requires a separate stored procedure from the one used in the pull or save. This stored procedure is designed to filter down on the specific options for a parameter.


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

**Step 4:** The Connection Details page needs to contain the following information for the new connection: Type **NorthwindExampleDB_MyName** in Connection Name, but include your own name in the suffix. Each connection name must be unique. For the connection string, type **Server=myServerAddress;Database=myDataBase;Trusted_Connection=True;**. You are using Windows authentication, so username and password are not required. Replace the server name and database name to match the one you are using for this walkthrough. 

![](/images/L-Dev-CustAging/04.jpg)
<br>
  
**Step 5:** In the Description field, include details about how the data connection will be used. 

![](/images/L-Dev-CustAging/05.jpg)
<br>

**Step 6:** Click the Save button to create the new data connection. 

![](/images/L-Dev-CustAging/06.jpg)
<br>

The Database Data Connection is now ready to be used in a Data Portal. You should always test a new connection with your security context. Follow the steps in [ Data Connections ](/wPortal/Data-Connections.html) to test your connection string. 

### Setting up the Data Portal

**Step 1:** To add a new data portal, return to [ https://portal.gointerject.com  ](https://portal.gointerject.com) and select Data Portals from the sidebar menu. 

![](/images/L-Dev-CustAging/07.jpg)
<br>

**Step 2:** Select New Data Portal 

![](/images/L-Dev-CustAging/08.jpg)
<br>

**Step 3:** Type **NorthwindCustomersDropdown_MyName** for the Data Portal Code. Since this field must be unique, add your name to the suffix. Select the connection that was made in the previous step, **NorthwindExampleDB_MyName**. Also enter a name for the stored procedure **\[demo\].\[Northwind_CustomerDropdown\]**, which will be created later. 

![](/images/L-Create-Dropdowns/04.png)
<br>

**Step 4:** Click **Create Data Portal** to save the new data portal. Additional options will show after selecting the Create Data Portal button for adding parameters. 

![](/images/L-Create-Dropdowns/05.png)
<br>

**Step 5:** To add your first formula parameter, click **Click here to add a Formula Parameter**. For this parameter, enter **Filter** for Name, **varchar** for Type, and **input** for Direction to input, as shown below. 

![](/images/L-Create-Dropdowns/06.png)

<br>

### Creating the Formula

**Step 1:** Open the report **INTERJECT Customer Collections** under the INTERJECT Demos in the [ Report Library ](/wAbout/Report-Library-Basics.html). 

![](/images/Walkthrough-CustAging/01.png)

This will bring up the Customer Aging Summary. 

![](/images/Walkthrough-CustAging/02.png)

**Step 2:** Next, unfreeze panes by going into [ Quick Tools ](/wPortal/INTERJECT-Ribbon-Menu-Items.html) and select **Freeze/Unfreeze Panes**.

![](/images/L-Create-Dropdowns/07.png)
<br>

**Step 3:** Now create a new report formula. In cell C4 type [ **=jDropdown()** ](/wIndex/jDropdown.html). 

![](/images/L-Create-Dropdowns/08.png)
<br>

**Step 4:** Now select the **DataPortal** argument section and type **"NorthwindCustomersDropdown_MyName"**.

![](/images/L-Create-Dropdowns/09.png)
<br>

**Step 5:** For this example, there are no parameters. Select **MultiSelect** and type **FALSE**. Then, in **Target Cell**, type **C17**. 

![](/images/L-Create-Dropdowns/10.png)
<br>

**Step 6:** Scroll down to **Value Column Name** and **Display Column Name** and input **CompanyName** and **DisplayText** respectively.

![](/images/L-Create-Dropdowns/11.png)
<br>

**Step 7:** Scroll to the bottom of the function wizard and select the **Instruction Text** argument. Type **Select a Customer**. Then click **OK** to confirm the changes.

![](/images/L-Create-Dropdowns/12.png)
<br>

**Step 8:** Right click cell B17 where the text **Company Name** is located. Then select **Hyperlink** to create a hyperlink.

![](/images/L-Create-Dropdowns/13.png)
<br>

**Step 9:** Click on **Place in This Document** and point the **Cell Reference** to the [jDropdown()](/wIndex/jDropdown.html). In this case, it is in cell **F7**.

![](/images/L-Create-Dropdowns/14.png)
<br>

**Step 10:** Select **ScreenTip**. Then, in the textbox, type **Interject Dropdown**. Select **OK** in both open windows to save the hyperlink.

![](/images/L-Create-Dropdowns/15.png)
<br>

**Step 11:** Now select the hyperlink you just made and type **Market** into the search options. Notice that there are 4 options. Select **BOTTM - Bottom-Dollar Markets**.

![](/images/L-Create-Dropdowns/16.png)
<br>

**Step 12:** Now that a Company has been selected, **Pull** the report.

![](/images/L-Create-Dropdowns/17.png)
<br>

**Step 13:** The pull will only return the **Bottom-Dollar Markets** data.

![](/images/L-Create-Dropdowns/18.png)
<br>