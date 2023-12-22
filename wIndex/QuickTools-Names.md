---
title: Quick Tools - Names Tools
layout: custom
keywords: [Quick Tools, Names Tools, Remove Names with Ref Errors from Book, Remove All Names from Sheet, Remove All Names from Book, Create Range Name for Sheet, Create Range Names for Sheet for 2 Column Selection]
headings: ["Overview", "Excel Name Manager", "Remove Names with Ref Errors from Book", "Remove All Names from Sheet", "Remove All Names from Book", "Create Range Name for Sheet", "Create Range Names for Sheet for 2 Column Selection", "Appending A Prefix and/or Suffix To A Name"]
description: The Names Tools within Quick Tools deal with defined names.
---
* * *

## Overview

The Names Tools within Quick Tools deal with defined names. Working with names is sometimes cumbersome within Excel. The Quick Tools makes the process easier and more convenient.

![](/images/QuickTools/NamesTools.png)
<br>

### Excel Name Manager

For reference: To view all the names within the Workbook, click on "Name Manager" on the Formulas tab:

![](/images/QuickTools/NameManager.png)
<br>

Each name has a scope, which can refer to a single sheet or the entire Workbook. The default scope when Excel creates a name is the Workbook. However, when a name is scoped to a single sheet, you can have multiple names with the same name, each referring to a single sheet. Notice there are 3 names that are scoped to the sheet "ReportVariable" and 3 similar names scoped to "ReportRange":

![](/images/QuickTools/NameManager2.png)
<br>

You can define a name that is scoped to the entire Workbook by selecting the range and entering the name in the Name Box:

![](/images/QuickTools/NameManager5.png)
<br>

To create a name scoped to a single sheet the Excel way, you have to use the Name manager. Select the range and click "New" from the Name Manger:

![](/images/QuickTools/NameManager3.png)
<br>

Next, give the range a name and defined the scope:

![](/images/QuickTools/NameManager4.png)
<br>


### Remove Names with Ref Errors from Book

Removes all named ranges in the Workbook with invalid references (Ref!).

Invalid references happen when cells refer to another cell that has been deleted. In such a case, Excel will display "Ref!" instead of the valid reference to indicate it is an invalid reference.

<b style='color:red;'><strong>Before:</strong></b>

Note: This name refers to a cell that is currently invalid:

![](/images/QuickTools/RefBefore.png)
<br>

<b style='color:green;'><strong>After:</strong></b>

![](/images/QuickTools/RefMiddle.png)
<br>

![](/images/QuickTools/RefAfter.png)
<br>

### Remove All Names from Sheet

Removes all user named ranges that are scoped to the current sheet.

<b style='color:red;'><strong>Before:</strong></b>

Note: There are 3 names that are scoped to the current sheet "ReportRange":

![](/images/QuickTools/DefinedNamesSheetBefore.png)
<br>

<b style='color:green;'><strong>After:</strong></b>

![](/images/QuickTools/DefinedNamesSheetAfter.png)
<br>

### Remove All Names from Book

Removes all user named ranges in the entire Workbook.

Note: This will still retain certain Excel predefined names such as Print_Titles & Print_Area.

<b style='color:red;'><strong>Before:</strong></b>

![](/images/QuickTools/DefinedNamesBookBefore.png)
<br>

<b style='color:green;'><strong>After:</strong></b>

![](/images/QuickTools/DefinedNamesBookAfter.png)
<br>

### Create Range Name for Sheet

Creates a named range (Sheet scoped) for current cell or selected range.

<b style='color:red;'><strong>Before:</strong></b>

First select the range you want to define:

![](/images/QuickTools/DefineNameRangeBefore.png)
<br>

Create a name for the range:

![](/images/QuickTools/DefineNameRangeMiddle.png)
<br>

<b style='color:green;'><strong>After:</strong></b>

![](/images/QuickTools/DefineNameRangeAfter.png)
<br>

Notice the new name is defined to the sheet "ReportRange":

![](/images/QuickTools/DefineNameRangeAfter2.png)
<br>

### Create Range Names for Sheet for 2 Column Selection

Creates a named range or multiple names (Sheet scoped) for right side column cells, the names of which are supplied in the left side column cells (selection must be 2 columns and max 30 rows).

<b style='color:red;'><strong>Before:</strong></b>

First select the 2 column range you want to create names for:

![](/images/QuickTools/SelectedNameRangeBefore.png)
<br>

Next open up the Interject Quick Tools and select the tool and click **OK**:

![](/images/QuickTools/SelectedNameRangeMiddle.png)
<br>

<b style='color:green;'><strong>After:</strong></b>

Notice 3 names were created correspond to the entries in the left column and they are all scoped to the sheet:

![](/images/QuickTools/SelectedNameRangeAfter.png)
<br>

### Appending A Prefix and/or Suffix To A Name

Interject can automatically have a prefix and/or suffix appended to a defined name when you create it using Quick Tools. For example, you may want to append the prefix "input_" to your filter names. You must first set up a few defined names for this to work.

**Step 1:** First select an empty spot within the report to store your prefix and suffix:

![](/images/QuickTools/PrefixSuffix1.png)
<br>

**Step 2:** Next, select the prefix name and give it the defined name "InterjectConfig_NamedRangePrefix":

![](/images/QuickTools/PrefixSuffix2.png)
<br>

**Step 3:** Give the suffix name the defined name "InterjectConfig_NamedRangeSuffix":

![](/images/QuickTools/PrefixSuffix3.png)
<br>

**Step 4:** Now select the 2 columns you want to create names for:

![](/images/QuickTools/SelectedNameRangeBefore.png)
<br>

**Step 5:** Next open up the Interject Quick Tools and select the tool and click **OK**:

![](/images/QuickTools/SelectedNameRangeMiddle.png)
<br>

Notice the defined names have the prefix and suffix you just set up:

![](/images/QuickTools/PrefixSuffix4.png)
<br>
