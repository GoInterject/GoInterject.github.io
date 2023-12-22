---
title: jCell/jCellN()
layout: custom
keywords: [jcell, account, segment, function, formula]
description: jCell retrieves data based on the provided parameters. 
---
* * *

##  Function Summary 

jCell retrieves data based on the provided parameters. The first argument is typically a [jAcct()](/wIndex/jAcct.html) lookup when a company has more than one segment to filter. The retrieved data is always summarized into a single value. 

Filter text for up to six segments of a chart of accounts. Use the Interject function [jAcct()](/wIndex/jAcct.html) when more than a single segment is used as a filter. 

###  Function Arguments   

| Parameter Name | Description                                                                                                                                                              | Default | Optional |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | -------- |
| Full Account   | Filter text for up to six segments of a chart of accounts. Use the Interject function [jAcct()](/wIndex/jAcct.html) when more than a single segment is used as a filter. |         | NO       |
| Period         | The month or quarter to filter the retrieved data.                                                                                                                       |         | YES      |
| Year           | The year or range of years to filter the retrieved data.                                                                                                                 |         | YES      |
| Source         | A source filter that may include budget, actual, or forecast, depending on user's system.                                                                                |         | YES      |
| Version        | Filters the retrieved data.                                                                                                                                              |         | YES      |
| Company        | Sub-grouping to retrieve data only from a specific company or district.                                                                                                  |         | YES      |
| Currency       |                                                                                                                                                                          |         | YES      |

### Excel Formula Bar Example  

```Excel
=jCellN(jAcct("Revenue - Sales",7002),11,2001,Actual)
```

An example of this function is currently in construction in our documentation labs. Check back soon for an example with more context. However, for a demo report using this feature, visit the **Epicor Demo** in the report Library and open the file **PL Trend - w/ DataCells**.

###  Function Composition 

| Argument Name | Example Mapping               | Explanation                                                                            |
| ------------- | ----------------------------- | -------------------------------------------------------------------------------------- |
| Function Name | jCellN()                      | The name of the report formula.                                                        |
| Full Account  | jAcct("Revenue - Sales",7002) | Which account the data is accessing based on the [jAcct()](/wIndex/jAcct.html) filter. |
| Period        | 11                            | Accessing the 11th period of that year to filter down further.                         |
| Year          | 2001                          | The year of which the data is from.                                                    |
| Source        | "Actuals"                     | Looking at Actuals specifically from the period and year specified.                    |
| Version       |                               |                                                                                        |
| Company       |                               |                                                                                        |
| Currency      |                               |                                                                                        |