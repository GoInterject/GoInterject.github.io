---
title: PairGroup()
layout: custom
keywords: [PairGroup, function]
description: The PairGroup function will active all [Pair()](Pair.html) functions defined within.
---

##  Function Summary
The PairGroup function will active all [Pair()](Pair.html) functions defined within. It is best practice to use the PairGroup function even when only entering one Pair.

For an example of this function, see [Lab Drill: Customer Aging](/wGetStarted/L-Drill-CustomerAging.html).

###  Function Arguments

<button class="collapsible-parameter">**Pair**<br>The Pair function transfers values from one cell to another upon a designated action or event (e.g. a drill or as defined in the function it is embedded in). Multiple Pairs can be added separated by a comma.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td><a href="https://docs.gointerject.com/wIndex/Pair.html">Pair()</a></td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 34 Pairs</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>No Pair function will be activated</td>
    </tr>
  </tbody>
</table>
</div>


###  Excel Formula Bar Example

```Excel
=PairGroup(Pair("2002-05",M22),Pair(M21,"Segment2"),Pair(F26:F125,"Segment1"))
```



###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =PairGroup()  |  The name of this function.  |  
|  Pair1  |  Pair("2002-05",M22)  |  Will transfer the value "2002-05" into cell M22 upon action or event.  |  
|  Pair2  |  Pair(M21,"Segment2")  |  Will transfer the value in cell M21 to the cell labeled as "Segment2" upon action or event.  |  
|  Pair3  |  Pair(F26:F125,"Segment1")  |  Will transfer a single cell value from F26:F125 into the cell labeled as "Segment1" upon action or event.  |  

###  Usable In These Functions

* [PairGroup](PairGroup.html)
* [ReportDefaults](ReportDefaults.html)
* [ReportDrill](ReportDrill.html)
