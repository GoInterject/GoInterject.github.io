---
title: "Create: Using Report Macro"
filename: "L-Create-ReportMacro.md"
layout: custom
keywords: [report, macro, VBA, triggers, hooks, sub, routine, function]
headings: ["Overview", "Setting up the Worksheet", "Using Report Macro", "Requirements for VBA", "Enabling VBA Hooks"]
links: ["/wIndex/ReportMacro.html", "/wIndex/ReportRange.html", "/wAbout/Customer-Aging.html"]
image_dir: "L-Create-RepMacro"
images: [
	{file: "01", type: "jpg", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""}, 
	{file: "02", type: "jpg", site: "Add-in", cat: "Quick Tools", sub: "", report: "Customer Aging Summary", ribbon: "Simple", config: ""}, 
	{file: "03", type: "jpg", site: "Add-in", cat: "Report", sub: "", report: "", ribbon: "Simple", config: "Yes"}, 
	{file: "04", type: "jpg", site: "Excel", cat: "Options", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "05", type: "jpg", site: "Excel", cat: "Options", sub: "Customize the Ribbon", report: "Customer Aging Summary", ribbon: "", config: "Yes"}, 
	{file: "06", type: "jpg", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "Simple", config: "Yes"}, 
	{file: "07", type: "jpg", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: "Yes"}, 
	{file: "08", type: "jpg", site: "Excel", cat: "Visual Basic", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""}, 
	{file: "09", type: "jpg", site: "Excel", cat: "Visual Basic", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""}, 
	{file: "10", type: "jpg", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: "Yes"}, 
	{file: "11", type: "jpg", site: "Excel", cat: "Function Wizard", sub: "", report: "Customer Aging Summary", ribbon: "", config: "Yes"}, 
	{file: "12", type: "jpg", site: "Excel", cat: "Function Wizard", sub: "", report: "Customer Aging Summary", ribbon: "", config: "Yes"}, 
	{file: "13", type: "jpg", site: "Excel", cat: "Function Wizard", sub: "", report: "Customer Aging Summary", ribbon: "", config: "Yes"}, 
	{file: "14", type: "jpg", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: "Yes"}, 
	{file: "15", type: "jpg", site: "Excel", cat: "Visual Basic", sub: "", report: "Customer Aging Summary", ribbon: "", config: "Yes"}, 
	{file: "16", type: "jpg", site: "Excel", cat: "Visual Basic", sub: "", report: "Customer Aging Summary", ribbon: "", config: "Yes"}, 
	{file: "17", type: "jpg", site: "Add-in", cat: "Progress Bar", sub: "Formulas", report: "Customer Aging Summary", ribbon: "", config: "Yes"}
	]
description: ReportMacro is an Excel formula provided by Interject. It allows Interject to interact with publicly defined VBA functions on a report. ReportMacro is useful for specialized reports where a customized action needs to be taken. This action can be built into a VBA Macro based on the complex needs of the report. Then, ReportMacro() is used to execute the custom action at the right point within the reporting process.
---
* * *

## Overview

[ReportMacro()](/wIndex/ReportMacro.html) is an Excel formula provided by Interject. It allows Interject to interact with publicly defined VBA functions on a report. ReportMacro is useful for specialized reports where a customized action needs to be taken. This action can be built into a VBA Macro based on the complex needs of the report. Then, ReportMacro is used to execute the custom action at the right point within the reporting process.

<blockquote class=lab_info>
 If you are following the Training Labs, this report file can be found in the Report Library at Training Labs > Lab 6 Special Features > Lab 6.3 Using Report Macro.
</blockquote>

### Setting up the Worksheet

The ReportMacro formula acts in conjunction with another Interject report formula such as a [ReportRange()](/wIndex/ReportRange.html). It is useful when a workbook requiring VBA macros must be used. ReportMacro() is an ordered formula, which means that Interject will perform executions on all report formulas placed above or to the left of the ReportMacro() formula before it is executed.

**Step 1:** Open the Customer Aging Report. (If this report is unfamiliar, click [here](/wAbout/Customer-Aging.html) for a business use case review on the Customer Aging Report.) This time, we want to make sure a value is set to 200 every time the report is pulled.

