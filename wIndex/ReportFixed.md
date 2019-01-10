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



DataPortal 


</td>  
<td>

The name of the Interject Data Portal which has been set up to connect to data. 
</td>  
<td>

  

</td>  
<td>



NO 


</td> </tr>  
<tr>  
<td>

RowDefRange 
</td>  
<td>



Select a single column range that has the values that compare to the RowDefName field of the data result. Each RowDefName defines a new target range where the records 

that match the value found in the RowDefName will be inserted. It is not required for a returned dataset to have a column called RowDefName. RowDefRange can look for a different column name if specified in the ColDefRange cell (explained below), which is directly above the RowDefRange column. 

Explain the **[leftover]** rowdefrange special tag that marks the target range will all records not matching will be presented. 


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

The Column Definition Range defining which columns from the database will be used by this function. Unlike the [ ReportRange ](/wIndex/ReportRange.html) function, ColDefRange in ReportFixed can only span a single row. 
</td>  
<td>

  

</td>  
<td>

NO  
</td> </tr>  
<tr>  
<td>

Parameters 
</td>  
<td>

Select cells which will be used as Parameters for the Data Portal. The cells must use Interject's [ Param ](/wIndex/Param.html) () function. 
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



=ReportFixed( 

DataPortal 

,RowDefRange 

,ColDefRange 

,Parameters 

) 


</td>  
<td>



=ReportFixed( 
<b>"NorthwindFixed"</b>
,  <b>B9</b> :  <b>B21</b>
,  <b>1</b> :  <b>1</b>
, 
) 


</td>  
<td>

  

</td> </tr> </table>

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

InterjectBasic 
</td>  
<td>

ReportFixed 
</td> </tr> </table>
