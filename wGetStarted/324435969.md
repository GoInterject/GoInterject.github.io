---
title: Interject Documentation > L13.1 Dev> Customer Aging Detail
layout: custom
---
* * *

##  **Overview**

In this example, you will learn to create a third report, Customer Aging Detail, that will be drilled to from the Customer Aging Report. This report shows a customer's outstanding balance by individual invoice. The Aging Detail is a more complex report than shown in the earlier lab [ Lab 12.2 Dev: Customer Orders ](/wGetStarted/324403205.html) , because it leverages two report formulas to create a report with subtotals. You should have already seen the Customer Aging Detail report while reviewing the business use case in the [ **Customer Aging in Real-World Walkthroughs** ](/wAbout/Customer-Aging_128091294.html) . 

You can go directly to any topic of this walk-through by clicking one of the links below. 

  * ####  Verifying the Data Connection 

  * ####  Copying and Modifying the Data Portal 

  * ####  Creating the Stored Procedure 

  * ####  Creating the Report 

  * ####  Creating a New Data Portal for 2 Recordsets 

  * ####  Updating the Stored Procedure for 2 Recordsets 

  * ####  Updating the Report for 2 Recordsets 




### 

###  Verifying the Data Connection 

Because this report uses the same database as [ Dev: Customer Aging Detail ](/wGetStarted/324567045.html) , you do not need to create another data connection. The same connection can be used for this report. The connection created in the previous example was named **NorthwindExampleDB_MyName** and your own data connection likely had your name in the suffix. 

###  Copying and Modifying the Data Portals 

For this report you are going to use two data portals. The first will be the same data portal used in a previous example called **NorthwindCustomers_MyName** . You created your own with your name in the suffix. The below steps will create a copy of this data portal for the customer invoice detail since it saves a little time. 

**Step 1:** Navigate to the data portal, **NorthwindCustomers_MyName** , and click the green clone button on the top right of the page. 

![](attachments/324435969/328303186.png)

  


**Step 2:** A new data portal named, **NorthwindCustomers_MyName_copy** , generates. Change this data portal name to **NorthwindCustomerInvoices_MyName** . Since each Data Portal Code must be unique, you should add your name to the suffix. 

![](attachments/324435969/328269910.jpg)

  


**Step 3:** Change the procedure name to run **[demo].[Northwind_Invoices_Pull_MyName]** , which you will create shortly. As in the last step, replace **_MyName** with your own name. 

![](attachments/324435969/328433982.jpg)

  


**Step 4:** You will use the existing Formula Parameters but for this example you need to add more more. Select **Click here to add a Formula Parameter** . Enter **IncludePaid** for Name, **varchar** for Type, and **input** for direction. Click the **More** button. 

![](attachments/324435969/328401105.jpg)

  


Enter **Include Paid** for Helper Name and enter **Include Invoices that have already been paid for by the customer** for Comments. Click the Save icon. 

![](attachments/324435969/328532161.jpg)

  


**Step 5:** Click the trash can icon on the far right of the Interject_LocalTimeZoneOffset to delete it. You are going to a use a different System Parameter for this data portal to illustrate a new System Parameter that has not been presented in previous examples. 

![](attachments/324435969/328269915.jpg)

  


**Step 6:** Click the drop-down on the **Interject_NTLogin** and change it **Interject_RequestContext** . This System Parameter provides all request and user context that is available in a single XML string. It is best practices to use **Interject_RequestContext** as the only System Parameter since it reduces work over the long run. Since this parameter includes all system parameter information, the data portal configuration does not need to be changed if the stored procedure needs to reference additional context. Click Save. 

![](attachments/324435969/328564893.jpg)

  


### 

###  Creating the Stored Procedure 

Stored procedures or data APIs serve as a middle tier for an INTERJECT report. In this example, you are using a stored procedure. INTERJECT can retrieve one or more result sets from the stored procedure into the spreadsheet report. 

