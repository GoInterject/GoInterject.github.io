---
title: Diagnostics - Find All Workbook Formulas
filename: "Diagnostics-FindAllFormulas.md"
layout: custom
keywords: [diagnostics, formulas, functions]
headings: ["Overview", "Text Formula", "Text All", "SQL Query", "XML"]
links: []
image_dir: "DiagnosticsFindAllFormulas"
images: [
    {file: "FindAllFormulas", type: "png", site: "Addin", cat: "Diagnostics", sub: "FindAllWorkbookFormulas", report: "", ribbon: "", config: ""}, 
    {file: "TextFormula", type: "png", site: "Addin", cat: "Diagnostics", sub: "FindAllWorkbookFormulas", report: "", ribbon: "", config: ""}, 
    {file: "TextAll", type: "png", site: "Addin", cat: "Diagnostics", sub: "FindAllWorkbookFormulas", report: "", ribbon: "", config: ""}, 
    {file: "SQLQuery", type: "png", site: "Addin", cat: "Diagnostics", sub: "FindAllWorkbookFormulas", report: "", ribbon: "", config: ""}, 
    {file: "SQLOutput", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
    {file: "XML", type: "png", site: "Addin", cat: "Diagnostics", sub: "FindAllWorkbookFormulas", report: "", ribbon: "", config: ""}
    ]
description: The Diagnostic command Find All Workbook Formulas will display information about every Interject formula in the active workbook. Depending on which line is first in the input field, it will output to several different formats.

---
* * *

## Overview

The Diagnostic command "Find All Workbook Formulas" will display information about every Interject formula in the active workbook. Depending on which line is first in the input field, it will output to several different formats.

![](/images/DiagnosticsFindAllFormulas/FindAllFormulas.png)
<br>


### Text Formula

Click on **Execute Selected Action** when "text_formula" is first in the input field and the **Results** will display information about all the Interject formulas used in the workbook:

![](/images/DiagnosticsFindAllFormulas/TextFormula.png)
<br>

### Text All

If the first input is "text_all", the results will be the same as "text_formula" but it will also display the Excel result of the function:

![](/images/DiagnosticsFindAllFormulas/TextAll.png)
<br>


### SQL Query

The "sql_query" will display SQL code that displays the formula information in a table form:

![](/images/DiagnosticsFindAllFormulas/SQLQuery.png)
<br>


![](/images/DiagnosticsFindAllFormulas/SQLOutput.png)
<br>

### XML

For an XML output, list "xml" in the first line of the input field:

![](/images/DiagnosticsFindAllFormulas/XML.png)
<br>

```
<root>
  <book Name="LabCreateCustomerAgingFinished.xlsx" LinkId="" Version="" LogUtcDate="2024-06-13 20:11:48.235">
    <sheet Name="NewReport_1" UsedRange="A1:L28" FormulaCount="3">
      <formula Address="C6" dp="NorthwindCustomersPull" code="=ReportRange(&quot;NorthwindCustomersPull&quot;,23:27,2:2,,Param(C17,C18,C19),TRUE,FALSE)" />
      <formula Address="F6" dp="" code="=jFreezePanes(A23,A16)" />
      <formula Address="H6" dp="" code="=jFocus(C17)" />
    </sheet>
    <sheet Name="Sheet1" UsedRange="A1" FormulaCount="0" />
  </book>
</root>
```