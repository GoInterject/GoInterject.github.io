---
title: jAcct()
layout: custom
keywords: [jacct, account, segment, function, formula, chart of accounts]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example"]
links: ["/wIndex/jCell.html"]
description: A helper function that specifies filters for up to six segments of a Chart of Accounts  
---
* * *

##  Function Summary 

A helper function that specifies filters for up to six segments of a Chart of Accounts. 

###  Function Arguments   
  
| Parameter Name | Description                              | Default | Optional |
| -------------- | ---------------------------------------- | ------- | -------- |
| Segment1       | The first segment of a chart of accounts |         | YES*     |
| ...            | ...                                      |         | YES*     |
| Segment6       | The last segment of a chart of accounts  |         | YES*     |

\* Note that segments are optional and defined by each organization's needs. 

###  Excel Formula Bar Example   

```Excel
=jCellN(jAcct("Revenue - Sales",7002),11,2001,Actual)
```

The jAcct function is wrapped in the [jCellN](/wIndex/jCell.html) function to filter which account it will pull.

An example of this function is currently in construction in our documentation labs. Check back soon for an example with more context. However, for a demo report using this feature, visit the **Epicor Demo** in the report Library and open the file **PL Trend - w/ DataCells**.

| Argument Name | Example Mapping   | Explanation                                                   |
| ------------- | ----------------- | ------------------------------------------------------------- |
| Function Name | jAcct()           | The name of the formula                                       |
| Segment 1     | "Revenue - Sales" | The first filter segment. Take only the revenue sales account |
| Segment 2     | 7002              | Filters to a specific location for a more specific account.   |