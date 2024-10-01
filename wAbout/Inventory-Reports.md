---
title: Inventory Reports
filename: "Inventory-Reports.md"
layout: custom
keywords: [inventory, reports, drill, detail, return, walkthrough]
headings: ["Overview", "Navigating to the Inventory Reports", "Drilling to the Detail", "Return From Drill and Re-Drill", "Alternate Inventory Example"]
links: ["/wAbout/Report-Library-Basics.html", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html", "/wGetStarted/Drilling-Between-Reports.html", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#return-from-drill", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html", "/wGetStarted/L-Modify-InventoryReport.html"]
image_dir: "Inventory"
images: [
	{file: "image2017-6-27_17-6-52", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "Interject Inventory Demo", ribbon: "Simple", config: ""}, 
	{file: "02", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Inventory By Category", ribbon: "", config: ""}, 
	{file: "image2017-6-12_17-32-49", type: "png", site: "Add-in", cat: "Pull Data", sub: "", report: "Inventory By Category", ribbon: "Simple", config: ""}, 
	{file: "04", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Inventory By Category", ribbon: "", config: ""}, 
	{file: "2.01-drilling-drill-on-grains-and-cereals", type: "gif", site: "Add-in", cat: "Progress Bar", sub: "", report: "Inventory By Category, Inventory Detail", ribbon: "Simple", config: ""}, 
	{file: "06", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Inventory Detail", ribbon: "", config: ""}, 
	{file: "07", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Inventory Detail", ribbon: "Simple", config: ""}, 
	{file: "08", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Inventory By Category", ribbon: "", config: ""}, 
	{file: "3.02-return-from-drill-drill-on-beverages", type: "gif", site: "Add-in", cat: "Progress Bar", sub: "", report: "Inventory By Category, Inventory Detail", ribbon: "Simple", config: ""}, 
	{file: "image2017-8-14_7-54-29", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Inventory Detail", ribbon: "", config: ""}, 
	{file: "11", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Inventory Detail", ribbon: "", config: ""}, 
	{file: "image2017-6-9_14-21-7", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Inventory By Category", ribbon: "", config: ""}, 
	{file: "image2017-6-9_14-22-56", type: "png", site: "Add-in", cat: "Pull Data", sub: "", report: "Inventory By Category", ribbon: "Simple", config: ""}, 
	{file: "14", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Inventory By Category", ribbon: "", config: ""}
	]
description: This lab is a basic inventory example for tracking product quantities. In this walkthrough, you will open a summary of our product categories and total quantities. You will then drill into the Inventory Detail tab to view specific products within that category
---
* * *

## Overview

This lab is a basic inventory example for tracking product quantities. In this walkthrough, you will open a summary of our product categories and total quantities. You will then drill into the Inventory Detail tab to view specific products within that category. There is also a secondary inventory option which allows us to view all of the categories, and the products within them, in a single sheet.

<blockquote class=lab_info>
 If you are following the Training Labs, this report file can be found in the Report Library at Training Labs > Lab 1 Real World Walkthroughs > Lab 1.2 Inventory Reports.
</blockquote>

### Navigating to the Inventory Reports

**Step 1:** Navigate to the Inventory report page inside the Interject Demos folder of the [Report Library](/wAbout/Report-Library-Basics.html) . The Report Library is a central place for publishing reporting templates. It is versioned and centrally located.

![](/images/Inventory/01.png)
<br>

**Step 2:** Check inventory by opening the workbook to see the different categories available.

![](/images/Inventory/02.png)
<br>

To access the totals of in-stock items, just pull the data into the spreadsheet using the [**Pull Data**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html) operation.

![](/images/Inventory/03.png)
<br>

Now you have an overview of totals for all inventoried categories, as seen below.

![](/images/Inventory/04.png)
<br>

In this example, though, you need to find out more than the total; you need to see how much grain you have, which means you need more a detailed view of current inventory.

To find the data, use the Drill function for inventory by detail.

### Drilling to the Detail

**Step 1:** To drill, select the category you want to drill to then give it a double click. For this example, you are going to drill on **Grains/Cereals** . In this instance use the hyperlink drill which only requires the click of the mouse to be drilled on. [Click here](/wGetStarted/Drilling-Between-Reports.html) to read more on Drills.

![](/images/Inventory/2.01-drilling-drill-on-grains-and-cereals.gif)
<br>

Drilling will take us to InventoryByDetail, which will automatically pull all the items in stock within that category.

![](/images/Inventory/06.png)
<br>

From here, you can see exactly what is logged in-stock at the time of the pull: **Grains/Cereals** in this example.
### Return From Drill and Re-Drill

You also need to gather a report of our beverage inventory.

**Step 1:** Select the [**Return From Drill**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#return-from-drill) Button to go back to the sheet you drilled from.

![](/images/Inventory/07.png)
<br>

This will bring us back to the previous tab.

![](/images/Inventory/08.png)
<br>

**Step 2:** Now repeat the steps from the first drill by clicking the Beverages category. Since this is a hyperlink drill the report will automatically take us deeper.

![](/images/Inventory/3.02-return-from-drill-drill-on-beverages.gif)
<br>

This will automatically pull the detail page again, but this time with products from the new category selected in the previous step.

![](/images/Inventory/10.png)
<br>

### Alternate Inventory Example

Now you will use a report that shows all the categories and their details in one sheet, without having to drill back and forth between the two sheets. To accomplish this, you are going to use InvByCategory_WithDetail.

**Step 1:** You need to open the WithDetails tab.

![](/images/Inventory/11.png)
<br>

When cleared, the sheet looks similar to the first category sheet.

![](/images/Inventory/12.png)
<br>

**Step 2:** Simply pull the data using the [**Pull Data**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html) button to view the inventory data.

![](/images/Inventory/13.png)
<br>

Now you can view every category and its detail all in one page, without any drills.

![](/images/Inventory/14.png)
<br>

That is all there is to it. To learn more about modifying this report, [click here](/wGetStarted/L-Modify-InventoryReport.html).
