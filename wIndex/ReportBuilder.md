---
title: Report Builder
filename: "ReportBuilder.md"
layout: custom
keywords: []
headings: ["Overview"]
links: []
image_dir: "ReportBuilder"
images: [
    {file: "", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}
]
description: 
---
* * *

## Overview

The Report Builder is a tool in the Interject Addin to easily create a report based on the settings in a [Data Portal](/wPortal/Data-Portals.html).

![](/images/ReportBuilder/Ribbon.png)
<br>

### Building A Report

Once a Data Portal is set up, you can quickly create a template report that will pull from it using the Report Builder.

To begin, open the Report Builder form.

![](/images/ReportBuilder/OpenReportBuilder.png)
<br>

Scroll through the list of Data Portals to **Northwind Customers**.

![](/images/ReportBuilder/ReportBuilderNorthwindCustomers.png)
<br>

Finally click on **Build Report Formula**.

![](/images/ReportBuilder/ReportBuilder.png)
<br>

The report is built:

![](/images/ReportBuilder/NorthwindCustomersReport.png)
<br>

### Helper Default Columns

By default, this initial report is set up to return all the columns from the data source. 

![](/images/ReportBuilder/AllColumnsReturned.png)
<br>

You can customize what specific columns are returned by entering a comma delimited list in the **Helper Default Columns** field when setting up the Data Portal:

![](/images/ReportBuilder/CommaDelimitedList.png)
<br>

Now when you build a report, only those columns will be set up:

![](/images/ReportBuilder/SelectedColumnsBuilt.png)
<br>

In addition, each column is set up with a custom dropdown where you can filter the data.

![](/images/ReportBuilder/ColumnFilters.png)
<br>

### Report Builder Section

The Report Builder Section is a section where you can customize each Data Portal parameter for greater flexibility in how the Report Builder builds the report. You can access this section by clicking the **More** button on the parameter you want to customize:

![](/images/ReportBuilder/FormulaParameters.png)
<br>

The section contains 4 entries:

- **Helper Name** : This adds a friendly name for the report parameter input in the Report Builder. Otherwise the parameter name is used, which has no spaces.
- **Helper Default** : This inserts a default value into the cell of the Excel report when using the Report Builder.
- **Options** : Use a comma separated list to provide the Excel user with a drop down list of options.
- **Comments** : This inserts an Excel comment, with our text, into the cell of the Excel report when using the Report Builder.

![](/images/ReportBuilder/ReportBuilderSection.png)
<br>

Now when you build the report, notice the results.

1. The parameter name is customized.
2. There is a note on the cell.
3. The parameter has a customized drop down list.
4. The parameter is defaulted to a value.

![](/images/ReportBuilder/CustomizedParameter.png)
<br>
