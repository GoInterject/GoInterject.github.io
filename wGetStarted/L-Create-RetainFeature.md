---
title: "Lab Create: Using the Retain Feature"
layout: custom
keywords: [retain, formulas, keep, dont-clear]
description: When using Interject to pull data into your spreadsheet, the report area will be cleared before new data is inserted. In some situations, you may want to bypass the clear action and retain some formulas, since pulling could remove formulas you have on other columns related to certain data rows. 
---
* * *

##  **Overview:**

When using Interject to pull data into your spreadsheet, the report area will be cleared before new data is inserted. In some situations, you may want to bypass the clear action and retain some formulas, since pulling could remove formulas you have on other columns related to certain data rows. This is especially true when you are budgeting or forecasting with historical numbers. The report may have history on the left and your forecasting formulas and numbers will be input on the right. This lab will show you how to update the data in a report without deleting rows that must be retained. 

The Retain feature relates to reports using the [ ReportVariable() ](/wIndex/ReportVariable.html) or [ ReportRange() ](/wIndex/ReportRange.html) functions. Since Interject must still update your data, it must determine which columns act as the key values, so it can place the correct data in the correct row. 

When Interject finds new data, it will add a new row and populate the data. Using the retain feature, Interject will never delete a row, it will simply zero the amounts. 

When a new row is added, there are two options: 1) to insert the new row at the bottom of the section or 2) to insert the row based on the sorting of the key values columns. The former is the default, since adding to the bottom of the section helps avoid adding new rows between your formulas. The lab below will walk through these and other steps on how to use the retain feature operates in your reports. 

Use the PL Trend report for this lab. 

###  Create Simple Formulas: 

To start, copy the columns  **L-N** in the  **PLTrend** tab and paste them into Column  **P-R.**

![](/images/L-Create-Retain/01.jpg)

<br> 

Then, unfreeze the sheet. 

![](/images/L-Create-Retain/02.jpg)

<br> 

Clear out the cell range  **P2:R5** from the new columns so new data does not populate on the right side. This is also a good time to clear out the extra input spaces in the  **P20:R26** cell range. 

![](/images/L-Create-Retain/03.jpg)

<br> 

Now input  **7002** into  **Location** and  **2002-05** into  **Month.** Then **Pull** the report. 

![](/images/L-Create-Retain/04.jpg)

<br> 

Now, with the blank section to the right, we will create a projection based on the previous 3 months. 

First, in cell  **Q26**, input  **Forecasting Formulas.** Then, edit the formula in  **P27** to be  **=IFERROR(EOMONTH(DATEVALUE(M23 &"-01"),1),"-")**. The following month formulas are set to use this formula and will update accordingly. 

![](/images/L-Create-Retain/05.jpg)

<br> 

Project a 10% increase to every value. First select cell **P29** and input the formula **=L29 * 1.10**. Copy cell **P29** to the clipboard. Next highlight cells **P29:R152**. Finally, right-click on the area and copy the formulas.

![](/images/L-Create-Retain/06.png)

<br>

###  Without RetainedRowColumns: 

If the accounts numbers were to change, the 10% increase would no longer be accurate since the data is old. Re-pull the data to update your numbers. 

![](/images/L-Create-Retain/07.jpg)

<br> 

Without using the RetainedRowColumns feature, if your formulas are on the same rows as the data detail rows, the formulas get deleted when pulling updated data. 

![](/images/L-Create-Retain/08.jpg)

<br>

**Note:** The reason that some of the rows do not lose their formulas is because they are what are considered summary rows. A ReportVariable() also contains detail rows which are rows that get deleted on a pull or clear. 

###  With RetainedRowColumns: 

To fix this, use the RetainedRowsColumns to retain the rows and your formulas. 

To do this, start by inputing **=L29 * 1.1** into cell **P29** again and then copy the formula into cells **P29:R152** like before.

![](/images/L-Create-Retain/09.png)

<br> 

Now, click on the cell  **G16,** which contains the ReportVariable() formula. Now click the  **fx** button to pull up the function wizard. 

![](/images/L-Create-Retain/10.jpg)

<br> 

Now scroll down to the **RetainRowColumns.** The RetainRowColumns argument expects a single string of comma delimited names of columns that will be retained after a data pull. Instead of entering the string, the [**jCombine()**](/wIndex/jCombine.html) helper function is helpful as it will concatenate the column names for us.

Enter **jCombine((F2:G2))** in the field. This will retain all inputs in columns **P-R** in the report. 

![](/images/L-Create-Retain/11.jpg)

<br> 

Now, if the data changes again, you need to **Pull** the report again. 

![](/images/L-Create-Retain/12.jpg)

<br> 

Notice that the formulas are still intact and accurate to the new data. 

![](/images/L-Create-Retain/13.jpg)
