---
title: jJoin()
filename: "jJoin.md"
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

 join data from multiple data sources (takes in two jDataSources, columns to join on, and the join type)

### Function Arguments

<button class="collapsible-parameter">**jDataSource1**<br>The name of the first Interject jDataSource to join.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String/<a href="https://docs.gointerject.com/wFunctions/jDataSource.html">jDataSource()</a></td>
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

<button class="collapsible-parameter">**jDataSource2**<br>The name of the second Interject jDataSource to join.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String/<a href="https://docs.gointerject.com/wFunctions/jDataSource.html">jDataSource()</a></td>
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

<button class="collapsible-parameter">**JDS1Columns**<br>The names of the column from jDataSource1 to join on.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String/<a href="https://docs.gointerject.com/wFunctions/Param.html">Param()</a></td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char; The values must match the order of the parameters in the data source (The order can be verified using the [Validation Report](/wTroubleshoot/Reports.html#validation-report-for-interject-events) )</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Conditionals**<br>A list of characters that represent the conditions to join the columns on.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String/<a href="https://docs.gointerject.com/wFunctions/Param.html">Param()</a></td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char; The values must match the order of the parameters in the data source (The order can be verified using the [Validation Report](/wTroubleshoot/Reports.html#validation-report-for-interject-events) )</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**JDS2Columns**<br>The names of the column from jDataSource2 to join on.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String/<a href="https://docs.gointerject.com/wFunctions/Param.html">Param()</a></td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char; The values must match the order of the parameters in the data source (The order can be verified using the [Validation Report](/wTroubleshoot/Reports.html#validation-report-for-interject-events) )</td>
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
