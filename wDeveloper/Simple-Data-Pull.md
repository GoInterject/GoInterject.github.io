---
title: Simple Data Pull
filename: "Simple-Data-Pull.md"
layout: custom
keywords: [data, pull, develop, build, create, jdropdown]
headings: ["Overview", "Understanding the Business Use Case", "Customer Aging", "Customer Orders", "jDropdowns"]
links: ["/wAbout/Customer-Aging.html", "/wDeveloper/L-Dev-CustomerAging.html", "/wAbout/Customer-Aging.html", "/wDeveloper/L-Dev-CustomerOrders.html", "/wGetStarted/L-Create-CustomerOrders.html", "/wDeveloper/L-Dev-jDropdowns.html"]
image_dir: ""
images: []
description: To clearly illustrate the end-to-end workflow of developing a report, you can begin with several simple data pull examples showing different report configurations. You will be reusing Interject reports used in previous sections, because these should be familiar to you if you read this documentation from the beginning.
---
* * *

## Overview

To clearly illustrate the end-to-end workflow of developing a report, you can begin with several simple data pull examples showing different report configurations. You will be reusing Interject reports used in previous sections, because these should be familiar to you if you read this documentation from the beginning. By the end of these sections, you will understand the process of creating spreadsheet friendly reports that can drill to other reports.

### Understanding the Business Use Case

To understand the business use case for the reports and drills used in this section, please review, [Real-World Walkthroughs - Customer Aging](/wAbout/Customer-Aging.html). It shows a user story for the Customer Aging Report and why users would want to drill to underlying reports like Customer Orders and Aging Detail.

Go directly to the following examples to begin each objective. It is ideal to complete the following examples in order.

### [Customer Aging](/wDeveloper/L-Dev-CustomerAging.html)

Customer Aging, you will learn how to create a simple data pull using the Customer Aging Report. To review the business use case for this report, see the [Real World Walkthroughs - Customer Aging](/wAbout/Customer-Aging.html). This section begins with the steps for creating the Interject data connection and data portals, followed by the steps on how to create the stored procedure. Finally, you will be directed to another page that shows how to use the data portal to create the spreadsheet report from scratch.

### [Customer Orders](/wDeveloper/L-Dev-CustomerOrders.html)

Customer Orders, you show you how to create a second report, Customer Orders, that will be drilled to from the Customer Aging Report. You should have already seen the Customer Orders report while reviewing the business use case in [Create: Customer Orders](/wGetStarted/L-Create-CustomerOrders.html). Continue to build the Interject configuration and database objects to support the report.

### [jDropdowns](/wDeveloper/L-Dev-jDropdowns.html)

This example will walk you through building a custom jDropdown stored procedure for your reports. You will walk through how to build the Data Connection, Data Portal, and stored procedure for the jDropdown example built on the Customer Aging report. This stored procedure is designed to filter down on the specific options for a parameter. Include all the columns that can be used as filter values in the report.
