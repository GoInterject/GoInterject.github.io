---
title: Interject Settings and Cache
filename: "SettingsCache.md"
layout: custom
keywords: [Diagnostics, Tools, Settings, Configurations, Config]
headings: ["Overview", "Opening the Folders", "Resetting Settings and Cache"]
links: ["/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#advanced-menu-items"]
image_dir: "SettingsCache"
images: [
    {file: "DiagnosticsRibbon", type: "png", site: "Addin", cat: "Ribbon", sub: "", report: "", ribbon: "Advanced", config: ""}, 
    {file: "Diagnostics", type: "png", site: "Addin", cat: "Diagnostics", sub: "Open User Folders", report: "", ribbon: "", config: ""}, 
    {file: "ResetFileCache", type: "png", site: "Addin", cat: "Diagnostics", sub: "Reset File Cache", report: "", ribbon: "", config: ""}, 
    {file: "ResetSettingsCache", type: "png", site: "Addin", cat: "Diagnostics", sub: "Reset Settings Cache", report: "", ribbon: "", config: ""}
    ]
description: Interject keeps multiple folders on your local drive for settings and a file cache. These folders help facilitate logging in, better performance, and functionality.
---
* * * 

## Overview

Interject keeps multiple folders on your local drive for settings and a file cache. These folders help facilitate logging in, better performance, and functionality.

**File Cache** (stores cached reports for easy retrieval via the Report Library):

- AppData/Local/Interject/FileCache

**Settings** (stores cached settings, settings/configurations file, error logs, activity logging information, and login tokens):

- AppData/Local/Interject/Settings
- AppData/Roaming/Interject/Settings

<br>

<blockquote class=highlight_note>
<b>Note:</b> Starting with Interject version 2.5.1.1, Interject stores the settings in the roaming profile so that settings can be synced across systems. The local folder still exists, however, for archival purposes.
</blockquote>

### Opening the Folders

You can open these folders easily by clicking on **Diagnostics** on the [Advanced Interject ribbon](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#advanced-menu-items), select **Open User Folders** and then click **Execute Selected Action**.

![](/images/SettingsCache/DiagnosticsRibbon.png)
<br>

![](/images/SettingsCache/Diagnostics.png)
<br>

### Resetting Settings and Cache

The Diagnostics window has a number of options to reset the local settings and file caches.

The "Reset File Cache" options will remove all locally cached files:

![](/images/SettingsCache/ResetFileCache.png)
<br>

The "Reset Settings Cache" option in the Public section that will reset the settings cache files:

![](/images/SettingsCache/ResetSettingsCache.png)
<br>
