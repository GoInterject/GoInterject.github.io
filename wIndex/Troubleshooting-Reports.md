---
title: Interject Documentation > Troubleshooting Reports
layout: custom
keywords: [troubleshooting reports]
description: Report errors occur for many reasons, some of which relate to how the server handles data and moves it to the report. 
---
* * *

##  **Overview**
Report errors occur for many reasons, some of which relate to how the server handles data and moves it to the report. Other reasons may include the report's direct configuration within Excel. INTERJECT provides various tools and features to help quickly and accurately diagnose report errors.  Click one of the topics below to read more. 

  * ####  Investigating Errors In Reports with the Progress Window 

  * ####  Validation Report for INTERJECT Events 

  * ####  Reporting a Problem to INTERJECT 

  * ####  Verifying Parameters In a Report 

  * ####  Investigating Errors using Activity Logs 

  * ####  RAM Monitoring 

  * ####  Testing Data Connections 

  * ####  View SQL Test for ActiveCell 


###  Investigating Errors In Reports with Progress Window 
There are two types of errors that INTERJECT can display: unhandled and handled. Unhandled errors are system generated, whereas handled errors are written by developers.    
For example, on a pull or save, an error may occur on the server which the report is trying to access. This error could be handled by the developer, or it could be an unhandled error. Developers can handle errors quickly by using “UserNotice": [link to more info about how to use it]. When the error is handled by the developer, a popup message will display a friendly error text set by the developer. 

[screenshot of popup error]. 

  


If an unhandled error occurs, INTERJECT will still report the error, but no popup message will be displayed to the user. Instead, the Progress Window will stay open, showing a red X next to the failed dataportal call. 

[screenshot of red X] 

  


When that happens, users can double click the failed dataportal to see the exact error the server returned. 

[screenshot of window showing error message]. 

###  Validation Report for Pull/Save Events 

When developing report templates, there are often many report formulas on a single template. The Validation Report is a tool to help report writers see how specific report formulas behave by interpreting the report formula inputs. It assists writers when there are multiple formulas on a report, since it displays the order of execution for those report formulas. This ensures that INTERJECT events occur in the intended order. The Validation Report also shows report writers how to check if a formula is included in the INTERJECT execution plan. Finally, the Validation Report tool displays to writers which parameters are being included in every report formula on the report template. 

If evaluating ReportRange, ReportFixed, or ReportVariable then click  **Pull Data Event**

If evaluating ReportSave then click  **Save Data Event**

If evaluating ReportDrill then click  **Drill Data Event**

[paste the validation report here and annotate it with what each thing means] 

  


**Step 1:** In the [ INTERJECT Ribbon ](/wPortal/INTERJECT-Ribbon-Menu-Items_83689479.html) click the  **Validation Report** drop down (Click  **Advanced Menu** if you do not see the  **Formulas** section in the Interject Ribbon) 

(screenshot) 

  


**Step 2:** From the drop down menu, choose the item that best fits the type of report formulas in your report (i.e. Pull Data Event, Save Data Event, or Drill Data Event): 

(screenshot) 

  


The Formula Validation for Event window will open. From here you can analyze what INTERJECT will execute if you were to do a real pull/save/drill. Below is an example of a validation report for the pull event on the Customer Aging: 

(screenshot) 

###  Reporting a Problem to INTERJECT 

Use the Report a Problem feature to report a problem to the INTERJECT support team. Additionally, the problem can be described to an INTERJECT employee by directly contacting INTERJECT support. 

  


As long as verbose logging is turned on, Report a Problem can send user data and execution diagnostics to the INTERJECT support team. To use Report a Problem: 

**Step 1:** Click **User Support Help** from the INTERJECT Ribbon 

(screenshot) 

**Step 2:** Click the **Report a Problem** tab in the **INTERJECT - Support** popup window 

(screenshot) 

**Step 3:** Fill out the form with an Email and optional Name, Phone, and Description 

(screenshot) 

**Step 4:** Click **Send Report**

(screenshot) 

  


To contact INTERJECT support: 

**Step 1:** Click **User Support Help** from the INTERJECT Ribbon 

(screenshot) 

**Step 2:** Click the **Contact Interject** tab in the **INTERJECT - Support** popup window 

(screenshot) 

**Step 3:** Contact INTERJECT support via phone or email 

