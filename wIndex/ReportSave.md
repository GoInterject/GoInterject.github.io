---
title: ReportSave()
layout: custom
keywords: [reportsave, function]
description: Used to save data back to data portal with Ctrl + Shift + U keystroke. 
---
* * *

##  Function Summary 

Used to save data back to data portal with Ctrl + Shift + U keystroke. 

###  Function Arguments

| Parameter Name | Description                                                                                                                                                                                | Default | Optional |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | -------- |
| DataPortal     | The name of the INTERJECT Data Portal set up to save data to the Stored Procedure or Web API.                                                                                              |         | NO       |
| RowDefRange    | Specify a range with values for each row to be saved back. If no value is specified, the row will not be sent to the Data Portal. See the exception below for CaptureAllRows.              |         | NO       |
| ColDefRange    | Input field names above the columns used in the XML to send to the data portal for saving. It is recommended special characters are not used when specifying column names to return.       |         | YES      |
| ResultsRange   | Specify a row with column headers that will be used to pull data in response to the save action. ResultsRange is similar to ColDefRange in the ReportRange function.                       |         | YES      |
| Parameters     | Select cells used as Parameters for the Data Portal. The cells must use INTERJECT's [ Param() ](/wIndex/Param.html) function.                                                              |         | YES      |
| AutoSaveFile   | If True, the file will save on each save data action if the action returns error free.                                                                                                     | FALSE   | YES      |
| CaptureAllRows | If True, the save action will not require a value in the RowDefRange to include in the XML package that will be assessed for the save. All rows noted by the RowDefRange will be returned. | FALSE   | YES      |

### Excel Formula Bar Example

```Excel
=ReportSave("NorthwindInvoiceSave",B42:B58,12:12,14:14)
```

To see an example of this function in use, visit the [ Lab Dev: Customer Aging Detail ](/wGetStarted/L-Dev-CustomerAgingDetail.html)

###  Function Composition    

| Argument Name | Example Mapping       | Explanation                                                                                                  |
| ------------- | --------------------- | ------------------------------------------------------------------------------------------------------------ |
| Function Name | =ReportSave()         | The name of the report formula                                                                               |
| DataPortal    | "NorthwindInvoiceSave | The name of a DataPortal that is configured to connect to a Northwind demo database                          |
| RowDefRange   | B42:B58               | The range in which row IDs are stored so the save knows which rows have values to save                       |
| Col Def Range | 12:12                 | The column names specified in this range will determine which data fields are saved to the data source       |
| ResultRange   | 14:14                 | The column names specified in this range will determine which data fields are returned from the data source. |
| Parameters    | N/A                   | Data to filter down the save or to pass more information back to the data source.                            |