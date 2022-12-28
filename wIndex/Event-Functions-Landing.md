---
title: Event Functions
layout: custom
keywords: [event, functions, overview]
description: Event Functions are functions designed to run when a designated event triggers them.
---

## **Event Functions Overview**

Event Functions are functions designed to run when a designated event triggers them. The values defined within the Event Function parameters will determine what event will _enable_ these functions to run. The placement of these functions within the report will determine _when_ these functions will be executed. This allows for synchronization and data precision within the report.

There are four Interject events:

• Pull-Run: This occurs when selecting [**Pull Data**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) from the Pull Data window.

• Pull-Clear: This occurs when selecting [**Clear**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) from the Pull Data window.

• Save-Run: This occurs when selecting [**Save Data**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#save-data) from the Save Data window.

• Save-Clear: This occurs when selecting [**Clear Save Notes**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#save-data) from the Save Data window.
<br>
<br>
The placement of the Event Function is important to synchronize their execution in relation to other functions. For example, if the function is placed in a cell before a [Data Pull Function](wIndex/Data-Functions-Landing.html) and is set to execute upon a Pull-Run event, then selecting a ""Pull Data"" will cause the Event Function to run first and then the data is pulled via the Data Pull Function. The order of functions is determined row by row. For example, a function in C10 will be ran before a function in B11 because row 10 comes before row 11.