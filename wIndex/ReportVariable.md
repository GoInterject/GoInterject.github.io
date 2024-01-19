---
title: ReportVariable()
filename: "ReportVariable.md"
layout: custom
keywords: [ReportVariable, variable, function, formula, data, pull]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Embeddable Helper Functions"]
links: ["/wIndex/ReportFixed.html", "/wGetStarted/L-Create-InventoryVariable.html", "https://docs.gointerject.com/wIndex/jDataPortal.html", "https://docs.gointerject.com/wIndex/Param.html", "https://docs.gointerject.com/wTroubleshoot/Reports.html#validation-report-for-pullsave-events", "/wGetStarted/L-Create-RetainFeature.html", "https://docs.gointerject.com/wIndex/jCombine.html", "https://docs.gointerject.com/wIndex/jCombine_If.html", "/wIndex/jDataPortal.html", "Param.html", "/wIndex/jCombine.html", "/wIndex/jCombine_IF.html"]
image_dir: ""
description: The ReportVariable function pulls data from a data source and inserts it into a spreadsheet.
---
* * *

##  Function Summary

The ReportVariable function pulls data from a data source and inserts it into a spreadsheet. It is similar to the [ReportFixed](/wIndex/ReportFixed.html) function because it takes row names as input in addition to column names. Only data that is mapped to both these row and column names from the data source will be inserted. Consequently, the range where data is inserted is defined by the boundaries of the RowDefRange and the ColDefRange. Data returned by this function can be filtered, formatted, and customized for a specific desired report.

This function differs from the ReportFixed function in that it will group the data based on the values defined in the RowDefRange argument. The grouping feature allows the data to be collapsed and expanded by category. Note: Entries for each group must contain an empty row above in order to populated with data correctly.

For an example of this function, see [Lab Create: Inventory Variable](/wGetStarted/L-Create-InventoryVariable.html).

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

<button class="collapsible-parameter">**RowDefRange**<br>A single column range that contains the values that map to the RowDefName field of the data source. Each value in this range will be matched to the same value in the RowDefName of the data source. Only these values will be populated with data after a pull action.<br><br>If the data source does not have a column "RowDefName", this function will look for a column name defined in the column in the ColDefRange and the row defined here in RowDefRange. For example, if row 2 is defined in ColDefRange and column B is defined in RowDefRange, this function will look at the value in B2 to map the data to.<br><br>If there are records in the data source that are excluded in this range, the data from those columns will be included in a [leftover] section after a pull action.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>A single column range (not whole)</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Function Error</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**ColDefRange**<br>Column definition range: A single row designating the names of the columns of the data source. Only data from these columns will be inserted. Range cannot span multiple rows. Best practice is to use a range instead of whole rows.</button>
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

<button class="collapsible-parameter">**FormatRange**<br>The range designating the formatting style (e.g. font, color) for the inserted data. Inserted data will be formated using this range as a template. Formulas can also be included, which will be used for the inserted data.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>Range</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Must match the range dimensions defined in ColDefRange</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Uses the formatting in the first row defined in RowDefRange</td>
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

<button class="collapsible-parameter">**RetainRowColumns**<br>The list of column names that will be used as a key for retaining information within the inserted data range. This can be a comma delimited string or a cell reference of a single column name defined in ColDefRange. <br><br>All data in the column(s) matching the names in this argument will be retained after a clear or pull action. Consequently, such rows are also retained and not deleted. However, all data in columns that are not defined in this argument are blanked out after a clear action or overridden after a pull action.<br><br>This feature makes forecasting calculations to remain in the report instead of being cleared. For an example of this feature, see [Using the Retain Feature](/wGetStarted/L-Create-RetainFeature.html).</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String/<a href="https://docs.gointerject.com/wIndex/jCombine.html">jCombine()</a>/<a href="https://docs.gointerject.com/wIndex/jCombine_If.html">jCombine_If()</a></td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>All data within the TargetDataRange is cleared on a clear action</td>
    </tr>
  </tbody>
</table>
</div>

<button class="collapsible-parameter">**InsertNewRowsWithin**<br>True: If RetainRowsColumns is used, will insert new data in the TargetDataRange on a pull action by alphabetical order of the first key listed in RetainRowColumns. <br><br>False: Will insert new data below the already present data in the TargetDataRange on a pull action if valid columns are defined in RetainRowColumns.</button>
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

<button class="collapsible-parameter">**UseTopSpacerRow**<br>True: Inserts data starting on the second row defined in TargetDataRange. (Retains top row on a pull or clear action.)<br><br>False: Inserts data starting on the first row defined in TargetDataRange.</button>
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

<button class="collapsible-parameter">**PopulateDuplicateRowDefs**<br>True: Inserts data for each appearance of a RowDefItem in the sheet.<br><br>False: Will only populate the last instance of a duplicate RowDefItem.</button>
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

###  Excel Formula Bar Example

```Excel
=ReportVariable("NorthwindVariable",B18:B54,2:2,4:4,Param(I14,I15),,FALSE,FALSE)
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =ReportVariable()  |  The name of this function.  |  
|  DataPortal  |  "NorthwindVariable"  |  This function will use the "NorthwindVariable" DataPortal for the data source.  |  
|  RowDefRange  |  B18:B54  |  The names found in B18:B54 will be used to map to the column names found in row 2 (ColDefRange). Only data that intersects these names will be inserted on these rows. Data will be grouped by the names found in this range.  |  
|  ColDefRange  |  2:2  |  The names found in row 2 will be used to map to the row names found in row B14:B27 (RowDefRange). Only data that intersects these names will be inserted on these columns.  |  
|  Format Range  | 4:4 |  The formatting used in row 4 will be used as a template for the inserted data.  |  
|  Parameters  |  Param(I14,I15)  |  Cells I14 and I15 will correspond to the parameters in the data source to filter the inserted data.  |  
|  RetainRowColumns  |  ""  |  Left blank to indicate not to retain any data in the TargetDataRange (B14:H15).  |  
|  InsertNewRowsWithin  |  FALSE  |  This value is automatically set to false since RetainRowColumns is blank.  |  
|  UseTopSpacerRow  |  FALSE  |  Data will be inserted on the first row (18) defined in RowDataRange.  |  
| PopulateDuplicateRowDefs | "" | Left blank to indicate to display duplicate RowDefItems |

###  Embeddable Helper Functions

* [jDataPortal](/wIndex/jDataPortal.html)
* [Param](Param.html)
* [jCombine](/wIndex/jCombine.html)
* [jCombineIF](/wIndex/jCombine_IF.html)
