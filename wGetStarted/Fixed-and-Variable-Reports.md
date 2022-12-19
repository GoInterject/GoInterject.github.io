---
title: Fixed and Variable Reports
layout: custom
keywords: [ variable, fixed, report, tutorial, example, walk-through ]
description: How to use fixed and variable data functions.
---

##  **Overview**

This section demonstrates additional Report Formulas, [ ReportFixed() ](/wIndex/ReportFixed.html) and [ ReportVariable() ](/wIndex/ReportVariable.html). Like ReportRange(), these are used for reporting but allow for special use cases. ReportFixed() provides for a report that is fixed on each row based on a Row Definition that you specify. If the returned record matches the Row Definition, the data is presented, but the report does not expand with new data records. The ReportVariable() function is a combination of ReportFixed() and ReportRange() which allow specific fixed sections to be set up. Within those sections, the data will expand or shrink based on the data result. 

###  [ Lab Create: Inventory Fixed ](/wGetStarted/L-Create-InventoryFixed.html)

This page illustrates the process of building a fixed inventory report from scratch using an example seen in the  [ Inventory Walk-through ](/wAbout/Inventory-Reports.html). By creating this report from scratch, you can better understand how to use the [ ReportFixed() ](/wIndex/ReportFixed.html) function. 

###  [ Lab Create: Inventory Variable Report ](/wGetStarted/L-Create-InventoryVariable.html)

Using the report seen in the [ Inventory Walk-through ](/wAbout/Inventory-Reports.html), this illustrates how ReportVariable() can provide all the data for each section in the report **Inventory By Category with Detail**. 

###  [ Lab Create: Financial Variable ](/wGetStarted/L-Create-FinancialVariable.html)

Using the report seen in the [ Financial Report - Walk-through ](/wAbout/Financial-Report.html), this example will illustrate how to use a ReportVariable() in a financial statement use case.

###  [ Lab Create: Customer Aging Detail ](/wGetStarted/L-Create-CustomerAgingDetail.html)

This advanced example uses both the ReportRange() and ReportVariable() functions together to build an auto-expanding report that provides aging detail drilled to in the [ Customer Aging - Walk-through ](/wAbout/Customer-Aging.html) example. 
