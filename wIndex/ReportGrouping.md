---
title: ReportGrouping()
layout: custom
keywords: [reportgrouping, function]
description: The ReportGrouping() INTERJECT formatting function is a triggered INTERJECT function. 
---

## Function Summary

The ReportGrouping() INTERJECT formatting function is a triggered INTERJECT function. This means that upon the execution of an INTERJECT action, a triggered function is activated. There are several trigger combinations that can be utilized by ReportGrouping() that are listed [here](/wIndex/ReportGrouping.html#trigger-combination-list). A ReportGrouping() function is often used to collapse or expand a native excel grouping upon the execution of an INTERJECT action. 

### Function Arguments

|Argument Name|Description|Default|Optional|
|:---|:---|:---|:---|
|OnPullSaveOrBoth|This defines the instance in which an INTERJECT action will trigger the function to be executed.||NO|
|OnClearRunOrBoth|This defines which INTERJECT event will trigger the function to be executed.                    ||NO|
|RowOrColumnGroup| Specifies which type of grouping to be impacted by the ReportGrouping() function. Can only be "Row" or "Column".||NO|
|GroupLevel| This accepts a value of "Expand", or "Collapse", or a level value to change an existing grouping to (1-8).||NO|
|Disabled| This disables the function if the value is "TRUE" and is used when testing a report.|FALSE|YES|

### Excel Formula Bar Example
```Excel
ReportGrouping("Both","Run","Column","Collapse",FALSE)
```
An example of this function is currently in construction in our documentation labs. Check back soon for an example with more context.

### Example Function Composition

|Argument Name|Example Mapping|Explanation|
|:---|:---|:---|
|Function Name|=ReportGrouping()|This is the excel function name used to call the function. It can only be used as a standalone function in a report.|
|OnPullSaveOrBoth|"Both"| This function will be executed on a Pull or a Save action. |
|OnClearRunOrBoth|"Run"| This function will be executed on a Pull-Run or a Save-Run Action+Event combination.|
|RowOrColumnGroup|"Column"|Specifies that that the groupings to be impacted will be "Column" groupings and thus "Row" groupings are left unaltered.|
|GroupLevel|"Collapse"|In combination with the RowOrColumnGroup argument, this will Collapse all column groupings on a Pull-Run, or Save-Run action.|
|Disabled|FALSE| This is left false since the ReportGrouping() function is active.|

### Trigger Combination List
The execution of the ReportGrouping() formatting function is determined by a combination of an INTERJECT action and an INTERJECT event. An action is a pull or save whereas an event is a clear or a run.

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
