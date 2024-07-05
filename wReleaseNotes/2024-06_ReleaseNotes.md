---
title: Release Notes
filename: "2024-06_ReleaseNotes.md"
layout: custom
keywords: [change log, updates, versions, history, what's new]
headings: ["June 2024", "Excel Add-in v2.5.1.1", "Portal Site", "Documentation Updates"]
links: ["/wAbout/SingleUser.html", "/wAbout/SharedComputer.html", "/wPortal/Roles.html", "/wPortal/FolderPermissions.html"]
image_dir: ""
images: []
description: Release notes for this month's updates
---
* * *

## June 2024

### Excel Add-in v2.5.1.1

_Released 6/4/24_

- 🐞 Wrapped decimal conversion in try/catch where Excel versions were being read in Addin Manager. This fixes a bug where setting the region on your machine causes the Addin Manager to not open.

- ✅ The folder location of the main settings and login information has been moved from the AppData/Local to AppData/Roaming. This ensures that a user's settings are accessible across different Windows instances. When logged in to Interject, the settings are synced and roam between the different environments. This will have little to no effect on single user computers as the roaming folder always exists and persists between logins.

- ✅ Adds a hook to sanitize incoming logs for potentially sensitive data that is included in parameters in error logs or database errors controlled by third party, not reports. Currently only looking for SSNs.

- ✅ The logging feature gathers a minimal amount of data and sends it to the Platform API in batches of no more than 100 or if the last logged data was added more than 5 hours ago.

- ✅ No more than once per day, the Add-in makes a single call to the Platform API to gather which log categories it should be logging. This only happens if it hasn't checked in more than 24 hours. That is also a way to turn off logging for all users; by setting the endpoint to return an empty string, no logs will be gathered.

### Portal Site

_Released 6/6/24_

- ✅ Added a page for managing roles which includes CRUD (Create, Read, Update, Delete) functions, and the ability to add/remove users from roles

- ✅ Added a page for managing folder permissions which adds ability to add/remove roles from folders

- ✅ Added feature for users in IdsClientAdmin role to set a user as a guest on a client account

### Documentation Updates

| Date | Type | Page | Changes |
|---|---|---|---|
| 6/1 | Update | [Installing - Single User](/wAbout/SingleUser.html#file-locations) | New Section |
| 6/1 | Update | [Installing - Shared Computer](/wAbout/SharedComputer.html#file-locations) | New Section |
| 6/12 | New | [Roles](/wPortal/Roles.html) | New page |
| 6/12 | New | [Folder Permissions](/wPortal/FolderPermissions.html) | New Page |
| 6/12 | Update | [Diagnostics](/wIndex/Diagnostics.html) | Updated links |
| 6/12 | New | [Diagnostics - Find All Workbook Formulas](/wIndex/Diagnostics-FindAllFormulas.html) | New Page |
| 6/12 | New | [Diagnostics - Replace Data Portal Codes](/wIndex/Diagnostics-ReplaceDataPortalCodes.html) | New Page |
