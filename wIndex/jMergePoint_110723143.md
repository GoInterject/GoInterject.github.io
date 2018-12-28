---
title: Interject Documentation > jMergePoint()
layout: custom
keywords: [jmergepoint, function]
description: jMergePoint acts as a reference point for ReportMerge.
---

##  Function Summary 

Acts as a reference point for [ ReportMerge ](/wIndex/110723133.html) . For examples and discussion, view the tutorial. 

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



TabName 


</td>  
<td>

Enter the name of the tab to be copied. Supports a single variable (example "Sheet1", "Sheet*", or just "*") 
</td>  
<td>

  

</td>  
<td>



NO 


</td> </tr>  
<tr>  
<td>



Placement 


</td>  
<td>



Enter "before" or "after" to indicate the placement of the sheet based on the anchor sheet 


</td>  
<td>

  

</td>  
<td>

NO 
</td> </tr>  
<tr>  
<td>

Anchor 
</td>  
<td>

Enter the name of the sheet to be used as the placement anchor. Also use jTabName() to indicate the current sheet, or use jTabName(Sheet2!a2) to reference another sheet. 
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



=jMergePoint 

(TabName 

,Placement 

,  Anchor 

) 


</td>  
<td>
= jMergePoint ("Trend" ,"before" , jTabName(First!E14)) 

=jMergePoint ("*" ,"before" , jTabName()) 

</td>  
<td>

Move the <b>Trend</b> tab from the other Excel file to be in front of the tab named "<b>First</b>".

  
Move all of the tabs to be in front of the current tab (the one with this formula in it) 


</td> </tr> </table>