![](/images/L-Create-RepMacro/01.jpg)
<br>

**Step 2:** To begin, **unfreeze** the panes.

![](/images/L-Create-RepMacro/02.jpg)
<br>

**Step 3:** If you see the **Developer Ribbon**, skip forward to the next section. However, if you do not see the **Developer Ribbon** select **File**.

![](/images/L-Create-RepMacro/03.jpg)
<br>

**Step 4:** Now, select **Options**.

![](/images/L-Create-RepMacro/04.jpg)
<br>

**Step 5:** Select the **Customize Ribbon** tab in the **Main Tabs** section, select the check box next to **Developer**, then select **OK**.

![](/images/L-Create-RepMacro/05.jpg)
<br>

**Step 6:** Select the **Developer Ribbon**.

![](/images/L-Create-RepMacro/06.jpg)
<br>

### Using Report Macro

**Step 1:** Select **Visual Basic**.

![](/images/L-Create-RepMacro/07.jpg)
<br>

**Step 2:** To create a new module, right click in the **Projects** window, place your cursor over **Insert**, and select **Module**.

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

**Step 3:** Insert your code into the editing window, then select **Debug**, then compile VBAProject and exit out of the VBA window.

![](/images/L-Create-RepMacro/09.jpg)
<br>

**Step 4:** In cell D8, Insert the label **Macro 1:** and align it to the right.

![](/images/L-Create-RepMacro/10.jpg)
<br>

**Step 5:** In cell E8 insert **=ReportMacro()** and select **fx**.

![](/images/L-Create-RepMacro/11.jpg)
<br>

**Step 6:** In the parameter OnpullSaveOrBoth, input **Pull**. In the parameter OnClearRunOrBoth, input **Both**.

![](/images/L-Create-RepMacro/12.jpg)
<br>

**Step 7:** For the MacroNameToRun parameter, input the exact name of the public function that you created. In this case, you will use **MyCustomFunction**.

![](/images/L-Create-RepMacro/13.jpg)
<br>

**Step 8:** Pull the data. You will notice that the ReportMacro was ordered after the report range action. This is due to Interject formula event ordering.

![](/images/L-Create-RepMacro/14.jpg)
<br>

### Requirements for VBA

ReportMacro() requires a public function without any parameters, as it is the initial interaction point with Interject. Inside of that initial function, any function can be run, including calls to subroutines and other functions, but the initializing macro must be a public function.

![](/images/L-Create-RepMacro/15.jpg)
<br>

ReportMacro() also requires the VBA macro to be in written in a shared module as it will not work with a Workbook or Sheet module.

![](/images/L-Create-RepMacro/16.jpg)
<br>

Interject will error out the ReportMacro formula upon completion of the Interject event associated with the macro formula, however the Interject event will complete.

![](/images/L-Create-RepMacro/17.jpg)
<br>

### Enabling VBA Hooks

Due to heavy load on user sessions, four of the six VBA hooks that Interject uses will be deprecated. This feature should only be enabled when a VBA macro is required for custom actions in specialized reports.

| VBA Hooks To Be Deprecated | When Used |
|-----|-----|
| Interject_SaveComplete | Upon completion of an Interject save event |
| Interject_PullComplete | Upon completion of an Interject pull event |
| Interject_ClearPullComplete | Upon completion of an Interject clear event |
| Interject_ClearSaveComplete | Upon completion of an Interject clear event on the save form |

| VBA Hooks To Be Supported | When Used |
|-----|-----|
| Interject_WorkbookOpen_Drill | When a drill opens a different workbook from the initial workbook |
| Interject_WorkbookOpen_Library | When a workbook is opened from the report library |

Enabling Interject VBA hooks is currently done by including a VBA Module with a public subroutine (not function) that matches the name hook above without any parameters. If the subroutine is found, it will be fired at the appropriate time, based on the type of VBA hook used. Using a VBA hook does not require a ReportMacro() formula in order to function, because the VBA hook is sent by Interject upon the completion of certain events.

```VB

' Simple Example of using a VBA hook

Public Sub Interject_PullComplete()

 If ActiveSheet.Range("L31") > 199 Then

 ActiveSheet.Range("L31") = 150

 End If

End Sub

```
