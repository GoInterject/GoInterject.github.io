---
title: ReportGrouping()
layout: custom
---

## Function Summary



### Function Arguments

|Parameter Name|Description|Default|Optional|
|:---|:---|:---|:---|
|OnPullSaveOrBoth||||
|OnClearRunOrBoth||||
|RowOrColumnGroup||||
|GroupLevel||||
|Disabled||||

### Excel Formula Bar Example

```Excel
ReportGrouping("Both","Run","Column","Collapse",FALSE)
```
An example of this function is currently in construction in our documentation labs. Check back soon for an example with more context.

### Example Function Composition

|Argument Name|Example Mapping|Explanation|
|:---|:---|:---|
|Function Name|`=ReportGrouping()`||
|OnPullSaveOrBoth|||
|OnClearRunOrBoth|||
|RowOrColumnGroup|||
|GroupLevel|||
|Disabled|||

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
