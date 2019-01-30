---
title: jAcct()
layout: custom
keywords: [jacct, function, chart of accounts]
description: A helper function that specifies filters for up to six segments of a Chart of Accounts  
---
##  Function Summary 

A helper function that specifies filters for up to six segments of a Chart of Accounts. 

###  Function Arguments   
  
| Parameter Name | Description                              | Default | Optional |
|----------------|------------------------------------------|---------|----------|
| Segment1       | The first segment of a chart of accounts |         | YES*     |
| ...            | ...                                      |         | YES*     |
| Segment6       | The last segment of a chart of accounts  |         | YES*     |

* Note that segments are optional and defined by each organization's needs. 

###  Excel Formula Bar Example   

```Excel
=jCellN(jAcct("Revenue - Sales",7002),11,2001,Actual)
```

An example of this function is currently in construction in our documentation labs. Check back soon for an example with more context. However, for a demo report using this feature, visit the **Epicor Demo** in the report Library and open the file **PL Trend - w/ DataCells**.

