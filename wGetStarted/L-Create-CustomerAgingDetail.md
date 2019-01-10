---
title: "Lab Create: Customer Aging Detail"
layout: custom
keywords: [ create, example, detail, report]
description: This example uses the Customer Aging demo to show the creation of a Customer Aging Detail report that will have variable customer subtotaled sections, each having their respective invoice detail.
---
* * *

##  **Overview**

This example uses the [ Customer Aging ](/wAbout/Customer-Aging.html) demo to show the creation of a Customer Aging Detail report that will have variable customer subtotaled sections, each having their respective invoice detail. You will use both the [ ReportRange() ](/wIndex/ReportRange.html) and [ ReportVariable() ](/wIndex/ReportVariable.html) formulas to create the output. 


###  Building the Report 

**Step 1:** You will begin by using INTERJECT's [ **Report Builder** ](wGetStarted\INTERJECT-Ribbon-Menu-Items.html#report-builder) to make a template for the report. Select NorthwindCustomers Data Portal and choose **Build Report Formula** to build the report. 

![](/images/L-Create-CustAgingDetail/01.png)

<br> 


When the template is complete, it should look like the one below. 

![](/images/L-Create-CustAgingDetail/02.png)

<br> 


**Step 2:** Now that you have the template, clear row 19, **IsMissingCRMID**, because it is not needed it for this report. 

![](/images/L-Create-CustAgingDetail/03.png)

<br> 


**Step 3:** Since you deleted one of the formula's parameters, you have to make sure you also delete it from the ReportRange function in C6. Select cell C6 and delete **C19** from the formula. Also, type **Market** in C16 so you can limit the data presented to only a few records as you are constructing the report. 

![](/images/L-Create-CustAgingDetail/04.png)

<br> 


Now the parameters are set and should only reference cells C16, C17, and C18 as shown below. 

![](/images/L-Create-CustAgingDetail/05.png)
<br>

###  ReportRange() 

**Step 1:** You can select [ **Pull Data** ](wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) to see which columns are available. Since the [ ReportRange() ](wIndex/ReportRange.html) function does not have a Column Definition defined, it should show all the columns with their column names. 

![](/images/L-Create-CustAgingDetail/06.png)

<br> 


After you pull the report it will look like the one below. 

![](/images/L-Create-CustAgingDetail/07.png)

<br> 


**Step 2:** Now that you have pulled the data, you can copy the headers you want into the column definitions row. Do this by holding Ctrl and clicking **CustomerID, CompanyName, ContactName,** and **Phone**. Then copy them and paste the values into cell A2. The below animated GIF illustrates the copy process. 

![](/images/L-Create-CustAgingDetail/08.gif)

<br> 


**Step 3:** For this report, you need to use the multi-row feature illustrated in a previous example. This will be the complete subtotal section that will be repeated for every customer shown. You will insert 6 rows under the **Column Definitions** row 2 and insert 6 rows under the **Formatting Range** row 10. This will give you room to format the report. Each section should have 7 rows beneath it, as shown below. 

![](/images/L-Create-CustAgingDetail/09.png)

<br> 


**Step 4:** Now you will move the Column Definition values into the correct positions. Move **CustomerID** to cell A5, another copy of **CustomerID** to cell G3, **CompanyName** to cell H3, **ContactName** to L3, and **Phone** to O3. You can also format the width of the columns to best fit the report. Match the following screenshot with the column widths. 

![](/images/L-Create-CustAgingDetail/10.png)

<br> 


**Step 5:** Before you setup the Column Definitions in the ReportRange() function, it is best to clear the report so the previously pulled data is erased. Use the Pull Data menu item to select the **Clear** button as illustrated below. 

![](/images/L-Create-CustAgingDetail/11.png)

<br> 


**Step 6:** Next, edit the ReportRange() formula. To access the formula you will select the cell C18 and click **fx** to bring up the Function Wizard. 

![](/images/L-Create-CustAgingDetail/12.png)

<br> 


Now add the ColDefRange and the FormatRange. Type **2:8** for the ColDefRange and **10:16** for the FormatRange as shown below. Notice these are encompassing all 7 rows you have for each section. 

![](/images/L-Create-CustAgingDetail/13.png)   


<br> 


**Step 7:** If you re-pull the data, the multi-row format will be repeated for every customer. 

![](/images/L-Create-CustAgingDetail/14.png)

<br> 


As seen in the following screenshot, you have 7 rows for each customer. It is not formatted yet, so it will not be clear which this is used for. But you can keep moving on. 

![](/images/L-Create-CustAgingDetail/15.png)

<br> 


**Step 8:** You can begin setting up the Formatting Range. 

![](/images/L-Create-CustAgingDetail/16.png)

<br> 


Give row 10,12,14, and 16 heights of 6.75. The error below illustrates how to drag the row height to get close to 6.75. You can also type in example data in G11, H11. In K11 you can type in a label **Contact** : and **Phone:** in N11. Format both of these to be right-aligned. 

