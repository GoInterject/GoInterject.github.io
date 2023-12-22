---
title: "Create: Working with Pivot Tables"
layout: custom
keywords: [pivot table, walkthrough]
headings: ["Overview", "Building the Support Tab", "Building the Pivot Table", "Customizing the Pivot Table"]
description: Pivot tables are a flexible and valuable tool for analyzing data in Excel. Interject makes it easier to scale and distribute pivot tables. In this walkthrough you will set up a pivot table based on an Interject report.
---
* * *

## Overview

Pivot tables are a flexible and valuable tool for analyzing data in Excel. Interject makes it easier to scale and distribute pivot tables. In this walkthrough you will set up a pivot table based on an Interject report. There are a couple advantages to combining Interject with pivot tables. It provides the ability to build security into pivot table reports, users only see data relative to their credentials. Also, by allowing filters that are used at the database level, the amount of data in a user's pivot table is limited to data that is needed only for the analysis.

<blockquote class=lab_info>
 If you are following the Training Labs, this report file can be found in the Report Library at Training Labs > Lab 6 Special Features > Lab 6.1 Working with Pivot Tables.
</blockquote>

### Building the Support Tab

**Step 1:** In this exercise, you will use the Customer Collections Demo from a previous [walkthrough](/wAbout/Customer-Aging.html). This demo can be found in the Report Library under the Interject Demo folder as shown below.

![](/images/L-Create-PivotTable/01.png)
<br>

**Step 2:** When you open the report it will look like the screenshot below. Select the **CustomerAccountDetail** tab.

![](/images/L-Create-PivotTable/02.png)
<br>

**Step 3:** To build the Pivot table, right click the **CustomerAccountDetail** tab and make another copy so you can complete the following steps.

![](/images/L-Create-PivotTable/03.png)
<br>

**Step 4:** In the copy sheet dialog box, select **move to end** to make the copy at the end of the list of tabs.

![](/images/L-Create-PivotTable/04.png)
<br>

Now rename the tab something that represents the data, such as **TargetForPivotTable**.

![](/images/L-Create-PivotTable/05.png)
<br>

**Step 5:** Once the tab is copied, you are going to insert 3 columns, separating the date column (column I) into Month, Year, and Year-Mth columns.

