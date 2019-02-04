---
title: ReportDrill()
layout: custom
keywords: [reportdrill, function]
description: ReportDrill is widely used throughout INTERJECT as a way to connect and pass information between workbooks and worksheets. 
---

## Function Summary

ReportDrill is widely used throughout INTERJECT as a way to connect and pass information between workbooks and worksheets. Drilling takes a defined input and passes it in as a parameter to another workbook or worksheet, similar to hyperlinks on a web page: Depending on the types of input behind the hyperlink, more detailed and specific information can be viewed. While there are few codes crucial to the process, they can be structured in ways that make them very powerful. In order to setup a drill that goes to another workbook it is necessary to setup drill codes in the [Report Library](/wGetStarted/L-Create-UpdatingReportLibrary#adding-a-drill-code-to-a-report) which have to be registered with INTERJECT.

### Function Arguments

| Parameter Name  | Description                                                                                                                                                                                | Default | Optional |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|----------|
| ReportCellToRun | A cell address on a worksheet within your report that contains an INTERJECT [Data](Data-Functions-Landing.html) or [Formatting](Formatting-Functions-Landing.html) function.               |         | YES      |
| ReportCodeToRun | A drill code that is setup in the [Report Library](/wGetStarted/L-Create-UpdatingReportLibrary#adding-a-drill-code-to-a-report) that allows you to drill between workbooks. |         | YES      |
| TransferPairs   | A [PairGroup](Pairgroup.html) and [Pair](Pair.html) function that determines which cell value you want to capture, and where you want to place it.                       |         | YES      |
| DrillName       | This defines the name of the drill displayed on the Excel report.                                                                                                                          |         | YES      |


### Excel Formula Bar Example

```Excel
ReportDrill(CustomerOrderHistory!C10,,PairGroup(Pair(B22:B24, CustomerOrderHistory!C23)),"Drill to Customer Orders History")
```
This example is sourced from [Lab Drill: Customer Aging](/wGetStarted/L-Drill-CustomerAging.html).

### Example Function Composition

| Argument Name   | Example Mapping                                    | Explanation                                                                                                                                                                                                                                                           |
|-----------------|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Function Name   | `=ReportDrill()`                                   | This is the excel function name used to call the function. It can have embedded functions.                                                                                                                                                                            |
| ReportCellToRun | CustomerOrderHistory!C10                           | The cell that is being run is an INTERJECT Data function on the CustomerOrderHistory Page. If this is left blank, then ReportCodeToRun cannot be blank.                                                                                                               |
| ReportCodeToRun | ""                                                 | This is left blank since the drill does not go to a different workbook. This cannot be left blank if the ReportCellToRun argument is left blank. If you wanted to run a drill on a different workbook, place the target workbook's drill code in this argument field. |
| TransferPairs   | PairGroup(Pair(B22:B24, CustomerOrderHistory!C23)) | This will copy a cell value from a cell within the specified range, then place that value on the CustomerOrderHistory worksheet, at cell C23.                                                                                                                         |
| DrillName       | "Drill to Customer Orders History"                 | The Drill name will appear as "Drill to Customer Orders History" inside of the drill form.                                                                                                                                                                            |

### Embeddable Helper Functions

* [PairGroup](Pairgroup.html)
* [Pair](Pair.html)

