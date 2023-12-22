---
title: Pair()
layout: custom
keywords: [Pair, helper, function, formula]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Usable In These Functions"]
description: The Pair function transfers values from one cell to another.
---
* * *

##  Function Summary

The Pair function transfers values from one cell to another. It is typically used in conjunction with the [PairGroup](/wIndex/PairGroup.html) function. Values are transferred upon a designated Interject event (e.g. a drill or as defined in the function it is embedded in). It is best practice to use the PairGroup function even when only entering one Pair.

For an example of this function, see [Lab Drill: Customer Aging](/wGetStarted/L-Drill-CustomerAging.html).

###  Function Arguments

<button class="collapsible-parameter">**From**<br>A string or a single cell indicating the value to be transferred. If a range is entered, it will designate a column of possible cells, one of which will be transferred. The cell to be transferred is determine by the row of the active cell when this function is triggered. For example, if the range starts with column H and the active cell is in row 34, the cell H34 will be transferred.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String/Range</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Will not transfer values</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**Target**<br>A range indicating where the value in From will be transferred to.</button>
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
		<td>Will Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**RequireValue**<br>True: [ReportDrill](/wIndex/ReportDrill.html) cannot be ran if the value in the From argument is blank.<br><br>False: ReportDrill can be ran if the value in the From argument is blank.</button>
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
		<td>True</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**ScopeRange**<br>**Deprecated**: This function for the current version of Interject performs the same no matter what value is entered in this argument.</button>
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
		<td>N/A</td>
    </tr>
  </tbody>
</table>
</div>

###  Excel Formula Bar Example

```Excel
=Pair(B22:B24,CustomerOrderHistory!C23)
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =Pair()  |  The name of this function.  |  
|  From  |  B22:B24  |  This function will transfer one cell value in B22:B24 to the Target. The particular cell it will transfer is determined by which cell is selected when the function is triggered. If the active cell is in row 22, then the value in B22 will be transferred.  |  
|  Target  |  CustomerOrderHistory!C23  |  The value in From will be transferred to cell C23 of the sheet "CustomerOrderHistory".  |  
|  RequireValue  |    |  Blank to indicate to not transfer blank cells.  |  
|  ScopeRange  |    |  **Deprecated**  |  

###  Usable In These Functions

* [PairGroup](PairGroup.html)
* [ReportDefaults](ReportDefaults.html)
* [ReportDrill](ReportDrill.html)
