---
title: ReportFixed()
layout: custom
keywords: [reportfixed, function]
description: Allows the report creator to insert data based on a coordinate match between a row marker and a column marker.  
---
* * *

##  Function Summary 

Allows the report creator to insert data based on a coordinate match between a row marker and a column marker. For examples and discussion, view the tutorial. 

###  Function Arguments:   

| Parameter Name | Description                                                                     | Default | Optional |
| -------------- | ------------------------------------------------------------------------------- | ------- | -------- |
| DataPortal     | The name of the Interject Data Portal which has been set up to connect to data. |         | NO       |
| RowDefRange | Select a single column range that has the values that compare to the RowDefName field of the data result. Each RowDefName defines a new target range where the records that match the value found in the RowDefName will be inserted. It is not required for a returned dataset to have a column called RowDefName. RowDefRange can look for a different column name if specified in the ColDefRange cell (explained below), which is directly above the RowDefRange column. <br> There is also a **\[leftover\]** section in most reports that all records that don't match a rowdef category are pull to. | | NO |
| ColDefRange | The Column Definition Range defining which columns from the database will be used by this function. Unlike the [ ReportRange() ](/wIndex/ReportRange.html) function, ColDefRange in ReportFixed can only span a single row. | | NO |
| Parameters | Select cells which will be used as Parameters for the Data Portal. The cells must use Interject's [ Param() ](/wIndex/Param.html) function. | | YES |

### Excel Formula Bar Example
```Excel
=ReportFixed("NorthwindFixed",B14:B27,2:2)
```

To see an example of this function in use, visit the [Create Inventory Fixed Lab.](/wGetStarted/L-Create-InventoryFixed.html)

###  Function Composition   
  | Argument Name | Example Mapping  | Explanation                                                                                                 |
  | ------------- | ---------------- | ----------------------------------------------------------------------------------------------------------- |
  | Function Name | =ReportFixed()   | The name of the report formula                                                                              |
  | DataPortal    | "NorthwindFixed" | The name of a DataPortal that is configured to connect to a Northwind demo database                         |
  | RowDefRange   | B14:B27          | Data will be inserted on the specified rows under the ColDefRange (Explained below)                |
  | ColDefRange   | 2:2              | The column names specified in this range will determine which data fields are returned from the data source |
  | Parameters    | N/A              | Used to specify what information to pass to or from the DataPortal.                               |
