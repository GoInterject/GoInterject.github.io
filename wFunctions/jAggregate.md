---
title: jAggregate()
filename: "jAggregate.md"
layout: custom
keywords: [jAggregate, sql, helper, function, formula, aggregate]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Usable In These SQL Helper Formulas"]
links: ["/wFunctions/jGroup.html", "/wFunctions/jDataSource.html"]
image_dir: ""
images: []
description: The jAggregate function defines aggregate values for jGroup and can also be evaluated to a specific cell.
---
* * *

##  Function Summary

The jAggregate function is used with jGroup to aggregate values and can also be used standalone with EvaluateToCell.

###  Function Arguments

<button class="collapsible-parameter">**DataSource**<br>Data source for the aggregate.</button>
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

<button class="collapsible-parameter">**AggregateType**<br>Options: ["MIN", "MAX", "COUNT", "SUM", "AVG"]</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>MIN, MAX, COUNT, SUM, or AVG</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**AggregateColumn**<br>Column to aggregate.</button>
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

<button class="collapsible-parameter">**EvaluateToCell**<br>Evaluate formula value to this cell, instead of using with jGroup.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String/Range</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Must resolve to a valid target cell when used</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Used as an aggregate definition for jGroup</td>
    </tr>
  </tbody>
</table>
</div>

###  Excel Formula Bar Example

```Excel
=jAggregate(B2,"SUM","Amount","")
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =jAggregate()  |  The name of this function.  |  
|  DataSource  |  B2  |  Uses source reference in B2.  |  
|  AggregateType  |  "SUM"  |  Sums values in the target column.  |  
|  AggregateColumn  |  "Amount"  |  Aggregates the Amount column.  |  
|  EvaluateToCell  |  ""  |  Blank indicates use with jGroup output definitions.  |  

###  Usable In These SQL Helper Formulas

* [jGroup()](/wFunctions/jGroup.html)
