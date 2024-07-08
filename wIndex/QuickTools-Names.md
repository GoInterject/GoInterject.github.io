---
title: Quick Tools - Names Tools
filename: "QuickTools-Names.md"
layout: custom
keywords: [Quick Tools, Names Tools, Remove Names with Ref Errors from Book, Remove All Names from Sheet, Remove All Names from Book, Create Range Name for Sheet, Create Range Names for Sheet for 2 Column Selection]
headings: ["Overview", "Excel Name Manager", "Remove Names with Ref Errors from Book", "Remove All Names from Sheet", "Remove All Names from Book", "Create Range Name for Sheet", "Create Range Names for Sheet for 2 Column Selection", "Appending A Prefix and/or Suffix To A Name"]
links: []
image_dir: "QuickToolsNames"
images: [
	{file: "NamesTools", type: "png", site: "Add-in", cat: "Quick Tools", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "NameManager", type: "png", site: "Excel", cat: "Name Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "NameManager2", type: "png", site: "Excel", cat: "Name Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "NameManager5", type: "png", site: "Add-in", cat: "Report", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "NameManager3", type: "png", site: "Excel", cat: "Name Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "NameManager4", type: "png", site: "Excel", cat: "Name Manager", sub: "New Name", report: "", ribbon: "", config: ""}, 
	{file: "RefBefore", type: "png", site: "Excel", cat: "Name Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "RefMiddle", type: "png", site: "Add-in", cat: "Quick Tools", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "RefAfter", type: "png", site: "Excel", cat: "Name Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "DefinedNamesSheetBefore", type: "png", site: "Excel", cat: "Name Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "DefinedNamesSheetAfter", type: "png", site: "Excel", cat: "Name Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "DefinedNamesBookBefore", type: "png", site: "Excel", cat: "Name Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "DefinedNamesBookAfter", type: "png", site: "Excel", cat: "Name Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "DefineNameRangeBefore", type: "png", site: "Add-in", cat: "Report", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "DefineNameRangeMiddle", type: "png", site: "Add-in", cat: "Quick Tools", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "DefineNameRangeAfter", type: "png", site: "Add-in", cat: "Report", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "DefineNameRangeAfter2", type: "png", site: "Excel", cat: "Name Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SelectedNameRangeBefore", type: "png", site: "Add-in", cat: "Report", sub: "", report: "", ribbon: "", config: "Yes"}, 
	{file: "SelectedNameRangeMiddle", type: "png", site: "Add-in", cat: "Quick Tools", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SelectedNameRangeAfter", type: "png", site: "Excel", cat: "Name Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "PrefixSuffix1", type: "png", site: "Add-in", cat: "Report", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "PrefixSuffix2", type: "png", site: "Add-in", cat: "Report", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "PrefixSuffix3", type: "png", site: "Add-in", cat: "Report", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SelectedNameRangeBefore", type: "png", site: "Add-in", cat: "Report", sub: "", report: "", ribbon: "", config: "Yes"}, 
	{file: "SelectedNameRangeMiddle", type: "png", site: "Add-in", cat: "Quick Tools", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "PrefixSuffix4", type: "png", site: "Excel", cat: "Name Manager", sub: "", report: "", ribbon: "", config: ""}
	]
description: The Names Tools within Quick Tools deal with defined names.
---
* * *

## Overview

The Names Tools within Quick Tools deal with defined names. Working with names is sometimes cumbersome within Excel. The Quick Tools makes the process easier and more convenient.

![](/images/QuickToolsNames/NamesTools.png)
<br>

### Excel Name Manager

For reference: To view all the names within the Workbook, click on "Name Manager" on the Formulas tab:

![](/images/QuickToolsNames/NameManager.png)
<br>

Each name has a scope, which can refer to a single sheet or the entire Workbook. The default scope when Excel creates a name is the Workbook. However, when a name is scoped to a single sheet, you can have multiple names with the same name, each referring to a single sheet. Notice there are 3 names that are scoped to the sheet "ReportVariable" and 3 similar names scoped to "ReportRange":

![](/images/QuickToolsNames/NameManager2.png)
<br>

You can define a name that is scoped to the entire Workbook by selecting the range and entering the name in the Name Box:

![](/images/QuickToolsNames/NameManager5.png)
<br>

To create a name scoped to a single sheet the Excel way, you have to use the Name manager. Select the range and click "New" from the Name Manger:

![](/images/QuickToolsNames/NameManager3.png)
<br>

Next, give the range a name and defined the scope:

![](/images/QuickToolsNames/NameManager4.png)
<br>


### Remove Names with Ref Errors from Book

Removes all named ranges in the Workbook with invalid references (Ref!).

Invalid references happen when cells refer to another cell that has been deleted. In such a case, Excel will display "Ref!" instead of the valid reference to indicate it is an invalid reference.

<b style='color:red;'><strong>Before:</strong></b>

This name refers to a cell that is currently invalid:

![](/images/QuickToolsNames/RefBefore.png)
<br>

<b style='color:green;'><strong>After:</strong></b>

![](/images/QuickToolsNames/RefMiddle.png)
<br>

![](/images/QuickToolsNames/RefAfter.png)
<br>

### Remove All Names from Sheet

Removes all user named ranges that are scoped to the current sheet.

<b style='color:red;'><strong>Before:</strong></b>

There are 3 names that are scoped to the current sheet "ReportRange":

![](/images/QuickToolsNames/DefinedNamesSheetBefore.png)
<br>

<b style='color:green;'><strong>After:</strong></b>

![](/images/QuickToolsNames/DefinedNamesSheetAfter.png)
<br>

### Remove All Names from Book

Removes all user named ranges in the entire Workbook.

Note: This will still retain certain Excel predefined names such as Print_Titles & Print_Area.

<b style='color:red;'><strong>Before:</strong></b>

![](/images/QuickToolsNames/DefinedNamesBookBefore.png)
<br>

<b style='color:green;'><strong>After:</strong></b>

![](/images/QuickToolsNames/DefinedNamesBookAfter.png)
<br>

### Create Range Name for Sheet

Creates a named range (Sheet scoped) for current cell or selected range.

<b style='color:red;'><strong>Before:</strong></b>

First select the range you want to define:

![](/images/QuickToolsNames/DefineNameRangeBefore.png)
<br>

Create a name for the range:

![](/images/QuickToolsNames/DefineNameRangeMiddle.png)
<br>

<b style='color:green;'><strong>After:</strong></b>

![](/images/QuickToolsNames/DefineNameRangeAfter.png)
<br>

Notice the new name is defined to the sheet "ReportRange":

![](/images/QuickToolsNames/DefineNameRangeAfter2.png)
<br>

### Create Range Names for Sheet for 2 Column Selection

Creates a named range or multiple names (Sheet scoped) for right side column cells, the names of which are supplied in the left side column cells (selection must be 2 columns and max 30 rows).

<b style='color:red;'><strong>Before:</strong></b>

First select the 2 column range you want to create names for:

![](/images/QuickToolsNames/SelectedNameRangeBefore.png)
<br>

Next open up the Interject Quick Tools and select the tool and click **OK**:

![](/images/QuickToolsNames/SelectedNameRangeMiddle.png)
<br>

<b style='color:green;'><strong>After:</strong></b>

Notice 3 names were created correspond to the entries in the left column and they are all scoped to the sheet:

![](/images/QuickToolsNames/SelectedNameRangeAfter.png)
<br>

### Appending A Prefix and/or Suffix To A Name

Interject can automatically have a prefix and/or suffix appended to a defined name when you create it using Quick Tools. For example, you may want to append the prefix "input_" to your filter names. You can also fix a suffix to the named ranges. It is best to include these config settings in a separate sheet.

**Step 1:** Open up a new Excel tab called "InterjectConfig".

![](/images/QuickToolsNames/NewTab.png)
<br>

**Step 2:** Select an empty spot within the sheet to store your prefix and suffix.

![](/images/QuickToolsNames/PrefixSuffix1.png)
<br>

**Step 3:** Select an empty cell and give it the named range of "InterjectConfig_Settings".

![](/images/QuickToolsNames/PrefixSuffix2.png)
<br>

**Step 4:** Interject will find any json pair in this named range to use. To have Excel format a json pair using the prefix and suffix set up, you can use the Interject [jSetting](/wIndex/jSetting.html) function. This function automatically formats a pair into json form. In the cell with the named range, enter the following:

```bash
=jSetting("NamedRangePrefix", C2)&jSetting("NamedRangeSuffix",C3)
```

The configurations are now set up.

![](/images/QuickToolsNames/PrefixSuffix3.png)
<br>

**Step 5:** Now select the 2 columns you want to create names for:

![](/images/QuickToolsNames/SelectedNameRangeBefore.png)
<br>

**Step 6:** Next open up the Interject Quick Tools and select the tool and click **OK**:

![](/images/QuickToolsNames/SelectedNameRangeMiddle.png)
<br>

Notice the defined names have the prefix and suffix you just set up:

![](/images/QuickToolsNames/PrefixSuffix4.png)
<br>

<blockquote class=highlight_note>
<b>Note:</b> The named range "InterjectConfig_Settings" can be scoped to the entire workbook or a particular sheet. Interject will apply the settings from the current sheet if they exist, otherwise it will apply the settings that are workbook scoped.</blockquote>
