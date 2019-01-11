---
title: jCombineIF()
layout: custom
keywords: [jcombineif, function]
description: jCombineIF() has a similar function to jCombine(). A key difference is that jCombineIF() uses a conditional statement to determine which values should be included into a single concatenated string. 
---

## Function Summary

jCombineIF() has a similar function to [jCombine()](/wIndex/jCombine). A key difference is that jCombineIF() uses a conditional statement to determine which values should be included into a single concatenated string. jCombineIF() requires the cell ranges for both the CriteriaRange and the SelectedRange to be continuous as jCombineIF() does not support non-continuous data ranges.

### Function Arguments

| Parameter Name | Description                                                                                                              | Default | Optional |
|----------------|--------------------------------------------------------------------------------------------------------------------------|---------|----------|
| CriteriaRange  | The criteria range is a range of cells that contain values. These values are used to compare against the criteria value. |         | NO       |
| SelectedRange  | This is the range of cells that are selected to be concatenated into a single string upon the criteria range matching the criteria value.|         | NO       |
| CriteriaValue  | This is a cell value that is used to compare to the values of cells in the criteria range. It is compared using a 'Like' operator. When the criteria value matches a cell value within the criteria range, the selected range value equivalent is concatenated.                         |         | NO       |
| Delimiter      | This defines a character value that will designate a separation between cell values. The default delimiter is a comma.   |         | YES      |

### Excel Formula Bar Example

```Excel
    jCombineIF(J16:O16,J15:O15,TRUE,";")
```
An example of this function is currently in construction in our documentation labs. Check back soon for an example with more context.

### Example Function Composition

| Argument Name | Example Mapping | Explanation |
|---------------|-----------------|-------------|
|Function Name  | `=jCombineIF()`   |This is the excel function name used to call the function. It can be used standalone in a report and can be embedded inside of [Data](Data-Functions-Landing.html) or [Formatting](Formatting-Functions-Landing.html) functions.   |
|CriteriaRange  | J16:O16        |The criteria range is a range of cells with values. When a cell in this range contains the value "TRUE" it is therefore matched to the criteria value of "TRUE". In this instance, the values of the cells in the selected range are concatenated into a single string value. |
|SelectedRange  | J15:O15        |This is the range of cells that will be concatenated upon a match between the criteria range and the criteria value.|
|CriteriaValue  | TRUE           | This is the value that is used to match to the Criteria range. When matched to the Criteria Range, jCombineIF will concatenate the associated selected range values. |
|Delimeter      | ";"            |This uses ";" as a delimiter between values in the concatenated string value. In this case it would look like this "ValueJ15;ValueK15;ValueL15;ValueM15;ValueN15;ValueO15".|

### Usable In These Report Formulas 

* [Param](Param.html)
* [ReportRange](ReportRange.html) 
* [ReportVariable](ReportVariable.html)
* [ReportFixed](ReportFixed.html)
* [ReportSave](ReportSave.html)