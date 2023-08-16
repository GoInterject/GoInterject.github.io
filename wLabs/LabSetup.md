---
title: Setting up the Lab Environment
layout: custom
keywords: [lab, guide, setup, start]
description: This page details the necessary requirements and steps to set up a local environment that can accommodate a user following the Lab Guide.
---
* * *

## Overview

The [Lab Guide](/wLabs/lab.html) provides a convenient way for users to become familiar with Interject. The Guide walks through several individual walkthroughs on how to modify and create reports, drilling to data, and exporting reports. In order for a user to follow along, it is necessary to first set up a local environment that can accommodate this Lab Guide. This page details the necessary requirements and steps to do this.

### Interject Data Report Flow

The reports in the Lab Guide contain [Interject report formulas](/wIndex/Excel-Function-Index.html), each referencing a [Data Portal](/wPortal/Data-Portals.html) setup on the [Interject Portal Website](/wPortal/The-INTERJECT-Website-Portal.html). These Data Portals in turn reference a Data Connection and a Stored Procedure that point to a data source where the data will be pulled from. When the data source is a database, the entire flow can be conceptualized by the following diagram:

![](/images/LabSetup/FlowChart.png)
<br>

### Subscription Setup

In order to have the necessary requirements to go through the Lab Guide, a user just needs to be subscribed to the "Publisher - Interject App". Once subscribed, a user can select this company from the Interject ribbon:

![](/images/LabSetup/Companies.png)
<br>

The Publisher - Interject App company gives a user access to all the lab files via the Report Library:

![](/images/LabSetup/ReportLibraryLabFiles.png)
<br>

In addition, the Publisher - Interject App company grants a user access to all the Data Portals referenced in the labs. All the Data Portals in the Lab Guide use an API Data Connection. Therefore, no local database is necessary.

To request a subscription, contact us at [info@gointerject.com](mailto:info@gointerject.com).

### Manual Setup

Setting up a Lab environment manually gives greater control and flexibility in making modifications. However, there are a number of steps necessary:

1. Download the database and install locally
2. Set up the Data Connections on the Interject Portal site
3. Set up the Data Portals on the Interject Portal site
4. Download the lab files
5. Change the Data Portal names in the files to match the ones manually set up

### Setting up the Database

The first step in manually setting up a Lab Environment is to establish a database on a local system where the Lab Guide will be used. Interject's choice of database is [SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads){:target="_blank"}{:rel="noopener noreferrer"} as the Lab Guide relies on Microsoft's [Northwind Database](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/downloading-sample-databases){:target="_blank"}{:rel="noopener noreferrer"}.

The following is a minimalist script to recreate the database using SQL Server 2014 or greater:

[labs_db_script_sql_server_2014.sql][1]

[1]:{{ site.url }}/download/labs_db_script_sql_server_2014.sql

This script will have all the necessary tables, functions, procedures, schemas, and roles. You will need to first create the database of your choosing and then run this script inside that database. You may use [SSMS](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-2017){:target="_blank"}{:rel="noopener noreferrer"} or another editor of your choice.

### Setting up the Data Connection

