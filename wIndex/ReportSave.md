---
title: ReportSave()
filename: "ReportSave.md"
layout: custom
keywords: [ReportSave, save, function, formula, data]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Embeddable Helper Functions"]
links: ["/wGetStarted/L-Dev-CustomerCreditSave.html", "https://docs.gointerject.com/wIndex/jDataPortal.html", "https://docs.gointerject.com/wIndex/Param.html", "/wTroubleshoot/Reports.html#validation-report-for-pullsave-events", "/wIndex/jDataPortal.html", "Param.html"]
image_dir: ""
images: []
description: The ReportSave function will use a designated DataPortal to save data in a worksheet to a data source.
---
* * *

##  Function Summary

The ReportSave function will use a designated DataPortal to save data in a worksheet to a data source. Typically this is done by setting up a DataPortal to run a procedure to take the designated data in the worksheet and save it to a data source. This function makes it convenient to upload local changes to the data source without having to edit it directly.

For an example of this function, see [Lab Dev: Customer Aging Detail](/wGetStarted/L-Dev-CustomerCreditSave.html).

###  Function Arguments

<button class="collapsible-parameter">**DataPortal**<br>The name of the Interject DataPortal that will be used when this function is ran.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String/<a href="https://docs.gointerject.com/wIndex/jDataPortal.html">jDataPortal()</a></td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**RowDefRange**<br>A single column range that contains the unique row IDs that will be used to save the rows in this range via the data source. A corresponding column name for the unique ID must be included in this column in the row defined in ColDefRange.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Must be a single column</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**ColDefRange**<br>Column definition range: The range designating the names of the columns that will be saved via the data source.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td></td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Will save all columns</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**ResultsRange**<br>The range designating the names of the columns that will be returned via the data source. Typically this is information sent back from the DataPortal to be displayed after a save.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td></td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>No return data is displayed</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Parameters**<br>The cells designating the matching parameters for the DataPortal. The values in these cells will filter the data that is saved via the data source.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td><a href="https://docs.gointerject.com/wIndex/Param.html">Param()</a></td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>The values must match the order of the parameters in the data source (The order can be verified using the [Validation Report](/wTroubleshoot/Reports.html#validation-report-for-pullsave-events) )</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Data is not filtered</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**AutoSaveFile**<br>True: Will save the workbook after a save action. (Saves at current save location without prompt. If file is not saved already, will save in the last used folder.)<br><br>False: Will not save the workbook after a save action.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Boolean</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td></td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>False</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**CaptureAllRows**<br>True: Will override the value in RowDefRange and designate all rows to be saved via the data source.<br><br>False: Will use the value in RowDefRange to determine which rows are saved.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Boolean</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td></td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>False</td>
    </tr>
  </tbody>
</table>
</div>

###  Excel Formula Bar Example

```Excel
=ReportSave("NorthwindInvoiceSave",B42:B58,12:12,14:14)
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =ReportSave()  |  The name of this function.  |  
|  DataPortal  |  "NorthwindInvoiceSave"  |  This function will use the "NorthwindInvoiceSave" DataPortal for the data source.  |  
|  RowDefRange  |  B42:B58  |  The unique row IDs are designated to be in column B and the rows 42:58 will be saved.  |  
|  Col Def Range  |  12:12  |  Row 12 is designated to contain the column names that will be saved via the data source.  |  
|  ResultRange  |  14:14  |  Row 14 is designated to contain the column names that will be displayed when returning from the save.  |  
|  Parameters  |  N/A  |  Data will not be filtered for this save.  |  

###  Embeddable Helper Functions

* [jDataPortal](/wIndex/jDataPortal.html)
* [Param](Param.html)
