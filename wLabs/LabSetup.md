---
title: Manual Setup for the Lab Guide
filename: "LabSetup.md"
layout: custom
keywords: [lab, guide, manual setup, start, Northwind, database, FinCube, data cells]
headings: ["Overview", "Interject Data Report Flow", "Manual Setup", "Step 1: Setting up the Database", "Step 2: Setting up the Data Connection", "Step 3: Setting up the Data Portals", "Step 4: Setting up FinCube", "Setting up the FinCube Data Connection", "Setting up the FinCube Data Portal", "Setting up the FinCube Data Cells Data Portals", "Step 5: The Report Files", "Step 6: Renaming the Data Portals"]
links: ["/wLabs/lab.html", "/wFunctions/Excel-Function-Index.html", "/wPortal/Data-Portals.html", "/wPortal/The-INTERJECT-Website-Portal.html", "#step-1-setting-up-the-database", "#step-2-setting-up-the-data-connection", "#step-3-setting-up-the-data-portals", "#step-4-setting-up-fincube", "#step-5-the-report-files", "#step-6-renaming-the-data-portals", "https://www.microsoft.com/en-us/sql-server/sql-server-downloads", "https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/downloading-sample-databases", "https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-2017", "https://portal.gointerject.com/", "/wPortal/The-INTERJECT-Website-Portal.html", "/wPortal/L-Database-Connection.html", "/wPortal/Data-Portals.html", "/wIndex/FinCubeTheFinancialCube.html", "/wAbout/Tabular-vs-Data-Cells.html", "/wFunctions/Data-Cell-Functions.html"]
image_dir: "LabSetupManual"
images: [
	{file: "FlowChart", type: "png", site: "External", cat: "Flow Chart", sub: "Data Report Flow", report: "", ribbon: "", config: ""}, 
	{file: "DataConnection", type: "png", site: "Portal", cat: "Data Connections", sub: "Details", report: "", ribbon: "", config: ""}, 
	{file: "FinCubeDataConnection", type: "png", site: "Portal", cat: "Data Connections", sub: "Details", report: "", ribbon: "", config: ""}, 
	{file: "FinCubeDataPortal", type: "png", site: "Portal", cat: "Data Portals", sub: "Details", report: "", ribbon: "", config: ""}, 
	{file: "ClientID", type: "png", site: "Add-in", cat: "About Interject", sub: "", report: "", ribbon: "", config: ""}
	]
description: This page details the necessary requirements and steps to set up a local environment that can accommodate a user following the Lab Guide.
---
* * *

## Overview

The [Lab Guide](/wLabs/lab.html) provides a convenient way for users to become familiar with Interject. The Guide has several individual walkthroughs on how to create reports, modify reports, drill to data, and export reports. For those who want greater control and flexibility in making modifications to the Lab Guide, this page details how to setup the environment manually.

### Interject Data Report Flow

The reports in the Lab Guide contain [Interject report formulas](/wFunctions/Excel-Function-Index.html), each referencing a [Data Portal](/wPortal/Data-Portals.html) setup on the [Interject Portal Website](/wPortal/The-INTERJECT-Website-Portal.html). These Data Portals in turn reference a Data Connection and a Stored Procedure that point to a data source where the data will be pulled from. When the data source is a database, the entire flow can be conceptualized by the following diagram:

![](/images/LabSetupManual/FlowChart.png)
<br>

### Manual Setup

There are a number of steps necessary for manual setup:

* **[Step 1:](#step-1-setting-up-the-database)** Download the database and install locally
* **[Step 2:](#step-2-setting-up-the-data-connection)** Set up the Data Connections on the Interject Portal site
* **[Step 3:](#step-3-setting-up-the-data-portals)** Set up the Data Portals on the Interject Portal site
* **[Step 4:](#step-4-setting-up-fincube)** Set up the FinCube Portals
* **[Step 5:](#step-5-the-report-files)** Download the lab files
* **[Step 6:](#step-6-renaming-the-data-portals)** Change the Data Portal names in the files to match the ones manually set up

The following walks through the steps to set up a Lab environment locally.

### Step 1: Setting up the Database

The first step in manually setting up a Lab environment is to establish a database on a local system where the Lab Guide will be used. Interject's choice of database is [SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads){:target="_blank"}{:rel="noopener noreferrer"} as the Lab Guide relies on Microsoft's [Northwind Database](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/downloading-sample-databases){:target="_blank"}{:rel="noopener noreferrer"}.

The following is a minimalist script to recreate the database using SQL Server 2014 or greater:

[labs_db_script_sql_server_2014.sql][1]

[1]:{{ site.url }}/download/labs_db_script_sql_server_2014.sql

This script will have all the necessary tables, functions, procedures, schemas, and roles. You will need to first create the database of your choosing and then run this script inside that database. You may use [SSMS](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-2017){:target="_blank"}{:rel="noopener noreferrer"} or another editor of your choice.

### Step 2: Setting up the Data Connection

Navigate to the [Interject Portal site](https://portal.gointerject.com/) and log in. For a guide about how to use the Interject Portal site, see [here](/wPortal/The-INTERJECT-Website-Portal.html).

Set up a Data Connection that points to the database you set up. The following example uses a database called "Interject_Lab_DB":

* **Name:** Local_Lab_DataSource
* **Description:** This is the Data Connection to a local database set up for the Lab Guide
* **Connection Type:** Database
* **Connection String:** Data Source=(local);Initial Catalog=Interject_Lab_DB;Integrated Security=SSPI;

![](/images/LabSetupManual/DataConnection.png)
<br>

For detailed instructions on how to set up a Data Connection, see [Portal: Database Connection](/wPortal/L-Database-Connection.html).

### Step 3: Setting up the Data Portals

Now that you have a database and set up a Data Connection to it, you need to start adding Data Portals. For instructions on how to set up Data Portals, see [Data Portals](/wPortal/Data-Portals.html). Following is a list of the Data Portals and their Stored Procedures used in the Labs.

<blockquote class=highlight_note>
<b>Note:</b> The Data Type and Direction are automatically set when selecting a System Parameter.
</blockquote>
<br>

<button class="collapsible-parameter">**NorthwindCreditSave**<br>Stored Procedure: [demo].[Northwind_Credit_Save]</button>
<div markdown="1" class="panel-parameter">
<table>
<tbody>

<td class="pph"><b>Parameter</b></td>
<td class="pph"><b>Parameter Type</b></td>
<td class="pph"><b>Data Type</b></td>
<td class="pph"><b>Direction</b></td>

<tr>
<td>Interject_RequestContext</td>
<td>System Parameter</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Interject_ReturnError</td>
<td>System Parameter</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>

<button class="collapsible-parameter">**NorthwindCustomerAccountDetail**<br>Stored Procedure: [demo].[Northwind_CustomerAccountDetail_Pull]</button>
<div markdown="1" class="panel-parameter">
<table>
<tbody>

<td class="pph"><b>Parameter</b></td>
<td class="pph"><b>Parameter Type</b></td>
<td class="pph"><b>Data Type</b></td>
<td class="pph"><b>Direction</b></td>

<tr>
<td>CompanyName</td>
<td>Formula Parameter</td>
<td>nvarchar</td>
<td>input</td>
</tr>
<tr>
<td>ContactName</td>
<td>Formula Parameter</td>
<td>varchar</td>
<td>input</td>
</tr>
<tr>
<td>CustomerID</td>
<td>Formula Parameter</td>
<td>varchar</td>
<td>input</td>
</tr>
<tr>
<td>UnappliedOnly</td>
<td>Formula Parameter</td>
<td>varchar</td>
<td>input</td>
</tr>
<tr>
<td>BeginDate</td>
<td>Formula Parameter</td>
<td>varchar</td>
<td>input</td>
</tr>
<tr>
<td>EndDate</td>
<td>Formula Parameter</td>
<td>varchar</td>
<td>input</td>
</tr>
<tr>
<td>Interject_ReturnError</td>
<td>System Parameter</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Interject_RequestContext</td>
<td>System Parameter</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>


<button class="collapsible-parameter">**NorthwindCustomerInvoices**<br>Stored Procedure: [demo].[Northwind_Invoices_Pull]</button>
<div markdown="1" class="panel-parameter">
<table>
<tbody>

<td class="pph"><b>Parameter</b></td>
<td class="pph"><b>Parameter Type</b></td>
<td class="pph"><b>Data Type</b></td>
<td class="pph"><b>Direction</b></td>

<tr>
<td>CompanyName</td>
<td>Formula Parameter</td>
<td>nvarchar</td>
<td>input</td>
</tr>
<tr>
<td>ContactName</td>
<td>Formula Parameter</td>
<td>varchar</td>
<td>input</td>
</tr>
<tr>
<td>CustomerID</td>
<td>Formula Parameter</td>
<td>varchar</td>
<td>input</td>
</tr>
<tr>
<td>ShowExpectedDate</td>
<td>Formula Parameter</td>
<td>varchar</td>
<td>input</td>
</tr>
<tr>
<td>IncludePaid</td>
<td>Formula Parameter</td>
<td>varchar</td>
<td>input</td>
</tr>
<tr>
<td>Interject_RequestContext</td>
<td>System Parameter</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>

<button class="collapsible-parameter">**NorthwindCustomerOrder**<br>Stored Procedure: [demo].[Northwind_CustomerOrder_Pull]</button>
<div markdown="1" class="panel-parameter">
<table>
<tbody>

<td class="pph"><b>Parameter</b></td>
<td class="pph"><b>Parameter Type</b></td>
<td class="pph"><b>Data Type</b></td>
<td class="pph"><b>Direction</b></td>

<tr>
<td>OrderID</td>
<td>Formula Parameter</td>
<td>int</td>
<td>input</td>
</tr>
<tr>
<td>CustomerID</td>
<td>Formula Parameter</td>
<td>nvarchar</td>
<td>output</td>
</tr>
<tr>
<td>ContactName</td>
<td>Formula Parameter</td>
<td>nvarchar</td>
<td>output</td>
</tr>
<tr>
<td>CompanyName</td>
<td>Formula Parameter</td>
<td>nvarchar</td>
<td>output</td>
</tr>
<tr>
<td>ShipAddress</td>
<td>Formula Parameter</td>
<td>nvarchar</td>
<td>output</td>
</tr>
<tr>
<td>ShipCity</td>
<td>Formula Parameter</td>
<td>nvarchar</td>
<td>output</td>
</tr>
<tr>
<td>ShipPostalCode</td>
<td>Formula Parameter</td>
<td>nvarchar</td>
<td>output</td>
</tr>
<tr>
<td>ShipCountry</td>
<td>Formula Parameter</td>
<td>nvarchar</td>
<td>output</td>
</tr>
<tr>
<td>Phone</td>
<td>Formula Parameter</td>
<td>nvarchar</td>
<td>output</td>
</tr>
<tr>
<td>Fax</td>
<td>Formula Parameter</td>
<td>nvarchar</td>
<td>output</td>
</tr>
<tr>
<td>OrderDate</td>
<td>Formula Parameter</td>
<td>date</td>
<td>output</td>
</tr>
<tr>
<td>RequiredDate</td>
<td>Formula Parameter</td>
<td>date</td>
<td>output</td>
</tr>
<tr>
<td>ShippedDate</td>
<td>Formula Parameter</td>
<td>date</td>
<td>output</td>
</tr>
<tr>
<td>ShipVia</td>
<td>Formula Parameter</td>
<td>nvarchar</td>
<td>output</td>
</tr>
<tr>
<td>Freight</td>
<td>Formula Parameter</td>
<td>money</td>
<td>output</td>
</tr>
<tr>
<td>Interject_RequestContext</td>
<td>System Parameter</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Interject_ReturnError</td>
<td>System Parameter</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>

<button class="collapsible-parameter">**NorthwindCustomerOrders**<br>Stored Procedure: [demo].[Northwind_CustomerOrders_Pull]</button>
<div markdown="1" class="panel-parameter">
<table>
<tbody>

<td class="pph"><b>Parameter</b></td>
<td class="pph"><b>Parameter Type</b></td>
<td class="pph"><b>Data Type</b></td>
<td class="pph"><b>Direction</b></td>

<tr>
<td>CompanyName</td>
<td>Formula Parameter</td>
<td>nvarchar</td>
<td>input</td>
</tr>
<tr>
<td>ContactName</td>
<td>Formula Parameter</td>
<td>varchar</td>
<td>input</td>
</tr>
<tr>
<td>CustomerID</td>
<td>Formula Parameter</td>
<td>varchar</td>
<td>input</td>
</tr>
<tr>
<td>Interject_NTLogin</td>
<td>System Parameter</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Interject_LocalTimeZoneOffset</td>
<td>System Parameter</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>

<button class="collapsible-parameter">**NorthwindCustomers**<br>Stored Procedure: [demo].[Northwind_Customers_Pull]</button>
<div markdown="1" class="panel-parameter">
<table>
<tbody>

<td class="pph"><b>Parameter</b></td>
<td class="pph"><b>Parameter Type</b></td>
<td class="pph"><b>Data Type</b></td>
<td class="pph"><b>Direction</b></td>

<tr>
<td>CompanyName</td>
<td>Formula Parameter</td>
<td>nvarchar</td>
<td>input</td>
</tr>
<tr>
<td>ContactName</td>
<td>Formula Parameter</td>
<td>varchar</td>
<td>input</td>
</tr>
<tr>
<td>CustomerID</td>
<td>Formula Parameter</td>
<td>varchar</td>
<td>input</td>
</tr>
<tr>
<td>Interject_NTLogin</td>
<td>System Parameter</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Interject_LocalTimeZoneOffset</td>
<td>System Parameter</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>

<button class="collapsible-parameter">**NorthwindFixed**<br>Stored Procedure: [demo].[Northwind_Customers_FixedPull]</button>
<div markdown="1" class="panel-parameter">
<table>
<tbody>

<td class="pph"><b>Parameter</b></td>
<td class="pph"><b>Parameter Type</b></td>
<td class="pph"><b>Data Type</b></td>
<td class="pph"><b>Direction</b></td>

<tr>
<td>Interject_NTLogin</td>
<td>System Parameter</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Interject_ReturnError</td>
<td>System Parameter</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>

<button class="collapsible-parameter">**NorthwindInvoiceSave**<br>Stored Procedure: [demo].[Northwind_Invoices_Save]</button>
<div markdown="1" class="panel-parameter">
<table>
<tbody>

<td class="pph"><b>Parameter</b></td>
<td class="pph"><b>Parameter Type</b></td>
<td class="pph"><b>Data Type</b></td>
<td class="pph"><b>Direction</b></td>

<tr>
<td>Interject_ReturnError</td>
<td>System Parameter</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Interject_RequestContext</td>
<td>System Parameter</td>
<td></td>
<td></td>
</tr>

</tbody>
</table>
</div>
<button class="collapsible-parameter">**NorthwindSalesPull**<br>Stored Procedure: [demo].[Northwind_Customers_RangeDetailPull]</button>
<div markdown="1" class="panel-parameter">
<table>
<tbody>

<td class="pph"><b>Parameter</b></td>
<td class="pph"><b>Parameter Type</b></td>
<td class="pph"><b>Data Type</b></td>
<td class="pph"><b>Direction</b></td>

<tr>
<td>UnitsInStockMin</td>
<td>Formula Parameter</td>
<td>varchar</td>
<td>input</td>
</tr>
<tr>
<td>Category</td>
<td>Formula Parameter</td>
<td>varchar</td>
<td>input</td>
</tr>
<tr>
<td>Interject_NTLogin</td>
<td>System Parameter</td>
<td></td>
<td></td>
</tr>
<tr>
<td>Interject_ReturnError</td>
<td>System Parameter</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</div>

### Step 4: Setting up FinCube

[FinCube](/wIndex/FinCubeTheFinancialCube.html) is a special Data Portal that is used for financial reporting. This Portal is called "Demo_Interject_FinCube" in the Lab files and is used in 6 labs:

* Lab 1.3 Financial Report
* Lab 2.4 Financial Report
* Lab 4.3 Financial Report
* Lab 5.5 Using the Retain Feature
* Lab 7.2 Basic Distribution
* Lab 7.3 Advanced Distribution

Due to the complexities of this Data Portal, it is advised to use the API connection for this Data Portal. The following steps through how to set up this Portal.

#### Setting up the FinCube Data Connection

The FinCube Portal can use an API connection. You can use the following settings to set up the Data Connection:

* **Name:** \<Your own custom Name>
* **Description:** \<Your own custom Description>
* **Connection Type:** Web Api
* **Api Root Url:** https://data-api.gointerject.com/api
* **Api Connection String Name:** FinancialDemo-Database

![](/images/LabSetupManual/FinCubeDataConnection.png)
<br>

#### Setting up the FinCube Data Portal

You can use the following settings for the FinCube Data Portal:

* **Name:** \<Your own custom Name>
* **Description:** \<Your own custom Description>
* **Connection:** \<Use the name of the Data Connection you set up in the last section>
* **Command Type:** Stored Procedure Name
* **Stored Procedure/Command:** Client.[FinCube]
* **Api Relative Url:** InterjectDefaultRequest

![](/images/LabSetupManual/FinCubeDataPortal.png)
<br>

#### Setting up the FinCube Data Cells Data Portals

[Data Cells](/wAbout/Tabular-vs-Data-Cells.html) are a special type of cell that can directly pull data into the cell using the [Data Cell Functions](/wFunctions/Data-Cell-Functions.html). Data Cells are used in Lab 7.1 Quick Export and PDF. In order for the Data Cells to work, there must be some Data Portals set up. All these Data Portals will use the FinCube Data Connection set up previously.

The FinCube Data Portals must be set up for your particular Client profile. Therefore you will need your ClientID. This can be found by clicking **About Interject** on the Interject ribbon:

![](/images/LabSetupManual/ClientID.png)
<br>

Following are the Data Portals that must be set up.

<blockquote class=highlight_note>
<b>Note:</b> There are no parameters in the FinCube Portals.
</blockquote>
<br>

| Data Portal | Description | Connection | Command Type | Stored Procedure/Command | Api Relative Url |
|-----|-----|-----|-----|-----|-----|
| UpdateCellDataStatus_\<ClientID>\* | For Data Cells Update | \<FinCube Data Connection> | Stored Procedure Name | [Client].[RequestStatus] | InterjectDefaultRequest |
| UpdateCellData_\<ClientID> | For Data Cells | \<FinCube Data Connection> | Stored Procedure Name | [Client].[Request] | InterjectDefaultRequest |
| ImportScheduler_\<ClientID> | For Scheduler | \<FinCube Data Connection> | Stored Procedure Name | [Client].[ImportScheduler] | InterjectDefaultRequest |
| SegmentData_\<ClientID> | For Data Cells | \<FinCube Data Connection> | Stored Procedure Name | [Client].[Segment] | InterjectDefaultRequest |

\* Use your ClientID here

### Step 5: The Report Files

The following zip file contains all the necessary files for the Lab Guide:

[LabFiles.zip][2]

[2]:{{ site.url }}/download/LabFiles.zip

<blockquote class=highlight_note>
<b>Note:</b> Some labs do not have a lab file as they either start with a blank Excel file or are continued from a previous lab. The following labs do not have a file: 3.1, 3.2, 3.3, 3.6, and 7.3.
</blockquote>
<br>

### Step 6: Renaming the Data Portals

Once you have created the Data Portals with your own custom names, you will have to change the name of the Data Portals in the Report formulas found in the Lab files. To help with this, the following is a list of all the labs along with their associated file and every Data Portal used in those files:

[LabDataPortals.xlsx][3]

[3]:{{ site.url }}/download/LabDataPortals.xlsx