The INTERJECT Website Portal allows you to create and manage the data portals and reference stored procedures you create. Data portals are stored locally in your Excel session when you log into INTERJECT. When requesting data, INTERJECT creates a point-to-point connection with the intended data source. 

The steps below assume you are proficient with SQL Management Studio for Microsoft SQL Server and in creating stored procedures. If you need additional training in this area, please contact us at [ info@gointerject.com ](mailto:info@gointerject.com) . 

**Step 1:** Create a stored procedure called [demo].[Northwind_Invoices_Pull_MyName] using the following example code. Please use your name in the suffix of the stored procedure name. 

**Customer Invoices** Expand source 
    
    
    CREATE PROC [demo].[Northwind_Invoices_Pull_MyName]
    
    	 @CompanyName VARCHAR(100)
    	,@ContactName NVARCHAR(100)
    	,@CustomerID VARCHAR(500) = ''
    	,@IncludePaid VARCHAR(5) = 0
    	,@Interject_RequestContext NVARCHAR(MAX)
    
    AS
    BEGIN
    
    SET NOCOUNT ON  -- helps reduce conflicts with ADO
    
    DECLARE @Interject_LoginName VARCHAR(200)
    DECLARE @UtcOffset	DECIMAL(6,4)
    
    -- Dataset has very old dates
    -- To give a static date to compare to we hard coded the date.
    DECLARE @DateCompare VARCHAR(20) = '1997-09-15'
    DECLARE @ErrorMessage VARCHAR(100)
    
    IF LEN(@CompanyName)>40
    BEGIN
    	SET @ErrorMessage = 'Usernotice:The company search text must not be more than 40 characters.'
    	RAISERROR (@ErrorMessage, 18, 1)
    	RETURN		
    END
    
    -- This is another SP that parses the xml in request context to get the needed system data
    EXEC [demo].[RequestContext_Parse]
    	@Interject_RequestContext		= @Interject_RequestContext	
    	,@Interject_LoginName			= @Interject_LoginName	OUTPUT
    	,@UtcOffset = @UtcOffset OUTPUT
    
    -- @IncludePaid is default 0.
    -- if set to Yes, change it to 1
    IF @IncludePaid = 'Yes'
    	SET @IncludePaid = 1
    
    -----------------------------------------------
    --	REMAINDER OF DATA QUERY
    -----------------------------------------------
    --Create CTE that sorts data by InvoiceDate's difference from the hardcoded DateCompare
    ;WITH Invoice_CTE
    AS
    (
        SELECT 
    		 [CustomerID]
    		,[InvoiceID]
    		,[InvoiceNum]
    		,[InvoiceTotal]
    		,[Current]
    		,[30Days]
    		,[60Days]
    		,[90Days]
    		,[IsPaid]
    	FROM 
    	(
    		SELECT 
    			 i.[CustomerID]
    			,i.[InvoiceID]
    			,i.[InvoiceNum]
    			,i.[InvoiceDate]
    			,i.[InvoiceTotal]
    			,CASE WHEN DATEDIFF(dd,InvoiceDate,@DateCompare) < 30 THEN (i.[InvoiceTotal]) ELSE 0 END AS [Current]
    			,CASE WHEN DATEDIFF(dd,InvoiceDate,@DateCompare) BETWEEN 30 AND 59 THEN (i.[InvoiceTotal]) ELSE 0 END AS [30Days]
    			,CASE WHEN DATEDIFF(dd,InvoiceDate,@DateCompare) BETWEEN 60 AND 89 THEN (i.[InvoiceTotal]) ELSE 0 END AS [60Days]
    			,CASE WHEN DATEDIFF(dd,InvoiceDate,@DateCompare) > 90 THEN (i.[InvoiceTotal]) ELSE 0 END AS [90Days]
    			,@IncludePaid AS IsPaid
    		FROM [demo].[Northwind_Invoices] i
    	) t
    	WHERE [IsPaid] = @IncludePaid
    	GROUP BY [CustomerID]
    			,[InvoiceID] 
    			,[InvoiceNum]
    			,[InvoiceTotal]
    			,[Current]
    			,[30Days]
    			,[60Days]
    			,[90Days]
    			,[IsPaid]
    )
    -- Final Select statement
    SELECT
    	 c.[CustomerID]
    	,c.[CompanyName]
    	,c.[ContactName]
    	,c.[ContactTitle]
    	,c.[Country]
    	,i.[InvoiceID]
    	,i.[InvoiceNum]
    	,i.[InvoiceDate]
    	,i.[OrderTotal]
        ,i.[Freight]
        ,i.[InvoiceTotal]
    	,i.[BillName]
        ,i.[BillAddress]
        ,i.[BillCity]
        ,i.[BillCountry]
    	,i.[IsPaid]
    	,o.[OrderID]
    	,cte.[IsPaid]
    	,cte.[Current]
    	,cte.[30Days]
    	,cte.[60Days]
    	,cte.[90Days]
    	,p.[PaidAmount]
    	,n.[KeyValue] AS Note
    	,d.[KeyValue] AS ExpectedDate
    FROM [demo].[Northwind_Invoices] i
    LEFT JOIN [demo].[Northwind_Customers] c
    	ON i.[CustomerID] = c.[CustomerID]
    LEFT JOIN Invoice_CTE cte
    	ON cte.[InvoiceID] = i.[InvoiceID]
    LEFT JOIN demo.Northwind_Payments p
    	ON i.[InvoiceID] = p.[InvoiceID]
    LEFT JOIN demo.Northwind_Orders o
    	ON o.[CustomerID] = i.[CustomerID]
    	AND o.[Freight] = i.[Freight]
    LEFT JOIN demo.Northwind_InvoiceExternal n
    	ON n.[InvoiceID] = i.[InvoiceID]
    	AND n.[KeyName] = 'NOTE'
    LEFT JOIN demo.Northwind_InvoiceExternal d
    	ON d.[InvoiceID] = i.[InvoiceID]
    	AND d.[KeyName] = 'ExpectedDate'
    WHERE 
    	i.IsPaid = @IncludePaid
    	AND
    	(@CompanyName='' OR c.[CompanyName] LIKE '%' + @CompanyName + '%')
    	AND
    	(@ContactName='' OR c.[ContactName] LIKE '%' + @ContactName + '%')
    	AND
    	(@CustomerID='' OR c.[CustomerID] = @CustomerID)
    ORDER BY c.[CompanyName]
    		,i.[InvoiceDate]
    		,i.[InvoiceID]
    
    END

  


