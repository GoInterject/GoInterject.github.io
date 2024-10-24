---
title: ReportDefaults()
filename: "ReportDefaults.md"
layout: custom
keywords: [ReportDefaults, defaults, event, trigger, function, formula]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Trigger Combination List", "Embeddable Helper Functions"]
links: ["/wFunctions/Event-Functions-Landing.html", "/wGetStarted/L-Create-CustomerAgingDetail.html#reportdefaults", "https://docs.gointerject.com/wFunctions/Pair.html", "https://docs.gointerject.com/wFunctions/PairGroup.html", "/wFunctions/PairGroup.html", "/wFunctions/Pair.html"]
image_dir: ""
images: []
description: The ReportDefaults function will copy a value from a range to another range when triggered upon a designated event.
---
* * *

##  Function Summary

The ReportDefaults function will copy a value from a range to another range when triggered upon a designated [event](/wFunctions/Event-Functions-Landing.html).

This function can be used to restore default values to a report after a desired action. For example, the values in the parameters section can be cleared after a clear event or set to a particular value. It can also be used to set initial parameters before a report is ran.

For an example of this function, see [Lab Create: Customer Aging Detail](/wGetStarted/L-Create-CustomerAgingDetail.html#reportdefaults).

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

<button class="collapsible-parameter">**TransferPairs**<br>A single Pair or PairGroup that contains a list of Pairs. The Pair function transfers values from one cell to another.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td><a href="https://docs.gointerject.com/wFunctions/Pair.html">Pair()</a>/<a href="https://docs.gointerject.com/wFunctions/PairGroup.html">PairGroup()</a></td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 34 Pairs</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Does not transfer any values</td>
    </tr>
  </tbody>
</table>
</div>

###  Excel Formula Bar Example

```Excel
=ReportDefaults("Save","Clear",PairGroup(Pair("",C12,FALSE)))
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =ReportDefaults()  |  The name of this function.  |  
|  OnPullSaveOrBoth  |  "Pull"  |  A pull action is designated as the run event.  |  
|  OnClearRunOrBoth  |  "Clear"  |  A clear event or run event (defined in OnPullSaveOrBoth) will trigger this function being ran.  |  
|  TransferPairs  |  PairGroup(Pair("",C12,FALSE))  |  Will copy a blank value to C12.  |  

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

###  Embeddable Helper Functions

* [PairGroup](/wFunctions/PairGroup.html)
* [Pair](/wFunctions/Pair.html)
