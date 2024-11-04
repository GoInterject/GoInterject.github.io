---
title: "Create: Inventory Fixed Report"
filename: "L-Create-InventoryFixed.md"
layout: custom
keywords: [fixed, inventory, report, create, jWorkbookProperty, northwind fixed, run on open, walkthrough]
headings: ["Overview", "Building the Report", "Setting up Run on Open", "jWorkbookProperty()"]
links: ["/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#report-builder", "/wIndex/Common-Dataportal-Index.html", "/wFunctions/ReportRange.html", "/wFunctions/ReportFixed.html", "/wFunctions/ReportFixed.html", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data", "/wAbout/ReportLibraryLinks.html", "/wGetStarted/L-Create-RunOnOpen.html", "/wFunctions/jWorkbookProperty.html"]
image_dir: "L-Create-InventoryFix"
images: [
	{file: "01", type: "png", site: "Add-in", cat: "Report Builder", sub: "", report: "", ribbon: "Simple", config: ""}, 
	{file: "02", type: "png", site: "Add-in", cat: "Report Builder", sub: "", report: "NorthwindFixed", ribbon: "Simple", config: ""}, 
	{file: "03", type: "png", site: "Add-in", cat: "Report", sub: "", report: "NorthwindFixed", ribbon: "", config: "Yes"}, 
	{file: "04", type: "png", site: "Add-in", cat: "Report", sub: "", report: "NorthwindFixed", ribbon: "", config: "Yes"}, 
	{file: "05", type: "png", site: "Add-in", cat: "Report", sub: "", report: "NorthwindFixed", ribbon: "", config: "Yes"}, 
	{file: "08", type: "png", site: "Add-in", cat: "Report", sub: "", report: "NorthwindFixed", ribbon: "", config: "Yes"}, 
	{file: "06", type: "png", site: "Excel", cat: "Function Wizard", sub: "", report: "NorthwindFixed", ribbon: "", config: "Yes"}, 
	{file: "07", type: "png", site: "Excel", cat: "Function Wizard", sub: "", report: "NorthwindFixed", ribbon: "", config: "Yes"}, 
	{file: "09", type: "png", site: "Excel", cat: "Function Wizard", sub: "", report: "NorthwindFixed", ribbon: "", config: "Yes"}, 
	{file: "10", type: "png", site: "Add-in", cat: "Report", sub: "", report: "NorthwindFixed", ribbon: "", config: "Yes"}, 
	{file: "11", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Inventory By Category", ribbon: "", config: "Yes"}, 
	{file: "12", type: "png", site: "Excel", cat: "Freeze Panes", sub: "", report: "Inventory By Category", ribbon: "", config: ""}, 
	{file: "13", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Inventory By Category", ribbon: "", config: ""}, 
	{file: "14", type: "png", site: "Add-in", cat: "Pull Data", sub: "", report: "Inventory By Category", ribbon: "Simple", config: ""}, 
	{file: "15", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Inventory By Category", ribbon: "", config: ""}, 
	{file: "16", type: "png", site: "Add-in", cat: "Ribbon", sub: "", report: "", ribbon: "Simple", config: ""}, 
	{file: "17", type: "png", site: "Excel", cat: "Info", sub: "Advanced Properties", report: "", ribbon: "", config: ""}, 
	{file: "18", type: "png", site: "Excel", cat: "Advanced Properties", sub: "Custom", report: "", ribbon: "", config: ""}, 
	{file: "19", type: "png", site: "Excel", cat: "Advanced Properties", sub: "Custom", report: "", ribbon: "", config: ""}, 
	{file: "20", type: "png", site: "Excel", cat: "Advanced Properties", sub: "Custom", report: "", ribbon: "", config: ""}, 
	{file: "SaveToReportLibrary", type: "png", site: "Add-in", cat: "Report Library", sub: "Right Click Menu", report: "Inventory By Category", ribbon: "", config: ""}, 
	{file: "15", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Inventory By Category", ribbon: "", config: ""}, 
	{file: "jWorkbookPropertySettingsClick", type: "png", site: "Excel", cat: "Info", sub: "", report: "Inventory By Category", ribbon: "", config: ""}, 
	{file: "jWorkbookPropertySettings", type: "png", site: "Excel", cat: "Advanced Properties", sub: "Summary", report: "", ribbon: "", config: ""}, 
	{file: "jWorkbookPropertyEntered", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Inventory By Category", ribbon: "", config: ""}
	]
description: In this page, you will go through the process of building a fixed Inventory report from scratch using the ReportFixed() function.
---
* * *

##  Overview

In this page, you will go through the process of building a fixed Inventory report from scratch using the ReportFixed() function.

<blockquote class=lab_info>
  If you are following the Training Labs, this is Lab 3.3. Note: The Report Library at Training Labs for this lab will be blank as you are creating a report from a new blank Excel sheet.
</blockquote>

###  Building the Report

**Step 1:** Begin like you did when creating the Customer Aging report, with the Interject [Report Builder](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#report-builder). It is where you select the  [Data Portal](/wIndex/Common-Dataportal-Index.html) that is needed for this particular report.

![](/images/L-Create-InventoryFix/01.png)
<br>

**Step 2:** For this Inventory report, choose the NorthwindFixed Data Portal and click **Build Report Formula**.

![](/images/L-Create-InventoryFix/02.png)
<br>

After the report is built, it will look like the one below. There are no parameters involved with this report, so none are listed after row 14.

![](/images/L-Create-InventoryFix/03.png)
<br>

Delete rows 11 through 24 since they are not needed for this lesson. The page should look as illustrated below.

![](/images/L-Create-InventoryFix/04.png)
<br>

**Step 3:** Because [ReportRange()](/wFunctions/ReportRange.html) is the most used pull function, the report builder builds one automatically. However, in this report you will be using the [ReportFixed()](/wFunctions/ReportFixed.html) function. Clear the ReportRange function in cell C6.

![](/images/L-Create-InventoryFix/05.png)
<br>

**Step 4:** A fixed report requires specific values to be entered in a row definition column. Enter the following categories as seen below. In cell B27, you also added a **Leftovers** section that is a special Interject feature, a Row Definition marking the start of a section that will include any data not matching the earlier fixed rows. This is helpful in ensuring all data is presented.

![](/images/L-Create-InventoryFix/08.png)
<br>

**Step 5:** In C6, type **=ReportFixed()**, then click the **fx** button to bring up the Function Wizard as shown below.

![](/images/L-Create-InventoryFix/06.png)
<br>

In order to bring in the correct data you will need to designate a Data Portal. The Data Portal for this example is **NorthwindFixed**.

![](/images/L-Create-InventoryFix/07.png)
<br>

**Step 6:** In a [ReportFixed](/wFunctions/ReportFixed.html) function you need to define the Column Definition and Row Definition ranges. Using the Function Wizard, use B16:B28 for the  RowDefRange . For Column Definitions, use row 2 by typing **2:2** in the ColDefRange argument.

![](/images/L-Create-InventoryFix/09.png)
<br>

**Step 7:** Now define the Column Definitions that are available in the Data Portal. Type **ProductTypeCount** in G2 and **UnitsInStock** in H2.

![](/images/L-Create-InventoryFix/10.png)
<br>

**Step 8:** In this step, add column labels, report titles, borders, and subtotals. Change the report to match.

![](/images/L-Create-InventoryFix/11.png)
<br>

**Step 9:** Freeze the report panes so that just the report area is shown for users. In previous examples jFreezePanes() functions were used, but in this page use the standard Freeze Panes feature in Excel. Adjust the worksheet's vertical and horizontal scroll bars until the report is positioned like below. Select cell D15 and use the View menu to set Freeze Panes as seen below.

![](/images/L-Create-InventoryFix/12.png)
<br>

The final product should look similar to the example below.

![](/images/L-Create-InventoryFix/13.png)
<br>

**Step 10:** Now select [**Pull Data**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) to view the data in the report.

![](/images/L-Create-InventoryFix/14.png)
<br>

Your final data pull should look like this. You may need to do additional formatting to match the output.

![](/images/L-Create-InventoryFix/15.png)

<br>

### Setting up Run on Open

**Step 1** Click on **File** in the Excel Ribbon to bring up the file screen.

![](/images/L-Create-InventoryFix/16.png)
<br>

**Step 2** Under Info, select **Advanced Properties** in the Properties dropdown. The Properties window will open.

![](/images/L-Create-InventoryFix/17.png)
<br>

**Step 3** Under the **Custom** tab find the **Name** textbox and type **Interject_RunOnOpen**. The **Type** field should be **Text**.

![](/images/L-Create-InventoryFix/18.png)
<br>

**Step 4** The **Value** box below takes two options: **True** or T:*TabName* **True** will will cause Excel to run on the first tab seen on open. Specify the tab name to default to that tab.

**Option 1** If you would like to run on the first tab seen, set value to **True** and click **Add**.

![](/images/L-Create-InventoryFix/19.png)
<br>

**Option 2** If you would like to run on a specific tab, set the value to **T:*TabName*** and click **Add**.

In this case, we want to pull CustomerAging on open, so type **T:InventoryByCategory** and that tab will be pulled.

![](/images/L-Create-InventoryFix/20.png)
<br>

**Step 5** Save the file to the Report Library "My Favorites" folder. (For detailed instructions on how to save a file to the Report Library, see [here](/wAbout/ReportLibraryLinks.html).)

![](/images/L-Create-InventoryFix/SaveToReportLibrary.png)
<br>

**Step 6** Close and reopen the file through the Report Library, and Excel will auto-pull the report.

![](/images/L-Create-InventoryFix/15.png)
<br>

For a full guide using a different report, refer to the [Run on Open Example](/wGetStarted/L-Create-RunOnOpen.html).

### jWorkbookProperty()

Finally, we will add a finishing touch with the [jWorkbookProperty()](/wFunctions/jWorkbookProperty.html) function. This function pulls information saved in the Excel file properties into the report. To start, click on File on the top menu and then click **Info**, **Properties**, and then **Advanced Properties**.

![](/images/L-Create-InventoryFix/jWorkbookPropertySettingsClick.png)
<br>

Enter some details into the Properties window.

![](/images/L-Create-InventoryFix/jWorkbookPropertySettings.png)
<br>

In cell **H11** enter **=jWorkbookProperty("company")** and see the results.

![](/images/L-Create-InventoryFix/jWorkbookPropertyEntered.png)
<br>
