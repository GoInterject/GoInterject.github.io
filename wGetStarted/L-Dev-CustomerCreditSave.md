---
title: "Lab Developer: Customer Credit Save"
layout: custom
keywords: [save, example, walkthrough, customer aging,]
description: "This section will detail a full review of how the INTERJECT save feature works"
---
##  **Overview:**

This section will detail a full review of how the INTERJECT save feature works. Start by using the Customer Aging example. This lab will show how to design three user input fields into an existing report. The INTERJECT platform will assist in creating a stored procedure that can be used in SQL Server to help facilitate the process. Other database engines or API methods can be used for the save process as well, but for simplicity you are focusing on SQL Server and a database stored procedure as the data source. You will be using the Customer Aging report, as you have already become familiar with its [ business use case ](/wAbout/Customer-Aging.html). 

###  Setting up the Data Portals: 

This report uses the same database as  [**Dev: Customer Aging**](/wGetStarted/L-Dev-CustomerAging.html) and other reports, you do not need to create another data connection. Use the same connection as in the previous lab. The Data Portals for saving data are very similar to their Pull counterparts. 

**Step 1:** Navigate to the [INTERJECT Portal](https://portal.gointerject.com/) Website, then select  **Data Portals** in the sidebar menu. 

![](/images/L-Dev-CustAgingSave/01.jpg)
<br>
  


**Step 2:** Click the  **New Data Portal** button. 

![](/images/L-Dev-CustAgingSave/02.jpg)
<br>
  


**Step 3:** In the  **Data Portal Code** field enter **NorthwindCreditSave_MyName**. 

![](/images/L-Dev-CustAgingSave/03.jpg)
<br>
  


**Step 4:** In the description, you will fill out a short detail saying what this data portal will be used for. In this case, it will say  **Simple Data Save**. 

![](/images/L-Dev-CustAgingSave/04.jpg)
<br>
  


**Step 5:** In the  **Category** field, label the type of data portal connection that this data portal will be. In this case it will be a  **Demo**. 

![](/images/L-Dev-CustAgingSave/05.jpg)
<br>
  


**Step 6:** In the connection drop down menu you will choose the data connection **NorthwindExampleDB_MyName** that you have already created in the [Customer Aging developer lab](/wGetStarted/L-Dev-CustomerAging.html#setting-up-the-data-connection). 

![](/images/L-Dev-CustAgingSave/06.jpg)
<br>
  


**Step 7:** For the  **Command Type** you will use the stored procedure option, and in  **Stored Procedure / Command** input a name for the stored procedure you will create later. In this case you use  **[demo].[Northwind_Credit_Save_MyName]**. Then click  **create data portal.**

![](/images/L-Dev-CustAgingSave/07.jpg)
<br>

###  Setting up System Parameters: 

System Parameters are similar to Formula Parameters, but the names are reserved for INTERJECT. To review the System parameters and their purposes, go to the System Parameters section of the [ Data Portal ](/wPortal/Data-Portals.html) page. 

In this example you are going to use  **Interject_ReturnError** and  **Interject_RequestContext**. 

**Step 1:** To add the first system parameter, click the  **Click here to add a System Parameter** button. Then select  **Interject_RequestContext** for the name and click **save**. 

![](/images/L-Dev-CustAgingSave/08.jpg)
<br>
  


**Step 2:** To add an additional system parameter, first click the  **Click here to add a System Parameter** button. Then select  **Interject_ReturnError** for the name of our second parameter. Then click **save**. 

![](/images/L-Dev-CustAgingSave/09.jpg)
<br>
  


###  Creating the Report: 

**Step 1:** Open the [Report Library](/wAbout/Report-Library-Basics.html) and open the [Interject Customer Aging](L-Create-CustomerAging.html) report.

![](/images/L-Dev-CustAgingSave/10_fix.jpg)
<br>

**Step 2:** Right click the workesheet tab and select **Move or Copy**.

![](/images/L-Dev-CustAgingSave/11_fix.jpg)
<br>

**Step 3:** Select the copy check box.

![](/images/L-Dev-CustAgingSave/12_fix.jpg)
<br>

**Step 4:** Rename the worksheet tab to **CustomerCredits** and the worksheet title to **Customer Credits**.

![](/images/L-Dev-CustAgingSave/13_fix.jpg)
<br>

**Step 5:** **Unfreeze** the panes.

![](/images/L-Dev-CustAgingSave/14_fix.jpg)
<br>

**Step 6:** Insert 4 rows below row 2. Then using the format painter, apply the format from row 9 and apply it to rows 3 and 5.

![](/images/L-Dev-CustAgingSave/15_fix.jpg)
<br>

**Step 7:** Delete columns **G:L**.

![](/images/L-Dev-CustAgingSave/16_fix.jpg)
<br>

**Step 8:** Add **InvoiceTotal**, **CreditLimit**, **AccountFreeze valueList:FreezeOptions**, and **AccountNotes** to cells G2,H2,J2, and K2 accordingly.

![](/images/L-Dev-CustAgingSave/17_fix.jpg)
<br>

**Step 9:** Change the cell type for cells G8 and H8 from General to Accounting.

![](/images/L-Dev-CustAgingSave/18_fix.jpg)
<br>

**Step 10:** Insert a column between columns H and I.

![](/images/L-Dev-CustAgingSave/19_fix.jpg)
<br>

**Step 11:** In cell I25 insert **Credit Remaining** and in cell I8 input the formula **=H8-G8**.

![](/images/L-Dev-CustAgingSave/20_fix.jpg)
<br>

**Step 12:** Add coditional formatting to cell J8 by selecting the home tab, and selecting conditional formatting, then select **New Rule...**

![](/images/L-Dev-CustAgingSave/21_fix.jpg)
<br>

**Step 13:** Select the rule type **Format only cells that contain** and select **Specific Text**, **containing**, **yes**.

![](/images/L-Dev-CustAgingSave/22_fix.jpg)
<br>

**Step 14:** Apply a red fill color by selecting the fill tab, then selecting the dark red color.

![](/images/L-Dev-CustAgingSave/23_fix.jpg)
<br>

**Step 15:** Add a white text color through selecting font, then inside the color dropdown select the white color.

![](/images/L-Dev-CustAgingSave/24_fix.jpg)
<br>

**Step 16:** In cell L2 input **\[Clear]** and in cell L6 input **MessageToUser**.

![](/images/L-Dev-CustAgingSave/25_fix.jpg)
<br>

**Step 17:** Apply the formatting range to the report range formula in cell C10 by selecting the **fx** button and inputting **8:8** into the **FormatRange** argument.

![](/images/L-Dev-CustAgingSave/26_fix.jpg)
<br>

**Step 18:** In cell H11 begin writing the report save formula by inserting **=ReportSave()**.

![](/images/L-Dev-CustAgingSave/27_fix.jpg)
<br>

**Step 19:** Select the **Fx** button and for the dataportal insert the [save dataportal](/wGetStarted/L-Dev-CustomerCreditSave.html#setting-up-the-data-portals) that you created earlier in this lab.

![](/images/L-Dev-CustAgingSave/28_fix.jpg)
<br>

**Step 20:** Select the range **B26:B27** for the **RowDefSave** argument, and select the range **4:4** for the **ColumnDefinitions**, and finally, the range **6:6** for the **ResultsRange** argument.

![](/images/L-Dev-CustAgingSave/29_fix.jpg)
<br>

**Step 21:** Insert **CustomerID** into cell **B4**,**CreditLimit** into cell **H4**, **AccountFreeze** into cell **J4** and **AccountNotes** into cell **K4**.

![](/images/L-Dev-CustAgingSave/30_fix.jpg)
<br>

**Step 22:** Refreeze the panes. Pull the report and it will look like this. Now it is ready for you to create a save stored procedure in the next section.

![](/images/L-Dev-CustAgingSave/31_fix.jpg)
<br>

###  Creating the Stored Procedure 

**Step 1:** First, select the  **Pull** button and pull the data into the spreadsheet. 


**Step 2:** In the excel sheet, click the cell with the ReportSave formula. Then  click  **Advanced Menu** in the INTERJECT Ribbon. This button is a toggle, so if it is currently showing  **Simple Menu** do not click it. 


**Step 3:** Then, click the  **System** dropdown and select  **View SQL Template for ActiveCell** . Make sure you have the ReportSave cell selected. 


A window will pop up providing the developer with the SQL template used to create the stored procedure. 

  


Copy and paste the template code into the MSSQL Server from your Excel sheet. This template is a helpful starting point that includes the Data Portal parameters and pre-formatted test code, but more work is needed to construct the required data save. Here is an example test code to compare with, but yours will be different. Do not copy this code and use it for your report as it will not work. 


<button class="collapsible">\[demo\].\[Northwind_Invoices_Pull_MyName\]</button>
<div markdown="1" class="panel">

```sql

CREATE PROC [demo].[Northwind_Credit_Save_MyName]

    -- System Params not in formula
     @Interject_RequestContext nvarchar(max)
    ,@Interject_ReturnError varchar(2000) OUTPUT
    ,@TestMode bit = 0 -- used only for testing the stored procedure directly.  It will show more results when set to 1.


AS

/*
==================================================================================
Test Code Example
Declare @Interject_ReturnError varchar(2000)

Execute [demo].[Northwind_Credit_Save]
	@Interject_RequestContext = '<?xml version="1.0" encoding="utf-16" standalone="yes"?>
<RequestContext>
    <ExcelVersion>16.0</ExcelVersion>
    <IdsVersion>2.3.22.0</IdsVersion>
    <FileName>Interject_CustomerDemo_v1.4.xlsx</FileName>
    <FilePath></FilePath>
    <TabName>CustomerCredits</TabName>
    <CellRange>H11</CellRange>
    <SourceFunction>Save</SourceFunction>
    <UtcOffset>-7</UtcOffset>
    <ColDefItems>
        <Value Row="4" Column="2">
            <Name>CustomerID</Name>
        </Value>
        <Value Row="4" Column="8">
            <Name>CreditLimit</Name>
        </Value>
        <Value Row="4" Column="10">
            <Name>AccountFreeze</Name>
        </Value>
        <Value Row="4" Column="11">
            <Name>AccountNotes</Name>
        </Value>
    </ColDefItems>
    <ResultDefItems>
        <Value Row="6" Column="12">
            <Name>MessageToUser</Name>
        </Value>
    </ResultDefItems>
    <RowDefItems>
        <Value Row="27" Column="2" ColumnName="CustomerID">
            <Name>BOTTM</Name>
        </Value>
    </RowDefItems>
    <UserContext>
    <MachineLoginName></MachineLoginName>
    <MachineName></MachineName>
    <FullName></FullName>
    <UserId>UFR62JQWx4</UserId>
    <ClientId>CgCfW9qi</ClientId>
    <LoginName></LoginName>
    <LoginAuthTypeId>10</LoginAuthTypeId>
    <LoginDateUtc></LoginDateUtc>
    <UserRoles>
        <Role></Role>
    </UserRoles>
</UserContext>
    <UserContextEncrypted>Encrypted only through interject api protocol, not direct connection</UserContextEncrypted>
    <XMLDataToSave>
  <c Column="Row" OrigValue="Row" />
  <c Column="CustomerID" OrigValue="CustomerID" />
  <c Column="CreditLimit" OrigValue="CreditLimit" />
  <c Column="AccountFreeze" OrigValue="AccountFreeze" />
  <c Column="AccountNotes" OrigValue="AccountNotes" />
  <r>
    <Row>27</Row>
    <CustomerID>BOTTM</CustomerID>
    <CreditLimit>50000</CreditLimit>
    <AccountFreeze>Yes</AccountFreeze>
    <AccountNotes>Customer has exceeded credit limit</AccountNotes>
  </r>
    </XMLDataToSave>
</RequestContext>'
	,@Interject_ReturnError = @Interject_ReturnError output

Select 	@Interject_ReturnError as '@Interject_ReturnError'
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
    
        ,[CustomerID] VARCHAR(max)
        ,[CreditLimit] VARCHAR(max)
        ,[AccountFreeze] VARCHAR(max)
        ,[AccountNotes] VARCHAR(max)
        -- remove the following columns after updating this code for your real data.  These are used for validation illustrations only
        ,[ExampleColumnKey] INT
        ,[ExampleColumnValue] VARCHAR(100)
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
            ,[CreditLimit]
            ,[AccountFreeze]
            ,[AccountNotes]

            -- The below columns are provided to help with this example.  Please remove.
            ,[ExampleColumnKey]
            ,[ExampleColumnValue]
        )
        SELECT
            -- The below row value is always provided by Interject
            T.c.value('./Row[1]', 'INT') as [_ExcelRow]
            -- The below columns are provided based on your column definitions in the ReportSave() function
            ,T.c.value('./CustomerID[1]', 'VARCHAR(max)') as [CustomerID]
            ,T.c.value('./CreditLimit[1]', 'VARCHAR(max)') as [CreditLimit]
            ,T.c.value('./AccountFreeze[1]', 'VARCHAR(max)') as [AccountFreeze]
            ,T.c.value('./AccountNotes[1]', 'VARCHAR(max)') as [AccountNotes]

            -- The below columns are provided to help with this example.  Please remove.
            ,T.c.value('./ExampleyColumnKey[1]', 'VARCHAR(100)') as [ExampleColumnKey]
            ,T.c.value('./ExampleColumnValue[1]', 'INT') as [ExampleColumnValue]
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
    
    -- Validate a stored procedure parameter input passed from the spreadsheet.  
    DECLARE @ParameterExample as varchar(50)  -- This is declared only to simulate a store procedure parameter
    IF @ParameterExample = 'TheWrongValue' and 'SkipThisExample' = 'True'
    BEGIN
        SET @ErrorMessageToUser = 'You selected an invalid value for ''Example Input''. Save aborted.'
        GOTO FinalResponseToUser
    END
    
    -- Validate that the details do not have duplicates on the primary key
    UPDATE m
    SET [_MessageToUser] = [_MessageToUser] + ', Duplicate key'
    FROM @DataToProcess m
    INNER JOIN
        (
            SELECT [ExampleColumnKey] 
            FROM @DataToProcess
            WHERE [ExampleColumnKey] <> ''
            GROUP BY [ExampleColumnKey]
            HAVING COUNT(1) > 1
        ) as t
        ON
            m.ExampleColumnKey = t.ExampleColumnKey
    
    -- Validate a column in a detail row, but don't exit if error since we can check multiple issues before notifing the user
    UPDATE @DataToProcess
    SET [_MessageToUser] = [_MessageToUser] + ', [ExampleColumnValue] is a required entry'
    WHERE [ExampleColumnValue] = ''
    
    -- Validate a column has valid text
    UPDATE @DataToProcess
    SET [_MessageToUser] = [_MessageToUser] + ', [ExampleColumnValue] must be either Yes or No'
    WHERE [ExampleColumnValue] IN ('Yes','No')
    
    -- Now check if there were any validation issues in the detail and stop processing if true
    IF EXISTS(SELECT 1 FROM @DataToProcess WHERE [_MessageToUser] <> '')
    BEGIN
        SET @ErrorMessageToUser = 'There were errors in the details of your input.  Please review the errors noted in each row.'
        GOTO FinalResponseToUser
    END
    
    IF @TestMode =1 
    BEGIN
        SELECT '@DataToProcess - After Validation' as ResultName
        SELECT * FROM @DataToProcess
    END
    
    --
    -- DATA UPDATE
    --
    
    -- This represents the table where the data would be updated to.  Remove this temp table since it is for example purposes only.
    CREATE TABLE #ExampleTableToUpdate 
    (
        [ExampleColumnKey]		INT PRIMARY KEY
        ,[ExampleColumnValue]	VARCHAR(100)

        ,[CustomerID] VARCHAR(max)
        ,[CreditLimit] VARCHAR(max)
        ,[AccountFreeze] VARCHAR(max)
        ,[AccountNotes] VARCHAR(max)
    )
    BEGIN TRY
        
        -- this table variable will log the changes to the target table so it can be used
        -- to return helpful feedback to the user about how the save action resulted
        DECLARE @ChangeLog as TABLE
        (
            [_ExcelRow] INT	-- will capture the source row that affected the target table
            ,[UpdateTypeCode] VARCHAR(10)  -- Will show UPDATE, INSERT, or DELETE
            ,[TargetTableKey] INT
        )
        
        BEGIN TRAN t1
            --
            --  use MERGE statement that UPDATES, INSERTS, and DELETES in one action
            --
            MERGE #ExampleTableToUpdate t -- t = the target table or view to update
            USING (
                SELECT
                * -- specify your specific columns to be used
                FROM @DataToProcess 
            ) s -- s = the source data to be used to update the target table
            -- the join on the column keys is specified below
            ON 
                s.[ExampleColumnKey] = t.[ExampleColumnKey]
                
            WHEN MATCHED -- Handles the update based on INNER JOIN
                AND NOT 
                (
                    t.[ExampleColumnValue] = t.[ExampleColumnValue] -- To ensure only changes are captured
                )
                THEN
                UPDATE SET
                    t.[ExampleColumnValue] = s.[ExampleColumnValue]
            --WHEN NOT MATCHED BY TARGET THEN -- Handles the insert based on LEFT JOIN -- NOT USED IN THIS SIMPLE EXAMPLE
            -- INSERT([ExampleColumnKey],[ExampleColumnValue])
            -- VALUES(s.ExampleColumnKey],s.[ExampleColumnValue])
            
            --WHEN NOT MATCHED BY SOURCE -- Handles the delete based on the RIGHT JOIN -- NOT USED IN THIS SIMPLE EXAMPLE
            -- AND... add restrictions so delete doesn't remove too much. Filter params are normally considered here.
            -- THEN 
            -- DELETE
                
            -- the output captures the changes to the table and logs to a table variable
            OUTPUT 
                isnull(inserted.[ExampleColumnKey],deleted.[ExampleColumnKey])  -- include deleted in case delete is added later. Inserted is used for both Update an Insert
                ,s.[_ExcelRow] 
                ,$action as UpdateTypeCode  -- this logs into an a change log table variable
            INTO @ChangeLog
            (
                [TargetTableKey]
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
    
After getting the template, it is important to modify the procedure for what is needed. For example, the parameters are automatically set to max, so an easy change would be to set them to more realistic character lengths. 


<button class="collapsible">\[demo\].\[Northwind_Invoices_Pull_MyName\]</button>
<div markdown="1" class="panel">

```sql

ALTER PROC [demo].[Northwind_Credit_Save_MyName]

     @Interject_RequestContext nvarchar(max)
    ,@Interject_ReturnError varchar(2000) OUTPUT
    ,@TestMode bit = 0

AS

    --
    -- Use helper to extract data from Interject_RequestContext. Remove items that are not needed
    -- The helper stored procedure [dbo].[RequestContext_Parse] is required for this section to function 
    --
    DECLARE @Interject_XMLDataToSave	    XML	
    DECLARE @Interject_NTLogin				VARCHAR(50)

    EXEC [dbo].[RequestContext_Parse]
            @Interject_RequestContext		= @Interject_RequestContext
        ,@Interject_XMLDataToSave		= @Interject_XMLDataToSave	OUTPUT
        ,@MachineLoginName				= @Interject_NTLogin		OUTPUT
    
    IF @TestMode = 1
    BEGIN
        SELECT
                @Interject_XMLDataToSave	AS '@Interject_XMLDataToSave'
            ,@Interject_NTLogin			AS '@Interject_NTLogin'
    END
    
    DECLARE @ErrorMessageToUser AS VARCHAR(1000) = ''
    DECLARE @NowUTC				AS DATETIME = GETUTCDATE()
    --
    -- PROCESS THE XML DATA INTO TABLE VARIABLE
    --
    
    DECLARE @DataToProcess TABLE
    (
            [_ExcelRow] INT 
        ,[_MessageToUser] VARCHAR(500) DEFAULT('')
        ,[CustomerID] VARCHAR(max)
        ,[CreditLimit] VARCHAR(max)
        ,[AccountFreeze] VARCHAR(max)
        ,[_FreezeBit] BIT DEFAULT(0)
        ,[AccountNotes] VARCHAR(max)
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
            ,[CreditLimit]
            ,[AccountFreeze]
            ,[AccountNotes]
        )
        SELECT
            
                T.c.value('./Row[1]', 'INT') as [_ExcelRow]
            ,T.c.value('./CustomerID[1]', 'VARCHAR(max)') as [CustomerID]
            ,T.c.value('./CreditLimit[1]', 'VARCHAR(max)')	 as [CreditLimit]
            ,T.c.value('./AccountFreeze[1]', 'VARCHAR(max)') as [AccountFreeze]
            ,T.c.value('./AccountNotes[1]', 'VARCHAR(max)')	 as [AccountNotes]
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
            m.[CustomerID] = t.[CustomerID]
    
    -- Validate a column has valid text
    UPDATE @DataToProcess
    SET [_MessageToUser] = [_MessageToUser] + ', Account Freeze must be either Yes or left blank'
    WHERE [AccountFreeze] NOT IN ('Yes','')

    UPDATE @DataToProcess
        SET [_MessageToUser] = [_MessageToUser] + ', Account Notes must be 140 characters or less'
    FROM @DataToProcess 
    WHERE LEN([AccountNotes]) >= 140
    
    -- Now check if there were any validation issues in the detail and stop processing if true
    IF EXISTS(SELECT 1 FROM @DataToProcess WHERE [_MessageToUser] <> '')
    BEGIN
        SET @ErrorMessageToUser = 'There were errors in the details of your input.  Please review the errors noted in each row.'
        GOTO FinalResponseToUser
    END
    
    
    IF @TestMode = 1 
    BEGIN
        SELECT '@DataToProcess - After Validation' as ResultName
        SELECT * FROM @DataToProcess
    END
    
    -- convert the 'yes' input into a bit for table storage
    UPDATE @DataToProcess
        SET [_FreezeBit] = 1
    WHERE [AccountFreeze] = 'Yes'

    UPDATE @DataToProcess
        SET CreditLimit = 0
    WHERE CreditLimit IS NULL
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
            ,[TargetTableKey] VARCHAR(5)
        )
        
        BEGIN TRAN t1
            --
            --  use MERGE statement that UPDATES, INSERTS, and DELETES in one action
            --
            MERGE [demo].[Northwind_AccountCredits] t -- t = the target table or view to update
            USING @DataToProcess s -- s = the source data to be used to update the target table
            ON 
                s.[CustomerID] = t.[CustomerID]
                
            WHEN MATCHED -- Handles the update based on INNER JOIN
                AND 
                (
                        t.[CustomerID]		<> s.[CustomerID]
                    OR t.[CreditLimit]		<> s.[CreditLimit]
                    OR t.[AccountFreeze]	<> s.[_FreezeBit]
                    OR t.[AccountNotes]		<> s.[AccountNotes]

                )
                THEN
                UPDATE SET
                        t.[CustomerID]		 = s.[CustomerID]
                    ,t.[CreditLimit]	 = s.[CreditLimit]
                    ,t.[AccountFreeze]	 = s.[_FreezeBit]
                    ,t.[AccountNotes]	 = s.[AccountNotes]
                    ,t.[LastChangedBy]	 = @Interject_NTLogin
                    ,t.[LastChangedDate] = @NowUTC
            WHEN NOT MATCHED BY TARGET THEN -- Handles the insert based on LEFT JOIN 
            INSERT (
                    [CustomerID]		
                ,[CreditLimit]		
                ,[AccountFreeze]	
                ,[AccountNotes]
                ,[LastChangedBy]
                ,[LastChangedDate]
            )
            VALUES (
                    s.[CustomerID]
                ,s.[CreditLimit]
                ,s.[_FreezeBit]
                ,s.[AccountNotes]
                ,@Interject_NTLogin
                ,@NowUTC
            )
                
            -- the output captures the changes to the table and logs to a table variable
            OUTPUT 
                    isnull(inserted.[CustomerID],deleted.[CustomerID])  -- include deleted in case delete is added later. Inserted is used for both Update an Insert
                ,s.[_ExcelRow] 
                ,$action as UpdateTypeCode  -- this logs into an a change log table variable
            INTO @ChangeLog
            (
                    [TargetTableKey]
                ,[_ExcelRow]
                ,[UpdateTypeCode]
            ); 
            
            --now we have enough information to update the message to user for each row
            UPDATE dtp
            SET [_MessageToUser] = 
                CASE cl.UpdateTypeCode
                    WHEN 'INSERT' THEN ', Added!'  -- not used in this example
                    WHEN 'UPDATE' THEN ', Updated!'
                END 
            FROM @DataToProcess dtp
                INNER JOIN @ChangeLog cl 
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

###  Testing the Stored Procedure 

For quick testing, click on the  **View SQL Test** and copy the test code to the development area. For more information, go to the [ common troubleshooting page ](/wGetStarted/Troubleshooting-Reports.html). 

![](/images/L-Dev-CustAgingSave/20.jpg)
<br>
  


Now that you have modified the stored procedure, go back to excel and see if the data gets correctly saved. 

![](/images/L-Dev-CustAgingSave/21.jpg)
<br>
  


After the save, there will be a return message stating what was changed based on the row. 

![](/images/L-Dev-CustAgingSave/22.jpg)
<br>
