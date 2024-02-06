---
title: View SQL Test for ActiveCell
filename: "View-SQL.md"
layout: custom
keywords: [report, investigate, activity, logs, error, user support]
headings: ["Overview"]
links: []
image_dir: "ViewSqlTest"
images: [{file: "29", type: "jpg", site: "Addin", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: "Yes"}, {file: "30", type: "jpg", site: "Addin", cat: "Ribbon", sub: "System", report: "Customer Aging Summary", ribbon: "Advanced", config: "Yes"}, {file: "SQLQuery", type: "png", site: "Addin", cat: "View SQL Test For ActiveCell", sub: "", report: "", ribbon: "", config: ""}, {file: "SQLQueryTest", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}]
description: The View SQL Test for ActiveCell tool can be used to track down issues with the SQL stored procedures being called by an Interject report function.
---
* * *

## Overview

The **View SQL Test for ActiveCell** tool can be used to track down issues with the SQL stored procedures being called by an Interject report function. Only ReportRange(), ReportVariable(), ReportFixed(), and ReportSave() report functions are supported by **View SQL Test for ActiveCell**.

**Step 1:** Select a cell containing a supported Interject report function:

![](/images/ViewSqlTest/29.jpg)
<br>

**Step 2:** On the **Administration** tab in the Interject Ribbon, click **View SQL Test for ActiveCell** under the **System** drop-down menu. A popup window will appear with a test SQL query:

![](/images/ViewSqlTest/30.jpg)
<br>

This SQL query can be run using any T-SQL environment (i.e. _Microsoft SQL Server Management Studio_ ). Running the query in non-T-SQL environments may require modification of the query. The result will be a table or list of tables in SQL Server or an error message which can be used to see exactly what data is being pulled/saved to/from a report.

![](/images/ViewSqlTest/SQLQuery.png)
<br>

![](/images/ViewSqlTest/SQLQueryTest.png)
<br>
