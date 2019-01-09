---
title: Interject Documentation > ReportSave()
layout: custom
keywords: [reportsave, function]
description: Used to save data back to data portal with Ctrl + Shift + U keystroke. 
---
* * *

##  Function Summary 

Used to save data back to data portal with Ctrl + Shift + U keystroke. 

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

The name of the INTERJECT Data Portal set up to save data to the Stored Procedure or Web API. 
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

Specify a range with values for each row to be saved back. If no value is specified, the row will not be sent to the Data Portal. See the exception below for CaptureAllRows.. 
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

Input field names above the columns used in the XML to send to the data portal for saving. It is recommended special characters are not used when specifying column names to return. 
</td>  
<td>


</td>  
<td>



YES 


</td> </tr>  
<tr>  
<td>

ResultsRange 
</td>  
<td>

Specify a row with column headers that will be used to pull data in response to the save action. ResultsRange is similar to ColDefRange in the ReportRange function. 
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

Select cells used as Parameters for the Data Portal. The cells must use INTERJECT's [ Param ](/wIndex/81756199.html)() function. 
</td>  
<td>


</td>  
<td>

YES 
</td> </tr>  
<tr>  
<td>

AutoSaveFile 
</td>  
<td>

If True, the file will save on each Save Data action if the action returns error-free. 
</td>  
<td>

FALSE 
</td>  
<td>

YES 
</td> </tr>  
<tr>  
<td>

CaptureAllRows 
</td>  
<td>

If True, the save action will not require a value in the RowDefRange to include in the XML package that will be assessed for the save. All rows noted by the RowDefRange will be returned. 
</td>  
<td>

FALSE 
</td>  
<td>

YES 
</td> </tr> </table>

  * Note: the save process works by: ____________ 



###  Function Composition 
    
    
    =PairGroup(
    			DataPortal
    			,RowDefRange
    			,ColDefRange
    			,ResultsRange
    			,Parameters
    			,AutoSaveFile
    			,CaptureAllRows
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

ReportSave 
</td> </tr> </table>

`=ReportSave("NorthwindCustomersSaveCRMandNotes",B15:B17,B2:K2,H3:K3)`
