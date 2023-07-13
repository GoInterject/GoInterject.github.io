---
title: "Develop: Simple Data Save"
layout: custom
keywords: [developer, example, walkthrough, SQL, SSMS, dataportal, data connection, data save]
description: In this example you will create a simple data save using the Customer Aging Detail report and the Northwind Customers data source.
---

##  **Overview**

In this example you will build from the previous report where you built a [Data Pull](/wGetStarted/L-Dev-CustomerAging.html). Here, you will create a data portal to save the data using the Interject function [ReportSave](/wIndex/ReportSave.html). This function makes it convenient to modify the data source right inside of your Excel report without having to edit the data source directly.

For this simple Data Save, you will set up a save and modify the report to save a customer's contact name and title.

<blockquote class=highlight_note>
<b>Note:</b> This example uses Microsoft's Northwind Database. You can download this database <a href="https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/downloading-sample-databases">here</a> or you can use this example as a guide for your own data source.
</blockquote>

## Setting up the Data Connection

For the Data Connection for this example, you will use the connection previously set up [here](/wGetStarted/L-Dev-CustomerAging.html#setting-up-the-data-connection).

## Setting up the Data Portal

**Step 1:** Navigate to [ https://portal.gointerject.com ](https://portal.gointerject.com) and [ log in ](/wPortal/Logging-In-to-Website-Portal.html). Click on **Data Portals** on the left side bar and then the **NEW DATA PORTAL** button.

![](/images/L-Dev-SimpleDataSave/NewDataPortal.png)
<br>

**Step 2:** Enter the following details on setting up the new data portal and click "**CREATE DATA PORTAL**".

* **Data Portal Code:** NorthWindSimpleDataSave
* **Description:** Data portal for simple data save
* **Category:** Demo
* **Connection:** NorthWindExampleDB_MyName
* **Command Type:** Stored Procedure
* **Stored Procedure/Command:** NorthWindSimpleDataSaveSP

Note: You will create the "NorthWindSimpleDataSaveSP" Stored Procedure later.
<br>

![](/images/L-Dev-SimpleDataSave/DataPortalDetails.png)
<br>

**Step 3:** After creating the data portal, scroll down and click "**Click here to add a System Parameter**" and ensure the **Interject_RequestContext** parameter is set.

![](/images/L-Dev-SimpleDataSave/AddSystemParameter.png)
<br>

The System Parameter "Interject_RequestContext" will transfer contextual data to the Stored Procedure you will set up later. In this example you will not need this info but it is a good practice to set this parameter for all your Stored Procedures. In addition, the auto generated template that will be used in this example uses this parameter.

## Setting up the Report

Begin by opening up the report that was completed in the [Data Pull](/wGetStarted/L-Dev-CustomerAging.html#create-the-report). You will modify this report to set up the ReportSave.

**Step 1:** Ensure "Market" is entered as a Company Name filter and pull the data:

![](/images/L-Dev-SimpleDataSave/PullData.png)
<br>

**Step 2:** Unfreeze the panes (if they are frozen):

![](/images/L-Dev-SimpleDataSave/UnfreezePanes.png)
<br>

**Step 3:** Highlight the first two rows, right click within the selection and click **Copy**:

![](/images/L-Dev-SimpleDataSave/HighlightFirstTwoRows.png)
<br>

**Step 4:** Right click row 3 and click **Insert Copied Cells**:

![](/images/L-Dev-SimpleDataSave/InsertCopiedRows.png)
<br>

**Step 5:** Copy & paste the same 2 rows again this time by right clicking row 5 and  **Insert Copied Cells**:

![](/images/L-Dev-SimpleDataSave/InsertCopiedRowsAgain.png)
<br>

**Step 6:** Set up the configuration section:

1. Entering "\[clear]" in the last column (This will clear the messages when pulling)
1. Clear all values in row 4 except the "CustomerID", "ContactName" and "ContactTitle" (These are the column names that will be used to save to the data source)
1. Enter "MessageToUser" in the last column on row 6 (The save will return a message in this column if necessary)
1. Add a row below the row containing the **ReportRange** function (You will add the ReportSave function on this new row)

![](/images/L-Dev-SimpleDataSave/SetupConfigSection.png)
<br>

## Setting up the ReportSave Function

The only thing left to set up in this report is the actual ReportSave function.

**Step 1:** Click on the cell below the "ReportRange" function and enter "=ReportSave()" and click the "fx" button to bring up the Function Wizard:

![](/images/L-Dev-SimpleDataSave/FunctionWizard.png)
<br>

**Step 2:** Enter the following details in the Function Wizard:

1. **DataPortal:** Enter the Data Portal you set up in the [beginning](/wGetStarted/L-Dev-SimpleDataSave.html#setting-up-the-data-portal).
1. **RowDefRange:** This range defines the unique keys in the data source for each row. In this case it is the CustomerID. Enter the single column range for the CustomerIDs and be sure to select one row beyond the last ID (to allow expansion).
1. **ColDefRange:** Enter "4:4". This range contains the columns that will be saved.
1. **ResultsRange:** Enter "6:6". This range represents the return message to the user.

![](/images/L-Dev-SimpleDataSave/FunctionWizardFilled2.png)
<br>

Everything is now ready for the ReportSave. You can further customize your report with styling and colors if you like:

![](/images/L-Dev-SimpleDataSave/ReportSetUp.png)
<br>

## Setting up the Stored Procedure

Now that the ReportSave function is completed, Interject can use it to generate an example Stored Procedure for your save.

**Step 1:** First click on the cell that contains the ReportSave. Ensure the [Advanced Menu](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#overview) is displayed. Click on **System** and then **View SQL Template For ActiveCell**:

![](/images/L-Dev-SimpleDataSave/SQLTemplate.png)
<br>

**Step 2:** Highlight the SQL code in the new window and copy the contents to the clipboard:

![](/images/L-Dev-SimpleDataSave/SQLTemplateCode.png)
<br>

**Step 3:** Open up the database you want to use and paste the copied SQL code into a new query:

![](/images/L-Dev-SimpleDataSave/ExecuteStoredProcedure.png)
<br>

## Add the RequestContext_Parse Stored Procedure

The template that is created by Interject references a Stored Procedure called "RequestContext_Parse". This SP will process the XML data that is passed to your SP via the "Interject_RequestContext" parameter. After processing this data, you will have SP variables you can use within your SP (e.g. "@Interject_UserID", "@Interject_LoginDateUTC"). In order for the Data save Stored Procedure to work, you need to create the "RequestContext_Parse" Stored Procedure. In your database, open up a new query and execute the following code:


<button class = "collapsible"> RequestContext_Parse </button>
<div markdown="1" class="panel">

```sql
/****** Object:  StoredProcedure [dbo].[RequestContext_Parse]    Script Date: 12/20/2022 11:23:26 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE proc [dbo].[RequestContext_Parse]

	@Interject_RequestContext		nvarchar(max)
	,@ExcelVersion					nvarchar(100)	 = '' output
	,@IdsVersion					nvarchar(100)	 = '' output
	,@FileName						nvarchar(1000)	 = '' output
	,@FilePath						nvarchar(1000)	 = '' output
	,@TabName						nvarchar(1000)	 = '' output
	,@CellRange						nvarchar(100)	 = '' output
	,@SourceFunction				nvarchar(100)	 = '' output
	,@UtcOffset						decimal(6,4)	 = 0 output
	,@ColDefItemsDelimited			xml				 = '' output
	,@ResultDefItemsDelimited		xml				 = '' output
	,@RowDefItemsDelimited			xml				 = '' output
	,@MachineLoginName				nvarchar(100)	 = '' output
	,@MachineName					nvarchar(100)	 = '' output
	,@Interject_UserID				nvarchar(100)	 = '' output
	,@Interject_ClientID			nvarchar(100)	 = '' output
	,@Interject_LoginName			nvarchar(100)	 = '' output
	,@Interject_LoginAuthTypeID		int				 = 0 output
	,@Interject_LoginDateUTC		datetime		 = null output
	,@Interject_UserRolesDelimited	nvarchar(max)	 = '' output
	,@UserContextEncrypted			nvarchar(4000)	 = '' output
	,@Interject_XMLDataToSave		xml				 = null output

	
as
/*
This SP is a helper to pull all data from the RequestContext that is passed from Interject. Below
are examples to pull all the data or just a couple values that you need (which is much less typing)


declare 
	@Interject_RequestContext		nvarchar(max)
	,@ExcelVersion					nvarchar(100)	 
	,@IdsVersion					nvarchar(100)	 
	,@FileName						nvarchar(1000)	 
	,@FilePath						nvarchar(1000)	 
	,@TabName						nvarchar(1000)	 
	,@CellRange						nvarchar(100)	 
	,@SourceFunction				nvarchar(100)	 
	,@UtcOffset						decimal(6,4)	 
	,@ColDefItemsDelimited			xml	 
	,@ResultDefItemsDelimited		xml	
	,@RowDefItemsDelimited			xml	 
	,@MachineLoginName				nvarchar(100)	 
	,@MachineName					nvarchar(100)	 
	,@Interject_UserID				nvarchar(100)	 
	,@Interject_ClientID			nvarchar(100)	 
	,@Interject_LoginName			nvarchar(100)	 
	,@Interject_LoginAuthTypeID		int				 
	,@Interject_LoginDateUTC		datetime		 
	,@Interject_UserRolesDelimited	nvarchar(max)	 
	,@UserContextEncrypted			nvarchar(4000)	 
	,@Interject_XMLDataToSave		xml	 

set @Interject_RequestContext = 
'<?xml version="1.0" encoding="utf-16" standalone="yes"?>
<RequestContext>
    <ExcelVersion>14.0</ExcelVersion>
    <IdsVersion>2.2.5.13</IdsVersion>
    <FileName>Interject_TestFile (version 1).xlsb</FileName>
    <FilePath>C:\Users\jeffh-high\AppData\Roaming\Microsoft\Excel</FilePath>
    <TabName>DB_ReportRangeShort</TabName>
    <CellRange>C6</CellRange>
    <SourceFunction>Range</SourceFunction>
    <UtcOffset>7</UtcOffset>
    <ColDefItems>
        <Value>customerid</Value>
        <Value>companyname</Value>
        <Value>contactname</Value>
        <Value>contacttitle</Value>
        <Value>address</Value>
        <Value>city</Value>
        <Value>region</Value>
        <Value>phone</Value>
        <Value>fax</Value>
    </ColDefItems>
    <ResultDefItems>
        <Value>customerid</Value>
        <Value>companyname</Value>
	</ResultDefItems>
    <RowDefItems>
        <Value Row="1">customerid</Value>
        <Value Row="2">companyname</Value>
	</RowDefItems>
    <UserContext>
        <MachineLoginName>jeffh-high</MachineLoginName>
        <MachineName>IJECT-VMWARE7</MachineName>
        <UserId>UoSnjxR2bD</UserId>	
        <ClientId>CKuWBCtT</ClientId>
        <LoginName>jeffh@gointerject.com</LoginName>
        <LoginAuthTypeId>10</LoginAuthTypeId>
        <LoginDateUtc>06/16/2014 11:04:08</LoginDateUtc>
        <UserRoles>
            <Role>SysAdmin</Role>
            <Role>SchedulerAdmin</Role>
            <Role>CustomItems</Role>
        </UserRoles>
    </UserContext>
    <UserContextEncrypted>KAJeycwLWiy0t4Xe4GxPiI0sskc=</UserContextEncrypted>
    <XMLDataToSave>
  <c Column="Row" OrigValue="Row" />
  <c Column="Start" OrigValue="Start" />
  <c Column="CodeInputs" OrigValue="CodeInputs" />
  <c Column="Description" OrigValue="Description" />
  <c Column="End" OrigValue="End" />
  <c Column="Duration" OrigValue="Duration" />
  <c Column="Client" OrigValue="Client" />
  <c Column="Code1" OrigValue="Code1" />
  <c Column="Code2" OrigValue="Code2" />
  <c Column="Code3" OrigValue="Code3" />
  <c Column="Code4" OrigValue="Code4" />
  <c Column="ChargeCategory" OrigValue="ChargeCategory" />
  <r>
    <Row>18</Row>
    <Start>0.291666666666667</Start>
    <CodeInputs>.ids.dev..</CodeInputs>
    <Description>upgrade timelook</Description>
    <End />
    <Duration>15.4</Duration>
    <Client>ids</Client>
    <Code1>dev</Code1>
    <Code2 />
    <Code3 />
    <Code4 />
    <ChargeCategory>NB</ChargeCategory>
  </r>
    </XMLDataToSave>
</RequestContext>
'
exec [dbo].[RequestContext_Parse]
	@Interject_RequestContext		= @Interject_RequestContext
	,@ExcelVersion					 = @ExcelVersion			 output
	,@IdsVersion					 = @IdsVersion				 output
	,@FileName						 = @FileName				 output
	,@FilePath						 = @FilePath				 output
	,@TabName						 = @TabName					 output
	,@CellRange						 = @CellRange				 output
	,@SourceFunction				 = @SourceFunction			 output
	,@UtcOffset						 = @UtcOffset				 output
	,@ColDefItemsDelimited			 = @ColDefItemsDelimited	 output
	,@ResultDefItemsDelimited		 = @ResultDefItemsDelimited	 output
	,@RowDefItemsDelimited			 = @RowDefItemsDelimited	 output
	,@MachineLoginName				 = @MachineLoginName		 output
	,@MachineName					 = @MachineName				 output
	,@Interject_UserID				 = @Interject_UserID		 output
	,@Interject_ClientID			 = @Interject_ClientID		 output
	,@Interject_LoginName			 = @Interject_LoginName		 output
	,@Interject_LoginAuthTypeID		 = @Interject_LoginAuthTypeID output
	,@Interject_LoginDateUTC		 = @Interject_LoginDateUTC	 output
	,@Interject_UserRolesDelimited	 = @Interject_UserRolesDelimited	output
	,@UserContextEncrypted			 = @UserContextEncrypted	 output
	,@Interject_XMLDataToSave		 = @Interject_XMLDataToSave			 output

Select
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


-- since all paramters are optional, you can also just ask for the values you need like below

exec [dbo].[RequestContext_Parse]
	@Interject_RequestContext		= @Interject_RequestContext
	,@Interject_LoginName			= @Interject_LoginName			 output
	,@Interject_UserID				= @Interject_UserID				 output

Select
	@Interject_UserID							as '@Interject_UserID'
	,@Interject_LoginName						as '@Interject_LoginName'


*/

	set nocount on 

	declare @Interject_RequestContextXML as xml
	set @Interject_RequestContextXML = @Interject_RequestContext 
	
	select
		@ExcelVersion							= T.c.value('./ExcelVersion[1]',						'nvarchar(100)') 
		,@IdsVersion							= T.c.value('./IdsVersion[1]',							'nvarchar(100)') 
		,@FileName								= T.c.value('./FileName[1]',							'nvarchar(1000)') 
		,@FilePath								= T.c.value('./FilePath[1]',							'nvarchar(1000)') 
		,@TabName								= T.c.value('./TabName[1]',								'nvarchar(1000)') 
		,@CellRange								= T.c.value('./CellRange[1]',							'nvarchar(100)') 
		,@SourceFunction						= T.c.value('./SourceFunction[1]',						'nvarchar(100)') 
		,@UtcOffset								= T.c.value('./UtcOffset[1]',							'decimal(6,4)') 
		,@MachineLoginName						= T.c.value('./UserContext[1]/MachineLoginName[1]',		'nvarchar(100)')
		,@MachineName							= T.c.value('./UserContext[1]/MachineName[1]',			'nvarchar(100)') 
		,@Interject_UserID						= T.c.value('./UserContext[1]/UserId[1]',				'nvarchar(100)') 
		,@Interject_ClientID					= T.c.value('./UserContext[1]/ClientId[1]',				'nvarchar(100)') 
		,@Interject_LoginName					= T.c.value('./UserContext[1]/LoginName[1]',			'nvarchar(100)') 
		,@Interject_LoginAuthTypeID				= T.c.value('./UserContext[1]/LoginAuthTypeId[1]',		'int') 
		,@Interject_LoginDateUTC				= T.c.value('./UserContext[1]/LoginDateUtc[1]',			'datetime') 
		,@UserContextEncrypted					= T.c.value('./UserContextEncrypted[1]',				'nvarchar(100)') 
		,@Interject_XMLDataToSave				= T.c.value('./XMLDataToSave[1]',						'nvarchar(max)') 
	from @Interject_RequestContextXML.nodes('/RequestContext') T(c)

	set @Interject_XMLDataToSave = cast(@Interject_RequestContextXML.query('/RequestContext/XMLDataToSave') as nvarchar(max))

	-- UserRolesDelimited
	Select @Interject_UserRolesDelimited =
		STUFF
		(
			(
				SELECT ',' + T.c.value('.', 'nvarchar(100)') 
				from @Interject_RequestContextXML.nodes('RequestContext/UserContext[1]/UserRoles[1]/Role') T(c)
				ORDER BY T.c.value('.', 'nvarchar(100)') 
				FOR XML PATH ('')
			)
			,1
			,1
			,''
		)


	-- ColDefItemsDelimited
	Select @ColDefItemsDelimited =
		STUFF
		(
			(
				SELECT ',' + T.c.value('.', 'nvarchar(500)') 
				from @Interject_RequestContextXML.nodes('RequestContext/ColDefItems/Value') T(c)
				ORDER BY T.c.value('.', 'nvarchar(500)') 
				FOR XML PATH ('')
			)
			,1
			,1
			,''
		)

	-- ResultDefItemsDelimited
	Select @ResultDefItemsDelimited =
		STUFF
		(
			(
				SELECT ',' + T.c.value('.', 'nvarchar(500)') 
				from @Interject_RequestContextXML.nodes('RequestContext/ResultDefItems/Value') T(c)
				ORDER BY T.c.value('.', 'nvarchar(500)') 
				FOR XML PATH ('')
			)
			,1
			,1
			,''
		)

	-- RowDefItemsDelimited
	Select @RowDefItemsDelimited =
		STUFF
		(
			(
				SELECT ',' + isnull(T.c.value('.', 'nvarchar(500)'),'') 
				+ isnull('|' + T.c.value('./@Row', 'nvarchar(500)'),'')
				from @Interject_RequestContextXML.nodes('RequestContext/RowDefItems/Value') T(c)
				ORDER BY T.c.value('.', 'nvarchar(500)') 
				FOR XML PATH ('')
			)
			,1
			,1
			,''
		)

GO
```
</div>

## Modifying the Stored Procedure

The SQL auto generated template by Interject is formatted based on the ReportSave function within your report. It includes the definitions you set in that function to build the Stored Procedure (SP). It also includes some example code. Some of this code you may choose to use depending on your purposes but other code you will not need and can delete. The following walks you through the major sections of the code with instructions on the changes. Deletions are marked with red highlight, changes are marked in yellow.

### Parameters

There are 2 parameters in the SP. The first one "Interject_RequestContext" was the System Parameter you set up in the Data Portal. Again, this XML contextual information will be passed by Interject to the SP upon execution.

The second parameter is a "TestMode" bit. If you are testing, you can set the value to 1 to print out detailed information upon execution. This will also rollback any changes so your database remains unchanged.

![](/images/L-Dev-SimpleDataSave/SPParams.png)
<br>

### Testing

The next section is a commented out code used for testing. If you want to test your SP, you can simply highlight the text within and execute it. Notice at the end the ContactName and ContactTitle data are sent for each row in your report. You can change this data if you desire for testing purposes.

![](/images/L-Dev-SimpleDataSave/SPTesting.png)
<br>

### Context Parameters

This section declares and sets variables with the RequestContext_Parse SP. This SP takes in the XML data sent by Interject and parses it into variables that you can use within your SP.

![](/images/L-Dev-SimpleDataSave/SPContextParams.png)
<br>

### Error Message

The ErrorMessageToUser is declared as blank to begin with. If the execution of the SP encounters any errors, it will set this variable with a message.

![](/images/L-Dev-SimpleDataSave/SPErrorMessage.png)
<br>

### Data To Process

This section declares a table variable ("@DataToProcess") that will be used to store all the data that will be processed in the save. Each record includes the corresponding row in Excel ("_ExcelRow"), and a message ("_MessageToUser") that can be sent back to the user.

The last two columns ("ExampleColumnKey" and "ExampleColumnValue") are just examples used to validate the data coming in. They are not used in this example so delete them. You also need to change the data types and size to match your data.

![](/images/L-Dev-SimpleDataSave/SPDataToProcess.png)
<br>

### Inserting the Data to Process

This section will take the XML data sent by Interject from your report and put it into the "@DataToProcess" table. Again, you can delete the "ExampleColumnKey" and "ExampleColumnValue" columns and change the data types and size to match your data.

![](/images/L-Dev-SimpleDataSave/SPInsertToDataToProcess.png)
<br>

### Validations

Now that you have all the data from your report into a table, you can do some validations on it before your target data source is updated. This section will run through certain validations and marks the \_MessageToUser upon a check. This is example code. You can use and modify it to match your report and data or you can delete it. There are 5 parts:

1. Validating a parameter is a certain value (not used in this example)
1. Validating the data to save does not contain duplicate keys (change data type and size to match your data)
1. Validating a required column is not blank (not used in this example)
1. Validating a column has certain text (not used in this example)
1. If any validation checks recorded a message, this SP will GOTO the end and not update any records (it will show the user the message on the corresponding row)

![](/images/L-Dev-SimpleDataSave/SPValidation.png)
<br>

### ChangeLog

You can delete the "CREATE TABLE #ExampleTableToUpdate" part, it is not used in this example. 

Next, another table variable is declared. The "@ChangeLog" table will be filled with information regarding the changes to the data, such as the row in the Excel report, the type of change that was done, and the corresponding key.

![](/images/L-Dev-SimpleDataSave/SPDeclareChangeLog.png)
<br>

### Merge

This section is where the data from your report (located in the "@DataToProcess" table), is merged with the target table in your database. It first declares a transaction. This is so the following changes can either be committed if no errors or rolled back if there is an error. 

Next it merges by joining the tables on your key and updating the desired columns when there is a change detected. 

Finally, it outputs the change information to the "@ChangeLog" table.

![](/images/L-Dev-SimpleDataSave/SPMerge.png)
<br>

### Set Message To User

This section sets the message that will be displayed to the user by comparing the action values in the "@ChangeLog" table. You can change the message to anything you like.

![](/images/L-Dev-SimpleDataSave/SPSetMessageToUser.png)
<br>

### Final Response To User

This last section simply returns the message on each row back to the user. This could be an "Update" or an error message if it was set previously.

It also raises an error message if the parameter "@ErrorMessageToUser" was set.

![](/images/L-Dev-SimpleDataSave/SPFinalResponseToUser.png)
<br>

Now that the Stored Procedure is finished, execute it to save it.

The following is the finished SP:

<button class = "collapsible"> NorthWindSimpleDataSaveSP </button>
<div markdown="1" class="panel">

```sql
CREATE OR ALTER PROC NorthWindSimpleDataSaveSP

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
	

	EXEC NorthWindSimpleDataSaveSP
		@TestMode = 1
		,@Interject_RequestContext = '<?xml version="1.0" encoding="utf-16" standalone="yes"?>
<RequestContext>
    <ExcelVersion>16.0</ExcelVersion>
    <IdsVersion>2.4.1.25</IdsVersion>
    <FileName>DevelopSimpleDataSave.xlsx</FileName>
    <FilePath>D:\Users\test\Documents\Documentation\DevReportSave</FilePath>
    <TabName>NewReport_1</TabName>
    <CellRange>C11</CellRange>
    <SourceFunction>Save</SourceFunction>
    <UtcOffset>-8</UtcOffset>
    <ColDefItems>
        <Value Row="4" Column="2">
            <Name>CustomerID</Name>
        </Value>
        <Value Row="4" Column="4">
            <Name>ContactName</Name>
        </Value>
        <Value Row="4" Column="5">
            <Name>ContactTitle</Name>
        </Value>
    </ColDefItems>
    <ResultDefItems>
        <Value Row="6" Column="13">
            <Name>MessageToUser</Name>
        </Value>
    </ResultDefItems>
    <RowDefItems>
        <Value Row="24" Column="2" ColumnName="CustomerID">
            <Name>BOTTM</Name>
        </Value>
        <Value Row="25" Column="2" ColumnName="CustomerID">
            <Name>GREAL</Name>
        </Value>
        <Value Row="26" Column="2" ColumnName="CustomerID">
            <Name>SAVEA</Name>
        </Value>
        <Value Row="27" Column="2" ColumnName="CustomerID">
            <Name>WHITC</Name>
        </Value>
    </RowDefItems>
    <UserContext>
    <MachineLoginName>test</MachineLoginName>
    <MachineName>1234</MachineName>
    <FullName> </FullName>
    <UserId>1234</UserId>
    <ClientId>1234</ClientId>
    <LoginName>test@email.com</LoginName>
    <LoginAuthTypeId>10</LoginAuthTypeId>
    <LoginDateUtc>03/06/2023 3:52:17</LoginDateUtc>
    <UserRoles>
        <Role></Role>
    </UserRoles>
</UserContext>
    <UserContextEncrypted>Encrypted only through interject api protocol, not direct connection</UserContextEncrypted>
    <XMLDataToSave>
  <c Column="Row" OrigValue="Row" />
  <c Column="CustomerID" OrigValue="CustomerID" />
  <c Column="ContactName" OrigValue="ContactName" />
  <c Column="ContactTitle" OrigValue="ContactTitle" />
  <r>
    <Row>24</Row>
    <CustomerID>BOTTM</CustomerID>
    <ContactName>Elizabeth Lincoln</ContactName>
    <ContactTitle>Accounting Manager</ContactTitle>
  </r>
  <r>
    <Row>25</Row>
    <CustomerID>GREAL</CustomerID>
    <ContactName>Howard Snyder</ContactName>
    <ContactTitle>Marketing Manager</ContactTitle>
  </r>
  <r>
    <Row>26</Row>
    <CustomerID>SAVEA</CustomerID>
    <ContactName>Jose Pavarotti</ContactName>
    <ContactTitle>Sales Representative</ContactTitle>
  </r>
  <r>
    <Row>27</Row>
    <CustomerID>WHITC</CustomerID>
    <ContactName>Karl Jablonski</ContactName>
    <ContactTitle>Owner</ContactTitle>
  </r>
    </XMLDataToSave>
</RequestContext>'

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
	dataportal parameter list, Interject will pass the related value automatically.
	
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
		,@Interject_XMLDataToSave	    xml	
	
	EXEC [dbo].[RequestContext_Parse]
		@Interject_RequestContext		= @Interject_RequestContext
		,@ExcelVersion					 = @ExcelVersion			 OUTPUT
		,@IdsVersion					 = @IdsVersion				 OUTPUT
		,@FileName						 = @FileName				 OUTPUT
		,@FilePath						 = @FilePath				 OUTPUT
		,@TabName						 = @TabName					 OUTPUT
		,@CellRange						 = @CellRange				 OUTPUT
		,@SourceFunction				 = @SourceFunction			 OUTPUT
		,@UtcOffset						 = @UtcOffset				 OUTPUT
		,@ColDefItemsDelimited			 = @ColDefItemsDelimited	 OUTPUT
		,@ResultDefItemsDelimited		 = @ResultDefItemsDelimited	 OUTPUT
		,@RowDefItemsDelimited			 = @RowDefItemsDelimited	 OUTPUT
		,@MachineLoginName				 = @MachineLoginName		 OUTPUT
		,@MachineName					 = @MachineName				 OUTPUT
		,@Interject_UserID				 = @Interject_UserID		 OUTPUT
		,@Interject_ClientID			 = @Interject_ClientID		 OUTPUT
		,@Interject_LoginName			 = @Interject_LoginName		 OUTPUT
		,@Interject_LoginAuthTypeID		 = @Interject_LoginAuthTypeID OUTPUT
		,@Interject_LoginDateUTC		 = @Interject_LoginDateUTC	 OUTPUT
		,@Interject_UserRolesDelimited	 = @Interject_UserRolesDelimited	OUTPUT
		,@UserContextEncrypted			 = @UserContextEncrypted	 OUTPUT
		,@Interject_XMLDataToSave		 = @Interject_XMLDataToSave	 OUTPUT
	
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
			SET @ErrorMessageToUser = 'Error in Parsing XML from Interject.  Error: ' + ERROR_MESSAGE()
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
			,[UpdateTypeCode] VARCHAR(10)  -- Will show UPDATE, INSERT, or DELETE
			,[CustomerID] NCHAR(5)
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
			--WHEN NOT MATCHED BY TARGET THEN -- Handles the insert based on LEFT JOIN -- NOT USED IN THIS SIMPLE EXAMPLE
			-- INSERT([ExampleColumnKey],[ExampleColumnValue])
			-- VALUES(s.ExampleColumnKey],s.[ExampleColumnValue])
			
			--WHEN NOT MATCHED BY SOURCE -- Handles the delete based on the RIGHT JOIN -- NOT USED IN THIS SIMPLE EXAMPLE
			-- AND... add restrictions so delete doesn't remove too much. Filter params are normally considered here.
			-- THEN 
			-- DELETE
				
			-- the output captures the changes to the table and logs to a table variable
			OUTPUT 
				isnull(inserted.[CustomerID],deleted.[CustomerID])  -- include deleted in case delete is added later. Inserted is used for both Update an Insert
				,s.[_ExcelRow] 
				,$action as UpdateTypeCode  -- this logs into an a change log table variable
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
					--WHEN 'INSERT' THEN ', Added!'  -- not used in this example
					--WHEN 'DELETE' THEN ', Deleted' -- this will never match the excel side but can be used for other types of logging
					WHEN 'UPDATE' THEN ', Updated!'
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

Now you can test the SP by using the [test code](/wGetStarted/L-Dev-SimpleDataSave.html#testing). For example, make a change to the data in the test code and execute the test. Because the "@TestMode" bit is set to 1, it will display all kinds of information about the SP process. Notice the changes and message to user that would be displayed.

![](/images/L-Dev-SimpleDataSave/TestingSP.png)
<br>

Note that when using the test script, no actually changes are being made to the database since the transaction of the merge is rolled back:

![](/images/L-Dev-SimpleDataSave/TestingRollback.png)
<br>

## Testing the ReportSave

The only thing left to do is test the SP by running the ReportSave function within the Excel report.

First pull the data:

![](/images/L-Dev-SimpleDataSave/TestingPullData.png)
<br>

Next make a change to a Contact Name or Contact Title and run the Report Save:

![](/images/L-Dev-SimpleDataSave/TestingSave.png)
<br>

Notice the results!:

![](/images/L-Dev-SimpleDataSave/TestingResults.png)
<br>
