---
title: Interject Documentation > jFreezePanes()
layout: custom
---
###    


###  Function Summary 

Addition to the quick tools menu that allows for quick freezing and unfreezing of sheets.   
  
<table>  
<tr>  
<td>



Parameter Name 


</td>  
<td>



Description 


</td>  
<td>



Default 


</td>  
<td>



Optional 


</td> </tr>  
<tr>  
<td>



FreezePanesCell 


</td>  
<td>



Specifies what cell the freeze will be attached to. The row above this cell will continue to be visible as you continue scrolling 


</td>  
<td>




</td>  
<td>



NO 


</td> </tr>  
<tr>  
<td>



AnchorViewCell 


</td>  
<td>



Specifies what row will be at the very top of the sheet after the freeze is executed 


</td>  
<td>




</td>  
<td>



NO 


</td> </tr> </table>  
  
<table>  
<tr>  
<td>



Formula 


</td>  
<td>



  



</td>  
<td>

  

</td> </tr>  
<tr>  
<td>



=jFreezePanes 

( 

FreezePanesCell 

,AnchorViewCell 

) 


</td>  
<td>



  



</td>  
<td>




</td> </tr> </table>

  


###  Function Composition   
  
<table>  
<tr>  
<td>



FromFile 


</td>  
<td>



Worksheet 


</td> </tr>  
<tr>  
<td>



Inventory Demo 


</td>  
<td>



InventoryByCategory 


</td> </tr> </table>

=jFreezePanes  (  A21  ,13:13  ) 
