---
title: BSpec()
filename: ""
layout: custom
keywords: []
headings: []
links: []
image_dir: ""
images: []
description: 
---
* * *

## Function Summary

A helper function that concatenates segments with a pipe delimiter.

### Function Arguments

<button class="collapsible-parameter">**Segment1-6**<br>A segment to concatenate.</button>
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
		<td>Empty concatenation</td>
 </tr>
 </tbody>
</table>
</div>

### Excel Formula Bar Example

```Excel
=BSpec(C1,C2,C3)
```

### Function Composition

| Argument Name | Example Mapping | Explanation | 
|------|------|------|
| Function Name | BSpec | The name of this function. |
| Segment1 | C1 | Cell C1 will be concatenated. |
| Segment2 | C2 | Cell C2 will be concatenated. |
| Segment3 | C3 | Cell C3 will be concatenated. |
