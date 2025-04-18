---
title: Quick Tools
filename: "Quick-Tools-Landing.md"
layout: custom
keywords: [Quick Tools]
headings: ["Overview", "Quick Tools"]
links: ["/wIndex/QuickTools-Panes.html#freezeunfreeze-panes", "/wFunctions/jFreezePanes.html", "/wIndex/QuickTools-Panes.html#freeze-all-tabs", "/wFunctions/jFreezePanes.html", "/wIndex/QuickTools-Format.html#center-across-columns", "/wIndex/QuickTools-Format.html#remove-wrap", "/wIndex/QuickTools-Format.html#inverse-sign", "/wIndex/QuickTools-Format.html#to-lower-case-to-proper-case-to-upper-case", "/wIndex/QuickTools-Format.html#to-lower-case-to-proper-case-to-upper-case", "/wIndex/QuickTools-Format.html#to-lower-case-to-proper-case-to-upper-case", "/wIndex/QuickTools-Format.html#trim-values", "/wIndex/QuickTools-Formula.html#remove-external-references", "/wIndex/QuickTools-Edit.html#blanks-to-zeros", "/wIndex/QuickTools-Edit.html#zeros-to-blanks", "/wIndex/QuickTools-Edit.html#remove-sheet-objects", "/wIndex/QuickTools-Names.html#remove-names-with-ref-errors-from-book", "/wIndex/QuickTools-Names.html#remove-all-names-from-sheet", "/wIndex/QuickTools-Names.html#remove-all-names-from-book", "/wIndex/QuickTools-Names.html#create-range-name-for-sheet", "/wIndex/QuickTools-Names.html#create-range-names-for-sheet-for-2-column-selection", "/wIndex/QuickTools-Hyperlink.html#reset-hyperlink-targets-for-selection", "/wIndex/QuickTools-Hyperlink.html#createedit-interject-hyperlink", "/wIndex/INTERJECT-Link-Index.html", "/wIndex/QuickTools-Other.html#unique-list-from-selection", "/wIndex/QuickTools-Other.html#unhide-all-sheets"]
image_dir: "QuickToolsLanding"
images: [
	{file: "17", type: "png", site: "Add-in", cat: "Ribbon", sub: "", report: "", ribbon: "Advanced", config: ""}, 
	{file: "QuickTools", type: "png", site: "Add-in", cat: "Quick Tools", sub: "", report: "", ribbon: "", config: ""}
	]
description: The Quick Tools window provides a convenient set of macro tools suggested by our users.
---
* * *

##  Overview

The Quick Tools window provides a convenient set of macro tools suggested by our users. 

![](/images/QuickToolsLanding/17.png)
<br>

These tools are efficient ways to complete the most common actions in Interject. 

<blockquote class=highlight_note>
<b style='color:red;'><strong>Note: The Quick Tools are actions and cannot be undone with the Excel Undo feature (Ctrl-Z). Be sure to save your work beforehand.</strong></b>
</blockquote>

<br>

![](/images/QuickToolsLanding/QuickTools.png)
<br>

### Quick Tools

| Type | Tool | Description |
| ---- | ---- | ---- |
| Pane | [Freeze/Unfreeze Panes](/wIndex/QuickTools-Panes.html#freezeunfreeze-panes) | Unfreezes or freezes the current sheet panes using [jFreezePanes()](/wFunctions/jFreezePanes.html) settings | 
| Pane | [Freeze all Tabs](/wIndex/QuickTools-Panes.html#freeze-all-tabs) | Unfreezes or freezes all sheet panes using [jFreezePanes()](/wFunctions/jFreezePanes.html) settings |
| Format | [Center Across Columns](/wIndex/QuickTools-Format.html#center-across-columns) | Centers across columns without merging cells for the selected cells |
| Format | [Remove Wrap](/wIndex/QuickTools-Format.html#remove-wrap) | Removes the word wrap formatting for the selected cells |
| Format | [Inverse Sign](/wIndex/QuickTools-Format.html#inverse-sign) | Reverses the sign of any numeric amount for the selected cells |
| Format | [To Lower Case](/wIndex/QuickTools-Format.html#to-lower-case-to-proper-case-to-upper-case) | Converts text to 'lower case' for the selected cells |
| Format | [To Proper Case](/wIndex/QuickTools-Format.html#to-lower-case-to-proper-case-to-upper-case) | Converts text to 'Proper Case' for the selected cells |
| Format | [To Upper Case](/wIndex/QuickTools-Format.html#to-lower-case-to-proper-case-to-upper-case) | Converts text to 'UPPER CASE' for the selected cells |
| Format | [Trim Values](/wIndex/QuickTools-Format.html#trim-values) | Trims spaces from start and end of text for the selected cells |
| Formula | [Remove External References](/wIndex/QuickTools-Formula.html#remove-external-references) | Removes all external references in the workbook with their values |  |
| Edit | [Blanks to Zeros](/wIndex/QuickTools-Edit.html#blanks-to-zeros) | Replaces any blank cells with zeroes for the selected cells |  |
| Edit | [Zeroes to Blanks](/wIndex/QuickTools-Edit.html#zeros-to-blanks) | Replaces any zero values with blanks for the selected cells |  |
| Edit | [Remove Sheet Objects](/wIndex/QuickTools-Edit.html#remove-sheet-objects) | Removes any shapes, pictures or other objects from the current sheet |  |
| Names | [Remove Names with Ref Errors from Book](/wIndex/QuickTools-Names.html#remove-names-with-ref-errors-from-book) | Removes all named ranges with invalid references (Ref!) in the workbook]() |  |
| Names | [Remove All Names from Sheet](/wIndex/QuickTools-Names.html#remove-all-names-from-sheet) | Removes all user named ranges that are scoped to the current sheet |  |
| Names | [Remove All Names from Book](/wIndex/QuickTools-Names.html#remove-all-names-from-book) | Removes all user named ranges in the workbook |  |
| Names | [Create Range Name for Sheet](/wIndex/QuickTools-Names.html#create-range-name-for-sheet) | Creates a named ranged scoped to the sheet for the selected range |  |
| Names | [Create Range Names for Sheet for 2 Column Selection](/wIndex/QuickTools-Names.html#create-range-names-for-sheet-for-2-column-selection) | For every value in the first column, creates named ranges in the second column (scoped to the sheet). Create names InterjectConfig_NamedRangePrefix and InterjectConfig_NamedRangeSuffix to modify name created. |  |
| Hyperlink | [Reset Hyperlink Targets for Selection](/wIndex/QuickTools-Hyperlink.html#reset-hyperlink-targets-for-selection) | Fixes hyperlink targets to point to current sheet for selected cells |  |
| Hyperlink | [Create/Edit Interject Hyperlink](/wIndex/QuickTools-Hyperlink.html#createedit-interject-hyperlink) | Opens a window to create/edit special [Interject Hyperlinks](/wIndex/INTERJECT-Link-Index.html). Add name range InterjectStyle_Hyperlink on formatted cell to preserve style of hyperlink. |  |
| Other | [Unique List from Selection](/wIndex/QuickTools-Other.html#unique-list-from-selection) | Create a unique list of values from selected cells places in a new tab |  |
| Other | [Unhide All Sheets](/wIndex/QuickTools-Other.html#unhide-all-sheets) | Unhides all hidden sheets in the workbook |  |
