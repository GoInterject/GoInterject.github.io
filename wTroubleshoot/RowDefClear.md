---
title: RowDef Data Clear
filename: "RowDefClear.md"
layout: custom
keywords: [RowDefRange, ColDefRange, Column definition missing, data clear]
headings: ["Overview", "Cause of the Error", "The Solution"]
links: ["/wFunctions/ReportVariable.html"]
image_dir: "RowDefClear"
images: [
	{file: "MultipleRowDefs", type: "png", site: "Add-in", cat: "Report", sub: "", report: "PL Report Categories by Location", ribbon: "", config: ""}, 
	{file: "MissingColumnDefinition", type: "png", site: "Add-in", cat: "Report", sub: "", report: "PL Report Categories by Location", ribbon: "", config: ""}, 
	{file: "ColumnDefinitions", type: "png", site: "Add-in", cat: "Report", sub: "", report: "PL Report Categories by Location", ribbon: "", config: ""}
	]
description: Data does not clear when multiple columns are defined as the RowDefRange for a ReportVariable. This happens only when the first column of the RowDefRange is missing from the ColDefRange.
---
* * *

## Overview

Data does not clear when multiple columns are defined as the RowDefRange for a [ReportVariable](/wFunctions/ReportVariable.html). This happens only when the first column of the RowDefRange is missing from the ColDefRange.

### Cause of the Error

Here is a report that has columns B and C defined as the RowDefRange in this ReportVariable (Notice the first column of the RowDefRange contains the **\[!DetailRow]**):

![](/images/RowDefClear/MultipleRowDefs.png)
<br>

This report does not clear the data when executing a Data Clear. The problem is the first column definition is missing in the ColDefRange:

![](/images/RowDefClear/MissingColumnDefinition.png)
<br>

### The Solution

To fix the problem, ensure all the columns are found in the ColDefRange:

![](/images/RowDefClear/ColumnDefinitions.png)
<br>