(screenshot) 

  


Some problems may occasionally require more extensive logging to identify and solve. For more information on **Reporting a Problem** using **Verbose Logging** see **Troubleshooting App Errors** . 

###  Verifying that Parameters in Report Formulas are Correctly Ordered   


**Cell Formula Review** is a feature used for analyzing  report  formulas and their parameters to check that values are correct. This feature has four different options to help analyze specific report formulas: 

  


Show Formula References: Displays the cell address for each formula parameter. 

[screenshot] 

Show Param Names: Displays text to the right of the formula describing what each formula parameter maps to in the data portal. This is very useful when troubleshooting parameters not being passed in correctly. 

[screenshot] 

Indent Data Cell Functions: Indents the formula parameters so they'll be more readable in the text-box. This is checked by default. 

[screenshot] 

Indent All Others: Indents the entire formula for readability. This is checked by default. 

[screenshot] 

  


When writing a report formula that requires data portal parameters, such as ReportRange(), Excel’s formula wizard does not show the mapping of the Param() formula to the data portal parameter. The formula wizard is limited to showing Value1, Value2, Value3, etc.. 

**[** Screenshot of Param() opened in formula wizard  **]** . 

  


It is possible to mis-order parameters within a formula. To verify that the correct cell values are being passed to the correct corresponding data portal parameter, use the Cell Formula Review. 

**Step 1:** Select the cell that has the Report Formula to review. 

[Screenshot] 

**Step 2:** In the INTERJECT Ribbon, click the  **Validation Report** drop down (Click  **Advanced Menu** if you do not see the  **Formulas** section in the INTERJECT Ribbon) 

(Screenshot) 

**Step 3:** From the drop down menu, click  **Cell Formula Review**

(Screenshot) 

###  Investigating Errors using Activity Logs 

You can use the Client Activity Dashboard to view user activity logs, and more specifically users' error logs. 

**Step 1:** Open the Client Activity Dashboard from the Interject report library. 

(Screenshot) 

**Step 2:** Navigate to the Error Detail tab and pull the report (the report will populate with information about the most recent user activity logs that contain errors). 

(Screenshot) 

**Step 3:** You can use the various filters and parameters on the report to refine the result set. This will help locate information for troubleshooting specific errors. 

(Screenshot) 

###  RAM Monitoring 

RAM monitoring is a toggled tool in an Excel report. When it is turned on, the memory use of the current workbook is recorded. When coupling this with **Report a Problem** , the RAM monitor is sent, along with the report, to INTERJECT support. To use RAM Monitoring: 

**Step 1:** Click Diagnostics on the INTERJECT Ribbon 

(Screenshot) 

**Step 2:** Select **Toggle Memory Logging** and click **Execute Selected Action**

(Screenshot) 

  


###  Testing Data Connections 

Before setting up a Data Connection to a Database, you can verify that the connection can be established within Excel. 

**Step 1:** With Excel open, go to the  INTERJECT Ribbon  menu and click  **Advanced Menu** (Skip this step if already in Advanced menu) 

(Screenshot) 

**Step 2:** Click  **System** drop-down, and select  **Check Connection**

(Screenshot) 

****Step 3:** ** In the text-box, paste the database connection string you will be using to configure the Data Connection. 

(Screenshot) 

When the connection functions properly, a message will be displayed, such as the one below. 

(Screenshot) 

  


###  View SQL Test for ActiveCell 

The **View SQL Test for ActiveCell** tool can be used to track down issues with the SQL stored procedures being called by an INTERJECT report function. Only ReportRange(), ReportVariable(), ReportFixed(), and ReportSave() report functions are supported by **View SQL Test for ActiveCell** . 

  


**Step 1:** Select a cell containing a supported INTERJECT report function. 

(screenshot) 

**Step 2:** On the **Administration** tab in the INTERJECT Ribbon, click **View SQL Test for ActiveCell** under the **System** drop-down menu. A popup window will appear with a test SQL query. 

(screenshot) 

  


This SQL query can be run using any T-SQL environment (i.e. _Microsoft SQL Server Management Studio_ ). Running the query in non-T-SQL environments may require modification of the query. The result will be a list of tables in SQL Server or an error message which can be used to see exactly what data is being pulled/saved to/from a report. 

  