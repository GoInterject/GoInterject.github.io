---
title: jCombineIF()
filename: "jCombine_IF.md"
layout: custom
keywords: [jCombineIF, helper, function, formula]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition"]
links: []
image_dir: ""
images: []
description: The jCombineIF function concatenates a range or multiple ranges of cells into a single string using a designated delimiter if a certain condition is met.
---
* * *

##  Function Summary

The jCombineIF function concatenates a range or multiple ranges of cells into a single string using a designated delimiter if a certain condition is met. Blank cells are skipped.

This function can be used as a standalone function and does not need to be embedded in another function.

###  Function Arguments

<button class="collapsible-parameter">**CriteriaRange**<br>A range designated to be the criteria range. Each cell in this range will be compared to the value in the CriteriaValue argument. If the cell matches, the corresponding cell in the SelectedRange will be concatenated.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Must match the dimensions of SelectedRange</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**SelectedRange**<br>A range that will be concatenated. Concatenation happens row by row (i.e. each column in the row concatenates before moving to the next row).</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Must match the dimensions of CriteriaRange</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**CriteriaValue**<br>A value designated to be the criteria (the first cell is used if a range is entered). If the value here matches a cell in the CriteriaRange argument, the corresponding cell in the SelectedRange will be concatenated.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range/String/Boolean</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Does not concatenate any cells</td>
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
=jCombineIF(J16:O16,J15:O15,TRUE,";")
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =jCombineIF()  |  The name of this function.  |  
|  CriteriaRange  |  J16:O16  |  The range J16:O16 will be used to compare values. If a cell in this range matches the CriteriaValue, the corresponding cell in SelectedRange will concatenated. For example, in this case, if J16 = True, then J15 will be concatenated. If J17 = True, then J16 will be concatenated, etc.  |  
|  SelectedRange  |  J15:O15  |  The range J15:O15 will be the values concatenated if the criteria is met.  |  
|  CriteriaValue  |  TRUE  |  The boolean value of True is used as the criteria.  |  
|  Delimiter  |  ";"  |  The semicolon ";" will be used as the delimiter for the concatenation.  |  