It is important to test the stored procedure in the database before testing it through the INTERJECT platform. Using Interject_RequestContext requires the test scripts to be much longer than in the previous steps. To help with this extra text INTERJECT will create the test code for you using the current users context. 

**Step 2:** First you must select a report formula that uses the data portal that is mapped to the stored procedure you want to test. You can quickly make a report formula and delete it since you are not creating the spreadsheet report yet. In a spreadsheet tab, in any cell, type **=ReportVariable("NorthwindCustomerInvoices",A42:A304,2:2,16:16,Param(H36,H37,H38,""))** but replace the data portal name with the name you created for your own example. Make sure the the cell with the ReportRange() formula is selected. 

![](attachments/324435969/328598112.png)

  


**Step 3:** Next, click **Advanced Menu** in the INTERJECT Ribbon. 

![](attachments/83689479/128892592.png)

This button is a toggle, so if it is currently showing **Simple Menu** the advanced menu is already showing. 

![](attachments/83689479/128336775.png)

  
**Step 4:** Click the **System** dropdown and select **View SQL Test for ActiveCell** . A window will pop up providing the developer with the SQL template used to create the stored procedure. 

![](attachments/324435969/328565047.png)

**Step 5:** Copy and paste the template code into the development environment, SQL Server Management Studio.   
The full text code is shown below. 

