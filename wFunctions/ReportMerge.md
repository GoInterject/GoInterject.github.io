---
title: ReportMerge()
layout: custom
filename: "ReportMerge.md"
keywords: []
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition"]
links: []
image_dir: ""
images: []
description: 
---
* * *

## Function Summary

This function is used to merge two workbooks into one. Add additional jMergePoint functions to indicate which tabs are merged and where to place them.

### Function Arguments

<button class="collapsible-parameter">**FileName**<br>Use the Report Library Sheet Link Code, or else a fully qualified path to the other Workbook.</button>
<div markdown="1" class="panel-parameter">
<table>
 <tbody>
 <tr>
		<td class="pph"><b>Type</b></td>
		<td>Cell/String</td>
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

<button class="collapsible-parameter">**MergeID**<br>Use a unique ID to identify this jMerge. This is required to clear tabs.</button>
<div markdown="1" class="panel-parameter">
<table>
 <tbody>
 <tr>
		<td class="pph"><b>Type</b></td>
		<td>Cell/String</td>
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

<button class="collapsible-parameter">**RemoveTabsOnClear**<br>(Optional) Indicate whether to delete merged tabs when clearing data. The default is False. Otherwise enter 'True'. If true you must enter a MergeID parameter value.</button>
<div markdown="1" class="panel-parameter">
<table>
 <tbody>
 <tr>
		<td class="pph"><b>Type</b></td>
		<td>Cell/String</td>
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

<button class="collapsible-parameter">**PullOnOpen**<br>(Optional) Run a pull on the worksheet after opening. The default is false</button>
<div markdown="1" class="panel-parameter">
<table>
 <tbody>
 <tr>
		<td class="pph"><b>Type</b></td>
		<td>Cell/String</td>
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

<button class="collapsible-parameter">**MergePoints**<br>(Optional) Provide a range reference to a list of jMergePoint functions. If none is provided, then all jMergePoint functions within the book will be considered.</button>
<div markdown="1" class="panel-parameter">
<table>
 <tbody>
 <tr>
		<td class="pph"><b>Type</b></td>
		<td>Cell/String</td>
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
<button class="collapsible-parameter">**Disabled**<br>(Optional) Function will not execute on pull if set to true. The default is false.</button>
<div markdown="1" class="panel-parameter">
<table>
 <tbody>
 <tr>
		<td class="pph"><b>Type</b></td>
		<td>Cell/String</td>
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

