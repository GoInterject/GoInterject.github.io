---
title: jGroup()
filename: "jGroup.md"
layout: custom
keywords: [jGroup, sql, helper, function, formula, group, aggregate]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Usable In These SQL Helper Formulas"]
links: ["/wFunctions/jDataSource.html", "/wFunctions/jAggregate.html", "/wFunctions/Param.html", "/wFunctions/jJoin.html"]
image_dir: ""
images: []
description: The jGroup function groups a jDataSource table by a column with aggregate support.
---
* * *

##  Function Summary

The jGroup function groups a jDataSource table by a column with aggregate support.

###  Function Arguments

<button class="collapsible-parameter">**DataSource**<br>DataSource to group from.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range/String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Must reference a valid SQL helper source</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**ColumnDefs**<br>A Param() list of jAggregate formulas.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Param(jAggregate(), ...)</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Must contain one or more valid jAggregate formulas</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**GroupingColumn**<br>The column to group the table on.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Must be a valid column in DataSource</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**GroupingType**<br>Grouping behavior option used by the SQL helper engine.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Should use a supported grouping type value</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Default grouping behavior is used</td>
    </tr>
  </tbody>
</table>
</div>

###  Excel Formula Bar Example

```Excel
=jGroup(B2,Param(jAggregate(B2,"SUM","Amount",""),jAggregate(B2,"COUNT","OrderID","")),"CustomerID","")
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =jGroup()  |  The name of this function.  |  
|  DataSource  |  B2  |  Uses source reference in B2.  |  
|  ColumnDefs  |  Param(jAggregate(...),jAggregate(...))  |  Defines output aggregate columns.  |  
|  GroupingColumn  |  "CustomerID"  |  Groups rows by CustomerID.  |  
|  GroupingType  |  ""  |  Uses default grouping behavior.  |  

###  Usable In These SQL Helper Formulas

* [jAggregate()](/wFunctions/jAggregate.html)
