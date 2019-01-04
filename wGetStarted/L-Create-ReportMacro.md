---
title: "Lab Create: Using Report Macro"
layout: custom
keywords: [report, macro, vba, hooks, sub, routine, function]
description:  Report Macro is useful for specialized reports where a customized action needs to be taken. This action can be built into a VBA Macro based on the complex needs of the report.
---
* * *

##  **Overview:**

Report Macro is an excel formula provided by INTERJECT. It allows IINTERJECT to interact with publicly defined VBA functions on a report.  Report Macro is useful for specialized reports where a customized action needs to be taken. This action can be built into a VBA Macro based on the complex needs of the report. Then, ReportMacro() is used to execute the custom action at the right point within the reporting process.

###  Using Report Macro 

The report macro formula acts in conjunction with another INTERJECT report formula such as a [ ReportRange() ](/KB/ExcelFunctions/ReportRange.html). It is useful when a workbook requiring VBA macros must be used. ReportMacro() is an ordered formula, which means that INTERJECT will perform executions on all report formulas placed above or to the left of the ReportMacro() formula before it is executed. 

**Step 1:** Open the Customer Aging Report. (If this report is unfamiliar, click [ here ](/KB/HowToUse/Walkthroughs/CustomerAging.html) for a business use case review on the Customer Aging Report.) This time, we want to make sure a value is set to 200 every time the report is pulled. 

![](/images/L-Create-RepMacro/01.jpg)

<br> 


**Step 2:** To begin, **unfreeze** the panes. 

![](/images/L-Create-RepMacro/02.jpg)

<br> 


**Step 3:** If you see the **Developer Ribbon**, skip this step and the next one. However, if you do not see the **Developer Ribbon** select **File**

![](/images/L-Create-RepMacro/03.jpg)

<br> 


**Step 4:** Now, select **Options.**

![](/images/L-Create-RepMacro/04.jpg)

<br> 


**Step 5:** Select the **Customize Ribbon** tab in the **Main Tabs** section, select the check box next to **Developer**, then select **OK**. 

![](/images/L-Create-RepMacro/05.jpg)

<br> 


**Step 6:** Select the **Developer Ribbon**. 

![](/images/L-Create-RepMacro/06.jpg)

<br> 


**Step 7:** Select **Visual Basic**. 

![](/images/L-Create-RepMacro/07.jpg)

<br> 


**Step 8:** To create a new module, right click in the **Projects** window, place your cursor over **Insert**, and select **Module**. 

![](/images/L-Create-RepMacro/08.jpg)

<br> 


The example code is provided here. 

```VB

Public Function MyCustomFunction()

  Call Place_Value(ActiveSheet.Range("L31"))

End Function  

 ' Clears the value in the cell then sets it to equal 200 

 Sub Place_Value(sTarget As Range)

  sTarget.ClearContents 

    sTarget = 200 

End Sub

```

  


**Step 9:** Insert your code into the editing window, then select **Debug**, then compile VBAProject and exit out of the VBA window. 

![](/images/L-Create-RepMacro/09.jpg)

<br> 


**Step 10:** In cell D8, Insert the label **Macro 1:** and align it to the right. 

![](/images/L-Create-RepMacro/10.jpg)

<br> 


**Step 11:** In cell E8 insert **=ReportMacro()** and select **fx**. 

![](/images/L-Create-RepMacro/11.jpg)

<br> 


**Step 12:** In the parameter OnpullSaveOrBoth, input **Pull**. In the parameter OnClearRunOrBoth, input **Both**. 

![](/images/L-Create-RepMacro/12.jpg)

<br> 


**Step 13:** For the MacroNameToRun parameter, input the exact name of the public function that you created. In this case, you will use **MyCustomFunction**. 

![](/images/L-Create-RepMacro/13.jpg)

<br> 


**Step 14:** Pull the data. You will notice that the report macro was ordered after the report range action. This is due to INTERJECT formula event ordering. 

![](/images/L-Create-RepMacro/14.jpg)

<br>

###  Requirements for VBA 

ReportMacro() requires a public function without any parameters, as it is the initial interaction point with INTERJECT. Inside of that initial function, any function can be run, including calls to subroutines and other functions, but the initializing macro must be a public function. 

![](/images/L-Create-RepMacro/15.jpg)

<br> 


ReportMacro() also requires the VBA macro to be in written in shared module, and it will not work with a Workbook or Sheet module. 

![](/images/L-Create-RepMacro/16.jpg)

<br> 


INTERJECT will error out the report macro formula upon completion of the INTERJECT event associated with the macro formula, however the INTERJECT event will complete. 

![](/images/L-Create-RepMacro/17.jpg)

<br>

###  Enabling VBA Hooks 

Due to heavy load on user sessions, four of the six VBA hooks that INTERJECT uses will be deprecated. This feature should only be enabled when a VBA macro is required for custom actions in specialized reports.   
  
<table>   
<tr>  
<th>



VBA Hooks To Be Deprecated 


</th>  
<th>



When Used 


</th> </tr>  
<tr>  
<td>



Interject_SaveComplete 


</td>  
<td>

Upon completion of an INTERJECT save event 
</td> </tr>  
<tr>  
<td>

Interject_PullComplete 
</td>  
<td>

Upon completion of an INTERJECT pull event 
</td> </tr>  
<tr>  
<td>

Interject_ClearPullComplete 
</td>  
<td>

Upon completion of an INTERJECT clear event 
</td> </tr>  
<tr>  
<td>

Interject_ClearSaveComplete 
</td>  
<td>

Upon completion of an INTERJECT clear event on the save form 
</td> </tr> </table>  
  
<table>    
<tr>  
<th>



VBA Hooks To Be Supported 


</th>  
<th>



When Used 


</th> </tr>  
<tr>  
<td>

Interject_WorkbookOpen_Drill 
</td>  
<td>



When a drill opens a different workbook from the initial workbook 


</td> </tr>  
<tr>  
<td>

Interject_WorkbookOpen_Library 
</td>  
<td>



When a workbook is opened from the report library. 


</td> </tr> </table>

  
Enabling INTERJECT VBA hooks is currently done by including a VBA Module with a public subroutine (not function) that matches the name hook above without any parameters. If the subroutine is found, it will be fired at the appropriate time, based on the type of VBA hook used. Using a VBA hook does not require a ReportMacro() formula in order to function, because the VBA hook is sent by INTERJECT upon the completion of certain events. 

```VB

' Simple Example of using a VBA hook

Public Sub Interject_PullComplete()

  If ActiveSheet.Range("L31") > 199 Then

    ActiveSheet.Range("L31") = 150

  End If 

End Sub 

```