---
title: ReportMacro()
layout: custom
keywords: [ReportMacro, macro, vba, event, trigger, function, formula]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Trigger Combination List"]
description: The ReportMacro function executes a designated VBA macro when triggered upon a designated event.
---
* * *

##  Function Summary

The ReportMacro function executes a designated VBA macro when triggered upon a designated [event](wIndex/Event-Functions-Landing.html). 

For an example of this function, see [Lab Create: Using Report Macro](/wGetStarted/L-Create-ReportMacro.html)

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

<button class="collapsible-parameter">**MacroNameToRun**<br>The name of the macro this function will run.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Macro in VBA cannot contain parameters</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Will Error</td>
    </tr>
  </tbody>
</table>
</div>

###  Excel Formula Bar Example

```Excel
=ReportMacro("Pull","Both","MyCustomFunction")
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =ReportMacro()  |  The name of this function.  |  
|  OnPullSaveOrBoth  |  "Pull"  |  A pull action is designated as the run event.  |  
|  OnClearRunOrBoth  |  "Both"  |  A clear event or run event (defined in OnPullSaveOrBoth) will trigger this macro being ran.  |  
|  MacroNameToRun  |  "MyCustomFunction"  |  The macro "MyCustomFunction" will be ran.  |  

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
