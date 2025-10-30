---
title: ReportHideRowOrColumn()
filename: "ReportHideRowOrColumn.md"
layout: custom
keywords: [ReportHideRowOrColumn, hide, event, trigger, function, formula]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Trigger Combination List"]
links: ["/wFunctions/Event-Functions-Landing.html", "/wGetStarted/L-Create-HideRowCol.html"]
image_dir: ""
images: []
description: The ReportHideRowOrColumn function will hide a designated row or column when triggered upon a designated event.
---
* * *

##  Function Summary

The ReportHideRowOrColumn function will hide a designated row or column when triggered upon a designated [event](/wFunctions/Event-Functions-Landing.html). If a cell within the defined range = "hide", the function will hide that row or column when triggered. If the defined range is a single row, the function will hide the column. If this range is a single column, the function will hide the row.

Typically this function is used to hide data that is impertinent to the current purpose of the report and/or filters being used. For example, a user can set up a report to hide invoices with zero balances or to show only accounts with a delinquent status, etc. (Note: the rows/columns are not actually hidden in the sense that Excel hides them. They are hidden from view by setting their width/height to 0. A user can simply expand the hidden rows by expanding the width.)

For an example of this function, see [Lab Create: Hiding Rows & Columns](/wGetStarted/L-Create-HideRowCol.html).

###  Function Arguments

<button class="collapsible-parameter">**OnPullSaveOrBoth**<br>A string that defines what type of action(s) the event in OnClearRunOrBoth refer to: **Pull** action, **Save** action, or **Both** actions.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>"pull", "save", "both"</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**OnClearRunOrBoth**<br>A string indicating which event(s) will trigger this function: **Clear** event, **Run** event, or **Both** events.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>"clear", "run", "both"</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**RowOrColumnGroup**<br>A single row or column where the function will look for the value of "hide". If a cell in this range = "hide", the function will hide that row or column. If this range is a single row, the function will hide the column. If this range is a single column, the function will hide the row.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Must be a single row or single column</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Disabled**<br>True: This function will be disabled.<br><br>False: This function will be enabled.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Boolean</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td></td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>False</td>
    </tr>
  </tbody>
</table>
</div>

###  Excel Formula Bar Example

```Excel
=ReportHideRowOrColumn("Pull","Both",C47:C48,FALSE)
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =ReportHideRowOrColumn()  |  The name of this function.  |  
|  OnPullSaveOrBoth  |  "Both"  |  A pull or save action are designated as the run event.  |  
|  OnClearRunOrBoth  |  "Run"  |  A run event (defined in OnPullSaveOrBoth) will trigger this function being ran.  |  
|  RowOrColumnGroup  |  C47:C48  |  A cell value of "hide" in the range C47:C48 will hide that row when triggered.  |  
|  Disabled  |  FALSE  |  This function will run.  |  

###  Trigger Combination List

The execution of this function is determined by a combination of an Interject action and an Interject event. An action is a pull or save action whereas an event is a clear or run event. The values in the OnPullSaveOrBoth and OnClearRunOrBoth arguments will determine what actions/events trigger the function's execution.

| Trigger Combo  |  OnPullSaveOrBoth  |  OnClearRunOrBoth   |  Event Function Executes On  |
|------|------|------|------|
| 1  |  Pull  |  Clear   |  Pull-Clear  |
| 2  |  Save  |  Clear   |  Save-Clear  |
| 3  |  Both  |  Clear   |  Pull-Clear, Save-Clear  |
| 4  |  Pull  |  Run   |  Pull-Run  |
| 5  |  Save  |  Run   |  Save-Run  |
| 6  |  Both  |  Run   |  Pull-Run, Save-Run  |
| 7  |  Pull  |  Both   |  Pull-Run, Pull-Clear  |
| 8  |  Save  |  Both   |  Save-Run, Save-Clear  |
| 9  |  Both  |  Both   |  Pull-Run, Pull-Clear, Save-Run, Save-Clear  |
