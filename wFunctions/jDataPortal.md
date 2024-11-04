---
title: jDataPortal()
filename: "jDataPortal.md"
layout: custom
keywords: [jDataPortal, helper, function, formula]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Usable In These Report Formulas"]
links: ["/wDeveloper/L-Dev-CustomerAgingDetail.html", "/wDeveloper/SetupjDataPortal.html", "/wPortal/INTERJECT-Roles.html", "/wFunctions/ReportRange.html", "/wFunctions/ReportVariable.html", "/wFunctions/ReportFixed.html"]
image_dir: ""
images: []
description: The jDataPortal function establishes a connection to an Interject Data Portal that will be used as the data source for the function it is embedded in.
---
* * *

##  Function Summary

The jDataPortal function establishes a connection to an Interject Data Portal that will be used as the data source for the function it is embedded in. Data sets accessed utilizing the jDataPortal are stored in memory. This allows the data set to be accessed later without having to query the data again via the Data Portal.

For an example of this function, see [Lab Dev: Customer Aging Detail](/wDeveloper/L-Dev-CustomerAgingDetail.html).

For instructions on how to set up this function, see [Setting Up the jDataPortal](/wDeveloper/SetupjDataPortal.html).

###  Function Arguments

<button class="collapsible-parameter">**DataPortalName**<br>The name of the Interject Data Portal that will be used as the data source for this function.</button>
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

<button class="collapsible-parameter">**DataResultNumber**<br>The index number of the data set requested. When multiple sets are returned from the data source, this parameter can specify the particular result set.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Integer</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td></td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Will return the first data set</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Filter**<br>A valid SQL statement that normally follows a WHERE statement. This will filter the data.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char; valid SQL statement</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Will not filter data</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**OrderBy**<br>A valid SQL statement that normally follows an ORDER BY statement. This will order the data.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char; valid SQL statement</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Will not order data</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**CommandOverride**<br>A string indicating a different Stored Procedure or API to run. This feature can only be done by ClientAdmin or a SysAdmin [roles](/wPortal/INTERJECT-Roles.html).</button>
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
		<td>Will not override</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**ConnectionOverride**<br>A string indicating a different data connection to run.</button>
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
		<td>Will not override</td>
    </tr>
  </tbody>
</table>
</div>

###  Excel Formula Bar Example

```Excel
=jDataPortal("NorthwindMultiRecord_Pull",2,"[CompanyName] Like '%s%'","[CustomerID] ASC")
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =jDataPortal  |  The name of this function.  |  
|  Data Portal Name  |  NorthwindMultiRecord_Pull  |  This function will use the "NorthwindMultiRecord_Pull" Data Portal for the data source.  |  
|  Data Result Number  |  2  |  This data connection will use the 2nd result set previously held in memory from previous calls.  |  
|  Filter  |  [CompanyName] Like ‘%s%’  |  This data connection will only return records whose CompanyName contains an 's' character.  |  
|  OrderBy  |  [CustomerID] ASC  |  The data result will be ordered by the column CustomerID in ascending order.  |  
|  CommandOverride  |    |  Left blank to indicate to not override the command.  |  
|  ConnectionOverride  |    |  Left blank to indicate to not override the connection.  |  

###  Usable In These Report Formulas

* [ReportRange()](/wFunctions/ReportRange.html)
* [ReportVariable()](/wFunctions/ReportVariable.html)
* [ReportFixed()](/wFunctions/ReportFixed.html)
