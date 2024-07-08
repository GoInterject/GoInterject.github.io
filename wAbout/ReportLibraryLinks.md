---
title: Report Library Links
filename: "ReportLibraryLinks.md"
layout: custom
keywords: [report library, link, file, version, report, update, upload, details, documentation]
headings: ["Overview", "Creating a New Link (File Open)", "Creating a New Link (File Not Open)", "Creating a New Version to an Existing Link", "Updating a Report Link", "The Report Link Details Form", "Types of Links", "Link Documentation"]
links: ["/wAbout/Report-Library-Basics.html#status", "/wAbout/Report-Library-Basics.html#link-version-section", "/wAbout/ReportLibrarySorting.html", "/wAbout/Report-Library-Basics.html#status", "/wGetStarted/L-Drill-DrillCodes.html", "https://docs.gointerject.com/wTroubleshoot/Cloud-File.html"]
image_dir: "ReportLibraryLinks"
images: [
	{file: "OpenReportLibrary", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "", ribbon: "Simple", config: ""}, 
	{file: "RightClick", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "CreateNewLink", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "CreateNewLinkSave", type: "png", site: "Add-in", cat: "Report Library", sub: "Details", report: "Customer Aging", ribbon: "", config: ""}, 
	{file: "NewLinkCreated", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "Customer Aging", ribbon: "", config: ""}, 
	{file: "SaveFileExplorer", type: "png", site: "Windows", cat: "Explorer", sub: "Explorer", report: "", ribbon: "", config: ""}, 
	{file: "CreateNewLinkFileClosed", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "Customer Aging", ribbon: "", config: ""}, 
	{file: "CreateNewLinkFileClosedSave", type: "png", site: "Add-in", cat: "Report Library", sub: "Details", report: "Customer Aging", ribbon: "", config: ""}, 
	{file: "LinkPathBrowseClick", type: "png", site: "Add-in", cat: "Report Library", sub: "Details", report: "", ribbon: "", config: ""}, 
	{file: "LinkPathBrowseExplorer", type: "png", site: "Windows", cat: "Explorer", sub: "Explorer", report: "", ribbon: "", config: ""}, 
	{file: "ClickSave", type: "png", site: "Add-in", cat: "Report Library", sub: "Details", report: "", ribbon: "", config: ""}, 
	{file: "Versions", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "OpenReportLibraryUpdateLink", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "Customer Aging", ribbon: "Simple", config: ""}, 
	{file: "CreateNewVersionClick", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "Customer Aging", ribbon: "", config: ""}, 
	{file: "VersionInfo", type: "png", site: "Add-in", cat: "Report Library", sub: "Details", report: "", ribbon: "", config: ""}, 
	{file: "ClickSave", type: "png", site: "Add-in", cat: "Report Library", sub: "Details", report: "", ribbon: "", config: ""}, 
	{file: "Overwriting", type: "png", site: "Add-in", cat: "Popup", sub: "Overwriting", report: "", ribbon: "", config: ""}, 
	{file: "LinkVersionWindow", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "Customer Aging", ribbon: "", config: ""}, 
	{file: "SelectedLinkMenu", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "Customer Aging", ribbon: "", config: ""}, 
	{file: "EditVersionClick", type: "png", site: "Add-in", cat: "Report Library", sub: "Right Click Menu", report: "Customer Aging", ribbon: "", config: ""}, 
	{file: "EditVersionDetails", type: "png", site: "Add-in", cat: "Report Library", sub: "Details", report: "Customer Aging", ribbon: "", config: ""}, 
	{file: "EditVersionCompleted", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "Customer Aging", ribbon: "", config: ""}, 
	{file: "ReportLinkDetails", type: "png", site: "Add-in", cat: "Report Library", sub: "Details", report: "Customer Aging", ribbon: "", config: ""}, 
	{file: "ReportLinkTypes", type: "png", site: "Add-in", cat: "Report Library", sub: "Details", report: "", ribbon: "", config: ""}, 
	{file: "DocumentationTypes", type: "png", site: "Add-in", cat: "Report Library", sub: "Details", report: "", ribbon: "", config: ""}
	]
description: The Report Library provides an easy interface where new reports can be uploaded, existing reports can be updated, and details and documentation about the report can be added.
---
* * *

## Overview

### Creating a New Link (File Open)

**Step 1:** To create a new link, begin by opening the Excel file you wish to upload and open the Report Library.

![](/images/ReportLibraryLinks/OpenReportLibrary.png)
<br>

**Step 2:** Select the folder you wish to upload the file to and right click in the Report Links section.

![](/images/ReportLibraryLinks/RightClick.png)
<br>

**Step 3:** Hover the cursor over **Save Current Workbook** and select **Create New Link**.

![](/images/ReportLibraryLinks/CreateNewLink.png)
<br>

