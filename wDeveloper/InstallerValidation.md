---
title: Checksums for Installers
filename: "InstallerValidation.md"
layout: custom
keywords: [checksum, validation, file integrity, Get-FileHash, hash, algorithm, value]
headings: ["Overview", "Generating a Checksum", "Full Reset"]
links: ["mailto:info@gointerject.com", "https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash?view=powershell-7.3", "https://portal.gointerject.com/download-interject.html", "https://test-portal.gointerject.com/download-interject.html"]
description: The data integrity of Interject installation files can be verified by comparing its checksum. Interject creates csv files containing the official checksum of the installation file. To verify an installer, you can generate a checksum for the file and compared it with the official checksum.
---
* * *

## Overview

The data integrity of Interject installation files can be verified by comparing its checksum. Interject creates csv files containing the official checksum of the installation file. To verify an installer, you can generate a checksum for the file and compare it with the official checksum.

To obtain the official checksum for our installation files, please contact us at [security@gointerject.com](mailto:info@gointerject.com).

### Generating a Checksum

To generate a checksum for a file, open Powershell and run the [Get-FileHash](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash?view=powershell-7.3){:target="_blank"}{:rel="noopener noreferrer"} command:

```powershell
Get-FileHash <FILE> -algorithm "<ALGO>"
```

* FILE = File to generate checksum
* ALGO = Algorithm to use (MD5, SHA1, SHA256, SHA512)

<br>

![](/images/Installer-Validation/Powershell.png)
<br>

### Full Reset

If the checksums do not match or you cannot obtain an official checksum for your installation version, it is recommended to uninstall the current version and obtain a new installer from our [portal site](https://portal.gointerject.com/download-interject.html) or [test portal site](https://test-portal.gointerject.com/download-interject.html). Obtain the official checksum and validate the file's checksum using the method in the previous section before installing.

<br>

<blockquote class=highlight_note>
<b>Note:</b> This checksum verification does not validate if files have been tampered with post-installation. It only verifies if the installer itself has been tampered with. Phishing with fake installers is a bigger concern than a virus that modifies interject files post-installation. Thus this method is just the first step towards security optimization.
</blockquote>
