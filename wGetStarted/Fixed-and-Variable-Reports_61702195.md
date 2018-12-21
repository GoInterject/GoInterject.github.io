---
title: Interject Documentation > Fixed and Variable Reports
layout: custom
---
* * *

##  **Overview**

This section demonstrates additional Report Formulas, [ ReportFixed() ](wIndex\ReportFixed_61702203.html) and [ ReportVariable() ](wIndex\ReportVariable_61702201.html) . Like ReportRange(), these are used for reporting but allow for special use cases. ReportFixed() provides for a report that is fixed on each row based on a Row Definition that you specify. If the returned record matches the Row Definition, the data is presented, but the report does not expand with new data records. The ReportVariable() function is a combination of ReportFixed() and ReportRange() which allow specific fixed sections to be set up. Within those sections, the data will expand or shrink based on the data result. 

###  [ Lab 3.1 Inventory Fixed ](/wGetStarted/L3.1-Inventory-Fixed_128429456.html)

This page illustrates the process of building a fixed inventory report from scratch using an example seen in the  [ Inventory Walk-through ](/wAbout/Inventory-Reports_128091499.html) . By creating this report from scratch, you can better understand how to use the [ ReportFixed() ](wIndex\ReportFixed_61702203.html) function. 

###  [ Lab 3.2 Inventory Variable Report ](/wGetStarted/L3.2-Inventory-Variable-Report_127872532.html)

Using the report seen in the [ Inventory Walk-through ](wAbout\Inventory-Reports_128091499.html) , this illustrates how ReportVariable() can provide all the data for each section in the report **Inventory By Category with Detail** . 

###  [ Lab 3.3 Financial Variable ](/wGetStarted/L3.3-Financial-Variable_128421724.html)

Using the report seen in the [ Financial Report - Walk-through ](/wAbout/Financial-Report_128091561.html) , this example will illustrate how to use a ReportVariable() in a financial statement use case. 

###  [ Lab 3.4 Customer Aging Detail ](/wGetStarted/L3.4-Customer-Aging-Detail_128429387.html)

This advanced example uses both the ReportRange() and ReportVariable() functions together to build an auto-expanding report that provides aging detail drilled to in the [ Customer Aging - Walk-through ](/wAbout/Customer-Aging_128091294.html) example. 
