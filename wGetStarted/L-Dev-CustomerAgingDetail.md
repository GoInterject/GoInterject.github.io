---
title: "Lab Dev: Customer Aging Detail"
layout: custom
keywords: [Customer Aging Detail, example, walkthrough, SQL, dataportal, server connection]
description: In this example, you will learn to create a third report, Customer Aging Detail, that will be drilled to from the Customer Aging Report. This report shows a customer's outstanding balance by individual invoice.
---
* * *

##  **Overview**

In this example, you will learn to create a third report, Customer Aging Detail, that will be drilled to from the Customer Aging Report. This report shows a customer's outstanding balance by individual invoice. The Aging Detail is a more complex report than shown in the earlier lab [ Lab Developer: Customer Orders ](/wGetStarted/L-Dev-CustomerOrders.html) , because it leverages two report formulas to create a report with subtotals. You should have already seen the Customer Aging Detail report while reviewing the business use case in the [ **Customer Aging in Real-World Walkthroughs** ](/wAbout/Customer-Aging.html). 

###  Verifying the Data Connection 

Because this report uses the same database as [ Lab Developer: Customer Aging Detail ](/wGetStarted/L-Dev-CustomerAgingDetail.html) , you do not need to create another data connection. The same connection can be used for this report. The connection created in the previous example was named **NorthwindExampleDB_MyName** and your own data connection likely had your name in the suffix. 

###  Copying and Modifying the Data Portals 

For this report you are going to use two data portals. The first will be the same data portal used in a previous example called **NorthwindCustomers_MyName** . You created your own with your name in the suffix. The below steps will create a copy of this data portal for the customer invoice detail since it saves a little time. 

**Step 1:** Navigate to the data portal, **NorthwindCustomers_MyName** , and click the green clone button on the top right of the page. 

![](/images/L-Dev-CustAgingDetail/01.png)
<br>
  


**Step 2:** A new data portal named, **NorthwindCustomers_MyName_copy** , generates. Change this data portal name to **NorthwindCustomerInvoices_MyName** . Since each Data Portal Code must be unique, you should add your name to the suffix. 

![](/images/L-Dev-CustAgingDetail/02.jpg)
<br>
  


**Step 3:** Change the procedure name to run **[demo].[Northwind_Invoices_Pull_MyName]** , which you will create shortly. As in the last step, replace **_MyName** with your own name. 

![](/images/L-Dev-CustAgingDetail/03.jpg)
<br>
  


**Step 4:** You will use the existing Formula Parameters but for this example you need to add more more. Select **Click here to add a Formula Parameter** . Enter **IncludePaid** for Name, **varchar** for Type, and **input** for direction. Click the **More** button. 

![](/images/L-Dev-CustAgingDetail/04.jpg)
<br>
  


Enter **Include Paid** for Helper Name and enter **Include Invoices that have already been paid for by the customer** for Comments. Click the Save icon. 

![](/images/L-Dev-CustAgingDetail/05.jpg)
<br>
  


**Step 5:** Click the trash can icon on the far right of the Interject_LocalTimeZoneOffset to delete it. You are going to a use a different System Parameter for this data portal to illustrate a new System Parameter that has not been presented in previous examples. 

![](/images/L-Dev-CustAgingDetail/06.jpg)
<br>
  


**Step 6:** Click the drop-down on the **Interject_NTLogin** and change it **Interject_RequestContext** . This System Parameter provides all request and user context that is available in a single XML string. It is best practices to use **Interject_RequestContext** as the only System Parameter since it reduces work over the long run. Since this parameter includes all system parameter information, the data portal configuration does not need to be changed if the stored procedure needs to reference additional context. Click Save. 

![](/images/L-Dev-CustAgingDetail/07.jpg)
<br>


###  Creating the Stored Procedure 

Stored procedures or data APIs serve as a middle tier for an INTERJECT report. In this example, you are using a stored procedure. INTERJECT can retrieve one or more result sets from the stored procedure into the spreadsheet report. 

The INTERJECT Website Portal allows you to create and manage the data portals and reference stored procedures you create. Data portals are stored locally in your Excel session when you log into INTERJECT. When requesting data, INTERJECT creates a point-to-point connection with the intended data source. 

