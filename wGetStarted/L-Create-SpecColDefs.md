---
title: "Create: Special Column Definitions"
filename: "L-Create-SpecColDefs.md"
layout: custom
keywords: [hyperlink, comment, dropdown, list, column definitions, validation, walkthrough]
headings: ["Overview", "Special Cell Value Comment", "Special Cell Value Hyperlink", "Special Cell Value Validation List", "Stacking Special Cell Types"]
links: ["/wGetStarted/L-Modify-CustomerAging.html"]
image_dir: "L-Create-SpecColDefs"
images: [
	{file: "01", type: "jpg", site: "Add-in", cat: "Quick Tools", sub: "", report: "Customer Credits", ribbon: "Advanced", config: ""}, 
	{file: "02", type: "jpg", site: "Add-in", cat: "Pull Data", sub: "", report: "Customer Credits", ribbon: "Advanced", config: ""}, 
	{file: "03", type: "jpg", site: "Add-in", cat: "Report", sub: "", report: "Customer Credits", ribbon: "", config: ""}, 
	{file: "04", type: "jpg", site: "Add-in", cat: "Report", sub: "", report: "", ribbon: "", config: "Yes"}, 
	{file: "05", type: "jpg", site: "Add-in", cat: "Pull Data", sub: "", report: "Customer Credits", ribbon: "Advanced", config: ""}, 
	{file: "06", type: "jpg", site: "Add-in", cat: "Report", sub: "", report: "Customer Credits", ribbon: "", config: "Yes"}, 
	{file: "07", type: "jpg", site: "Add-in", cat: "Report", sub: "", report: "Customer Credits", ribbon: "", config: "Yes"}, 
	{file: "08", type: "jpg", site: "Add-in", cat: "Pull Data", sub: "", report: "Customer Credits", ribbon: "Advanced", config: "Yes"}, 
	{file: "09", type: "jpg", site: "Add-in", cat: "Report", sub: "", report: "Customer Credits", ribbon: "", config: "Yes"}, 
	{file: "10", type: "jpg", site: "External", cat: "Browser", sub: "", report: "Customer Credits", ribbon: "", config: "Yes"}, 
	{file: "11", type: "jpg", site: "Add-in", cat: "Report", sub: "", report: "Customer Credits", ribbon: "", config: "Yes"}, 
	{file: "12", type: "jpg", site: "Add-in", cat: "Report", sub: "", report: "Customer Credits", ribbon: "", config: "Yes"}, 
	{file: "13", type: "jpg", site: "Add-in", cat: "Report", sub: "", report: "Customer Credits", ribbon: "Advanced", config: "Yes"}, 
	{file: "14", type: "jpg", site: "Add-in", cat: "Pull Data", sub: "", report: "Customer Credits", ribbon: "Advanced", config: "Yes"}, 
	{file: "15", type: "jpg", site: "Add-in", cat: "Report", sub: "", report: "Customer Credits", ribbon: "", config: "Yes"}, 
	{file: "16", type: "jpg", site: "External", cat: "Browser", sub: "", report: "Customer Credits", ribbon: "", config: "Yes"}
	]
description: Interject's Special Column Definitions are a convenient way you can customize a cell and provide additional features to your reports.
---
* * *

## Overview

Interject's Special Column Definitions are a convenient way you can customize a cell and provide additional features to your reports. There are a number of options available:

1. **Adding a cell comment**
2. **Adding a hyperlink to a web address**
3. **Adding a custom drop down validation to each row**

![](/images/L-Create-SpecColDefs/00.png)
<br>

You can even add multiple cell values, for example a comment and a hyperlink.

These additional features are added by editing the Column Definition Row. The Column Definition Row is a row that designates, and filters, the placement of information. For example, if your report is presenting the field "Company Name", your Column Definition would have a cell with the value "Company Name". To add one of these features to the cells in a column where the report is populated you use an identifier such as **AddComm** for comments, **hLink** for hyperlinks, and **Valuelist** for a drop down list. 

This example uses the Customer Credits report, which is in the [Customer Aging](/wGetStarted/L-Modify-CustomerAging.html).

<blockquote class=lab_info>
 If you are following the Training Labs, this report file can be found in the Report Library at Training Labs > Lab 5 Advanced Features > Lab 5.4 Special Column Definitions.
</blockquote>

### Special Cell Value Comment

