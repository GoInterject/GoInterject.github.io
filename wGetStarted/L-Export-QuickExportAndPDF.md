---
title: "Export: Workbook, Sheet, and PDF"
filename: "L-Export-QuickExportAndPDF.md"
layout: custom
keywords: [quick, export, PDF, publish, distribute, data cells, walkthrough]
headings: ["Overview", "Export Workbook", "Export Sheet", "Quick PDF"]
links: ["/wAbout/Tabular-vs-Data-Cells.html", "/wAbout/Tabular-vs-Data-Cells.html", "/wAbout/Financial-Report.html", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#export-book", "/wFunctions/jRangeTag.html", "https://learn.microsoft.com/en-us/troubleshoot/dynamics/gp/have-microsoft-save-pdf-xps-add-in", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#export-book", "/wGetStarted/L-Export-BasicDist.html"]
image_dir: "L-Export-QuickExPDF"
images: [
	{file: "01", type: "png", site: "Add-in", cat: "Report", sub: "", report: "PL Trend Report", ribbon: "", config: ""}, 
	{file: "02", type: "png", site: "Add-in", cat: "Pull Data", sub: "", report: "PL Trend Report", ribbon: "Simple", config: ""}, 
	{file: "03", type: "png", site: "Add-in", cat: "Report", sub: "", report: "PL Trend Report", ribbon: "", config: ""}, 
	{file: "04", type: "png", site: "Add-in", cat: "Export And Distribution", sub: "", report: "PL Trend Report", ribbon: "Simple", config: ""}, 
	{file: "05", type: "png", site: "Add-in", cat: "Report", sub: "", report: "PL Trend Report", ribbon: "Simple", config: ""}, 
	{file: "ExportSheet", type: "png", site: "Add-in", cat: "Export And Distribution", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "OpenReport", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "Interject Customer Collections", ribbon: "", config: ""}, 
	{file: "PullData", type: "png", site: "Add-in", cat: "Pull Data", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""}, 
	{file: "jRangeTagItems", type: "png", site: "Add-in", cat: "Report", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "ExcludeCells", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""}, 
	{file: "ClickExportSheet", type: "png", site: "Add-in", cat: "Export And Distribution", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "ExportedSheet", type: "png", site: "Add-in", cat: "Report", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "06", type: "png", site: "Add-in", cat: "Export And Distribution", sub: "", report: "PL Trend Report", ribbon: "Simple", config: ""}, 
	{file: "07", type: "png", site: "Windows", cat: "Explorer", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "08", type: "png", site: "External", cat: "Browser", sub: "", report: "PL Trend Report", ribbon: "", config: ""}
	]
description: The Quick Export and PDF method is the simplest way of distributing. The purpose of Quick Export is to build a new workbook from the current workbook and remove all the external links and Data Cell formulas so users without Interject can view the report.
---
* * *

## Overview

The Export method is the simplest way of distributing. The purpose of Export is to build a new workbook, sheet, or PDF from the current workbook and remove all the external links and [Data Cell](/wAbout/Tabular-vs-Data-Cells.html) formulas so users without Interject can view the report. It's important to note that [Tabular](/wAbout/Tabular-vs-Data-Cells.html) Interject reports can be viewed immediately by users without Interject and do not need to be exported to be shared. Although Tabular reports use special report formulas, the formulas remain out of view for users without Interject, and any data pulled into the report are simply values. Outside users can view them without any modification.

<blockquote class=lab_info>
 If you are following the Training Labs, this report file can be found in the Report Library at Training Labs > Lab 7 Exporting Data > Lab 7.1 Quick Export and PDF.
</blockquote>

### Export Workbook

Interject features the option to export the workbook. This export process removes Data Cell formulas and external links from a sheet or workbook so users without Interject can view them.

Take the report **PL Trend Report with Data Cells** from the [Financial Walkthrough](/wAbout/Financial-Report.html) as an example. It is shown below.

![](/images/L-Export-QuickExPDF/01.png)
<br>

**Step 1:** First, use the [**Pull Data**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) operation to pull the report for Location 7002 and month 2002-05.

<blockquote class=highlight_note>
<b>Note:</b> Ensure that the <b>Calculate Data Cells</b> is checked.
</blockquote>
<br>

![](/images/L-Export-QuickExPDF/02.png)
<br>

Now you have the report to distribute. However, if you send this report with data cells, people without Interject will not be able to view all the Data Cell formulas like in cell K16 below. Without Interject installed that formula will show as **#NAME**.

![](/images/L-Export-QuickExPDF/03.png)
<br>

**Step 2:** To prevent this issue, you can use [Export Book](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#export-book) to create a new book and convert the data cell functions into regular values. Select Export Book and then Export Workbook.

![](/images/L-Export-QuickExPDF/04.png)
<br>

Once complete, the report will upload into a brand new workbook with fixed values instead of data cell formulas. This allows users without Interject to view the report.

![](/images/L-Export-QuickExPDF/05.png)
<br>

### Export Sheet

The Export Sheet option does everything the Export Workbook does but only exports the current sheet.

![](/images/L-Export-QuickExPDF/ExportSheet.png)
<br>

In addition, the Export Sheet features allows you additional options to customize what is exported. It does this by utilizing the [jRangeTag](/wFunctions/jRangeTag.html) to set three settings:

* **ExportSheetRange:** Specifies the range to be exported
* **ExportSheetExcludeColumnRange:** Specifies a range where if a cell has the value of "Exclude", that column will not be exported
* **ExportSheetExcludeRowRange:** Specifies a range where if a cell has the value of "Exclude", that row will not be exported

This feature is handy when you want to export a report's data, while excluding certain columns or rows.

**Step 1:** Open up the Interject Customer Collections report:

![](/images/L-Export-QuickExPDF/OpenReport.png)
<br>

**Step 2:** Enter "Market" for the **Company Name** filter and pull the data:

![](/images/L-Export-QuickExPDF/PullData.png)
<br>

**Step 3:** In cell G15, enter the following jRangeTag formula to specify you want to export only the data in the report:

```
=jRangeTag("ExportSheetRange", B21:L26)
```

In G16, enter the following to specify the range Interject will look for values of "Exclude" to exclude columns:

```
=jRangeTag("ExportSheetExcludeColumnRange", B20:L20)
```

In G17, enter the following to specify the range Interject will look for values of "Exclude" to exclude rows:

```
=jRangeTag("ExportSheetExcludeRowRange", A21:A26)
```

![](/images/L-Export-QuickExPDF/jRangeTagItems.png)
<br>

**Step 4:** Now to exclude certain columns and rows, enter "Exclude" in cells F20, G20, H20, and A23:

![](/images/L-Export-QuickExPDF/ExcludeCells.png)
<br>


**Step 5:** Lastly, export the sheet:

![](/images/L-Export-QuickExPDF/ClickExportSheet.png)
<br>

Another workbook is opened up with just the one sheet exported. The excluded columns and row do not appear in the exported sheet:

![](/images/L-Export-QuickExPDF/ExportedSheet.png)
<br>

### Quick PDF

Exporting to PDFs from Excel has been available since Excel 2010 (and even with Excel 2007 as explained [here](https://learn.microsoft.com/en-us/troubleshoot/dynamics/gp/have-microsoft-save-pdf-xps-add-in){:target="_blank"}{:rel="noopener noreferrer"}). You will select this option and choose a folder in which to save the PDF. After saving, the PDF will open for review.

**Step 1:** Go back to the PL Trend with Data Cells from the previous section. You can again select [**Export Book**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#export-book), but this time follow up with the **Quick PDF** button.

![](/images/L-Export-QuickExPDF/06.png)
<br>

**Step 2:** When you export to a PDF you will be required to declare a save location.

![](/images/L-Export-QuickExPDF/07.png)
<br>

**Step 3:** The PDF opens in the default browser. The published file should look like the one below.

![](/images/L-Export-QuickExPDF/08.png)
<br>

You have completed the quick exporting section. Continue on to learn about the [Basics of Distribution](/wGetStarted/L-Export-BasicDist.html).