The steps below assume you are proficient with SQL Management Studio for Microsoft SQL Server and in creating stored procedures. If you need additional training in this area, please contact us at [ info@gointerject.com ](mailto:info@gointerject.com) . 

**Step 1:** Create a stored procedure called [demo].[Northwind_Invoices_Pull_MyName] using the following example code. Please use your name in the suffix of the stored procedure name. 

[Download Script][1]

It is important to test the stored procedure in the database before testing it through the INTERJECT platform. Using Interject_RequestContext requires the test scripts to be much longer than in the previous steps. To help with this extra text INTERJECT will create the test code for you using the current users context. 

**Step 2:** First you must select a report formula that uses the data portal that is mapped to the stored procedure you want to test. You can quickly make a report formula and delete it since you are not creating the spreadsheet report yet. In a spreadsheet tab, in any cell, type **=ReportVariable("NorthwindCustomerInvoices",A42:A304,2:2,16:16,Param(H36,H37,H38,""))** but replace the data portal name with the name you created for your own example. Make sure the the cell with the ReportRange() formula is selected. 

![](/images/L-Dev-CustAgingDetail/08.png)
<br>
  


**Step 3:** Next, click **Advanced Menu** in the INTERJECT Ribbon. 

![](/images/L-Dev-CustAgingDetail/09.png)
<br>

This button is a toggle, so if it is currently showing **Simple Menu** the advanced menu is already showing. 

![](/images/L-Dev-CustAgingDetail/10.png)
<br>
  
**Step 4:** Click the **System** dropdown and select **View SQL Test for ActiveCell** . A window will pop up providing the developer with the SQL template used to create the stored procedure. 

![](/images/L-Dev-CustAgingDetail/11.png)
<br>

**Step 5:** Copy and paste the template code into the development environment, SQL Server Management Studio.   
The full text code is shown below. 

[Download Script][2]

**Step 7:** When this code is executed, it returns the following result set. 

![](/images/L-Dev-CustAgingDetail/12.png)
<br>

###  Create The Report 

At this point you, have a tested a new stored procedure that uses parameters to filter the results. You set up an INTERJECT data connection to go to your example database and you added another INTERJECT data portal to use that connection, which is mapped to the stored procedure that you just created. So now you are ready to build the spreadsheet report using two data portals. 

The steps for building the spreadsheet report are in the lab [ Customer Aging Detail ](/wGetStarted/L3.4-Customer-Aging-Detail.html) . You have likely completed this in earlier training sessions. Repeat the instructions with your newly created data portals discussed in this topic. When you are done, your report should resemble the screenshot below. 

![](/images/L-Dev-CustAgingDetail/13.png)
<br>

###  Creating a New Data Portal With Multiple Recordsets 

You just created a report that used ReportRange() to list all the customers with subtotaled regions. Then ReportVariable() was used to populate the invoices for each customer region. Two separate data portals were used and two connections were made to the database. 

To illustrate the multiple recordset feature of INTERJECT, you can take this one step further. You can copy the second data portal and stored procedure and modify it so that it returns both recordsets. In this approach, you make only one connection to the database, which is more efficient. And this process requires one less data portal and stored procedure to create. 

Multiple recordsets are a very efficient report approach when your data is not a simple list. In this example the feature will work as follows. On the first data request two recordsets are retrieved by INTERJECT. ReportRange() uses the customer summary list recordset but both recordsets temporarily remain in memory until all report formulas are completed. This allows the ReportVariable() to access the second recordset for populating the details in the same report run. The following steps will help you create this change yourself. 

**Step 1:** Navigate to the data portal that you just created , similar to **NorthwindCustomerInvoices_MyName** , and click the green clone button on the top right of the page. 

![](/images/L-Dev-CustAgingDetail/14.jpg)
<br>
  


**Step 2:** A new data portal named, **NorthwindCustomerInvoices_MyName_copy** , generates. Change this data portal name to **NorthwindMultiRecord_MyName** . You can add your name to the suffix, because each data portal code must be unique. 

![](/images/L-Dev-CustAgingDetail/15.jpg)
<br>
  


