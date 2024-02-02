---
title: Report Errors
filename: "Reports.md"
layout: custom
keywords: [report, errors, validation report, user support, progress window, cell formula, sql test]
headings: ["Overview", "Investigating Report Errors", "Validation Report for Interject Events", "Testing Data Connections", "View SQL Test for ActiveCell"]
links: ["/wTroubleshoot/Investigating-Errors.html", "/wTroubleshoot/Validation-Report.html", "/wTroubleshoot/Testing-Data-Connections.html", "/wTroubleshoot/View-SQL.html"]
image_dir: ""
images: []
description: Report errors occur for many reasons, some of which relate to how the server handles data and moves it to the report. Other reasons may include the report's direct configuration within Excel. Interject provides various tools and features to help quickly and accurately diagnose report errors.
---
* * *

## Overview

Report errors occur for many reasons, some of which relate to how the server handles data and moves it to the report. Other reasons may include the report's direct configuration within Excel. Interject provides various tools and features to help quickly and accurately diagnose report errors. Click one of the topics below to read more.

### [Investigating Report Errors](/wTroubleshoot/Investigating-Errors.html)

Two tools useful in investigating report errors are the Progress Bar Window and the Client Activity Dashboard. The Interject Progress Bar Window appears when processing data. When an error occurs, it will display information related to the error. The Client Activity Dashboard is an Excel file setup to generate information regarding activity, Data Portal usage, user details, version reports, and error logs.

### [Validation Report for Interject Events](/wTroubleshoot/Validation-Report.html)

The Validation Report is a tool to help report writers see how specific report formulas behave by interpreting the report formula inputs. When developing report templates, there are often many Interject report formulas in a single template. The Validation Report can help analyze the the order of execution for the report formulas. This ensures that Interject events occur in the intended order. The Validation Report also shows report writers how to check if a formula is included in the Interject execution plan. Finally, the Validation Report tool displays to writers which parameters are being included in every report formula on the report template.

### [Testing Data Connections](/wTroubleshoot/Testing-Data-Connections.html)

Before setting up a Data Connection to a Database, you can verify that the connection can be established within Excel by accessing the Check Connection window.

### [View SQL Test for ActiveCell](/wTroubleshoot/View-SQL.html)

The View SQL Test for ActiveCell tool can be used to track down issues with the SQL stored procedures being called by an Interject report function. Only ReportRange(), ReportVariable(), ReportFixed(), and ReportSave() report functions are supported by View SQL Test for ActiveCell.
