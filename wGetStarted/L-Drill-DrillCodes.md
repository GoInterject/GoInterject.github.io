---
title: "Drill: Drilling to a Separate Workbook"
filename: "L-Drill-DrillCodes.md"
layout: custom
keywords: [data drill codes, report library, report]
headings: ["Overview", "Opening the Report and Drilling", "Uploading the Report With a Drill Code", "Adding the Drill Code to the ReportDrill Function", "Running the Drill"]
links: ["/wGetStarted/Drilling-Between-Reports.html", "/wAbout/Report-Library-Basics.html", "/wGetStarted/L-Drill-CustomerAging.html", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data", "/wAbout/ReportLibraryLinks.html", "/wIndex/ReportDrill.html", "/wIndex/QuickTools-Panes.html#freezeunfreeze-panes"]
image_dir: "L-Drill-DrillCodes"
description: Interject also gives its users the flexibility in drilling data not only to a different sheet within Excel but a separate workbook altogether. 
---
* * *

## Overview

Interject makes it easy to set up the report drill feature discussed in the section [Drilling Between Reports](/wGetStarted/Drilling-Between-Reports.html). Interject also gives its users the flexibility in drilling data not only to a different sheet within Excel but a separate workbook altogether. Interject achieves this functionality by the use of Data Drill Codes that are set up in the [Report Library](/wAbout/Report-Library-Basics.html). 

Drill Codes are needed when a drill needs to go to a separate workbook, and that workbook is saved in the Report Library. You can add Drill Codes to a report by adding them to the Report Link Details window, as seen below. The Drill Codes must be unique to others that were saved prior. A report can have up to three drill codes, each pointing to different worksheet tabs. More are allowed, but you must contact Interject for assistance.

![](/images/L-Drill-DrillCodes/DrillCodes.png)
<br>

<blockquote class=lab_info>
If you are following the Training Labs, this report file can be found in the Report Library at Training Labs > Lab 4 Drilling To Data > Lab 4.4 Drilling to a Separate Workbook.
</blockquote>

### Opening the Report and Drilling

For this walkthrough, you will be using the same report you setup the original drill for in [Drill: Customer Aging Report](/wGetStarted/L-Drill-CustomerAging.html). To get a sense of the original drill again, you will perform a drill to a different sheet within the same report.

**Step 1:** Begin by opening the Report Library and opening the report **Interject Customer Collections**.

![](/images/L-Drill-DrillCodes/CustomerCollections.png)
<br>

**Step 2:** Enter **Market** for the Company Name and **Pull Data**.

![](/images/L-Drill-DrillCodes/FilterAndPull.png)
<br>

**Step 3:** Next select the **Bottom-Dollar Markets** and click **Drill on Data**.

![](/images/L-Drill-DrillCodes/DrillData.png)
<br>

Select **Drill to Aging Detail** and then **Do Drill**.

![](/images/L-Drill-DrillCodes/DoDrill.png)
<br>

The drill is completed and generates the report in the **CustomerAgingDetail** sheet.

![](/images/L-Drill-DrillCodes/CustomerAgingDetailDrill.png)
<br>

[Clear the data](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) and switch back to the **CustomerAging** sheet.

### Uploading the Report With a Drill Code

In order to drill to a separate workbook, you must first upload the targeted workbook to the Report Library. For instructions on how to upload a report, see [Report Library Links](/wAbout/ReportLibraryLinks.html).

**Step 1:** Begin by first saving the report locally (be sure to use a different name than the original). Next open the Report Library up and select the **My Favorites** folder.

![](/images/L-Drill-DrillCodes/ReportLibrary.png)
<br>

**Step 2:** Right click in the **Report Links** section and click **Save Current Workbook** and then **Create New Link**.

![](/images/L-Drill-DrillCodes/CreateNewLink.png)
<br>

**Step 3:** In the **Create New Link** form, enter the following details:

* Link Name: TargetReportForDrill
* Status: Live
* Data Drill Code: TargetDataDrillCode
* Target Tab Name: CustomerAgingDetail
* Report Cell: \<Leave blank to run the whole sheet\>

![](/images/L-Drill-DrillCodes/CreateNewLinkDetails.png)
<br>

The Data Drill Code is a unique code that will "point" to this workbook in the Report Library. When a [ReportDrill](/wIndex/ReportDrill.html) function is set up with this code, Interject will open the corresponding workbook in the Library with the same code. The **Target Tab** tells Interject to open the workbook to this tab. If a cell reference is listed in **Report Cell**, it will run the Interject function found there. If this field is left blank, it will simply run the entire sheet.

Close the file before proceeding to the next section.

### Adding the Drill Code to the ReportDrill Function

In this section you will open up the original report and edit it so that it can drill to the report you just uploaded using the Drill Code.

**Step 1:** Open up the original **Interject Customer Collections** report again via the Report Library as you did in the [beginning](#opening-the-report-and-drilling).

**Step 2:** You will need to access the configuration section of the report. Begin by [unfreezing](/wIndex/QuickTools-Panes.html#freezeunfreeze-panes) the panes by selecting **PANES: Freeze/Unfreeze Panes** from the **Quick Tools** menu.

![](/images/L-Drill-DrillCodes/Unfreeze.png)
<br>

**Step 3:** Select the cell that contains the ReportDrill function for the **Customer Aging Detail** and click the **fx** button to edit the function.

![](/images/L-Drill-DrillCodes/EditDrillFunction.png)
<br>

**Step 4:** For the **ReportCodeToRun** enter **TargetDataDrillCode**.

![](/images/L-Drill-DrillCodes/FunctionArguments.png)
<br>

### Running the Drill

All there is left to do is run the drill!

Select the **Bottom-Dollar Markets** and click **Drill on Data**. Click **OK**.

![](/images/L-Drill-DrillCodes/DrillData.png)
<br>

Select **Drill to Aging Detail** and then **Do Drill**.

![](/images/L-Drill-DrillCodes/DoDrill.png)
<br>

This time notice a separate workbook, the one you uploaded, is opened and the drill performed!

![](/images/L-Drill-DrillCodes/SeperateWorkbook.png)
<br>

