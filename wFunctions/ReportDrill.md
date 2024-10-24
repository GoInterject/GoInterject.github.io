---
title: ReportDrill()
filename: "ReportDrill.md"
layout: custom
keywords: [ReportDrill, drill, function, formula, data]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Embeddable Helper Functions"]
links: ["/wGetStarted/L-Drill-DrillCodes.html", "/wGetStarted/L-Drill-CustomerAging.html", "/wFunctions/Data-Functions-Landing.html", "/wGetStarted/L-Drill-DrillCodes.html", "/wFunctions/Pair.html", "https://docs.gointerject.com/wFunctions/Pair.html", "https://docs.gointerject.com/wFunctions/PairGroup.html", "/wFunctions/PairGroup.html", "/wFunctions/Pair.html"]
image_dir: ""
images: []
description: The ReportDrill function provides a convenient way to run another targeted function while at the same time, transferring contextual data for filtering to that function.
---
* * *

##  Function Summary

The ReportDrill function provides a convenient way to run another targeted function while at the same time, transferring contextual data for filtering to that function. It is widely used as a way to connect and pass information between workbooks and worksheets. Drilling takes a defined input and passes it in as a parameter to another workbook or worksheet, similar to hyperlinks on a web page. Depending on the types of input behind the hyperlink, more detailed and specific information can be viewed. The ReportDrill function can be structured in ways that make drilling data very powerful.

In order to set up a drill that targets a function in another workbook, it is necessary to set up a drill code in the [Report Library](/wGetStarted/L-Drill-DrillCodes.html).

For an example of this function, see [Lab Drill: Customer Aging](/wGetStarted/L-Drill-CustomerAging.html).

###  Function Arguments

<button class="collapsible-parameter">**ReportCellToRun**<br>A cell address in a worksheet within your report that contains an Interject [Data Pull Function](/wFunctions/Data-Functions-Landing.html). The Data Pull Functions of the sheet of this range will be ran upon a Drill action. (This parameter will be ignored if <b>ReportCodeToRun</b> is not blank)</button>
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
		<td>Uses cell reference in ReportCodeToRun</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**ReportCodeToRun**<br>The name of the drill code that has been set up in the [Report Library](/wGetStarted/L-Drill-DrillCodes.html) that allows you to drill between workbooks.</button>
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
		<td>Uses cell reference in ReportCellToRun</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**TransferPairs**<br>A Pair or a PairGroup that contains a list of [Pairs](/wFunctions/Pair.html). The Pair function transfers values from one cell to another. This is typically used to filter the data you are drilling. This function will transfer the value in the Pair range (determined by the active cell you are drilling) to the target cell.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td><a href="https://docs.gointerject.com/wFunctions/Pair.html">Pair()</a>/<a href="https://docs.gointerject.com/wFunctions/PairGroup.html">PairGroup()</a></td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 34 Pairs</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Does not transfer anything</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**DrillName**<br>The name of this drill as will be displayed in the list of data drills.</button>
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
		<td>Uses the ReportCellToRun/ReportCodeToRun as the name</td>
    </tr>
  </tbody>
</table>
</div>

###  Excel Formula Bar Example

```Excel
=ReportDrill(CustomerOrderHistory!C10,,PairGroup(Pair(B22:B24, CustomerOrderHistory!C23)),"Drill to Customer Orders History")
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =ReportDrill()  |  The name of this function.  |  
|  ReportCellToRun  |  CustomerOrderHistory!C10  |  The Data Pull Functions within sheet "CustomerOrderHistory" will be ran upon a Drill action.  |  
|  ReportCodeToRun  |  ""  |  Left blank because targeted function is found in ReportCellToRun argument.  |  
|  TransferPairs  |  PairGroup(Pair(B22:B24, CustomerOrderHistory!C23))  |  When this drill is ran, will copy the value in B22:B24 (whatever row the active cell is on when the drill is ran) to the CustomerOrderHistory worksheet cell C23.  |  
|  DrillName  |  "Drill to Customer Orders History"  |  The drill name will appear as "Drill to Customer Orders History" inside the Data Drill window.  |  

###  Embeddable Helper Functions

* [PairGroup](/wFunctions/PairGroup.html)
* [Pair](/wFunctions/Pair.html)
