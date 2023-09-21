---
title: Validation Report for Interject Events
layout: custom
keywords: [report, error, user support, validation report, formula, parameters]
description: The Validation Report is a tool to help report writers see how specific report formulas behave by interpreting the report formula inputs.
---
* * *

## Overview

The Validation Report is a tool to help report writers see how specific report formulas behave by interpreting the report formula inputs. When developing report templates, there are often many Interject report formulas in a single template. The Validation Report can help analyze the the order of execution for the report formulas. This ensures that Interject events occur in the intended order. The Validation Report also shows report writers how to check if a formula is included in the Interject execution plan. Finally, the Validation Report tool displays to writers which parameters are being included in every report formula on the report template.

![](/images/error-reports/ValidationReportMenu.png)
<br>

### The Validation Report

The Validation Report can assist in analyzing Interject functions and events. For an overview on Interject events, see [here](/wIndex/Event-Functions-Landing.html).

* **Pull Data Event**: Analyzes all functions triggered by a Pull-Run event.
* **Save Data Event**: Analyzes all functions triggered by a Save-Run event.
* **Drill Data Event**: Analyzes all functions triggered by a Data-Drill event.
* **Clear Pull Data Event**: Analyzes all functions triggered by a Pull-Clear event.
* **Clear Save Data Event**: Analyzes all functions triggered by a Save-Clear event.
* **Go Back Event**: Analyzes all functions triggered by a [Go-Back](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#return-from-drill) event.
* **Data Cell Function**: Analyzes all [Data Cell](/wIndex/Data-Cell-Functions.html) functions.
* **Data Cell Last Change Report**: Analyzes the changes and updates in the [Data Cell](/wIndex/Data-Cell-Functions.html) functions.
* **Cell Formula Review**: [Analyzes a Report Formula](/wIndex/Report-Formula-Reviews.html).



### Pull Data Event Example

Open the report you need to troubleshoot. This example will use the [CustomerAging](/wGetStarted/L-Create-CustomerAging.html) report.

**Step 1:** In the [Interject Ribbon](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html), click the **Validation Report** drop down (Click **Advanced Menu** if you do not see this):

![](/images/error-reports/04.jpg)
<br>

**Step 2:** From the drop down menu, choose the item that best fits the type of report formulas in your report (i.e. Pull Data Event, Save Data Event, or Drill Data Event):

![](/images/error-reports/05.jpg)
<br>

The Formula Validation for Event window will open. From here you can analyze what Interject will execute if you were to do a real pull/save/drill. Below is an example of a validation report for the pull event on the Customer Aging.

![](/images/error-reports/06.jpg)
<br>

### Verify Formula Parameters

**Cell Formula Review** is a feature used for analyzing report formulas and their parameters to verify that report formulas are correct. This feature has four different options to help analyze specific report formulas:

* Show Formula References
* Show Param Names
* Indent Data Cell Functions
* Indent All Others

![](/images/error-reports/FormulatReviewWindow.png)
<br>

When writing a report formula that requires data portal parameters, such as ReportRange(), Excel’s formula wizard does not show the mapping of the Param() formula to the data portal parameter. The formula wizard is limited to showing Value1, Value2, Value3, etc.

![](/images/error-reports/13.jpg)
<br>

It is possible to mis-order parameters within a formula. To verify that the correct cell values are being passed to the correct corresponding data portal parameter, use the Cell Formula Review.

**Step 1:** Select the cell that has the Report Formula to review. In the Interject Ribbon, click the **Validation Report** drop down (Click **Advanced Menu** if you do not see the **Formulas** section in the Interject Ribbon).

![](/images/error-reports/14.jpg)
<br>

**Step 2:** From the drop down menu, click **Cell Formula Review**.

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
<br>
