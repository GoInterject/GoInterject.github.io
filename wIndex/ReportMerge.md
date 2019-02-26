---
title: ReportMerge()
layout: custom
keywords: [reportmerge, function]
description: Allows the user to merge multiple Excel reports into one based on jMergePoints. 
---

##  Function Summary 
Allows the user to merge multiple Excel reports into one based on [ jMergePoints ](/wIndex/jMergePoint.html) . For examples and discussion, view the tutorial. 

###  Function Arguments   

| Parameter Name | Description                                                                                                   | Default | Optional |
| -------------- | ------------------------------------------------------------------------------------------------------------- | ------- | -------- |
| FileName       | The name of the workbook to connect. Either a full path name to the file, or a Report Library Sheet Link Code |         | NO       |
| MergeID        | A unique ID to identify the jMerge (required to clear tabs)                                                   |         | YES      |
| RemoveTabsOnClear | Indicates whether or not to delete merged tabs upon clearing data            | FALSE (TRUE requires a MergeID Value) | YES      |
| PullOnOpen     | Run a pull on the worksheet after opening                                                                     | FALSE   | YES      |
| MergePoints    | Provide a range reference to a list of jMergePoint functions. If none is provided, then all jMergePoint functions within the book will be considered | | YES |
| Disabled       | Function will not execute on pull if set to true                                                              | FALSE   | YES      |

### Excel Formula Bar Example

###  Function Composition