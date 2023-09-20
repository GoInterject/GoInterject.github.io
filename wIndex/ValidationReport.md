---
title: Validation Report
layout: custom
keywords: [functions, formula, detailed information, code, events, triggers]
description: The Validation Report feature displays detailed information about Interject pull, save, and drill functions, data cell functions, and events.
---
* * *

## Overview

The Validation Report feature displays detailed information about Interject [pull, save, and drill functions](/wIndex/Excel-Function-Index.html), [data cell functions](/wAbout/Tabular-vs-Data-Cells.html), and [events](/wIndex/Event-Functions-Landing.html).

The Validation Report is located on the [Advanced Menu](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#advanced-menu-items) of the Interject ribbon.

![](/images/ValidationReport/Ribbon.png)
<br>

By selecting any of the validation options, you can view the code behind each action. Detail information is given for selected ranges, data portals, parameters, formatting codes, and more. This helps users learn as well as diagnose code problems.

![](/images/ValidationReport/ValidationReportItems.png)
<br>

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

This command will list all functions that will be triggered on a Clear Pull or Clear Save event. It displays information similar to the [Pull/Save Data Event](#pull-save-data-event).

### Go Back Event

Displays functions triggered by the [Go Back](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#return-from-drill) event. This event is not currently functional.

![](/images/ValidationReport/GoBackEvent.png)
<br>

### Data Cell Functions



### Data Cell Last Change Report


### Cell Formula Review


[here](/wIndex/Report-Formula-Reviews.html) 