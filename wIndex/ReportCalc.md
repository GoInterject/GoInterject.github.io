---
title: ReportCalc()
layout: custom
keywords: [reportcalc, function]
description: ReportCalc executes a calculation on a worksheet or workbook. 
---

##  Function Summary 

ReportCalc executes a calculation on a worksheet or workbook. It will calculate any excel function, which includes INTERJECT functions, as long as they are within its target scope. ReportCalc can be triggered on specific events such as a Pull, Save, Clear, and Run. 

###  Function Arguments   

| Parameter Name   | Description                                                                                                                                   | Default | Optional |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- |
| OnPullSaveOrBoth | A switch that toggles which INTERJECT event ReportCalc will be executed on. There are three options: **Pull**, **Save**, **Both**.            |         | NO       |
| OnClearRunOrBoth | Another switch that toggles which INTERJECT event ReportCalc will be executed on. There are also three options: **Clear**, **Run**, **Both**. |         | NO       |
| SheetOrWorkBook  | SheetOrWorkbook determines the scope of information ReportCalc will calculate, and it only has two options: **Sheet** or **Workbook**         |         | NO       |
| SheetName        | This is only applicable if the chosen scope of the ReportCalc is **Sheet**, as it specifies which sheet to run the calculations on.           |         | YES      |
| Disable          | This is a switch that disables the ReportCalc if the toggle is changed to "TRUE"                                                              | FALSE   | YES      |

### Excel Formula Bar Example
```Excel
=ReportCalc("Both","Both","Sheet")
```

For an example of this formula in use, visit the [Lab Create: Hiding Rows & Columns](/wGetStarted/L-Create-HideRowCol.html#hiding-rows)



###  Function Composition 

| Argument Name    | Example Mapping | Explanation                                                                               |
| ---------------- | --------------- | ----------------------------------------------------------------------------------------- |
| Function Name    | =ReportCalc()   | The name of the report formula                                                            |
| OnPullSaveOrBoth | "Both"          | The ReportCalc will be executed on both a pull and a save                                 |
| OnClearRunOrBoth | "Both"          | The ReportCalc will be executed on both a clear and a run.                                |
| SheetOrWorkbook  | "Sheet"         | The ReportCalc will be executed on only the current sheet and not on the entire workbook. |