---
title: Interject TLS for HTTPS
filename: "TLS.md"
layout: custom
keywords: [Security, Privacy, Data Governance, Transport, Config, IDSSettings, Install Code]
headings: ["Enabling TLS 1.2 for Earlier Interject Version", "Set TLS 1.2 Setting via Install Code", "Set TLS Settings via IDSSettings File"]
links: []
image_dir: "TLS"
images: []
description: Interject uses the Transport Layer Security (TLS). TLS is a cryptographic protocol designed to provide secure communication over a computer network. It ensures data privacy and integrity between two communicating applications by encrypting the information exchanged. 
---
* * *

## Overview

Interject uses the Transport Layer Security (TLS). TLS is a cryptographic protocol designed to provide secure communication over a computer network. It ensures data privacy and integrity between two communicating applications by encrypting the information exchanged. 

### Enabling TLS 1.2 for Earlier Interject Version

For Interject version 2.3.34 and earlier, the default is TLS 1.1. The TLS setting can be changed by first enabling earlier versions to use TLS 1.2.

**Step 1:** Open the installation folder for Interject and open the **AddinManager.exe.config** with a text editor.

![](/images/TLS/InstallFolder.png)
<br>

**Step 2:** Add the following line and save the file:

```
<!-- Enable TLS 1.2 and above -->
  <runtime>
    <AppContextSwitchOverrides value="Switch.System.Net.DontEnableSystemDefaultTlsVersions=false"/>
  </runtime>
```

![](/images/TLS/AddinManagerConfig.png)

**Step 3:** Restart the Addin Manager. Right click the Interject Addin Manger icon in the system tray and select **Exit**.

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

You can manual set the TLS setting via the IDSSetting.xml.

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

