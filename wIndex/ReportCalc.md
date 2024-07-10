---
title: ReportCalc()
filename: "ReportCalc.md"
layout: custom
keywords: [ReportCalc, calculation, event, trigger, function, formula]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Trigger Combination List"]
links: ["wIndex/Event-Functions-Landing.html", "/wGetStarted/L-Create-HideRowCol.html"]
image_dir: ""
images: []
description: The ReportCalc function executes a calculation of formulas in a worksheet or workbook when triggered upon a designated event.
---
* * *

##  Function Summary

The ReportCalc function executes a calculation of formulas in a worksheet or workbook when triggered upon a designated [event](wIndex/Event-Functions-Landing.html).

<blockquote class=highlight_note>
<b>Note:</b> The latest version of the Interject Add-In will automatically perform a recalculation on the workbook whenever the pull, save, or drill window is displayed.
</blockquote>
<br>

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

<button class="collapsible-parameter">**SheetOrWorkBook**<br>A string indicating to perform the calculation on a designated sheet or the entire workbook.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>"sheet", "workbook"</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**SheetName**<br>The name of the sheet that the calculation will be performed on if SheetOrWorkBook = "sheet".</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Will run calculations on current sheet</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Disable**<br>True: This function will be disabled.<br><br>False: This function will be enabled.</button>
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
=ReportCalc("Both","Both","Sheet")
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =ReportCalc()  |  The name of this function.  |  
|  OnPullSaveOrBoth  |  "Both"  |  A pull or save action are designated as the run event.  |  
|  OnClearRunOrBoth  |  "Both"  |  A clear event or run event (defined in OnPullSaveOrBoth) will trigger this function being ran.  |  
|  SheetOrWorkbook  |  "Sheet"  |  A calculation of the sheet will be performed.  |  
|  SheetName  |    |  Blank to indicate to perform the calculation on the current sheet.  |  
|  Disable  |    |  Blank to indicate to enable this function.  |  

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
