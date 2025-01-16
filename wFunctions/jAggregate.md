---
title: jAggregate()
filename: "jAggregate.md"
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

Aggregate data from a data source (takes in a jDataSource and an aggregate function) 

### Function Arguments

<button class="collapsible-parameter">**jDataSource**<br>The name of the Interject jDataSource that will be used as the data source for this function.</button>
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

<button class="collapsible-parameter">**AggregateFunctions**<br>A boolean statement including the aggregate functions used.</button>
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

<button class="collapsible-parameter">**JDSColumns**<br>The names of the column from jDataSource to aggregate.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String/<a href="https://docs.gointerject.com/wFunctions/Param.html">Param()</a></td>
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

<button class="collapsible-parameter">**Evaluate**<br>The Segment number to check the value against.</button>
<div markdown="1" class="panel-parameter">
<table>
 <tbody>
 <tr>
		<td class="pph"><b>Type</b></td>
		<td>Boolean</td>
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
