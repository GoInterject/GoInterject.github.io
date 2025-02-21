---
title: ReportLookup()
filename: "ReportLookup.md"
layout: custom
keywords: [ReportLookup, lookup, function, formula, data, pull]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Embeddable Helper Functions"]
links: ["/wFunctions/jDataPortal.html", "https://docs.gointerject.com/wFunctions/jDataPortal.html", "https://docs.gointerject.com/wFunctions/Param.html", "/wTroubleshoot/Reports.html#validation-report-for-interject-events", "/wFunctions/jDataPortal.html", "/wFunctions/jDataPortal.html", "/wFunctions/Param.html"]
image_dir: ""
images: []
description: The ReportLookup function pulls a single piece of data from a data source and inserts it into a single cell within a spreadsheet.
---
* * *

##  Function Summary

The ReportLookup function pulls a single piece of data from a data source and inserts it into a single cell within a spreadsheet. 

###  Function Arguments

<button class="collapsible-parameter">**Data Portal**<br>The name of the Interject Data Portal that will be used as the data source for this function. The helper function [jDataPortal()](/wFunctions/jDataPortal.html) can be used to further define which row to use from the Data Portal.</button>
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

<button class="collapsible-parameter">**TargetDataRange**<br>A single cell where the data will be inserted. If the Data Portal returns a list of data, this function will return the value from the first row.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Cell Range</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Single cell</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>No data inserted</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**ColDefRange**<br>Column definition range: A single cell indicating the name of the column of the data source. Only data from this column will be inserted.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Cell Range</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Single cell</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Returns the first column from the data source</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Parameters**<br>The cells designating the matching parameters for the Data Portal. The values in these cells will filter the data that is inserted from the data source.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td><a href="https://docs.gointerject.com/wFunctions/Param.html">Param()</a></td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>The values must match the order of the parameters in the data source (The order can be verified using the [Validation Report](/wTroubleshoot/Reports.html#validation-report-for-interject-events) )</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Data is not filtered</td>
    </tr>
  </tbody>
</table>
</div>

###  Excel Formula Bar Example

```Excel
=ReportLookup(jDataPortal("NorthwindCustomers",1,"[CustomerID] Like '%SAVE%'"),C14,H1)
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =ReportLookup()  |  The name of this function.  |  
|  DataPortal  |  "jDataPortal("NorthwindCustomers",1,"[CustomerID] Like ‘%SAVE%')"  |  Uses the helper function [jDataPortal()](/wFunctions/jDataPortal.html) designating the "NorthwindCustomers" Data Portal. Filters the records to include only those whose CustomerID contains the string "save".  |  
|  TargetDataRange  |  C14  |  Data will be inserted to cell C14.  |  
|  ColDefRange  |  H1  |  The column name in H1 will be the data field that is returned from the data source.  |  
|  Parameters  |  N/A  |  The data returned from the data source will not be filtered.  |  

###  Embeddable Helper Functions

* [jDataPortal](/wFunctions/jDataPortal.html)
* [Param](/wFunctions/Param.html)
