---
title: Initial Data Load
layout: custom
keywords: []
description: 
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
> 	  @MasterEpicorDatabase          = '[INSERT>MasterDatbase]'
> 	 ,@DefaultDatabaseNameSource     = '[INSERT>DefaultDatabase]'
> ```
>
> - 1b
> ```SQL
> --Import data 
> EXEC [Custom].[ERP_InstallScript2_EpicorImport]
> ```
>
> - 1c
> ```SQL
> --Specify historical periods in which to seed Interject Data Store
> EXEC [Custom].[ERP_InstallScript3_ReportingImport]
> 	  @ReportingImport_YearBegin     = 'INSERT>YYYY'
>	 ,@ReportingImport_YearEnd       = 'INSERT>YYYY'
> ```
>
> - 1d
> ```SQL
> --Specify historical periods in which to seed Interject Data Store
> EXEC [Custom].[ERP_InstallScript4_GroupingImport]
> ```
> 
> **Step 2:** Execute the following Script for SQL Agent Jobs
> 
> - 2a
> ```SQL
> --Import configuration setup from Epicor and initial setup of Interject
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
> **Step 3:** Click “My Data>Data Connections in the left-hand menu 
> ![New connection Button](/images/A-InitialDataLoad/NewConnection0.png){: .center-image }
>
> **Step 4:** Select “New Connection” button on the top right of Page
> ![New connection Button](/images/A-SQL-Installation/NewConnections.png){: .center-image }
>
> **Step 5:** Select "Database" in the **Connection Type** field.
>
> **Step 6:** Fill in the Connection Details pag, which contains the following inputs for new connections:
> ![Connection Details Page](/images/Database/04.png){: .center-image }
> 
> * **Name:** A unique friendly name used when connecting a Data Portal to the Data Connection
> * **Description** (optional): description of what the connection string is connecting to
> * **Connection String:** used by INTERJECT to connect to the specified server & database
> "Server=SQL02.lsusa.local\D12INTUITION;Database=Interject_Reporting@Epicor3; Integrated Security = SSPI;"
>

## Redirect the DB Connection to the new DB in Interject portal

> To Do
>
> **Step 1:** Go to **My Apps** on the left menu of the [portal.gointerject.com](https://portal.gointerject.com) page
>![Epicor Tools Connection Page](/images/A-InitialDataLoad/MyApps.png){: .center-image }
>
> **Step 2:** Select "Interject Financials - Epicor" 
>
> **Step 3:** Under the Connection Redirect section -scroll to bottom of screen - select the connection you wish to overide in the left side, then the new data connection on the right
> ![Epicor Tools Connection Page](/images/A-InitialDataLoad/ConnectionRedirect.png){: .center-image }
>
> **Step 4:** Save your changes
