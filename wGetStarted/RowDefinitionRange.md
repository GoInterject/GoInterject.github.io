---
title: Advanced Principles for the Row Definition Range
filename: "RowDefinitionRange.md"
layout: custom
keywords: [Rowdef name, multi-column, multiple, aggregation]
headings: ["Overview", "Multi-Column RowDef Feature", "Opening and Displaying the Report", "RowDef Items", "Information Sent to Data Source", "Multi-Column Row Definitions"]
links: ["/wGetStarted/Fixed-and-Variable-Reports.html", "/wIndex/InterjectConfig_Settings.html", "/wFunctions/ReportFixed.html#function-arguments", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#system"]
image_dir: "RowDefinitionRange"
images: [
	{file: "PLReportRL", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""},
	{file: "PullData", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""},
	{file: "Unfreeze", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""},
	{file: "ExpandGroups", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""},
	{file: "PLTrendRowDefItems", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""},
	{file: "FixedRowDefRange", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""},
	{file: "VariableRowDefRange", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""},
	{file: "ViewSQLClick", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""},
	{file: "ViewSQLFixedSingleColumn", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""},
	{file: "RowDefItems2", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""},
	{file: "CategoryName", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}
]
description: 
---

## Overview

Interject provides [Fixed and Variable Reports](/wGetStarted/Fixed-and-Variable-Reports.html) that populate data based on a Row Definition. Traditionally this is a single column range defined in the report. The Interject Add-in uses this range to query the data. Only records that contain the row def items defined  inside this range are returned.

Starting with version 2.5.0, Interject provides the option of defining multiple columns in the row definition range. With this multi-column feature, the combination of row def items provide a unique *key* for matching up the data.

Another feature that has been added is the ability to define multiple row def items within a single column. This is typically a list separated by a delimiter. The list feature provides a way to further filter the data for a Variable Report. For a Fixed Report, Interject can either return the last record that matches this criteria or aggregate the records in a sum.

To accommodate these new features, a new setting is introduced where one can set the default delimiter and choose to either auto-sum up the list or return the last record. The setting is a named range called [InterjectConfig_Settings](/wIndex/InterjectConfig_Settings.html) that you define inside the Excel file.

## Multi-Column RowDef Feature

The following example illustrates this feature.

### Opening and Displaying the Report

**Step 1:** Begin by opening the Report Library and open the "PL by Location" report:

![](/images/RowDefinitionRange/PLReportRL.png)
<br>

**Step 2:** Pull the data.

![](/images/RowDefinitionRange/PullData.png)
<br>

**Step 3:** Unfreeze the Report.

![](/images/RowDefinitionRange/Unfreeze.png)
<br>

**Step 4:** To expand all the groups, click the "2" in top left of the report:

![](/images/RowDefinitionRange/ExpandGroups.png)
<br>

Notice this report is a Variable Report with the RowDef Items defined in column B:

![](/images/RowDefinitionRange/PLTrendRowDefItems.png)
<br>



- Show Single district on one column
- Show Multiple Districts each on their own column
- Go back to single district column
- Add a second col definition in the row def called locations (new multi col feature)	
- Show Districts on each row in the detail
    - Group locations together on separate group (rowdef)
    - Show how to combine locations using comma delimiter (new aggregation feature) and express this work in a single RowDef column config as well.


## RowDef Items

The Fixed and Variable Reports take a parameter called "RowDefRange" (for more information about this parameter, see [ReportFixed](/wFunctions/ReportFixed.html#function-arguments)). This parameter defines a range that includes a set of individual values which are "RowDef Items". Here is an example of a Fixed Report with a single column of row def items (B16:B28):

![](/images/RowDefinitionRange/FixedRowDefRange.png)
<br>

In the case of a Variable Report, the RowDef Items define the summary rows of the data. Note the two RowDef Items "Beverages" and "Condiments" are summary rows in the screenshot below. They define the entire group of detail rows that follow:

![](/images/RowDefinitionRange/VariableRowDefRange.png)
<br>

### Information Sent to Data Source

When requesting a pull data inside a report, Interject wraps up the pertinent information from the report into XML and sends it to the data source. To understand the RowDef Items further you can view this information. Click the cell that contains the report function, then the [System menu](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#system) and then "View SQL Test For ActiveCell":

![](/images/RowDefinitionRange/ViewSQLClick.png)
<br>

Notice the RowDef Items in this report:

![](/images/RowDefinitionRange/ViewSQLFixedSingleColumn.png)
<br>

Beginning with Interject version 2.5.0, a second set of RowDef Items are defined as well that give greater flexibility on how to handle these items:

![](/images/RowDefinitionRange/RowDefItems2.png)
<br>

It is up to the data source to process this XML information in a way that generates the desired data returned to the report. In order for Interject to match up the data for these RowDef Items, there needs to be a column returned from the data source called "RowDefName." If the data source does not return a column called "RowDefName", Interject will use the value defined in the Column Definition range in the same column as the RowDef Items. For example, this report can return a column called "CategoryName" to match the RowDef Items:

![](/images/RowDefinitionRange/CategoryName.png)
<br>

### Multi-Column Row Definitions


If there are multiple columns defined in the RowDef range, then each row may have a set of values in each column. The combination of these values in each row constitutes a single RowDef Item. 



-	Default naming convention a column “RowDefName” with values of R00001, R00002, … (Interject uses this column to determine which group the detail row belongs to)

-	For multi column row def, need a way to mark the RowDefName  ( 
-	How to handle the RowDef items in the stored procedure with fancy aggregation (e.g. ellipses or !)
