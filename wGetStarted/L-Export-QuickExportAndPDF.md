---
title: Interject | Lab Quick Export and PDF
layout: custom
---
* * *

##  **Overview**

This method of distribution is the simplest. The purpose of Quick Export is to build a new workbook from the current workbook and remove all the external links and [ Data Cell ](/KB/HowItWorks/ListsVsCells.html) formulas so users without INTERJECT can view the report. It's important to note that [ Tabular ](/KB/HowItWorks/ListsVsCells.html) INTERJECT reports can be viewed immediately by users without INTERJECT and do not need to be exported to be shared. Although Tabular reports use special report formulas, the formulas remain out of view for users without INTERJECT, and any data pulled into the report are simply values. Outside users can view them without any modification. 

###  Quick Export 

Quick Export removes [ Data Cell ](/KB/HowItWorks/ListsVsCells.html) formulas and external links from a workbook so users without INTERJECT can view them. 

Take the report **PL Trend Report with Data Cells** from the [ Financial Walk-through ](/KB/HowToUse/Walkthroughs/Financial.html) as an example. It is shown below.   
![](https://interject.atlassian.net/wiki/download/attachments/128718475/image2017-7-12_15-6-33.png?version=1&modificationDate=1499897192843&cacheVersion=1&api=v2)

  


**Step 1:** First, use the [ **Pull Data** ](/KB/InterjectRibbon.html#InterjectRibbonMenuItems-PullData) operation to pull the report for Location 7002 and month 2002-05. 

![](https://interject.atlassian.net/wiki/download/attachments/128718475/image2017-7-20_16-1-54.png?version=1&modificationDate=1500591716268&cacheVersion=1&api=v2)

  


Now you have the report to distribute. However, if you send this report with data cells, people without INTERJECT will not be able to view all the Data Cell formulas like in cell K16 below. Without INTERJECT installed that formula will show as **#NAME** . 

![](https://interject.atlassian.net/wiki/download/attachments/128718475/image2017-7-12_16-9-36.png?version=1&modificationDate=1499900976073&cacheVersion=1&api=v2)

  


**Step 2:** To prevent this issue, you can use **[ Export Book ](/KB/InterjectRibbon.html#InterjectRibbonMenuItems-ExportBook) ** to create a new book and convert the data cell functions into regular values. 

![](https://interject.atlassian.net/wiki/download/attachments/128718475/image2017-7-20_16-9-19.png?version=1&modificationDate=1500592160481&cacheVersion=1&api=v2)

  


Once complete, the report will upload into a brand new workbook with fixed values instead of data cell formulas. This allows users without INTERJECT to view the report. 

![](https://interject.atlassian.net/wiki/download/attachments/128718475/image2017-7-12_16-29-12.png?version=1&modificationDate=1499902151611&cacheVersion=1&api=v2)

  


###  Quick PDF 

Exporting to PDFs from Excel has been available since Excel 2010 (and even with Excel 2007 accompanied by the download available  _ [ here ](http://www.microsoft.com/downloads/details.aspx?familyid=4d951911-3e7e-4ae6-b059-a2e79ed87041) _ ). You will select this option and choose a folder in which to save the PDF. After saving, the PDF will open for review. 

**Step 1:** Go back to the PL Trend with Data Cells from the previous section. You can again select [ **Export Book** , ](/KB/InterjectRibbon.html#InterjectRibbonMenuItems-ExportBook) but this time follow up with the **Quick PDF** button. 

** ![](https://interject.atlassian.net/wiki/download/attachments/128718475/image2017-8-9_9-27-41.png?version=1&modificationDate=1502296062664&cacheVersion=1&api=v2)   
**

  


**Step 2:** When you export to a PDF you will be required to declare a save location. 

** ![](https://interject.atlassian.net/wiki/download/attachments/128718475/image2017-7-12_16-33-30.png?version=1&modificationDate=1499902409967&cacheVersion=1&api=v2)   
**

  


**Step 3:** The PDF opens in the default browser. The published file should look like the one below. 

![](https://interject.atlassian.net/wiki/download/attachments/128718475/image2017-7-12_16-34-24.png?version=1&modificationDate=1499902463901&cacheVersion=1&api=v2)

  


You have completed exporting. Continue on to learn about the [ Basics of Distribution ](/KB/HowToCreate/ExportReport/Distributing.html) . 

  


**Next Step:** [ Basic Distribution ](/KB/HowToCreate/ExportReport/Distributing.html)

  


##  Related Links: 

[ Inventory Reports ](/KB/HowToUse/Walkthroughs/Inventory.html)

[ Tabular vs Data Cells ](/KB/HowItWorks/ListsVsCells.html)

[ INTERJECT Ribbon Menu Items ](/KB/InterjectRibbon.html)

[ L11.2 Basic Distribution ](/KB/HowToCreate/ExportReport/Distributing.html)
