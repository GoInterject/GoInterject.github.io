---
title: Macro Security
filename: "MacroSecurity.md"
layout: custom
keywords: [macro, security, sign key, VBA, checksum]
headings: ["Overview", "Uploading A Macro File", "Opening A Macro File", "Security Settings", "Checking Settings", "File Extensions"]
links: ["/wIndex/MacroSecurity#file-extensions", "/wIndex/MacroSecurity#file-extensions"]
description: Macro security involves mitigating the opening and uploading of Excel files that contain macros to ensure no malicious code affects any system.
---
* * *

## Overview

Macro security involves mitigating the opening and uploading of Excel files that contain macros to ensure no malicious code affects any system. These macro files have the file extension of .xlsm, as opposed to a macro free file extension of .xlsx. These macro files can potentially contain malicious code that when opened via the Report Library, can execute harmful actions. New versions of the Interject Add-In (versions 2.4.x and above) will contain configurations that will mitigate this risk. 

The overall goal of macro security is to ensure a macro file is not opened in the Interject Report Library without it matching the exact file that was uploaded. There are security attack vectors where a previously downloaded file can be replaced or if a file is a direct file path, the file could be later replaced.  If the Interject platform database becomes compromised there are additional attack vectors to be considered.

Since the Report Library trusts all macro files inherently and sidesteps macro warnings, we must be sure the file is valid before opening to ensure Interject protects the user.  With this functionality, Interject can also be a better security vehicle to allow macro files while disabling them in the network.

### Uploading A Macro File

Interject macro security involves enabling/disabling macro file transactions to/from the Report Library. If enabled, when the file is uploaded, a checksum is created on the file. Next, the client's signing key from the Interject Cloud Platform is used on the checksum to create a signed hash. This hash is a unique identifier that is stored in the Interject Cloud Platform for the uploaded file.

![](/images/MacroSecurity/UploadMacroFile.png)
<br>

### Opening A Macro File

When a user attempts to open a file from the Report Library, the file is downloaded to the cache so a signed hash can be created. The two signed hashes are then compared. If they do not match, the file is deleted and the file open is denied. If they do match, the file is opened. This feature prevents unauthorized altercation of uploaded files from being opened. If the hashes do not match then an admin user can download the file for inspection. The file then can be reviewed and re-uploaded to create a new signed hash.

![](/images/MacroSecurity/OpenMacroFile.png)
<br>

### Security Settings

There are key settings that can be used to configure macro security. They can only be set up in the Interject Platform API which are cached locally in an encrypted file. Local settings in the IDSSettings.xml or App.config file are not used since they are not encrypted and could be used to override macro security settings by bad actors. Currently, only Interject can setup and change these settings.
 
The macro security related settings are:

| Setting | Description | Value |
|----|----|----|
| ExcelMacrosEnabled | Enables upload/open of macro files. If this setting is missing AND the MacroFileSigningKey or FileSigningAPI settings have been set, then those can be used to enable a valid upload/open uploading of macro files. | True/False |
| AllowMacroFilesFromDate | Allows users to open files that have been uploaded before this date. This setting makes it possible for users to be able to continue to utilize their existing reports after macro security has been introduced. Typically this setting date is set to the date when macro security is to be implemented. | Date |
| MacroFileSigningKey | A key that is used to digital sign the macro files. | Long string of characters |
| FileSigningAPI | A link to an API that will digital sign the macro files. | URL Link |
| FileSigningAPI_V2 | Currently not used. | URL Link |
| AdditionalFileExtensionsAllowed | Allows a company to upload/open unauthorized file types | List of [File Extensions](/wIndex/MacroSecurity#file-extensions) (e.g.".ppt, .pptx")|
| FileExtensionsNotAllowed | Prohibits a company to upload/open authorized file types | List of [File Extensions](/wIndex/MacroSecurity#file-extensions) (e.g. ".doc, .docx")|

### Checking Settings

The security settings can be set up for each client/company. To confirm the settings, navigate to Interject Diagnostics > Public > Apply Special Features:

![](/images/Testing/DiagnosticsMacroSecuritySettings.png)

### File Extensions

The following displays which file types are allowed to upload/open from the Report Library (if the company has rights):

| File | Ext. | Description |
|----|----|----|
| Excel | xls | Excel file (97-2003) |
| Excel | xlsx | Excel file | 
| Excel | xlsm | Excel file (macro enabled) |
| Excel | xlt | Excel template file (97-2003) |
| Excel | xltx | Excel template file |
| Excel | xltm | Excel template file (macro enabled) |
| Excel | xlsb | Excel binary file |
| Text | txt | Text file |
| Word | doc | Word document (97-2003) |
| Word | docx | Word document |
| Adobe | pdf | Portable Document Format file | 
| Image | png | Portable Network Graphic file |
| Image | jpg | Joint Photographic Experts Group file |
 