**Step 4:** The [Report Link Details Form](#report-link-details-form) appears where you can enter details about the report:

1. Enter a name for the report
2. Enter an optional description
3. Set the status of the report to live (see [here](/wAbout/Report-Library-Basics.html#status) for more info on statuses)
4. Click save to save the report

![](/images/ReportLibraryLinks/CreateNewLinkSave.png)
<br>

The new report now appears in the Library:

![](/images/ReportLibraryLinks/NewLinkCreated.png)
<br>

<blockquote class=highlight_note>
<b>Note:</b> If the file is not saved locally you will be prompted to save the file first before you can upload the file to the Report Library.
</blockquote>
<br>

![](/images/ReportLibraryLinks/SaveFileExplorer.png)
<br>

### Creating a New Link (File Not Open)

**Step 1:** To save a file that is not currently open, begin by right clicking on the Report Links Section and select **Create New Link**:

![](/images/ReportLibraryLinks/CreateNewLinkFileClosed.png)
<br>

**Step 2:** The Link Details Window appears where you can enter details about the report:

1. Enter a name for the report
2. Enter an optional description
3. Set the status of the report to live

![](/images/ReportLibraryLinks/CreateNewLinkFileClosedSave.png)
<br>

**Step 3:** For the Link Path, click **Browse**:

![](/images/ReportLibraryLinks/LinkPathBrowseClick.png)
<br>

Browse to the file you wish to upload and click **Open**:

![](/images/ReportLibraryLinks/LinkPathBrowseExplorer.png)
<br>

**Step 4:** Finally click **Save**:

![](/images/ReportLibraryLinks/ClickSave.png)
<br>

### Creating a New Version to an Existing Link

The Report Library provides an interface where reports can be versioned. Each successive upload will automatically increment the version number:

![](/images/ReportLibraryLinks/Versions.png)
<br>

**Step 1:** To upload a new version to an existing link, begin by opening the Excel file you wish to upload and open the Report Library.

![](/images/ReportLibraryLinks/OpenReportLibraryUpdateLink.png)
<br>

**Step 2:** Next, right click on the name of the link you want to update, hover the cursor over **Save Current Workbook** and select **Create New Link**.

![](/images/ReportLibraryLinks/CreateNewVersionClick.png)
<br>

**Step 3:** You may optionally choose to enter a name for this version and add notes detailing the changes:

![](/images/ReportLibraryLinks/VersionInfo.png)
<br>

**Step 4:** Finally click **Save**.

![](/images/ReportLibraryLinks/ClickSave.png)
<br>

You will be prompted to set the previous version to "Superseded". Click **Yes**:

![](/images/ReportLibraryLinks/Overwriting.png)
<br>

Notice the new report is added and automatically incremented the version number:

![](/images/ReportLibraryLinks/LinkVersionWindow.png)
<br>

### Updating a Report Link

You can update a report link details via the right-click menu in the Report Library.

<blockquote class=highlight_note>
<b>Note:</b> Report links in the "MyFavorites" folder are not editable.
</blockquote>
<br>

**Step 1:** Begin by opening the Report Library and right click on the report you wish to edit. Hover the cursor over **Selected Link** and you can view the sub menu:

![](/images/ReportLibraryLinks/SelectedLinkMenu.png)
<br>

**Step 2:** Click the **Edit** option:

![](/images/ReportLibraryLinks/EditVersionClick.png)
<br>

**Step 3:** The Link Details Window appears where you can change the details. Update the description and click **Save**:

![](/images/ReportLibraryLinks/EditVersionDetails.png)
<br>

Notice the details of the version have been updated:

![](/images/ReportLibraryLinks/EditVersionCompleted.png)
<br>

### The Report Link Details Form

The Report Link Details form displays information about the selected report. This form is specific to the selected report link [version](/wAbout/Report-Library-Basics.html#link-version-section).

![](/images/ReportLibraryLinks/ReportLinkDetails.png)
<br>

* **Link Name:** The name of the report link
* **Sort:** The sorting order of the report link (see [here](/wAbout/ReportLibrarySorting.html) for more info)
* **Link Description:** A description for the report
* **Link Folder:** The folder in which the report resides
* **Status:** The current status of the report (see [here](/wAbout/Report-Library-Basics.html#status) for more info)
* **Version Name:** The name of the version for this report
* **Version Note:** A note explaining the version of this report
* **Link Type:** The type of this link (see [here](#types-of-links) for more info)
* **Link Path:** The path to the source for this report link
* **Documentation Type:** The type of documentation for this report link (see [here](#link-documentation) for more info)
* **Documentation Path:** The path to the source for this report's documentation
* **Drill Codes:** Drill codes enable drilling to this report link (see [here](/wGetStarted/L-Drill-DrillCodes.html) for more info)

### Types of Links

The reports in the Report Library are called links because the link to a source. As such there are different types of links for a report:

![](/images/ReportLibraryLinks/ReportLinkTypes.png)
<br>

* **Local/Network File:** The report source is a file that resides on the user's local or network system
* **Folder Link:** A link to a local or network folder (e.g. D:\Users\test\Documents)
* **Website Link:** The report source is a website link (i.e. http or https address)
* **Report Library File:** The report source is a file that resides inside the Report Library itself

<br>

<blockquote class=highlight_note>
<b>Note:</b> Files that reside in the cloud (e.g. OneDrive, SharePoint, etc.) cannot be saved as a local file or a Report Library file (see <a href="https://docs.gointerject.com/wTroubleshoot/Cloud-File.html">here</a> for more info).
</blockquote>

### Link Documentation

You have the option to include documentation for the selected report link. This could be a local file, a link to a specific folder, or a website link:

![](/images/ReportLibraryLinks/DocumentationTypes.png)
<br>
