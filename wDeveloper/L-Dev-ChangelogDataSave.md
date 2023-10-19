---
title: "Develop: Change Log Data Save"
layout: custom
keywords: [developer, example, walkthrough, SQL, SSMS, Data Portal, data connection, data save, history]
description: In this example you will modify the simple data save using the Customer Aging Detail report and the Northwind Customers data source to add or delete a customer.
---
* * *

## Overview

In this example you will modify the previous [Insert &amp; Delete Data Save](/wDeveloper/L-Dev-InsertDeleteDataSave.html), which was set up to insert and delete customers. In this Change Log Data Save, you will modify the Stored Procedure (SP) again to include a change log.

A change log is basically an additional table in the database that will record all the changes that take place to the targeted table. This history table keeps track of what records and fields were changed, what type of change took place (e.g. update, insert, deleted, added), who performed the change and the date and time it took place. It also keeps track of the old values that were changed so you can compare the old with the new values.

This walkthrough involves 5 main steps:

1. [Set up a Data Connection](#setting-up-the-data-connection) ([completed already](/wGetStarted/L-Dev-CustomerAging.html#setting-up-the-data-connection))
2. [Set up a Data Portal](#setting-up-the-data-portal)
3. [Setting up the report to handle the save](#setting-up-the-report)
4. [Set up the Stored Procedure (SP) to handle the save](#setting-up-the-stored-procedure)
5. [Test the Stored Procedure &amp; ReportSave](#testing-the-stored-procedure)

<blockquote class=highlight_note>
<b>Note:</b> This example uses Microsoft's Northwind Database. You can download this database <a href="https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/downloading-sample-databases">here</a> or you can use this example as a guide for your own data source.
</blockquote>

## Setting up the Data Connection

For the Data Connection for this example, you will use the connection previously set up [here](/wGetStarted/L-Dev-CustomerAging.html#setting-up-the-data-connection).

## Setting up the Data Portal

**Step 1:** Navigate to [ https://portal.gointerject.com ](https://portal.gointerject.com) and [ log in ](/wPortal/Logging-In-to-Website-Portal.html). Click on **Data Portals** on the left side bar and then the **NEW DATA PORTAL** button.

![](/images/L-Dev-ChangelogDataSave/NewDataPortal.png)
<br>

**Step 2:** Enter the following details on setting up the new data portal and click "**CREATE DATA PORTAL**".

* **Data Portal Code:** NorthwindChangelogDataSave
* **Description:** Data portal for changelog data save
* **Category:** Demo
* **Connection:** NorthwindExampleDB_MyName (replace "MyName" with your name)
* **Command Type:** Stored Procedure
* **Stored Procedure/Command:** NorthwindChangelogDataSaveSP

**Note:** You will create the "NorthwindChangelogDataSaveSP" Stored Procedure [later](#setting-up-the-stored-procedure).
<br>

![](/images/L-Dev-ChangelogDataSave/DataPortalDetails.png)
<br>

**Step 3:** After creating the data portal, scroll down and click **Click here to add a System Parameter** and ensure the **Interject_RequestContext** parameter is set.

![](/images/L-Dev-ChangelogDataSave/AddSystemParameter.png)
<br>

The System Parameter [Interject_RequestContext](/wIndex/Request-Context-Parse.html) will transfer contextual data to the Stored Procedure you will set up later. In this example you will not need this info but it is a good practice to set this parameter for all your Stored Procedures.

## Setting up the Report

Begin by opening up the report that was completed in the [previous data save](/wDeveloper/L-Dev-InsertDeleteDataSave.html#setting-up-the-report). 

The only thing that needs to be changed in this report is the name of the Data Portal in the ReportSave formula:

![](/images/L-Dev-ChangelogDataSave/ChangeReportSaveFunction.png)
<br>

## Setting up the Stored Procedure

Next you will created a new Stored Procedure that builds from the [previous save](/wDeveloper/L-Dev-InsertDeleteDataSave.html#modifying-the-stored-procedure). To make this easier, simply copy the SP into a new query, change the command to "CREATE OR ALTER PROC NorthwindChangelogDataSaveSP" and execute it to save it. Then you can begin making modifications to it. For your convenience, the SP is posted here.

**Note:** The code for testing the SP has been removed. It will be handled [later](#testing-the-stored-procedure):

<button class = "collapsible"> NorthwindInsertDeleteDataSaveSP </button>
<div markdown="1" class="panel">

```sql

```
</div>

Execute the above code to save the Store Procedure.

## Modifying the Stored Procedure

The following walks you through the major sections of the code with instructions on the changes. Additions are marked in yellow.

### Current Date and Time

### ChangeLog

### Old Values

### IsDeleted

### Added Back

### Merge Update

### Merge Insert

### Merge Output

### Update ChangeLog

### Update History Table

### Final Stored Procedure

Now that the Stored Procedure is finished, execute it to save it.

The following is the finished SP:

<button class = "collapsible"> NorthwindInsertDeleteDataSaveSP </button>
<div markdown="1" class="panel">

```sql

```
</div>

## Testing the Stored Procedure

Interject provides a convenient way to get SQL code that will test your SP right from within the Excel report. First select the cell in the Excel report containing the ReportSave function. Then on the [Advanced Menu](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#overview), click on "View SQL Test For ActiveCell" on the "System" dropdown:

![](/images/L-Dev-InsertDeleteDataSave/ViewSQLTestClick.png)
<br>

Copy the test code to the clipboard:

![](/images/L-Dev-InsertDeleteDataSave/CopyTestCode.png)
<br>

Paste the code into a new query and be sure to add the "@TestMode = 1" parameter to print out additional information about the SP process:

![](/images/L-Dev-InsertDeleteDataSave/PasteTestCode.png)
<br>

Make some changes to the data:

![](/images/L-Dev-InsertDeleteDataSave/ExecuteTestCode.png)
<br>

After execution, you should see the messages showing what was changed:

![](/images/L-Dev-InsertDeleteDataSave/TestCodeExecuted.png)
<br>

## Testing the ReportSave

The only thing left to do is test the SP by running the ReportSave function within the Excel report.

Next make some changes and run the Report Save:

![](/images/L-Dev-InsertDeleteDataSave/TestingTheReportChanges.png)
<br>

Notice the results!:

![](/images/L-Dev-InsertDeleteDataSave/TestingTheReportResults.png)
<br>

