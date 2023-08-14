---
title: "Create: Interject Run On Open"
layout: custom
keywords: [autorun, RunOnOpen, run, pull, property]
description: Use this property to auto-pull the report when opening for the first tab that appears. No VBA required.
---
* * *

## Overview

Some reports require default values, settings, or have summary pages that must be pulled before others in order for the report to function properly. Using the Run on Open Interject property will auto-run the first tab that appears. This can save time and helps streamline Interject processes.

We will walk through Run on Open using the [Customer Aging Report](/wGetStarted/L-Create-CustomerAging.html).

<blockquote class=lab_info>
 If you are following the Training Labs, this report file can be found in the Report Library at Training Labs > Lab 6 Special Features > Lab 6.4 Interject Run On Open.
</blockquote>

### Setting up Run on Open via Diagnostics

The [Diagnostics](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#diagnostics) window provides an easy way to set up the run on open feature. It also provides many more ways to customize this feature. To setup the feature you need to input the correct code in the Input field and click **Execute Selected Action**.

![](/images/L-Create-RunOnOpen/DiagnosticsRunOnOpen.png)
<br>

### RunOnOpen Input Syntax

| Code | Description |
|---|---|
| T: | Designates an Excel Tab (followed by the name of a tab) |
| F: | Designates a report Formula (followed by a cell reference or a named range) |
| RunOnce | Runs the designated report once and then turns off the setting |
| Prompt | Opens the Pull Data window upon file open |
| Test= | Executes the code that follows in test mode and displays results |
| ! | The exclamation symbol negates or excludes an action |
| \| | The pipe symbol is used to connect two pieces of code (e.g. a tab and a cell) |
| , | The comma is used to enter multiple codes |

### RunOnOpen Examples Codes

| Examples | Description |
| --- | --- |
| T:Sheet1 | Will run all report formulas in the sheet "Sheet1" |
| T:Sheet1\|F:A5 | Will run the report formula in cell A5 in Sheet "Sheet1" |
| T:Sheet1\|F:!A5 | Will run all report formulas in the sheet "Sheet1" except for the formula in cell A5 |
| F:A5 | Will run the report formula in cell A5 in the active sheet |
| F:CellName | Will run the report formula in the range name "CellName" |
| RunOnce,T:Sheet1 | Will run all report formulas in the sheet "Sheet1" and then turn off the setting |
| RunOnce,F:A5 | Will run the report formula in cell A5 in the active sheet and then turn off the setting |
| T:Sheet1,T:Sheet2\|F:CellName | Will run the report formulas in "Sheet1" and then in "Sheet2" and then in the range name "CellName" |
| Prompt | Will open the Pull Data window when the file opens |
| Test= true | Displays information in Results as if RunOnOpen was actually executed |
| Test= F:A5 | Displays information in Results as if the formula in A5 was executed as RunOnOpen |

### RunOnOpen Example

**Step 1:** To begin, open the **Customer Collections** report in the [Report Library](/wAbout/Report-Library-Basics.html).

![](/images/L-Create-RunOnOpen/CustomCollectionsReportLibrary.png)
<br>

**Step 2:** Click on the Advanced Menu if it is not already displayed.

![](/images/L-Create-RunOnOpen/AdvancedMenu.png)
<br>

**Step 3:** Click on **Diagnostics**.

![](/images/L-Create-RunOnOpen/Diagnostics.png)
<br>

**Step 4:** The RunOnOpen feature is located on the System Tools folder of the Diagnostics. Input **F:C6** in the Input field and click **Execute Selected Action**.

![](/images/L-Create-RunOnOpen/EnterCode.png)
<br>

**Step 5:** Save the file and reopen it to find the report automatically runs the report formula found in cell C6.

![](/images/L-Create-RunOnOpen/08.png)
<br>
