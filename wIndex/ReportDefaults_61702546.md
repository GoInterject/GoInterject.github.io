---
title: Interject Documentation > ReportDefaults()
layout: custom
---
* * *

##  Function Summary 

Allows the report creator to set specific values for cells based on the Pull and Save events. 

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



Select which events to trigger on: 

  * Pull 
  * Save 
  * Both (Pull and Save) 


</td>  
<td>


</td>  
<td>



YES 


</td> </tr>  
<tr>  
<td>

OnClearRunOrBoth 
</td>  
<td>



Select which actions to trigger on: 

  * Run 
  * Clear 
  * Both (Run and Clear) 


</td>  
<td>


</td>  
<td>

YES 
</td> </tr>  
<tr>  
<td>

TransferPairs  
</td>  
<td>

Use the [ PairGroup() ](/wIndex/81756186.html) function to note which values are placed in the cells.  
</td>  
<td>


</td>  
<td>

YES 
</td> </tr> </table>

###  Function Composition 
    
    
    =ReportRange(
    			OnPullSaveOrBoth
    			,OnClearRunOrBoth
    			,TransferPairs
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

ReportDefaults  
</td> </tr> </table>

=ReportDefaults("Pull","Clear",PairGroup(Pair("Test Input 1",E8),Pair("Test Input 2",E9),Pair("Not a valid date input 3",E10))) 
