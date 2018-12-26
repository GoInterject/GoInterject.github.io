---
title: ReportLookup()
layout: custom
---


##  Function Summary 

Allows the report creator to insert a specific data value into a cell based on certain criteria. Most INTERJECT report functions import a list of data, but this function allows users to choose a specific data column and row and place that data point in a cell. 

Used in conjunction with the [ jDataPortal() ](/wIndex/jDataPortal_61702544.html) helper function, ReportLookup() can access DataPortal data still in the memory from report functions that have already returned data, so there are no additional connections to the data source. 

### Function Arguments

| Argument Name   | Description                                                      | Default | Optional |
|-----------------|------------------------------------------------------------------|---------|----------|
| DataPortal      | The name of the INTERJECT Data Portal set up to connect to data. |         | NO       |
| TargetDataRange | Select a single cell to place the data value. If the Data Portal returns a list of data, this function will return the value from the first row. The helper function [jDataPortal()](/wIndex/jDataPortal_61702544.html) can be used to further define which row to use from the Data Portal by using its Filter and OrderBy arguments.                                                                 |         | NO       |
| ColDefRange     | The Column Definition Range determines which column from the stored procedure record will be returned.                                                                  |         | NO       |
| Parameters      |  Select a single cell or range of cells which will be used as [Parameters]() for the Data Portal. The cells must be wrapped inside of INTERJECT's [Param]() helper function.                                                                |         | YES      |

### Excel Formula Bar Example

```Excel
ReportLookup(jDataPortal("NorthwindCustomers",1,"[CustomerID] Like '%SAVE%'"),C14,H1)
```

### Example Function Composition

| Argument Name  | Example Mapping   | Explanation                                                                                |
|----------------|-------------------|--------------------------------------------------------------------------------------------|
| Function Name  | `=ReportLookup()` | This is the excel function name used to call the function. It can have embedded functions. |
| DataPortal     | "jDataPortal("NorthwindCustomers",1,"[CustomerID] Like '%SAVE%')"|                                                                                            |
| TargetDataRange|                   |                                                                                            |
| ColDefRange    |                   |                                                                                            |
| Parameters     |                   |                                                                                            |

### Embeddable Helper Functions

* [jDataPortal](/wIndex/jDataPortal_61702544.html)
* [Param]()
* [jCombine]()
* [jCombineIF]()
*   

