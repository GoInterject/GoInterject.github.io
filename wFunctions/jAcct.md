---
title: jAcct()
filename: "jAcct.md"
layout: custom
keywords: [jacct, account, segment, function, formula, chart of accounts]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example"]
links: ["/wFunctions/jCell.html"]
image_dir: ""
images: []
description: A helper function that specifies filters for up to six segments of a Chart of Accounts 
---
* * *

## Function Summary

A helper function that specifies filters for up to six segments of a Chart of Accounts. 

### Function Arguments

<button class="collapsible-parameter">**Segment1-6**<br>desc</button>
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
		<td></td>
 </tr>
 </tbody>
</table>
</div>

### Excel Formula Bar Example

```Excel
=jCellN(jAcct("Revenue - Sales",7002),11,2001,Actual)
```

### Function Composition

The jAcct function is wrapped in the [jCellN](/wFunctions/jCell.html) function to filter which account it will pull.

An example of this function is currently in construction in our documentation labs. Check back soon for an example with more context. However, for a demo report using this feature, visit the **Epicor Demo** in the report Library and open the file **PL Trend - w/ DataCells**.

| Argument Name | Example Mapping | Explanation |
|------|------|------|
| Function Name | jCellN | The name of this function. |
| Segment1 | "Revenue - Sales" | The first filter segment. Take only the revenue sales account. |
| Segment2 | 7002 | Filters to a specific location for a more specific account. |

