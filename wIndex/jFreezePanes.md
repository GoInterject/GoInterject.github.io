---
title: jFreezePanes()
layout: custom
keywords: [jfreezepanes, function]
description: This function is designed to be used along with the QuickTools option for freeze/unfreeze panes.
---

## Function Summary
Setting view ports in Excel using the native freeze panes functionality becomes rather trying at times. jFreezePanes() is to be placed directly on a report. This function is designed to be used along with the [QuickTools](/wGetStarted/INTERJECT-Ribbon-Menu-Items_83689479.html#quick-tools) option for freeze/unfreeze panes. Additionally, in the QuickTools menu, there is another option called **Freeze All Tabs** which will iterate through every worksheet in the active workbook and run the jFreezePanes() function on every page. It will only freeze panes on tabs that have jFreezePanes() function on them; additionally, when running **Freeze All Tabs** it will not unfreeze panes.


### Function Arguments

| Argument Name   | Description                                                                                                                                  | Default | Optional |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------|---------|----------|
| FreezePanesCell | Specifies what cell or range of cells the top row of the freeze panes. The rows between this and the anchorview cell will be frozen in place |         | NO       |
| AnchorViewCell  | Specifies what cell or range of cells will be at the very top of the sheet after a freeze panes is executed on the report.                   |         | NO       |

### Excel Formula Bar Example

```Excel
 jFreezePanes(A21,A15)
```
This example comes from [Lab Create: Customer Aging](/wGetStarted/L-Create-CustomerAging_128429314.html#final-result-1).

Even though the arguments for this function accepts range values, it is best practice to avoid using an entire row as a range, for example "14:14".

### Example Function Composition

| Argument Name   | Example Mapping | Explanation                                                                                                          |
|-----------------|-----------------|----------------------------------------------------------------------------------------------------------------------|
| Function Name   | `=jFreezePanes()` | This is the excel function name used to call the function. It can only be used as a standalone function in a report. |
| FreezePanesCell | A22             | This means that all rows below the 22st row will have the capability to scroll in the Excel viewport. Since this is set to column A, no columns are frozen.    |
| AnchorViewCell  | A15          | Specifies that the the rows below the 15th row and above the 21st row will be frozen in place and remain in the Excel viewport at all times even when scrolling.|
