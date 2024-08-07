---
title: The Three Ways to Drill
filename: "L-Drill-TheThreeWays.md"
layout: custom
keywords: [menu, hyperlink, drill, double click drill, Interject_DoubleClick, custom properties]
headings: ["Overview", "The Menu Method", "The Hyperlink Method", "The Double Click Method"]
links: ["/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#drill-on-data", "/wAbout/Customer-Aging.html", "/wAbout/Inventory-Reports.html", "/wGetStarted/L-Drill-InventoryReport.html#creating-hyperlinks-as-drills", "/wAbout/Customer-Aging.html", "https://support.office.com/en-us/article/View-or-change-the-properties-for-an-Office-file-21D604C2-481E-4379-8E54-1DD4622C6B75"]
image_dir: "L-Drill-TheThreeWays"
images: [
	{file: "01", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""}, 
	{file: "02", type: "png", site: "Add-in", cat: "Data Drill", sub: "", report: "Customer Aging Summary", ribbon: "Advanced", config: ""}, 
	{file: "03", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Detail", ribbon: "", config: ""}, 
	{file: "04", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Inventory by Category", ribbon: "", config: ""}, 
	{file: "InventoryDrill", type: "gif", site: "Add-in", cat: "Data Drill", sub: "", report: "Inventory by Category", ribbon: "Simple", config: ""}, 
	{file: "06", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""}, 
	{file: "DrillToAgingDetail", type: "gif", site: "Add-in", cat: "Data Drill", sub: "", report: "Customer Aging Summary", ribbon: "Simple", config: ""}, 
	{file: "08", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Detail", ribbon: "", config: ""}, 
	{file: "properties", type: "png", site: "Excel", cat: "Info", sub: "Advanced Properties", report: "", ribbon: "", config: ""}
	]
description: Interject facilitates three different ways to drill. Each method is easy to choose the best one different situations.
---
* * *

## Overview

Interject facilitates three different ways to drill. Each method is easy to choose the best one different situations.

### The Menu Method

The [Drill on Data](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#drill-on-data) menu item is available in every report containing a drill function. For this example, you will drill using the [Customer Aging demo](/wAbout/Customer-Aging.html).

![](/images/L-Drill-TheThreeWays/01.png)
<br>

There are four steps to using the menu.

1. First, select the cell to drill on. In this example you will chose theSave-a-lot Markets customer's 90 days balance.
2. Select the **Drill on Data** menu in the Interject ribbon.
3. Select the drill option in the Data Drill window. In this example, chose **Drill to Aging Detail**.
4. Complete the drill by clicking **Do Drill**.

![](/images/L-Drill-TheThreeWays/02.png)
<br>

This automatically takes you to the desired destination and usually pulls the data as well.

![](/images/L-Drill-TheThreeWays/03.png)
<br>

### The Hyperlink Method

The hyperlink drill method is another option. It is one of the simplest ways for a user to drill in Interject and makes it intuitive for the user to know where drills are available. For this example, you will drill using the [Inventory Reports Demo](/wAbout/Inventory-Reports.html) seen below.

![](/images/L-Drill-TheThreeWays/04.png)
<br>

By clicking the hyperlink cell, it will automatically trigger the Interject drill. Since there is only one drill option, the Data Drill window will not appear as in previously shown examples. If multiple drill options are present, the Data Drill window will appear so the user can select which drill option to use. The animated GIF below illustrates how the hyperlink drill works in Interject.

![](/images/L-Drill-TheThreeWays/InventoryDrill.gif)
<br>

It is that simple. To know how to set up a hyperlink drill for one of the reports, [click here](/wGetStarted/L-Drill-InventoryReport.html#creating-hyperlinks-as-drills) to see how it was set up in the example above.

### The Double Click Method

The double click method is similar to the hyperlink method in that it reduces the number of button clicks. But there is a configuration step to activate it for a workbook. For this example, you will be using the [Customer Aging](/wAbout/Customer-Aging.html) Summary to do the drill.

![](/images/L-Drill-TheThreeWays/06.png)
<br>

The animated GIF below illustrates how the double click method works. The user simply double clicks on the cell to drill on and the Data Drill window appears. In this example, there are multiple drill options so the Data Drill window appears to let the user choose which to use. If only one drill option was available, Interject would have went directly to the target.

![](/images/L-Drill-TheThreeWays/DrillToAgingDetail.gif)
<br>

Again, you should see the target report as shown below.

![](/images/L-Drill-TheThreeWays/08.png)
<br>

To enable a workbook with the double click method, the custom properties of the Excel workbook must include a property **Interject_DoubleClick**, and it must be set to **True**.

On the file menu:

1. Click **Info**
2. Click **Properties**
3. Click **Advanced Properties**
4. Click the **Custom** tab
5. Enter **Interject_DoubleClick** for the Name
6. Enter **True** for the Value
7. Click **Add**

![](/images/L-Drill-TheThreeWays/properties.png)
<br>

For more on how to update custom properties, refer to the following link:

[https://support.office.com/en-us/article/View-or-change-the-properties-for-an-Office-file-21D604C2-481E-4379-8E54-1DD4622C6B75](https://support.office.com/en-us/article/View-or-change-the-properties-for-an-Office-file-21D604C2-481E-4379-8E54-1DD4622C6B75){:target="_blank"}{:rel="noopener noreferrer"}
