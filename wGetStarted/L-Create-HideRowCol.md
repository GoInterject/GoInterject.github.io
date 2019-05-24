---
title: "Lab Create: Hiding Rows and Columns"
layout: custom
keywords: []
description:
---
##  **Overview**

**ReportHideRowsOrColumns()** is a function that allows you to hide both rows and columns when they are not needed. In this example, you will begin with hiding columns M, N, and O. In this lab, you will change the report to only reveal the 90 days column when there are invoices that are 90 days overdue. This will prepare you to create a report that could show any of the hidden columns if there were values in the column. This will remove the data clutter that can occur in reports. 

This lab also details how to show or hide rows based on whether or not the rows contain an expected date value. There are multiple ways to accomplish this, however this lab only indicates explores one of the possibilities. This lab walks through how in a pinch situation where you are unable to contact the IT department and need to get a solution quickly. This approach is not part of the Best Practices, however will be a good bandaid. To totally solve the issue, the IT department will need to create a SQL parameter to link to the filter on the report. The SQL parameter in this instance has already been created, however, to have a SQL filter created contact your IT department. 

In this example you will be using the  [ Customer Aging Detail  ](/wGetStarted/L3.4-Customer-Aging-Detail.html) Report you created earlier or use the steps below to navigate to the provided one in the report library. 


###  **Hiding Rows**

**Step 1:** To begin, open the **Customer Collections** report in the [ Report Library ](/wAbout/Report-Library-Basics.html). 

![](/images/L-Create-HideRowCol/01.png)

<br> 


Now that you have the report, you can decide which rows you want to hide temporarily. Make sure you are in the tab labelled **CustomerAgingDetail**. 

**Step 2:** Next you will unfreeze panes by going into [ Quick Tools ](/wPortal/INTERJECT-Ribbon-Menu-Items.html) and select **Freeze/Unfreeze Panes**. 

![](/images/L-Create-HideRowCol/02.jpg)

<br>

**Step 3:** First, you need a filter that acts as a flag for an Excel formula. On **row 39** insert a new row above it. 

![](/images/L-Create-HideRowCol/03.jpg)

<br> 


**Step 4:** In cell **G39** input **Show Expected Date:** to label the filter for later use. 

![](/images/L-Create-HideRowCol/04.jpg)

<br> 


**Step 3:** Now restrict the cell **H39** to only toggle between Yes, No, or leave it as an empty string. 

To do this, select the parameter cell, navigate to the **Data** Excel Ribbon, then select **Data Validation**. 

![](/images/L-Create-HideRowCol/05.jpg)

<br> 


**Step 4:** Click the **Allow** dropdown and select **List.**

![](/images/L-Create-HideRowCol/06.jpg)

<br> 


**Step 5:** Now change the allowed **Source** input to be **Yes, No**. 

![](/images/L-Create-HideRowCol/07.jpg)

**Note:** This will make a drop down list consisting of two options, **Yes** and **No**. 

<br> 


**Step 6:** Now select **row 30** and insert two rows above it. 

![](/images/L-Create-HideRowCol/08.jpg)

<br> 


**Step 7:** In cell **G30** input **Formula Refresh** and in cell **G31** insert **Hide Rows:** to label what each INTERJECT Report Formula is used for. 

![](/images/L-Create-HideRowCol/09.jpg)

<br> 


**Step 8:** In cell **H30** insert **=ReportCalc()** and then select the **fx** button to bring up the function wizard. 

![](/images/L-Create-HideRowCol/10.jpg)

<br>

**Note:** When hiding rows and columns it is important that a **ReportCalc** **()** is used along with a **ReportHideRowOrColumn()**. Since the ReportHideRowOrColumn() leverages cell values as flags, it requires the outputs of Excel formulas to be updated after an INTERJECT Pull event. The order of the INTERJECT events matters in this example so the order of Report Formulas matters. INTERJECT reads Report Formulas from Left to Right, Top to Bottom, thus the ReportCalc() is created before the ReportHideRowOrColumn() so that it is executed by INTERJECT first. 

<br> 


**Step 9:** In the fields **OnPullSaveOrBoth**, **OnClearRunOrBoth**, **SheetOrWorkbook** input **Both**, **Both**, **Sheet** respectively 

![](/images/L-Create-HideRowCol/11.jpg)

<br> 


**Step 10:** In the variable formatting range, in this case cell **C16**, input this formula **=IF($H$42="Yes","Show",IF(R16="","Show","Hide"))**. Be sure that it is in the **Report Variable** formatting range or the formula will not be copied down as intended. By selecting the cell in the formatting range, the formula will copy down to the rest of the report. 

