---
title: jCombineSmart()
layout: custom
keywords: [jcombine, function, jcombinesmart]
description: The jCombineSmart() function is helpful for developers who want to concatenate the values of cells while simultaneously removing duplicates and skipping any empty cells. 
---
## Function Summary

The jCombineSmart() function is helpful for developers who want to concatenate the values of cells while simultaneously skipping any empty cell and removing any duplicates. jCombineSmart() can use both a cell range and a list of cell addresses. jCombineSmart() can use both a cell range and a list of cell addresses. When using a list of cell addresses the addresses must be enclosed in parenthesis and delimited by a comma e.g. (A1:A5,B1:B20). When a continuous sequence of numbers is found in the selected range then the range code will be used to represent that sequence e.g. (1,2,3) becomes (1..3).By default, the range code is shown with two periods but this is also customizable. Converting to numeric is also a feature for developers to trim any leading zeros from the selected range. This feature is false by default.

### Function Arguments

| Argument Name | Description | Default | Optional |
|----------------|-------------|---------|----------|
|Selected Range |This designates a range of cells from a worksheet that will be concatenated. This can also be used with a delimited list of cells.||NO|
|Delimiter|This defines a character value that will designate a separation between cell values. The default delimiter is a comma.|","|YES|
|Range Code |This defines a character that will designate when a list of cells is concationated into a range.| ".." | YES|
|Convert to Numeric |This will remove any leading zeros within the Selected Range. The results will be reflected when the jCombineSmart() function is executed.|FALSE|YES|

### Excel Formula Bar Example

```Excel
jCombineSmart(A15:A30,,,TRUE)
```
This is a simplified example to show the format you would see in excel. 
### Example Function Composition

| Argument Name | Example Mapping | Explanation |
|---------------|-----------------|-------------|
|Function Name  |=jCombineSmart()    |This is the excel function name used to call the function. It can be used standalone in a report and can be embedded inside of [Data](Data-Functions-Landing.html) or [Formatting](Formatting-Function-Landing.html) functions  |
|Selected Range |(A15:A30)    |In this example we have selected a range of values to look like this: ValueOfA15 though ValueOfA30|
|Delimiter      |""              |The reason for leaving the delimiting value as blank means that jCombineSmart will use its default comma delimiter. To change the delimiter all you need to do is set a delimiting character value. For example ";".|
|Range Code     |""          | Like the delimiter, keeping this blank means jCombineSmart will use its default value of two periods. This can easily be changed by adding a charactor or series of charactors of your choosing.|
|Convert To Numeric |TRUE |Any leading zero will now be trimmed off. For example 0001 will trim to 1.|

### Usable In These Functions

* [Param](Param.html)
* [ReportRange](ReportRange.html) 
* [ReportVariable](ReportVariable.html)
* [ReportFixed](ReportFixed.html)
* [ReportSave](ReportSave.html)
