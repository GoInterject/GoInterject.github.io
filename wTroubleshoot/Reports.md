---
title: Troubleshooting Reports
layout: custom
keywords: [ report, error, validation report, user support, progress window,cell formula, sql test ]
description:  INTERJECT provides various tools and features to help quickly and accurately diagnose report errors.
---
* * *

##  **Overview**

Report errors occur for many reasons, some of which relate to how the server handles data and moves it to the report. Other reasons may include the report's direct configuration within Excel. INTERJECT provides various tools and features to help quickly and accurately diagnose report errors.  Click one of the topics below to read more. 


###  Investigating Errors In Reports with Progress Window 

There are two types of errors that INTERJECT can display: unhandled and handled. Unhandled errors are system generated, whereas handled errors are written by developers.  For example, on a pull or save, an error may occur on the server which the report is trying to access. This error could be handled by the developer, or it could be an unhandled error. Developers can handle errors quickly by using “UserNotice": [link to more info about how to use it]. When the error is handled by the developer, a popup message will display a friendly error text set by the developer. For example a common error is the misspelling of a dataportal, which displays a handled error when pulling a report with a misspelled dataportal. 

![](/images/error-reports/01.jpg)

<br> 


If an unhandled error occurs, INTERJECT will still report the error, but no popup message will be displayed to the user. Instead, the Progress Window will stay open, showing a red X next to the failed dataportal call. 

![](/images/error-reports/02.jpg)

<br> 


When that happens, users can double click the failed dataportal to see the exact error the server returned. 

![](/images/error-reports/03.jpg)

###  Validation Report for Pull/Save Events 

When developing report templates, there are often many report formulas on a single template. The Validation Report is a tool to help report writers see how specific report formulas behave by interpreting the report formula inputs. It assists writers when there are multiple formulas on a report, since it displays the order of execution for those report formulas. This ensures that INTERJECT events occur in the intended order. The Validation Report also shows report writers how to check if a formula is included in the INTERJECT execution plan. Finally, the Validation Report tool displays to writers which parameters are being included in every report formula on the report template. 

If evaluating ReportRange, ReportFixed, or ReportVariable then click  **Pull Data Event**

If evaluating ReportSave then click  **Save Data Event**

If evaluating ReportDrill then click  **Drill Data Event**

