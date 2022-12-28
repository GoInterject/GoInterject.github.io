---
title: jDropdown()
layout: custom
keywords: [jDropdown, function]
description: The jDropdown function returns data from a DataPortal that can be displayed in a dropdown window for the user to select and insert into a designated cell within the spreadsheet.
---

##  Function Summary
The jDropdown function returns data from a DataPortal that can be displayed in a dropdown window for the user to select and insert into a designated cell within the spreadsheet. It is typically used to easily insert a valid parameter into the spreadsheet to filter the data returned by a report function after a pull action. When this function is linked to a hyperlink, the user can simply click on the hyperlink to display a list of valid parameters and insert one or more into the spreadsheet.

For an example of this function, see [jDropdown](/wGetStarted/L-Create-Dropdowns.html).

###  Function Arguments

<button class="collapsible-parameter">**DataPortal**<br>The name of the Interject DataPortal that will be used as the data source for this function.</button>
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

<button class="collapsible-parameter">**Parameters**<br>The cells designating the parameters for the DataPortal. The values in these cells will filter the data that is inserted from the data source.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td><a href="https://docs.gointerject.com/wIndex/Param.html">Param()</a></td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>The values must match the order of the parameters in the data source (The order can be verified using the [ Validation Report ](/wTroubleshoot/Reports.html#validation-report-for-pullsave-events) )</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Data is not filtered</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**MultiSelect**<br>True: Will enable the option to select multiple entries to insert.<br><br>False: Will only enable one entry to be selected.</button>
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

<button class="collapsible-parameter">**Target Cell**<br>The range where the selected entry will be inserted (will insert into every cell in this range).</button>
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
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Value Column Name**<br>The name of the column to be used for the entry or entries that will be inserted into the Target Cell.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
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

<button class="collapsible-parameter">**Display Column Name**<br>Then name of the column from the DataPortal that will be displayed in the drop down list.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Uses Value Column Name</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Delimiter**<br>The string that will be used as the delimiter when inserting multiple selections.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>","</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Instruction Text**<br>The string that will be displayed in the popup window under the window title.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>"Please select the desired options below."</td>
    </tr>
  </tbody>
</table>
</div>


###  Excel Formula Bar Example

```Excel
=jDropdown(jDataPortal("NorthwindCustomersDropdown",1),,FALSE,C17,"CompanyName","DisplayText",,"Select a Customer")
```



###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =jDropdown()  |  The name of this function.  |  
|  DataPortal  |  jDataPortal("NorthwindCustomersDropdown",1)  |  Uses the helper function [jDataPortal()](/wIndex/jDataPortal.html) designating the "NorthwindCustomersDropdown" DataPortal. Filters the records to include only those whose CustomerID contains the string "save".  |  
|  Parameters  |  ""  |  The data returned from the data source will not be filtered.  |  
|  MultiSelect  |  FALSE  |  Only one entry can be selected from the dropdown window.  |  
|  Target Cell  |  C17  |  The entry selected will be inserted into cell C17.  |  
|  Value Column Name  |  "CompanyName"  |  The selected value for the column "CompanyName" will be inserted.  |  
|  Display Column Name  |  "DisplayText"  |  ???  |  
|  Delimiter  |    |  Value ignored because MultiSelect is false.  |  
|  Instruction Text  |  "Select a Customer"  |  The text "Select a Customer" will be displayed under the title in the dropdown window.  |  

###  Embeddable Helper Functions

* [jDataPortal](/wIndex/jDataPortal.html)
* [ Param ](Param.html)
