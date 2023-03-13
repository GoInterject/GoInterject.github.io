---
title: ReportFixed()
layout: custom
keywords: [ReportFixed, function]
description: The ReportFixed function pulls data from a data source and inserts it into a spreadsheet.
---

##  Function Summary
The ReportFixed function pulls data from a data source and inserts it into a spreadsheet. It is similar to the [ ReportRange ](/wIndex/ReportRange.html) function but with the addition of receiving row names as input in addition to column names. Only data that is mapped to both these row and column names from the data source will be inserted. Consequently, the range where data is inserted is defined by the boundaries of the RowDefRange and the ColDefRange. Data returned by this function can be filtered, formatted, and customized for a specific desired report.

For an example of this function, see [Create Inventory Fixed Lab.](/wGetStarted/L-Create-InventoryFixed.html)

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

<button class="collapsible-parameter">**RowDefRange**<br>A single column range whose values that map to the RowDefName field of the data source. Each value in this range will be matched to the same value in the RowDefName of the data source. Only these values will be populated with data after a pull action.<br><br>If the data source does not have a column "RowDefName", this function will look for a column name defined in the column in the ColDefRange and the row defined here in RowDefRange. For example, if row 2 is defined in ColDefRange and column B is defined in RowDefRange, this function will look at the value in B2 to map the data to.<br><br>If there are records in the data source that are excluded in this range, the data from those columns will be included in a [leftover] section after a pull action.</button>
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

<button class="collapsible-parameter">**ColDefRange**<br>A single row range designating the names of the columns of the data source. Only data from these columns will be inserted. Best practice is to use a range instead of whole rows.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 500 columns. Must be a single row.</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Will Error</td>
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
		<td>The values must match the order of the parameters in the data source (The order can be verified using the <a href="https://docs.gointerject.com/wTroubleshoot/Reports.html#validation-report-for-pullsave-events">Validation Report</a>)</td>
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
=ReportFixed("NorthwindFixed",B14:B27,2:2)
```



###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =ReportFixed()  |  The name of this function.  |  
|  DataPortal  |  "NorthwindFixed"  |  This function will use the "NorthwindCustomers" DataPortal for the data source.  |  
|  RowDefRange  |  B14:B27  |  The names found in B14:B27 will be used to map to the column names found in row 2 (ColDefRange). Only data that intersects these names will be inserted on these rows.  |  
|  ColDefRange  |  2:2  |  The names found in row 2 will be used to map to the row names found in row B14:B27 (RowDefRange). Only data that intersects these names will be inserted on these columns.  |  
|  Parameters  |  N/A  |  The data returned from the data source will not be filtered.  |  

###  Embeddable Helper Functions

* [jDataPortal](/wIndex/jDataPortal.html)
* [Param](/wIndex/Param.html)
