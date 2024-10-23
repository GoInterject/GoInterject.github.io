---
title: Report Library Basics
filename: "Report-Library-Basics.md"
layout: custom
keywords: [report library, folder, link, version, resize, file, status, navigate, search]
headings: ["Overview", "Opening The Report Library", "Resizing the Report Library", "The Report Library", "Folders Section", "Report Link Section", "Link Version Section", "Status", "Opening a Report", "Navigating the Report Library", "Using the Search Feature", "Using the keyboard", "Using the mouse", "Using the Diagnostics Form", "Related Links"]
links: ["/wAbout/Resizing-Form-Windows.html", "/wGetStarted/L-Create-UpdatingReportLibrary", "/wAbout/Logging-In.html", "/wAbout/Updating-Interject.html", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html", "/wAbout/Real-World-Walkthroughs.html", "/wAbout/Inventory-Reports.html"]
image_dir: "ReportLibraryBasics"
images: [
	{file: "Ribbon", type: "png", site: "Add-in", cat: "Ribbon", sub: "Report Library", report: "", ribbon: "Simple", config: ""}, 
    {file: "ReportLibrary", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "Interject Inventory Demo", ribbon: "", config: ""}, 
    {file: "Resize", type: "png", site: "Add-in", cat: "Report Library", sub: "Resize", report: "", ribbon: "", config: ""}, 
    {file: "ReportLibraryFoldersSection", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "Interject Inventory Demo", ribbon: "", config: ""}, 
    {file: "ReportLibraryLinksSection", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "Interject Inventory Demo", ribbon: "", config: ""}, 
    {file: "ReportLibraryVersionSection", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "Interject Inventory Demo", ribbon: "", config: ""}, 
    {file: "LinkVersionSection", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "", ribbon: "", config: ""}, 
    {file: "Statuses", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "", ribbon: "", config: ""}, 
    {file: "OpenReport", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "Interject Inventory Demo", ribbon: "", config: ""}, 
    {file: "ReportOpened", type: "png", site: "Add-in", cat: "Report", sub: "", report: "Quick Customer Search", ribbon: "Advanced", config: ""}, 
    {file: "ReportLibrarySearch", type: "png", site: "Add-in", cat: "Report Library", sub: "", report: "", ribbon: "", config: ""}, 
    {file: "SearchReportLinksWindowReports", type: "png", site: "Add-in", cat: "Report Library", sub: "Search", report: "", ribbon: "", config: ""}, 
    {file: "SearchReportLinksWindowSearch", type: "png", site: "Add-in", cat: "Report Library", sub: "Search", report: "", ribbon: "", config: ""}, 
    {file: "SearchReportLinksWindowGoto", type: "png", site: "Add-in", cat: "Report Library", sub: "Search", report: "", ribbon: "", config: ""}, 
    {file: "SearchReportLinksWindowDownload", type: "png", site: "Add-in", cat: "Report Library", sub: "Search", report: "", ribbon: "", config: ""}
]
description: The Report Library is a way for your team to share reports from a central location going beyond just a Sharepoint or a Shared Network Folder.The reports are uploaded to the library and can be accessed from any computer using Excel via Interject.
---
* * *

## Overview

The Report Library is a way for your team to share reports from a central location going beyond just a Sharepoint or a Shared Network Folder. The reports are uploaded to the library and can be accessed from any computer using Excel via Interject. The reports can also be versioned, so reverting to a previous report is simple.

### Opening The Report Library

Once Interject is installed, an Interject Ribbon will be added to Excel.

**Step 1:** To start, click the Interject Ribbon menu and open the Report Library. Click the icon or use the keystroke Ctrl+Shift+L on the keyboard.

![](/images/ReportLibraryBasics/Ribbon.png)
<br>

**Step 2:** The Report Library consists of folders and sub-folders, just like a typical folder hierarchy (max three levels deep for simplicity).

![](/images/ReportLibraryBasics/ReportLibrary.png)
<br>

### Resizing the Report Library

By clicking on the Resize button in the top right corner, you can resize the Report Library. Available preset sizes are Small, Medium, and Large or you may scale it to a custom value. For more info about resizing forms, see [Resizing Interject Windows](/wAbout/Resizing-Form-Windows.html).

![](/images/ReportLibraryBasics/Resize.png)
<br>

### The Report Library

Each section of the Report Library is detailed below. Before opening a report from the library, look through the Folders and Report Links, and check the Link Version of the desired report. There are 3 main sections of the Report Library: Folders Section, Report Link Section, and the Link Version Section.

### Folders Section

The Folders section of the Report Library contains a hierarchy of folders (max three folders deep for simplicity). You can expand or collapse any folder.

![](/images/ReportLibraryBasics/ReportLibraryFoldersSection.png)
<br>

### Report Link Section

The reports of the selected folder will be displayed here in the Report Link section.

![](/images/ReportLibraryBasics/ReportLibraryLinksSection.png)
<br>

### Link Version Section

This section contains details of the selected report.

![](/images/ReportLibraryBasics/ReportLibraryVersionSection.png)
<br>

There are 4 areas within this section:

1. View Details (Brings up the Link Details window where you can view additional information about this report)
2. View Documentation (Opens the documentation for this report. If grayed out then documentation has not been set up)
3. Link Name & Description
4. Versions (Displays the Version note and lists all the versions)

![](/images/ReportLibraryBasics/LinkVersionSection.png)
<br>

### Status

There are 4 statuses of a link version, each with their own distinctive color:

* _Green_ : Currently Live
* _Gray_ : Superseded, this is an older version of a previous live report
* _Yellow_ : In Testing
* _Red_ : In Development

![](/images/ReportLibraryBasics/Statuses.png)
<br>

## Opening a Report

To open a report:

1. Select the folder
2. Select the report
3. Select the version
4. Click **Open Link**

![](/images/ReportLibraryBasics/OpenReport.png)
<br>

The report link is opened:

![](/images/ReportLibraryBasics/ReportOpened.png)
<br>

## Navigating the Report Library

Navigating the Report Library efficiently is important when there are numerous reports. Interject makes this easy by providing 3 ways to navigate the Library and find the report you are looking for.

### Using the Search Feature

You can search the Report Library for reports by clicking on the **Search** button:

![](/images/ReportLibraryBasics/ReportLibrarySearch.png)
<br>

The Search Report Links window shows all the reports in order:

![](/images/ReportLibraryBasics/SearchReportLinksWindowReports.png)
<br>

As you begin typing in the search field, the most relevant hits will appear on top:

![](/images/ReportLibraryBasics/SearchReportLinksWindowSearch.png)
<br>

Clicking on **Goto** will highlight that report in the Report Library:

![](/images/ReportLibraryBasics/SearchReportLinksWindowGoto.png)
<br>

You may also download a .CSV file, which lists the ID, Report Path, Report Name, and Description of all reports:

![](/images/ReportLibraryBasics/SearchReportLinksWindowDownload.png)
<br>

### Using the keyboard

**Step 1:** Use the up and down arrow keys to navigate the folders. Use the right and left keys to move in and out of sub-folders.

**Step 2:** To go into the Report Link section hit Tab.

**Step 3:** To get back to the Folder section hit Shift Tab.

**Step 4:** Hitting enter on a report link will open the report and close the Report Library.

### Using the mouse

**Step 1:** Click on a folder to see the Report Link(s) in the folder

**Step 2:** Double-click on a folder to open a sub-folder

**Step 3:** Double-clicking on a link opens the report and keeps the Report Library open, while single-clicking the **Open Link** button will open the selected report and close Report Library

For how to add or change files in the Report Library, please check out [Lab Create: Updating the Report Library](/wGetStarted/L-Create-UpdatingReportLibrary) .

## Related Links

[Logging In](/wAbout/Logging-In.html)

[Updating Interject](/wAbout/Updating-Interject.html)

[Interject Ribbon Menu Items](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html)

[Real-World Walkthroughs](/wAbout/Real-World-Walkthroughs.html)

[Inventory Reports](/wAbout/Inventory-Reports.html)

