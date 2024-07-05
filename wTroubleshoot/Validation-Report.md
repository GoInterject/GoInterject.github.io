---
title: Validation Report
filename: "Validation-Report.md"
layout: custom
keywords: [report, error, user support, validation report, formula, parameters, functions, detailed information, code, events, triggers]
headings: ["Overview", "Validation Report Options", "Pull/Save Data Event", "Drill Event", "Clear Pull/Save Data Event", "Go Back Event", "Data Cell Functions", "Data Cell Last Change Report", "Cell Formula Review"]
links: ["/wIndex/Excel-Function-Index.html", "/wAbout/Tabular-vs-Data-Cells.html", "/wIndex/Event-Functions-Landing.html", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#advanced-menu-items", "/wIndex/Event-Functions-Landing.html", "/wIndex/ReportDrill.html", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#return-from-drill", "/wAbout/Tabular-vs-Data-Cells.html#data-cells", "/wIndex/Report-Formula-Reviews.html#cell-formula-review"]
image_dir: "ValidationReport"
images: [
    {file: "Ribbon", type: "png", site: "Add-in", cat: "Ribbon", sub: "", report: "", ribbon: "Advanced", config: ""}, 
    {file: "ValidationReportItems", type: "png", site: "Add-in", cat: "Ribbon", sub: "Validation Report", report: "", ribbon: "Advanced", config: ""}, 
    {file: "PullEvent", type: "png", site: "Add-in", cat: "Validation Report", sub: "Pull/Save Data Event", report: "", ribbon: "", config: ""}, 
    {file: "DrillEvent", type: "png", site: "Add-in", cat: "Validation Report", sub: "Drill Event", report: "", ribbon: "", config: ""}, 
    {file: "GoBackEvent", type: "png", site: "Add-in", cat: "Validation Report", sub: "Go Back Event", report: "", ribbon: "", config: ""}, 
    {file: "DataCells", type: "png", site: "Add-in", cat: "Validation Report", sub: "Data Cell Functions", report: "", ribbon: "", config: ""}, 
    {file: "RequestXML", type: "png", site: "Add-in", cat: "Validation Report", sub: "Data Cell Functions", report: "", ribbon: "", config: ""}, 
    {file: "CurrentFormulas", type: "png", site: "Add-in", cat: "Validation Report", sub: "Data Cell Functions", report: "", ribbon: "", config: ""}, 
    {file: "PreviouslyLoadedFormulas", type: "png", site: "Add-in", cat: "Validation Report", sub: "Data Cell Functions", report: "", ribbon: "", config: ""}, 
    {file: "ToggleDataCellAuditMode", type: "png", site: "Add-in", cat: "Diagnostics", sub: "Toggle DataCell Audit Mode", report: "", ribbon: "", config: ""}, 
    {file: "CurrentFormulasCellReferences", type: "png", site: "Add-in", cat: "Validation Report", sub: "Data Cell Functions", report: "", ribbon: "", config: ""}, 
    {file: "LastChangeReport", type: "png", site: "Add-in", cat: "Validation Report", sub: "Data Cell Last Change Report", report: "", ribbon: "", config: ""}
    ]
description: The Validation Report feature displays detailed information about Interject pull, save, and drill functions, data cell functions, and events.
---
* * *

## Overview

The Validation Report feature displays detailed information about Interject pull, save, and drill [functions](/wIndex/Excel-Function-Index.html), [data cell functions](/wAbout/Tabular-vs-Data-Cells.html), and [events](/wIndex/Event-Functions-Landing.html). It is a tool to help report writers see how specific report formulas behave by interpreting the report formula inputs. When developing report templates, there are often many Interject report formulas in a single template. The Validation Report can help analyze the order of execution for the report formulas. This ensures that Interject events occur in the intended order. The Validation Report also shows report writers how to check if a formula is included in the Interject execution plan. Finally, the Validation Report tool displays to writers which parameters are being included in every report formula on the report template.

The Validation Report is located on the [Advanced Menu](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#advanced-menu-items) of the Interject ribbon.

![](/images/ValidationReport/Ribbon.png)
<br>

By selecting any of the validation options, you can view the code behind each action. Detail information is given for selected ranges, data portals, parameters, formatting codes, and more. This helps users learn as well as diagnose code problems.

![](/images/ValidationReport/ValidationReportItems.png)
<br>

### Validation Report Options

The Validation Report can assist in analyzing Interject functions and events. For an overview on Interject events, see [Event Functions](/wIndex/Event-Functions-Landing.html).

* [**Pull Data Event**](#pullsave-data-event): Analyzes all functions triggered by a Pull-Run event
* [**Save Data Event**](#pullsave-data-event): Analyzes all functions triggered by a Save-Run event
* [**Drill Data Event**](#drill-event): Analyzes all functions triggered by a Data-Drill event
* [**Clear Pull Data Event**](#clear-pullsave-data-event): Analyzes all functions triggered by a Pull-Clear event
* [**Clear Save Data Event**](#clear-pullsave-data-event): Analyzes all functions triggered by a Save-Clear event
* [**Go Back Event**](#go-back-event): Analyzes all functions triggered by a Go-Back event
* [**Data Cell Function**](#data-cell-functions): Analyzes all Data Cell functions
* [**Data Cell Last Change Report**](#data-cell-last-change-report): Analyzes the changes and updates in the Data Cell functions
* [**Cell Formula Review**](#cell-formula-review): Analyzes a Report Formula

### Pull/Save Data Event

The Pull or Save Data Event will list detailed information for all Interject functions triggered by the Pull or Save Data event. Information shown includes:

* **Action** : Lists the name of the function and its location in the report. (Functions will be ran in the order they appear.)
* **On Actions** : The events that will trigger this function
* **Formula** : The formula text of the function
* **Instruction Range** : The range containing the instructions for the function
* **ErrorText** : Any logged errors with the event
* **Function Instruction (Parameters)** : Lists the parameters of the function in detail

![](/images/ValidationReport/PullEvent.png)
<br>

### Drill Event

The Drill Event command analyzes all [ReportDrill](/wIndex/ReportDrill.html) functions within the sheet. 

![](/images/ValidationReport/DrillEvent.png)
<br>

### Clear Pull/Save Data Event

This command will list all functions that will be triggered on a Clear Pull or Clear Save event. It displays information similar to the [Pull/Save Data Event](#pullsave-data-event).

### Go Back Event

Displays functions triggered by the [Go Back](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#return-from-drill) event (also called Return from Drill). (Note: This event is not currently functional.)

![](/images/ValidationReport/GoBackEvent.png)
<br>

### Data Cell Functions

Interject [data cells](/wAbout/Tabular-vs-Data-Cells.html#data-cells) focus on a single formula within the spreadsheet. The Data Cell Function option displays detailed information regarding data cells in the report so you can troubleshoot any issues.

![](/images/ValidationReport/DataCells.png)
<br>

This report contains 3 major sections:

* Request XML
* Current Formulas
* Previously Loaded formulas

**Request XML** shows exactly what is sent to the data portal in XML form.

![](/images/ValidationReport/RequestXML.png)
<br>

**Current Formulas** displays the current account balances within the data portal.

![](/images/ValidationReport/CurrentFormulas.png)
<br>

**Previously Loaded Formulas** will show the formulas loaded previously if any.

![](/images/ValidationReport/PreviouslyLoadedFormulas.png)
<br>

To display the cell references in the validation report, you can turn this option on in diagnostics by clicking "Toggle DataCell Audit Mode" and then **Execute Selected Action**:

![](/images/ValidationReport/ToggleDataCellAuditMode.png)
<br>

This will show the cell references in the Data Cell Functions report:


![](/images/ValidationReport/CurrentFormulasCellReferences.png)
<br>

### Data Cell Last Change Report

This option shows the changes made from the last pull to the current one including the source formula for the change.

![](/images/ValidationReport/LastChangeReport.png)
<br>

### Cell Formula Review

Interject's Cell Formula Review is useful for displaying detailed information about a selected formula. For more information, see [here](/wIndex/Report-Formula-Reviews.html#cell-formula-review).