**Customer Invoices Test Script** Expand source 
    
    
    Execute [demo].[Northwind_Invoices_Pull_MyName]
    	@CompanyName = 'market'
    	,@ContactName = ''
    	,@CustomerID = ''
    	,@IncludePaid = ''
    	,@Interject_RequestContext = '<?xml version="1.0" encoding="utf-16" standalone="yes"?>
    <RequestContext>
        <ExcelVersion>16.0</ExcelVersion>
        <IdsVersion>2.3.0.11</IdsVersion>
        <FileName>Interject_CustomerDemo_v1.xlsx</FileName>
        <FilePath>C:\Users\MaryM\AppData\Local\Interject\FileCache</FilePath>
        <TabName>CustomerAgingDetail</TabName>
        <CellRange>H27</CellRange>
        <SourceFunction>Ranges</SourceFunction>
        <UtcOffset>-7</UtcOffset>
        <ColDefItems>
            <Value Row="2" Column="1">
                <Name>CustomerId</Name>
            </Value>
            <Value Row="2" Column="2">
                <Name>InvoiceID</Name>
            </Value>
            <Value Row="2" Column="9">
                <Name>InvoiceNum</Name>
            </Value>
            <Value Row="2" Column="10">
                <Name>OrderID</Name>
            </Value>
            <Value Row="2" Column="11">
                <Name>InvoiceDate</Name>
            </Value>
            <Value Row="2" Column="12">
                <Name>Current</Name>
            </Value>
            <Value Row="2" Column="13">
                <Name>30Days</Name>
            </Value>
            <Value Row="2" Column="14">
                <Name>60Days</Name>
            </Value>
            <Value Row="2" Column="15">
                <Name>90Days</Name>
            </Value>
            <Value Row="2" Column="18">
                <Name>ExpectedDate</Name>
            </Value>
            <Value Row="2" Column="20">
                <Name>Note</Name>
            </Value>
            <Value Row="2" Column="21">
                <Name>[Clear]</Name>
            </Value>
        </ColDefItems>
        <ResultDefItems />
        <RowDefItems>
            <Value Row="46" Column="1" ColumnName="CustomerId">
                <Name>BOTTM</Name>
            </Value>
            <Value Row="53" Column="1" ColumnName="CustomerId">
                <Name>BOTTM</Name>
            </Value>
            <Value Row="60" Column="1" ColumnName="CustomerId">
                <Name>BOTTM</Name>
            </Value>
            <Value Row="67" Column="1" ColumnName="CustomerId">
                <Name>BOTTM</Name>
            </Value>
            <Value Row="74" Column="1" ColumnName="CustomerId">
                <Name>GREAL</Name>
            </Value>
            <Value Row="81" Column="1" ColumnName="CustomerId">
                <Name>GREAL</Name>
            </Value>
            <Value Row="88" Column="1" ColumnName="CustomerId">
                <Name>GREAL</Name>
            </Value>
            <Value Row="95" Column="1" ColumnName="CustomerId">
                <Name>GREAL</Name>
            </Value>
            <Value Row="102" Column="1" ColumnName="CustomerId">
                <Name>SAVEA</Name>
            </Value>
            <Value Row="109" Column="1" ColumnName="CustomerId">
                <Name>SAVEA</Name>
            </Value>
            <Value Row="116" Column="1" ColumnName="CustomerId">
                <Name>SAVEA</Name>
            </Value>
            <Value Row="123" Column="1" ColumnName="CustomerId">
                <Name>SAVEA</Name>
            </Value>
            <Value Row="130" Column="1" ColumnName="CustomerId">
                <Name>WHITC</Name>
            </Value>
            <Value Row="137" Column="1" ColumnName="CustomerId">
                <Name>WHITC</Name>
            </Value>
            <Value Row="144" Column="1" ColumnName="CustomerId">
                <Name>WHITC</Name>
            </Value>
            <Value Row="151" Column="1" ColumnName="CustomerId">
                <Name>WHITC</Name>
            </Value>
        </RowDefItems>
        <UserContext>
        <MachineLoginName>MaryM</MachineLoginName>
        <MachineName>.</MachineName>
        <FullName> </FullName>
        <UserId>UUvP4HYoeu</UserId>
        <ClientId>CgCfW9qi</ClientId>
        <LoginName>MaryM@mycompany.com</LoginName>
        <LoginAuthTypeId>10</LoginAuthTypeId>
        <LoginDateUtc>05/03/2018 5:39:48</LoginDateUtc>
        <UserRoles>
            <Role>ClientAdmin</Role>
        </UserRoles>
    </UserContext>
        <UserContextEncrypted>Encrypted only through interject api protocol, not direct connection</UserContextEncrypted>
        <XMLDataToSave></XMLDataToSave>
    </RequestContext>'
    

  


