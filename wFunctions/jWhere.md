---
title: jWhere()
filename: "jWhere.md"
layout: custom
keywords: [jWhere, sql, helper, function, formula, where, filter]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Usable In These SQL Helper Formulas"]
links: ["/wFunctions/jFilter.html"]
image_dir: ""
images: []
description: The jWhere function defines where-clause expressions for SQL helper filtering.
---
* * *

##  Function Summary

The jWhere function defines where-clause expressions for SQL helper filtering.

###  Function Arguments

<button class="collapsible-parameter">**Column**<br>Column from the jDataSource table.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Must be a valid column name from the SQL helper source</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Value**<br>Value to compare against.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Use value text compatible with the target comparison</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Blank value comparison is used</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**SqlOperator**<br>SQL operator for where clause [=, ==, <>, !=, >, <, like, is null, is not null, exists].</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Must be a supported operator</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Defaults to "=" behavior</td>
    </tr>
  </tbody>
</table>
</div>

###  Excel Formula Bar Example

```Excel
=jWhere("Country","USA","=")
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =jWhere()  |  The name of this function.  |  
|  Column  |  "Country"  |  Uses the Country column.  |  
|  Value  |  "USA"  |  Compares rows against USA.  |  
|  SqlOperator  |  "="  |  Uses equals comparison.  |  

###  Usable In These SQL Helper Formulas

* [jFilter()](/wFunctions/jFilter.html)
