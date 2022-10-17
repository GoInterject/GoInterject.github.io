---
title: "jDropdown()"
layout: custom
keywords: [jDropdown, function]
description: The jDropdown formula is used for filtering on multiple parameters at once.
---

## Function Summary

The jDropdown formula helps developers simplify the use of parameters in a data pull or save. It can reduce the rows of data in a report, speeding the report process, sparing server resources, and pulling data more efficiently. 

### Function Arguments

| Argument Name       | Description                                                                                                                                           | Default           | Optional |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | -------- |
| DataPortal          | This is the name of the Interject Data Portal which has been set up to connect to the data                                                            |                   | NO       |
| Parameters          | Select cells to be used as parameters for the Data Portal. Use Interject's [Param()](/wIndex/Param.html) function to specificy the cells used |                   | NO       |
| MultiSelect         | Specify if the dropdown allows for multiple options to be selected                                                                                    | FALSE             | NO       |
| Target Cell         | Specify the Cell location of where the selected options will be set                                                                                   |                   | NO       |
| Value Column Name   | Specify which column to use as the value. The value will be copied to the Target Cell                                                                 |                   | NO       |
| Display Column Name | Specify which column to use as the display text for the options in the dropdown window.                                                               | Value Column Name | YES      |
| Delimiter           | Specify the delimiter to use when MultiSelect is TRUE                                                                                                 | ", "              | YES      |
| Instruction Text    | Specify the help text to display to a user in the dropdown window                                                                                    |                   | YES      |


### Excel Formula Bar Example

```Excel
=jDropdown(jDataPortal("NorthwindCustomersDropdown",1),,FALSE,C17,"CompanyName","DisplayText",,"Select a Customer")
```
The simplified version of this example is sourced from [Lab Create: Parameter Dropdowns](/wGetStarted/L-Create-Dropdowns.html).

### Example Function Composition

| Argument Name       | Example Mapping                             | Explanation                                                                                              |
| ------------------- | ------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Function Name       | =jDropdown()                                | This is the excel function name used to call the function.                                               |
| DataPortal          | jDataPortal("NorthwindCustomersDropdown",1) | Using the [jDataPortal()](/wIndex/jDataPortal.html) function, select the first result in dataportal "NorthwindCustomersDropdown" |
| Parameters          | ""                                          | No Parameters are used.                                                                                  |
| MultiSelect         | FALSE                                       | Only one option is selectable at a time.                                                                 |
| Target Cell         | C17                                         | The cell that will recieve the resulting value.                                                          |
| Value Column Name   | "CompanyName"                               | The value of this column will be returned to the Target Cell.                                            |
| Display Column Name | "DisplayText"                               | When selecting a customer, options will be displayed as this column value.                               |
| Delimiter           | ""                                          | The default delimiter of a ", " is used        .                                                         |
| Instruction Text    | "Select a Customer"                         | Some guidance as to what the user needs to do.                                                           |
