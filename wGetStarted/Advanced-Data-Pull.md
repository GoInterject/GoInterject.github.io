---
title: Advanced Data Pull
layout: custom
keywords: [pull, advanced, walkthrough, example]
description: INTERJECT reports can handle a wide variety of complex reports. Up to this point you have seen simple reports where a single recordset is returned to single area of the spreadsheet. This topic will share advanced reporting configurations that use multiple recordsets and multiple INTERJECT report formulas and supporting functions to construct advanced presentations. 
---

##  Overview 

INTERJECT reports can handle a wide variety of complex reports. Up to this point you have seen simple reports where a single recordset is returned to single area of the spreadsheet. This topic will share advanced reporting configurations that use multiple recordsets and multiple INTERJECT report formulas and supporting functions to construct advanced presentations. 

###  Understanding The Business Use Case 

In the below instructions it will be helpful to understand the business use case for the reports examples used. Please review the lab, [ **Real-World Walkthroughs - Customer Aging** ](/wAbout/Customer-Aging.html). 

You will learn the user story for the Customer Aging Report and why users would drill to underlying reports like Customer Orders and Customer Aging Detail. The example below will be focusing on the Customer Aging Detail report. 

Be sure to complete the simple data pull lab that preceded this topic before moving forward. 

###  [ Lab Dev: Customer Aging Detail ](/wGetStarted/L-Dev-CustomerAgingDetail.html)

In this example, you will learn to create a third report, Customer Aging Detail, that will be drilled to from the Customer Aging Report. This report shows a customer's outstanding balance by individual invoice. The Aging Detail is a more complex report than shown in the earlier lab [ Lab Developer: Customer Orders ](/wGetStarted/L-Dev-CustomerOrders.html), because it leverages two report formulas to create a report with subtotals. You should have already seen the Customer Aging Detail report while reviewing the business use case in the [ **Customer Aging in Real-World Walkthroughs** ](/wAbout/Customer-Aging.html). 