Once the report is ready you can view how to the left of the data there is a column filled with **Show** and **Hide**. Once you finish this example only the **Show** will be visible. 

![](/images/L-Create-HideRowCol/12.jpg)

<br> 


**Step 11:** To check if the excel formula is functioning pull the report using the Company Parameter, **Market**. 

![](/images/L-Create-HideRowCol/13.jpg)

<br> 


**Step 12:** In cell **H31**, type in **=ReportHideRoworColumn** and select **fx**. 

![](/images/L-Create-HideRowCol/14.jpg)

<br> 


**Step 13:** The Function Argument window will appear and in **OnPullsSavesOrBoth** you will input **Pull**

![](/images/L-Create-HideRowCol/15.jpg)

<br> 


**Step 14:** **** In the box labeled **OnClearRunOrBoth** you will input **Both**. 

![](/images/L-Create-HideRowCol/16.jpg)

<br> 


**Step 15:** For the third box labeled **RoworColumnRange** input **C47:C48**. Do this by selecting the cells, not by typing in the values. 

![](/images/L-Create-HideRowCol/17.jpg)

<br> 


**Step 16:** Set cell **H42** to **No** then use the [ **Pull Data** ](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) menu item to check your work.   

![](/images/L-Create-HideRowCol/18.jpg)

<br> 


You will now only be able to view the invoices without expected dates. 

![](/images/L-Create-HideRowCol/19.jpg)

<br> 


**Step 17:** Now that the formula is complete, you can reformat the page using [ Quick Tools ](/wPortal/INTERJECT-Ribbon-Menu-Items.html) and Freeze the panes. 

![](/images/L-Create-HideRowCol/20.jpg)

<br> 


###  Hiding Columns 

In this next example our goal is too hide the rows that have a payment expected date and show the rows without one. 

**Step 1:** To begin you will unfreeze the report using [ Quick Tools ](/wPortal/INTERJECT-Ribbon-Menu-Items.html). 

![](/images/L-Create-HideRowCol/21.png)

<br> 



You are now ready to begin editing the excel sheet. 

![](/images/L-Create-HideRowCol/22.jpg)

<br> 


**Step 2:** Select cell **M34** and **N34** and insert **Hide**. This is to hide the columns where the overdue charges are under 90 days since this data is not needed often. 

![](/images/L-Create-HideRowCol/23.jpg)

<br> 


**Step 3:** In cell **G30** input **Refresh Functions:**, in cell **G31** input **Hide Columns:**, and in cell **G32** input **Hide Rows:**, then right align all 3 cells to create labels for report formulas so they don't get mixed up. 

![](/images/L-Create-HideRowCol/24.jpg)

<br> 


**Step 4:** Select cell **O34** and insert **=IF(SUMIF(C47:C48,"Show",O47:O48) > 0, "Show", "Hide")**. 

![](/images/L-Create-HideRowCol/25.jpg)

<br> 


**Step 5:** In cell **G31** insert **Hide Columns:** and in cell **H31** input **=ReportHideRoworColumn()**

![](/images/L-Create-HideRowCol/26.jpg)

<br> 


**Step 6:** Select cell **H31** and click the **fx** button to open the function wizard 

![](/images/L-Create-HideRowCol/27.jpg)

<br> 


**Step 7:** In the function wizard input **Pull** in the field labeled **OnPullSaveOrBoth**, input **Both** in the field **OnClearRunOrBoth**. 

![](/images/L-Create-HideRowCol/28.jpg)

<br> 


**Step 8:** Select the filed **RowOrColumnRange** then select the three cells containing **Hide**. In this case it will be **M39:O39**. 

![](/images/L-Create-HideRowCol/29.jpg)

<br> 


**Step 9:** Select cells **M** **5** and **O** **5** and shift them left 3 cells by cutting the cells and pasting them into **J** **5** and **M** **5** respectively. 

![](/images/L-Create-HideRowCol/30.jpg)

<br> 


**Step 10:** Select cells **L19** and **N19** and shift them left 3 cells by cutting the cells and pasting them into **I19** and **K19** respectively. 

![](/images/L-Create-HideRowCol/31.jpg)

<br> 


**Step** **11:** Re-freeze the report 

![](/images/L-Create-HideRowCol/32.jpg)

<br> 


**Step 12:** In cell **H39** input **Market** and set cell **H42** to **No** and Pull the report 

![](/images/L-Create-HideRowCol/33.jpg)

<br> 


Your report is now finished and can hide rows and columns where the invoices have an expected date and there is no invoice that is 90 days past due. 

![](/images/L-Create-HideRowCol/34.jpg)


Finally, clear the report and upload it to the ![ Report Library ](/wGetStarted/L-Create-UpdatingReportLibrary.html).