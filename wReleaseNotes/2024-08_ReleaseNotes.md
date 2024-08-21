---
title: Release Notes
filename: "2024-08_ReleaseNotes.md"
layout: custom
keywords: [change log, updates, versions, history, what's new]
headings: ["August 2024", "Excel Add-in v2.5.2.11", "Portal Site", "Auth API", "Documentation Updates"]
links: ["/wIndex/SettingsCache.html", "/wIndex/Diagnostics-ListDataPortals.html", "/wIndex/Diagnostics-DoubleClick.html", "/wIndex/Diagnostics-GarbageCollection.html", "/wIndex/Diagnostics-FindAllFormulas.html", "/wIndex/Diagnostics-ReplaceDataPortalCodes.html", "/wIndex/Diagnostics-ClearDataCellCache.html", "/wIndex/Diagnostics-ClearErrorLog.html", "/wIndex/Diagnostics-ReinitiateInterject.html", "/wIndex/Diagnostics-InstallConfig.html", "/wIndex/Diagnostics-EnterpriseConnection.html", "/wPortal/DownloadInterject.html", "/wPortal/MyApps.html", "/wPortal/PublishedApps.html", "/wPortal/Subscribers.html", "/wPortal/AddUser.html", "/wPortal/OrganizationProfile.html", "/wPortal/User-Profile.html"]
image_dir: ""
images: []
description: Release notes for this month's updates
---
* * *

## August 2024

### Excel Add-in v2.5.2.11

_Released 8/20/24_

* ✅ Force use of TLS 1.2 in Add-in Manager

* ✅ Add alternate login method using default system browser instead of WebView2 for scenarios where the user's environment does not or can not support WebView2 embedded browser

* ♻️ Roles are synced a maximum of every 20 minutes to allow changes made in the Interject Portal site to propagate to end users more effectively

* ♻️ Update icons in ribbon menu to be more modern and appear cleaner in various themes

* 🐞 Fix minor bug with macro security enforcement

### Portal Site

_Released 8/20/24_

* ✅ Data Portal command text field now supports SQL and JSON code editing

### Auth API

_Released 8/20/24_

* ✅ Add roles objects to user's client's data

### Documentation Updates

| Date | Type | Page | Changes |
|---|---|---|---|
| 8/21 | Update | [Lab Guide](/wLabs/lab.html) | New labs |
| 8/21 | Update | [Request Context Parse](/wIndex/Request-Context-Parse.html) | Updated code |
| 8/21 | Update | [Develop: Editing Data Save](/wDeveloper/L-Dev-EditingDataSave.html) | Updated code |
| 8/21 | Update | Multiple lab docs | Updated notes/links |
