---
title: ReportRun()
filename: "ReportRun.md"
layout: custom
keywords: [ReportRun, run, event, trigger, function, formula]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Trigger Combination List"]
links: ["/wFunctions/Event-Functions-Landing.html", "/wGetStarted/L-Create-PivotTable.html", "/wFunctions/Data-Functions-Landing.html", "/wFunctions/Event-Functions-Landing.html", "#function-composition"]
image_dir: ""
images: []
description: The ReportRun function will run a designated report function(s) within a Workbook when triggered upon a designated event.
---
* * *

##  Function Summary

The ReportRun function will run a designated report function(s) within a Workbook when triggered upon a designated [event](/wFunctions/Event-Functions-Landing.html). This is typically used to synchronize the running of functions in other sheets within the Workbook. 

For an example of this function, see [Working with Pivot Tables](/wGetStarted/L-Create-PivotTable.html).

###  Function Arguments

<button class="collapsible-parameter">**ReportCellToRun**<br>A cell address in a worksheet within your report that contains an Interject [Data](/wFunctions/Data-Functions-Landing.html) or [Event](/wFunctions/Event-Functions-Landing.html) function.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td></td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Will not run a report</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**RunEntireWorksheet**<br>True: Will run all the report functions located in the sheet specified in ReportCellToRun.<br><br>False: Will only run the report function designated in ReportCellToRun.</button>
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
		<td>True</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**OnAction**<br>A string indicating which event(s) will trigger this function (see table [below](#function-composition) for events).</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>"pull", "save", "pullandsave", "pullclear", "saveclear", "pullandsaveclear"</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>"pull"</td>
    </tr>
  </tbody>
</table>
</div>


###  Excel Formula Bar Example

```Excel
=ReportRun(ReportRunTargetForPivot!C4,TRUE,"PullClear")
```



###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =ReportRun()  |  The name of this function.  |  
|  ReportCellToRun  |  ReportRunTargetForPivot!C4  |  The function located in sheet "ReportRunTargetForPivot" at cell C4 will be ran when this function is triggered.  |  
|  RunEntireWorksheet  |  TRUE  |  All data report functions located in sheet "ReportRunTargetForPivot" will be ran when this function is triggered.  |  
|  OnAction  |  PullClear  |  This function will be triggered on a Pull-Clear event only.  |  

###  Trigger Combination List


The execution of this function is determined by an Interject event.

| Trigger  |  OnAction  |  Event Function Executes On  |
|------|------|------|
| 1  |  Pull  |  Pull-Run  |
| 2  |  Save  |  Save-Run  |
| 3  |  PullAndSave  |  Pull-Run, Save-Run  |
| 4  |  PullClear  |  Pull-Clear  |
| 5  |  SaveClear  |  Save-Clear  |
| 6  |  PullAndSaveClear  |  Pull-Clear, Save-Clear  |
