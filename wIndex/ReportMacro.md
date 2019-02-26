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

