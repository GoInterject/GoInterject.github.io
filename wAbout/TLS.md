---
title: Interject TLS for HTTPS
filename: "TLS.md"
layout: custom
keywords: [Security, Privacy, Data Governance, Transport, Config, IDSSettings, Install Code]
headings: ["Overview", "TLS 1.0/1.1 End of Support", "Enabling TLS 1.2 for Earlier Interject Version", "Set TLS 1.2 Setting via Install Code", "Set TLS Settings via IDSSettings File"]
links: ["https://learn.microsoft.com/en-us/lifecycle/announcements/tls-support-ending-10-31-2024", "https://portal.gointerject.com/download-interject.html", "#enabling-tls-12-for-earlier-interject-version", "#set-tls-12-setting-via-install-code"]
image_dir: "TLS"
images: []
description: Interject uses the Transport Layer Security (TLS). TLS is a cryptographic protocol designed to provide secure communication over a computer network. It ensures data privacy and integrity between two communicating applications by encrypting the information exchanged. 
---
* * *

## Overview

Interject uses the Transport Layer Security (TLS). TLS is a cryptographic protocol designed to provide secure communication over a computer network. It ensures data privacy and integrity between two communicating applications by encrypting the information exchanged.

### TLS 1.0/1.1 End of Support

For Interject version 2.3.34 and earlier, the default is TLS 1.1. Support for TLS 1.0 and TLS 1.1 will end by October 31, 2024. For more info, see [here](https://learn.microsoft.com/en-us/lifecycle/announcements/tls-support-ending-10-31-2024){:target="_blank"}{:rel="noopener noreferrer"}. Your options are:

 - [Upgrade Interject](https://portal.gointerject.com/download-interject.html)
 - Update to TLS 1.2 by [enabling TLS 1.2](#enabling-tls-12-for-earlier-interject-version) and [changing the settings](#set-tls-12-setting-via-install-code)

### Enabling TLS 1.2 for Earlier Interject Version

The TLS setting can be changed by first enabling earlier versions to use TLS 1.2. This is a config file located in the Interject installation folder.

**Step 1:** To determine where Interject is installed, open Excel and click on the File tab:

![](/images/TLS/ExcelFileTab.png)
<br>

Click on **Options**:

![](/images/TLS/FileTabOptions.png)
<br>

The installation location is on the **Add-Ins** tab:

![](/images/TLS/InterjectInstallationLocation.png)
<br>

**Step 2:** Open the installation folder for Interject in a file browser and open the **AddinManager.exe.config** with a text editor.

![](/images/TLS/InstallFolder.png)
<br>

**Step 3:** Add the following line and save the file:

```
<!-- Enable TLS 1.2 and above -->
  <runtime>
    <AppContextSwitchOverrides value="Switch.System.Net.DontEnableSystemDefaultTlsVersions=false"/>
  </runtime>
```
<br>

![](/images/TLS/AddinManagerConfig.png)

**Step 4:** Restart the Addin Manager. Right click the Interject Addin Manger icon in the system tray and select **Exit**.

![](/images/TLS/ExitAddinManager.png)
<br>

Restart the Addin Manger.

![](/images/TLS/StartAddinManager.png)
<br>

### Set TLS 1.2 Setting via Install Code

You can set the TLS setting to 1.2 by entering an install code.

Click on the **Advanced Menu** to reveal the **System** menu. On the **System** menu, click **Configure Install**.

![](/images/TLS/ConfigureInstall.png)
<br>

Enter "TLS1.2" and click **Continue**.

![](/images/TLS/TLS12.png)
<br>

Restart Excel to ensure TLS 1.2 setting is active.

### Set TLS Settings via IDSSettings File

You can manual set the TLS setting via the **IDSSetting.xml**.

**Step 1:** Open the Diagnostics, select **Open User Folders** and click **Execute Selected Action**.

![](/images/TLS/OpenUserFolders.png)
<br>

In the Settings folder, open the **IDSSetting.xml** file with a text editor.

![](/images/TLS/SettingsFolder.png)
<br>

You can change the TLS setting in the **TlsOverride** tag.

![](/images/TLS/TLSSetting.png)
<br>

Restart Excel to ensure your settings are active.
