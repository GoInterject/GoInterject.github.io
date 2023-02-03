---
title: Quick Tools - Names Tools
layout: custom
keywords: [Quick Tools, Names Tools, Remove Names with Ref Errors from Book, Remove All Names from Sheet, Remove All Names from Book, Create Range Name for Sheet, Create Range Names for Sheet for 2 Column Selection]
description: The Names Tools within Quick Tools deal with defined names.
---
* * *

## Overview

The Names Tools within Quick Tools deal with defined names.

![](/images/QuickTools/NamesTools.png)
<br>

### Remove Names with Ref Errors from Book

Removes all defined names in Workbook with invalid references (Ref!).

Before:

![](/images/QuickTools/RefBefore.png)
<br>

After:

![](/images/QuickTools/RefMiddle.png)
<br>

![](/images/QuickTools/RefAfter.png)
<br>

### Remove All Names from Sheet

Removes all defined names in the current sheet (retains Print Titles & Area names).

Before (Click on the <**Name Manager**> for a list of defined names):

![](/images/QuickTools/DefinedNamesBefore.png)
<br>

After (Notice only the defined names scoped to "CustomerAging" tab are removed):

![](/images/QuickTools/DefinedNamesSheetAfter.png)
<br>

### Remove All Names from Book

Removes all defined names in the Workbook (retains Print Titles & Area names).

Before:

![](/images/QuickTools/DefinedNamesSheetAfter.png)
<br>

After (Notice the Print Titles & Area names are retained):

![](/images/QuickTools/DefinedNamesBookAfter.png)
<br>

### Create Range Name for Sheet

Creates a defined name (Sheet scoped) for current cell or selected range.

Before:

![](/images/QuickTools/DefineNameRangeBefore.png)
<br>

Create a name for the range:

![](/images/QuickTools/DefineNameRangeMiddle.png)
<br>

After:

![](/images/QuickTools/DefineNameRangeAfter.png)
<br>

### Create Range Names for Sheet for 2 Column Selection

Creates a defined name or multiple names (Sheet scoped) for right side column cells, the names of which are supplied in the left side column cells (selection must be 2 columns and max 30 rows).

Before:

![](/images/QuickTools/SelectedNameRangeBefore.png)
<br>

After:

![](/images/QuickTools/SelectedNameRangeAfter.png)
<br>

You can automatically have a prefix and/or suffix appended to these names by using a defined name. First select an empty cell and type in the prefix or suffix you want to be appended. Give the cell the name "InterjectConfig_NamedRangePrefix" or "InterjectConfig_NamedRangeSuffix":

![](/images/QuickTools/SelectedNameRangePrefix.png)
<br>

Next run the Quick Tool "Create Range Names for Sheet for Selected Labels":

![](/images/QuickTools/SelectedNameRangeAfter2.png)
<br>

Notice the defined names have the prefix or suffix you just set up:

![](/images/QuickTools/SelectedNameRangeAfter3.png)
<br>


