---
title: jRangeTag()
layout: custom
keywords: [jrangetag, function]
description: The jRangeTag() function is used to label or tag a range or a single cell with a custom name.
---
##  Function Summary 

The jRangeTag() function is used to label or tag a range or a single cell with a custom name. It is possible to use jRangeTag() to insert specific data into the specified region. It is also possible to use jRangeTag() to locate setting on a worksheet 

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



Tag 


</td>  
<td>

The user defined name for a cell range or address 
</td>  
<td>

  

</td>  
<td>

NO 
</td> </tr>  
<tr>  
<td>

Range 
</td>  
<td>

This is the cell area or address that is selected within the worksheet 
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



=jRangeTag( 

Tag 

,Range 

) 


</td>  
<td>



=jRangeTag( 

"Settings" 

,"F3:J12" 

) 


</td>  
<td>



  


← This is the custom name for the range 

← The set of cells in the worksheet that will be identified by the tag 


</td> </tr> </table>
