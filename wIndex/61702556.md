---
title: Interject Documentation > ReportDrill()
layout: custom
---
* * *

  


##  What is a ReportDrill   


ReportDrill is widely used throughout INTERJECT as a way to connect and pass information between workbooks. Drilling takes a defined input and passes it in as a parameter to another workbook, similar to hyperlinks on a web page: Depending on the types of input behind the hyperlink, more detailed and specific information can be viewed. While there are few codes crucial to the process, they can be structured in ways that make them very powerful. Find examples of Drilling in [ Creating Your Own Drills ](https://interject.atlassian.net/wiki/display/ID/Creating+Your+Own+Drills) .   


###  Before starting, you'll need 

Intermediate knowledge of Excel   


Advanced knowledge of INTERJECT reports 

###  Function Arguments   
  
<table>  
<tr>  
<td>



**Parameter Name**


</td>  
<td>



**Description**


</td>  
<td>



**Default**


</td>  
<td>



**Optional**


</td> </tr>  
<tr>  
<td>



ReportCellToRun 


</td>  
<td>



Input the sheet name and a cell for the function to populate. 

Functions  inside  workbook. 


</td>  
<td>



  



</td>  
<td>



YES* 


</td> </tr>  
<tr>  
<td>



ReportCodeToRun 


</td>  
<td>



Enter a registered Drill Code to open a file and run a report  outside  the current workbook. 

Drill codes can be set up in the  [ report library  ](https://interject.atlassian.net/wiki/display/ID/Updating+Report+Library) and are used to connect sheets in different workbooks. 


</td>  
<td>



  



</td>  
<td>



YES* 


</td> </tr>  
<tr>  
<td>



TransferPairs** 


</td>  
<td>



Enter  [ Pairs  ](/wIndex/81756188.html) within a  [ PairGroup  ](/wIndex/81756186.html) function to copy data and restrict when the drill is used. 

See [ Drill: Customer Aging Report ](/wGetStarted/128421015.html) for more information on usage. 


</td>  
<td>



  



</td>  
<td>



YES 


</td> </tr>  
<tr>  
<td>



DrillName 


</td>  
<td>



The drill name shown to users when the drill button or keystroke is applied. 


</td>  
<td>



  



</td>  
<td>



YES 


</td> </tr> </table>

*  Either ReportCellToRun or ReportCodeToRun must be entered. 

** Only one argument is needed but adding the TransferPairs argument will allow for data transfer. 

  


  


  


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



=ReportDrill( 

ReportCellToRun 

,TransferPairs 

,DrillName 

) 


</td>  
<td>



=ReportDrill( 

** Drill_Order!B2  **

,PairGroup( 

Pair( 

**F13** :  **F14**

,  **Drill_Order!H7**

,  **TRUE**

) 

) 

,  **"Open Order Page"**

) 


</td>  
<td>



  


←Cell is being drilled 

← A PairGroup (Needed to indicated more pair) 

  


←Source cell to get data 

← Target cell to put data 

← This TRUE flag indicates the values are required. 

  


← Title of drill 

  



</td> </tr> </table>
