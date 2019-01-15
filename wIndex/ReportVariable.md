---
title: ReportVariable()
layout: custom
keywords: [reportvariable, function, variable]
description: Directs a list of data into rows that include multiple ranges or sections where each can be subtotaled and formatted to make a financial statement or other report with sub groupings. 
---
* * *

##  Function Summary 
Directs a list of data into rows that include multiple ranges or sections where each can be subtotaled and formatted to make a financial statement or other report with sub groupings. 

###  Function Arguments   

| Parameter Name | Description                                                                             | Default | Optional |
| -------------- | --------------------------------------------------------------------------------------- | ------- | -------- |
| DataPortal     | This is the name of the INTERJECT Data Portal which has been set up to connect to data. |         | NO       |
| RowDefRange    | Select a single column range that has the values referencing the RowDefName field of the data result. Each RowDefName defines a new target range where records matching the value found in the RowDefName will be inserted. It is not required for a returned data set to have a column called **RowDefName** . RowDefRange can look for a different column name if specified in the ColDefRange cell (explained below), which is directly above the RowDefRange column. <br> Explain the **[leftover]** rowdefrange special tag that marks the target range will all records not matching will be presented.             |         | NO       |
| ColDefRange         |The Column Definition Range defining which columns from the database will be used by this function. Unlike the [ ReportRange ](/wIndex/ReportRange.html) function, ColDefRange in ReportFixed can only span a single row. |         | YES      |
| FormatRange         |This Range defines the format (eg. font / color) or formula to be copied down to the TargetDataRange. If left blank, the first row of the TargetDataRange format is applied. When a ColDefRange spans multiple rows, a FormatRange must be used and must match the number of rows selected in the ColDefRange. |         | YES      |
| Parameters          | Select cells which will be used as parameters for the Data Portal. The parameters must be selected in the same order specified in the Data Portal setup. The order can be checked by using the validation report . A [ report builder ](/wPortal/INTERJECT-Ribbon-Menu-Items.html) will also list the parameters correctly to aid new report building. The cells must use INTERJECT's [ Param ](/wIndex/Param.html)() function. |         | YES      |
| UseEntireRow        | If True, INTERJECT will insert a row instead of a range in order to control displace of cells. | FALSE   | YES      |
| RetainRowColumns    |This can either be a string noting the names of the columns in the ColDefRange or a range that points to the ColDefRange items. The noted columns will be considered the key for the inserted row. When using this feature, rows are no longer cleared from the target range, but data are cleared still without deleting rows. The columns noted as **retained** are not cleared, while all other ColDef item columns are cleared. The purpose of this feature is to allow number trends to lead into forecasting calculations. On a data re-pull, it is critical the calculation formulas are not removed, but only data that is shown in the trend columns are updated.  [ See example here. ](/wGetStarted/Creating-a-Simple-Report.html)             |         | YES      |
| InsertNewRowsWithin |If RetainRowColumns are specified, the system will automatically add new rows when the key (represented by the noted columns in RetainRowColumns) is not present in the target data range. These new rows will be added to the bottom of the data range to ensure users' calculated formulas are minimally affected. If InsertNewRowsWithin is true, the new rows will be inserted within the target range based on the alphabetical order of the key. At this time, the ability to further refine the order is not allowed. | FALSE   | YES      |
| UseTopSpacerRow     | For the TargetDataRange, adding a top spacer row inserts the data on the second row of the range and allows the first row to retain it's formatting. This is used in cases where rows are inserted into the range and the user needs to place the row at the top of the target range.             |         | YES      |

###  Function Composition 
    
    
    =ReportVariable(
    				DataPortal
    				,RowDefRange
    				,ColDefRange
    				,FormatRange
    				,Parameters
    				,UseEntireRow
    				,PutFieldNamesAtTop
    				,RetainRowColumns
    				,InsertNewRowsWithin
    				,UseTopSpacerRow
    )

  


###  Function Example   
  
<table>  
<tr>  
<th>

From File 
</th>  
<th>

Worksheet 
</th> </tr>  
<tr>  
<td>

INTERJECTBasic 
</td>  
<td>

ReportVariable 
</td> </tr> </table>
