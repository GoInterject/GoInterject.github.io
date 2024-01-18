---
title: Creating with Interject
filename: "Creating-with-INTERJECT.md"
layout: custom
keywords: [create, modify, reports, walkthroughs]
headings: ["Overview", "Modifying an Existing Report", "Creating a Simple Report", "Fixed and Variable Reports", "Drilling Between Reports", "Hiding Rows & Columns", "Building jDropdowns", "Working with Pivot Tables", "Special Column Definitions", "Protecting Sheets", "Using Report Macro", "Using the Retained Feature", "Interject Run On Open", "Exporting Reports"]
links: ["mailto:help@gointerject.com", "https://docs.gointerject.com/wLabs/lab.html", "/wGetStarted/Modifying-an-Existing-Report.html", "/wGetStarted/L-Modify-CustomerAging.html", "/wGetStarted/L-Modify-InventoryReport.html", "/wGetStarted/L-Modify-FinancialReport.html", "/wGetStarted/Creating-a-Simple-Report.html", "/wGetStarted/L-Create-CustomerAging.html", "/wGetStarted/L-Create-CustomerOrders.html", "/wGetStarted/Fixed-and-Variable-Reports.html", "/wGetStarted/L-Modify-InventoryReport.html", "/wGetStarted/L-Modify-FinancialReport.html", "/wGetStarted/L-Drill-CustomerAging.html", "/wGetStarted/Drilling-Between-Reports.html", "/wGetStarted/L-Drill-CustomerAging.html", "/wGetStarted/L-Drill-InventoryReport.html", "/wGetStarted/L-Drill-FinancialReport.html", "/wGetStarted/L-Drill-DrillCodes.html", "/wGetStarted/L-Drill-TheThreeWays.html", "/wGetStarted/L-Create-HideRowCol.html", "/wGetStarted/L-Create-Dropdowns.html", "/wGetStarted/L-Create-PivotTable.html", "/wGetStarted/L-Create-SpecColDefs.html", "/wGetStarted/L-Create-Protecting.html", "/wGetStarted/L-Create-ReportMacro.html", "/wGetStarted/L-Create-RetainFeature.html", "/wGetStarted/L-Create-RunOnOpen.html", "/wGetStarted/Exporting-Reports.html"]
description: This section is for report writers who need to create or modify reports. You will run through basic modification, creation, and publishing of reports.
---
* * *

##  Overview

This section is for report writers who need to create or modify reports. You will run through basic modification, creation, and publishing of reports. Feel free to [contact](mailto:help@gointerject.com) us if you cannot find your answer in these sections. 

<blockquote class=lab_info>

A <a href="https://docs.gointerject.com/wLabs/lab.html">Lab Guide</a> is offered to guide you through learning about the Interject features step-by-step. As you work through the labs, you will see this blue banner on documentation pages that lead you to the correct file for that particular page. If you are new to the Interject Add-In, these labs are a great place to start!
</blockquote>

### [Modifying an Existing Report](/wGetStarted/Modifying-an-Existing-Report.html)

Reporting needs change often. Account details, specific formatting, even spreadsheet formulas require modification, that is why Interject's reports are so highly customizable using familiar spreadsheet knowledge. This section walks through common report modifications using [Customer Aging](/wGetStarted/L-Modify-CustomerAging.html), [Inventory](/wGetStarted/L-Modify-InventoryReport.html), and [Financial](/wGetStarted/L-Modify-FinancialReport.html) reports as an example. 

### [Creating a Simple Report](/wGetStarted/Creating-a-Simple-Report.html)

This section details how to create reports from scratch. Here, you will walk through making a [Customer Aging](/wGetStarted/L-Create-CustomerAging.html) and [Customer Orders](/wGetStarted/L-Create-CustomerOrders.html) report from the ground up. The focus is on using simple single range tabular reports. 

### [Fixed and Variable Reports](/wGetStarted/Fixed-and-Variable-Reports.html)

Reports often require various formats and subtotal sections, and this is especially true for financial reports. This section goes through several, more advanced report examples: [Inventory](/wGetStarted/L-Modify-InventoryReport.html), [Financial](/wGetStarted/L-Modify-FinancialReport.html) and [Customer Aging Detail](/wGetStarted/L-Drill-CustomerAging.html). These will illustrate how Interject provides a number of options for your reporting needs. 

### [Drilling Between Reports](/wGetStarted/Drilling-Between-Reports.html)

Creating drills, it is possible to generate a simple suite of reports that enable you and your end-users to navigate anywhere from within the spreadsheet environment. Examples in this section include building drills in a [Customer Aging](/wGetStarted/L-Drill-CustomerAging.html), [Inventory](/wGetStarted/L-Drill-InventoryReport.html), and [Financial report](/wGetStarted/L-Drill-FinancialReport.html). Also included is [drilling to a separate workbook](/wGetStarted/L-Drill-DrillCodes.html). There is more than one way for the user to interact with the drill feature. See the page [Three Ways to Drill](/wGetStarted/L-Drill-TheThreeWays.html) for more details.

### [Hiding Rows & Columns](/wGetStarted/L-Create-HideRowCol.html)

ReportHideRowsOrColumns() is a function that allows you to hide both rows and columns when not needed. In this example, you will begin with hiding columns L, M, N, and O. To practice there is a file below that has been specifically prepared for this formula. 

### [Building jDropdowns](/wGetStarted/L-Create-Dropdowns.html)

When manually entering different filter values, it can be difficult to remember what the exact filter names are and which are even available. This is especially true in large reports with many filtering options. However, you can use Interject’s jDropdown formula to automatically create hyperlinked lists of available filters, which makes filtering in large reports a much simpler task. 

### [Working with Pivot Tables](/wGetStarted/L-Create-PivotTable.html)

Pivot tables are excellent tools to help us find answers quickly. Interject can help simplify pivot table presentation and distribution. 

### [Special Column Definitions](/wGetStarted/L-Create-SpecColDefs.html)

Special Column Definitions are optional tags that bring out additional features to your standard column definition rows. They are great for space savers or to allow for faster formatting of the Pulled data. 

### [Protecting Sheets](/wGetStarted/L-Create-Protecting.html)

Sheet Protection expands upon the already existing protection functions in excel but brings with it the Interject UI and security rights. 

To use it, navigate to the Interject ribbon and click on the  **Sheet Protector** button in the  **Tools** section. 

### [Using Report Macro](/wGetStarted/L-Create-ReportMacro.html)

The Report Macro function allows Interject to interact with public macros in Excel. These macros can be automatically run after pulling or clearning data.

### [Using the Retained Feature](/wGetStarted/L-Create-RetainFeature.html)

When using Interject to pull data into your spreadsheet, the report area will be cleared before new data is inserted. In some situations, you may want to bypass the clear action and retain some formulas, since pulling could remove formulas you have on other columns related to certain data rows.


### [Interject Run On Open](/wGetStarted/L-Create-RunOnOpen.html)

Some reports require default values, settings, or have summary pages that must be pulled before others in order for the report to function properly. Using the Run on Open Interject property will auto-run the first tab that appears. 

### [Exporting Reports](/wGetStarted/Exporting-Reports.html)

Interject reports can be published or exported when needed. In most situations, Interject reports are shared like a web page, where all end users have access but can only see cost centers they have rights to. Still, there are times when reports must be saved to file folders or emailed, and this section walks through the specifics of distribution and all the available methods. 
