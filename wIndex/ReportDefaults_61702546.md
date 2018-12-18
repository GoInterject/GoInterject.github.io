---
title: ReportDefaults()
layout: custom
---

## Function Summary

A ReportDefaults() formatting function is utilized to capture and send values from one cell (or set of cells) to another. It gets executed on a specified INTERJECT action and then it captures the values from one cell (or set of cells) and sends the values to the corresponding target cell(s). To view a list of actions go to the [Trigger Combination List](/wIndex/ReportDefaults_61702546.html#trigger-combination-list). Many times, the ReportDefaults() function is used to clear out report filters after an INTERJECT clear is performed. This is because [Data Functions](/wIndex/Data-Functions-Landing.html) do not clear the filters after a clear action since they only clear their corresponding target data ranges. Additionally, a ReportDefaults() function can be used to set default filter parameters after an INTERJECT action has occurred.

### Function Arguments

| Argument Name   | Description | Default | Optional |
|------------------|-------------|---------|----------|
| OnPullSaveOrBoth | This defines the instance in which an INTERJECT action will trigger the function to be executed.|         | NO       |
| OnClearRunOrBoth | This defines which INTERJECT event will trigger the function to be executed.                    |         | NO       |
| TransferPairs    | Enter  [ Pairs  ](/wIndex/Pair_81756188.html) within a  [ PairGroup  ](/wIndex/PairGroup_81756186.html) function to copy data and restrict what data is captured. See [ Drill: Customer Aging Report ](/wGetStarted/128421015.html) for more information on usage. |         | YES      |

### Excel Formula Bar Example

```Excel
ReportDefaults("Save","Clear",PairGroup(Pair("",C12,FALSE)))
```
An example of this function is currently in construction in our documentation labs. Check back soon for an example with more context.

### Example Function Composition

| Argument Name    | Example Mapping               | Explanation                                                                                                          |
|------------------|-------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Function Name    | `=ReportDefaults()`           | This is the excel function name used to call the function. It can only be used as a standalone function in a report. |
| OnPullSaveOrBoth | "Pull"                        | The report default will be triggered to run on a pull action                                                         |
| OnClearRunOrBoth | "Clear"                       | The clear event means that the function will be triggered on a combination of "Pull-Clear".                          |
| TransferPairs    | PairGroup(Pair("",C12,FALSE)) | This will copy a blank value and place it as the new value for C12.                                                  |


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


### Embeddable Helper Functions

* [Pair](/wIndex/Pair_81756188.html)
* [PairGroup](/wIndex/PairGroup_81756186.html)