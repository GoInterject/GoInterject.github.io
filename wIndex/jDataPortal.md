---
title: jDataPortal()
layout: custom
keywords: [jDataPortal, function]
description: The jDataPortal function establishes a connection to an Interject DataPortal that will be used as the data source for the function it is embedded in.
---

##  Function Summary
The jDataPortal function establishes a connection to an Interject DataPortal that will be used as the data source for the function it is embedded in. Data sets accessed utilizing the jDataPortal are stored in memory. This allows the data set to be accessed later without having to query the data again via the DataPortal.

For an example of this function, see [Lab Dev: Customer Aging Detail](/wGetStarted/L-Dev-CustomerAgingDetail.html).

###  Function Arguments

<button class="collapsible-parameter">**DataPortalName**<br>The name of the Interject DataPortal that will be used as the data source for this function.</button>
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

<button class="collapsible-parameter">**DataResultNumber**<br>The number of the particular data set held in memory from previous queries. Each time the jDataPortal is accessed, it will return a data set held in memory. By specifying a number here, that particular data set can be returned.</button>
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
		<td>Will query data via the DataPortal</td>
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
|  Data Portal Name  |  NorthwindMultiRecord_Pull  |  This function will use the "NorthwindMultiRecord_Pull" DataPortal for the data source.  |  
|  Data Result Number  |  2  |  This data connection will use the 2nd result set previously held in memory from previous calls.  |  
|  Filter  |  [CompanyName] Like ‘%s%’  |  This data connection will only return records whose CompanyName contains an 's' character.  |  
|  OrderBy  |  [CustomerID] ASC  |  The data result will be ordered by the column CustomerID in ascending order.  |  
|  CommandOverride  |    |  Left blank to indicate to not override the command.  |  
|  ConnectionOverride  |    |  Left blank to indicate to not override the connection.  |  

###  Usable In These Report Formulas

* [ReportRange()](ReportRange.html)
* [ReportVariable()](ReportVariable.html)
* [ReportFixed()](ReportFixed.html)
