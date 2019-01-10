---
title: ReportMacro()
layout: custom
keywords: [reportmacro, function]
description: ReportMacro allows a report developer to call VBA macros on Save, Pull, Clear, or Run events. 
---
* * *

##  Function Summary 
ReportMacro allows a report developer to call VBA macros on Save, Pull, Clear, or Run events. The VBA macro must be a named Sub in the workbook. This function will ignore all errors during the macro's execution. 

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



OnPullSaveOrBoth 


</td>  
<td>

Events will be triggered on "Pull", "Save," or both. This parameter accepts a string. 
</td>  
<td>


</td>  
<td>



NO 


</td> </tr>  
<tr>  
<td>

OnClearRun  OrBoth  
</td>  
<td>

Events will be triggered on "Clear", "Run," or both. This parameter accepts a string.  
</td>  
<td>


</td>  
<td>

NO  
</td> </tr>  
<tr>  
<td>

MacroNameToRun  
</td>  
<td>



The macro Sub name that will be executed. The placement of this function determines when it is run in comparison to other Report formulas. 


</td>  
<td>


</td>  
<td>

NO  
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



=ReportMacro( 

OnPullSaveOrBoth 

,OnClearRun  OrBoth 

,MacroNameToRun 

) 


</td>  
<td>



=ReportMacro( 

<b>"Pull"</b>

,  <b>"Both"</b>

, <b>"MyVBAMacro"</b>

) 


</td>  
<td>



← The VBA macro will run on the Pull data event. 

← The VBA macro will run on both Clear and Run events. 

← The VBA macro to run from workbook storage. All errors will be ignored. 


</td> </tr> </table>

###  Example from   
  
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


</td> </tr> </table>