Here is the example validation report for a pull data event on the customer aging report: 
    
    
                    Validation Report on event 'PULL' for tab 'CustomerAging' and selected cell 'E14'
    =========================================================================================
    ACTION ITEM:
    Action #1: [Cell C6] "ReportRange"
    On Actions: Pull,ClearPull
    Formula: =ReportRange("NorthwindCustomers",23:24,2:2,,Param(C17,C18,C19),TRUE,FALSE)
    Instruction Range: [Not entered]
    ErrorText: [No Errors] >>>>>>>>>> Data Range Instruction 
    
    <====== This section is the exact Instructions sent to Interject from the Report =======> 
    
    DataPortal: NorthwindCustomers <---Argument Setting in the Report Range Formula that defines the procedure that you are using to pull data from the database 
    
    Connection: <---The name of the database that you are connecting to 
    
    ColDefRange: 2:2 <---Argument Setting in the Report Range Formula that sets the location for the placement of columns from the database to Excel 
    
    TargetRange: 23:24 <---Argument Setting in the Report Range Formula that sets the location that Interject will populate data in 
    
    FormatRange: 23:23 <---Argument Setting in the Report Range Formula that sets the location of the Formatting Range for the report 
    
    Parameter String: Market^C17|^C18|^C19 <---Argument Setting in the Report Range Formula that sets where the Parameter Values on the Report are located 
    
    UseEntireRow: True <---Argument Setting in the Report Range Formula that defaults to "True" 
    
    PutFieldNamesAtTop: False <---Argument Setting in the Report Range Formula that defaults to "False" 
    
    RetainRowColumns: [Blank] <---Argument Setting in the Report Range Formula that defaults to "Blank" 
    
    InsertNewRowsWithin: False <---Argument Setting in the Report Range Formula that defaults to "False" 
    
    UseTopSpacerRow: False <---Argument Setting in the Report Range Formula that defaults to "False" 
    
    Parameter Break Out: <---This section defines the parameters 
    
    Formula Param Name [#1]: @CompanyName	<---This is the value of the first parameter defined in the parameter string 
    
    Input/Output: input <---Determines whether the parameter is an input or an output 
    
    DataType: nvarchar <---Determines the data type of the parameter 
    
    Input Errors: None <---Checks to see if there are errors on the input values for the parameter 
    
    Set Value: [Blank] <---Determines if the parameter has a default value "" 
    
    Formula Param Name [#2]: @ContactName	<---This is the value of the second parameter defined in the parameter string 
    
    Input/Output: input <---Determines the direction of the parameter 
    
    DataType: varchar <---Determines the data type of the parameter 
    
    Input Errors: None <---Checks to see if there are errors on the input values for the parameter 
    
    Set Value: [Blank] <---Determines if the parameter has a default value "" 
    
    Formula Param Name [#3]: @CustomerID	<---This is the value of the third parameter defined in the parameter string 
    
    Input/Ouput: input <---Determines the data type of the parameter 
    
    DataType: varchar <---Determines the data type of the parameter 
    
    Input Errors: None <---Checks to see if there are errors on the input values for the parameter 
    
    Set Value: [Blank] <---Determines if the parameter has a default value "" 
    >>>> System Params Not in Formula 
    <=====This section details the system parameters set in the dataportal=====> 
    System Param Name: @Interject_NTLogin 
    Input/Ouput: input 
    DataType: varchar Length: 0 Set Value: [Blank] "" 
    System Param Name: @Interject_LocalTimeZoneOffset 
    Input/Output: input 
    DataType: money Length: 0 Set Value: [Blank] "" 
                  

Open the report you need to troubleshoot, this example will use the [ CustomerAging ](/KB/HowToCreate/ModifyReport/CustomerAging.html) report. 

**Step 1:** In the [ INTERJECT Ribbon ](/KB/InterjectRibbon.html) click the  **Validation Report** drop down (Click  **Advanced Menu** if you do not see the  **Formulas** section in the Interject Ribbon) 

![](/images/error-reports/04.jpg)

<br> 


**Step 2:** From the drop down menu, choose the item that best fits the type of report formulas in your report (i.e. Pull Data Event, Save Data Event, or Drill Data Event): 

![](/images/error-reports/05.jpg)

<br> 


The Formula Validation for Event window will open. From here you can analyze what INTERJECT will execute if you were to do a real pull/save/drill. Below is an example of a validation report for the pull event on the Customer Aging: 

![](/images/error-reports/06.jpg)

<br> 


###  Reporting a Problem to INTERJECT 

Use the Report a Problem feature to report a problem to the INTERJECT support team. Additionally, the problem can be described to an INTERJECT employee by directly contacting INTERJECT support. 

  


As long as verbose logging is turned on, Report a Problem can send user data and execution diagnostics to the INTERJECT support team. To use Report a Problem: 

**Step 1:** Click **User Support Help** from the INTERJECT Ribbon. 

![](/images/error-reports/07.jpg)

<br> 


**Step 2:** Click the **Report a Problem** tab in the **INTERJECT - Support** popup window. 

![](/images/error-reports/08.jpg)

<br> 


**Step 3:** Fill out the form with an Email and optional Name, Phone, and Description then Click **Send Report.**

![](/images/error-reports/09.jpg)

<br> 


To contact INTERJECT support: 

**Step 1:** Click **User Support Help** from the INTERJECT Ribbon 

![](/images/error-reports/10.jpg)

<br> 


**Step 2:** Click the **Contact Interject** tab in the **INTERJECT - Support** popup window 

![](/images/error-reports/11.jpg)

<br> 


**Step 3:** Contact INTERJECT support via phone or email 

![](/images/error-reports/12.jpg)

<br> 


Some problems may occasionally require more extensive logging to identify and solve. For more information on **Reporting a Problem** using **Verbose Logging** see [ Troubleshooting App Errors ](/KB/HowToDevelop/Troubleshooting/AppErrors.html). 

###  Verifying that Parameters in Report Formulas are Correctly Ordered   


**Cell Formula Review** is a feature used for analyzing  report  formulas and their parameters to verify that report formulas are correct. This feature has four different options to help analyze specific report formulas: 

When writing a report formula that requires data portal parameters, such as ReportRange(), Excel’s formula wizard does not show the mapping of the Param() formula to the data portal parameter. The formula wizard is limited to showing Value1, Value2, Value3, etc.. 

![](/images/error-reports/13.jpg)

<br> 


It is possible to mis-order parameters within a formula. To verify that the correct cell values are being passed to the correct corresponding data portal parameter, use the Cell Formula Review. 

**Step 1:** Select the cell that has the Report Formula to review.  In the INTERJECT Ribbon, click the  **Validation Report** drop down (Click  **Advanced Menu** if you do not see the  **Formulas** section in the INTERJECT Ribbon) 

![](/images/error-reports/14.jpg)

<br> 


**Step 2:** From the drop down menu, click  **Cell Formula Review**

![](/images/error-reports/15.jpg)

<br> 


Show Formula References: Displays the cell address for each formula parameter. 

![](/images/error-reports/16.jpg)

<br> 


Show Param Names: Displays text to the right of the formula describing what each formula parameter maps to in the data portal. This is very useful when troubleshooting parameters not being passed in correctly. 

![](/images/error-reports/17.jpg)

<br> 


Indent Data Cell Functions: Indents the formula parameters so they'll be more readable in the text-box. This is checked by default. 

![](/images/error-reports/18.jpg)

<br> 


Indent All Others: Indents the entire formula for readability. This is checked by default. 

![](/images/error-reports/19.jpg)

###  Investigating Errors using Activity Logs 

You can use the Client Activity Dashboard to view user activity logs, and more specifically users' error logs. 

**Step 1:** Open the Client Activity Dashboard from the Interject report library. 

![](/images/error-reports/20.jpg)

<br> 


**Step 2:** Navigate to the Error Log tab and pull the report (the report will populate with information about the most recent user activity logs that contain errors). 

![](/images/error-reports/21.jpg)

<br> 


**Step 3:** You can use the various filters and parameters on the report to refine the result set. This will help locate information for troubleshooting specific errors. 

![](/images/error-reports/22.jpg)

###  RAM Monitoring 

RAM monitoring is a toggled tool in an Excel report. When it is turned on, the memory use of the current workbook is recorded. When coupling this with **Report a Problem**, the RAM monitor is sent, along with the report, to INTERJECT support. To use RAM Monitoring: 

**Step 1:** Click Diagnostics on the INTERJECT Ribbon 

![](/images/error-reports/23.jpg)

<br> 


**Step 2:** Select **Toggle Memory Logging** and click **Execute Selected Action**

![](/images/error-reports/24.jpg)

<br> 


###  Testing Data Connections 

Before setting up a Data Connection to a Database, you can verify that the connection can be established within Excel. 

**Step 1:** With Excel open, go to the  INTERJECT Ribbon  menu and click  **Advanced Menu** (Skip this step if already in Advanced menu) 

![](/images/error-reports/25.jpg)

<br> 


**Step 2:** Click  **System** drop-down, and select  **Check Connection**

![](/images/error-reports/26.jpg)

<br> 


**Step 3:** In the text-box, paste the database connection string you will be using to configure the Data Connection. 

![](/images/error-reports/27.jpg)

<br> 


When the connection functions properly, a message will be displayed, such as the one below. 

![](/images/error-reports/28.jpg)

<br> 


###  View SQL Test for ActiveCell 

The **View SQL Test for ActiveCell** tool can be used to track down issues with the SQL stored procedures being called by an INTERJECT report function. Only ReportRange(), ReportVariable(), ReportFixed(), and ReportSave() report functions are supported by **View SQL Test for ActiveCell**. 

  


**Step 1:** Select a cell containing a supported INTERJECT report function. 

![](/images/error-reports/29.jpg)

<br> 


**Step 2:** On the **Administration** tab in the INTERJECT Ribbon, click **View SQL Test for ActiveCell** under the **System** drop-down menu. A popup window will appear with a test SQL query. 

![](/images/error-reports/30.jpg)

<br> 


This SQL query can be run using any T-SQL environment (i.e. _Microsoft SQL Server Management Studio_ ). Running the query in non-T-SQL environments may require modification of the query. The result will be a list of tables in SQL Server or an error message which can be used to see exactly what data is being pulled/saved to/from a report. 

  

