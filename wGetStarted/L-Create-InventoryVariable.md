---
title: Interject | Lab Inventory Variable
layout: custom
---
  


* * *

##  **  
Overview **   


The [ ReportVariable() ](/KB/ExcelFunctions/ReportVariable.html) function directs data into multiple specified ranges of a report that can grow and shrink with the data. It is ideal for a financial report or any report that has subtotaled sections.  In this example, you will use the report seen in the [ Inventory Walk-through ](/KB/HowToUse/Walkthroughs/Inventory.html) . Once completed all rows of the report **Inventory By Category with Detail** will be populated with a single ReportVariable() function. 

###  Report Variable 

**Step 1:** Open the INTERJECT [ Report Library ](/KB/HowToUse/ReportLibraryBasics.html) and select the **Interject Inventory Demo** in the **Interject Demos** folder. 

![](https://interject.atlassian.net/wiki/download/attachments/127872532/image2017-6-29_11-42-23.png?version=1&modificationDate=1498761744718&cacheVersion=1&api=v2)

  


**Step 2:** The report will open in the **InventoryByCategory** tab, as shown below. 

![](https://interject.atlassian.net/wiki/download/attachments/127872532/image2017-8-14_12-44-21.png?version=1&modificationDate=1502739861979&cacheVersion=1&api=v2)

  


** Step 3:  ** For this exercise, you will be using the worksheet **InvByCategory_WithDetail** . This worksheet is already setup for a Variable section report, and it will help focus on key concepts rather than the spreadsheet text and formatting. Click on the tab  **InvByCategory_WithDetail** . 

![](https://interject.atlassian.net/wiki/download/attachments/127872532/image2017-8-14_12-44-59.png?version=1&modificationDate=1502739900565&cacheVersion=1&api=v2)

  


  


**Step 4:** Open the configuration section of this report using the following three steps. 

  1. First, select the **View** ribbon. 
  2. Second, pull down the Freeze Panes menu and select Unfreeze. 
  3. Last, click the plus sign, as shown below, to can expand the column groupings  . 



![](https://interject.atlassian.net/wiki/download/attachments/127872532/image2017-6-13_15-30-0.png?version=1&modificationDate=1497393002217&cacheVersion=1&api=v2)

  


Scroll to the top, and  the full configuration area is seen  in the left of the report.Clear the formula in cell C4 so you can build the ReportVariable() function from the beginning. 

![](https://interject.atlassian.net/wiki/download/attachments/127872532/image2017-6-13_12-40-22.png?version=1&modificationDate=1497382823498&cacheVersion=1&api=v2)

**  
**

**Step 5:** Now create a new report formula. In cell C4 type  **=[ ReportVariable() ](/KB/ExcelFunctions/ReportVariable.html) ** . 

![](https://interject.atlassian.net/wiki/download/attachments/127872532/image2017-6-13_12-59-45.png?version=1&modificationDate=1497383986956&cacheVersion=1&api=v2)   
  


**Step 6:** Next, click the **Fx** button left of the formula to open the Function Wizard. 

![](https://interject.atlassian.net/wiki/download/attachments/127872532/image2017-6-13_13-30-41.png?version=1&modificationDate=1497385842140&cacheVersion=1&api=v2)

  


**Step 7:** F  irst enter the Dataportal for this example. Type  **NorthwindVariable** in the Dataportal argument.  ![](https://interject.atlassian.net/wiki/download/attachments/127872532/image2017-6-13_13-34-24.png?version=1&modificationDate=1497386065563&cacheVersion=1&api=v2)   


**   
**

** Step 8  : ** Next, setup the Column and Row Definitions for this report. 

For the **RowDefRange** argument, type **B18:B54** . This not only covers the Row Definitions for the main body of the report but includes the **Leftover** section as well. This leftover section is special, since it will show any records that did not populate in one of the sections above. This helps ensure you are not missing any data in the report.  ![](https://interject.atlassian.net/wiki/download/attachments/127872532/image2017-6-13_13-54-29.png?version=1&modificationDate=1497387270604&cacheVersion=1&api=v2)

  


For the **ColDefRange** argument, simply input **2:2** , since the Column Definitions are already setup in row 2 for this report. 

![](https://interject.atlassian.net/wiki/download/attachments/127872532/image2017-6-13_13-58-41.png?version=1&modificationDate=1497387522839&cacheVersion=1&api=v2)

  


**Step 9:** The detail rows of a Variable report are typically formatted using the Formatting Range. Initially, use the first row of the first section to set the formatting. Leave the FormatRange argument blank. 

![](https://interject.atlassian.net/wiki/download/attachments/127872532/image2017-6-23_16-2-17.png?version=1&modificationDate=1498258938273&cacheVersion=1&api=v2)

  
Pull the report.    
![](https://interject.atlassian.net/wiki/download/attachments/127872532/image2017-6-23_16-24-20.png?version=1&modificationDate=1498260261628&cacheVersion=1&api=v2)

**  
**

With the report pulled, see how data was inserted into each of its sections, and each section expanded to fit the data. You can even see how the **Leftover** section works. Try changing the cell B19 from **Beverages** to **BeveragesSkip** . When you pull again, that section's records will move to the bottom. Go ahead and change B19 back to **Beverages** and repull. The data will return to the correct section. 

** ![](https://interject.atlassian.net/wiki/download/attachments/127872532/image2017-8-14_13-7-22.png?version=1&modificationDate=1502741242968&cacheVersion=1&api=v2) **

  


**Step 10:** Once you have pulled the report, adjust the formatting. You can select the top row (row 19) and change the format in one of the columns. Make **Product Name** bold, as it is below. 

![](https://interject.atlassian.net/wiki/download/thumbnails/127872532/image2017-7-11_13-17-17.png?version=1&modificationDate=1499804236587&cacheVersion=1&api=v2&width=1000&height=583)

**  
**

Pull again. 

** ![](https://interject.atlassian.net/wiki/download/attachments/127872532/image2017-6-23_16-58-27.png?version=1&modificationDate=1498262308572&cacheVersion=1&api=v2) **

  


You can see that all the rows below **Chai** in the Product Name column are bold like the first row. If you scroll further down the report, the other sections will have the bold format as well. 

** ![](https://interject.atlassian.net/wiki/download/attachments/127872532/image2017-6-23_17-5-6.png?version=1&modificationDate=1498262707608&cacheVersion=1&api=v2) **

**  
**

**Step 11:** The most common approach is using a formatting range. The existing report has a Formatting Range prepared in row 7. Update the ReportVariable() function in C4 to have a Formatting Range of **7:7** . From this point forward,  when the data is pulled,  the formatting, values, and formulas placed in the Formatting Range will be used in all the sections below.    


![](https://interject.atlassian.net/wiki/download/attachments/127872532/2.08ReportVariable-Function%20argument%20Format%20Range%201.png?version=1&modificationDate=1498259833697&cacheVersion=1&api=v2) **  
**

**  
**

**Step 12:** Now, add the filters.  In this Dataportal and report there are two filter options, **Min Qty In Stock** and **Product** **Name** . Open the Function Wizard again on cell C4 and enter  **Param( I14,  I15  ) ** into the  **Parameter** argument. This configures INTERJECT to look for the filters in cells I14 and I15. The order of cell references appearing in the Param() function must coincide with the order that was originally setup for the Dataportal. 

![](https://interject.atlassian.net/wiki/download/attachments/127872532/image2017-6-23_17-16-34.png?version=1&modificationDate=1498263395221&cacheVersion=1&api=v2)

###  Final Touches 

Once you have finished all steps above, check the report by re-pulling. 

![](https://interject.atlassian.net/wiki/download/attachments/127872532/image2017-6-23_17-25-59.png?version=1&modificationDate=1498263960620&cacheVersion=1&api=v2)

  


The data should be presented as shown below. 

![](https://interject.atlassian.net/wiki/download/attachments/127872532/image2017-6-23_17-37-5.png?version=1&modificationDate=1498264626857&cacheVersion=1&api=v2)

  


###  Final Result 

One the pins are frozen the final result should look similar to the image below.   
![](https://interject.atlassian.net/wiki/download/attachments/127872532/image2017-6-23_17-47-25.png?version=1&modificationDate=1498265246770&cacheVersion=1&api=v2)

  


##  Related Links: 

[ Creating a Simple Report ](/KB/HowToCreate/CreateReport.html)

[ ReportVariable() ](/KB/ExcelFunctions/ReportVariable.html)

[ ReportFixed ](/KB/ExcelFunctions/ReportFixed.html)

#    


  

