---
title: AdxLoader Don't Match
layout: custom
keywords: [app, addin, missing, reset]
description: Every once in a while, Excel Add-ins may end up missing or fail to load in Excel. If your Interject addin is missing, you can follow these steps to reset it.
---
* * *

## Overview

This issue results in an error message upon opening Excel:

"The file format and extension of 'adxloader.interject.dll' don't match. The file could be corrupted or unsafe. Unless you trust its source, don't open it. Do you want to open it anyway?"

![](/images/AdxLoader/AdxLoaderDontMatch.png)
<br>

<blockquote class=highlight_note>
<b>Note:</b> This file is a binary file so clicking to open this file will display gibberish characters. Simply click "No" and then perform the following steps to fix.
</blockquote>

### Cause of Error

The most likely cause of this error is that the bit version of Excel is out of sync with the Interject Addin bit version. This will happen if Microsoft Excel is updated or switched between 32 and 64 bit installations.

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

### Solution

If your bit version of Excel changes, you will need to uninstall Interject and reinstall. This should sync up the bit versions. For more infoation, see the following pages:

* **[Uninstalling](/wAbout/Uninstalling.html)**
* **[Installing Single User](/wAbout/SingleUser.html)**
* **[Installing Shared Computer](/wAbout/SharedComputer.html)**
