---
title: ReportGrouping()
layout: custom
keywords: [ReportGrouping, grouping, event, trigger, function, formula]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Trigger Combination List"]
description: The ReportGrouping function will collapse or expand groups within the sheet when triggered upon a designated event.
---
* * *

##  Function Summary

The ReportGrouping function will collapse or expand groups within the sheet when triggered upon a designated [event](wIndex/Event-Functions-Landing.html). This function is helpful in grouping or ungrouping sections in a [ReportVariable](/wIndex/ReportVariable.html) after it is generated.

For an example of this function, see [Lab Create: Inventory Variable Report](/wGetStarted/L-Create-InventoryVariable.html#reportgrouping).

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

<button class="collapsible-parameter">**RowOrColumnGroup**<br>A string indicating if row groupings will be acted upon or column groupings.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>"row", "column"</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**GroupLevel**<br>A string indicating to expand or collapse all groupings or an integer from 1 to 8 indicating what level the groups will be set to.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>"expand", "collapse", or 1 through 8</td>
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
=ReportGrouping("Both","Run","Column","Collapse",FALSE)
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =ReportGrouping()  |  The name of this function.  |  
|  OnPullSaveOrBoth  |  "Both"  |  A pull or save action are designated as the run event.  |  
|  OnClearRunOrBoth  |  "Run"  |  A run event (defined in OnPullSaveOrBoth) will trigger this function being ran.  |  
|  RowOrColumnGroup  |  "Column"  |  Only column groupings will be acted upon when this function is triggered.  |  
|  GroupLevel  |  "Collapse"  |  The column groupings will collapse upon being triggered.  |  
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