**Step 3:** Change the procedure name to run **[demo].[Northwind_CustomerInvoices_Pull_MyName]** but use your own name as the suffice. You will create this stored procedure shortly. Everything else in the cloned data portal remains the same. 

![](/images/L-Dev-CustAgingDetail/16.jpg)
<br>

###  Updating the Stored Procedure for 2 Recordsets 

**Step 1:** In SQL Server Management Studio, open the stored procedure used in the report that pulled the invoice detail. The stored procedure name should be similar to [demo].[Northwind_Invoices_Pull_MyName]. 

![](/images/L-Dev-CustAgingDetail/17.png)
<br>

**Step 2:** Change the name of the stored procedure to [demo].[Northwind_CustomerInvoices_MyName], using your own name as the suffix. By using ‘Create procedure’ as shown below, the stored procedure will be copied to the new name when executed. 

![](/images/L-Dev-CustAgingDetail/18.png)
<br>

**Step 3:** Change the **Create procedure** back to **Alter procedure** and continue with editing the new procedure. 

**Step 4:** You have to make a few changes to the stored procedure so the summary record set showing a list of customers can be provided. First add **into #InvoiceDetail** as shown below. It will put the invoice detail in a temporary table to be used later in the stored procedure. 

![](/images/L-Dev-CustAgingDetail/19.png)
<br>

**Step 5:** After the SQL statement, add **Select * from #InvoiceDetail** . Then order by the CustomerID. This step returns the invoice detail as the first recordset from the stored procedure. 

**Step 6:** Next you must use the detail to generate a customer summary list. The below code should be copied into the bottom of the stored procedure. This code simply creates a distinct list of all the customers include in the invoice detail and orders by the customer name. 

Steps 5 and 6 should look like below: 

```SQL
    -- Select all detail from the dataset created above
    SELECT * FROM #InvoiceDetail
    ORDER BY [CustomerID]
    
    -- Select unique customers to form a summary list of all of the customers.
    SELECT DISTINCT 
    	 [CustomerID]
    	,[CompanyName]
    	,[ContactName]
    	,[ContactTitle]
    	,[Country] 
    FROM #InvoiceDetail
    ORDER BY CustomerID
```
**Step 7:** The changes to the stored procedure are complet. It is important to test the stored procedure in the database before testing it through the INTERJECT platform. You can use the same test script used earlier in this topic. Your test code should look similar to the SQL below. 

[Download Script][3]

When this code is executed, it should return two recordsets as shown below. 

![](/images/L-Dev-CustAgingDetail/20.png)
<br>

###  Updating the Report for 2 Recordsets 

You are ready to modify the report to use your new data portal. The changes are simple since you only need to use a new function, jDataPortal(), to specify the data portal recordset number for each report function. 

**Step 1:** In the **Customer Aging Detail** report that you just completed, change the **=ReportRange()** function by replacing the previous data portal with the new one. However, you will be encasing the new data portal inside a jDataPortal() function. So **=ReportRange(“oldDataPortalCode”,..** becomes **=ReportRange(jDataPortal(“NorthwindMultiRecord_MyName”,2),...** The end result should look like the below screenshot for ReportRange(). 

![](/images/L-Dev-CustAgingDetail/21.png)
<br>

The second parameter, DataResultNumber, indicates which recordset this report function will use. Using **2** causes the ReportRange() function to grab the second recordset that is a simple list of customers. 

**Step 4:** Now change the **=ReportVariable()** function by replacing the previous data portal with the new one. Again you must encase the new data portal inside a jDataPortal() function. So **=ReportVariable(“oldDataPortalCode”,..** becomes **=ReportVariable(jDataPortal(“NorthwindMultiRecord_MyName”,1),...** In this step you are using **1** so the first record set is used in this report function. The end result should look like the below screenshot for ReportVariable(). 

![](/images/L-Dev-CustAgingDetail/22.png)
<br>

**Step 5:** Once the report formulas are edited, you can re-pull the data in the report and the results should be the same as when it used two data portals. 

![](/images/L-Dev-CustAgingDetail/23.png)
<br>


[1]:/images/L-Dev-CustAgingDetail/S1.sql
[2]:/images/L-Dev-CustAgingDetail/S2.sql
[3]:/images/L-Dev-CustAgingDetail/S3.sql