**Step 7:** When this code is executed, it returns the following result set. 

![](attachments/324435969/328532284.png)

### 

###  Create The Report 

At this point you, have a tested a new stored procedure that uses parameters to filter the results. You set up an INTERJECT data connection to go to your example database and you added another INTERJECT data portal to use that connection, which is mapped to the stored procedure that you just created. So now you are ready to build the spreadsheet report using two data portals. 

The steps for building the spreadsheet report are in the lab [ Customer Aging Detail ](/wGetStarted/L3.4-Customer-Aging-Detail_128429387.html) . You have likely completed this in earlier training sessions. Repeat the instructions with your newly created data portals discussed in this topic. When you are done, your report should resemble the screenshot below. 

![](attachments/324435969/328597883.png)

### 

###  Creating a New Data Portal With Multiple Recordsets 

You just created a report that used ReportRange() to list all the customers with subtotaled regions. Then ReportVariable() was used to populate the invoices for each customer region. Two separate data portals were used and two connections were made to the database. 

To illustrate the multiple recordset feature of INTERJECT, you can take this one step further. You can copy the second data portal and stored procedure and modify it so that it returns both recordsets. In this approach, you make only one connection to the database, which is more efficient. And this process requires one less data portal and stored procedure to create. 

Multiple recordsets are a very efficient report approach when your data is not a simple list. In this example the feature will work as follows. On the first data request two recordsets are retrieved by INTERJECT. ReportRange() uses the customer summary list recordset but both recordsets temporarily remain in memory until all report formulas are completed. This allows the ReportVariable() to access the second recordset for populating the details in the same report run. The following steps will help you create this change yourself. 

**Step 1:** Navigate to the data portal that you just created , similar to **NorthwindCustomerInvoices_MyName** , and click the green clone button on the top right of the page. 

![](attachments/324435969/328532225.jpg)

  


**Step 2:** A new data portal named, **NorthwindCustomerInvoices_MyName_copy** , generates. Change this data portal name to **NorthwindMultiRecord_MyName** . You can add your name to the suffix, because each data portal code must be unique. 

![](attachments/324435969/328335666.jpg)

  


**Step 3:** Change the procedure name to run **[demo].[Northwind_CustomerInvoices_Pull_MyName]** but use your own name as the suffice. You will create this stored procedure shortly. Everything else in the cloned data portal remains the same. 

![](attachments/324435969/328597786.jpg)

  


### 

###  Updating the Stored Procedure for 2 Recordsets 

**Step 1:** In SQL Server Management Studio, open the stored procedure used in the report that pulled the invoice detail. The stored procedure name should be similar to [demo].[Northwind_Invoices_Pull_MyName]. 

![](attachments/324435969/328597796.png)

**Step 2:** Change the name of the stored procedure to [demo].[Northwind_CustomerInvoices_MyName], using your own name as the suffix. By using ‘Create procedure’ as shown below, the stored procedure will be copied to the new name when executed. 

![](attachments/324435969/328597801.png)

