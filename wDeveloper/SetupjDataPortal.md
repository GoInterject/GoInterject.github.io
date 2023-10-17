---
title: Setting up the jDataPortal
layout: custom
keywords: [portal, connection, override, command]
description: The jDataPortal is a powerful Interject function that not only allows users to customize the connection to an Interject Data Portal. In addition to establishing a connection to a Portal, users can also override certain parameters of the Portal to customize their reporting needs.
---
* * *

## Overview

The [jDataPortal](/wIndex/jDataPortal.html) is a powerful Interject function that not only allows users to customize the connection to an Interject Data Portal. In addition to establishing a connection to a Portal, users can also override certain parameters of the Portal to customize their reporting needs.

### Setup jDataPortal

In this section, you will open a report and change the Data Portal to a jDataPortal.

Begin by opening up the Customer Collections report.

![](/images/SetupjDataPortal/CustomerCollectionsReport.png)
<br>

In order to access the Interject configuration area,unfreeze the panes via the Quick Tools menu.

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

The **DataResultNumber** is the second parameter for the jDataPortal. This parameter specifies the particular data set you want returned. For instance, if the stored procedure for the data portal returns three queries, entering 2 for this parameter will return the second query to your report.

You can also enter negative numbers to specify the query in relation to the last query. For example, -1 will return the last query listed in your stored procedure. To illustrate, the following chart shows an example for a stored procedure returning four data sets:

| Query<br>Position | Postive<br>Reference | Negative<br>Reference |
|---|---|---|
| Query 1 | 1 | -4 |
| Query 2 | 2 | -3 |
| Query 3 | 3 | -2 |
| Query 4 | 4 | -1 |

### Order By

The **OrderBy** parameter accepts a valid SQL statement that will be applied to the data result. In this section you will add a value for this parameter in order to order the results.

First select the jDataPortal function by putting the cursor inside the name and click the **fx** button to bring up Excel's Function Wizard.

![](/images/SetupjDataPortal/SelectFx.png)
<br>

In the **OrderBy** field, enter:

```
"[CustomerName] DESC"
```

![](/images/SetupjDataPortal/AddOrderBy.png)
<br>

Now Pull the data again and notice the results are ordered by Company Name in descending order.

![](/images/SetupjDataPortal/ResultsOrdered.png)
<br>

### Filter

Like the **OrderBy** parameter, the **Filter** parameter also accepts a valid SQL statement that will be applied to the results. 

Bring up the Function Wizard again and for the **Filter** parameter, enter

```
"[ContactTitle] LIKE '%Manager%'"
```

![](/images/SetupjDataPortal/AddFilter.png)
<br>

Pull the data again and notice the results are filtered to only included entries whose Contact Title includes "Manager".

![](/images/SetupjDataPortal/ResultsFiltered.png)
<br>

### Overriding a Connection

With the **ConnectionOverride** parameter, a jDataPortal function can use a different Interject [Data Connection](/wPortal/Data-Connections.html) when accessing the Data Portal. Making the same Data Portal for different connections is redundant. This parameter makes it possible to host one Data Portal with many different possible connections and thus accommodate your unique reporting needs.

To use, simply enter the name of the connection from the Portal site that you want to use:

![](/images/SetupjDataPortal/ConnectionOverride.png)
<br>

### Overriding a Command

Similar to the **ConnectionOverride**, the **CommandOverride** can override the command (stored procedure) stored in the Data Portal. Again, you only need one Data Portal to access different stored procedures and thus cut down on the required maintenance of having to manage many different portals. 

Command overrides are can only be performed by a ClientAdmin or SysAdmin [role](/wPortal/INTERJECT-Roles.html).

![](/images/SetupjDataPortal/CommandOverride.png)
<br>
