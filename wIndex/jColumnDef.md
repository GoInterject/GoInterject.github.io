---
title: jColumnDef()
layout: custom
keywords: [jcolumndef, function]
description: This function assists financial reports using the FinCube DataPortal to specify segment filters for each amount column. 
---
* * *

##  Function Summary 

This function assists financial reports using the FinCube DataPortal to specify segment filters for each amount column. See the the [ FinCube ](/wIndex/FinCube---The-Financial-Cube.html) page for an explanation of this function and how each argument can use filters. The following arguments represent the same segments used within the FinCube DataPortal. 

###  Function Arguments   

| Parameter Name | Segment Reference | Description                                                           | Default | Optional |
| -------------- | ----------------- | --------------------------------------------------------------------- | ------- | -------- |
| Source         | Segment12         | Input is typically "Actual," "Budget," or forecast codes like "Fcast1" through "Fcast12." In some configurations, codes can be combined to include unposted and staged monthly numbers (actuals will only include posted entries). <br> <br> To see unposted in addition to posted entries, combine the two: "Actual,Unposted". If staged entries are configured in the INTERJECT installation, use "Actual,Unposted,Staged". |         | YES      |
| Period         | Segment9          | Month 1 through 12. For year to date amounts, use YTD1 through YTD12. |         | YES      |
| Year           | Segment10         | Year                                                                  |         | YES      |
| Version        | Segment11         | If configured, this can filter data to specific versions.             |         | YES      |
| Segment1       | Same              | Configurable segment. Account may be a common example.                |         | YES      |
| Segment2       | Same              | Configurable segment. District may be a common example.               |         | YES      |
| Segment3       | Same              | Configurable segment. Line of Business may be a common example.       |         | YES      |
| Segment4       | Same              | Configurable segment.                                                 |         | YES      |
| Segment5       | Same              | Configurable segment.                                                 |         | YES      |
| Segment6       | Same              | Configurable segment.                                                 |         | YES      |
| Segment7       | Same              | Configurable segment. Currency may be a common example.               |         | YES      |
| Segment8       | Same              | Configurable segment. Company may be a common example.                |         | YES      |

### Excel Formula Bar Example

```Excel
jColumnDef(Actual,11,2001,,,,,)
```

To see an example of this function in use, visit the [Lab Create: Financial Variable ](/wGetStarted/L-Create-FinancialVariable.html)

###  Function Composition   

| Formula  | Example  | Explanation                                                                                   |
| -------- | -------- | --------------------------------------------------------------------------------------------- |
| Source   | "Actual" | Where the data comes from. In this case it is actuals but it could be budgets or projections. |
| Period   | 11       | The period of which the data is from.                                                         |
| Year     | 2001     | The year of which the data is from.                                                           |
| Version  |          |                                                                                               |
| Segment1 |          |                                                                                               |
| Segment2 |          |                                                                                               |
| Segment3 |          |                                                                                               |
| Segment4 |          |                                                                                               |
| Segment5 |          |                                                                                               |
| Segment6 |          |                                                                                               |
| Segment7 |          |                                                                                               |
| Segment8 |          |                                                                                               |
