---
title: Interject Documentation > L9 Using the Retain Feature
layout: custom
---
* * *

##  **Overview:**

When using INTERJECT to pull data into your spreadsheet, the report area will be cleared before new data is inserted. In some situations, you may want to bypass the clear action and retain some formulas, since pulling could remove formulas you have on other columns related to certain data rows. This is especially true when you are budgeting or forecasting with historical numbers. The report may have history on the left and your forecasting formulas and numbers will be input on the right. This lab will show you how to update the data in a report without deleting rows that must be retained. 

The Retain feature relates to reports using the [ ReportVariable() ](/wIndex/61702201.html) or [ ReportRange() ](/wIndex/61702199.html) functions. Since INTERJECT must still update your data, it must determine which columns act as the key values, so it can place the correct data in the correct row. 

When INTERJECT finds new data, it will add a new row and populate the data. Using the retain feature, INTERJECT will never delete a row, it will simply zero the amounts. 

When a new row is added, there are two options: 1) to insert the new row at the bottom of the section or 2) to insert the row based on the sorting of the key values columns. The former is the default, since adding to the bottom of the section helps avoid adding new rows between your formulas. The lab below will walk through these and other steps on how to use the retain feature operates in your reports. 

Use the PL Trend report for this lab. 

###  Create Simple Formulas: 

To start, copy the columns  **L-N** in the  **PLTrend** tab and paste them into Column  **P-R.**

![](attachments/361332831/363331616.jpg)

  


Then, unfreeze the sheet. 

![](attachments/361332831/363659320.jpg)

  


Clear out the cell range  **P2:R5** from the new columns so new data does not populate on the right side. This is also a good time to clear out the extra input spaces in the  **P20:R26** cell range. 

![](attachments/361332831/363429948.jpg)

  


Now input  **7002** into  **Location** and  **2002-05** into  **Month.** Then **Pull** the report. 

![](attachments/361332831/363626536.jpg)

  


Now, with the blank section to the right, we will create a projection based on the previous 3 months. 

First, in cell  **Q26** , input  **Forecasting Formulas.** Then, edit the formula in  **P27** to be  **=IFERROR(EOMONTH(DATEVALUE(M23 &"-01"),1),"-") ** . The following month formulas are set to use this formula and will update accordingly. 

![](attachments/361332831/363593824.jpg)

  


Project a 10% increase to every value by inputting  **=L33*1.10** into cell  **P29.** Then copy this formula into the range of the cells from **P29:R152** . 

![](attachments/361332831/363397149.jpg)

### 

###  Without RetainedRowColumns: 

If the accounts numbers were to change, the 10% increase would no longer be accurate since the data is old. Re-pull the data to update your numbers. 

![](attachments/361332831/363626541.jpg)

  


Without using the RetainedRowColumns feature, if your formulas are on the same rows as the data detail rows, the formulas get deleted when pulling updated data. 

![](attachments/361332831/363495479.jpg)

**Note:** The reason that some of the rows do not lose their formulas is because they are what are considered summary rows. A ReportVariable() also contains detail rows which are rows that get deleted on a pull or clear. 

### 

###  With RetainedRowColumns: 

To fix this, use the RetainedRowsColumns to retain the rows and your formulas. 

To do this, input  **=L33*1.10** into cell  **P29.** Then copy this formula into all of the blue cells. 

![](attachments/361332831/363331621.jpg)

  


Now, click on the cell  **G16,** which contains the ReportVariable() formula. Now click the  **fx** button to pull up the function wizard. 

![](attachments/361332831/363364422.jpg)

  


When selecting a range of cells, RetainedRowColumns uses a single string delimiting character separated list as its input. This means that the  **jcombine()** [link] helper function is required. 

Now scroll down to the  **RetainRowColumns.** In that box, input  **jcombine((F2:G2))** . This will retain all inputs in columns  **P-R** in the report. 

![](attachments/361332831/363659325.jpg)

  


Now, if the data changes again, you need to **Pull** the report again. 

![](attachments/361332831/363331626.jpg)

  


Notice that the formulas are still intact and accurate to the new data. 

![](attachments/361332831/363495484.jpg)
