---
title: jCombineSmart()
layout: custom
keywords: [jcombine, function, jcombinesmart]
description: The jCombineSmart() function is helpful for developers who want to concatenate the values of cells while simultaneously removing duplicates and skipping any empty cells. 
---
## Function Summary

The jCombineSmart() function helps to concatenate the values of cells while simultaneously skipping any empty cells and removing any duplicates. jCombineSmart() can use both a cell range and a list of cell addresses. When using a list of cell addresses, they must be enclosed in parenthesis and delimited by commas, e.g. (A1:A5,B1:B20). When a continuous sequence of numbers is found in the selected range, only the first an last numbers in the sequence will be shown, and the middle values will be truncated to two periods, e.g. (1,2,3,4,5) becomes (1..5). This range code is set by default but may be customized by develpers. Converting to numeric is also a feature available for developers to trim any leading zeros from the selected range. This feature is false by default.

### Function Arguments

| Argument Name | Description | Default | Optional |
|----------------|-------------|---------|----------|
|Selected Range |Designates a range of cells, within a worksheet, to concatenate. This can also be used with a delimited list of cells.||NO|
|Delimiter|Defines the character value to designate a separation between cell values. A comma is the default delimiter.|","|YES|
|Range Code |Defines the characters to designate when a list of cells is concatenated into a range.| ".." | YES|
|Convert to Numeric |This will remove any leading zeros within the Selected Range. Executing the jCombineSmart() function wil will reflect the results of this feature.|FALSE|YES|

### Excel Formula Bar Example

```Excel
jCombineSmart(A15:A30,,,TRUE)
```
This is a simplified example to show the format you would see in Excel. 
### Example Function Composition

| Argument Name | Example Mapping | Explanation |
|---------------|-----------------|-------------|
|Function Name  |=jCombineSmart()    |The Excel function name used to call the function. It can be used alone in a report and can be embedded inside of [Data](Data-Functions-Landing.html) or [Formatting](Formatting-Function-Landing.html) functions  |
|Selected Range |(A15:A30)    |In this example a range of values would look like this: ValueOfA15 through ValueOfA30|
|Delimiter      |""              |Leaving the delimiting value blank means that jCombineSmart will use its default comma delimiter. Set a delimiting character value by entering a character into the function after the range value. For example, ";".|
|Range Code     |""          | Like the delimiter, keeping this blank means jCombineSmart will use its default value of two periods. Change it by adding a charactor or series of charactors of your choosing.|
|Convert To Numeric |TRUE |Any leading zero will now be trimmed off. For example 0001 will trim to 1.|

### Usable In These Functions

* [Param](Param.html)
* [ReportRange](ReportRange.html) 
* [ReportVariable](ReportVariable.html)
* [ReportFixed](ReportFixed.html)
* [ReportSave](ReportSave.html)
