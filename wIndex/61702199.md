---
title: Interject Documentation > ReportRange()
layout: custom
---
##  Function Summary 

Directs data into a single range of a spreadsheet with options for formatting, formulas, and columns.  ReportRange() is designed to populate a specific area in a spreadsheet with a list of data returned from the dataportal. 

###  Function Arguments   
  
<table>  
<tr>  
<th>

Parameter Name 
</th>  
<th>

Description 
</th>  
<th>

Default 
</th>  
<th>

Optional 
</th> </tr>  
<tr>  
<td>

Dataportal 
</td>  
<td>

This is the name of the Interject Dataportal which has been set up to connect to data.  
</td>  
<td>

  

</td>  
<td>



NO 


</td> </tr>  
<tr>  
<td>

TargetDataRange 
</td>  
<td>

Designate the range to place the data on the worksheet. It must include at least two rows. Fetched rows are inserted in between.  
</td>  
<td>

  

</td>  
<td>

NO 
</td> </tr>  
<tr>  
<td>

ColDefRange  
</td>  
<td>

Column Definition Range defines which columns from the database will be used. It can span multiple rows. Best practice is to avoid selecting entire row because it reduces column quantity and conserves memory usage. The maximum number of columns is three hundred.  
</td>  
<td>

  

</td>  
<td>

YES 
</td> </tr>  
<tr>  
<td>

FormatRange  
</td>  
<td>

This Range defines the format (eg. font / color) or formula to be copied down to the TargetDataRange. If left blank, the first row of the TargetDataRange format is applied.When a ColDefRange spans multiple rows, a FormatRange must be used and must match the number of rows selected in the ColDefRange.  
</td>  
<td>

  

</td>  
<td>

YES 
</td> </tr>  
<tr>  
<td>

Parameters  
</td>  
<td>

Select cells which will be used as parameters for the Data Portal. The parameters must be selected in the same order as they are specified in the Data Portal setup. The order can be checked by using the [ validation report ](/wPortal/INTERJECT-Ribbon-Menu-Items_83689479.html) . A [ report builder ](/wIndex/61702199.html) will also list the parameters correctly to help jump start building a new report. The cells must use Interject’s [ Param ](/wIndex/81756199.html) () function .  
</td>  
<td>

  

</td>  
<td>

YES 
</td> </tr>  
<tr>  
<td>

UseEntireRow  
</td>  
<td>

If True, Interject will insert a row instead of a range in order to control displace of cells. 
</td>  
<td>

FALSE 
</td>  
<td>

YES 
</td> </tr>  
<tr>  
<td>

PutFieldNamesAtTop 
</td>  
<td>

If the column headers are unknown, this can be used to insert them as the first row. This will only function if ColDefRange is not defined. 
</td>  
<td>

  

</td>  
<td>

YES 
</td> </tr>  
<tr>  
<td>

RetainRowColumns 
</td>  
<td>

This can either be a string noting the names of the columns in the ColDefRange or a range that points to the ColDefRange items. The noted columns will be considered the key for the inserted row. When using this feature rows are no longer cleared from the target range. But data is cleared still without deleting the rows. The columns noted as **retained** are not cleared and all other ColDefItems columns are cleared. The purpose of this feature is to allow a trend of numbers to lead into calculations for forecasting. On a repull of data, it is critical the calculation formulas are not removed, but only data that is shown in the trend columns are updated. [ See example here ](/wGetStarted/Creating-a-Simple-Report_128408585.html) . 
</td>  
<td>

  

</td>  
<td>

YES 
</td> </tr>  
<tr>  
<td>

InsertNewRowsWithin 
</td>  
<td>

Defaulted to false. If RetainRowColumns are specified, the system will automatically add new rows when the key (represented by the noted columns in RetainRowColumns) is not present in the target data range. These new rows will be added to the bottom of the data range to ensure the users calculated formulas are minimally affected. If InsertNewRowsWithin is true, the new rows will be inserted within the target range based on the alphabatical order of the key. At this time, the ability to further refine the order is not allowed. 
</td>  
<td>

FALSE 
</td>  
<td>

YES 
</td> </tr>  
<tr>  
<td>

UseTopSpacerRow 
</td>  
<td>

For the TargetDataRange, adding a top spacer row inserts the data on the second row of the range and allows the first row to retain its formatting. This is used in cases where rows are inserted into the range and the user needs the ability to place the row at the top of the target range. 
</td>  
<td>

  

</td>  
<td>

YES 
</td> </tr> </table>

  


###  Function Composition   
  
<table>  
<tr>  
<th>

Formula 
</th>  
<th>

Example 
</th>  
<th>

Explanation 
</th> </tr>  
<tr>  
<td>



=ReportRang( 

DataPortal 

TargetDataRange 

ColDefRange 

FormatRange 

Parameters 

UseEntireRow 

PutFieldNamesAtTop 

RetainRowColumns 

InsertNewRowsWithin 

UseTopSpacerRow 


</td>  
<td>



=ReportRange( 

** "NorthwindCustomers"  **

** 12  :  13  **

** 1  :  1  **

Param **( C6  ,  C7  ,  C8  ) **

**TRUE**

**FALSE)**


</td>  
<td>



  
← A DataPortal configured to connect to a Northwind demo database 

← Data will be inserted between rows 12 and 13 

← The columns specified in that range will define what fields are returned 

← First row of target data range will be used to format incoming data since this field is blank 

← Cells C6 to C8 will be passed in order to the data portal to help filter data 

← Entire rows will be displaced when inserting data 

← The names of columns will not be added as the first row of data 

← Optional field. Left Blank 

← Optional field. Left Blank 

← Optional field. Left Blank 


</td> </tr> </table>

###  Example from:   
  
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

InterjectBasic  
</td>  
<td>

ReportRange  
</td> </tr> </table>

  


  


  

