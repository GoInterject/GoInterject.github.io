---
title: Event Functions
filename: "Event-Functions-Landing.md"
layout: custom
keywords: [event, functions, trigger]
headings: ["Overview", "ReportMacro", "ReportRun", "ReportCalc", "ReportDefaults", "ReportGrouping", "ReportHideRowOrColumn"]
links: ["/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#save-data", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#save-data", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#drill-on-data", "/wFunctions/Data-Functions-Landing.html", "/wTroubleshoot/Validation-Report.html", "/wFunctions/ReportMacro.html", "/wFunctions/ReportRun.html", "/wFunctions/ReportCalc.html", "/wFunctions/ReportDefaults.html", "/wFunctions/ReportGrouping.html", "/wFunctions/ReportVariable.html", "/wFunctions/ReportHideRowOrColumn.html"]
image_dir: ""
images: []
description: Event Functions are functions designed to run when a designated event triggers them.
---
* * *

## Overview

Event Functions are functions designed to run when a designated event triggers them. The values defined within the Event Function parameters will determine what event will _enable_ these functions to run. The placement of these functions within the report will determine _when_ these functions will be executed. This allows for synchronization and data precision within the report.

There are five Interject _events_:

• Pull-Run: This occurs when selecting [**Pull Data**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) from the Pull Data window.

• Pull-Clear: This occurs when selecting [**Clear**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) from the Pull Data window.

• Save-Run: This occurs when selecting [**Save Data**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#save-data) from the Save Data window.

• Save-Clear: This occurs when selecting [**Clear Save Notes**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#save-data) from the Save Data window.

• Data-Drill: This occurs when selecting a [**Drill on Data**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#drill-on-data) from the Data Drill window.

The placement of the Event Function is important to synchronize their execution in relation to other functions. For example, if the function is placed in a cell before a [Data Pull Function](/wFunctions/Data-Functions-Landing.html) and is set to execute upon a Pull-Run event, then selecting a "Pull Data" will cause the Event Function to run first and then the data is pulled via the Data Pull Function. The order of functions is determined row by row. For example, a function in C10 will be ran before a function in B11 because row 10 comes before row 11.

To view detailed information about the functions in your report that are triggered by these events, see [Validation Report](/wTroubleshoot/Validation-Report.html).

There are 6 Interject Event Functions: ReportMacro, ReportRun, ReportCalc, ReportDefaults, ReportGrouping, ReportHideRowOrColumn.

### [ReportMacro](/wFunctions/ReportMacro.html)

The ReportMacro function executes a designated VBA macro when triggered upon a designated event. 

### [ReportRun](/wFunctions/ReportRun.html)

The ReportRun function will run a designated report function(s) within a Workbook when triggered upon a designated event. This is typically used to synchronize the running of functions in other sheets within the Workbook. 

### [ReportCalc](/wFunctions/ReportCalc.html)

The ReportCalc function executes a calculation of formulas in a worksheet or workbook when triggered upon a designated event.

### [ReportDefaults](/wFunctions/ReportDefaults.html)

The ReportDefaults function will copy a value from a range to another range when triggered upon a designated event.

### [ReportGrouping](/wFunctions/ReportGrouping.html)

The ReportGrouping function will collapse or expand groups within the sheet when triggered upon a designated event. This function is helpful in grouping or ungrouping sections in a [ReportVariable](/wFunctions/ReportVariable.html) after it is generated.

### [ReportHideRowOrColumn](/wFunctions/ReportHideRowOrColumn.html)

The ReportHideRowOrColumn function will hide a designated row or column when triggered upon a designated event. If a cell within the defined range = "hide", the function will hide that row or column when triggered. If the defined range is a single row, the function will hide the column. If this range is a single column, the function will hide the row. Typically this function is used to hide data that is impertinent to the current purpose of the report and/or filters being used. For example, a user can set up a report to hide invoices with zero balances or to show only accounts with a delinquent status, etc.
