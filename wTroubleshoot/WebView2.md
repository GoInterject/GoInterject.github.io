---
title: WebView2 Installation
filename: "WebView2.md"
layout: custom
keywords: [login]
headings: ["Overview", "Verifying Installation", "Via Windows Settings", "Via Control Panel", "Installation", "Repair"]
links: ["https://learn.microsoft.com/en-us/microsoft-edge/webview2/", "https://developer.microsoft.com/en-us/microsoft-edge/webview2/", "https://learn.microsoft.com/en-us/microsoft-edge/webview2/concepts/distribution"]
image_dir: "WebView2"
images: [{file: "StartSettings", type: "png", site: "Windows", cat: "Start Menu", sub: "", report: "", ribbon: "", config: ""}, {file: "AddOrRemovePrograms", type: "png", site: "Windows", cat: "Settings", sub: "", report: "", ribbon: "", config: ""}, {file: "WebView2Installed", type: "png", site: "Windows", cat: "Apps & features", sub: "", report: "", ribbon: "", config: ""}, {file: "StartControlPanel", type: "png", site: "Windows", cat: "Start Menu", sub: "", report: "", ribbon: "", config: ""}, {file: "ProgramsAndFeatures", type: "png", site: "Windows", cat: "Control Panel", sub: "", report: "", ribbon: "", config: ""}, {file: "WebView2InstalledControlPanel", type: "png", site: "Windows", cat: "Programs and Features", sub: "", report: "", ribbon: "", config: ""}, {file: "ModifyWebView2", type: "png", site: "Windows", cat: "Apps & features", sub: "", report: "", ribbon: "", config: ""}, {file: "RepairWebView2", type: "png", site: "Windows", cat: "Repair", sub: "", report: "", ribbon: "", config: ""}]
description: Interject uses WebView2 for its login screen. If WebView2 is not installed, nothing will appear when you click the login button. Most systems have WebView2 already installed. If, however, it is not, you can install WebView2 manually.
---
* * *

## Overview

Interject uses [WebView2](https://learn.microsoft.com/en-us/microsoft-edge/webview2/){:target="_blank"}{:rel="noopener noreferrer"} for its login screen. If WebView2 is not installed, nothing will appear when you click the login button. Most systems have WebView2 already installed. If, however, it is not, you can install WebView2 manually.

### Verifying Installation

You can verify that WebView2 is installed by opening up the windows settings and viewing the installed programs.

#### Via Windows Settings

Press the ⊞ Win + I to bring up the Windows settings. Alternatively you can click the Start button and type "Settings".

![](/images/WebView2/StartSettings.png)
<br>

On the Windows Settings form, type "add" and the **Add or remove programs** should appear.

![](/images/WebView2/AddOrRemovePrograms.png)
<br>

In the "App & features", type "webview2" to verify if WebView2 is installed.

![](/images/WebView2/WebView2Installed.png)
<br>

#### Via Control Panel

Click the Start button and type "Control Panel".

![](/images/WebView2/StartControlPanel.png)
<br>

Next click **Program and Features**.

![](/images/WebView2/ProgramsAndFeatures.png)
<br>

In the search field, enter "WebView2" to see if it is installed.

![](/images/WebView2/WebView2InstalledControlPanel.png)
<br>

### Installation

To install the WebView2 Runtime manually, you can download it [here](https://developer.microsoft.com/en-us/microsoft-edge/webview2/){:target="_blank"}{:rel="noopener noreferrer"}. Select the desired distribution mode and download and install it. The Evergreen distribution mode is recommended. To learn more about the different modes, see [WebView2 Runtime](https://learn.microsoft.com/en-us/microsoft-edge/webview2/concepts/distribution){:target="_blank"}{:rel="noopener noreferrer"}.

### Repair

If after installing WebView2 you still do not see the Interject login screen, you might need to repair WebView2. Find WebView2 in the list of installed programs as explained [previously](#verifying-installation). Then click **Modify**.

![](/images/WebView2/ModifyWebView2.png)
<br>

Next click **Repair**.

![](/images/WebView2/RepairWebView2.png)
<br>
