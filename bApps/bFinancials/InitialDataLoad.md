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
> ```SQL
> --Import configuration setup from Epicor and initial setup of Interject
> EXEC [Custom].[EPR_InstallScript1_DatabaseConfig]
> 	  @MasterEpicorDatabase          = '[MasterDatbase]'
> 	 ,@DefaultDatabaseNameSource     = '[DefaultDatabase]'
> ```
> ```SQL
> --Import data 
> EXEC [Custom].[EPR_InstallScript2_EpicorImport]
> 
> EXEC [Custom].[EPR_InstallScript3_ReportingImport]
> 	  @ReportingImport_YearBegin     = '2000'
>	 ,@ReportingImport_YearEnd       = '2016'
> 
> EXEC [Custom].[EPR_InstallScript4_GroupingImport]
> 
> ```
> 
> **Step 2:** Execute the following Script for SQL Agent Jobs
> 
> ```SQL
> EXEC [Custom].[EPR_InstallScript5_SetupJobs]
> ```
> 
> The following 4 jobs will be created: 
> * \[Interject_Reporting_CheckSchedule_ImportActual\] - Syncs Actual data between Epicor tables to Interject table
> * \[Interject_Reporting_CheckSchedule_ImportBudget\] - Syncs Budget data between Epicor tables to Interject table
> * \[Interject_Reporting_AddJobsFromScheduler\] - Process data and distribute it to interject tables 
> * \[Interject_Reporting_ImporEpicor_DeletesRecords\] - Validates data and remove records nightly if data was removed form epicor tables 

### Steps Required for Interject Application Setup

> To Do
>
> **Step 1:** Now log into [portal.gointerject.com](https://portal.gointerject.com) and select Data Connections on left side menu and change company to "Epicor Test III"
> ![New connection Button](/images/A-InitialDataLoad/Login1.png){: .center-image }
> - Change Client \(Company\) to new setup “Epicor Test” 
> ![New connection Button](/images/A-InitialDataLoad/changeco.png){: .center-image }
>
> **Step 2:** Click "My Data in the left-hand menu and select "New Connection" button on the top right of the page.
> ![New connection Button](/images/A-InitialDataLoad/NewConnection0.png){: .center-image }
> ![New connection Button](/images/A-SQL-Installation/NewConnections.png){: .center-image }
>
> **Step 5:** Select "Database" in the **Connection Type** field.
>
> **Step 6:** Fill in the Connection Details page contains the following inputs for new connections:
> 
> * **Name:** A unique friendly name used when connecting a Data Portal to the Data Connection
> * **Description** (optional): description of what the connection string is connecting to
> * **Connection String:** used by INTERJECT to connect to the specified server & database
>
> ![Connection Details Page](/images/Database/04.png){: .center-image }
>
> Use the following connection string:
> - "Server=SQL02.lsusa.local\D12INTUITION;Database=Interject_Reporting@Epicor3; Integrated Security = SSPI;"
>

## Redirect the DB Connection to the new DB in Interject portal

> To Do
>
> **Step 1:** Go to **My Apps** on the left menu of the [portal.gointerject.com](https://portal.gointerject.com) page
>![Epicor Tools Connection Page](/images/A-InitialDataLoad/MyApps.png){: .center-image }
>
> **Step 2:** Select "Interject Financials - Epicor" 
>
> **Step 3:** Under the Connection Redirect section, select the connection you wish to overide in the left side, then the new data connection on the right
> 
> **Step 4:** Save your changes
> ![Epicor Tools Connection Page](/images/A-InitialDataLoad/ConnectionRedirect.png){: .center-image }
>
