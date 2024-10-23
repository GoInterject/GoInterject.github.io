---
title: "Drill: Customer Aging Report"
filename: "L-Drill-CustomerAging.md"
layout: custom
keywords: [drill, create, build, customer aging, walkthrough]
headings: ["Overview", "Unfreezing the Excel Sheet", "Build the Drill", "Final Results"]
links: ["/wFunctions/ReportDrill.html", "/wFunctions/PairGroup.html", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html", "/wAbout/ReportLibraryLinks.html"]
image_dir: "L-Drill-CustAging"
images: [
	{file: "01", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""}, 
	{file: "02", type: "png", site: "Excel", cat: "Freeze Panes", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""}, 
	{file: "03", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: "Yes"}, 
	{file: "04", type: "png", site: "Excel", cat: "Function Wizard", sub: "", report: "Customer Aging Summary", ribbon: "", config: "Yes"}, 
	{file: "05", type: "png", site: "Excel", cat: "Function Wizard", sub: "", report: "Customer Aging Summary", ribbon: "", config: "Yes"}, 
	{file: "06", type: "png", site: "Excel", cat: "Function Wizard", sub: "", report: "Customer Aging Summary", ribbon: "", config: "Yes"}, 
	{file: "07", type: "png", site: "Excel", cat: "Function Wizard", sub: "", report: "Customer Aging Summary", ribbon: "", config: "Yes"}, 
	{file: "08", type: "png", site: "Excel", cat: "Function Wizard", sub: "", report: "Customer Aging Summary", ribbon: "", config: "Yes"}, 
	{file: "09", type: "png", site: "Excel", cat: "Function Wizard", sub: "", report: "Customer Aging Summary", ribbon: "", config: "Yes"}, 
	{file: "10", type: "png", site: "Add-in", cat: "Pull Data", sub: "", report: "Customer Aging Summary", ribbon: "Simple", config: "Yes"}, 
	{file: "11", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""}, 
	{file: "13", type: "png", site: "Add-in", cat: "Data Drill", sub: "", report: "Customer Aging Summary", ribbon: "Simple", config: ""}, 
	{file: "14", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Orders", ribbon: "", config: ""}
	]
description: In this example, you will be setting up a simple drill to the customer orders history. It is a great use case for creating your first drill.
---
* * *

## Overview

In this example, you will be setting up a simple drill to the customer orders history. It is a great use case for creating your first drill.

<blockquote class=lab_info>
 If you are following the Training Labs, this report file can be found in the Report Library at Training Labs > Lab 4 Drilling To Data > Lab 4.1 Customer Aging.
</blockquote>

### Initializing the Report

**Step 1:** To begin, open the Interject Customer Collections report from the Report Library.

![](/images/L-Drill-CustAging/01.png)
<br>

**Step 2:** Unfreeze the panes. Go to the **View** tab, find the **Freeze Pane** option, and select **Unfreeze Panes**.

![](/images/L-Drill-CustAging/02.png)
<br>

**Step 3:** In this report the [ReportDrill()](/wFunctions/ReportDrill.html) functions may have been already set up. To follow along in this guide, you will need to remove these functions so you can set them up manually. Scroll up to the configuration rows and select the three drills and clear their contents.

![](/images/L-Drill-CustAging/03.png)
<br>

### Build the Drill

**Step 1:** To begin, select cell C7 and type **=ReportDrill()**. Then click the **fx** button to bring up the Function Wizard.

![](/images/L-Drill-CustAging/04.png)
<br>

**Step 2:** Now select the ReportCellToRun argument and type in **CustomerOrderHistory!C10** . This is the cell location of the Report Formula in the target report that you will be drilling to. In the screenshot below, you can see the specific cell you are drilling to in the CustomerOrderHistory tab.

You are going to skip the ReportCodeToRun argument, since that is used only when drilling to a separate workbook from the Report Library.

![](/images/L-Drill-CustAging/05.png)
<br>

**Step 3:** Next, we will use the TransferPairs argument to note which cell values in the source worksheet will be transferred to the target worksheet during the drill operation. To do this we use special functions to pair the source cells to the target cells. Type [**PairGroup(Pair())**](/wFunctions/PairGroup.html) in the TransferPairs argument to get it started. You will return to add more to this argument.

![](/images/L-Drill-CustAging/06.png)
<br>

**Step 4:** Then you will specify the name for the drill. In this case you will type **"Drill to Customer Order History"**.

![](/images/L-Drill-CustAging/07.png)
<br>

**Step 5:** Complete the TransferPairs argument. In the Formula Bar, click inside the word **Pair()** within the text **PairGroup(Pair())**. See the illustration below. Once this is done, the Function Wizard will automatically change to help with the Pair() function. Type **B22:B24** in the **From** argument. This is the column where the CustomerID is going to be presented in the source report. By noting a range from row 22 to 24 in column B, Interject will expand that range to the data presented in this source report.

![](/images/L-Drill-CustAging/08.png)
<br>

**Step 6:** Select the Target input field and navigate to the **CustomerOrderHistory** tab, where you will choose which cell you want to receive the value. In this case you want C23. Excel should automatically fill in the argument with the text **CustomerOrderHistory!C23** . Click OK to finish updating the function, and it will automatically go back to the source worksheet.

![](/images/L-Drill-CustAging/09.png)
<br>

**Step 7:** Now that you have created the drill, you can use [**Pull Data**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html) to bring in the customers to the source worksheet.

![](/images/L-Drill-CustAging/10.png)
<br>

Below is when the data is pulled.

![](/images/L-Drill-CustAging/11.png)
<br>

### Final Results

**Step 1:** To demonstrate the new drill, click on one of the customer rows and select **Drill on Data**. Click on the button **Do Drill** and Interject will navigate to the target worksheet, bring in the CustomerID selected by the filter, then run the report. The screenshot below should resemble the result.

![](/images/L-Drill-CustAging/13.png)
<br>

You completed the drill. You can return to the source worksheet, **Customer Aging** , and re-freeze the panes, clear the report, and save it. Now it is ready to be published to the users.

![](/images/L-Drill-CustAging/14.png)
<br>

Finally, clear the report and save the file to the Report Library "My Favorites" folder. (For detailed instructions on how to save a file to the Report Library, see [here](/wAbout/ReportLibraryLinks.html).)