Navigate to the [Interject Portal site](https://portal.gointerject.com/) and log in. For a guide about the Interject Portal site, see [here](/wPortal/The-INTERJECT-Website-Portal.html).

Set up a Data Connection that points to the database you set up. The examples used on this page will use the following:

* **Name: ** Local_Lab_DataSource
* **Description: ** This is the Data Connection to a local database set up for the Lab Guide
* **Connection Type: ** Database
* **Connection String: ** Data Source=(local);Initial Catalog=Interject_Lab_DB;Integrated Security=SSPI;

![](/images/LabSetup/DataConnection.png)
<br>

For detailed instructions on how to set up a Data Connection, see [Portal: Database Connection](/wPortal/L-Database-Connection.html).

### Setting up the Data Portals

Now that you have a database and set up a Data Connection to it, you need to start adding Data Portals. For instructions on how to set up Data Portals, see [Data Portals](/wPortal/Data-Portals.html).

The following is a list of the Data Portal used in the Lab Guide:

<hr>

#### Data Portal: NorthwindCreditSave

Stored Procedure: **[demo].[Northwind_Credit_Save]**

| Parameter | Parameter Type | Data Type | Direction |
| ----- | ----- | ----- | ----- |
| Interject_RequestContext | System Parameter\* | | |
| Interject_ReturnError | System Parameter | | |

\* **Note:** The Data Type and Direction are automatically set when selecting a System Parameter

<hr>

#### Data Portal: NorthwindCustomerAccountDetail

Stored Procedure: **[demo].[Northwind_CustomerAccountDetail_Pull]**

| Parameter | Parameter Type | Data Type | Direction |
| ----- | ----- | ----- | ----- |
| CompanyName | Formula Parameter | nvarchar | input |
| ContactName | Formula Parameter | varchar | input |
| CustomerID | Formula Parameter | varchar | input |
| UnappliedOnly | Formula Parameter | varchar | input |
| BeginDate | Formula Parameter | varchar | input |
| EndDate | Formula Parameter | varchar | input |
| Interject_ReturnError | System Parameter | | |
| Interject_RequestContext | System Parameter | | |

<hr>

#### Data Portal: NorthwindCustomerInvoices

Stored Procedure: **[demo].[Northwind_Invoices_Pull]**

| Parameter | Parameter Type | Data Type | Direction |
| ----- | ----- | ----- | ----- |
| CompanyName | Formula Parameter | nvarchar | input |
| ContactName | Formula Parameter | varchar | input |
| CustomerID | Formula Parameter | varchar | input |
| ShowExpectedDate | Formula Parameter | varchar | input |
| IncludePaid | Formula Parameter | varchar | input |
| Interject_RequestContext | System Parameter | | |

<hr>

#### Data Portal: NorthwindCustomerOrder

Stored Procedure: **[demo].[Northwind_CustomerOrder_Pull]**

| Parameter | Parameter Type | Data Type | Direction |
| ----- | ----- | ----- | ----- |
| OrderID | Formula Parameter | int | input |
| CustomerID | Formula Parameter | nvarchar | output |
| ContactName | Formula Parameter | nvarchar | output |
| CompanyName | Formula Parameter | nvarchar | output |
| ShipAddress | Formula Parameter | nvarchar | output |
| ShipCity | Formula Parameter | nvarchar | output |
| ShipPostalCode | Formula Parameter | nvarchar | output |
| ShipCountry | Formula Parameter | nvarchar | output |
| Phone | Formula Parameter | nvarchar | output |
| Fax | Formula Parameter | nvarchar | output |
| OrderDate | Formula Parameter | date | output |
| RequiredDate | Formula Parameter | date | output |
| ShippedDate | Formula Parameter | date | output |
| ShipVia | Formula Parameter | nvarchar | output |
| Freight | Formula Parameter | money | output |
| Interject_RequestContext | System Parameter | | |
| Interject_ReturnError | System Parameter | | |

<hr>

#### Data Portal: NorthwindCustomerOrders

Stored Procedure: **[demo].[Northwind_CustomerOrders_Pull]**

| Parameter | Parameter Type | Data Type | Direction |
| ----- | ----- | ----- | ----- |
| CompanyName | Formula Parameter | nvarchar | input |
| ContactName | Formula Parameter | varchar | input |
| CustomerID | Formula Parameter | varchar | input |
| Interject_NTLogin | System Parameter | | |
| Interject_LocalTimeZoneOffset | System Parameter | | |

<hr>

#### Data Portal: NorthwindCustomers

Stored Procedure: **[demo].[Northwind_Customers_Pull]**

| Parameter | Parameter Type | Data Type | Direction |
| ----- | ----- | ----- | ----- |
| CompanyName | Formula Parameter | nvarchar | input |
| ContactName | Formula Parameter | varchar | input |
| CustomerID | Formula Parameter | varchar | input |
| Interject_NTLogin | System Parameter | | |
| Interject_LocalTimeZoneOffset | System Parameter | | |

<hr>

#### Data Portal: NorthwindFixed

Stored Procedure: **[demo].[Northwind_Customers_FixedPull]**

| Parameter | Parameter Type | Data Type | Direction |
| ----- | ----- | ----- | ----- |
| Interject_NTLogin | System Parameter | | |
| Interject_ReturnError | System Parameter | | |

<hr>

#### Data Portal: NorthwindInvoiceSave

Stored Procedure: **[demo].[Northwind_Invoices_Save]**

| Parameter | Parameter Type | Data Type | Direction |
| ----- | ----- | ----- | ----- |
| Interject_ReturnError | System Parameter | | |
| Interject_RequestContext | System Parameter | | |

<hr>

#### Data Portal: NorthwindSalesPull

Stored Procedure: **[demo].[Northwind_Customers_RangeDetailPull]**

| Parameter | Parameter Type | Data Type | Direction |
| ----- | ----- | ----- | ----- |
| UnitsInStockMin | Formula Parameter | varchar | input |
| Category | Formula Parameter | varchar | output |
| Interject_NTLogin | System Parameter | | |
| Interject_ReturnError | System Parameter | | |

### Demo_Interject_FinCube

The "Demo_Interject_FinCube" is a Data Portal that is used in 6 labs:

* Lab 1.3 Financial Report
* Lab 2.4 Financial Report
* Lab 4.3 Financial Report
* Lab 5.5 Using the Retain Feature
* Lab 7.2 Basic Distribution
* Lab 7.3 Advanced Distribution

The [FinCube](/wIndex/FinCube---The-Financial-Cube.html) is a special Data Portal used for Financial reporting. Due to the complexities of this Data Portal, it is advised to use the API connection for this Data Portal instead of setting it up locally.

#### FinCube Data Connection

You can use the following settings for the FinCube Data Connection:

* **Name:** <Your own custom Name>
* **Description:** <Your own custom Description>
* **Connection Type:** Web Api
* **Api Root Url:** https://data-api.gointerject.com/api
* **Api Connection String Name:** FinancialDemo-Database

![](/images/LabSetup/FinCubeDataConnection.png)
<br>

#### FinCube Data Portal

You can use the following settings for the FinCube Data Portal:

* **Name:** <Your own custom Name>
* **Description:** <Your own custom Description>
* **Connection:** <Use the name of the Data Connection you set up>
* **Command Type:** Stored Procedure Name
* **Stored Procedure/Command:** Client.[FinCube]
* **Api Relative Url:** InterjectDefaultRequest

![](/images/LabSetup/FinCubeDataPortal.png)
<br>

### The Report Files

The following zip file contains all the necessary files for the Lab Guide:

[LabFiles.zip][2]

[2]:{{ site.url }}/download/LabFiles.zip

<br>

> Note: Some labs do not have a lab file as they either start with a blank Excel file or are continued from a previous lab. The following do not have a file: 3.1, 3.2, 3.3, 3.6, and 7.3.

### Renaming the Data Portals

Once you have created the Data Portals with your own custom names, you will have to change the name of the Data Portals in the Report formulas found in the Lab files. To help with this, the following is a list of all the labs along with their associated file and every Data Portal used in those files:

[LabDataPortals.xlsx][3]

[3]:{{ site.url }}/download/LabDataPortals.xlsx
