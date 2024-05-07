---
title: "Create: Customer Aging Detail Report"
filename: "L-Create-CustomerAgingDetail.md"
layout: custom
keywords: [create, customer aging, detail, report, range, variable, ReportDefaults, Northwind customers, walkthrough]
headings: ["Overview", "Building the Report", "ReportRange()", "ReportVariable()", "ReportDefaults()", "Formatting the Report"]
links: ["/wAbout/Customer-Aging.html", "/wIndex/ReportRange.html", "/wIndex/ReportVariable.html", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#report-builder", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data", "/wIndex/ReportRange.html", "/wIndex/ReportRange.html", "/wIndex/ReportVariable.html", "/wIndex/ReportDefaults.html", "/wIndex/Event-Functions-Landing.html", "/wAbout/ReportLibraryLinks.html"]
image_dir: "L-Create-CustAgingDetail"
images: [{file: "01", type: "png", site: "Addin", cat: "Report Builder", sub: "", report: "NorthwindCustomers", ribbon: "Advanced", config: ""}, {file: "02", type: "png", site: "Addin", cat: "Report", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "05", type: "png", site: "Excel", cat: "Right Click Menu", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "06", type: "png", site: "Addin", cat: "Pull Data", sub: "", report: "NorthwindCustomers", ribbon: "Simple", config: "Yes"}, {file: "07", type: "png", site: "Addin", cat: "Report", sub: "", report: "NorthwindCustomers", ribbon: "", config: ""}, {file: "08", type: "gif", site: "Excel", cat: "Right Click Menu", sub: "Copy", report: "NorthwindCustomers", ribbon: "Simple", config: "Yes"}, {file: "09", type: "png", site: "Addin", cat: "Report", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "10", type: "png", site: "Addin", cat: "Report", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "11", type: "png", site: "Addin", cat: "Pull Data", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "12", type: "png", site: "Excel", cat: "Function Wizard", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "13", type: "png", site: "Excel", cat: "Function Wizard", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "14", type: "png", site: "Addin", cat: "Pull Data", sub: "", report: "NorthwindCustomers", ribbon: "Simple", config: "Yes"}, {file: "15", type: "png", site: "Addin", cat: "Report", sub: "", report: "NorthwindCustomers", ribbon: "", config: ""}, {file: "16", type: "png", site: "Addin", cat: "Report", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "17", type: "png", site: "Addin", cat: "Report", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "18", type: "png", site: "Addin", cat: "Report", sub: "", report: "NorthwindCustomers", ribbon: "Simple", config: "Yes"}, {file: "19", type: "png", site: "Addin", cat: "Report", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "20", type: "png", site: "Addin", cat: "Pull Data", sub: "", report: "NorthwindCustomers", ribbon: "Simple", config: "Yes"}, {file: "21", type: "png", site: "Addin", cat: "Report", sub: "", report: "NorthwindCustomers", ribbon: "", config: ""}, {file: "22", type: "png", site: "Addin", cat: "Report", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "23", type: "png", site: "Addin", cat: "Report", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "24", type: "png", site: "Addin", cat: "Report", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "25", type: "png", site: "Addin", cat: "Report", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "26", type: "png", site: "Addin", cat: "Pull Data", sub: "", report: "NorthwindCustomers", ribbon: "Simple", config: "Yes"}, {file: "27", type: "png", site: "Excel", cat: "Function Wizard", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "28", type: "png", site: "Excel", cat: "Function Wizard", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "29", type: "png", site: "Excel", cat: "Function Wizard", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "30", type: "png", site: "Excel", cat: "Function Wizard", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "31", type: "png", site: "Excel", cat: "Function Wizard", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "32", type: "png", site: "Addin", cat: "Report", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "33", type: "png", site: "Addin", cat: "Pull Data", sub: "", report: "NorthwindCustomers", ribbon: "Simple", config: "Yes"}, {file: "34", type: "png", site: "Addin", cat: "Report", sub: "", report: "NorthwindCustomers", ribbon: "", config: ""}, {file: "ReportDefaultsEntry", type: "png", site: "Addin", cat: "Report", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "ReportDefaultsEntered", type: "png", site: "Excel", cat: "Function Wizard", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "ClearAfterReportDefaults", type: "png", site: "Addin", cat: "Pull Data", sub: "", report: "NorthwindCustomers", ribbon: "Simple", config: "Yes"}, {file: "ParameterCleared", type: "png", site: "Addin", cat: "Report", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "35", type: "png", site: "Addin", cat: "Report", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "36", type: "png", site: "Addin", cat: "Report", sub: "", report: "NorthwindCustomers", ribbon: "", config: "Yes"}, {file: "37", type: "png", site: "Addin", cat: "Report", sub: "", report: "NorthwindCustomers", ribbon: "", config: ""}]
description: This example uses the Customer Aging demo to show the creation of a Customer Aging Detail report that will have variable customer subtotaled sections, each having their respective invoice detail. You will use both the ReportRange() and ReportVariable() formulas to create the output.
---
* * *

## Overview

This example uses the [Customer Aging](/wAbout/Customer-Aging.html) demo to show the creation of a Customer Aging Detail report that will have variable customer subtotaled sections, each having their respective invoice detail. You will use both the [ReportRange()](/wIndex/ReportRange.html) and [ReportVariable()](/wIndex/ReportVariable.html) formulas to create the output.

<blockquote class=lab_info>
 If you are following the Training Labs, this is Lab 3.6. Note: The Report Library at Training Labs for this lab will be blank as you are creating a report from a new blank Excel sheet.
</blockquote>

### Building the Report

**Step 1:** You will begin by using Interject's [Report Builder](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#report-builder) to make a template for the report. Select NorthwindCustomers Data Portal and choose **Build Report Formula** to build the report.

![](/images/L-Create-CustAgingDetail/01.png)
<br>

When the template is complete, it should look like the one below.

![](/images/L-Create-CustAgingDetail/02.png)
<br>

**Step 2:** Add 3 rows above row 25. Highlight rows 19-21 and rick-click on row 19 and click **Insert**.

![](/images/L-Create-CustAgingDetail/05.png)
<br>

### ReportRange()

**Step 1:** You can select [Pull Data](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) to see which columns are available. Since the [ReportRange()](/wIndex/ReportRange.html) function does not have a Column Definition defined, it should show all the columns with their column names.

![](/images/L-Create-CustAgingDetail/06.png)
<br>

After you pull the report it will look similar to the one below.

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

Give row 10,12,14, and 16 heights of 6.75. The image below illustrates how to drag the row height to get close to 6.75. You can also type in example data in G11, H11. In K11 you can type in a label **Contact** : and **Phone:** in N11. Format both of these to be right-aligned.

![](/images/L-Create-CustAgingDetail/17.png)
<br>

**Step 9:** Now you need to create a formula that will total all of the detail that will later be populated between row 13 and 14. To create a total, type **=SUBTOTAL(9,L13:L14)** in L15. In cell H15 you will type **="Total Open Invoices For " & H11.** H11 represents the name of the customer, and by linking it to H11, the subtotal line will note the customer name again.

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

### ReportVariable()

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

**Step 6:** To define the second formula, add **=ReportVariable()** to cell C23 and click the fx button. The placement of this formula matters, since you want it to run after the ReportRange(). The [ReportRange()](/wIndex/ReportRange.html) will be pulled first to provide the list of customer sections, and then the [ReportVariable()](/wIndex/ReportVariable.html) will populate the invoices for each section.

![](/images/L-Create-CustAgingDetail/27.png)
<br>

**Step 7:** Using the Function Wizard, add **NorthwindCustomerInvoices** as the Data Portal.

![](/images/L-Create-CustAgingDetail/28.png)
<br>

**Step 8:** Next, you will specify the new Column Definition and Formatting Range. Type **2:2** into ColDefRange and **12:12** into FormatRange.

![](/images/L-Create-CustAgingDetail/29.png)
<br>

**Step 9:** With a ReportVariable, a RowDefRange is required, since it marks what data is to be included in each section. Type **A43:A44** into the RowDefRange. You will be placing the CustomerID in column A shortly.

![](/images/L-Create-CustAgingDetail/30.png)
<br>

**Step 10:** Now type **Param(C33,C34,C35,\"\")** to establish the parameters for the formula that match the previous ReportRange(). Both Report Formulas are setup to use the same filters. Click OK to finish.

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

### ReportDefaults()

**Step 1:** The parameters in C33:C36 are not cleared after clearing the data. You can setup a [ReportDefaults()](/wIndex/ReportDefaults.html) formula to have these cleared after you clear the data. ReportDefaults is an [event](/wIndex/Event-Functions-Landing.html) function, which means it triggers on a particular Interject event. Click on cell **G23** and enter **=ReportDefaults()** and click on the Function Wizard button.

![](/images/L-Create-CustAgingDetail/ReportDefaultsEntry.png)
<br>

**Step 2:** Enter **Pull** for **OnPullSaveOrBoth** field, **clear** for **OnClearRunOrBoth**, and **Pair("",C33:C36)** for **TransferPairs**. This will transfer "" into cells C33:C36 after a Pull-Clear event.

![](/images/L-Create-CustAgingDetail/ReportDefaultsEntered.png)
<br>

**Step 3:** Clear the report.

![](/images/L-Create-CustAgingDetail/ClearAfterReportDefaults.png)
<br>

Notice the parameters are reset.

![](/images/L-Create-CustAgingDetail/ParameterCleared.png)
<br>

### Formatting the Report

**Step 1:** You can go a step further and setup the formatting for the invoice detail and add a subtotal formula in row 12.

![](/images/L-Create-CustAgingDetail/35.png)
<br>

Type **=SUM(L12:O12)** into cell P12 to add the formula for total. You will also change the color on cell R12 and T12.

![](/images/L-Create-CustAgingDetail/36.png)
<br>

**Step 2:** After you add some headers–and move some cells, freeze panes, and formatting–the final product will look like this.

![](/images/L-Create-CustAgingDetail/37.png)
<br>

Finally, clear the report and save the file to the Report Library "My Favorites" folder. (For detailed instructions on how to save a file to the Report Library, see [here](/wAbout/ReportLibraryLinks.html).)
