---
title: Customer Aging
filename: "Customer-Aging.md"
layout: custom
keywords: [customer, aging, modify, drill, save, detail, pivot table, walkthrough]
headings: ["Overview", "Navigating to the Aging Summary", "Drilling Into the Aging Detail", "Saving the Data", "Moving to a Pivot Table"]
links: ["/wAbout/Report-Library-Basics.html", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#drill-on-data", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#drill-on-data", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#save-data", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#save-data", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data", "/wAbout/Inventory-Reports.html"]
image_dir: "Walkthrough-CustAging"
images: [
	{file: "01", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "Interject Customer Collections", ribbon: "Simple", config: ""}, 
	{file: "02", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "Simple", config: ""}, 
	{file: "03", type: "png", site: "Add-in", cat: "Pull Data", sub: "", report: "Customer Aging Summary", ribbon: "Simple", config: ""}, 
	{file: "04", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""}, 
	{file: "05", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""}, 
	{file: "06", type: "png", site: "Add-in", cat: "Pull Data", sub: "", report: "Customer Aging Summary", ribbon: "Simple", config: ""}, 
	{file: "07", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""}, 
	{file: "08", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""}, 
	{file: "09", type: "png", site: "Add-in", cat: "Data Drill", sub: "Drill to Aging Detail", report: "Customer Aging Summary", ribbon: "Simple", config: ""}, 
	{file: "10", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Detail", ribbon: "", config: ""}, 
	{file: "11", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Detail", ribbon: "", config: ""}, 
	{file: "12", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Detail", ribbon: "", config: ""}, 
	{file: "13", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Detail", ribbon: "", config: ""}, 
	{file: "14", type: "png", site: "Add-in", cat: "Save Data", sub: "", report: "Customer Aging Detail", ribbon: "Simple", config: ""}, 
	{file: "15", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Detail", ribbon: "", config: ""}, 
	{file: "16", type: "png", site: "Add-in", cat: "Pull Data", sub: "", report: "Customer Aging Detail", ribbon: "Simple", config: ""}, 
	{file: "17", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Detail", ribbon: "", config: ""}, 
	{file: "18", type: "png", site: "Add-in", cat: "Pull Data", sub: "", report: "Customer Aging Detail", ribbon: "Simple", config: ""}, 
	{file: "19", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Detail", ribbon: "", config: ""}, 
	{file: "20", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Detail", ribbon: "", config: ""}, 
	{file: "21", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Pivot Table For Customer Transactions", ribbon: "", config: ""}, 
	{file: "22", type: "png", site: "Add-in", cat: "Pull Data", sub: "", report: "Pivot Table For Customer Transactions", ribbon: "Simple", config: ""}, 
	{file: "23", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Pivot Table For Customer Transactions", ribbon: "", config: ""}, 
	{file: "24", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Pivot Table For Customer Transactions", ribbon: "", config: ""}, 
	{file: "25", type: "gif", site: "Excel", cat: "Pivot Table Fields", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "26", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Pivot Table For Customer Transactions", ribbon: "", config: ""}
	]
description: In this walkthrough, you will open a basic aging summary and modify it to fit your specific needs. You will then drill into the details tab, take notes on any unpaid invoices, then save them back to the database.
---
* * *

## Overview

This lab is a basic Customer Aging demonstration for tracking invoices for multiple customers. In this walkthrough, you will open a basic aging summary and modify it to fit your specific needs. You will then drill into the details tab, take notes on any unpaid invoices, then save them back to the database. This Detail report will also provide the data needed to drill further into each order and customer.

<blockquote class=lab_info>
 If you are following the Training Labs, this report file can be found in the Report Library at Training Labs > Lab 1 Real World Walkthoughs > Lab 1.1 Customer Aging.
</blockquote>

### Navigating to the Aging Summary

**Step 1:** Open the report **Interject Customer Collections** under the Interject Demos in the [Report Library](/wAbout/Report-Library-Basics.html).

![](/images/Walkthrough-CustAging/01.png)
<br>

This will bring up the Customer Aging Summary.

![](/images/Walkthrough-CustAging/02.png)
<br>

**Step 2:** You can retrieve the data by clicking [**Pull Data**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) in the Interject menu and clicking **Pull Data** in the subsequent popup.

![](/images/Walkthrough-CustAging/03.png)
<br>

This will populate the data into the spreadsheet.

![](/images/Walkthrough-CustAging/04.png)
<br>

**Step 3:** Since you are not concerned with _all_ the customers right now-- you only need the status of those in the Market sector--filter **Market** in the **Company Name** filter.

![](/images/Walkthrough-CustAging/05.png)
<br>

Now use [Pull Data](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) again to refresh the data.

![](/images/Walkthrough-CustAging/06.png)
<br>

**Step 4:** Once the companies are pulled, you can see that **Save-a-lot-Markets** has invoices 90 days overdue!

![](/images/Walkthrough-CustAging/07.png)
<br>

### Drilling Into the Aging Detail

**Step 1** : Now, use the [**Drill**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#drill-on-data) operation on the Customer Aging Detail report for a closer look at the overdue invoices. Here you can select any cell on the row below because as long as you select a cell on the row with the overdue invoices the [**Drill**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#drill-on-data) will take us to the details of that client's invoices.

![](/images/Walkthrough-CustAging/08.png)
<br>

Once that cell is selected you can drill deeper into the data. Below are the descriptions for each step.

 1. First, select cell or row to drill.
 2. Select the Drill operation in the Interject Ribbon.
 3. Select the desired drill you would like to perform , in this case you are selecting **Drill to Aging Detail**.
 4. Complete the drill by selecting **Do Drill**.

![](/images/Walkthrough-CustAging/09.png)
<br>

This allows us to see which invoices have not been paid. Looking deeper into the report, notice that more recent invoices are paid, but the customer is struggling to pay past-dated invoices.

![](/images/Walkthrough-CustAging/10.png)
<br>

**Step 2:** Notice that Jose mailed a check for the first invoice and it should arrive on the 18th. However, you would still need to call about the other invoice and add a comment on what was discussed.

![](/images/Walkthrough-CustAging/11.png)
<br>

**Step 3:** Now that you have talked with Jose, you find out that he will be mailing the check with the overdue funds tomorrow. To keep from forgetting, you can add a comment to your report.

![](/images/Walkthrough-CustAging/12.png)
<br>

### Saving the Data

**Step 1:** Now that the notes are written down, you need click the [**Save Data**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#save-data) operation to save the notes back to the database.

![](/images/Walkthrough-CustAging/13.png)
<br>

**Step 2:** To do this, click the [**Save Data**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#save-data) menu in the Interject Ribbon menu and the **Save Data** in the popup.

![](/images/Walkthrough-CustAging/14.png)
<br>

Notice the Save Results column and ensure that it was updated correctly and there were no errors.

![](/images/Walkthrough-CustAging/15.png)
<br>

**Step 3:** Once this is complete, use [**Clear**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) and [**Pull**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) the Customer Aging Detail report to ensure the note is saved in the database.

![](/images/Walkthrough-CustAging/16.png)
<br>

Clicking the [**Clear**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) operation will remove any data that was pulled into the spreadsheet.

![](/images/Walkthrough-CustAging/17.png)
<br>

Notice that the filters are not cleared, so a re-pull is easy.

**Step 4:** Now you will use the [**Pull Data**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) operation the data again to ensure it is completely refreshed.

![](/images/Walkthrough-CustAging/18.png)
<br>

You will see that the saved data was pulled back into the spreadsheet, confirming that it was saved correctly.

![](/images/Walkthrough-CustAging/19.png)
<br>

Now, you can move to a Pivot Table so that you can easily manipulate the data provided by the Customer Aging tab.

### Moving to a Pivot Table

**Step 1:** First, navigate to the Pivot table tab.

To do this Click on the **PivotTableAndReportRun** tab.

![](/images/Walkthrough-CustAging/20.png)
<br>

For this example,you are going to use a Company Name **Market** filter to narrow our search just like you did for Customer Aging.

![](/images/Walkthrough-CustAging/21.png)
<br>

**Step 2:** Now lets use [**Pull Data**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) to retrieve the data.

![](/images/Walkthrough-CustAging/22.png)
<br>

From pulling, you can see that Save-a-lot-Markets has already paid their invoices for 1998 but are behind on previous invoices.

![](/images/Walkthrough-CustAging/23.png)
<br>

If you want even more specific detail though, such as month-to-month information. You can alter the Pivot table to accommodate this.

**Step 3:** Click anywhere inside the Pivot table to bring up the table's field list.

![](/images/Walkthrough-CustAging/24.png)
<br>

**Step 4:** Now you can drag the Year-Mth box in the Row Labels to the column labels.

![](/images/Walkthrough-CustAging/25.gif)
<br>

Notice that you do not need to use the[**Pull Data**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) is needed to view the new layouts.

![](/images/Walkthrough-CustAging/26.png)
<br>

From here you can see that Save-a-lot Markets had large invoices in July and August that are not payed. However, you can also see the effort to pay off those invoices in the following months by the over-payments they have made. Take note of this activity and proceed to the next report: [Inventory Report Walk-Through.](/wAbout/Inventory-Reports.html)
