---
title: Initial Data Load
filename: "InitialDataLoad.md"
layout: custom
keywords: [Epicor, setup, init, data]
headings: ["Begin Data Load", "Steps Required for Interject Application Setup - Data Connection", "Redirect the DB Connection to the new DB in Interject portal"]
links: ["https://docs.gointerject.com/bApps/bFinancials/DeactiveDB.html", "https://portal.gointerject.com", "https://portal.gointerject.com"]
image_dir: "Train"
images: [{file: "sample", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "Login1", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "changeco", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "NewConnection0", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "NewConnections", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "04", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "MyApps", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "ConnectionRedirect", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}]
description: Setup to initialize Epicor Enterprise Data.
---

## Begin Data Load

> To Do
>
> **Step 1:** Execute the following Script DB to initialize Epicor Enterprise Data
>
>
> - 1a
> ```SQL
> --Import configuration setup from Epicor and initial setup of Interject
> EXEC [Custom].[ERP_InstallScript1_DatabaseConfig]
>       @MasterEpicorDatabase          = '[<INSERT Master DB NAME>]'
>      ,@DefaultDatabaseNameSource     = '[<INSERT Default DB name>]'
> ```
> SAMPLE
> ![Epicor Tools Connection Page](/images/Train/sample.png){: .center-image }
>
> **Note:** You may choose to limit the import to a specific database or databases. Please see the [Deactivate Databases](https://docs.gointerject.com/bApps/bFinancials/DeactiveDB.html) page to do so.
>
> - 1b
> ```SQL
> --Import data 
> EXEC [Custom].[ERP_InstallScript2_EpicorImport]
> ```
>
> - 1c
> ```SQL
> --Enable Rollups
> EXEC [Custom].[ERP_InstallScript3_GroupingImport]
> ```
>
> - 1d
>```SQL
> --Specify historical periods in which to seed Interject Data Store
> EXEC [Custom].[ERP_InstallScript4_ReportingImport]
> 	  @ReportingImport_YearBegin     = 'YYYY'
>	 ,@ReportingImport_YearEnd       = 'YYYY'
>    ,@ImportBudget = 'INSERT value Yes or No'
> ```
> SAMPLE
> ```SQL
> EXEC [Custom].[ERP_InstallScript4_ReportingImport]
> @ReportingImport_YearBegin	= '2000'
> ,@ReportingImport_YearEnd	    = '2016'
> ,@ImportBudget				= 'Yes'
>```
>
> **Step 2:** Execute the following Script for SQL Agent Jobs
> 
> - 2a
> ```SQL
> --Setup SQL Agent Jobs to seed "nightly" sync of Interject data store
> EXEC [Custom].[ERP_InstallScript5_SetupJobs]
> ```
> 
> The following 4 jobs will be created: 
> * \[Interject_Reporting_CheckSchedule_ImportActual\] - Syncs Actual data between Epicor tables to Interject table
> * \[Interject_Reporting_CheckSchedule_ImportBudget\] - Syncs Budget data between Epicor tables to Interject table
> * \[Interject_Reporting_AddJobsFromScheduler\] - Process data and distribute it to interject tables 
> * \[Interject_Reporting_ImporEpicor_DeletesRecords\] - Validates data and remove records nightly if data was removed from Epicor tables 

### Steps Required for Interject Application Setup - Data Connection

> To Do
>
> **Step 1:** Now log into [portal.gointerject.com](https://portal.gointerject.com) and select Data Connections on left side menu and change company to "Epicor Test III"
> ![New connection Button](/images/A-InitialDataLoad/Login1.png){: .center-image }
> 
> **Step 2:** Change Client \(Company\) Dropdown in upper right hand corner of portal site 
> ![New connection Button](/images/A-InitialDataLoad/changeco.png){: .center-image }
>
> **Step 3:** Click “My Data > Data Connections in the left-hand menu 
> ![New connection Button](/images/A-InitialDataLoad/NewConnection0.png){: .center-image }
>
> **Step 4:** Select “New Connection” button on the top right of Page
> ![New connection Button](/images/A-SQL-Installation/NewConnections.png){: .center-image }
>
> **Step 5:** Select "Database" in the **Connection Type** field.
>
> **Step 6:** Fill in the Connection Details page, which contains the following inputs for new connections:
> ![Connection Details Page](/images/Database/04.png){: .center-image }
> 
> * **Name:** A unique friendly name used when connecting a Data Portal to the Data Connection
> * **Description** (optional): description of what the connection string is connecting to
> * **Connection String:** used by Interject to connect to the specified server & database
> "Server=Scotty-Test;Database=Northwind Integrated Security = SSPI;”
>

## Redirect the DB Connection to the new DB in Interject portal

> To Do
>
> **Step 1:** Go to **My Apps** on the left menu of the [Interject Portal](https://portal.gointerject.com) page and select the "Interject Financials - Epicor offering. Versions may change
>![Epicor Tools Connection Page](/images/A-InitialDataLoad/MyApps.png){: .center-image }
>
> **Step 2:** At the bottom of the page in the “Connection Redirect” section choose to replace any existing Data Connection  Connection with “new connection” 
>
> **Step 3:** Click save
> ![Epicor Tools Connection Page](/images/A-InitialDataLoad/ConnectionRedirect.png){: .center-image }
>
>
