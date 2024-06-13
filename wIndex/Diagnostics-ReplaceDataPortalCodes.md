---
title: Diagnostics - Replace Data Portal Codes
filename: "Diagnostics-ReplaceDataPortalCodes.md"
layout: custom
keywords: []
headings: ["Overview"]
links: []
image_dir: "DiagnosticsReplaceDataPortalCodes"
images: [
    {file: "ReplaceDataPortalCodes", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
    {file: "Results", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}
]
]
description: 
---
* * *

## Overview

The Diagnostics "Replace Data Portal Codes" command will replace all data portal codes in the current active workbook. This makes it handy to replace only the codes that are currently in Interject formulas and not elsewhere.

![](/images/DiagnosticsReplaceDataPortalCodes/ReplaceDataPortalCodes.png)
<br>

Simply enter the codes to be changed in the input field (case sensitive):

![](/images/DiagnosticsReplaceDataPortalCodes/Results.png)
<br>

The **Results** field shows the output of the changes:

```bash
before:



wb: LabCreateCustomerAgingFinished.xlsx   2 Sheets   Link:                                           
    ws: NewReport_1 (4)      UsedRange:A1:L29
        cell: C6           =ReportRange("NorthwindCustomersPull",24:28,2:2,,Param(C18,C19,C20),TRUE,FALSE)
        cell: F6           =jFreezePanes(A24,A17)                            
        cell: H6           =jFocus(C18)                                      
        cell: C7           =ReportSave("NorthwindCustomersSave",25:29,3:3,,Param(C19,C20,C21),TRUE,FALSE)
    ws: Sheet1 (no formulas)      UsedRange:A1

DataPortalCodes:
    NorthwindCustomersPull
    NorthwindCustomersSave

after:



wb: LabCreateCustomerAgingFinished.xlsx   2 Sheets   Link:                                           
    ws: NewReport_1 (4)      UsedRange:A1:L29
        cell: C6           =ReportRange("Northwind_Customers_Pull",24:28,2:2,,Param(C18,C19,C20),TRUE,FALSE)
        cell: F6           =jFreezePanes(A24,A17)                            
        cell: H6           =jFocus(C18)                                      
        cell: C7           =ReportSave("Northwind_Customers_Save",25:29,3:3,,Param(C19,C20,C21),TRUE,FALSE)
    ws: Sheet1 (no formulas)      UsedRange:A1

DataPortalCodes:
    Northwind_Customers_Pull
    Northwind_Customers_Save

```