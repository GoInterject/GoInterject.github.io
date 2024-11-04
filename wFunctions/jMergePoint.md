---
title: jMergePoint()
filename: "jMergePoint.md"
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

Use jMergePoint functions to indicate which tabs are merged from a jMerge command, and where to place them.

### Function Arguments

<button class="collapsible-parameter">**TabName**<br>Enter the name of the tab to be copied. This supports a single wildcard *. Example: ""Sheet1"", ""Sheet*"" or just ""*""</button>
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

<button class="collapsible-parameter">**Placement**<br>Enter ""before"" or ""after"" to indicate the placement of the copied sheet, as compared to the anchor sheet.</button>
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

<button class="collapsible-parameter">**Anchor**<br>Enter the name of the sheet used as a placement anchor. You can also use jTabName() to indicate the current sheet, or use jTabName(Sheet2!a2) to reference another sheet.</button>
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

