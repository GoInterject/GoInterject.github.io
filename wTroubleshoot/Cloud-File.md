---
title: Cloud File Uploads Incorrectly
filename: "Cloud-File.md"
layout: custom
keywords: [network, cloud, website, url, drive, file, report library, upload, download, open, link]
headings: ["Overview", "Identifying Cloud Files", "Description of the Errors", "Solution: Saving to Local Drive", "Solution: Uploading as a Website Link"]
links: ["/wAbout/Report-Library-Basics.html"]
image_dir: "CloudFile"
images: [{file: "OneDriveLink", type: "png", site: "Addin", cat: "Report Library", sub: "Details", report: "OneDriveReport", ribbon: "", config: ""}, {file: "SharePointLink", type: "png", site: "Addin", cat: "Report Library", sub: "Details", report: "SharepointWebLink", ribbon: "", config: ""}, {file: "ReportLibraryMissingDetails", type: "png", site: "Addin", cat: "Report Library", sub: "", report: "SharepointWebLink", ribbon: "", config: ""}, {file: "UnableToOpen", type: "png", site: "Addin", cat: "Report Library", sub: "Error Popup", report: "", ribbon: "", config: ""}, {file: "ReportLibraryFile", type: "png", site: "Addin", cat: "Report Library", sub: "Details", report: "Financial Report", ribbon: "", config: ""}, {file: "SharePointWebsiteLink", type: "png", site: "Addin", cat: "Report Library", sub: "Details", report: "SharepointWebLink", ribbon: "", config: ""}]
description: Sometimes uploading a report from a cloud drive results in errors. This guide helps you identify cloud files, reveals possible errors that may occur, and a few workarounds.
---
* * *

## Overview

The [Report Library](/wAbout/Report-Library-Basics.html) provides a central hub where you can upload and download reports. Sometimes uploading a report from a cloud drive (e.g. OneDrive, SharePoint) results in errors. This guide helps you identify cloud files, reveals possible errors that may occur, and covers a few workarounds.

### Identifying Cloud Files

You can identify the cloud file when you try to upload it to the Report Library. For example, the link path will be sourced from https://. Compare the following two examples:

**OneDrive link:**

![](/images/CloudFile/OneDriveLink.png)
<br>

**SharePoint link:**

![](/images/CloudFile/SharePointLink.png)
<br>

### Description of the Errors

After uploading a cloud file to the Report Library, it may display missing details such as the Uploaded Date:

![](/images/CloudFile/ReportLibraryMissingDetails.png)
<br>

In addition, attempting to open the link may not do anything or may give the following error:

![](/images/CloudFile/UnableToOpen.png)
<br>

### Solution: Saving to Local Drive

Another work-around is to save the file on a local non-cloud synced folder (e.g. "Downloads"). Then simply upload the file as a Report Library File:

![](/images/CloudFile/ReportLibraryFile.png)
<br>

### Solution: Uploading as a Website Link

One work-around is to upload the cloud file as a Website link. Opening a Website link from the Report Library will simply open the URL in the Link Path. This may open the file, ask for credentials to log in, or simply download the file.

![](/images/CloudFile/SharePointWebsiteLink.png)
<br>
