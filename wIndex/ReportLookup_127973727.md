---
title: Interject Documentation > ReportLookup()
layout: custom
keywords: [reportlookup, function]
description: Allows the report creator to insert a specific data value into a cell based on certain criteria. 
---
* * *

##  Function Summary 

Allows the report creator to insert a specific data value into a cell based on certain criteria. Most INTERJECT report functions import a list of data, but this function allows users to choose a specific data column and row and place that data point in a cell. 

Used in conjunction with the [ jDataPortal() ](/wIndex/61702544.html) helper function, ReportLookup() can access DataPortal data still in the memory from report functions that have already returned data, so there are no additional connections to the data source. 

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



DataPortal 


</td>  
<td>

The name of the INTERJECT Data Portal set up to connect to data. 
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



Select a single cell to place the data value. If the DataPortal returns a list of data, this function will return the value from the first row. The helper function [ jDataPortal() ](/wIndex/61702544.html) can be used to further define which row to use from the DataPortal. 


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

The Column Definition Range defines which column from the database will be used. 
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

Select cells which will be used as Parameters for the Data Portal. The cells must use INTERJECT's [ Param ](/wIndex/81756199.html) () function. 
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



=ReportLookup( 

DataPortal 

,TargetDataRange 

,ColDefRange 

,Parameters 

) 


</td>  
<td>



=ReportLookup( 

<b>"NorthwindFixed"</b>
,  <b>B9</b>
,  <b>C1</b>
, 
) 


</td>  
<td>


</td> </tr> </table>
