---
title: jSetting()
layout: custom
keywords: [jSetting, helper, function, formula]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition"]
links: []
description: The jSetting function is a simple way to create a Tag/Value pair that can be used internally by the Interject system.
---
* * *

##  Function Summary

The jSetting function is a simple way to create a JSON Tag/Value pair that can be used internally by the Interject system.

This function can be used as a standalone function and does not need to be embedded in another function.

###  Function Arguments

<button class="collapsible-parameter">**Tag**<br>The title or tag of the setting.</button>
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
		<td>Empty string</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Value**<br>The value of the setting.</button>
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
		<td>Empty string</td>
    </tr>
  </tbody>
</table>
</div>

###  Excel Formula Bar Example

```Excel
=jSetting("NamedRangePrefix", "Filter")
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =jSetting()  |  The name of this function.  |  
|  Tag  |  "NamedRangePrefix"  |  This setting is tagged as "NamedRangePrefix"  |  
|  Value  | "Filter"   |  This setting's value is "Filter"  |  

