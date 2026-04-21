---
title: jJoin()
filename: "jJoin.md"
layout: custom
keywords: [jJoin, sql, helper, function, formula, join]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Usable In These SQL Helper Formulas"]
links: ["/wFunctions/jDataSource.html", "/wFunctions/jQuery.html", "/wFunctions/jFilter.html", "/wFunctions/jGroup.html", "/wFunctions/jAggregate.html"]
image_dir: ""
images: []
description: The jJoin function joins two jDataSource references on a common column.
---
* * *

##  Function Summary

The jJoin function joins two jDataSources on a common column.

###  Function Arguments

<button class="collapsible-parameter">**FirstDataSource**<br>First data source to join on.</button>
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

<button class="collapsible-parameter">**SecondDataSource**<br>Second data source to join on.</button>
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

<button class="collapsible-parameter">**JoinType**<br>SQL join type: INNER, OUTER, LEFT, RIGHT.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>INNER, OUTER, LEFT, or RIGHT</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**DS1JoinColumn**<br>Column to join from in the first jDataSource.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Must be a valid column in FirstDataSource</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**DS2JoinColumn**<br>Column to join from in the second jDataSource.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Must be a valid column in SecondDataSource</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

###  Excel Formula Bar Example

```Excel
=jJoin(B2,C2,"INNER","CustomerID","CustomerID")
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =jJoin()  |  The name of this function.  |  
|  FirstDataSource  |  B2  |  Uses first source reference in B2.  |  
|  SecondDataSource  |  C2  |  Uses second source reference in C2.  |  
|  JoinType  |  "INNER"  |  Performs an inner join.  |  
|  DS1JoinColumn  |  "CustomerID"  |  Joins using CustomerID from first source.  |  
|  DS2JoinColumn  |  "CustomerID"  |  Joins using CustomerID from second source.  |  

###  Usable In These SQL Helper Formulas

* [jGroup()](/wFunctions/jGroup.html)
* [jAggregate()](/wFunctions/jAggregate.html)
