---
title: jFreezePanes()
layout: custom
keywords: [jFreezePanes, window, helper, function, formula]
description: The jFreezePanes function freezes a designated pane so the user can scroll through data and still keep the frozen pane in view.
---
* * *

##  Function Summary

The jFreezePanes function freezes a designated pane so the user can scroll through data and still keep the frozen pane in view. The function also hides a designated range of the report, typically the configuration section of an Interject report. This provides the user with a more user-friendly simplified viewing experience.

This action can be triggered by the Freeze/UnFreeze Panes found in [Quick Tools](/wGetStarted/Interject-Ribbon-Menu-Items.html#quick-tools) on the Interject Ribbon Menu. There is also an option there to Freeze All Tabs, which will freeze all sheets containing the jFreezePanes function (it will not unfreeze the panes).

For an example of this function, see [Lab Create: Customer Aging](/wGetStarted/L-Create-CustomerAging.html).

###  Function Arguments

<button class="collapsible-parameter">**FreezePanesCell**<br>A range of cells, the first row of which will be used as the last row frozen in place. All rows after this row will be unfrozen and able to scroll freely after a freeze panes action. This is typically the header row of column names above the targeted data that is or will be inserted. This will allow the header row to stay in view while scrolling through the data.  Best practice is to use a range instead of whole rows.</button>
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
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**AnchorViewCell**<br>A range of cells, the first row of which will be the top most displayed row after a freeze panes action. This is typically the row just below the Interject's configuration area.  Best practice is to use a range instead of whole rows.</button>
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
		<td>Will display all rows</td>
    </tr>
  </tbody>
</table>
</div>

###  Excel Formula Bar Example

```Excel
=jFreezePanes(A21,A15)
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =jFreezePanes()  |  The name of this function.  |  
|  FreezePanesCell  |  A22  |  Row 22 will be frozen in place and all rows from 23 on will be able to scroll.  |  
|  AnchorViewCell  |  A15  |  Row 15 will be the topmost row in view after a freeze panes action.  |  
