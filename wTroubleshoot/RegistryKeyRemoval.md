---
title: Registry Key Removal
filename: "RegistryKeyRemoval.md"
layout: custom
keywords: []
headings: ["Overview", "Steps to Resolve"]
links: ["mailto:info@gointerject.com"]
image_dir: ""
images: []
description: Some users have reported issues when attempting to uninstall the Interject Add-In in order to install the latest version. The uninstaller sometimes fails due to residual registry keys associated with Interject. These leftover keys prevent clean reinstallation of the add-in.
---
* * *

## Overview

Some users have encountered a rare issue when attempting to uninstall the Interject Add-In in order to install the latest version. The issue may be with some residual registry keys associated with Interject. In such a case, doing a complete uninstall by using the installer of the same version as the installed Interject version may solve this issue. If this is not successful, a manual removal of registry keys can be done. To facilitate this last resort option, we have presented a PowerShell script to assist in locating the keys:

[regkey_find.ps1][1]

[1]:{{ site.url }}/download/regkey_find.ps1

**Steps to Resolve:**

1. [Locate Registry Keys](#1-locate-interject-registry-keys) (use script and/or manually inspect registry)
2. [Manually Remove Registry Keys](#2-manually-remove-registry-keys)
3. [Reboot](#3-reboot)
4. [Reinstall Interject](#4-reinstall-interject)

### 1. Locate Interject Registry Keys

#### Running the Script

Run the provided script to list all Interject-related registry entries:

```powershell
.\regkey_find.ps1
```

<blockquote class=highlight_note>
<b>Note:</b> You may need to run PowerShell as Administrator.
</blockquote>
<br>

It will return all keys and subkeys that include "interject" in their path or name.

Example output of registry locations:

* HKCU:\Software\Interject
* HKLM:\Software\Classes\Installer\Products\{GUID}
* HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Interject

These entries indicate locations that may contain leftover Interject references.

#### Additional Registry Locations

A particular support case revealed additional registry locations that may block successful installation of Interject when residual installer files are missing or corrupted. This issue occurred because the system believed Interject was installed, but the cached installer package (.msi) was missing, causing the installation to fail. The error in the log file was:

&emsp; _Warning: Local cached package 'C:\WINDOWS\Installer\ad71cbc.msi' is missing._

The following locations might have additional entries that may need to be manually deleted:

* HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\
(multiple Interject versions may be present here)
* HKEY_USERS\[SID Identifier]\Software\Microsoft\Installer\Products\
* HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Installer\UserData\<UserSID>\Products\

### 2. Manually Remove Registry Keys

Open Registry Editor (regedit) and navigate to the paths returned by the script. Carefully remove any entries related to Interject.

<blockquote class=highlight_note>
<b>Note:</b> Editing the registry can affect your system. Only remove keys that are clearly related to Interject. If unsure, contact support. 
</blockquote>
<br>

### 3. Reboot

After removing the above keys, perform a full system reboot.

### 4. Reinstall Interject

After cleaning the registry, proceed to install the latest version of Interject from the official source.

### Additional Notes

This issue has primarily occurred when older versions of the Interject add-in were not completely uninstalled.

In most cases, this process has resolved install errors and allowed the new version to work without issue.

If the problem persists after removing registry keys, please contact us at [info@gointerject.com](mailto:info@gointerject.com) for further assistance.
