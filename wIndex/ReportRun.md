---
title: ReportRun()
layout: custom
keywords: [reportrun, function]
description: ReportRun executes a Report Function in another tab without changing the tab focus. 
---

##  Function Summary 

ReportRun executes a Report Function in another tab without changing the tab focus. It can handle both run and clear events. 


###  Function Arguments   
| Parameter Name | Description | Default | Optional |
| -------------- | ----------- | ------- | -------- |
|ReportCellToRun | A range within the target worksheet to run a report function. | | NO |
| RunEntireWorksheet | A boolean toggle that will enable or disable an entire worksheet's report functions from running | TRUE | YES |
| OnAction | A control for which type of report function to run. Options include: <br> * Pull <br> * Save <br> * PullAndSave <br> * PullClear <br> * SaveClear <br> * PullAndSaveClear <br> * Back | PULL | YES |

  
### Excel Formula Bar Example
```Excel
=ReportRun(ReportRunTargetForPivot!C4,TRUE,"PullClear")
```

To see an example of this function in use, visit the [Pivot table lab.](/wGetStarted/L-Create-PivotTable.html)


###  Function Composition 
| Argument Name      | Example Mapping            | Explanation                                                                                                                  |
| ------------------ | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Function Name      | =ReportRun()               | The name of the report formula                                                                                               |
| ReportCellToRun    | ReportRunTargetForPivot!C4 | Specify what range in the worksheet to run the action. In this case, run the report range in the target sheet located in C4. |
| RunEntireWorksheet | TRUE                       | Run all the pulls in the target worksheet not just the one specificed above.                                                 |
| OnAction           | PullClear                  | This will happen on the "PullClear" Event only                                                                               |
