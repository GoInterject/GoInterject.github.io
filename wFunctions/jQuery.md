---
title: jQuery()
filename: "jQuery.md"
layout: custom
keywords: [jQuery, sql, helper, function, formula, query]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Usable In These SQL Helper Formulas"]
links: ["/wFunctions/jDataSource.html", "/wFunctions/jFilter.html", "/wFunctions/jJoin.html", "/wFunctions/jGroup.html", "/wFunctions/jAggregate.html"]
image_dir: ""
images: []
description: The jQuery function runs a SQL query against a jDataSource reference.
---
* * *

##  Function Summary

The jQuery function runs a SQL query against a jDataSource reference.

###  Function Arguments

<button class="collapsible-parameter">**DataSource**<br>The range reference to a jDataSource or the tag of it.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range/String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Must reference a valid jDataSource output or tag</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Query**<br>The SQL query to run on the DataSource.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Must be a valid SQL query string for the in-memory source</td>
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
=jQuery(B2,"SELECT CustomerID, CompanyName FROM SourceData WHERE Country = 'USA'")
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =jQuery()  |  The name of this function.  |  
|  DataSource  |  B2  |  Uses the jDataSource reference stored in B2.  |  
|  Query  |  "SELECT CustomerID, CompanyName FROM SourceData WHERE Country = 'USA'"  |  Filters and projects data from the cached source.  |  

###  Usable In These SQL Helper Formulas

* [jFilter()](/wFunctions/jFilter.html)
* [jJoin()](/wFunctions/jJoin.html)
* [jGroup()](/wFunctions/jGroup.html)
* [jAggregate()](/wFunctions/jAggregate.html)
