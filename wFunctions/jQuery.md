---
title: jQuery()
filename: "jQuery.md"
layout: custom
keywords: [function, formula]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition"]
links: []
image_dir: ""
images: []
description: 
---
* * *

## Function Summary 

A query statement to extract data from a data source using SQL like syntax.

### Function Arguments

<button class="collapsible-parameter">**jDataSource**<br>The name of the Interject jDataSource that will be used as the data source for this function.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String/<a href="https://docs.gointerject.com/wFunctions/jDataSource.html">jDataSource()/</a><a href="https://docs.gointerject.com/wFunctions/Param.html">Param()/</a><a href="https://docs.gointerject.com/wFunctions/jJoin.html">jJoin()/</a><a href="https://docs.gointerject.com/wFunctions/jFilter.html">jFilter()</a></td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Query**<br>A valid SQL statement.</button>
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
		<td>Function error</td>
 </tr>
 </tbody>
</table>
</div>

<button class="collapsible-parameter">**Parameters**<br>The cells designating the parameters for the Data Portal. The values in these cells will filter the data that is inserted from the data source.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td><a href="https://docs.gointerject.com/wFunctions/Param.html">Param()</a></td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>The values must match the order of the parameters in the data source (The order can be verified using the [Validation Report](/wTroubleshoot/Reports.html#validation-report-for-interject-events) )</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Data is not filtered</td>
    </tr>
  </tbody>
</table>
</div>

### Excel Formula Bar Example

```Excel
```

### Function Composition

| Argument Name | Example Mapping | Explanation |
|------|------|------|
| Function Name |  | The name of this function. |
