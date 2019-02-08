---
title: "Lab Developer: Customer Credit Save"
layout: custom
keywords: [save, example, walkthrough, customer aging,]
description:
---
##  **Overview:**

This section will detail a full review of how the INTERJECT save feature works. Using the Customer Credits example, it will show how to design three user input fields into an existing report. The INTERJECT platform will assist in creating a stored procedure that can be used in SQL Server to help facilitate the process.  Other database engines or API methods can be used for the save process as well, but for simplicity you are focusing on SQL Server and a database stored procedure as the data source.  You will be using the Customer Credits report, as you have already become familiar with its [ business use case ](/wAbout/Customer-Aging.html). 

###  Setting up the Data Portals: 

This report uses the same database as  **Dev: Customer Aging** and other reports, you do not need to create another data connection. Use the same connection as in previous labs. The  Data Portals for saving data are very similar to their Pull counterparts. 

**Step 1:** Navigate to the INTERJECT Portal Website at:    
[ https://portal.gointerject.com/  ](https://portal.gointerject.com/) then select  **Data Portals** in the sidebar menu. 

![](/images/L-Dev-CustAgingSave/01.jpg)
<br>
  


**Step 2:** Click the  **New Data Portal** button. 

![](/images/L-Dev-CustAgingSave/02.jpg)
<br>
  


**Step 3:** In the  **Data Portal Code** field enter  **NorthwindCreditSave_MyName**. 

![](/images/L-Dev-CustAgingSave/03.jpg)
<br>
  


**Step 4:** In the description, you will fill out a short detail saying what this data portal will be used for. In this case, it will say  **Simple Data Save** . 

![](/images/L-Dev-CustAgingSave/04.jpg)
<br>
  


**Step 5:** In the  **Category** field, label the type of data portal connection that this data portal will be. In this case it will be a  **Demo** . 

![](/images/L-Dev-CustAgingSave/05.jpg)
<br>
  


**Step 6:** In the connection drop down menu you will choose the data connection  **NorthwindExampleDB_MyName** that you have already created. 

![](/images/L-Dev-CustAgingSave/06.jpg)
<br>
  


**Step 7:** For the  **Command Type** you will use the stored procedure option, and in  **Stored Procedure / Command** input a name for the stored procedure you will create later. In this case you use  **[demo].[Northwind_Credit_Save_MyName]** .  Then click  **create data portal.**

![](/images/L-Dev-CustAgingSave/07.jpg)
<br>

###  Setting up Formula Parameters: 

For this Data Portal, there are no formula parameters to be used. 

###  Setting up System Parameters: 

System Parameters are similar to Formula Parameters, but the names are reserved. To review the System parameters and their purposes, go to the System Parameters section of the [ Data Portal ](/wPortal/Data-Portals.html) page. 

In this example you are going to use  **Interject_ReturnError** and  **Interject_RequestContext** . 

**Step 1:** To add the first system parameter, click the  **Click here to** **add a System Parameter** button. Then select  **Interject_RequestContext** for the name and click **save** . 

![](/images/L-Dev-CustAgingSave/08.jpg)
<br>
  


**Step 2:** To add a new system parameter, first click the  **Click here to add a System Parameter** button. Then select  **Interject_ReturnError** for the name of our second parameter. Then click **save** . 

![](/images/L-Dev-CustAgingSave/09.jpg)
<br>
  


###  Creating the Report: 

**Step 1:** Unfreeze panes. 

![](/images/L-Dev-CustAgingSave/10.jpg)
<br>
  


**Step 2:** First, **insert** a row above **row 7** select cell  **C7** and input  **=ReportSave()** . Then, click the  **fx** button to open the report wizard. 

![](/images/L-Dev-CustAgingSave/11.jpg)
<br>
  


**Step 3:** In the  **DataPortal** section, input the dataportal name of the dataportal you just created. It was recommended that you name it  **NorthwindCreditSave_MyName.**

![](/images/L-Dev-CustAgingSave/12.jpg)
<br>
  


**Step 4:** The RowDefRange is for your ID row. In this case, input  **B23:B24.**

![](/images/L-Dev-CustAgingSave/13.jpg)
<br>
  


**Step 5:** It is best practice to separate the column definitions. To do so, copy rows 1 and 2, then right click row 3 and insert the copied rows. In cell  **A3** change the value to  **Column Definitions - Save.**

![](/images/L-Dev-CustAgingSave/14.jpg)
<br>
  


**Step 6:** Now delete the values in the range  **C4:G4** so that only the save-optional columns that are remaining. In this case, leave only **CustomerID,** **Credit Limit, AccountFreeze,** and  **AccountNotes**

![](/images/L-Dev-CustAgingSave/15.jpg)
<br>
  


**Step 7:** Saves are often two way processes. They push data back to the database but can also pull in feedback responses and new data. To create the results range and retrieve data, to do this, add  **MessageToUser** to cell  **N6.**

![](/images/L-Dev-CustAgingSave/16.jpg)
<br>
  


**Step 8:** Also make sure to put a  **[Clear]** in cell  **N2,** but not in  **N4,** so that the data can be cleared on pulls. 

![](/images/L-Dev-CustAgingSave/17.jpg)
<br>
  


**Step 9:** Now select the  **ReportSave()** function again and select  **fx.**

![](/images/L-Dev-CustAgingSave/18.jpg)
<br>
  


**Step 10:** In the  **ColDef,** input  **4:4** and  **6:6** in the  **ResultsRange** . The save will not use parameters, so leave it blank. 

![](/images/L-Dev-CustAgingSave/19.jpg)
<br>

###  Creating the Stored Procedure 

**Step 1:** First, select the  **Pull** button and pull the data into the spreadsheet. 


**Step 2:** In the excel sheet, click the cell with the ReportSave formula. Then  click  **Advanced Menu** in the INTERJECT Ribbon. This button is a toggle, so if it is currently showing  **Simple Menu** do not click it. 


**Step 3:** Then, click the  **System** dropdown and select  **View SQL Template for ActiveCell** . Make sure you have the ReportSave cell selected. 


A window will pop up providing the developer with the SQL template used to create the stored procedure. 

  


Copy and paste the template code into the MSSQL Server from your Excel sheet. This template is a helpful starting point that includes the Data Portal parameters and pre-formatted test code, but more work is needed to construct the required data save. Here is an example test code to compare with, but yours will be different. Do not copy this code and use it for your report as it will not work. 

[Download Script][1]

    
After getting the template, it is important to modify the procedure for what is needed. For example, the parameters are automatically set to max, so an easy change would be to set them to more realistic character lengths. 

[Download Script][2]

###  Testing the Stored Procedure 

For quick testing, click on the  **View SQL Test** and copy the test code to the development area. For more information, go to the [ common troubleshooting page ](/wGetStarted/Troubleshooting-Reports.html). 

![](/images/L-Dev-CustAgingSave/20.jpg)
<br>
  


Now that you have modified the stored procedure, go back to excel and see if the data gets correctly saved. 

![](/images/L-Dev-CustAgingSave/21.jpg)
<br>
  


After the save, there will be a return message telling what was changed based on the row. 

![](/images/L-Dev-CustAgingSave/22.jpg)
<br>

[1]:{{ site.url }}/images/L-Dev-CustAgingSave/S1.sql
[2]:{{ site.url }}/images/L-Dev-CustAgingSave/S2.sql