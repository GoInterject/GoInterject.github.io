---
title: Interject Documentation > PairGroup()
layout: custom
---
##  Function Summary 

Provides an easy method to add multiple [ Pair() ](/wIndex/81756188.html) functions together. 

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



Pair1 


</td>  
<td>

Add a [ Pair() ](/wIndex/81756188.html) function. 
</td>  
<td>

  

</td>  
<td>



YES 


</td> </tr>  
<tr>  
<td>

... 
</td>  
<td>

... 
</td>  
<td>

  

</td>  
<td>

... 
</td> </tr>  
<tr>  
<td>

Pair34  
</td>  
<td>

Add a  [ Pair() ](/wIndex/81756188.html) function.  
</td>  
<td>

  

</td>  
<td>

YES  
</td> </tr> </table>

**  
**

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



= PairGroup( 
    
    
                Pair1

,... 

,Pair34 

) 


</td>  
<td>



=  ReportDrill  ( 

**Drill_Order!B2**

, 

, **PairGroup** ( 

Pair( 

**F13:F14**

,  **Drill_Order!H7**

,  **TRUE**

) 

) 

,  **"Open Order Page"**

) 


</td>  
<td>



  


  


  


← Pair Group function embedded in ReportDrill formula. This example accepts a single [ pair ](/wIndex/81756188.html) . 


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

Drill_Orders 
</td> </tr> </table>
