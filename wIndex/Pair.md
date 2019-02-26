---
title: Pair()
layout: custom
keywords: [pair, function]
description: The Pair() function is used to specify a, "From" value or range to a, "Target" location or range. It is not meant to be standalone function, rather, it is meant to be used with a PairGroup() function.
---
##  Function Summary 

The Pair() function is used to specify a **From** value or range to a **Target** location or range. It is not meant to be standalone function, rather, it is meant to be used with a [PairGroup()](PairGroup.md) function. It is best practice to always embed the Pair() function inside a PairGroup() function even when you only need to use one Pair() action. The Pair() and PairGroup() functions are meant to be embedded inside of [Data functions](Data-Functions-Landing.html). This is because the action of copying the value of a cell and having a target cell receive the value requires a trigger produced by an INTERJECT Event. To check which functions Pair() can be used with, see the list at  the bottom of this page.

###  Function Arguments   

| Argument Name | Description                                                                                                    | Default | Optional |
|----------------|----------------------------------------------------------------------------------------------------------------|---------|----------|
| From           | Enter a range or string that describes what will be copied from into the specified target                      |         | NO       |
| Target         | Enter a range or string related to a target cell that will receive the values specified in the From parameter. |         | NO       |
| RequireValue   | Enter a True or False to indicate if the From value is required to exist in the data.                          | TRUE    | YES      |
| ScopeRange     | This will limit the pair to only be used when the user is selected in the entered range.                       |         | YES      |

### Excel Formula Bar Example

```Excel
Pair(B22:B24,CustomerOrderHistory!C23)
```
This example can be found in [Lab Drill: Customer Aging](/wGetStarted/L-Drill-CustomerAging.html)

### Example Function Composition   

| Argument Name | Example Mapping          | Explanation|
|---------------|--------------------------|---|
| Function Name | =Pair()                 | This is the excel name used to call the function. It is not meant to standalone and is meant to be embedded inside of a [ PairGroup() ](PairGroup.html) function. |
| From          | B22:B24                  | In this example this represents a range of cells that expands and contracts with a [ReportRange()](/wIndex/ReportRange.html) function. Only a single cell value from within this range of cells will be selected to be copied. That cell is defined by user selection within the report. For example clicking on cell B23 would tell the function to only copy the value from cell B23 but not all the others.         |
| Target        | CustomerOrderHistory!C23 | Once the cell has been copied, this argument specifies the location of the cell or cells that the value will be pasted to.                                                |
| RequireValue  | TRUE | Since this value is true, no blank cell values will be copied. If you wanted to copy blank values you would set this to FALSE|
| ScopeRange    | " "                      | This is blank since when it is not set to a range it enables a user to select a cell within the row range specified in the From argument but not necessarily force them to select a cell within the specific column of "B". For example the Pair() function would copy "B23" if the user selected "Q23". To disable this, input the same range as in the From argument. In this example that would be "B22:B24".|


###  Usable In These Functions   

* [PairGroup()](PairGroup.html)
* [ReportDefaults()](ReportDefaults.html)
* [ReportDrill()](ReportDrill.html)

