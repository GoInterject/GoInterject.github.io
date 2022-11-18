---
title: "Lab Create: Inventory Variable"
layout: custom
keywords: [variable, report, inventory, example]
description: In this example, you will use the report seen in the Inventory Walk-through. Once completed all rows of the report Inventory By Category with Detail will be populated with a single ReportVariable() function. 
---
* * *

##  **Overview**   


The [ ReportVariable() ](/wIndex/ReportVariable.html) function directs data into multiple specified ranges of a report that can grow and shrink with the data. It is ideal for a financial report or any report that has subtotaled sections.  In this example, you will use the report seen in the [ Inventory Walk-through ](/wAbout/Inventory-Reports.html). Once completed all rows of the report **Inventory By Category with Detail** will be populated with a single ReportVariable() function. 

<blockquote class=lab_info>
  If you are following the Training Labs, this report file can be found in the Report Library at Training Labs > Lab 3 Creating Reports > Lab 3.4 Inventory Variable Report.
</blockquote>

###  Report Variable 

**Step 1:** Open the INTERJECT [ Report Library ](/wAbout/Report-Library-Basics.html) and select the **Interject Inventory Demo** in the **Interject Demos** folder. 

![](/images/L-Create-InventoryVar/01.png)

<br> 


**Step 2:** The report will open in the **InventoryByCategory** tab, as shown below. 

![](/images/L-Create-InventoryVar/02.png)

<br> 


**Step 3:** For this exercise, you will be using the worksheet **InvByCategory_WithDetail**. This worksheet is already setup for a Variable section report, and it will help focus on key concepts rather than the spreadsheet text and formatting. Click on the tab  **InvByCategory_WithDetail**. 

![](/images/L-Create-InventoryVar/03.png)

<br> 


**Step 4:** Open the configuration section of this report using the following three steps. 

1. First, select the **View** ribbon. 
2. Second, pull down the Freeze Panes menu and select Unfreeze. 
3. Last, click the plus sign, as shown below, to can expand the column groupings. 



![](/images/L-Create-InventoryVar/04.png)

<br> 


Scroll to the top, and  the full configuration area is seen  in the left of the report. Clear the formula in cell C4 so you can build the ReportVariable() function from the beginning. 

![](/images/L-Create-InventoryVar/05.png)



**Step 5:** Now create a new report formula. In cell C4 type [ **=ReportVariable()** ](/wIndex/ReportVariable.html). 

![](/images/L-Create-InventoryVar/06.png)

<br> 


**Step 6:** Next, click the **Fx** button left of the formula to open the Function Wizard. 

![](/images/L-Create-InventoryVar/07.png)

<br> 


**Step 7:** F  irst enter the Dataportal for this example. Type  **NorthwindVariable** in the Dataportal argument.  

![](/images/L-Create-InventoryVar/08.png)   

<br>

**Step 8:** Next, setup the Column and Row Definitions for this report. 

For the **RowDefRange** argument, type **B18:B54**. This not only covers the Row Definitions for the main body of the report but includes the **Leftover** section as well. This leftover section is special, since it will show any records that did not populate in one of the sections above. This helps ensure you are not missing any data in the report.  

![](/images/L-Create-InventoryVar/09.png)

<br> 


For the **ColDefRange** argument, simply input **2:2**, since the Column Definitions are already setup in row 2 for this report. 

![](/images/L-Create-InventoryVar/10.png)

<br> 


**Step 9:** The detail rows of a Variable report are typically formatted using the Formatting Range. Initially, use the first row of the first section to set the formatting. Leave the FormatRange argument blank. 

![](/images/L-Create-InventoryVar/11.png)

<br> 

Pull the report.    

![](/images/L-Create-InventoryVar/12.png)

<br>

With the report pulled, see how data was inserted into each of its sections, and each section expanded to fit the data. You can even see how the **Leftover** section works. Try changing the cell B19 from **Beverages** to **BeveragesSkip**. When you pull again, that section's records will move to the bottom. Go ahead and change B19 back to **Beverages** and repull. The data will return to the correct section. 

![](/images/L-Create-InventoryVar/13.png) 

<br> 


**Step 10:** Once you have pulled the report, adjust the formatting. You can select the top row (row 19) and change the format in one of the columns. Make **Product Name** bold, as it is below. 

![](/images/L-Create-InventoryVar/14.png)

<br>

Pull again. 

![](/images/L-Create-InventoryVar/15.png)

<br> 


You can see that all the rows below **Chai** in the Product Name column are bold like the first row. If you scroll further down the report, the other sections will have the bold format as well. 

![](/images/L-Create-InventoryVar/16.png) 

<br>

**Step 11:** The most common approach is using a formatting range. The existing report has a Formatting Range prepared in row 7. Update the ReportVariable() function in C4 to have a Formatting Range of **7:7**. From this point forward,  when the data is pulled,  the formatting, values, and formulas placed in the Formatting Range will be used in all the sections below.    


![](/images/L-Create-InventoryVar/17.png) 

<br>

**Step 12:** Now, add the filters.  In this Dataportal and report there are two filter options, **Min Qty In Stock** and **Product** **Name**. Open the Function Wizard again on cell C4 and enter  **Param( I14,  I15  )** into the  **Parameter** argument. This configures INTERJECT to look for the filters in cells I14 and I15. The order of cell references appearing in the Param() function must coincide with the order that was originally setup for the Dataportal. 

![](/images/L-Create-InventoryVar/18.png)

<br>

###  Final Touches 

Once you have finished all steps above, check the report by re-pulling. 

![](/images/L-Create-InventoryVar/19.png)

<br> 


The data should be presented as shown below. 

![](/images/L-Create-InventoryVar/20.png)

<br> 


###  Final Result 

Once the panes are frozen the final result should look similar to the image below.   

![](/images/L-Create-InventoryVar/21.png)

<br>

Finally, clear the report, refreeze the panes, and upload it to the ![ Report Library ](/wGetStarted/L-Create-UpdatingReportLibrary.html).