---
title: Param()
layout: custom
keywords: [param, function]
description: Param is used to help select one or multiple parameters for each of your report formulas. 
 
---
##  Function Summary 

Param is used to help select one or multiple parameters for each of your report formulas 

NOTE - One value to one cell. But can go one to many. In second case will return XML of entire thing. 

###  Function Arguments   

| Parameter Name | Description                    | Default | Optional |
| -------------- | ------------------------------ | ------- | -------- |
| Value1         | Enter parameter value or link. |         | YES      |
| ...            | ...                            |         | ...      |
| Value40        | Enter parameter value or link. |         | YES      |


### Excel Formula Bar Example
```Excel
=ReportRange("NorthwindCustomers",B14:H15,B2:H2,B4:H4,Param(C7,C8,C9),FALSE,FALSE,,FALSE,FALSE)
```
To see an example of this function in use, visit the [Lab Create: Customer Aging](/wGetStarted/L-Create-CustomerAging.html)

###  Function Composition   

| Argument Name | Example Mapping | Explanation                                                             |
| ------------- | --------------- | ----------------------------------------------------------------------- |
| Function Name | Param()         | Inside the ReportRange, call the param function to call multiple cells  |
| Value1        | C7              | the value in C7 will be passed through as a parameter to the dataportal |
| Value2        | C8              | the value in C8 will be passed through as a parameter to the dataportal |
| Value3        | C9              | the value in C9 will be passed through as a parameter to the dataportal |
