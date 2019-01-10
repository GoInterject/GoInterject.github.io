---
title: ReportRun()
layout: custom
keywords: [reportrun, function]
description: ReportRun executes a Report Function in another tab without changing the tab focus. 
---

##  Function Summary 

ReportRun executes a Report Function in another tab without changing the tab focus. It can handle both run and clear events. 

**  
**

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



ReportCellToRun 


</td>  
<td>

A range within the target worksheet to run a report function.  
</td>  
<td>

  

</td>  
<td>



NO 


</td> </tr>  
<tr>  
<td>

RunEntireWorksheet  
</td>  
<td>

A boolean toggle that will enable or disable an entire Worksheet’s Report Functions from running. (CLEAN UP LANGUAGE / CLARIFY HOW TO USE)  
</td>  
<td>

TRUE 
</td>  
<td>

YES 
</td> </tr>  
<tr>  
<td>

OnAction  
</td>  
<td>



A control for which type of Report Function to run. Options include: 

  * ‘Pull’ 
  * ‘Save’ 
  * 'PullAndSave’ 
  * ‘PullClear’ 
  * ‘SaveClear’ 
  * ‘PullAndSaveClear’ 
  * 'Back’ 


</td>  
<td>

PULL 
</td>  
<td>

YES 
</td> </tr> </table>

  


###  Function Composition 

=ReportRun( 

ReportCellToRun 

,RunEntireWorksheet 

,OnAction 

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

InterjectBasic  
</td>  
<td>

ReportRun  
</td> </tr> </table>

=ReportRun(ReportRunTarget!C2,TRUE,"Pull") 