**Step 3:** Change the **Create procedure** back to **Alter procedure** and continue with editing the new procedure. 

**Step 4:** You have to make a few changes to the stored procedure so the summary record set showing a list of customers can be provided. First add **into #InvoiceDetail** as shown below. It will put the invoice detail in a temporary table to be used later in the stored procedure. 

![](attachments/324435969/328335685.png)

**Step 5:** After the SQL statement, add **Select * from #InvoiceDetail** . Then order by the CustomerID. This step returns the invoice detail as the first recordset from the stored procedure. 

**Step 6:** Next you must use the detail to generate a customer summary list. The below code should be copied into the bottom of the stored procedure. This code simply creates a distinct list of all the customers include in the invoice detail and orders by the customer name. 

Steps 5 and 6 should look like below: 

**Summary From Detail** Expand source 
    
    
    -- Select all detail from the dataset created above
    SELECT * FROM #InvoiceDetail
    ORDER BY [CustomerID]
    
    -- Select unique customers to form a summary list of all of the customers.
    SELECT DISTINCT 
    	 [CustomerID]
    	,[CompanyName]
    	,[ContactName]
    	,[ContactTitle]
    	,[Country] 
    FROM #InvoiceDetail
    ORDER BY CustomerID

  


**Step 7:** The changes to the stored procedure are complet. It is important to test the stored procedure in the database before testing it through the INTERJECT platform. You can use the same test script used earlier in this topic. Your test code should look similar to the SQL below. 

**MultiRecord Test Script** Expand source 
    
    
    Execute [demo].[Northwind_CustomerInvoices_Pull_MyName]
    	@CompanyName = 'market'
    	,@ContactName = ''
    	,@CustomerID = ''
    	,@IncludePaid = ''
    	,@Interject_RequestContext = '<?xml version="1.0" encoding="utf-16" standalone="yes"?>
    <RequestContext>
        <ExcelVersion>16.0</ExcelVersion>
        <IdsVersion>2.3.0.11</IdsVersion>
        <FileName>Interject_CustomerDemo_v1.xlsx</FileName>
        <FilePath>C:\Users\Marym\AppData\Local\Interject\FileCache</FilePath>
        <TabName>CustomerAgingDetail</TabName>
        <CellRange>H27</CellRange>
        <SourceFunction>Ranges</SourceFunction>
        <UtcOffset>-7</UtcOffset>
        <ColDefItems>
            <Value Row="2" Column="1">
                <Name>CustomerId</Name>
            </Value>
            <Value Row="2" Column="2">
                <Name>InvoiceID</Name>
            </Value>
            <Value Row="2" Column="9">
                <Name>InvoiceNum</Name>
            </Value>
            <Value Row="2" Column="10">
                <Name>OrderID</Name>
            </Value>
            <Value Row="2" Column="11">
                <Name>InvoiceDate</Name>
            </Value>
            <Value Row="2" Column="12">
                <Name>Current</Name>
            </Value>
            <Value Row="2" Column="13">
                <Name>30Days</Name>
            </Value>
            <Value Row="2" Column="14">
                <Name>60Days</Name>
            </Value>
            <Value Row="2" Column="15">
                <Name>90Days</Name>
            </Value>
            <Value Row="2" Column="18">
                <Name>ExpectedDate</Name>
            </Value>
            <Value Row="2" Column="20">
                <Name>Note</Name>
            </Value>
            <Value Row="2" Column="21">
                <Name>[Clear]</Name>
            </Value>
        </ColDefItems>
        <ResultDefItems />
        <RowDefItems>
            <Value Row="46" Column="1" ColumnName="CustomerId">
                <Name>BOTTM</Name>
            </Value>
            <Value Row="61" Column="1" ColumnName="CustomerId">
                <Name>BOTTM</Name>
            </Value>
            <Value Row="76" Column="1" ColumnName="CustomerId">
                <Name>BOTTM</Name>
            </Value>
            <Value Row="91" Column="1" ColumnName="CustomerId">
                <Name>BOTTM</Name>
            </Value>
            <Value Row="106" Column="1" ColumnName="CustomerId">
                <Name>GREAL</Name>
            </Value>
            <Value Row="117" Column="1" ColumnName="CustomerId">
                <Name>GREAL</Name>
            </Value>
            <Value Row="128" Column="1" ColumnName="CustomerId">
                <Name>GREAL</Name>
            </Value>
            <Value Row="139" Column="1" ColumnName="CustomerId">
                <Name>GREAL</Name>
            </Value>
            <Value Row="150" Column="1" ColumnName="CustomerId">
                <Name>SAVEA</Name>
            </Value>
            <Value Row="173" Column="1" ColumnName="CustomerId">
                <Name>SAVEA</Name>
            </Value>
            <Value Row="196" Column="1" ColumnName="CustomerId">
                <Name>SAVEA</Name>
            </Value>
            <Value Row="219" Column="1" ColumnName="CustomerId">
                <Name>SAVEA</Name>
            </Value>
            <Value Row="242" Column="1" ColumnName="CustomerId">
                <Name>WHITC</Name>
            </Value>
            <Value Row="258" Column="1" ColumnName="CustomerId">
                <Name>WHITC</Name>
            </Value>
            <Value Row="274" Column="1" ColumnName="CustomerId">
                <Name>WHITC</Name>
            </Value>
            <Value Row="290" Column="1" ColumnName="CustomerId">
                <Name>WHITC</Name>
            </Value>
        </RowDefItems>
        <UserContext>
        <MachineLoginName>MaryM</MachineLoginName>
        <MachineName>.</MachineName>
        <FullName> </FullName>
        <UserId>UUvP4HYoeu</UserId>
        <ClientId>CgCfW9qi</ClientId>
        <LoginName>Mary@mycompany.com</LoginName>
        <LoginAuthTypeId>10</LoginAuthTypeId>
        <LoginDateUtc>05/03/2018 5:39:48</LoginDateUtc>
        <UserRoles>
            <Role>ClientAdmin</Role>
        </UserRoles>
    </UserContext>
        <UserContextEncrypted>Encrypted only through interject api protocol, not direct connection</UserContextEncrypted>
        <XMLDataToSave></XMLDataToSave>
    </RequestContext>'

  