A comment is often used to note more detailed information about the data in a cell. Comments are useful when the information contained within them are not required but need to be referenced when you put your mouse over the cell. In this example you will add comments to the InvoiceTotal column to note the customer's last unpaid invoice.

To start, unfreeze the panes.

![](/images/L-Create-SpecColDefs/01.jpg)
<br>

In the Company Name field in cell **C21** input **Market** and Pull the data.

![](/images/L-Create-SpecColDefs/02.jpg)
<br>

The report looks like this:

![](/images/L-Create-SpecColDefs/03.jpg)
<br>

Select cell **G2** and input **InvoiceTotal Addcomm:LastUnpaidInvoice**.

![](/images/L-Create-SpecColDefs/04.jpg)
<br>

<blockquote class=highlight_note>
<b>Note:</b> <b>Addcomm</b> designates the type of special column that you are using and <b>LastUnpaidInvoice</b> is the actual content in the comment.
</blockquote>
<br>

Pull the data.

![](/images/L-Create-SpecColDefs/05.jpg)
<br>

Place your cursor over cell **G27** and review the comment that is placed in the cell. Notice that the **InvoiceTotal** column was pulled as it was before the changes but it has a comment associated with it that now details the last unpaid invoice of the customer.

![](/images/L-Create-SpecColDefs/06.jpg)

### Special Cell Value Hyperlink

Select cell **C2** and input **CompanyName hlink:MapsURL**.

![](/images/L-Create-SpecColDefs/07.jpg)
<br>

<blockquote class=highlight_note>
<b>Note:</b> The <b>MapsURL</b> segment of the <b>hlink</b> string designates a column built in the SQL stored procedure. The hlink string only links to a whole column of data you cannot concatenate values in Excel, but can in the SQL stored procedure as long as it results in a single column.
</blockquote>
<br>

Pull the data.

![](/images/L-Create-SpecColDefs/08.jpg)
<br>

**CompanyName** is still pulled normally but instead of the normal dataset, it will create a hyperlink formula. The **Link Location** goes to Google Maps and searches for the full address for that company. This way the location data is accessible but does not overcrowd the information while the **Friendly Name** of the URL is the **Company Name**.

![](/images/L-Create-SpecColDefs/09.jpg)
<br>

Select cell **C27** and notice that it takes you to Google Maps.

![](/images/L-Create-SpecColDefs/10.jpg)
<br>

<blockquote class=highlight_note>
<b>Note:</b> The addresses may not be valid as they are fabricated data from the Northwind Database.
</blockquote>
<br>

### Special Cell Value Validation List

Inserting data validation dropdown lists are similar to the other special column definitions. When used they create dropdown lists using comma delimited strings, with each value inside the string separated by commas. In this example you will add data validation to the account freeze column to limit possible input values.

For this example, use **AccountFreeze** in cell **K2**.

Select the cell, then input **AccountFreeze Valuelist:FreezeOptions**. Pull the Data again.

![](/images/L-Create-SpecColDefs/11.jpg)
<br>

**AccountFreeze** will be shown as a blank value but upon selecting the cell, you can see that there is a drop down list with the options **Yes** or **No**. If there was a comma separated list instead of **FreezeOptions** , the value list would only include what is in the comma separated list.

![](/images/L-Create-SpecColDefs/12.jpg)
<br>

Through using this feature with Interject, you can have a different validation list for every row in your report. Even though this is not shown in this example, if you wanted to select a city name inside of a state, it is possible to have the validation list only show the cities available within the state which would have to change based on the row the data is on.

### Stacking Special Cell Types

Excel allows users to have multiple special cell values attributed to a single cell. This is also the case when using Interject integration. You can add multiple cell value types in the column definitions of the report.

For this example, use **Company Name** cell **C2**

Select the cell, then input **CompanyName hlink:MapURL** **Addcomm:AddressLong**

![](/images/L-Create-SpecColDefs/13.jpg)
<br>

Pull the data.

![](/images/L-Create-SpecColDefs/14.jpg)
<br>

Hover your mouse over cell **C27** and it will have a comment attributed to the cell along with the hyperlink.

![](/images/L-Create-SpecColDefs/15.jpg)
<br>

Click on the hyperlink in cell **C27** and notice that the functionality of the hyperlink is unaltered and that the comment brought back the address that is used in the google map search.

![](/images/L-Create-SpecColDefs/16.jpg)
<br>
