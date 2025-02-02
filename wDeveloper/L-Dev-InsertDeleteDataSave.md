---
title: "Develop: Insert &amp; Delete Data Save"
filename: "L-Dev-InsertDeleteDataSave.md"
layout: custom
keywords: [developer, example, walkthrough, SQL, SSMS, Data Portal, data connection, data save, insertions, deletions]
headings: ["Overview", "Setting Up the Data Connection", "Setting Up the Data Portal", "Setting Up the Report", "Setting Up the Soft Delete", "Setting Up the Stored Procedure", "Modifying the Stored Procedure", "Data to Process", "Inserting the Data to Process", "Update DataToProcess", "ChangeLog", "Merge Select", "Merge Update", "Merge Insert", "Merge Output", "Update ChangeLog", "Set Message To User", "Final Stored Procedure", "Testing the Stored Procedure", "Testing the ReportSave"]
links: ["/wDeveloper/L-Dev-EditingDataSave.html", "#setting-up-the-data-connection", "/wDeveloper/L-Dev-CustomerAging.html#setting-up-the-data-connection", "#setting-up-the-data-portal", "#setting-up-the-report", "#setting-up-the-soft-delete", "#setting-up-the-stored-procedure", "#testing-the-stored-procedure", "https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/downloading-sample-databases", "https://docs.gointerject.com/wLabs/LabSetup.html#step-1-setting-up-the-database", "/wDeveloper/L-Dev-CustomerAging.html#setting-up-the-data-connection", "https://portal.gointerject.com", "/wPortal/Logging-In-to-Website-Portal.html", "https://docs.gointerject.com/wDeveloper/L-Dev-InsertDeleteDataSave.html#setting-up-the-stored-procedure", "/wDeveloper/Request-Context-Parse.html", "/wDeveloper/L-Dev-EditingDataSave.html#setting-up-the-report", "/wDeveloper/L-Dev-CustomerAging.html#creating-the-stored-procedure", "/wDeveloper/L-Dev-EditingDataSave.html#final-stored-procedure", "https://docs.gointerject.com/wDeveloper/L-Dev-InsertDeleteDataSave.html#testing-the-stored-procedure", "#setting-up-the-report", "#merge-insert", "#data-to-process", "#update-changelog", "#setting-up-the-soft-delete", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#overview"]
image_dir: "L-Dev-InsertDeleteDataSave"
images: [
	{file: "NewDataPortal", type: "png", site: "Portal", cat: "Data Portals", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "DataPortalDetails", type: "png", site: "Portal", cat: "Data Portals", sub: "Details", report: "", ribbon: "", config: ""}, 
	{file: "AddSystemParameter", type: "png", site: "Portal", cat: "Data Portals", sub: "Details", report: "", ribbon: "", config: ""}, 
	{file: "ChangeReportSaveFunction", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: "Yes"}, 
	{file: "AddColumnDefNames", type: "png", site: "Add-in", cat: "Report", sub: "", report: "", ribbon: "", config: "Yes"}, 
	{file: "AddDeleteColumn", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""}, 
	{file: "ClickDataValidation", type: "png", site: "Excel", cat: "Data Validation", sub: "Data Validation", report: "", ribbon: "", config: ""}, 
	{file: "DataValidationWindow", type: "png", site: "Excel", cat: "Data Validation", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "EnterClear", type: "png", site: "Add-in", cat: "Report", sub: "", report: "", ribbon: "", config: "Yes"}, 
	{file: "AddIsDeletedToPullSP", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SPDataToProcess", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SPInsertToDataToProcess", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SPUpdateDataToProcess", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SPChangeLog", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SPMergeSelect", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SPMergeUpdate", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SPMergeInsert", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SPOutput2", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SPUpdateChangeLog", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SPSetMessageToUser", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "ViewSQLTestClick", type: "png", site: "Add-in", cat: "Ribbon", sub: "System", report: "", ribbon: "", config: "Yes"}, 
	{file: "CopyTestCode", type: "png", site: "Add-in", cat: "View SQL Test For ActiveCell", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "PasteTestCode", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "ExecuteTestCode", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "TestCodeExecuted", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "TestingTheReportChanges", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""}, 
	{file: "TestingTheReportResults", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""}
	]
description: In this example you will modify the Editing Data Save using the Customer Aging Detail report and the Northwind Customers data source to add or delete a customer.
---
* * *

## Overview

In this example you will modify the previous [Editing Data Save](/wDeveloper/L-Dev-EditingDataSave.html), which was set up to edit a customer's contact name and title. In this Insert &amp; Delete Data Save, you will walkthrough the steps to edit all the columns. In addition, you will also include the ability to insert or delete a customer from within the Excel report.

<blockquote class=highlight_note>
<b>Note:</b> The Customer Aging Report used in this example is a report that displays a customer's outstanding balances. It is not normally used to edit, insert, or delete a customer directly. However, for this walkthrough demonstration purpose, you will modify the report in order to do so.
</blockquote>
<br>

This walkthrough involves 6 main steps:

1. [Set up a Data Connection](#setting-up-the-data-connection) ([completed already](/wDeveloper/L-Dev-CustomerAging.html#setting-up-the-data-connection))
2. [Set up a Data Portal](#setting-up-the-data-portal)
3. [Setting up the report to handle the save](#setting-up-the-report)
4. [Setting up the soft delete](#setting-up-the-soft-delete)
5. [Set up the Stored Procedure (SP) to handle the save](#setting-up-the-stored-procedure)
6. [Test the Stored Procedure &amp; ReportSave](#testing-the-stored-procedure)

<br>

<blockquote class=highlight_note>
<b>Note:</b> This example uses Microsoft's <a href="https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/downloading-sample-databases">Northwind Database</a>. To download a minimized copy of the Northwind database for use in these labs, see <a href="https://docs.gointerject.com/wLabs/LabSetup.html#step-1-setting-up-the-database">here</a>.
</blockquote>

## Setting Up the Data Connection

For the Data Connection for this example, you will use the connection previously set up [here](/wDeveloper/L-Dev-CustomerAging.html#setting-up-the-data-connection).

## Setting Up the Data Portal

**Step 1:** Navigate to [https://portal.gointerject.com](https://portal.gointerject.com) and [log in](/wPortal/Logging-In-to-Website-Portal.html). Click on **Data Portals** on the left side bar and then the **NEW DATA PORTAL** button.

![](/images/L-Dev-InsertDeleteDataSave/NewDataPortal.png)
<br>

**Step 2:** Enter the following details on setting up the new data portal and click "**CREATE DATA PORTAL**".

* **Data Portal Code:** NorthwindInsertDeleteDataSave
* **Description:** Data portal for insert and delete data save
* **Category:** Demo
* **Connection:** NorthwindExampleDB_MyName (replace "MyName" with your name)
* **Command Type:** Stored Procedure
* **Stored Procedure/Command:** NorthwindInsertDeleteDataSaveSP

<blockquote class=highlight_note>
<b>Note:</b> You will create the "NorthwindInsertDeleteDataSaveSP" Stored Procedure <a href="https://docs.gointerject.com/wDeveloper/L-Dev-InsertDeleteDataSave.html#setting-up-the-stored-procedure">later</a>
</blockquote>
<br>

![](/images/L-Dev-InsertDeleteDataSave/DataPortalDetails.png)
<br>

**Step 3:** After creating the data portal, scroll down and click **Click here to add a System Parameter** and ensure the **Interject_RequestContext** parameter is set.

![](/images/L-Dev-InsertDeleteDataSave/AddSystemParameter.png)
<br>

The System Parameter [Interject_RequestContext](/wDeveloper/Request-Context-Parse.html) will transfer contextual data to the Stored Procedure you will set up later. In this example you will not need this info but it is a good practice to set this parameter for all your Stored Procedures.

## Setting Up the Report

Begin by opening up the report that was completed in the [previous data save](/wDeveloper/L-Dev-EditingDataSave.html#setting-up-the-report). You will modify this report to set up the Insert &amp; Delete Data Save.

**Step 1:** First click on the cell containing the ReportSave function and change it to match the Data Portal you just set up:

![](/images/L-Dev-InsertDeleteDataSave/ChangeReportSaveFunction.png)
<br>

**Step 2:** Next add the **CompanyName**, **Phone**, **City**, **Country** and **Delete** to the "Column Definition - Save" configuration row so that this data will be saved to the data source:

![](/images/L-Dev-InsertDeleteDataSave/AddColumnDefNames.png)
<br>

**Step 3:** Next you will add a **Delete?** column to the report. This way if there is a "Yes" marked in this column, the record for that row will be deleted. This prevents the accidental deletion of records if they are missing from the report:

![](/images/L-Dev-InsertDeleteDataSave/AddDeleteColumn.png)
<br>

Highlight the cells on the new **Delete?** column and click **Data Validation** to bring up the Data Validation window:

![](/images/L-Dev-InsertDeleteDataSave/ClickDataValidation.png)
<br>

For the Validation criteria, click on **List** for the Allow field and enter **Yes** for the Source:

![](/images/L-Dev-InsertDeleteDataSave/DataValidationWindow.png)
<br>

**Step 4:** Finally, enter **\[clear]** into cell N2 in order for the entries in the Delete column to be cleared out on a pull.

![](/images/L-Dev-InsertDeleteDataSave/EnterClear.png)
<br>

That's it. The report is now ready to add, delete, or update a customer.

## Setting Up the Soft Delete

There are two main ways to delete a record from a database: a hard delete and a soft delete. A hard delete simply removes the record from the database altogether. A soft delete simply flags the record as deleted. This approach is preferable over a hard delete because you can recover the data easily by switching the flag. The example in this data save uses a soft delete. In order to implement this, you will need to set up a column in the targeted data table that will store a `IsDeleted` BIT value to distinguish which records have been soft deleted.

**Step 1:** Execute the following SQL to add a `IsDeleted` column to the table that you are saving to:

```sql
ALTER TABLE dbo.Northwind_Customers
ADD IsDeleted BIT
```

**Step 2:** Now that the new column has been added, you need to set all the existing values to 0. Execute the following SQL on the same table:

```sql
UPDATE dbo.Northwind_Customers SET IsDeleted = 0
```

**Step 3:** Next, since you don't want to allow nulls for this flag, set the `IsDeleted` column to "Not Null" by executing the following SQL:

```sql
ALTER TABLE dbo.Northwind_Customers
ALTER COLUMN IsDeleted BIT NOT NULL
```

**Step 4:** Lastly, in order to only pull records that are not deleted, you will need to add the following line to the Stored Procedure [previously set up](/wDeveloper/L-Dev-CustomerAging.html#creating-the-stored-procedure) that pulls the data for this report:

![](/images/L-Dev-InsertDeleteDataSave/AddIsDeletedToPullSP.png)
<br>

## Setting Up the Stored Procedure

Next you will created a new Stored Procedure that builds from the [previous save](/wDeveloper/L-Dev-EditingDataSave.html#final-stored-procedure). To make this easier, simply copy the SP into a new query, change the command to "CREATE OR ALTER PROC NorthwindInsertDeleteDataSaveSP" and execute it to save it. Then you can begin making modifications to it. For your convenience, the SP is posted here.

<blockquote class=highlight_note>
<b>Note:</b> The code for testing the SP has been removed. It will be handled <a href="https://docs.gointerject.com/wDeveloper/L-Dev-InsertDeleteDataSave.html#testing-the-stored-procedure">later</a>
</blockquote>
<br>

<button class = "collapsible"> NorthwindInsertDeleteDataSaveSP </button>
<div markdown="1" class="panel">

```sql
CREATE OR ALTER PROC [dbo].[NorthwindInsertDeleteDataSaveSP]

	-- System Params not in formula
	@Interject_RequestContext nvarchar(max)
	,@TestMode bit = 0 -- used only for testing the stored procedure directly. It will show more results when set to 1.

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
		,@FileName						NVARCHAR(1000)
		,@FilePath						NVARCHAR(1000)
		,@TabName						NVARCHAR(1000)
		,@CellRange						NVARCHAR(100)
		,@SourceFunction				NVARCHAR(100)
		,@UtcOffset						DECIMAL(6,4)
		,@ColDefItemsDelimited			xml
		,@ResultDefItemsDelimited		xml
		,@RowDefItemsDelimited			xml
		,@MachineLoginName				NVARCHAR(100)
		,@MachineName					NVARCHAR(100)
		,@Interject_UserID				NVARCHAR(100)
		,@Interject_ClientID			NVARCHAR(100)
		,@Interject_LoginName			NVARCHAR(100)
		,@Interject_LoginAuthTypeID		INT
		,@Interject_LoginDateUTC		DATETIME
		,@Interject_UserRolesDelimited	NVARCHAR(max)
		,@UserContextEncrypted			NVARCHAR(4000)
		,@Interject_XMLDataToSave		xml
	
	EXEC [dbo].[RequestContext_Parse]
		@Interject_RequestContext		= @Interject_RequestContext
		,@ExcelVersion					= @ExcelVersion					OUTPUT
		,@IdsVersion					= @IdsVersion					OUTPUT
		,@FileName						= @FileName						OUTPUT
		,@FilePath						= @FilePath						OUTPUT
		,@TabName						= @TabName						OUTPUT
		,@CellRange						= @CellRange					OUTPUT
		,@SourceFunction				= @SourceFunction				OUTPUT
		,@UtcOffset						= @UtcOffset					OUTPUT
		,@ColDefItemsDelimited			= @ColDefItemsDelimited			OUTPUT
		,@ResultDefItemsDelimited		= @ResultDefItemsDelimited		OUTPUT
		,@RowDefItemsDelimited			= @RowDefItemsDelimited			OUTPUT
		,@MachineLoginName				= @MachineLoginName				OUTPUT
		,@MachineName					= @MachineName					OUTPUT
		,@Interject_UserID				= @Interject_UserID				OUTPUT
		,@Interject_ClientID			= @Interject_ClientID			OUTPUT
		,@Interject_LoginName			= @Interject_LoginName			OUTPUT
		,@Interject_LoginAuthTypeID		= @Interject_LoginAuthTypeID	OUTPUT
		,@Interject_LoginDateUTC		= @Interject_LoginDateUTC		OUTPUT
		,@Interject_UserRolesDelimited	= @Interject_UserRolesDelimited	OUTPUT
		,@UserContextEncrypted			= @UserContextEncrypted			OUTPUT
		,@Interject_XMLDataToSave		= @Interject_XMLDataToSave		OUTPUT
	
	IF @TestMode = 1
	BEGIN
		SELECT
			@ExcelVersion					as '@ExcelVersion'
			,@IdsVersion					as '@IdsVersion'
			,@FileName						as '@FileName'
			,@FilePath						as '@FilePath '
			,@TabName						as '@TabName'
			,@CellRange						as '@CellRange'
			,@SourceFunction				as '@SourceFunction'
			,@UtcOffset						as '@UtcOffset'
			,@ColDefItemsDelimited			as '@ColDefItemsDelimited'
			,@ResultDefItemsDelimited		as '@ResultDefItemsDelimited'
			,@RowDefItemsDelimited			as '@RowDefItemsDelimited'
			,@MachineLoginName				as '@MachineLoginName'
			,@MachineName					as '@MachineName'
			,@Interject_UserID				as '@Interject_UserID'
			,@Interject_ClientID			as '@Interject_ClientID'
			,@Interject_LoginName			as '@Interject_LoginName'
			,@Interject_LoginAuthTypeID		as '@Interject_LoginAuthTypeID'
			,@Interject_LoginDateUTC		as '@Interject_LoginDateUTC'
			,@Interject_UserRolesDelimited	as '@Interject_UserRolesDelimited'
			,@UserContextEncrypted			as '@UserContextEncrypted'
			,@Interject_XMLDataToSave		as '@Interject_XMLDataToSave'
	END

	DECLARE @ErrorMessageToUser as varchar(1000) = ''
	
	--
	-- PROCESS THE XML DATA INTO TABLE VARIABLE
	-- varchar(max) is used for the data type by default. Please change for the specific requirement.
	--

	DECLARE @DataToProcess TABLE
	(
		-- the below are system values used internally in this stored procedures
		 [_ExcelRow] INT
		,[_MessageToUser] VARCHAR(500) DEFAULT('')
		-- Below are your columns expected from the spreadsheet that is calling this save stored procedure
		-- Please change the (max) to the expected length of the text input. If limiting length, be sure to make the size larger than allowed so you can add validation to notify the user
	
		,[CustomerID] NCHAR(5)
		,[ContactName] NVARCHAR(30)
		,[ContactTitle] NVARCHAR(30)
	)

	IF DATALENGTH(@Interject_XMLDataToSave) > 0
	BEGIN
		declare @DataToProcessXML as XML
		-- Handle conversion of XML text into an XML variable.
		BEGIN TRY
			SET @DataToProcessXML = CAST(@Interject_XMLDataToSave as XML)
		END TRY
		BEGIN CATCH
			SET @ErrorMessageToUser = 'Error in Parsing XML from Interject. Error: ' + ERROR_MESSAGE()
			GOTO FinalResponseToUser
		END CATCH
		
		-- Insert the XML into the table variable for further processing
		INSERT into @DataToProcess(
			[_ExcelRow]
			-- The below columns are provided based on your column definitions in the ReportSave() function]
			,[CustomerID]
			,[ContactName]
			,[ContactTitle]

		)
		SELECT
			-- The below row value is always provided by Interject
			T.c.value('./Row[1]', 'INT') as [_ExcelRow]
			-- The below columns are provided based on your column definitions in the ReportSave() function
			,T.c.value('./CustomerID[1]', 'NCHAR(5)') as [CustomerID]
			,T.c.value('./ContactName[1]', 'NVARCHAR(30)') as [ContactName]
			,T.c.value('./ContactTitle[1]', 'NVARCHAR(30)') as [ContactTitle]
		FROM @DataToProcessXML.nodes('/XMLDataToSave/r') T(c)
	END
	
	-- TestMode is provided so a test save can be executed and all related data can be
	-- easily viewed for testing while not effecting any data in the database
	IF @TestMode =1
	BEGIN
		SELECT '@DataToProcess - After XML Processing' as ResultName
		SELECT * FROM @DataToProcess
	END
	
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
		SET @ErrorMessageToUser = 'There were errors in the details of your input. Please review the errors noted in each row.'
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
			,[UpdateTypeCode] VARCHAR(10) -- Will show UPDATE, INSERT, or DELETE
			,[CustomerID] NCHAR(5)
		)
		
		BEGIN TRAN t1
			--
			-- use MERGE statement that UPDATES, INSERTS, and DELETES in one action
			--
			MERGE dbo.Northwind_Customers t -- t = the target table or view to update
			USING (
				SELECT
					[_ExcelRow]
					,[CustomerID]
					,[ContactName]
					,[ContactTitle]
				FROM @DataToProcess
			) s -- s = the source data to be used to update the target table
			-- the join on the column keys is specified below
			ON
				s.[CustomerID] = t.[CustomerID]
				
			WHEN MATCHED -- Handles the update based on INNER JOIN
				AND NOT
				(
					s.[ContactName] = t.[ContactName] -- To ensure only changes are captured
					AND
					s.[ContactTitle] = t.[ContactTitle]
				)
				THEN
				UPDATE SET
					t.[ContactName] = s.[ContactName]
					,t.[ContactTitle] = s.[ContactTitle]
			--WHEN NOT MATCHED BY TARGET THEN -- Handles the insert based on LEFT JOIN -- NOT USED IN THIS EXAMPLE
			-- INSERT([ExampleColumnKey],[ExampleColumnValue])
			-- VALUES(s.ExampleColumnKey],s.[ExampleColumnValue])
			
			--WHEN NOT MATCHED BY SOURCE -- Handles the delete based on the RIGHT JOIN -- NOT USED IN THIS EXAMPLE
			-- AND... add restrictions so delete doesn't remove too much. Filter params are normally considered here.
			-- THEN
			-- DELETE
				
			-- the output captures the changes to the table and logs to a table variable
			OUTPUT
				isnull(inserted.[CustomerID],deleted.[CustomerID]) -- include deleted in case delete is added later. Inserted is used for both Update an Insert
				,s.[_ExcelRow]
				,$action as UpdateTypeCode -- this logs into an a change log table variable
			INTO @ChangeLog
			(
				[CustomerID]
				,[_ExcelRow]
				,[UpdateTypeCode]
			);
			
			--now we have enough information to update the message to user for each row
			UPDATE dtp
			SET [_MessageToUser] =
				CASE cl.UpdateTypeCode
					--WHEN 'INSERT' THEN ', Added!' -- not used in this example
					--WHEN 'DELETE' THEN ', Deleted' -- this will never match the excel side but can be used for other types of logging
					WHEN 'UPDATE' THEN ', Updated!'
					--ELSE ', No change' -- not used in this example
				END
			FROM @DataToProcess dtp
				INNER JOIN @ChangeLog cl -- use Left Join if 'No Change' is to be identified
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
		
		SET @ErrorMessageToUser = ERROR_MESSAGE()
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
		,SUBSTRING([_MessageToUser],3,1000) as [MessageToUser] -- This is a field that, if it matches a column in the Results Range, will be placed in that column for the specified row
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

### Data to Process

Since you are going to be saving more columns of data back to the data source, you need to add these columns to the @DataToProcess table. Be sure to match the data type of the table you will be saving the data to.

You will also add a `ToBeDeleted NVARCHAR` column to capture the new Delete column you added [previously](#setting-up-the-report). The `ToBeDeleted BIT` column is another column needed to be added. This column will be set to a default 0 (meaning not deleted). Both these columns will represent if the record should be deleted.

![](/images/L-Dev-InsertDeleteDataSave/SPDataToProcess.png)
<br>

### Inserting the Data to Process

Again, these additions are simply adding the additional columns so that they will be saved.

![](/images/L-Dev-InsertDeleteDataSave/SPInsertToDataToProcess.png)
<br>

### Update DataToProcess

This section will be added to store a BIT version of the `ToBeDeleted NVARCHAR` column in order for easier comparison [later](#merge-insert). 

![](/images/L-Dev-InsertDeleteDataSave/SPUpdateDataToProcess.png)
<br>

### ChangeLog

Add the following 2 columns to the `@ChangeLog` table. They will capture the changes from in the `IsDeleted` column.

![](/images/L-Dev-InsertDeleteDataSave/SPChangeLog.png)
<br>

### Merge Select

Next you will update the merge statement to include the additional columns to save:

![](/images/L-Dev-InsertDeleteDataSave/SPMergeSelect.png)
<br>

### Merge Update

The "WHEN MATCHED" section handles updates to the data. It needs to be updated to add the additional columns. In addition, you will need to select both `ToBeDeleted` columns that were added [earlier](#data-to-process).

![](/images/L-Dev-InsertDeleteDataSave/SPMergeUpdate.png)
<br>

### Merge Insert

Just after the previous section, you will add another section "WHEN NOT MATCHED BY TARGET". This will handle new insertions.

![](/images/L-Dev-InsertDeleteDataSave/SPMergeInsert.png)
<br>

### Merge Output

You will need to change the Merge Output to capture the changes in the `IsDeleted` column. The SQL Server keyword "inserted" captures what has been inserted with the Merge and "deleted" captures what was deleted. By included both values in the Output, you can determine how this column has changed. This will be required as explained in the next [section](#update-changelog).

![](/images/L-Dev-InsertDeleteDataSave/SPOutput2.png)
<br>

### Update ChangeLog

Because this SP is using a [soft delete](#setting-up-the-soft-delete), any time a record is "deleted", the Merge statement will actually see it as an update because it is simply changing the `IsDeleted` column. Similarly, when the record is added back, it is another update. Thus there are 4 types of actions: Update, Update "Deleted", Update "Added Back", and Insert. 

In order to distinguish between the different types of updates, you will need to change the UpdateTypeCode in the `@ChangeLog` table based on `IsDeleted` column. After the Output statement, add the following 2 update statements to set the correct type of action statement:

![](/images/L-Dev-InsertDeleteDataSave/SPUpdateChangeLog.png)
<br>

### Set Message To User

The last piece of code that needs to be changed is setting the message to the user. You will simply add a few cases to handle the "Added Back", "Deleted", and "Inserted" cases:

![](/images/L-Dev-InsertDeleteDataSave/SPSetMessageToUser.png)
<br>

### Final Stored Procedure

Now that the Stored Procedure is finished, execute it to save it.

The following is the finished SP:

<button class = "collapsible"> NorthwindInsertDeleteDataSaveSP </button>
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

## Testing the Stored Procedure

Interject provides a convenient way to get SQL code that will test your SP right from within the Excel report. First select the cell in the Excel report containing the ReportSave function. Then on the [Advanced Menu](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#overview), click on "View SQL Test For ActiveCell" on the "System" dropdown:

![](/images/L-Dev-InsertDeleteDataSave/ViewSQLTestClick.png)
<br>

Copy the test code to the clipboard:

![](/images/L-Dev-InsertDeleteDataSave/CopyTestCode.png)
<br>

Paste the code into a new query and be sure to add the "@TestMode = 1" line to print out additional information about the SP process:

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
