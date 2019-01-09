---
title: ReportHideRowOrColumn()
layout: custom
keywords: [reporthideroworcolumn, function]
description: ReportHideRowOrColumn() utilizes cell the values "Show" and "Hide" as input parameters. 
---

## Function Summary

ReportHideRowOrColumn() utilizes cell the values "Show" and "Hide" as input parameters. These parameters are set within the RowOrColumnRange argument, wherein if a cell within that range has a value of "Hide" then the function will hide that column or row depending on which type of cell range is being used. Additionally, this function is triggered on an INTERJECT Action+Event combination. Also, this function requires a [ReportCalc()](/wIndex/ReportCalc_137265163.html) function to be executed in the INTERJECT call stack before the ReportHideRowOrColumn() is called in the stack. This is because the ReportHideRowOrColumn() function requires the most up to date cell formula outputs (if formulas are being used to create the "Show"/"Hide" cell values), which does not occur if the ReportHideRowOrColumn() function is called directly after a trigger combination is called.  There are several trigger combinations that can be utilized by ReportGrouping() that are listed [here](/wIndex/ReportHideRowOrColumn_341147669.html#trigger-combination-list).

### Function Arguments

|Argument Name|Description|Default|Optional|
|:---|:---|:---|:---|
|OnPullSaveOrBoth|This defines the instance in which an INTERJECT action will trigger the function to be executed.||NO|
|OnClearRunOrBoth|This defines which INTERJECT event will trigger the function to be executed.                    ||NO|
|RowOrColumnRange| Specifies a cell range that is either a single column or a single row but **NOT** both.||NO|
|Disabled| This disables the function if the value is "TRUE" and is used when testing a report.|FALSE|YES|

### Excel Formula Bar Example
```Excel
ReportHideRowOrColumn("Pull","Both",C47:C48,FALSE)
```

To view this example with more context it is sourced from [Lab Create: HidingRowsColumns](/wGetStarted/L5-HidingRowsColumns_137363494.html).

### Example Function Composition

|Argument Name|Example Mapping|Explanation|
|:---|:---|:---|
|Function Name|`=ReportHideRowOrColumn()`|This is the excel function name used to call the function. It can only be used as a standalone function in a report.|
|OnPullSaveOrBoth|"Pull"| Determines that the function will be triggered on a Pull action.|
|OnClearRunOrBoth|"Both"| This specifies that the function will  be triggered on a Clear or Run event. The trigger combination created is a Pull-Clear or a Pull-Run. These triggers are created by combining this argument with the value for OnPullSaveOrBoth.|
|RowOrColumnRange|C47:C48| Specifies the single column range from cell C47 to C48. This is often placed on a target data range of a [Data](Data-Functions-Landing.html) function.|
|Disabled|FALSE| This is left false since the ReportHideRowOrColumn() function is active.|


### Trigger Combination List
The execution of the ReportDefaults() formatting function is determined by a combination of an INTERJECT action and an INTERJECT event. An action is a pull or save whereas an event is a clear or a run.

| Argument Name    | Function Event Trigger Options | Option Explanation                                                                            |
|------------------|--------------------------------|-----------------------------------------------------------------------------------------------|
| **Trigger 1**    |                                |                                                                                               |
| OnPullSaveOrBoth | "Pull"                         | This will trigger the default to execute when the user performs a Pull-Run INTERJECT event.   |
| OnClearRunOrBoth | "Run"                          |                                                                                               |
| **Trigger 2**    |                                |                                                                                               |
| OnPullSaveOrBoth | "Pull"                         | This will trigger the default to execute when the user performs a Pull-Clear INTERJECT event. |
| OnClearRunOrBoth | "Clear"                        |                                                                                               |
| **Trigger 3**    |                                |                                                                                               |
| OnPullSaveOrBoth | "Save"                         | This will trigger the default to execute when the user performs a Save-Run INTERJECT event.   |
| OnClearRunOrBoth | "Run"                          |                                                                                               |
| **Trigger 4**    |                                |                                                                                               |
| OnPullSaveOrBoth | "Save"                         | This will trigger the default to execute when the user performs a Save-Clear INTERJECT event. |
| OnClearRunOrBoth | "Clear"                        |                                                                                               |
| **Trigger 5**    |                                |                                                                                               |
| OnPullSaveOrBoth | "Both"                         | This will trigger the default to execute when the user performs a Save-Run, Save-Clear, Pull-Run, Pull-Clear INTERJECT event. |
| OnClearRunOrBoth | "Both"                         |                                                                                               |
| **Trigger 6**    |                                |                                                                                               |
| OnPullSaveOrBoth | "Both"                         | This will trigger the default to execute when the user performs a Save-Clear or a Pull-Clear INTERJECT event. |
| OnClearRunOrBoth | "Clear"                        |                                                                                               |
| **Trigger 7**    |                                |                                                                                               |
| OnPullSaveOrBoth | "Save"                         | This will trigger the default to execute when the user performs a Save-Clear or a Save-Run INTERJECT event. |
| OnClearRunOrBoth | "Both"                        |                                                                                               |
| **Trigger 8**    |                                |                                                                                               |
| OnPullSaveOrBoth | "Pull"                         | This will trigger the default to execute when the user performs a Pull-Clear or a Pull-Run INTERJECT event. |
| OnClearRunOrBoth | "Both"                        |                                                                                               |

### Required Function List
* [ReportCalc()](/wIndex/ReportCalc_137265163.html)
