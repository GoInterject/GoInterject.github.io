---
title: ReportRange()
layout: custom
keywords: [ReportRange, function]
description: The ReportRange function pulls data from a data source and inserts it into a single range within a spreadsheet.
---

##  Function Summary
The ReportRange function pulls data from a data source and inserts it into a single range within a spreadsheet. Receives a list of columns for input that will be pulled from the data source. Only data that is mapped to these column names will be inserted. Data returned by this function can be filtered, formatted, and customized for a specific desired data set.

For an example of this function, see [ Lab Create: Customer Aging ](/wGetStarted/L-Create-CustomerAging.html).

###  Function Arguments

| Parameter Name  |  Description  |  Type   |  Constraints  |  If Blank  |
|------|------|------|------|------|
|  DataPortal  |  The name of the Interject DataPortal that will be used as the data source for this function.  |  String/[jDataPortal()](/wIndex/jDataPortal.html)  |  Max 255 char  |  Function Error  |
|  TargetDataRange  |  The range where the data will be inserted. Data is inserted starting at the first row. The last row defined here will be the bottom row below the data.  |  Range  |  Min 2 rows. Must match the width of the range defined in ColDefRange  |  No data inserted  |
|  ColDefRange  |  The range designating the names of the columns of the data source. Only data from these columns will be inserted. Range can span multiple rows. Best practice is to use a range instead of whole rows.  |  Range  |  Max 500 columns. Must match the width of the range defined in TargetDataRange  |  Uses all columns from the data source  |
|  FormatRange  |  The range designating the formatting style (e.g. font, color) for the inserted data. Inserted data will be formated using this range as a template. Formulas can also be included, which will be used for the inserted data.  |  Range  |  Must match the range dimensions defined in ColDefRange  |  Uses the formatting in the first row defined in TargetDataRange  |
|  Parameters  |  The cells designating the parameters for the DataPortal. The values in these cells will filter the data that is inserted from the data source.  |  [ Param() ](Param.html)  |  The values must match the order of the parameters in the data source (The order can be verified using the [ Validation Report ](/wTroubleshoot/Reports.html#validation-report-for-pullsave-events) )  |  Data is not filtered  |
|  UseEntireRow  |  True: New rows will be added for the inserted data. Every row besides the bottom row defined in TargetDataRange will be deleted first.<br/><br/>False: Data will be inserted into the range defined in TargetDataRange. All other cells outside this range will be unaffected.  |  Boolean  |    |  False  |
|  PutFieldNamesAtTop  |  True: Will insert the column names on a row above the inserted data if ColDefRange is blank.<br/><br/>False: Will not insert column names.  |  Boolean  |    |  False  |
|  RetainRowColumns  |  The list of column names that will be used as a key for retaining information within the inserted data range. This can be a comma delimited string or a cell reference of a single column name defined in ColDefRange. <br/><br/>All data in the column(s) matching the names in this argument will be retained after a clear or pull action. Consequently, such rows are also retained and not deleted. However, all data in columns that are not defined in this argument are blanked out after a clear action or overridden after a pull action.<br/><br/>This feature makes forecasting calculations to remain in the report instead of being cleared. For an example of this feature, see [Using the Retain Feature ](/wGetStarted/L-Create-RetainFeature.html).  |  String/[ jCombine() ](jCombine.html)/[ jCombineIF() ](jCombine_IF.html)  |  Max 255 char  |  All data within the TargetDataRange is cleared on a clear action  |
|  InsertNewRowsWithin  |  True: If RetainRowsColumns is used, will insert new data in the TargetDataRange on a pull action by alphabetical order of the first key listed in RetainRowColumns. <br/><br/>False: Will insert new data below the already present data in the TargetDataRange on a pull action if valid columns are defined in RetainRowColumns.  |  Boolean  |    |  False  |
|  UseTopSpacerRow  |  True: Inserts data starting on the second row defined in TargetDataRange. (Retains top row on a pull or clear action.)<br/><br/>False: Inserts data starting on the first row defined in TargetDataRange.  |  Boolean  |    |  False  |

###  Excel Formula Bar Example

```Excel
=ReportRange("NorthwindCustomers",B14:H15,B2:H2,B4:H4,Param(C7,C8,C9),FALSE,FALSE,,FALSE,FALSE)
```



###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =ReportRange()  |  The name of this function.  |  
|  DataPortal  |  "NorthwindCustomers"  |  This function will use the "NorthwindCustomers" DataPortal for the data source.  |  
|  TargetDataRange  |  B14:H15  |  Data will be inserted starting at row 14 and only extend from column B to column H.  |  
|  ColDefRange  |  B2:H2  |  The column names specified in B2:H2 will determine which data fields are returned from the data source.  |  
|  FormatRange  |  B4:H4  |  The formatting used in this range will be used as a template for the inserted data.  |  
|  Parameters  |  Param(C7,C8,C9)  |  Cells C7, C8, and C9 will correspond to the parameters in the data source to filter the inserted data.  |  
|  UseEntireRow  |  FALSE  |  Interject will insert a range into the sheet and will not insert full rows.  |  
|  PutFieldNamesAtTop  |  FALSE  |  The inserted data will not contain a row of the column names above the data.  |  
|  RetainRowColumns  |  ""  |  Left blank to indicate not to retain any data in the TargetDataRange (B14:H15).  |  
|  InsertNewRowsWithin  |  FALSE  |  This value is automatically set to false since RetainRowColumns is blank.  |  
|  UseTopSpacerRow  |  FALSE  |  Data will be inserted on the first row (14) defined in TargetDataRange.  |  

###  Embeddable Helper Functions

* [jDataPortal](/wIndex/jDataPortal.html)
* [ Param ](Param.html)
* [jCombine](/wIndex/jCombine.html)
* [jCombineIF](/wIndex/jCombine_IF.html)
