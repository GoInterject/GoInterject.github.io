---
title: jDataSource()
filename: "jDataSource.md"
layout: custom
keywords: [jDataSource, sql, helper, function, formula, data source, cache]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Usable In These SQL Helper Formulas"]
links: ["/wFunctions/jQuery.html", "/wFunctions/jFilter.html", "/wFunctions/jJoin.html", "/wFunctions/jGroup.html", "/wFunctions/jAggregate.html"]
image_dir: ""
images: []
description: The jDataSource function provides an easy way to cache sheet data and Data Portals for SQL helper formulas.
---
* * *

##  Function Summary

The jDataSource function provides an easy way to cache sheet data and Data Portals for SQL helper formulas. It can cache a worksheet range or Data Portal output and return a reference that can be reused by other SQL helpers such as jQuery, jFilter, jJoin, jGroup, and jAggregate.

###  Function Arguments

<button class="collapsible-parameter">**DataSource**<br>An Excel range or Data Portal to pull data from into a local cache.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range/String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Must resolve to a valid range or Data Portal reference</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**ColDefRange**<br>The column definition range used when the source requires explicit column names.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Should align with the source column structure</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Uses source defaults</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Params**<br>Data Portal params go here.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String/Param()</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Must match expected Data Portal parameter order</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>No Data Portal parameters are passed</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**CacheTag**<br>Optional tag used to identify the cached source.</button>
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
		<td>Source is cached without a custom tag</td>
    </tr>
  </tbody>
</table>
</div>

###  Excel Formula Bar Example

```Excel
=jDataSource("NorthwindCustomers",B2:H2,Param(C7,C8),"NorthwindCache")
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =jDataSource()  |  The name of this function.  |  
|  DataSource  |  "NorthwindCustomers"  |  Uses the NorthwindCustomers Data Portal as the source.  |  
|  ColDefRange  |  B2:H2  |  Uses B2:H2 as the column definition range.  |  
|  Params  |  Param(C7,C8)  |  Sends parameters from C7 and C8.  |  
|  CacheTag  |  "NorthwindCache"  |  Tags the cached source for reuse.  |  

###  Usable In These SQL Helper Formulas

* [jQuery()](/wFunctions/jQuery.html)
* [jFilter()](/wFunctions/jFilter.html)
* [jJoin()](/wFunctions/jJoin.html)
* [jGroup()](/wFunctions/jGroup.html)
* [jAggregate()](/wFunctions/jAggregate.html)
