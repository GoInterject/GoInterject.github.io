---
title: jDataSource()
filename: "jDataSource.md"
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

 A formula for defining a data source, support for many different data sources (SQL, Excel, etc)

### Function Arguments

<button class="collapsible-parameter">**DataPortal**<br>The name of the Interject Data Portal that will be used as the data source for this function.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String/<a href="https://docs.gointerject.com/wFunctions/jDataPortal.html">jDataPortal()</a></td>
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

<button class="collapsible-parameter">**ColDefRange**<br>Column definition range: A range designating the names of the columns of the data source. Only data from these columns will be inserted. Range can span multiple rows. Best practice is to use a range instead of whole rows.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 500 columns. Must match the width of the range defined in TargetDataRange</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Uses all columns from the data source</td>
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

<button class="collapsible-parameter">**TagInCache**<br>The name of the data source in the cache.</button>
<div markdown="1" class="panel-parameter">
<table>
 <tbody>
 <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range/String</td>
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

### Excel Formula Bar Example

```Excel
```

### Function Composition

| Argument Name | Example Mapping | Explanation |
|------|------|------|
| Function Name |  | The name of this function. |
