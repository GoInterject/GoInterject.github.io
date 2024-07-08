---
title: "Drill: Inventory Report"
filename: "L-Drill-InventoryReport.md"
layout: custom
keywords: [drill, report, hyperlinks, walkthrough]
headings: ["Overview", "Unfreezing the Report", "Setting up the Drill", "Creating Hyperlinks as Drills"]
links: ["/wAbout/Inventory-Reports.html", "/wIndex/ReportDrill.html", "/wIndex/PairGroup.html", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html", "wGetStarted/L-Drill-FinancialReport.html"]
image_dir: "L-Drill-Inventory"
images: [
	{file: "01", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Inventory by Category", ribbon: "", config: ""}, 
	{file: "02", type: "png", site: "Excel", cat: "Freeze Panes", sub: "", report: "Inventory by Category", ribbon: "", config: ""}, 
	{file: "03", type: "png", site: "Excel", cat: "Function Wizard", sub: "", report: "Inventory by Category", ribbon: "", config: "Yes"}, 
	{file: "04", type: "png", site: "Excel", cat: "Function Wizard", sub: "", report: "Inventory by Category", ribbon: "", config: "Yes"}, 
	{file: "05", type: "png", site: "Excel", cat: "Function Wizard", sub: "", report: "Inventory by Category", ribbon: "", config: "Yes"}, 
	{file: "06", type: "png", site: "Excel", cat: "Function Wizard", sub: "", report: "Inventory by Category", ribbon: "", config: "Yes"}, 
	{file: "07", type: "png", site: "Excel", cat: "Function Wizard", sub: "", report: "Inventory by Category", ribbon: "", config: "Yes"}, 
	{file: "08", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Inventory by Category", ribbon: "", config: "Yes"}, 
	{file: "09", type: "png", site: "Excel", cat: "Right Click Menu", sub: "", report: "Inventory by Category", ribbon: "", config: "Yes"}, 
	{file: "10", type: "png", site: "Excel", cat: "Insert Hyperlink", sub: "", report: "Inventory by Category", ribbon: "", config: "Yes"}, 
	{file: "11", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Inventory by Category", ribbon: "", config: "Yes"}, 
	{file: "12", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Inventory by Category", ribbon: "", config: ""}, 
	{file: "13", type: "png", site: "Add-in", cat: "Pull Data", sub: "", report: "Inventory by Category", ribbon: "Simple", config: ""}, 
	{file: "14", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Inventory by Category", ribbon: "", config: ""}, 
	{file: "InventoryDrill", type: "gif", site: "Add-in", cat: "Data Drill", sub: "", report: "Inventory by Category", ribbon: "", config: ""}
	]
description: In this example, you will view drilling between reports using the same Inventory reports created during the Real World Inventory Walkthrough. You will set up a drill from the Inventory by Category tab to the Inventory by Detail tab of the workbook. You will also set up a hyperlink so the drill can be more intuitive to users.
---
* * *

## Overview

In this example, you will view drilling between reports using the same Inventory reports created during the [Real World Inventory Walkthrough](/wAbout/Inventory-Reports.html). You will set up a drill from the **Inventory by Category** tab to the **Inventory by Detail** tab of the workbook. You will also set up a hyperlink so the drill can be more intuitive to users.

<blockquote class=lab_info>
 If you are following the Training Labs, this report file can be found in the Report Library at Training Labs > Lab 4 Drilling To Data > Lab 4.2 Inventory Report.
</blockquote>

### Initializing the Report

**Step 1:** To begin, open the Interject Inventory Demo report from the Report Library.

![](/images/L-Drill-Inventory/01.png)
<br>

**Step 2:** Now unfreeze the panes to access the report formulas.

![](/images/L-Drill-Inventory/02.png)
<br>

**Step 3:** In this report the [ReportDrill()](/wIndex/ReportDrill.html) function has already been set up. To follow along in this guide, you will need to remove this function so you can set them up manually. Scroll up to the configuration rows and select the the drill and clear their contents.

![](/images/L-Drill-Inventory/02b.png)
<br>

**Step 4:** Also in this report, the hyperlinks have already been set up. You will set these links up manually [later](#creating-hyperlinks-as-drills). Therefore, select them and remove the hyperlinks.

![](/images/L-Drill-Inventory/02c.png)
<br>

The report is now ready to be set up for drilling.

### Setting up the Drill

**Step 1:** Type [**=ReportDrill()**](/wIndex/ReportDrill.html) into cell C5. Then, click the **fx** button to bring up the Function Wizard.

![](/images/L-Drill-Inventory/03.png)
<br>

**Step 2:** Now type **InventoryByDetail!C4** into the ReportCellToRun argument to specify the range you want to navigate to. You will be skipping the ReportCodeToRun argument since that is only used for drilling to other workbooks in the Report Library.

![](/images/L-Drill-Inventory/04.png)
<br>

**Step 3:** Next use the TransferPairs argument to note which cell values in the source worksheet will be transferred to the target worksheet during the drill operation. To do this, use special functions to pair the source cells to the target cells. Type [**PairGroup(Pair())**](/wIndex/PairGroup.html) in the TransferPairs argument to get it started.

![](/images/L-Drill-Inventory/05.png)
<br>

**Step 4:** In the Formula Bar, click within the word **Pair()** inside the text **PairGroup(Pair())** while the Function Wizard is open. See the illustration below. Once this is done, the Function Wizard will automatically change to help with the Pair() function. Type **B15:B23** in the From argument as shown below. Column B is where the CustomerID will be shown in the source report. By noting a range from row 15 to 23 in column B, Interject will expand that range to the data that is presented in this source report.

![](/images/L-Drill-Inventory/06.png)
<br>

**Step 5:** Next, select the Target argument and navigate to the **InventoryByDetail** tab. You want to place the CustomerID in cell E11 during the drill operation. Excel will fill in the formula automatically based on where you click. Click **OK** to finish updating the function and it will take you back to the source report.

![](/images/L-Drill-Inventory/07.png)
<br>

After pressing OK, the report formula should look as it does in the image below.

![](/images/L-Drill-Inventory/08.png)
<br>

### Creating Hyperlinks as Drills

**Step 1:** Now you are going to create hyperlinks for the drill. First, highlight the cells you want to setup the hyperlink, then right click and choose **Link**. In some versions of Excel it will show as **Hyperlink**.

![](/images/L-Drill-Inventory/09.png)
<br>

<blockquote class=highlight_note>
<b>Note:</b> Each drill will need to be linked individually, not all at once. If they are linked all at once then the drills will not work as it will drill everything at once, rather than one at a time.
</blockquote>
<br>

**Step 2:** In the Hyperlink pop-up window, you will select **Place in This Document**. Then select **ScreenTip**, type **Interject Drill**, and press OK. Although this technically sets up a hyperlink to cell A1 in the same tab, Interject will override the event so the Interject drill will activate.

![](/images/L-Drill-Inventory/10.png)
<br>

After you select **OK**, select on each of the remaining cells one by one and press **CTL-Y** to apply the last used action (in this case applying the link). Then the cells will be linked to the drill, as shown below.

![](/images/L-Drill-Inventory/11.png)
<br>

When the panes are refrozen, the report should look like the image below.

![](/images/L-Drill-Inventory/12.png)
<br>

**Step 3:** [Pull Data](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html) to see data for each category you just linked.

![](/images/L-Drill-Inventory/13.png)
<br>

Here, you have the report pulled and are ready to go.

![](/images/L-Drill-Inventory/14.png)
<br>

**Step 4:** Now that you have the data, and can click the hyperlink. As shown in the animated GIF below, click on **Totals for Grains/Cereals** and Interject will drill to the detail of that category in the target worksheet. Hyperlinks only show the Drill window when there is more than one drill option setup. In this case, you only setup one drill and it goes there automatically.

![](/images/L-Drill-Inventory/InventoryDrill.gif)
<br>

Hyperlinking Drills is a simple way to make Interject reports faster and more user-friendly. Click [here](wGetStarted/L-Drill-FinancialReport.html) for the Financial Report Drill walkthrough.

