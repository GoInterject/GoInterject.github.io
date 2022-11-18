---
title: ReportMacro()
layout: custom
keywords: [reportmacro, function]
description: ReportMacro allows a report developer to call VBA macros on Save, Pull, Clear, or Run events. 
---
* * *

##  Function Summary 
ReportMacro allows a report developer to call VBA macros on Save, Pull, Clear, or Run events. The VBA macro must be a named Sub in the workbook. This function will ignore all errors during the macro's execution. 

###  Function Arguments   
  
| Parameter Name   | Description                                                                               | Default | Optional |
| ---------------- | ----------------------------------------------------------------------------------------- | ------- | -------- |
| OnPullSaveOrBoth | Events will be triggered on **Pull**, **Save**, or both. This parameter accepts a string. |         | NO       |
| OnClearRunOrBoth | Events will be triggered on **Clear**, **Run**, or both. This parameter accepts a string. |         | NO       |
| MacroNameToRun | The macro Sub name that will be executed. The placement of this function determines when it is run in comparison to other Report formulas. | | NO |

### Excel Formula Bar Example
```Excel
=ReportMacro("Pull","Both","MyCustomFunction")
```

To see an example of this function in use, visit the [Lab Create: Using Report Macro](/wGetStarted/L-Create-ReportMacro.html)

###  Function Composition

| Argument Name    | Example Mapping    | Explanation                                           |
| ---------------- | ------------------ | ----------------------------------------------------- |
| Function Name    | =ReportMacro()     | The name of the report formula.                       |
| OnPullSaveOrBoth | "Pull"             | The Macro will only run on a pull event.              |
| OnClearRunOrBoth | "Both"             | It will be run on the clear or run event of the pull. |
| MacroNameToRun   | "MyCustomFunction" | Only the function specified will be ran.              |


### Trigger Combination List

The execution of the ReportDefaults() formatting function is determined by a combination of an Interject action and an Interject event. An action is a pull or save whereas an event is a clear or a run.

| Argument Name    | Function Event Trigger Options | Option Explanation                                                                            |
|------------------|--------------------------------|-----------------------------------------------------------------------------------------------|
| **Trigger 1**    |                                |                                                                                               |
| OnPullSaveOrBoth | "Pull"                         | This will trigger the default to execute when the user performs a Pull-Run Interject event.   |
| OnClearRunOrBoth | "Run"                          |                                                                                               |
| **Trigger 2**    |                                |                                                                                               |
| OnPullSaveOrBoth | "Pull"                         | This will trigger the default to execute when the user performs a Pull-Clear Interject event. |
| OnClearRunOrBoth | "Clear"                        |                                                                                               |
| **Trigger 3**    |                                |                                                                                               |
| OnPullSaveOrBoth | "Save"                         | This will trigger the default to execute when the user performs a Save-Run Interject event.   |
| OnClearRunOrBoth | "Run"                          |                                                                                               |
| **Trigger 4**    |                                |                                                                                               |
| OnPullSaveOrBoth | "Save"                         | This will trigger the default to execute when the user performs a Save-Clear Interject event. |
| OnClearRunOrBoth | "Clear"                        |                                                                                               |
| **Trigger 5**    |                                |                                                                                               |
| OnPullSaveOrBoth | "Both"                         | This will trigger the default to execute when the user performs a Save-Run, Save-Clear, Pull-Run, Pull-Clear Interject event. |
| OnClearRunOrBoth | "Both"                         |                                                                                               |
| **Trigger 6**    |                                |                                                                                               |
| OnPullSaveOrBoth | "Both"                         | This will trigger the default to execute when the user performs a Save-Clear or a Pull-Clear Interject event. |
| OnClearRunOrBoth | "Clear"                        |                                                                                               |
| **Trigger 7**    |                                |                                                                                               |
| OnPullSaveOrBoth | "Save"                         | This will trigger the default to execute when the user performs a Save-Clear or a Save-Run Interject event. |
| OnClearRunOrBoth | "Both"                        |                                                                                               |
| **Trigger 8**    |                                |                                                                                               |
| OnPullSaveOrBoth | "Pull"                         | This will trigger the default to execute when the user performs a Pull-Clear or a Pull-Run Interject event. |
| OnClearRunOrBoth | "Both"                        |                                                                                               |



