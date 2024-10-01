---
title: Corrupted Interject Installation
filename: "CorruptedInstallation.md"
layout: custom
keywords: [corrupt, installation, uninstall, microsoft troubleshooter, manual, registry]
headings: ["Overview", "Manual Uninstall", "Uninstalling With the Microsoft Troubleshooter"]
links: ["https://support.microsoft.com/en-us/topic/fix-problems-that-block-programs-from-being-installed-or-removed-cca7d1b6-65a9-3d98-426b-e9f927e1eb4d"]
image_dir: "CorruptedInstallation"
images: [
    {file: "TroubleshooterInterject", type: "png", site: "Windows", cat: "Microsoft Troubleshooter", sub: "", report: "", ribbon: "", config: ""},
    {file: "TroubleshooterYesUninstall", type: "png", site: "Windows", cat: "Microsoft Troubleshooter", sub: "", report: "", ribbon: "", config: ""},
    {file: "TroubleshooterFixed", type: "png", site: "Windows", cat: "Microsoft Troubleshooter", sub: "", report: "", ribbon: "", config: ""}
]
description: There are some instances where Interject may be left in an incomplete or corrupted state after installation. This can happen, for example, if the Interject installer was executed from within a zipped folder, without being properly extracted first. In such cases, the installation process may only partially complete, leading to issues such as being unable to uninstall or reinstall Interject properly. When this happens, manual intervention is required to fully remove the corrupted installation.
---
* * *

## Overview

There are some instances where Interject may be left in an incomplete or corrupted state after installation. This can happen, for example, if the Interject installer was executed from within a zipped folder, without being properly extracted first. In such cases, the installation process may only partially complete, leading to issues such as being unable to uninstall or reinstall Interject properly. When this happens, manual intervention is required to fully remove the corrupted installation.

### Manual Uninstall

A manual uninstall of Interject involves deleting various files and making changes to the Windows registry, which can be complicated and prone to errors. To simplify this process, Microsoft provides a [Troubleshooter](https://support.microsoft.com/en-us/topic/fix-problems-that-block-programs-from-being-installed-or-removed-cca7d1b6-65a9-3d98-426b-e9f927e1eb4d){:target="_blank"}{:rel="noopener noreferrer"} tool that can assist in removing problematic installations. This tool automates much of the cleanup process, helping ensure that all Interject-related files and registry entries are completely removed, allowing for a fresh reinstallation.

### Uninstalling With the Microsoft Troubleshooter

After downloading and starting the tool, simply find Interject Excel in the list of programs to uninstall:

![](/images/CorruptedInstallation/TroubleshooterInterject.png)
<br>

Click **Yes, try uninstall**:

![](/images/CorruptedInstallation/TroubleshooterYesUninstall.png)
<br>

After a short time, you should see that Interject was successfully uninstalled:

![](/images/CorruptedInstallation/TroubleshooterFixed.png)
<br>

Now you can reinstall Interject.
