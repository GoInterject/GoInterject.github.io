---
title: "Develop: Change Log Data Save"
filename: "L-Dev-ChangelogDataSave.md"
layout: custom
keywords: [developer, example, walkthrough, SQL, SSMS, Data Portal, data connection, data save, history]
headings: ["Overview", "Setting Up the Data Connection", "Setting Up the Data Portal", "Setting Up the Report", "Setting Up the Tables", "Setting Up the Stored Procedure", "Modifying the Stored Procedure", "Current Date and Time", "ChangeLog", "Merge Update", "Merge Insert", "Merge Output", "Update Target Table", "Update History Table", "Final Stored Procedure", "Testing the Stored Procedure", "Testing the ReportSave"]
links: ["/wDeveloper/L-Dev-InsertDeleteDataSave.html", "#setting-up-the-data-connection", "/wGetStarted/L-Dev-CustomerAging.html#setting-up-the-data-connection", "#setting-up-the-data-portal", "#setting-up-the-report", "#setting-up-the-stored-procedure", "#testing-the-stored-procedure", "https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/downloading-sample-databases", "/wGetStarted/L-Dev-CustomerAging.html#setting-up-the-data-connection", "https://portal.gointerject.com", "/wPortal/Logging-In-to-Website-Portal.html", "https://docs.gointerject.com/wDeveloper/L-Dev-ChangelogDataSave.html#setting-up-the-stored-procedure", "/wIndex/Request-Context-Parse.html", "/wDeveloper/L-Dev-InsertDeleteDataSave.html#setting-up-the-report", "/wDeveloper/L-Dev-InsertDeleteDataSave.html#final-stored-procedure", "https://docs.gointerject.com/wDeveloper/L-Dev-ChangelogDataSave.html#testing-the-stored-procedure", "#setting-up-the-tables", "#changelog", "#update-history-table", "/wDeveloper/L-Dev-InsertDeleteDataSave.html#update-changelog", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#overview"]
image_dir: "L-Dev-ChangelogDataSave"
images: [
	{file: "NewDataPortal", type: "png", site: "Portal", cat: "Data Portals", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "DataPortalDetails", type: "png", site: "Portal", cat: "Data Portals", sub: "Details", report: "", ribbon: "", config: ""}, 
	{file: "AddSystemParameter", type: "png", site: "Portal", cat: "Data Portals", sub: "Details", report: "", ribbon: "", config: ""}, 
	{file: "ChangeReportSaveFunction", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""}, 
	{file: "SPCurrentDate", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SPChangeLog2", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SPMergeUpdate", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SPMergeInsert", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SPMergeOutput", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SPUpdateTable", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SPInsertHistory", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "ViewSQLTestClick", type: "png", site: "Add-in", cat: "Ribbon", sub: "System", report: "", ribbon: "", config: ""}, 
	{file: "CopyTestCode", type: "png", site: "Add-in", cat: "View SQL Test For ActiveCell", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "PasteTestCode", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "ExecuteTestCode", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "TestCodeExecuted", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "TestingTheReportChanges", type: "png", site: "Add-in", cat: "Report", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "TestingTheReportResults", type: "png", site: "Add-in", cat: "Report", sub: "", report: "", ribbon: "", config: ""}
	]
description: In this example you will modify the simple data save using the Customer Aging Detail report and the Northwind Customers data source to add or delete a customer.
---
* * *

## Overview

In this example you will modify the previous [Insert &amp; Delete Data Save](/wDeveloper/L-Dev-InsertDeleteDataSave.html), which was set up to insert and delete customers. In this Change Log Data Save, you will modify the Stored Procedure (SP) again to include a change log.

A change log is basically an additional table in the database that will record all the changes that take place to the targeted table. This history table keeps track of what records and columns were changed, what type of change took place (e.g. update, insert, deleted, added), who performed the change and the date and time it took place. It also keeps track of the old values that were changed so you can compare the old with the new values and recover data if desired.

This walkthrough involves 5 main steps:

1. [Set up a Data Connection](#setting-up-the-data-connection) ([completed already](/wGetStarted/L-Dev-CustomerAging.html#setting-up-the-data-connection))
2. [Set up a Data Portal](#setting-up-the-data-portal)
3. [Setting up the report to handle the save](#setting-up-the-report)
4. [Set up the Stored Procedure (SP) to handle the save](#setting-up-the-stored-procedure)
5. [Test the Stored Procedure &amp; ReportSave](#testing-the-stored-procedure)

<blockquote class=highlight_note>
<b>Note:</b> This example uses Microsoft's Northwind Database. You can download this database <a href="https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/downloading-sample-databases">here</a> or you can use this example as a guide for your own data source.
</blockquote>

## Setting Up the Data Connection

For the Data Connection for this example, you will use the connection previously set up [here](/wGetStarted/L-Dev-CustomerAging.html#setting-up-the-data-connection).

## Setting Up the Data Portal

**Step 1:** Navigate to [https://portal.gointerject.com](https://portal.gointerject.com) and [log in](/wPortal/Logging-In-to-Website-Portal.html). Click on **Data Portals** on the left side bar and then the **NEW DATA PORTAL** button.

![](/images/L-Dev-ChangelogDataSave/NewDataPortal.png)
<br>

**Step 2:** Enter the following details on setting up the new data portal and click "**CREATE DATA PORTAL**".

* **Data Portal Code:** NorthwindChangelogDataSave
* **Description:** Data portal for changelog data save
* **Category:** Demo
* **Connection:** NorthwindExampleDB_MyName (replace "MyName" with your name)
* **Command Type:** Stored Procedure
* **Stored Procedure/Command:** NorthwindChangelogDataSaveSP

<blockquote class=highlight_note>
<b>Note:</b> You will create the "NorthwindChangelogDataSaveSP" Stored Procedure <a href="https://docs.gointerject.com/wDeveloper/L-Dev-ChangelogDataSave.html#setting-up-the-stored-procedure">later</a>.
</blockquote>
<br>

![](/images/L-Dev-ChangelogDataSave/DataPortalDetails.png)
<br>

**Step 3:** After creating the data portal, scroll down and click **Click here to add a System Parameter** and ensure the **Interject_RequestContext** parameter is set.

![](/images/L-Dev-ChangelogDataSave/AddSystemParameter.png)
<br>

The System Parameter [Interject_RequestContext](/wIndex/Request-Context-Parse.html) will transfer contextual data to the Stored Procedure you will set up later. In this example you will not need this info but it is a good practice to set this parameter for all your Stored Procedures.

## Setting Up the Report

Begin by opening up the report that was completed in the [previous data save](/wDeveloper/L-Dev-InsertDeleteDataSave.html#setting-up-the-report). 

The only thing that needs to be changed in this report is the name of the Data Portal in the ReportSave formula:

![](/images/L-Dev-ChangelogDataSave/ChangeReportSaveFunction.png)
<br>

## Setting Up the Tables

An additional table will be created to store the history of changes made to the targeted table, in this case `dbo.Northwind_Customers`. This history table will contain the current and previous column values. It also includes `EditedBy`, `ActionType`, and `DateEdited` columns to keep track of who did the change, what type of change occurred, and when the change took place.

<blockquote class=highlight_note>
<b>Note:</b> There are two types of tables to use for a history table: wide and tall. A wide table uses all the columns, both current and old, making it "wide". Thus multiple changes to a single record would only take up one record space in a wide history table.
<br><br>
A tall table would typically contain an attribute column to represent what column was changed. It also contains two columns representing the current value and the old value. A record in a tall table represents one single change to a column value.
<br><br>
This example uses a wide table for simplicity. In practice, a tall table is more efficient in storage for history tables.
</blockquote>
<br>

Execute the following SQL code to create this history table:

```sql
CREATE TABLE [dbo].[Northwind_Customers_History] (
	[TransactionID] [int] IDENTITY(1,1) NOT NULL,
	[CustomerID] [nchar] (5) NOT NULL,
	[CompanyName] [nvarchar] (40) NULL,
	[CompanyNameOld] [nvarchar] (40) NULL,
	[ContactName] [nvarchar] (30) NULL,
	[ContactNameOld] [nvarchar] (30) NULL,
	[ContactTitle] [nvarchar] (30) NULL,
	[ContactTitleOld] [nvarchar] (30) NULL,
	[Address] [nvarchar] (60) NULL,
	[City] [nvarchar] (15) NULL,
	[CityOld] [nvarchar] (15) NULL,
	[Region] [nvarchar] (15) NULL,
	[PostalCode] [nvarchar] (10) NULL,
	[Country] [nvarchar] (15) NULL,
	[CountryOld] [nvarchar] (15) NULL,
	[Phone] [nvarchar] (24) NULL,
	[PhoneOld] [nvarchar] (24) NULL,
	[Fax] [nvarchar] (24) NULL,
	[ClientID] [nvarchar] (15) NULL,
	[IsDeleted] [bit] NULL,
	[EditedBy] [nvarchar] (40) NOT NULL,
	[ActionType] [nvarchar] (10) NOT NULL,
	[DateEdited] [datetime2] (7) NOT NULL,
	PRIMARY KEY (TransactionID)
)
```

Next you will add 3 columns to the targeted table, `dbo.Northwind_Customers` to also keep track of the update details in the original table.

Execute the following SQL to add the three columns:

```sql
ALTER TABLE dbo.Northwind_Customers
ADD EditedBy NVARCHAR(40),
    UpdateTypeCode VARCHAR(10),
    LastDateEdited DATETIME2(7)
```

## Setting Up the Stored Procedure

Next you will create a new Stored Procedure that builds from the [previous save](/wDeveloper/L-Dev-InsertDeleteDataSave.html#final-stored-procedure). To make this easier, simply copy the SP into a new query, change the command to "CREATE OR ALTER PROC NorthwindChangelogDataSaveSP" and execute it to save it. Then you can begin making modifications to it. For your convenience, the SP is posted here.

<blockquote class=highlight_note>
<b>Note:</b> The code for testing the SP has been removed. It will be handled <a href="https://docs.gointerject.com/wDeveloper/L-Dev-ChangelogDataSave.html#testing-the-stored-procedure">later</a>
</blockquote>
<br>

<button class = "collapsible"> NorthwindChangelogDataSaveSP </button>
<div markdown="1" class="panel">

```sql
CREATE OR ALTER   PROC [dbo].[NorthwindInsertDeleteDataSaveSP]

	-- System Params not in formula
	@Interject_RequestContext nvarchar(max)
	,@TestMode bit = 0 -- used only for testing the stored procedure directly.  It will show more results when set to 1.

AS

/*
==================================================================================
	CREATED DATE: 3/7/2023 8:22 AM
	CREATED BY: Interject Default
	DESCRIPTION: Example data pull to be used with Interject
	
	---------------------------------------------------------------------------
	TEST Example: Use the below to test this stored procedure:
	---------------------------------------------------------------------------
	
	This section has been removed. To get sample code for testing this stored procedure,
	select the cell in Excel containing the ReportSave function. Then click on the Interject
	ribbon, click System > View SQL Test For ActiveCell.

	---------------------------------------------------------------------------
	Validation Example:
	---------------------------------------------------------------------------
	Note: By adding 'UserNotice:' to the error message, Interject will show the message in an alert box and not flag the formula with an error.
	Without it, the formula will show an error with the text the user can click into.
	
	IF @ParameterName = 'TheWrongValue'
	BEGIN
		RAISERROR ('UserNotice:You selected an invalid value. Unable to continue.',
		18, -- Severity,
		1) -- State)
		
		RETURN
	END
	
	---------------------------------------------------------------------------
	Reserved Parameters:
	---------------------------------------------------------------------------
	Note: If the below parameters are added to your stored procedure and to the
	data portal parameter list, Interject will pass the related value automatically.
	
	@Interject_XMLDataToSave varchar(max) - Required for saving data. It contains XML for the designated cells values.
	@Interject_ColDefItems varchar(max) - Provides the Column Definitions in XML designated within the report formula.
	@Interject_RowDefItems varchar(max) - Provides the Row Definitions in XML designated within the report formula.
	@Interject_SourceFileAndPath varchar(500) - Provides the path and file name delimited by '|' of the current file.
	@Interject_SourceFilePathAndTab varchar(1000) - Provides the path, file name and active tab name delimited by '|' of the current file.
	@Interject_LocalTimeZoneOffset money - Provides a number (0.000) that represents the offset of the users time to UTC time.
	@Interject_NTLogin varchar(50) - Provides the user's computer login name for their current session.
	@Interject_UserID varchar(50) - Provides the Interject User ID for their current session.
	@Interject_LoginName varchar(50) - Provides the Interject Full name for their current session.
	@Interject_ExcelVersion varchar(50) - Provides the users Excel version.
	@Interject_UserRoles varchar(1000) - Provides the Interject roles assigned to the user.
	@Interject_ClientID varchar(50) - Provides the Interject Client ID for their current session.
	@Interject_ReturnError varchar(2000) - Is an output parameter that can be used to return an error back to the user. Pass empty string for no error.
	@Interject_RequestContext nvarchar(max) - Provides all above request context and both the open text and encrypted version of the user context.

==================================================================================
*/

	--
	-- Use helper to extract data from Interject_RequestContext. Remove items that are not needed
	-- The helper stored procedure [dbo].[RequestContext_Parse] is required for this section to function
	--

	DECLARE
		@ExcelVersion					NVARCHAR(100)
		,@IdsVersion					NVARCHAR(100)	
		,@FileName					NVARCHAR(1000)	
		,@FilePath					NVARCHAR(1000)
		,@TabName						NVARCHAR(1000)	
		,@CellRange					NVARCHAR(100)	
		,@SourceFunction				NVARCHAR(100)	
		,@UtcOffset					DECIMAL(6,4)	
		,@ColDefItemsDelimited			xml	
		,@ResultDefItemsDelimited		xml	
		,@RowDefItemsDelimited			xml
		,@MachineLoginName				NVARCHAR(100)
		,@MachineName					NVARCHAR(100)	
		,@Interject_UserID				NVARCHAR(100)
		,@Interject_ClientID			NVARCHAR(100)
		,@Interject_LoginName			NVARCHAR(100)	
		,@Interject_LoginAuthTypeID		INT		
		,@Interject_LoginDateUTC		     DATETIME
		,@Interject_UserRolesDelimited	NVARCHAR(max)
		,@UserContextEncrypted			NVARCHAR(4000)
		,@Interject_XMLDataToSave	     xml	
	
	EXEC [dbo].[RequestContext_Parse]
		@Interject_RequestContext		 = @Interject_RequestContext
		,@ExcelVersion					 = @ExcelVersion				OUTPUT
		,@IdsVersion					 = @IdsVersion					OUTPUT
		,@FileName					 = @FileName					OUTPUT
		,@FilePath					 = @FilePath					OUTPUT
		,@TabName						 = @TabName					OUTPUT
		,@CellRange					 = @CellRange			  		OUTPUT
		,@SourceFunction				 = @SourceFunction		  		OUTPUT
		,@UtcOffset					 = @UtcOffset		   			OUTPUT
		,@ColDefItemsDelimited			 = @ColDefItemsDelimited			OUTPUT
		,@ResultDefItemsDelimited		 = @ResultDefItemsDelimited		OUTPUT
		,@RowDefItemsDelimited			 = @RowDefItemsDelimited			OUTPUT
		,@MachineLoginName				 = @MachineLoginName			OUTPUT
		,@MachineName					 = @MachineName				OUTPUT
		,@Interject_UserID				 = @Interject_UserID			OUTPUT
		,@Interject_ClientID			 = @Interject_ClientID			OUTPUT
		,@Interject_LoginName			 = @Interject_LoginName			OUTPUT
		,@Interject_LoginAuthTypeID		 = @Interject_LoginAuthTypeID		OUTPUT
		,@Interject_LoginDateUTC			 = @Interject_LoginDateUTC		OUTPUT
		,@Interject_UserRolesDelimited	 = @Interject_UserRolesDelimited	OUTPUT
		,@UserContextEncrypted			 = @UserContextEncrypted			OUTPUT
		,@Interject_XMLDataToSave		 = @Interject_XMLDataToSave		OUTPUT
	
	IF @TestMode = 1
	BEGIN
		SELECT
			@ExcelVersion					as '@ExcelVersion'
			,@IdsVersion					as '@IdsVersion'
			,@FileName					as '@FileName'
			,@FilePath					as '@FilePath '
			,@TabName						as '@TabName'
			,@CellRange					as '@CellRange'
			,@SourceFunction				as '@SourceFunction'
			,@UtcOffset					as '@UtcOffset'
			,@ColDefItemsDelimited			as '@ColDefItemsDelimited'
			,@ResultDefItemsDelimited		as '@ResultDefItemsDelimited'
			,@RowDefItemsDelimited			as '@RowDefItemsDelimited'
			,@MachineLoginName				as '@MachineLoginName'
			,@MachineName					as '@MachineName'
			,@Interject_UserID				as '@Interject_UserID'
			,@Interject_ClientID			as '@Interject_ClientID'
			,@Interject_LoginName			as '@Interject_LoginName'
			,@Interject_LoginAuthTypeID		as '@Interject_LoginAuthTypeID'
			,@Interject_LoginDateUTC			as '@Interject_LoginDateUTC'
			,@Interject_UserRolesDelimited	as '@Interject_UserRolesDelimited'
			,@UserContextEncrypted			as '@UserContextEncrypted'
			,@Interject_XMLDataToSave		as '@Interject_XMLDataToSave'
	END

	DECLARE @ErrorMessageToUser as varchar(1000) = ''
	
	--
	-- PROCESS THE XML DATA INTO TABLE VARIABLE
	-- varchar(max) is used for the data type by default.  Please change for the specific requirement.
	--

	DECLARE @DataToProcess TABLE
	(
		-- the below are system values used internally in this stored procedures
		 [_ExcelRow] INT 
		,[_MessageToUser] VARCHAR(500) DEFAULT('')
		-- Below are your columns expected from the spreadsheet that is calling this save stored procedure
		-- Please change the (max) to the expected length of the text input.  If limiting length, be sure to make the size larger than allowed so you can add validation to notify the user
	
		,[CustomerID] NCHAR(5)
		,[CompanyName] NVARCHAR(30)
		,[ContactName] NVARCHAR(30)
		,[ContactTitle] NVARCHAR(30)
		,[Phone] NVARCHAR(24)
		,[Phone_Int] INT
		,[City] NVARCHAR(15)
		,[Country] NVARCHAR(15)
		,[ToBeDeleted] NVARCHAR(10)
		,[ToBeDeletedBit] BIT DEFAULT(0)
	)

	IF DATALENGTH(@Interject_XMLDataToSave) > 0 
	BEGIN
		declare @DataToProcessXML as XML
		-- Handle conversion of XML text into an XML variable.  
		BEGIN TRY
			SET @DataToProcessXML = CAST(@Interject_XMLDataToSave as XML)
		END TRY
		BEGIN CATCH
			SET @ErrorMessageToUser = 'Error in Parsing XML from Interject.  Error: ' + ERROR_MESSAGE()
			GOTO FinalResponseToUser
		END CATCH
		
		-- Insert the XML into the table variable for further processing
		INSERT into @DataToProcess(
		    [_ExcelRow]
		    ,[CustomerID]
		    ,[CompanyName]
		    ,[ContactName]
		    ,[ContactTitle]
		    ,[Phone]
		    ,[City]
		    ,[Country]
		    ,[ToBeDeleted]

		)
		SELECT
			-- The below row value is always provided by Interject
			T.c.value('./Row[1]', 'INT') as [_ExcelRow]
			-- The below columns are provided based on your column definitions in the ReportSave() function
			,T.c.value('./CustomerID[1]', 'NCHAR(5)') as [CustomerID]
			,T.c.value('./CompanyName[1]', 'NVARCHAR(30)') as [CompanyName]
			,T.c.value('./ContactName[1]', 'NVARCHAR(30)') as [ContactName]
			,T.c.value('./ContactTitle[1]', 'NVARCHAR(30)') as [ContactTitle]
			,T.c.value('./Phone[1]', 'NVARCHAR(24)') as [Phone]
			,T.c.value('./City[1]', 'NVARCHAR(15)') as [City]
			,T.c.value('./Country[1]', 'NVARCHAR(15)') as [Country]
			,T.c.value('./Delete[1]', 'NVARCHAR(10)') as [ToBeDeleted]
		FROM @DataToProcessXML.nodes('/XMLDataToSave/r') T(c)
	END
	
	-- TestMode is provided so a test save can be executed and all related data can be 
	-- easily viewed for testing while not effecting any data in the database
	IF @TestMode =1 
	BEGIN
		SELECT '@DataToProcess - After XML Processing' as ResultName
		SELECT * FROM @DataToProcess
	END
	
	UPDATE @DataToProcess 
		SET [ToBeDeletedBit] = 1
	WHERE [ToBeDeleted] = 'yes'

	--
	-- VALIDATION SECTION - Ensure inputs received from Excel are valid
	--

	-- Validate that the details do not have duplicates on the primary key
	UPDATE m
	SET [_MessageToUser] = [_MessageToUser] + ', Duplicate key'
	FROM @DataToProcess m
	INNER JOIN
		(
			SELECT [CustomerID] 
			FROM @DataToProcess
			WHERE [CustomerID] <> ''
			GROUP BY [CustomerID]
			HAVING COUNT(1) > 1
		) as t
		ON
			m.CustomerID = t.CustomerID
	
	-- Now check if there were any validation issues in the detail and stop processing if true
	IF EXISTS(SELECT 1 FROM @DataToProcess WHERE [_MessageToUser] <> '')
	BEGIN
		SET @ErrorMessageToUser = 'There were errors in the details of your input.  Please review the errors noted in each row.'
		GOTO FinalResponseToUser
	END

	--
	-- DATA UPDATE
	--

	BEGIN TRY
		
		-- this table variable will log the changes to the target table so it can be used
		-- to return helpful feedback to the user about how the save action resulted
		DECLARE @ChangeLog as TABLE
		(
			[_ExcelRow] INT	-- will capture the source row that affected the target table
			,[UpdateTypeCode] VARCHAR(10)  -- Will show UPDATE, INSERT, DELETE or ADDED_BACK
			,[CustomerID] NCHAR(5)
			,[IsDeleted] BIT
			,[IsDeletedOld] BIT
		)
		
		BEGIN TRAN t1
			--
			--  use MERGE statement that UPDATES, INSERTS, and DELETES in one action
			--
			MERGE dbo.Northwind_Customers t -- t = the target table or view to update
			USING (
				SELECT
				    [_ExcelRow]
				    ,[CustomerID]
				    ,[CompanyName]
				    ,[ContactName]
				    ,[ContactTitle]
				    ,[Phone]
				    ,[City]
				    ,[Country]
				    ,[ToBeDeleted]
				    ,[ToBeDeletedBit]
				FROM @DataToProcess 
			) s -- s = the source data to be used to update the target table
			-- the join on the column keys is specified below
			ON 
				s.[CustomerID] = t.[CustomerID]
				
			WHEN MATCHED -- Handles the update based on INNER JOIN
				AND NOT 
				(
				 -- To ensure only changes are captured
					s.[CompanyName] = t.[CompanyName]
					AND
					s.[ContactName] = t.[ContactName]
					AND
					s.[ContactTitle] = t.[ContactTitle]
					AND
					s.[Phone] = t.[Phone]
					AND
					s.[City] = t.[City]
					AND
					s.[Country] = t.[Country]
					AND
					s.[ToBeDeletedBit] = t.[IsDeleted]
				)
				THEN
				UPDATE SET
				      t.[CompanyName] = s.[CompanyName]
					,t.[ContactName] = s.[ContactName]
					,t.[ContactTitle] = s.[ContactTitle]
					,t.[Phone] = s.[Phone]
					,t.[City] = s.[City]
					,t.[Country] = s.[Country]
					,t.[IsDeleted] = s.[ToBeDeletedBit]   

			 WHEN NOT MATCHED BY TARGET
				AND
				LOWER(s.[ToBeDeleted]) <> 'yes'
				THEN INSERT (
				    [CustomerID]
				    ,[CompanyName]
				    ,[ContactName]
				    ,[ContactTitle]
				    ,[Phone]
				    ,[City]
				    ,[Country]
				    ,[IsDeleted]
				)
				VALUES (
				    [CustomerID]
				    ,[CompanyName]
				    ,[ContactName]
				    ,[ContactTitle]
				    ,[Phone]
				    ,[City]
				    ,[Country]
				    ,0
				)
			-- the output captures the changes to the table and logs to a table variable
			OUTPUT 
				isnull(inserted.[CustomerID],deleted.[CustomerID])  -- include deleted in case delete is added later. Inserted is used for both Update an Insert
				,s.[_ExcelRow] 
				,$action as UpdateTypeCode  -- this logs into an a change log table variable
				,inserted.[IsDeleted]
				,deleted.[IsDeleted] 
			INTO @ChangeLog
			(
				[CustomerID]
				,[_ExcelRow]
				,[UpdateTypeCode]
				,[IsDeleted]
				,[IsDeletedOld]
			); 

		  UPDATE @ChangeLog
		  SET UpdateTypeCode = 'DELETE'
		  WHERE UpdateTypeCode = 'UPDATE'
			 AND [IsDeleted] = 1
			
		  UPDATE @ChangeLog 
		  SET UpdateTypeCode = 'ADDED_BACK'
		  WHERE UpdateTypeCode = 'UPDATE'
			 AND [IsDeleted] = 0
			 AND [IsDeletedOld] = 1

    		  IF @TestMode = 1
			BEGIN
			SELECT * FROM dbo.Northwind_Customers
			END

			--now we have enough information to update the message to user for each row
			UPDATE dtp
			SET [_MessageToUser] = 
				CASE cl.UpdateTypeCode
					WHEN 'ADDED_BACK' THEN ', Added!'
					WHEN 'DELETE' THEN ', Deleted!'
					WHEN 'UPDATE' THEN ', Updated!'
					WHEN 'INSERT' THEN ', Inserted!'
					--ELSE ', No change'  -- not used in this example
				END 
			FROM @DataToProcess dtp
				INNER JOIN @ChangeLog cl  -- use Left Join if 'No Change' is to be identified
					 ON dtp.[_ExcelRow] = cl.[_ExcelRow]
				
		IF @TestMode = 1
		BEGIN
			SELECT '@ChangeLog- Show log of changes made' as ResultName
			select * from @ChangeLog
			
			ROLLBACK TRAN t1 -- note this does not roll back changes to table variables, only real tables
			SELECT 'Changes rolled back since in TEST mode!' as TestModeNote
		END
		ELSE
		BEGIN
			COMMIT TRAN t1
		END
	END TRY
	BEGIN CATCH
		IF @@TRANCOUNT > 0
			ROLLBACK TRAN t1
		
		SET @ErrorMessageToUser =  ERROR_MESSAGE()
		GOTO FinalResponseToUser
	END CATCH
	
FinalResponseToUser:
--
-- PROVIDE RESPONSE TO THE SAVE ACTION
--
	
	-- if test mode, show the final table 
	IF @TestMode = 1 
	BEGIN
		SELECT '@DataToProcess - After Validation' as ResultName
		SELECT * FROM @DataToProcess
	END
	
	-- return the recordset results back to the spreadsheet, if needed.
	SELECT
		[_ExcelRow] as [Row] -- this relates to the original row of the spreadsheet the data came from
		,SUBSTRING([_MessageToUser],3,1000) as [MessageToUser]  -- This is a field that, if it matches a column in the Results Range, will be placed in that column for the specified row
	FROM @DataToProcess
	
	-- if there is an error, raise error and Interject will catch and present to the user.
	-- Note that this is specifically done after the above resultset is returned, since initiating an error before
	-- will not allow a result set to be returned to provide feedback on each row 
	IF @ErrorMessageToUser <> ''
	BEGIN
		-- by adding 'UserNotice:' as a prefix to the message, Interject will not consider it a unhandled error 
		-- and will present the error to the user in a message box.
		SET @ErrorMessageToUser = 'UserNotice:' + @ErrorMessageToUser
		
		RAISERROR (@ErrorMessageToUser,
		18, -- Severity,
		1) -- State)
		RETURN
	END
```
</div>

Execute the above code to save the Store Procedure.

## Modifying the Stored Procedure

The following walks you through the major sections of the code with instructions on the changes. Additions are marked in yellow.

### Current Date and Time

Just after the "BEGIN TRY" statement, you will add a parameter to capture the current date. By storing this once in a parameter, the same date and time stamp will be used for all the updates that follow. Note that the UTC date/time is used, which is standard practice for consistency.

![](/images/L-Dev-ChangelogDataSave/SPCurrentDate.png)
<br>

### ChangeLog

The `@ChangeLog` table will need to be updated to included all the changes in the columns. This is done by adding the column and its counterpart with the "Old" suffix to show the changes. Note that the `EditedBy` and `LastDateEdited` columns are also added.

![](/images/L-Dev-ChangelogDataSave/SPChangeLog2.png)
<br>

### Merge Update

The only thing to add in the Merge Update section is the additional 3 columns that were added to the targeted table [previously](#setting-up-the-tables): `LastDateEdited`, `EditedBy`, `UpdateTypeCode`.

![](/images/L-Dev-ChangelogDataSave/SPMergeUpdate.png)
<br>

### Merge Insert

Again, add the 3 additional columns in the Merge Insert section.

![](/images/L-Dev-ChangelogDataSave/SPMergeInsert.png)
<br>

### Merge Output

The output of the Merge will need to add all the additional columns that were added to the `@ChangeLog` table [previously](#changelog). This will make it possible to transfer these values to the history table [later](#update-history-table).

![](/images/L-Dev-ChangelogDataSave/SPMergeOutput.png)
<br>

### Update Target Table

Now that all the changes have been correctly recorded in the `@ChangeLog` table, we need to sync the `UpdateTypeCode` from the `@ChangeLog` table to the target table. For more information on why this is necessary, see [here](/wDeveloper/L-Dev-InsertDeleteDataSave.html#update-changelog).

![](/images/L-Dev-ChangelogDataSave/SPUpdateTable.png)
<br>

### Update History Table

The last thing to change is to add all the changes that took place, which are recorded in the `@ChangeLog` table, to the history table. Add the following section after the previous section:

![](/images/L-Dev-ChangelogDataSave/SPInsertHistory.png)
<br>

### Final Stored Procedure

Now that the Stored Procedure is finished, execute it to save it.

The following is the finished SP:

<button class = "collapsible"> NorthwindChangelogDataSaveSP </button>
<div markdown="1" class="panel">

```sql
CREATE OR ALTER   PROC [dbo].[NorthwindChangelogDataSaveSP]

	-- System Params not in formula
	@Interject_RequestContext nvarchar(max)
	,@TestMode bit = 0 -- used only for testing the stored procedure directly.  It will show more results when set to 1.
	
AS

/*
==================================================================================
	CREATED DATE: 3/7/2023 8:22 AM
	CREATED BY: Interject Default
	DESCRIPTION: Example data pull to be used with Interject
	
	---------------------------------------------------------------------------
	TEST Example: Use the below to test this stored procedure:
	---------------------------------------------------------------------------
	
	This section has been removed. To get sample code for testing this stored procedure,
	select the cell in Excel containing the ReportSave function. Then click on the Interject 
	ribbon, click System > View SQL Test For ActiveCell.

	---------------------------------------------------------------------------
	Validation Example:
	---------------------------------------------------------------------------
	Note: By adding 'UserNotice:' to the error message, Interject will show the message in an alert box and not flag the formula with an error.
	Without it, the formula will show an error with the text the user can click into.
	
	IF @ParameterName = 'TheWrongValue'
	BEGIN
		RAISERROR ('UserNotice:You selected an invalid value. Unable to continue.',
		18, -- Severity,
		1) -- State)
		
		RETURN
	END
	
	---------------------------------------------------------------------------
	Reserved Parameters:
	---------------------------------------------------------------------------
	Note: If the below parameters are added to your stored procedure and to the
	data portal parameter list, Interject will pass the related value automatically.
	
	@Interject_XMLDataToSave varchar(max) - Required for saving data. It contains XML for the designated cells values.
	@Interject_ColDefItems  varchar(max) - Provides the Column Definitions in XML designated within the report formula.
	@Interject_RowDefItems varchar(max) - Provides the Row Definitions in XML designated within the report formula.
	@Interject_SourceFileAndPath varchar(500) - Provides the path and file name delimited by '|' of the current file.
	@Interject_SourceFilePathAndTab varchar(1000) - Provides the path, file name and active tab name delimited by '|' of the current file.
	@Interject_LocalTimeZoneOffset money - Provides a number (0.000) that represents the offset of the users time to UTC time.
	@Interject_NTLogin varchar(50) - Provides the user's computer login name for their current session.
	@Interject_UserID varchar(50) - Provides the Interject User ID for their current session.
	@Interject_LoginName varchar(50) - Provides the Interject Full name for their current session.
	@Interject_ExcelVersion varchar(50) - Provides the users Excel version.
	@Interject_UserRoles varchar(1000) - Provides the Interject roles assigned to the user.
	@Interject_ClientID varchar(50) - Provides the Interject Client ID for their current session.
	@Interject_ReturnError varchar(2000) - Is an output parameter that can be used to return an error back to the user. Pass empty string for no error.
	@Interject_RequestContext nvarchar(max) - Provides all above request context and both the open text and encrypted version of the user context.

==================================================================================
*/

	--
	-- Use helper to extract data from Interject_RequestContext. Remove items that are not needed
	-- The helper stored procedure [dbo].[RequestContext_Parse] is required for this section to function 
	--
	
	DECLARE
		@ExcelVersion					NVARCHAR(100)
		,@IdsVersion					NVARCHAR(100)	
		,@FileName					NVARCHAR(1000)	
		,@FilePath					NVARCHAR(1000)
		,@TabName						NVARCHAR(1000)	
		,@CellRange					NVARCHAR(100)	
		,@SourceFunction				NVARCHAR(100)	
		,@UtcOffset					DECIMAL(6,4)	
		,@ColDefItemsDelimited			xml	
		,@ResultDefItemsDelimited		xml	
		,@RowDefItemsDelimited			xml
		,@MachineLoginName				NVARCHAR(100)
		,@MachineName					NVARCHAR(100)	
		,@Interject_UserID				NVARCHAR(100)
		,@Interject_ClientID			NVARCHAR(100)
		,@Interject_LoginName			NVARCHAR(100)	
		,@Interject_LoginAuthTypeID		INT		
		,@Interject_LoginDateUTC		     DATETIME
		,@Interject_UserRolesDelimited	NVARCHAR(max)
		,@UserContextEncrypted			NVARCHAR(4000)
		,@Interject_XMLDataToSave	     xml	
	
	EXEC [dbo].[RequestContext_Parse]
		@Interject_RequestContext		 = @Interject_RequestContext
		,@ExcelVersion					 = @ExcelVersion				OUTPUT
		,@IdsVersion					 = @IdsVersion					OUTPUT
		,@FileName					 = @FileName					OUTPUT
		,@FilePath					 = @FilePath					OUTPUT
		,@TabName						 = @TabName					OUTPUT
		,@CellRange					 = @CellRange			  		OUTPUT
		,@SourceFunction				 = @SourceFunction		  		OUTPUT
		,@UtcOffset					 = @UtcOffset		   			OUTPUT
		,@ColDefItemsDelimited			 = @ColDefItemsDelimited			OUTPUT
		,@ResultDefItemsDelimited		 = @ResultDefItemsDelimited		OUTPUT
		,@RowDefItemsDelimited			 = @RowDefItemsDelimited			OUTPUT
		,@MachineLoginName				 = @MachineLoginName			OUTPUT
		,@MachineName					 = @MachineName				OUTPUT
		,@Interject_UserID				 = @Interject_UserID			OUTPUT
		,@Interject_ClientID			 = @Interject_ClientID			OUTPUT
		,@Interject_LoginName			 = @Interject_LoginName			OUTPUT
		,@Interject_LoginAuthTypeID		 = @Interject_LoginAuthTypeID		OUTPUT
		,@Interject_LoginDateUTC			 = @Interject_LoginDateUTC		OUTPUT
		,@Interject_UserRolesDelimited	 = @Interject_UserRolesDelimited	OUTPUT
		,@UserContextEncrypted			 = @UserContextEncrypted			OUTPUT
		,@Interject_XMLDataToSave		 = @Interject_XMLDataToSave		OUTPUT
	
	IF @TestMode = 1
	BEGIN
		SELECT
			@ExcelVersion					as '@ExcelVersion'
			,@IdsVersion					as '@IdsVersion'
			,@FileName					as '@FileName'
			,@FilePath					as '@FilePath '
			,@TabName						as '@TabName'
			,@CellRange					as '@CellRange'
			,@SourceFunction				as '@SourceFunction'
			,@UtcOffset					as '@UtcOffset'
			,@ColDefItemsDelimited			as '@ColDefItemsDelimited'
			,@ResultDefItemsDelimited		as '@ResultDefItemsDelimited'
			,@RowDefItemsDelimited			as '@RowDefItemsDelimited'
			,@MachineLoginName				as '@MachineLoginName'
			,@MachineName					as '@MachineName'
			,@Interject_UserID				as '@Interject_UserID'
			,@Interject_ClientID			as '@Interject_ClientID'
			,@Interject_LoginName			as '@Interject_LoginName'
			,@Interject_LoginAuthTypeID		as '@Interject_LoginAuthTypeID'
			,@Interject_LoginDateUTC			as '@Interject_LoginDateUTC'
			,@Interject_UserRolesDelimited	as '@Interject_UserRolesDelimited'
			,@UserContextEncrypted			as '@UserContextEncrypted'
			,@Interject_XMLDataToSave		as '@Interject_XMLDataToSave'
	END

	DECLARE @ErrorMessageToUser as varchar(1000) = ''
	
	--
	-- PROCESS THE XML DATA INTO TABLE VARIABLE
	-- varchar(max) is used for the data type by default.  Please change for the specific requirement.
	--

	DECLARE @DataToProcess TABLE
	(
		-- the below are system values used internally in this stored procedures
		 [_ExcelRow] INT 
		,[_MessageToUser] VARCHAR(500) DEFAULT('')
		-- Below are your columns expected from the spreadsheet that is calling this save stored procedure
		-- Please change the (max) to the expected length of the text input.  If limiting length, be sure to make the size larger than allowed so you can add validation to notify the user
	
		,[CustomerID] NCHAR(5)
		,[CompanyName] NVARCHAR(30)
		,[ContactName] NVARCHAR(30)
		,[ContactTitle] NVARCHAR(30)
		,[Phone] NVARCHAR(24)
		,[Phone_Int] INT
		,[City] NVARCHAR(15)
		,[Country] NVARCHAR(15)
		,[ToBeDeleted] NVARCHAR(10)
		,[ToBeDeletedBit] BIT DEFAULT(0)
	)

	IF DATALENGTH(@Interject_XMLDataToSave) > 0 
	BEGIN
		declare @DataToProcessXML as XML
		-- Handle conversion of XML text into an XML variable.  
		BEGIN TRY
			SET @DataToProcessXML = CAST(@Interject_XMLDataToSave as XML)
		END TRY
		BEGIN CATCH
			SET @ErrorMessageToUser = 'Error in Parsing XML from Interject.  Error: ' + ERROR_MESSAGE()
			GOTO FinalResponseToUser
		END CATCH
		
		-- Insert the XML into the table variable for further processing
		INSERT into @DataToProcess(
		    [_ExcelRow]
		    ,[CustomerID]
		    ,[CompanyName]
		    ,[ContactName]
		    ,[ContactTitle]
		    ,[Phone]
		    ,[City]
		    ,[Country]
		    ,[ToBeDeleted]
		)
		SELECT
			-- The below row value is always provided by Interject
			T.c.value('./Row[1]', 'INT') as [_ExcelRow]
			-- The below columns are provided based on your column definitions in the ReportSave() function
			,T.c.value('./CustomerID[1]', 'NCHAR(5)') as [CustomerID]
			,T.c.value('./CompanyName[1]', 'NVARCHAR(30)') as [CompanyName]
			,T.c.value('./ContactName[1]', 'NVARCHAR(30)') as [ContactName]
			,T.c.value('./ContactTitle[1]', 'NVARCHAR(30)') as [ContactTitle]
			,T.c.value('./Phone[1]', 'NVARCHAR(24)') as [Phone]
			,T.c.value('./City[1]', 'NVARCHAR(15)') as [City]
			,T.c.value('./Country[1]', 'NVARCHAR(15)') as [Country]
			,T.c.value('./Delete[1]', 'NVARCHAR(10)') as [ToBeDeleted]
		FROM @DataToProcessXML.nodes('/XMLDataToSave/r') T(c)
	END
	
	-- TestMode is provided so a test save can be executed and all related data can be 
	-- easily viewed for testing while not effecting any data in the database
	IF @TestMode =1 
	BEGIN
		SELECT '@DataToProcess - After XML Processing' as ResultName
		SELECT * FROM @DataToProcess
	END
	
	UPDATE @DataToProcess 
		SET [ToBeDeletedBit] = 1
	WHERE [ToBeDeleted] = 'yes'
	
	--
	-- VALIDATION SECTION - Ensure inputs received from Excel are valid
	--

	-- Validate that the details do not have duplicates on the primary key
	UPDATE m
	SET [_MessageToUser] = [_MessageToUser] + ', Duplicate key'
	FROM @DataToProcess m
	INNER JOIN
		(
			SELECT [CustomerID] 
			FROM @DataToProcess
			WHERE [CustomerID] <> ''
			GROUP BY [CustomerID]
			HAVING COUNT(1) > 1
		) as t
		ON
			m.CustomerID = t.CustomerID
	
	-- Now check if there were any validation issues in the detail and stop processing if true
	IF EXISTS(SELECT 1 FROM @DataToProcess WHERE [_MessageToUser] <> '')
	BEGIN
		SET @ErrorMessageToUser = 'There were errors in the details of your input.  Please review the errors noted in each row.'
		GOTO FinalResponseToUser
	END
 
	--
	-- DATA UPDATE
	--

	BEGIN TRY
	   DECLARE @CurrentDateTime DATETIME2 = GETUTCDATE()
		
		-- this table variable will log the changes to the target table so it can be used
		-- to return helpful feedback to the user about how the save action resulted
		DECLARE @ChangeLog as TABLE
		(
			 --[ChangeLogID] INT IDENTITY(1,1) NOT NULL
			[_ExcelRow] INT	-- will capture the source row that affected the target table
			,[UpdateTypeCode] VARCHAR(10)  -- Will show UPDATE, INSERT, or DELETE
			,[CustomerID] NCHAR(5)
			,[CompanyName] NVARCHAR(40)
			,[CompanyNameOld] NVARCHAR(40)
			,[ContactName] NVARCHAR(30)
			,[ContactNameOld] NVARCHAR(30)
			,[ContactTitle] NVARCHAR(30)
			,[ContactTitleOld] NVARCHAR(30)
			,[Phone] NVARCHAR(24)
			,[PhoneOld] NVARCHAR(24)
			,[City] NVARCHAR(15)
			,[CityOld] NVARCHAR(15)
			,[Country] NVARCHAR(15)
			,[CountryOld] NVARCHAR(15)
			,[EditedBy] NVARCHAR(40) NOT NULL
			,[LastDateEdited] DATETIME2(7) NOT NULL
			,[IsDeleted] BIT
			,[IsDeletedOld] BIT
		)
		
		BEGIN TRAN t1
			--
			--  use MERGE statement that UPDATES and INSERTS in one action
			--
			MERGE dbo.Northwind_Customers t -- t = the target table or view to update
			USING (
				SELECT
				    [_ExcelRow]
				    ,[CustomerID]
				    ,[CompanyName]
				    ,[ContactName]
				    ,[ContactTitle]
				    ,[Phone]
				    ,[City]
				    ,[Country]
				    ,[ToBeDeleted]
				    ,[ToBeDeletedBit]
				FROM @DataToProcess 
			) s -- s = the source data to be used to update the target table
			-- the join on the column keys is specified below
			ON 
				s.[CustomerID] = t.[CustomerID]
				
			WHEN MATCHED -- Handles the update based on INNER JOIN
				AND NOT 
				(
				 -- To ensure only changes are captured
					s.[CompanyName] = t.[CompanyName]
					AND
					s.[ContactName] = t.[ContactName]
					AND
					s.[ContactTitle] = t.[ContactTitle]
					AND
					s.[Phone] = t.[Phone]
					AND
					s.[City] = t.[City]
					AND
					s.[Country] = t.[Country]
					AND
					s.[ToBeDeletedBit] = t.[IsDeleted]
				)
				THEN
				UPDATE SET
				      t.[CompanyName] = s.[CompanyName]
					,t.[ContactName] = s.[ContactName]
					,t.[ContactTitle] = s.[ContactTitle]
					,t.[Phone] = s.[Phone]
					,t.[City] = s.[City]
					,t.[Country] = s.[Country]
					,t.[LastDateEdited] = @CurrentDateTime
					,t.[EditedBy] = @MachineLoginName
					,t.[UpdateTypeCode] = 'UPDATE'
					,t.[IsDeleted] = s.[ToBeDeletedBit]   

			 WHEN NOT MATCHED BY TARGET
				AND
				LOWER(s.[ToBeDeleted]) <> 'yes'
				THEN INSERT (
				    [CustomerID]
				    ,[CompanyName]
				    ,[ContactName]
				    ,[ContactTitle]
				    ,[Phone]
				    ,[City]
				    ,[Country]
				    ,[IsDeleted]
				    ,[EditedBy]
				    ,[UpdateTypeCode]
				    ,[LastDateEdited]
				)
				VALUES (
				    [CustomerID]
				    ,[CompanyName]
				    ,[ContactName]
				    ,[ContactTitle]
				    ,[Phone]
				    ,[City]
				    ,[Country]
				    ,0
				    ,@MachineLoginName
				    ,'INSERT'
				    ,@CurrentDateTime
				)
			-- the output captures the changes to the table and logs to a table variable
			OUTPUT 
				isnull(inserted.[CustomerID],deleted.[CustomerID])  -- include deleted in case delete is added later. Inserted is used for both Update an Insert
				,s.[_ExcelRow] 
				,$action as UpdateTypeCode  -- this logs into an a change log table variable
				,s.[CompanyName]
				,s.[ContactName]
				,s.[ContactTitle]
				,s.[Phone]
				,s.[City]
				,s.[Country]
				,deleted.[CompanyName]
				,deleted.[ContactName]
				,deleted.[ContactTitle]
				,deleted.[Phone]
				,deleted.[City]
				,deleted.[Country]
				,@MachineLoginName
				,@CurrentDateTime
				,inserted.[IsDeleted]
				,deleted.[IsDeleted] 
			INTO @ChangeLog
			(
				[CustomerID]
				,[_ExcelRow]
				,[UpdateTypeCode]
				,[CompanyName]
				,[ContactName]
				,[ContactTitle]
				,[Phone]
				,[City]
				,[Country]
				,[CompanyNameOld]
				,[ContactNameOld]
				,[ContactTitleOld]
				,[PhoneOld]
				,[CityOld]
				,[CountryOld]
				,[EditedBy]
				,[LastDateEdited]
				,[IsDeleted]
				,[IsDeletedOld]
			); 

		  UPDATE @ChangeLog
		  SET UpdateTypeCode = 'DELETE'
		  WHERE UpdateTypeCode = 'UPDATE'
			 AND [IsDeleted] = 1
			
		  UPDATE @ChangeLog 
		  SET UpdateTypeCode = 'ADDED_BACK'
		  WHERE UpdateTypeCode = 'UPDATE'
			 AND [IsDeleted] = 0
			 AND [IsDeletedOld] = 1

		  UPDATE [dbo].[Northwind_Customers]
		  SET [dbo].[Northwind_Customers].UpdateTypeCode = cl.UpdateTypeCode
		  FROM [dbo].[Northwind_Customers] nc
		  INNER JOIN @ChangeLog cl
		  ON nc.CustomerID = cl.CustomerID
	   
    		  IF @TestMode = 1
			BEGIN
			SELECT * FROM dbo.Northwind_Customers
			END

			 -- Export the ChangeLog records to the History table
			 INSERT INTO dbo.Northwind_Customers_History (
				[CustomerID]
				,[CompanyName]
				,[CompanyNameOld]
				,[ContactName]
				,[ContactNameOld]
				,[ContactTitle]
				,[ContactTitleOld]
				,[Phone]
				,[PhoneOld]
				,[City]
				,[CityOld]
				,[Country]
				,[CountryOld]
				,[EditedBy]
				,[ActionType]
				,[DateEdited]
			 )
			 SELECT
				cl.[CustomerID]
				,cl.[CompanyName]
				,cl.[CompanyNameOld]
				,cl.[ContactName]
				,cl.[ContactNameOld]
				,cl.[ContactTitle]
				,cl.[ContactTitleOld]
				,cl.[Phone]
				,cl.[PhoneOld]
				,cl.[City]
				,cl.[CityOld]
				,cl.[Country]
				,cl.[CountryOld]
				,cl.[EditedBy]
				,cl.[UpdateTypeCode]
				,cl.[LastDateEdited]
			 FROM @ChangeLog cl
			 WHERE cl.UpdateTypeCode IS NOT NULL

			--now we have enough information to update the message to user for each row
			UPDATE dtp
			SET [_MessageToUser] = 
				CASE cl.UpdateTypeCode
					WHEN 'ADDED_BACK' THEN ', Added!'
					WHEN 'DELETE' THEN ', Deleted!'
					WHEN 'UPDATE' THEN ', Updated!'
					WHEN 'INSERT' THEN ', Inserted!'
					--ELSE ', No change'  -- not used in this example
				END 
			FROM @DataToProcess dtp
				INNER JOIN @ChangeLog cl  -- use Left Join if 'No Change' is to be identified
					 ON dtp.[_ExcelRow] = cl.[_ExcelRow]
				
		IF @TestMode = 1
		BEGIN
			SELECT '@ChangeLog- Show log of changes made' as ResultName
			select * from @ChangeLog
			
			ROLLBACK TRAN t1 -- note this does not roll back changes to table variables, only real tables
			SELECT 'Changes rolled back since in TEST mode!' as TestModeNote
		END
		ELSE
		BEGIN
			COMMIT TRAN t1
		END
	END TRY
	BEGIN CATCH
		IF @@TRANCOUNT > 0
			ROLLBACK TRAN t1
		
		SET @ErrorMessageToUser =  ERROR_MESSAGE()
		GOTO FinalResponseToUser
	END CATCH
	
FinalResponseToUser:
--
-- PROVIDE RESPONSE TO THE SAVE ACTION
--
	
	-- if test mode, show the final table 
	IF @TestMode = 1 
	BEGIN
		SELECT '@DataToProcess - After Validation' as ResultName
		SELECT * FROM @DataToProcess
	END
	
	-- return the recordset results back to the spreadsheet, if needed.
	SELECT
		[_ExcelRow] as [Row] -- this relates to the original row of the spreadsheet the data came from
		,SUBSTRING([_MessageToUser],3,1000) as [MessageToUser]  -- This is a field that, if it matches a column in the Results Range, will be placed in that column for the specified row
	FROM @DataToProcess
	
	-- if there is an error, raise error and Interject will catch and present to the user.
	-- Note that this is specifically done after the above resultset is returned, since initiating an error before
	-- will not allow a result set to be returned to provide feedback on each row 
	IF @ErrorMessageToUser <> ''
	BEGIN
		-- by adding 'UserNotice:' as a prefix to the message, Interject will not consider it a unhandled error 
		-- and will present the error to the user in a message box.
		SET @ErrorMessageToUser = 'UserNotice:' + @ErrorMessageToUser
		
		RAISERROR (@ErrorMessageToUser,
		18, -- Severity,
		1) -- State)
		RETURN
	END
```
</div>

## Testing the Stored Procedure

Interject provides a convenient way to get SQL code that will test your SP right from within the Excel report. First select the cell in the Excel report containing the ReportSave function. Then on the [Advanced Menu](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#overview), click on "View SQL Test For ActiveCell" on the "System" dropdown:

![](/images/L-Dev-ChangelogDataSave/ViewSQLTestClick.png)
<br>

Copy the test code to the clipboard:

![](/images/L-Dev-ChangelogDataSave/CopyTestCode.png)
<br>

Paste the code into a new query and be sure to add the "@TestMode = 1" parameter to print out additional information about the SP process:

![](/images/L-Dev-ChangelogDataSave/PasteTestCode.png)
<br>

Make some changes to the data:

![](/images/L-Dev-ChangelogDataSave/ExecuteTestCode.png)
<br>

After execution, you should see the messages showing what was changed:

![](/images/L-Dev-ChangelogDataSave/TestCodeExecuted.png)
<br>

## Testing the ReportSave

The only thing left to do is test the SP by running the ReportSave function within the Excel report.

Next make some changes and run the Report Save:

![](/images/L-Dev-ChangelogDataSave/TestingTheReportChanges.png)
<br>

Notice the results!:

![](/images/L-Dev-ChangelogDataSave/TestingTheReportResults.png)
<br>
