---
title: "Lab Export: Quick Export and PDF"
layout: custom
keywords: [ quick, export, pdf, data cells]
description: This method of distribution is the simplest. The purpose of Quick Export is to build a new workbook from the current workbook and remove all the external links and Data Cell formulas so users without INTERJECT can view the report.
---
* * *

##  **Overview**

This method of distribution is the simplest. The purpose of Quick Export is to build a new workbook from the current workbook and remove all the external links and [ Data Cell ](/wAbout/Tabular-vs-Data-Cells.html) formulas so users without INTERJECT can view the report. It's important to note that [ Tabular ](/wAbout/Tabular-vs-Data-Cells.html) INTERJECT reports can be viewed immediately by users without INTERJECT and do not need to be exported to be shared. Although Tabular reports use special report formulas, the formulas remain out of view for users without INTERJECT, and any data pulled into the report are simply values. Outside users can view them without any modification. 

###  Quick Export 

Quick Export removes [ Data Cell ](/wAbout/Tabular-vs-Data-Cells.html) formulas and external links from a workbook so users without INTERJECT can view them. 

Take the report **PL Trend Report with Data Cells** from the [ Financial Walk-through ](/wAbout/Financial-Reports.html) as an example. It is shown below.

![](/images/L-Export-QuickExPDF/01.png)

<br> 

**Step 1:** First, use the [**Pull Data**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) operation to pull the report for Location 7002 and month 2002-05.

![](/images/L-Export-QuickExPDF/02.png)

<br> 

Now you have the report to distribute. However, if you send this report with data cells, people without INTERJECT will not be able to view all the Data Cell formulas like in cell K16 below. Without INTERJECT installed that formula will show as **#NAME**. 

![](/images/L-Export-QuickExPDF/03.png)

<br> 

**Step 2:** To prevent this issue, you can use [ Export Book ](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#export-book) to create a new book and convert the data cell functions into regular values. 

![](/images/L-Export-QuickExPDF/04.png)

<br> 

Once complete, the report will upload into a brand new workbook with fixed values instead of data cell formulas. This allows users without INTERJECT to view the report. 

![](/images/L-Export-QuickExPDF/05.png)

<br> 

###  Quick PDF 

Exporting to PDFs from Excel has been available since Excel 2010 (and even with Excel 2007 accompanied by the download available [ here ](http://www.microsoft.com/downloads/details.aspx?familyid=4d951911-3e7e-4ae6-b059-a2e79ed87041)). You will select this option and choose a folder in which to save the PDF. After saving, the PDF will open for review. 

**Step 1:** Go back to the PL Trend with Data Cells from the previous section. You can again select [ **Export Book**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#export-book), but this time follow up with the **Quick PDF** button. 

![](/images/L-Export-QuickExPDF/06.png)   

<br> 

**Step 2:** When you export to a PDF you will be required to declare a save location. 

![](/images/L-Export-QuickExPDF/07.png)   

<br> 

**Step 3:** The PDF opens in the default browser. The published file should look like the one below. 

![](/images/L-Export-QuickExPDF/08.png)

<br> 

You have completed the quick exporting section. Continue on to learn about the [ Basics of Distribution ](/wGetStarted/L-Export-BasicDist.html). 
