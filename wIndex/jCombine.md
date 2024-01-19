---
title: jCombine()
filename: "jCombine.md"
layout: custom
keywords: [jCombine, helper, function, formula]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Usable In These Functions"]
links: ["/wGetStarted/L-Create-RetainFeature.html", "ReportRange.html", "ReportVariable.html"]
image_dir: ""
description: The jCombine function concatenates a range or multiple ranges of cells into a single string using a designated delimiter.
---
* * *

##  Function Summary

The jCombine function concatenates a range or multiple ranges of cells into a single string using a designated delimiter. Blank cells are skipped.

This function can be used as a standalone function and does not need to be embedded in another function.

For an example of this function, see [Lab Create: Using the Retain Feature](/wGetStarted/L-Create-RetainFeature.html).

###  Function Arguments

<button class="collapsible-parameter">**Selected Range**<br>A range or multiple ranges that will be concatenated. If multiple ranges are selected, they need to be enclosed in parenthesis and separated by a comma (e.g. "(a2,a14:b15,c6)"). Concatenation happens row by row (i.e. each column in the row concatenates before moving to the next row).</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range/(Range, Range, …)</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 7 ranges</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Delimiter**<br>The string that will be used as the delimiter when selecting multiple cells.</button>
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
		<td>","</td>
    </tr>
  </tbody>
</table>
</div>

###  Excel Formula Bar Example

```Excel
=jCombine((A2,F2:G2,R2:T2))
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =jCombine()  |  The name of this function.  |  
|  Selected Range  |  (A2,F2:G2,R2:T2)  |  The ranges selected for concatenation are: A2, F2:G2, and R2:T2.  |  
|  Delimiter  |    |  Blank to indicate a comma is to be used as the delimiter.  |  

###  Usable In These Functions

* [ReportRange](ReportRange.html) 
* [ReportVariable](ReportVariable.html)
