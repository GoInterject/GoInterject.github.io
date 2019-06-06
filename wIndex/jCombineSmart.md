---
title: jCombineSmart()
layout: custom
keywords: [jcombine, function, jcombinesmart]
description: The jCombineSmart() function is helpful for developers who want to concatenate the values of cells while simultaneously removing duplicates and skipping any empty cells. 
---
## Function Summary

The jCombineSmart() function is helpful for developers who want to concatenate the values of cells while simultaneously skipping any empty cell and removing any duplicate cells. jCombineSmart()can use both a cell range and a list of cell addresses. A list of cell addresses will require a delimiting character between each cell address in the list. The delimiter character can be custom, but it is a comma by default. When using jCombineSmart() in a list of ranges that are not continuous it needs to have a second pair of parentheses around the first set. When concationated numbers have been formated into a range we use a range code to indicate it. Also custom, this is two periods by default. Converting to numearic is also a feature for developers to trim any leading zeros from the selected range. This feature is false by default. 

### Function Arguments

| Argument Name | Description | Default | Optional |
|----------------|-------------|---------|----------|
|Selected Range |This designates a range of cells from a worksheet that will be concatenated. This can also be used with a delimited list of cells.||NO|
|Delimeter|This defines a character value that will designate a separation between cell values. The default delimiter is a comma.|","|NO|
|Range Code |This defines a characot that will designate when a list of cells is concationated into a range.| ".." | NO|
|Convert to Numeric |This will remove any leading zeros within the Selected Range. The results will be reflected when the jCombineSmart() function is executed.|FALSE|YES|

### Excel Formula Bar Example

```Excel
jCombineSmart(A15:A30,,,TRUE)
```
The simplified example created to show the format that you would see in excel. 
### Example Function Composition

| Argument Name | Example Mapping | Explanation |
|---------------|-----------------|-------------|
|Function Name  |=jCombineSmart()    |This is the excel function name used to call the function. It can be used standalone in a report and can be embedded inside of [Data](Data-Functions-Landing.html) or [Formatting](Formatting-Function-Landing.html) functions  |
|Selected Range |(A15:A30)    |In this example we have selected a range of values to look like this: ValueOfA15 though ValueOfA30|
|Delimeter      |" "              |The reason for leaving the delimiting value as blank means that jCombineSmart will use its default comma delimiter. To change the delimiter all you need to do is set a delimiting character value. For example ";".|
|Range Code     |" "          | Like the delimiter, keeping this blank means jCombineSmart will use its default value of two periods. This can easily be changed by adding a charactor or series of charactors of your choosing.'|
|Convert To Numeric |TRUE |Any leading zero will now be trimmed off the value. For example 0001 will trim to 1.|

### Usable In These Functions

* [Param](Param.html)
* [ReportRange](ReportRange.html) 
* [ReportVariable](ReportVariable.html)
* [ReportFixed](ReportFixed.html)
* [ReportSave](ReportSave.html)
