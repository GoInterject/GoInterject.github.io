---
title: jFilter()
filename: "jFilter.md"
layout: custom
keywords: [jFilter, sql, helper, function, formula, where]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Usable In These SQL Helper Formulas"]
links: ["/wFunctions/jDataSource.html", "/wFunctions/jWhere.html", "/wFunctions/jJoin.html", "/wFunctions/jGroup.html", "/wFunctions/jAggregate.html"]
image_dir: ""
images: []
description: The jFilter function filters a SQL helper data source using jWhere clause expressions.
---
* * *

##  Function Summary

The jFilter function filters a SQL helper data source using jWhere clause expressions.

###  Function Arguments

<button class="collapsible-parameter">**DataSource**<br>Data Source to filter.</button>
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

<button class="collapsible-parameter">**jWhere**<br>jWhere statements describing the where clause.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>jWhere()</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Must contain valid jWhere expressions</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>No filtering is applied</td>
    </tr>
  </tbody>
</table>
</div>

###  Excel Formula Bar Example

```Excel
=jFilter(B2,jWhere("Country","USA","="))
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =jFilter()  |  The name of this function.  |  
|  DataSource  |  B2  |  Uses the SQL helper source reference in B2.  |  
|  jWhere  |  jWhere("Country","USA","=")  |  Returns only rows where Country equals USA.  |  

###  Usable In These SQL Helper Formulas

* [jJoin()](/wFunctions/jJoin.html)
* [jGroup()](/wFunctions/jGroup.html)
* [jAggregate()](/wFunctions/jAggregate.html)