In the Month column in cell J21, type **=TEXT(I21,\"mm\")**.

In the Year column in K21, type **=TEXT($I21,\"yyyy\")**.

In the Year-Mth column in L21, type **=TEXT(I21,\"yyyy-mm\")**.

![](/images/L-Create-PivotTable/06.png)
<br>

**Step 6:** Next, you are going to add two parameters to the report by inserting two rows below **Show Unapplied Only** and labeling them **Begin Date:** and **End Date:**.

![](/images/L-Create-PivotTable/07.jpg)
<br>

**Step 7:** Select cell C14 and copy it to C18 and C19.

![](/images/L-Create-PivotTable/08.jpg)
<br>

**Step 8:** Use the quick tools menu in the interject ribbon. In the dialog box select **Freeze/UnFreeze Panes (current tab)** and click **Run and Close**.

![](/images/L-Create-PivotTable/09.jpg)
<br>

**Step 9:** Select the report formula in cell C4, then select the function wizard.

![](/images/L-Create-PivotTable/10.jpg)
<br>

**Step 10:** In the parameters section of the dialog box change the Parameters field to this: **Param(C14,,C16,,C18,C19)**.

![](/images/L-Create-PivotTable/11.jpg)
<br>

**Step 11:** Hide rows C15, and C17 since they will not be needed for this report but exist as possible parameters in the stored procedure.

![](/images/L-Create-PivotTable/12.jpg)
<br>

**Note:** The parameter section of the report should look like the following screenshot.

![](/images/L-Create-PivotTable/13.jpg)
<br>

**Step 12:** Now that you have entered the fields, you can use [**Pull Data**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) on the report, filtering for companies with **Market** in their names. First type **Market** in the filter cell C1 and then **Pull Data**.

![](/images/L-Create-PivotTable/14.jpg)
<br>

**Step 13:** Highlight the cells B21 to M122. **Important:** Be sure to include row 21, the column labels on the top of the range, and include the bottom anchor row, which is one row past the last customer record. The anchor row is important since it will grow and shrink as the data is pulled and cleared. Exclude the Paid? column from the table range.

![](/images/L-Create-PivotTable/14b.png)
<br>

**Step 14:** In the screenshot below, you can see there are four steps to preparing the contents of the pivot table.

1. Select the Insert ribbon as noted below.
2. Within the Insert ribbon, click the PivotTable menu item so the Create PivotTable window appears.
3. Ensure the range **TargetForPivotTable!$B$21:$M$122** is selected in the **Select a table or range** box.
4. Click the OK button, and a new tab will be created with the new pivot table.

![](/images/L-Create-PivotTable/15.png)
<br>

### Building the Pivot Table

**Step 1:** From here you can pivot in any way needed.

![](/images/L-Create-PivotTable/16.png)
<br>

**Step 2:** Use the PivotTable pane on the right to place Year in the columns. Company Name and Type go to rows, Country goes in Filters. Then, choose the Amount to be summed. Your pivot table should match the screenshot below.

![](/images/L-Create-PivotTable/17.png)
<br>

**Step 3:** Rename the tab "Pivot" and you can customize the look by clicking **Design** and then expand the table previews and select a color theme.

![](/images/L-Create-PivotTable/17b.png)
<br>

### Customizing the Pivot Table

**Step 1:** Prepare the pivot table worksheet to interact with the Interject worksheet. That way the data can be updated based on select filters, and security can be considered. You will insert the configuration rows at the top as you normally do with Interject reports, but Report Formulas is the only section being used. You will also add a Title and hide the grids.

![](/images/L-Create-PivotTable/18.png)
<br>

**Step 2:** Now set up the [ReportRun()](/wIndex/ReportRun.html) function. This will cause the target sheet to perform a [**Pull Data**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html) or [**Clear Data**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html) when Pull Data is triggered from the pivot table worksheet.

![](/images/L-Create-PivotTable/19.png)
<br>

**Step 3:** In the ReportCellToRun argument, select the **TargetForPivotTable** tab and select the ReportRange() formula in C4.

![](/images/L-Create-PivotTable/20.png)
<br>

**Step 4:** Type **True** in the **RunEntireWorksheet** argument. And type **Pull** in the OnAction argument. This will trigger the second worksheet to run only when [**Pull Data**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) is performed on the current pivot table worksheet.

![](/images/L-Create-PivotTable/21.png)
<br>

On a second line under row 4 (insert new row if needed), you will do the same for the second ReportRun(). This time, however, type **PullClear** in the OnAction argument so that the pivot table clear function works correctly.

![](/images/L-Create-PivotTable/22.png)
<br>

**Step 5:** Now that the ReportRange() fields are prepared, you can add filters for the searches. Rename the title to **Pivot Table For Customer Transactions** as seen below. Also, add the filters Company Name, Contact Name, CustomerID, Show Unapplied Only, Begin Date, and End Date. The filters in the **Pivot** tab should match the filters in the **TargetForPivotTable** tab.

**Note**: Remember there are 2 hidden rows that you have to match.

![](/images/L-Create-PivotTable/23.png)
<br>

**Step 6:** Navigate to cell C14 of the **TargetForPivotTable** tab. Ensure the type is General.

![](/images/L-Create-PivotTable/23b.png)
<br>

**Step 7:** For the Company Name, type **=if(Pivot!B12=\"\",\"\",Pivot!B12)**. This formula will make the filters equal between pages and if the Pivot worksheet filter is blank, it will be blank as well. Normally, Excel will make the result **0** if not handled with this formula. Copy cell C14 and paste it through C19 so the other filters are linked as well.

![](/images/L-Create-PivotTable/24.png)
<br>

**Step 8:** Now go back to the pivot table and make sure it is working properly. Enter the following filters to check the pull.

![](/images/L-Create-PivotTable/25.png)
<br>

Now you can see that the table only pulled data from transactions occurring in 1997, so the filters, ReportRun(), and pivot table are working as they should.

![](/images/L-Create-PivotTable/26.png)
<br>

For more ways to work with a pivot table, see the [pivot table section](/wAbout/Customer-Aging.html#CustomerAging-pivot) on the customer aging walkthrough.