When this code is executed, it should return two recordsets as shown below. 

![](attachments/324435969/328532260.png)

### 

###  Updating the Report for 2 Recordsets 

You are ready to modify the report to use your new data portal. The changes are simple since you only need to use a new function, jDataPortal(), to specify the data portal recordset number for each report function. 

**Step 1:** In the **Customer Aging Detail** report that you just completed, change the **=ReportRange()** function by replacing the previous data portal with the new one. However, you will be encasing the new data portal inside a jDataPortal() function. So **=ReportRange(“oldDataPortalCode”,..** becomes **=ReportRange(jDataPortal(“NorthwindMultiRecord_MyName”,2),...** The end result should look like the below screenshot for ReportRange(). 

![](attachments/324435969/328401287.png)

The second parameter, DataResultNumber, indicates which recordset this report function will use. Using **2** causes the ReportRange() function to grab the second recordset that is a simple list of customers. 

**Step 4:** Now change the **=ReportVariable()** function by replacing the previous data portal with the new one. Again you must encase the new data portal inside a jDataPortal() function. So **=ReportVariable(“oldDataPortalCode”,..** becomes **=ReportVariable(jDataPortal(“NorthwindMultiRecord_MyName”,1),...** In this step you are using **1** so the first record set is used in this report function. The end result should look like the below screenshot for ReportVariable(). 

![](attachments/324435969/328401292.png)

  


**Step 5:** Once the report formulas are edited, you can re-pull the data in the report and the results should be the same as when it used two data portals. 

![](attachments/324435969/328532252.png)
