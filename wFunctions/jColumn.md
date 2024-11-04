---
title: jColumn()
filename: "jColumn.md"
layout: custom
keywords: []
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition"]
links: []
image_dir: ""
images: []
description: 
---
* * *

## Function Summary

Provides an easy way to define columns for financial/operational data.

### Function Arguments

<button class="collapsible-parameter">**Source**<br>Source relates to values such as Budget, Actual, Forecast.</button>
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
		<td></td>
 </tr>
 </tbody>
</table>
</div>

<button class="collapsible-parameter">**Year**<br>Specify the year. Also accepts dates or YYYY-MM format for year</button>
<div markdown="1" class="panel-parameter">
<table>
 <tbody>
 <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range/String/Boolean</td>
 </tr>
 <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char</td>
 </tr>
 <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Does not concatenate any cells</td>
 </tr>
 </tbody>
</table>
</div>

<button class="collapsible-parameter">**Period**<br>Period number relates to month (1 to 12) and also accepts date or YYYY-MM format for month. When Balance Type is QTR it relates to quarter (1 to 4)</button>
<div markdown="1" class="panel-parameter">
<table>
 <tbody>
 <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range/String/Boolean</td>
 </tr>
 <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char</td>
 </tr>
 <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Does not concatenate any cells</td>
 </tr>
 </tbody>
</table>
</div>

<button class="collapsible-parameter">**BalanceType**<br>[Optional] Specify a balance type. Accepts MTD, QTD, YTD and QTR. Blank defaults to MTD</button>
<div markdown="1" class="panel-parameter">
<table>
 <tbody>
 <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range/String/Boolean</td>
 </tr>
 <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char</td>
 </tr>
 <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Does not concatenate any cells</td>
 </tr>
 </tbody>
</table>
</div>
<button class="collapsible-parameter">**Version**<br>[Optional] Specify a version code if applicable</button>
<div markdown="1" class="panel-parameter">
<table>
 <tbody>
 <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range/String/Boolean</td>
 </tr>
 <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char</td>
 </tr>
 <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Does not concatenate any cells</td>
 </tr>
 </tbody>
</table>
</div>
<button class="collapsible-parameter">**Segment 1-8**<br>[Optional] Specify Segment 1-8.</button>
<div markdown="1" class="panel-parameter">
<table>
 <tbody>
 <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range/String/Boolean</td>
 </tr>
 <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char</td>
 </tr>
 <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Does not concatenate any cells</td>
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

