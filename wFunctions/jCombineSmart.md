---
title: jCombineSmart()
filename: "jCombineSmart.md"
layout: custom
keywords: [jCombineSmart, helper, function, formula]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition"]
links: []
image_dir: ""
images: []
description: The jCombine function concatenates a range or multiple ranges of cells into a single string using a designated delimiter.
---
* * *

##  Function Summary

The jCombineSmart function concatenates a range or multiple ranges of cells into a single string using a designated delimiter. Blank cells and duplicate cells are skipped and the resulting concatenation is sorted. This function can also be set to interpret the input as numbers so that sorting can be numerically ascending. In addition, it applies continuous ranges where possible. For example, "2,6,6,1,3" becomes "1..3,6".

This function can be used as a standalone function and does not need to be embedded in another function.

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

<button class="collapsible-parameter">**Range Code**<br>The text displayed as the range operator for continuous ranges.</button>
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
		<td>".."</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Convert To Numeric**<br>True: Trims inputs of leading zeros and converts to a numeric value.<br><br>False: Treats inputs as text.</button>
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
=jCombineSmart(F2:L2, "|", "...", True)
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =jCombine()  |  The name of this function.  |  
|  Selected Range  |  F2:L2  |  The range F2:L2 will be the values concatenated.  |  
|  Delimiter  |  "\|"  |  The pipe "\|" will be used as the delimiter for the concatenation.  |  
|  Range Code  |  "..."  |  Three dots "..." will be used as the range operator for continuous ranges.  |  
|  Convert To Numeric  |  True  |  Will convert the cells to a numeric value.  |  
