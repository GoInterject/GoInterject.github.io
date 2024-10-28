---
title: jRangeTag()
filename: "jRangeTag.md"
layout: custom
keywords: [jRangeTag, helper, function, formula]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition"]
links: ["/wGetStarted/L-Export-BasicDist.html"]
image_dir: ""
images: []
description: The jRangeTag function simply tags a designated range with a name.
---
* * *

##  Function Summary

The jRangeTag function simply tags a designated range with a name. This is used to support certain automated processes unique to Interject functions, for example report distribution.

For an example of this function, see [Lab Create: Basic Distribution](/wGetStarted/L-Export-BasicDist.html).

###  Function Arguments

<button class="collapsible-parameter">**Tag**<br>The name to tag the range</button>
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
		<td>Will fail</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Range**<br>The range to be associated with the Tag</button>
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
		<td>Will fail</td>
    </tr>
  </tbody>
</table>
</div>

###  Excel Formula Bar Example

```Excel
=jRangeTag("Location",M22)
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =jRangeTag()  |  The name of this function.  |  
|  Tag  |  "Location"  |  This range is tagged as "Location".  |  
|  Range  |  M22  |  The range to be tagged is M22.  |  
