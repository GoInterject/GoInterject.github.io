---
title: SQL Database Installation
layout: custom
keywords: []
description: 
---

## Settings

### SQL Server Version
To check your MSSQL version, run ```SELECT @@VERSION``` in a query window. 

MSSQL Server 2008 and newer is supported.

### SQL Database Mail Profile
To check the Mail profile, run ```SELECT name FROM msdb.dbo.sysmail_profile```.

In this case, the result should be **PROD | BETA | DEV:Mail**


## Deployment via SSMS

The following activies are to be completed while conected to the SQL Server via SSMS using a user account belonging to the SysAdmin Server Role. Scripts should be executed in order to work correctly.

**Step 1**

Execute **\01.PrepareServer_MasterDB.sql** in **[master]** db to implement the following on the SQL Server. Estimated run time is a minute.

- CREATE [Interject_Reporting] database, if not already exist 

**Step 2**

Execute **\02.ReportingDB_FullDeployScript.sql** in **[Interject_Reporting]** db to implement the following on the SQL Server:

-	Interject Financials for Spreadsheets w/Epicor Enterprise integration database objects

**Step 3**

Execute **\03.ReportingDB_ExecuteScripts.sql** in **[Interject_Reporting]** db to initialize Epicor Enterprise data for Interject Financials for Spreadsheets.
```SQL
Execute [Custom].[EPR_InstallScript1_DatabaseConfig]

Execute [Custom].[EPR_InstallScript1_DatabaseConfig]
	@MasterEpicorDatabase = '[DemoControl]'
	,@DefaultDatabaseNameSource = '[DemoHold]'

Execute [Custom].[EPR_InstallScript2_EpicorImport]
Execute [Custom].[EPR_InstallScript3_ReportingImport]

Execute [Custom].[EPR_InstallScript3_ReportingImport]
	@ReportingImport_YearBegin = '1996'
	,@ReportingImport_YearEnd = '2000'

Execute [Custom].[EPR_InstallScript4_GroupingImport]
Execute [Custom].[EPR_InstallScript6_FullAccountGrouping]
EXEC [Custom].[EPR_InstallScript7_CostCenterGrouping]
```
**Step 4**

Execute **\04.ReportingDB_Permissions.sql** in **[Interject_Reporting]** db to implement the following on the SQL Server:

-	CREATE **[db_Interject]** database role
-	IF SQL-AUTH: CREATE **[InterjectAppUser]** database user and add to database role
-	IF WIN-AUTH:  CREATE **[INTERJECT\InterjectUsers]** database user and add to database role
-	APPLY PERMISSIONS TO SCHEMAS for database role
    - **[Client]** – EXECUTE
    - **[Custom]** – EXECUTE
    - **[Report]** – EXECUTE

**Step 5**

Execute **\04.ReportingDB_AddSignaturePermissions.sql** in **[Interject_Reporting]** db to implement the following on the SQL Server:

*** Edit the script to set an alternative password for the certificate ***

-	CREATE CERTIFICATE **[InterjectCertificate]**
-	CREATE CERTIFICATE USER **[InterjectCertificateUser]**
-	Add certificate to stored procedures with dynamic sql.
    - [Custom].[GL_COA_withBalances]
    - [Custom].[GL_JEQuery]
    - [Custom].[EPR_Grouping_Import]
    - [Custom].[GL_Segment]
    - [FinCube].[FinalCalculation]
    - [FinCube].[FinalCalculation]
    - [Note].[Note_Save]
    - [Note].[Note_Fixed_Get]
    - [Note].[Note_Save]
    - [Report].[MembersByCategory_Pull]
    - [Client].[FinCube_DynamicRow]

-	APPLY PERMISSIONS TO SCHEMAS for certificate user
    - [FSGroup] – SELECT   
    - [FSData] – SELECT
    - [ImportERP] – SELECT

**Step 6**

