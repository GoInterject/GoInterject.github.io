---
title: "Lab Create: Hiding Rows and Columns"
layout: custom
keywords: []
description:
---
##  **Overview**

The **ReportHideRowOrColumn()** function allows you to hide rows columns when they are not needed, for example if a row contains no data. In the first example, you will hide rows containing a total value of zero. The second example shows how to hide columns using the same function and for a similar reason. 

Once completed, these two features can be combined to hide, without eliminating, certain unneeded values and generally clean up the presentation of your financial reports. 

Both of these examples use the [ Customer Aging Detail  ](/wGetStarted/L3.4-Customer-Aging-Detail.html) report created in a previous walk through. You can navigate to the report by opening the **Customer Collections** report in the **Interject Demo** folder of the [ Report Library ](/wAbout/Report-Library-Basics.html). 

![](/images/L-Create-HideRowCol/01.png)

<br> 

###  **Hiding Rows**
 
**Step 1:** With the report opened to the **CustomerAgingDetail** tab, type "Market" into the company name filter and pull the data using Ctrl+Shift+J rot he pull button. Notice on row 61 that Great Lakes Market has an entry with zero value. Rows like this are what we'll hide using the ReportHideRowOrColumn function.

![](/images/L-Create-HideRowCol/PullMarket.png)

**Step 2:**  Unfreeze the report formula panes by clicking the [ Quick Tools ](/wPortal/INTERJECT-Ribbon-Menu-Items.html) icon in the ribbon menu and selecting **Freeze/Unfreeze Panes**. 

![](/images/L-Create-HideRowCol/02.jpg)

<br>

**Step 3:** Type **Hide/Show Inv w/0 Subs** in cell **K27**. Then type **=ReportHideRowOrColumn()** in cell **L27**.

![](/images/L-Create-HideRowCol/TypeFormulas.png)

<br> 


**Step 4:** With cell **L27** still selected, click on the **fx** button to open the formula wizard.
- For **OnPullSaveOrBoth**, type **Pull**
- For **OnClearRunOrBoth**, type **Both**
- For **RowOrColumnRange**, enter **C43:C44** \(this will copy the formula through all rows of the report\)
- For **Disabled**, do not enter anything
- Hit OK

![](/images/L-Create-HideRowCol/FormWizard.png)

<br> 


**Step 5:** Now, in cell **C16**, type **=IF(P16=0,"Hide","Show")**. This specifies how to handle 0 values based on the formula entered for the subtotal column.  

![](/images/L-Create-HideRowCol/EnterForm.png)

<br> 


**Step 6:** Type **Market** into the customer name parameter again, then pull the report. Notice this time that the row containing no subtotal is now hidden. The data is not gone, it just isn't displayed in the report any longer.

![](/images/L-Create-HideRowCol/HideResult.png)

<br> 

