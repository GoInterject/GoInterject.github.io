---
title: Troubleshooting Reports
layout: custom
keywords: [ report, error, validation report, user support, progress window,cell formula, sql test ]
description:  Interject provides various tools and features to help quickly and accurately diagnose report errors.
---
* * *

##  **Overview**

Report errors occur for many reasons, some of which relate to how the server handles data and moves it to the report. Other reasons may include the report's direct configuration within Excel. Interject provides various tools and features to help quickly and accurately diagnose report errors.  Click one of the topics below to read more. 


###  Investigating Errors In Reports with Progress Window 

There are two types of errors that Interject can display: unhandled and handled. Unhandled errors are system generated, whereas handled errors are written by developers.  For example, on a pull or save, an error may occur on the server which the report is trying to access. This error could be handled by the developer, or it could be an unhandled error. Developers can handle errors quickly by using “UserNotice": [Read about UserNotice here](https://docs.gointerject.com/wGetStarted/L-Dev-Error-Handling.html). When the error is handled by the developer, a popup message will display a friendly error text set by the developer. For example a common error is the misspelling of a dataportal, which displays a handled error when pulling a report with a misspelled dataportal. 

![](/images/error-reports/01.jpg)

<br> 


If an unhandled error occurs, Interject will still report the error, but no popup message will be displayed to the user. Instead, the Progress Window will stay open, showing a red X next to the failed dataportal call. 

![](/images/error-reports/02.jpg)

<br> 


When that happens, users can double click the failed dataportal to see the exact error the server returned. 

![](/images/error-reports/03.jpg)

###  Validation Report for Pull/Save Events 

When developing report templates, there are often many report formulas on a single template. The Validation Report is a tool to help report writers see how specific report formulas behave by interpreting the report formula inputs. It assists writers when there are multiple formulas on a report, since it displays the order of execution for those report formulas. This ensures that Interject events occur in the intended order. The Validation Report also shows report writers how to check if a formula is included in the Interject execution plan. Finally, the Validation Report tool displays to writers which parameters are being included in every report formula on the report template. 

If evaluating ReportRange, ReportFixed, or ReportVariable then click  **Pull Data Event**

If evaluating ReportSave then click  **Save Data Event**

If evaluating ReportDrill then click  **Drill Data Event**

Open the report you need to troubleshoot, this example will use the [ CustomerAging ](/wGetStarted/L-Create-CustomerAging.html) report. 

**Step 1:** In the [ Interject Ribbon ](/wGetStarted/Interject-Ribbon-Menu-Items.html) click the  **Validation Report** drop down (Click  **Advanced Menu** if you do not see the  **Formulas** section in the Interject Ribbon) 

![](/images/error-reports/04.jpg)

<br> 


**Step 2:** From the drop down menu, choose the item that best fits the type of report formulas in your report (i.e. Pull Data Event, Save Data Event, or Drill Data Event): 

![](/images/error-reports/05.jpg)

<br> 


The Formula Validation for Event window will open. From here you can analyze what Interject will execute if you were to do a real pull/save/drill. Below is an example of a validation report for the pull event on the Customer Aging: 

![](/images/error-reports/06.jpg)

<br> 


###  Reporting a Problem to Interject 

Use the Report a Problem feature to report a problem to the Interject support team. Additionally, the problem can be described to an Interject employee by directly contacting Interject support. 

  


As long as verbose logging is turned on, Report a Problem can send user data and execution diagnostics to the Interject support team. To use Report a Problem: 

**Step 1:** Click **User Support Help** from the Interject Ribbon. 

![](/images/error-reports/07.jpg)

<br> 


**Step 2:** Click the **Report a Problem** tab in the **Interject - Support** popup window. 

![](/images/error-reports/08.jpg)

<br> 


**Step 3:** Fill out the form with an Email and optional Name, Phone, and Description then Click **Send Report.**

![](/images/error-reports/09.jpg)

<br> 


To contact Interject support: 

**Step 1:** Click **User Support Help** from the Interject Ribbon 

![](/images/error-reports/10.jpg)

<br> 


**Step 2:** Click the **Contact Interject** tab in the **Interject - Support** popup window 

![](/images/error-reports/11.jpg)

<br> 


**Step 3:** Contact Interject support via phone or email 

![](/images/error-reports/12.jpg)

<br> 


Some problems may occasionally require more extensive logging to identify and solve. For more information on **Reporting a Problem** using **Verbose Logging** see [ Troubleshooting App Errors ](/wTroubleshoot/App-Errors.html). 

###  Verifying that Parameters in Report Formulas are Correctly Ordered   


**Cell Formula Review** is a feature used for analyzing  report  formulas and their parameters to verify that report formulas are correct. This feature has four different options to help analyze specific report formulas: 

When writing a report formula that requires data portal parameters, such as ReportRange(), Excel’s formula wizard does not show the mapping of the Param() formula to the data portal parameter. The formula wizard is limited to showing Value1, Value2, Value3, etc.. 

![](/images/error-reports/13.jpg)

<br> 


It is possible to mis-order parameters within a formula. To verify that the correct cell values are being passed to the correct corresponding data portal parameter, use the Cell Formula Review. 

**Step 1:** Select the cell that has the Report Formula to review.  In the Interject Ribbon, click the  **Validation Report** drop down (Click  **Advanced Menu** if you do not see the  **Formulas** section in the Interject Ribbon) 

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

RAM monitoring is a toggled tool in an Excel report. When it is turned on, the memory use of the current workbook is recorded. When coupling this with **Report a Problem**, the RAM monitor is sent, along with the report, to Interject support. To use RAM Monitoring: 

**Step 1:** Click Diagnostics on the Interject Ribbon 

![](/images/error-reports/23.jpg)

<br> 


**Step 2:** Select **Toggle Memory Logging** and click **Execute Selected Action**

![](/images/error-reports/24.jpg)

<br> 


###  Testing Data Connections 

Before setting up a Data Connection to a Database, you can verify that the connection can be established within Excel. 

**Step 1:** With Excel open, go to the  Interject Ribbon  menu and click  **Advanced Menu** (Skip this step if already in Advanced menu) 

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

The **View SQL Test for ActiveCell** tool can be used to track down issues with the SQL stored procedures being called by an Interject report function. Only ReportRange(), ReportVariable(), ReportFixed(), and ReportSave() report functions are supported by **View SQL Test for ActiveCell**. 

  


**Step 1:** Select a cell containing a supported Interject report function. 

![](/images/error-reports/29.jpg)

<br> 


**Step 2:** On the **Administration** tab in the Interject Ribbon, click **View SQL Test for ActiveCell** under the **System** drop-down menu. A popup window will appear with a test SQL query. 

![](/images/error-reports/30.jpg)

<br> 


This SQL query can be run using any T-SQL environment (i.e. _Microsoft SQL Server Management Studio_ ). Running the query in non-T-SQL environments may require modification of the query. The result will be a list of tables in SQL Server or an error message which can be used to see exactly what data is being pulled/saved to/from a report. 

  

[1]:/images/error-reports/S1.txt