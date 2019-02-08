
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