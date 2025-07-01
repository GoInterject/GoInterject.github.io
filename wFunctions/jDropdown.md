---
title: jDropdown()
filename: "jDropdown.md"
layout: custom
keywords: [jDropdown, helper, function, formula]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Embeddable Helper Functions"]
links: ["/wGetStarted/L-Create-Dropdowns.html", "https://docs.gointerject.com/wGetStarted/L-Create-Dropdowns.html#creating-a-custom-jdropdown-list", "https://docs.gointerject.com/wFunctions/jDataPortal.html", "https://docs.gointerject.com/wFunctions/Param.html", "/wTroubleshoot/Reports.html#validation-report-for-interject-events", "/wFunctions/jDataPortal.html", "/wFunctions/jDataPortal.html", "/wFunctions/Param.html"]
image_dir: ""
images: []
description: The jDropdown function returns data from a Data Portal that can be displayed in a dropdown window for the user to select and insert into a designated cell within the spreadsheet.
---
* * *

##  Function Summary

The jDropdown function returns data from a Data Portal that can be displayed in a dropdown window for the user to select and insert into a designated range of cells within the spreadsheet. It is typically used to easily insert a valid parameter into the spreadsheet to filter the data returned by a report function after a pull action. When this function is linked to a hyperlink, the user can simply click on the hyperlink to display a list of valid parameters and insert one or more into the spreadsheet.

For an example of this function, see [jDropdown](/wGetStarted/L-Create-Dropdowns.html).

###  Function Arguments

<button class="collapsible-parameter">**Data Portal**<br>The name of the Interject Data Portal that will be used as the data source for this function. A <a href="https://docs.gointerject.com/wGetStarted/L-Create-Dropdowns.html#creating-a-custom-jdropdown-list">Custom List</a> may be entered instead of a Data Portal.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String/<a href="https://docs.gointerject.com/wFunctions/jDataPortal.html">jDataPortal()</a></td>
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

<button class="collapsible-parameter">**Parameters**<br>The cells designating the parameters for the Data Portal. The values in these cells will filter the data that is inserted from the data source.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td><a href="https://docs.gointerject.com/wFunctions/Param.html">Param()</a></td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>The values must match the order of the parameters in the data source (The order can be verified using the <a href="/wTroubleshoot/Reports.html#validation-report-for-interject-events">Validation Report</a>)</td>
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

<button class="collapsible-parameter">**Target Cell**<br>The range where the selected entry(s) will be inserted. If a single cell is designated, the entry will go there. If a range of cells with header values is designated, the entries will populate on the same row as the jDropdown link starting at the first column of this range.</button>
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

<button class="collapsible-parameter">**Display Column Name**<br>Then name of the column from the Data Portal that will be displayed in the drop down list.</button>
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
|  DataPortal  |  jDataPortal("NorthwindCustomersDropdown",1)  |  Uses the helper function [jDataPortal()](/wFunctions/jDataPortal.html) designating the "NorthwindCustomersDropdown" Data Portal. Filters the records to include only those whose CustomerID contains the string "save".  |  
|  Parameters  |  ""  |  The data returned from the data source will not be filtered.  |  
|  MultiSelect  |  FALSE  |  Only one entry can be selected from the dropdown window.  |  
|  Target Cell  |  C17  |  The entry selected will be inserted into cell C17.  |  
|  Value Column Name  |  "CompanyName"  |  The selected value for the column "CompanyName" will be inserted.  |  
|  Display Column Name  |  "DisplayText"  |  The values from the column "DisplayText" will be displayed in the dropdown options.  |  
|  Delimiter  |    |  Value ignored because MultiSelect is false.  |  
|  Instruction Text  |  "Select a Customer"  |  The text "Select a Customer" will be displayed under the title in the dropdown window.  |  

###  Embeddable Helper Functions

* [jDataPortal](/wFunctions/jDataPortal.html)
* [Param](/wFunctions/Param.html)
