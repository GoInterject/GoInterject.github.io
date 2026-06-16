---
title: Interject TLS for HTTPS
filename: "TLS.md"
layout: custom
keywords: [Security, Privacy, Data Governance, Transport, Config, IDSSettings, Install Code]
headings: ["Overview", "TLS 1.0/1.1 End of Support", "Default TLS for Interject", "Set TLS Settings via IDSSettings File", "Enabling System Default TLS Settings for the Addin Manager"]
links: ["https://learn.microsoft.com/en-us/lifecycle/announcements/tls-support-ending-10-31-2024", "https://portal.gointerject.com/download-interject.html", "#set-tls-settings-via-idssettings-file"]
image_dir: "TLS"
images: [
	{file: "OpenUserFolders", type: "png", site: "Add-in", cat: "Diagnostics", sub: "Open User Folders", report: "", ribbon: "", config: ""},
	{file: "SettingsFolder", type: "png", site: "Windows", cat: "Explorer", sub: "", report: "", ribbon: "", config: ""},
	{file: "TLSSetting", type: "png", site: "Windows", cat: "Notepad", sub: "", report: "", ribbon: "", config: ""},
	{file: "ExcelFileTab", type: "png", site: "Excel", cat: "", sub: "", report: "", ribbon: "", config: ""},
	{file: "FileTabOptions", type: "png", site: "Excel", cat: "", sub: "", report: "", ribbon: "", config: ""},
	{file: "InterjectInstallationLocation", type: "png", site: "Excel", cat: "Options", sub: "", report: "", ribbon: "", config: ""},
	{file: "InstallFolder", type: "png", site: "Windows", cat: "Explorer", sub: "", report: "", ribbon: "", config: ""},
	{file: "AddinManagerConfig", type: "png", site: "Windows", cat: "Notepad", sub: "", report: "", ribbon: "", config: ""},
	{file: "ExitAddinManager", type: "png", site: "Add-in", cat: "Add-in Manager", sub: "", report: "", ribbon: "", config: ""},
	{file: "StartAddinManager", type: "png", site: "Windows", cat: "Start Menu", sub: "", report: "", ribbon: "", config: ""}
]
description: Interject uses the Transport Layer Security (TLS). TLS is a cryptographic protocol designed to provide secure communication over a computer network. It ensures data privacy and integrity between two communicating applications by encrypting the information exchanged. 
---
* * *

## Overview

Interject uses the Transport Layer Security (TLS). TLS is a cryptographic protocol designed to provide secure communication over a computer network. It ensures data privacy and integrity between two communicating applications by encrypting the information exchanged.

<br>

### TLS 1.0/1.1 End of Support

For Interject version 2.3.34 and earlier, the default is TLS 1.1. Eventually TLS 1.0/1.1 will enter into end of life. Your two options before then are:

 1. [Upgrade Interject](https://portal.gointerject.com/download-interject.html)

 2. Update to TLS 1.2 by [changing the settings](#set-tls-settings-via-idssettings-file)

<br>

### Default TLS for Interject

Interject's Addin and Addin Manager have a default TLS setting based on the Interject version:

Interject versions 2.5.2.13 and above:

- Addin - Uses latest TLS available
- Addin Manager - Uses latest TLS available

Interject versions 2.5.0.14 through 2.5.2.11:

- Addin - Uses TLS 1.2 as default
- Addin Manager - Uses TLS 1.1 as default

Interject versions below 2.5.0.14:

- Addin - Uses TLS 1.1 as default
- Addin Manager - Uses TLS 1.1 as default

<br>

### Set TLS Settings via IDSSettings File

You can manually set the TLS setting via the **IDSSettings.xml**.

**Step 1:** Open the Diagnostics, select **Open User Folders** and click **Execute Selected Action**.

![](/images/TLS/OpenUserFolders.png)
<br>

A few folders should open up.

<blockquote class=highlight_note>
<b>Note:</b> Interject version prior to 2.5.1.1 will use the local folder for the settings file. Starting with 2.5.1.1, Interject uses the roaming folder for its settings.
</blockquote>
<br>

**Step 2:** In the Settings folder, open the **IDSSettings.xml** file with a text editor.

![](/images/TLS/SettingsFolder.png)
<br>

You can change the TLS setting in the **TlsOverride** tag. If this tag is missing you can add it anywhere inside the \<Global\> section:

```
<TlsOverride>TLS 1.2</TlsOverride>
```

![](/images/TLS/TLSSetting.png)
<br>

Restart Excel to ensure your settings are active.

<br>

### Enabling System Default TLS Settings for the Addin Manager

In addition to setting the TLS setting for the Addin, you can also optionally set the Addin Manager to use System default TLS settings. This means that the .NET Framework will automatically choose the most secure and highest TLS version supported by both the client (your application) and the server it is communicating with. Typically, this is TLS 1.2 or TLS 1.3 on modern systems.

To ensure your system's default TLS setting is used by the Addin Manager you must edit a config file located in the Interject installation folder.

**Step 1:** To determine where Interject is installed, open Excel and click on the File tab:

![](/images/TLS/ExcelFileTab.png)
<br>

Click on **Options**:

![](/images/TLS/FileTabOptions.png)
<br>

The installation location is on the **Add-Ins** tab:

![](/images/TLS/InterjectInstallationLocation.png)
<br>

**Step 2:** Open the installation folder for Interject in a file browser and open the **InterjectAddinManager.exe.config** with a text editor.

![](/images/TLS/InstallFolder.png)
<br>

**Step 3:** Add the following line after the \<startup> section and before the \<appSettings>:

```
<!-- Enable TLS 1.2 and above -->
  <runtime>
    <AppContextSwitchOverrides value="Switch.System.Net.DontEnableSystemDefaultTlsVersions=false"/>
  </runtime>
```
<br>

![](/images/TLS/AddinManagerConfig.png)

Be sure to save the file.

**Step 4:** Restart the Addin Manager. Right click the Interject Addin Manager icon in the system tray and select **Exit**.

![](/images/TLS/ExitAddinManager.png)
<br>

Restart the Addin Manager.

![](/images/TLS/StartAddinManager.png)
<br>
