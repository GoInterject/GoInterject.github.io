---
title: AdxLoader Don't Match
filename: "AdxLoader.md"
layout: custom
keywords: [app, addin, missing, reset]
headings: ["Overview", "Cause of Error", "Solution", "Displaying Excel Bit Version", "Helpful Microsoft Office Links"]
links: ["/wAbout/Uninstalling.html", "/wAbout/SingleUser.html", "/wAbout/SharedComputer.html", "https://support.microsoft.com/en-us/office/choose-between-the-64-bit-or-32-bit-version-of-office-2dee7807-8f95-4d0c-b5fe-6c6f49b8d261", "https://www.microsoft.com/en-us/microsoft-365/download-office", "https://learn.microsoft.com/en-us/deployoffice/change-bitness"]
description: Every once in a while, Excel Add-ins may end up missing or fail to load in Excel. If your Interject addin is missing, you can follow these steps to reset it.
---
* * *

## Overview

This issue results in an error message upon opening Excel:

"The file format and extension of 'adxloader.interject.dll' don't match. The file could be corrupted or unsafe. Unless you trust its source, don't open it. Do you want to open it anyway?"

![](/images/AdxLoader/AdxLoaderDontMatch.png)
<br>

<blockquote class=highlight_note>
<b>Note:</b> This file is a binary file so clicking to open this file will display unreadable characters. Simply click "No" and then perform the following steps to fix.
</blockquote>

### Cause of Error

The most likely cause of this error is that the bit version of Excel is out of sync with the Interject Addin bit version. This will happen if the architecture type of Microsoft Excel/Office is changed (e.g. 32 and 64 bit).

### Solution

If your architecture bit version of Excel/Office changes, you will need to uninstall Interject and reinstall. This should sync up the bit versions. For more information, see the following pages:

* **[Uninstalling](/wAbout/Uninstalling.html)**
* **[Installing Single User](/wAbout/SingleUser.html)**
* **[Installing Shared Computer](/wAbout/SharedComputer.html)**

### Displaying Excel Bit Version

You can verify the bit version of Excel by clicking on **File** on the menu and then **Account**.

![](/images/AdxLoader/ClickAccount.png)
<br>

Click **About Excel**.

![](/images/AdxLoader/ClickAboutExcel.png)
<br>

The bit version is displayed:

![](/images/AdxLoader/ExcelBitVersion.png)
<br>

### Helpful Microsoft Office Links

For information regarding 32-bit versus 64-bit, see [here](https://support.microsoft.com/en-us/office/choose-between-the-64-bit-or-32-bit-version-of-office-2dee7807-8f95-4d0c-b5fe-6c6f49b8d261){:target="_blank"}{:rel="noopener noreferrer"}.

For downloading Microsoft Office, see [here](https://www.microsoft.com/en-us/microsoft-365/download-office){:target="_blank"}{:rel="noopener noreferrer"}.

For information on changing the architecture type, see [here](https://learn.microsoft.com/en-us/deployoffice/change-bitness){:target="_blank"}{:rel="noopener noreferrer"}.
