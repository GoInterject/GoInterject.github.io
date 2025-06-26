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

### Steps to Resolve

1. Locate Interject Registry Keys

Run the provided script to list all Interject-related registry entries:

```powershell
.\regkey_find.ps1
```

<blockquote class=highlight_note>
<b>Note:</b> You may need to run PowerShell as Administrator.
</blockquote>
<br>

The script searches under the following hives:

- HKCU:\Software
- HKLM:\Software
- HKLM:\Software\WOW6432Node

It will return all keys and subkeys that include "interject" in their path or name.

2. Review Script Output

Example output:

```bash
HKCU:\Software\Interject
HKLM:\Software\Classes\Installer\Products\{GUID}
HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Interject
```

These entries indicate locations that may contain leftover Interject references.

3. Manually Remove Registry Keys

Open Registry Editor (regedit) and navigate to the paths returned by the script. Carefully remove any entries related to Interject.

<blockquote class=highlight_note>
<b>Note:</b> Editing the registry can affect your system. Only remove keys that are clearly related to Interject. If unsure, contact support. 
</blockquote>
<br>

4. Reinstall Interject

After cleaning the registry, proceed to install the latest version of Interject from the official source.

### Additional Notes

This issue has primarily occurred when older versions of the Interject add-in were not completely uninstalled.

In most cases, this process has resolved install errors and allowed the new version to work without issue.

If the problem persists after removing registry keys, please contact us at [info@gointerject.com](mailto:info@gointerject.com) for further assistance.
