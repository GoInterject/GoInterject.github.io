---
title: jColumnDef()
layout: custom
keywords: [jColumnDef, helper, function, formula]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition"]
links: ["/wIndex/FinCube---The-Financial-Cube.html", "/wGetStarted/L-Create-FinancialVariable.html", "/wIndex/FinCube---The-Financial-Cube.html"]
description: The jColumnDef function defines a column based on one or more parameters.
---
* * *

##  Function Summary

The jColumnDef function defines a column based on one or more parameters. Each parameter represents a segment. The segments can be set to filter the data that this column represents. Typically this function is used with a Data Pull function for a financial report.

The jColumnDef function utilizes a DataPortal to interact with the segments. This DataPortal is specifically setup for the particular needs of the company using Interject. The segments are thus customizable. For most companies, the Interject [FinCube](/wIndex/FinCube---The-Financial-Cube.html) DataPortal will suffice for their reporting needs.

For an example of this function, see [Lab Create: Financial Variable](/wGetStarted/L-Create-FinancialVariable.html).

###  Function Arguments

The parameters and segments listed below are some examples of the FinCube DataPortal. Actual parameters will vary depending on what DataPortal is being used. For more information about these parameters, see [FinCube](/wIndex/FinCube---The-Financial-Cube.html).

<button class="collapsible-parameter">**Source (Segment12)**<br>The source of the data (e.g. "Actual", "Budget", "Projection", etc.).</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String/Range</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char or single cell</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Does not filter data</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Period (Segment9)**<br>The period of the data (e.g. 1-12 for a month of the year, 1-4 for a quarter). Also accepts YYYY-MM format.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String/Range</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char or single cell</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Does not filter data</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Year (Segment10)**<br>The year of the data. Also accepts YYYY-MM format.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String/Range</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char or single cell</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Does not filter data</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Version (Segment11)**<br>The version of the data.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String/Range</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char or single cell</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Does not filter data</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Customizable (Segment1-8)**<br>Configurable segment.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Custom</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Custom</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Custom</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**BalanceType**<br>A string indicating the balance type.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>"MTD", "QTD", "YTD", "QTR"</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>"MTD"</td>
    </tr>
  </tbody>
</table>
</div>

###  Excel Formula Bar Example

```Excel
=jColumnDef(Actual,11,2001)
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  jColumnDef  |  The name of this function.  |  
|  Source  |  "Actual"  |  The data for this column will be from "Actual".  |  
|  Period  |  11  |  The data for this column will be from period 11.  |  
|  Year  |  2001  |  The data for this column will be from year 2001.  |  
