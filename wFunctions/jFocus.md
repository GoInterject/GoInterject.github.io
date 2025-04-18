---
title: jFocus()
filename: "jFocus.md"
layout: custom
keywords: [jFocus, helper, function, formula]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition"]
links: ["/wFunctions/jFreezePanes.html", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#quick-tools", "/wGetStarted/L-Create-CustomerAging.html"]
image_dir: ""
images: []
description: The jFocus function will move the cursor and select a targeted range after a freeze panes action using Interject's Freeze/UnFreeze Panes action.
---
* * *

##  Function Summary

The jFocus function will move the cursor and select a targeted range after a freeze panes action using Interject's Freeze/UnFreeze Panes action. The [jFreezePanes](/wFunctions/jFreezePanes.html) function must be set up for this to trigger. The Freeze/UnFreeze Panes action can be found in [Quick Tools](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#quick-tools) on the Interject Ribbon Menu.

For an example of this function, see [Lab Create: Customer Aging](/wGetStarted/L-Create-CustomerAging.html).

###  Function Arguments

<button class="collapsible-parameter">**Target**<br>The range that will be selected after a freeze panes action.</button>
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
		<td>Will select the cell defined in jFreezePanes FreezePanesCell argument</td>
    </tr>
  </tbody>
</table>
</div>

###  Excel Formula Bar Example

```Excel
=jFocus(C17)
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =jFocus  |  The name of this function.  |  
|  Target  |  C17  |  Cell C17 will be selected after a freeze panes action.  |  
