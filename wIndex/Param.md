---
title: Param()
filename: "Param.md"
layout: custom
keywords: [Param, helper, function, formula]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Usable In These Functions"]
links: ["/wTroubleshoot/Reports.html#validation-report-for-pullsave-events", "/wGetStarted/L-Drill-CustomerAging.html", "ReportFixed.html", "ReportLookup.html", "ReportRange.html", "ReportSave.html", "ReportVariable.html", "jDropdown.html"]
image_dir: ""
images: []
description: The Param function transfers values as parameters to the DataPortal.
---
* * *

##  Function Summary
The Param function transfers values as parameters to the DataPortal. The values must match the order of the parameters in the data source (The order can be verified using the [Validation Report](/wTroubleshoot/Reports.html#validation-report-for-pullsave-events) ).

For an example of this function, see [Lab Drill: Customer Aging](/wGetStarted/L-Drill-CustomerAging.html).

###  Function Arguments

<button class="collapsible-parameter">**Value1**<br>A string or single cell indicating the value to be transferred as a parameter to the DataPortal. Multiple values can be entered separated by a comma.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String/Single Cell</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char or must be a single cell</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Will not transfer value</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Val2 - Val40**<br>A string or single cell indicating the value to be transferred as a parameter to the DataPortal. Multiple values can be entered separated by a comma.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String/Single Cell</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char or must be a single cell</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Will not transfer value</td>
    </tr>
  </tbody>
</table>
</div>

###  Excel Formula Bar Example

```Excel
=ReportRange("NorthwindCustomers",B14:H15,B2:H2,B4:H4,Param(C7,C8,C9),FALSE,FALSE,,FALSE,FALSE)
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  Param()  |  The name of this function.  |  
|  Value1  |  C7  |  The value in C7 will be passed as a parameter to the DataPortal  |  
|  Val2  |  C8  |  The value in C8 will be passed as a parameter to the DataPortal  |  
|  Val3  |  C9  |  The value in C9 will be passed as a parameter to the DataPortal  |  

###  Usable In These Functions

* [ReportFixed](ReportFixed.html)
* [ReportLookup](ReportLookup.html)
* [ReportRange](ReportRange.html)
* [ReportSave](ReportSave.html)
* [ReportVariable](ReportVariable.html)
* [jDropdown](jDropdown.html)
