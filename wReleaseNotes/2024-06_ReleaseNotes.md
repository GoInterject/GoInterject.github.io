---
title: Release Notes
filename: "2024-06_ReleaseNotes.md"
layout: custom
keywords: [change log, updates, versions, history, what's new]
headings: ["June 2024", "Excel Addin v2.5.1.1", "Portal Site", "Documentation Updates"]
links: []
image_dir: ""
images: []
description: Release notes for this month's updates
---
* * *

## June 2024

### Excel Addin v2.5.1.1

_Released 6/4/24_

- 🐞 Wrapped decimal conversion in try/catch where excel versions were being read in addin manager. This fixes a bug where setting the region on your machine causes the addin manager to not open.

- ✅ The main settings and login information are moved from the AppData local to AppData roaming so that when a user is in a shared environment with multiple possible windows instances they could log into, their Interject login and settings can roam between them. This will have little to no effect on single user computers as the roaming folder always exists and persists between logins.

- ✅ Adds a hook to sanitize incoming logs for potentially sensitive data. Currently only looking for SSNs.

- ✅ The logging feature gathers a minimal amount of data and sends it to the Platform API in batches of no more than 100 or if the last logged data was added more than 5 hours ago.

- ✅ No more than once per day, the add-in makes a single call to the Platform API to gather which log categories it should be logging. This only happens if it hasn't checked in more than 24 hours. That is also a way to turn off logging for all users; by setting the endpoint to return an empty string, no logs will be gathered.

### Portal Site

_Released 6/6/24_

- ✅ Added a page for managing roles which includes crud functions, and the ability to add/remove users from roles

- ✅ Added a page for managing folder permissions which adds ability to add/remove roles from folders

- ✅ Added feature for users in IdsClientAdmin role to set a user as a guest on a client account

### Documentation Updates

| Date | Type | Page | Changes |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