![](/images/L-Create-CustAgingDetail/17.png)

<br> 


**Step 9:** Now you need to create a formula that will total all of the detail that will later be populated between row 13 and 14. To create a total, type **=SUBTOTAL(9,L13:L14)** in L15. In cell H15 you will type **="Total Open Invoices For " & H11". ** H11 represents the name of the customer, and by linking it to H11, the subtotal line will note the customer name again. 

![](/images/L-Create-CustAgingDetail/18.png)

<br> 


After that, you will copy the formula put in cell L15 to cell M15, N15, O15, and P15. These subtotals will be used for the aging buckets that will be setup later in this page. See the example below and adjust the formatting to match. 

![](/images/L-Create-CustAgingDetail/19.png)

<br> 


**Step 10:** Re-pull the data to make sure it is formatted correctly. 

![](/images/L-Create-CustAgingDetail/20.png)

<br> 


The formatting has been copied down to the rest of the report and there are subtotal sections. Now you need to populate the section detail with the customer invoice detail. 

![](/images/L-Create-CustAgingDetail/21.png)

<br>

###  ReportVariable() 

**Step 1:** In the Report Formula Section, add a new row under row 18. 

![](/images/L-Create-CustAgingDetail/22.png)

<br> 


**Step 2:** Rename the first pull to **Pull 1 - Customer Sections** (in cell B18) in order to keep track of the report formulas. In cell B19 type in **Pull 2 - Invoices for each section**. The new ReportVariable() will be added to C19 shortly. 

![](/images/L-Create-CustAgingDetail/23.png)

<br> 


**Step 3:** Because you are adding a new Report Formula, you need a new Column Definition and Formatting Range. The illustration below shows two additional sections added. Please update to match. 

![](/images/L-Create-CustAgingDetail/24.png)

<br> 


**Step 4:** Since you have ranges and definitions for both of the formulas, you will rename them so you know which formulas they specify. Please update cells A1, A3, A11, and A13 to match the following text. 

![](/images/L-Create-CustAgingDetail/25.png)

<br> 


**Step 5:** Now you will clear the data to prepare for creating the new formula. 

![](/images/L-Create-CustAgingDetail/26.png)

<br> 


**Step 6:** To define the second formula, add **=ReportVariable()** to cell C23 and click the fx button. The placement of this formula matters, since you want it to run after the ReportRange(). The [ ReportRange() ](/wIndex/ReportRange.html) will be pulled first to provide the list of customer sections, and then the [ ReportVariable() ](/wIndex/ReportVariable.html) will populate the invoices for each section. 

![](/images/L-Create-CustAgingDetail/27.png)

<br> 


**Step 7:** Using the Function Wizard, add **NorthwindCustomerInvoices** as the DataPortal. 

![](/images/L-Create-CustAgingDetail/28.png)

<br> 


**Step 8:** Next, you will specify the new Column Definition and Formatting Range. Type **2:2** into ColDefRange and **12:12** into FormatRange. 

![](/images/L-Create-CustAgingDetail/29.png)

<br> 


**Step 9:** With a ReportVariable, a RowDefRange is required, since it marks what data is to be included in each section. Type **A43:A44** into the RowDefRange. You will be placing the CustomerID in column A shortly. 

![](/images/L-Create-CustAgingDetail/30.png)

<br> 


**Step 10:** Now type **Param(C33,C34,C35,"")"** to establish the parameters for the formula that match the previous ReportRange(). Both Report Formulas are setup to use the same filters. Click OK to finish. 

![](/images/L-Create-CustAgingDetail/31.png)

<br> 


**Step 11:** Before the pull, you need to specify the columns for the invoices that will be included in the detail section. Type **CustomerID** in cell A2, **InvoiceID** in cell B2, **InvoiceNum** in cell I2, **OrderID** in cell J2, **InvoiceDate** in cell K2, **Current** in cell L2, **30Days** in cell M2, **60Days** in cell N2, **90Days** in O2, **ExpectedDate** in R2, and **Note** in T2. Please note that the screenshot below may not show all the characters that need to be typed. Please double check with the last sentence. 

![](/images/L-Create-CustAgingDetail/32.png)

<br> 


**Step 12:** Once completed, re-pull the data. 

![](/images/L-Create-CustAgingDetail/33.png)

<br> 


After pulling the report you now have invoice detail in each section. 

![](/images/L-Create-CustAgingDetail/34.png)

<br> 


**Step 13:** You can go a step further and setup the formatting for the invoice detail and add a subtotal formula in row 12. 

![](/images/L-Create-CustAgingDetail/35.png)

<br> 


Type **=SUM(L12:O12)** into cell P12 to add the formula for total. You will also change the color on cell R12 and T12. 

![](/images/L-Create-CustAgingDetail/36.png)

<br> 


**Step 14:** After you add some headers–and move some cells, freeze panes, and formatting–the final product will look like this. 

![](/images/L-Create-CustAgingDetail/37.png)

<br>