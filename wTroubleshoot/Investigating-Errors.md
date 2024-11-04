---
title: Investigating Report Errors
filename: "Investigating-Errors.md"
layout: custom
keywords: [report, error, user support, progress bar window, activity log]
headings: ["Overview", "Using the Progress Bar Window", "Using Activity Logs"]
links: ["/wDeveloper/L-Dev-Error-Handling.html"]
image_dir: "InvestigatingReportErrors"
images: [
	{file: "01", type: "jpg", site: "Add-in", cat: "Progress Bar", sub: "Error Popup", report: "Customer Aging Summary", ribbon: "", config: ""}, 
	{file: "02", type: "jpg", site: "Add-in", cat: "Progress Bar", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""}, 
	{file: "03", type: "jpg", site: "Add-in", cat: "Progress Bar", sub: "Formulas", report: "Customer Aging Summary", ribbon: "", config: "Yes"}, 
	{file: "20", type: "png", site: "Add-in", cat: "Report Library", sub: "Client Activity Dashboard", report: "Customer Aging Summary", ribbon: "", config: "Yes"}, 
	{file: "21", type: "jpg", site: "Add-in", cat: "Report", sub: "", report: "Activity Dashboard", ribbon: "", config: ""}, 
	{file: "22", type: "jpg", site: "Add-in", cat: "Report", sub: "", report: "Error Log", ribbon: "", config: ""}
	]
description: Report errors can happen for a number of reasons. There are two types of errors that Interject can display, handled and unhandled. Errors can be investigated using the Progress Bar Window or Activity Logs.
---
* * *

## Overview

Report errors can happen for a number of reasons. There are two types of errors that Interject can display: handled and unhandled. Handled errors are errors that the developers have foreseen may occur and have written code to handle. The handling usually involves displaying detailed information. Unhandled errors are errors not specifically coded for and left for the system to handle. For example, on a pull or save, an error may occur on the server which the report is trying to access. This error could be handled by the developer, but it could also be an unhandled error. Developers can handle errors by using the keyword "UserNotice" in SQL (see [here](/wDeveloper/L-Dev-Error-Handling.html) for more info). When the error is handled by the developer, a popup message will display a friendly error text set by the developer.

Errors can be investigated using the Progress Bar Window or Activity Logs.

### Using the Progress Bar Window

The Interject Progress Bar Window appears when processing data. When an error occurs, it will display information related to the error. An example of a common error is the misspelling of a data portal, which displays a handled error message when pulling a report with a misspelled data portal.

![](/images/InvestigatingReportErrors/01.jpg)
<br>

If an unhandled error occurs, Interject will still report the error, but no popup message will be displayed to the user. Instead, the Progress Bar Window will stay open, showing a red X next to the failed data portal call.

![](/images/InvestigatingReportErrors/02.jpg)
<br>

When that happens, users can double click the failed data portal to see the exact error the server returned.

![](/images/InvestigatingReportErrors/03.jpg)
<br>

### Using Activity Logs

The Client Activity Dashboard is an Excel file setup to generate information regarding activity, Data Portal usage, user details, version reports, and error logs. It is a useful tool in diagnosing errors.

**Step 1:** Open the Client Activity Dashboard from the Interject Report Library.

![](/images/InvestigatingReportErrors/20.png)
<br>

**Step 2:** Navigate to the Error Log tab and pull the report (the report will populate with information about the most recent user activity logs that contain errors).

![](/images/InvestigatingReportErrors/21.jpg)
<br>

**Step 3:** You can use the various filters and parameters on the report to refine the result set. This will help locate information for troubleshooting specific errors.

![](/images/InvestigatingReportErrors/22.jpg)
<br>
