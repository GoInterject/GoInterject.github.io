---
title: Setting Up the jDataPortal
filename: "SetupjDataPortal.md"
layout: custom
keywords: [portal, connection, override, command]
headings: ["Overview", "Setup jDataPortal", "Result Sets", "Order By", "Filter", "Overriding a Connection", "Overriding a Command"]
links: ["/wFunctions/jDataPortal.html", "https://learn.microsoft.com/en-us/dotnet/api/system.data.dataview.sort", "https://learn.microsoft.com/en-us/dotnet/api/system.data.dataview.rowfilter", "https://learn.microsoft.com/en-us/dotnet/api/system.data.datacolumn.expression", "/wPortal/Data-Connections.html", "https://portal.gointerject.com/DataPortals.html", "/wPortal/INTERJECT-Roles.html"]
image_dir: "SetupjDataPortal"
images: [
	{file: "CustomerCollectionsReport", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "Interject Customer Collections", ribbon: "", config: ""}, 
	{file: "UnFreezePanes", type: "png", site: "Add-in", cat: "Quick Tools", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "ReportFunctionSelected", type: "png", site: "Add-in", cat: "Report", sub: "", report: "", ribbon: "", config: "Yes"}, 
	{file: "FormulaBar", type: "png", site: "Add-in", cat: "Report", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "PullData", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: "Yes"}, 
	{file: "SelectFx", type: "png", site: "Add-in", cat: "Report", sub: "", report: "", ribbon: "", config: "Yes"}, 
	{file: "AddOrderBy", type: "png", site: "Excel", cat: "Function Arguments", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "ResultsOrdered", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""}, 
	{file: "AddFilter", type: "png", site: "Excel", cat: "Function Arguments", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "ResultsFiltered", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""}, 
	{file: "ConnectionOverride", type: "png", site: "Excel", cat: "Function Arguments", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "CommandOverride", type: "png", site: "Excel", cat: "Function Arguments", sub: "", report: "", ribbon: "", config: ""}
	]
description: The jDataPortal is a powerful Interject function that not only allows users to customize the connection to an Interject Data Portal. In addition to establishing a connection to a Portal, users can also override certain parameters of the Portal to customize their reporting needs.
---
* * *

## Overview

The [jDataPortal](/wFunctions/jDataPortal.html) is a powerful Interject function that not only allows users to not only establish and customize the connection to an Interject Data Portal, but also override certain parameters of the Portal to customize reporting needs.

### Setup jDataPortal

In this section, you will open a report and change the Data Portal to a jDataPortal.

Begin by opening up the Customer Collections report.

![](/images/SetupjDataPortal/CustomerCollectionsReport.png)
<br>

In order to access the Interject configuration area, unfreeze the panes via the Quick Tools menu.

![](/images/SetupjDataPortal/UnFreezePanes.png)
<br>

Select the report function.

![](/images/SetupjDataPortal/ReportFunctionSelected.png)
<br>

In the formula bar, change the **DataPortal** parameter from "Northwind Customers" to:

```
jDataPortal("Northwind Customers")
```

![](/images/SetupjDataPortal/FormulaBar.png)
<br>

Enter "Market" for the Company Name filter and Pull the data.

![](/images/SetupjDataPortal/PullData.png)
<br>

### Result Sets

The **DataResultNumber** is the second parameter for the jDataPortal. This parameter specifies the particular data set you want returned. For instance, if the stored procedure for the data portal returns 4 queries, entering 2 for this parameter will return the 2nd query to your report.

You can also enter negative numbers to specify the query in relation to the last query. For example, -1 will return the last query listed in your stored procedure. To illustrate, the following chart shows an example for a stored procedure returning 4 data sets:

| Query<br>Position | Postive<br>Reference | Negative<br>Reference |
|---|---|---|
| Query 1 | 1 | -4 |
| Query 2 | 2 | -3 |
| Query 3 | 3 | -2 |
| Query 4 | 4 | -1 |

### Order By

The **OrderBy** parameter accepts comma separated values of column names that will be used to sort the data result set. In this section you will add a value for this parameter to order the results.

First select the jDataPortal function by putting the cursor inside the name and click the **fx** button to bring up Excel's Function Wizard.

![](/images/SetupjDataPortal/SelectFx.png)
<br>

In the **OrderBy** field, enter:

```
"[CustomerName] DESC"
```

![](/images/SetupjDataPortal/AddOrderBy.png)
<br>

Now Pull the data again and notice the results are in descending order by Company Name.

![](/images/SetupjDataPortal/ResultsOrdered.png)
<br>

The **OrderBy** parameter accepts multiple column names (e.g. "CompanyName, ContactTitle"). Some key points:

* This parameter is not case sensitive
* Brackets may or may not surround column names
* Result sets are sorted in the order of the columns listed
* Sorts in ascending order (ASC) unless descending order (DESC) is specified

For more information, see Microsoft's [DataView.Sort](https://learn.microsoft.com/en-us/dotnet/api/system.data.dataview.sort){:target="_blank"}{:rel="noopener noreferrer"}.

### Filter

The **Filter** parameter accepts valid expressions that will be applied to the results. 

Bring up the Function Wizard again and for the **Filter** parameter, enter:

```
"[ContactTitle] LIKE '%Manager%'"
```

![](/images/SetupjDataPortal/AddFilter.png)
<br>

Pull the data again and notice the results are filtered to only included entries whose Contact Title includes "Manager".

![](/images/SetupjDataPortal/ResultsFiltered.png)
<br>

The **Filter** parameter excepts multiple expressions. Some key points:

* This parameter is not case sensitive
* Brackets may or may not surround column names
* Multiple expressions can be added using the keywords 'AND' or 'OR'
* Terms can be compared using '<', '>', '<=', '>=', '<>' or '='

For more information, see Microsoft's [DataView.RowFilter](https://learn.microsoft.com/en-us/dotnet/api/system.data.dataview.rowfilter){:target="_blank"}{:rel="noopener noreferrer"}. For more information about syntax and keywords, see [Expressions](https://learn.microsoft.com/en-us/dotnet/api/system.data.datacolumn.expression){:target="_blank"}{:rel="noopener noreferrer"}.

### Overriding a Connection

With the **ConnectionOverride** parameter, a jDataPortal function can use a different Interject [Data Connection](/wPortal/Data-Connections.html) when accessing the Data Portal. Making the same Data Portal for different connections is redundant. This parameter makes it possible to host one Data Portal with many different possible connections and thus accommodate your unique reporting needs.

To use, simply enter the name of the connection from the [Portal site](https://portal.gointerject.com/DataPortals.html) that you want to use:

![](/images/SetupjDataPortal/ConnectionOverride.png)
<br>

### Overriding a Command

Similar to the **ConnectionOverride**, the **CommandOverride** can override the command (stored procedure) stored in the Data Portal. Again, you only need one Data Portal to access different stored procedures and thus cut down on the required maintenance of having to manage many different portals. 

Command overrides can only be performed by a ClientAdmin [role](/wPortal/INTERJECT-Roles.html).

![](/images/SetupjDataPortal/CommandOverride.png)
<br>
