---
title: Fixed and Variable Reports
filename: "Fixed-and-Variable-Reports.md"
layout: custom
keywords: [variable, fixed, variable, reports, walkthroughs]
headings: ["Overview", "Inventory Fixed Report", "Inventory Variable Report", "Financial Variable Report", "Customer Aging Detail Report"]
links: ["/wFunctions/ReportFixed.html", "/wFunctions/ReportVariable.html", "/wGetStarted/L-Create-InventoryFixed.html", "/wAbout/Inventory-Reports.html", "/wFunctions/ReportFixed.html", "/wGetStarted/L-Create-InventoryVariable.html", "/wAbout/Inventory-Reports.html", "/wGetStarted/L-Create-FinancialVariable.html", "/wAbout/Financial-Report.html", "/wGetStarted/L-Create-CustomerAgingDetail.html", "/wAbout/Customer-Aging.html"]
image_dir: ""
images: []
description: This section demonstrates additional Report Formulas such as ReportFixed and ReportVariable. 
---
* * *

##  Overview

This section demonstrates additional Report Formulas, [ReportFixed()](/wFunctions/ReportFixed.html) and [ReportVariable()](/wFunctions/ReportVariable.html). Like ReportRange(), these are used for reporting but allow for special use cases. ReportFixed() provides for a report that is fixed on each row based on a Row Definition that you specify. If the returned record matches the Row Definition, the data is presented, but the report does not expand with new data records. The ReportVariable() function is a combination of ReportFixed() and ReportRange() which allow specific fixed sections to be set up. Within those sections, the data will expand or shrink based on the data result. 

### [Inventory Fixed Report](/wGetStarted/L-Create-InventoryFixed.html)

This page illustrates the process of building a fixed inventory report from scratch using an example seen in the [Inventory Walkthrough](/wAbout/Inventory-Reports.html). By creating this report from scratch, you can better understand how to use the [ReportFixed()](/wFunctions/ReportFixed.html) function. 

### [Inventory Variable Report](/wGetStarted/L-Create-InventoryVariable.html)

Using the report seen in the [Inventory Walkthrough](/wAbout/Inventory-Reports.html), this illustrates how ReportVariable() can provide all the data for each section in the report **Inventory By Category with Detail**. 

### [Financial Variable Report](/wGetStarted/L-Create-FinancialVariable.html)

Using the report seen in the [Financial Report - Walkthrough](/wAbout/Financial-Report.html), this example will illustrate how to use a ReportVariable() in a financial statement use case.

### [Customer Aging Detail Report](/wGetStarted/L-Create-CustomerAgingDetail.html)

This advanced example uses both the ReportRange() and ReportVariable() functions together to build an auto-expanding report that provides aging detail drilled to in the [Customer Aging - Walkthrough](/wAbout/Customer-Aging.html) example. 
