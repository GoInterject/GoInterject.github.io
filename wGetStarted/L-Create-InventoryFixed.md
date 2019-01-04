---
title: Interject | Lab Inventory Fixed
layout: custom
---
* * *

##  **Overview**

In this page, you will go through the process of building a fixed Inventory report from scratch using the ReportFixed() function. 

###  Building the Report 

**Step 1:** Begin like you did when creating the Customer Aging report, with the Interject [ Report Builder ](/KB/InterjectRibbon.html#InterjectRibbonMenuItems-ReportBuilder) . It is where you select the  [ DataPortal ](/KB/CommonDataPortals.html) that is needed for this particular report. 

** ![](https://interject.atlassian.net/wiki/download/attachments/128429456/image2017-7-3_12-35-53.png?version=1&modificationDate=1499110554521&cacheVersion=1&api=v2) **

  


**Step 2:** For this Inventory report, choose the NorthwindFixed DataPortal and click **Build Report Formula** . 

** ![](https://interject.atlassian.net/wiki/download/attachments/128429456/image2017-6-21_15-0-5.png?version=1&modificationDate=1498082406344&cacheVersion=1&api=v2) **

**  
**

After the report is built, it will look like the one below. There are no parameters involved with this report, so none are listed after row 14. 

![](https://interject.atlassian.net/wiki/download/attachments/128429456/image2017-8-4_14-19-42.png?version=1&modificationDate=1501881583159&cacheVersion=1&api=v2)

  


Delete rows 11 through 24 since they are not needed for this lesson. The page should look as illustrated below. **  
** ![](https://interject.atlassian.net/wiki/download/thumbnails/128429456/image2017-7-3_14-4-7.png?version=1&modificationDate=1499115848408&cacheVersion=1&api=v2&width=696&height=543)

**  
**

**Step 3:** Because [ ReportRange() ](/KB/ExcelFunctions/ReportRange.html) is the most used pull function, the report builder builds one automatically. However, in this report you will be using the [ ReportFixed() ](/KB/ExcelFunctions/ReportDrill.html) function. Clear the ReportRange function in cell C6. 

** ![](https://interject.atlassian.net/wiki/download/thumbnails/128429456/image2017-7-3_14-10-52.png?version=1&modificationDate=1499116253002&cacheVersion=1&api=v2&width=744&height=538) **

  


In C6, type **=ReportFixed()** , then click the **fx** button to bring up the Function Wizard as shown below. 

** ![](https://interject.atlassian.net/wiki/download/thumbnails/128429456/image2017-7-3_14-16-33.png?version=1&modificationDate=1499116594406&cacheVersion=1&api=v2&width=854&height=693) **

  


**Step 4:** In order to bring in the correct data you will need to designate a Dataportal. The Dataportal for this example is **NorthwindFixed** . 

![](https://interject.atlassian.net/wiki/download/attachments/128429456/image2017-7-3_15-5-16.png?version=1&modificationDate=1499119517942&cacheVersion=1&api=v2)

**  
**

**Step 5:** A fixed report requires specific values to be entered in a row definition column. In the below example, the Dataportal is expecting the inventory categories typed in B14 to B21. In cell B25, you also added a **Leftovers** section that is a special INTERJECT feature, a Row Definition marking the start of a section that will include any data not matching the earlier fixed rows. This is helpful in ensuring all data is presented. 

![](https://interject.atlassian.net/wiki/download/attachments/128429456/image2017-8-4_14-4-8.png?version=1&modificationDate=1501880649910&cacheVersion=1&api=v2)

  


**Step 6:** In a [ ReportFixed ](/KB/ExcelFunctions/ReportFixed.html) function you need to define the Column Definition and Row Definition ranges. Using the Function Wizard, use B14:B26 for the  RowDefRange  . For Column Definitions, use row 2 by typing **2:2** in the ColDefRange argument. 

![](https://interject.atlassian.net/wiki/download/attachments/128429456/image2017-7-4_9-6-24.png?version=1&modificationDate=1499184385586&cacheVersion=1&api=v2)

  


**Step 7: N** ow define the Column Definitions that are available in the Dataportal. Type **ProductTypeCount** in G2 and **UnitsInStock** in H2. 

** ![](https://interject.atlassian.net/wiki/download/attachments/128429456/image2017-8-4_14-51-19.png?version=1&modificationDate=1501883480564&cacheVersion=1&api=v2)   
**

**Step 8:** In this step, addcolumn labels, report titles, borders, and subtotals. Change the report to match. 

![](https://interject.atlassian.net/wiki/download/thumbnails/128429456/image2017-6-23_16-9-43.png?version=1&modificationDate=1498259384188&cacheVersion=1&api=v2&width=743&height=548)

  


**Step 9:** Freeze the report panes so that just the report area is shown for users. In previous examples jFreezePanes() functions were used , but in this page use the standard Freeze Panes feature in Excel. Adjust the worksheet's vertical and horizontal scroll bars until the report is positioned like below. Select cell D13 and use the View menu to set Freeze Panes as seen below. 

![](https://interject.atlassian.net/wiki/download/attachments/128429456/1.09CreateReport-Freeze.png?version=1&modificationDate=1499119408759&cacheVersion=1&api=v2)

  


The final product should look similar to the example below. 

![](https://interject.atlassian.net/wiki/download/thumbnails/128429456/image2017-6-23_16-17-18.png?version=1&modificationDate=1498259839475&cacheVersion=1&api=v2&width=606&height=371)

  


**Step 10:** Now select [ **Pull Data** ](/KB/InterjectRibbon.html#InterjectRibbonMenuItems-PullData) to view the data in the report. 

![](https://interject.atlassian.net/wiki/download/attachments/128429456/image2017-7-20_13-4-57.png?version=1&modificationDate=1500581099036&cacheVersion=1&api=v2)

  


Your final data pull should look like this. You may need to do additional formatting to match the output. 

![](https://interject.atlassian.net/wiki/download/thumbnails/128429456/image2017-7-11_13-6-51.png?version=1&modificationDate=1499803611144&cacheVersion=1&api=v2&width=668&height=370)

  


##  Related Links: 

[ Inventory Reports ](/KB/HowToUse/Walkthroughs/Inventory.html)

[ L1.1 Modify: Customer Aging ](/KB/HowToCreate/ModifyReport/CustomerAging.html)

[ L10 Updating the Report Library ](/KB/HowToCreate/ReportLibrary.html)

[ INTERJECT Ribbon Menu Items ](/KB/InterjectRibbon.html)

[ Basics of Report Formulas ](/KB/HowItWorks/BasicsReportFormulas.html)
