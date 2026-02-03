---
title: Release Notes
filename: "2026-02_ReleaseNotes.md"
layout: custom
keywords: [change log, updates, versions, history, what's new]
headings: ["February 2026", "Excel Add-in", "Customer Portal", "Platform API"]
links: []
image_dir: ""
images: []
description: Release notes for this month's updates
---

## February 2026

### **Excel Add-in** (GoInterject/ids-legacy)

✨ Features:
- Multi-folder report management (#64)
- Document validation for downloaded files (#94)

🔧 Improvements:
- Automatic release scope detection (#97)
- Disabled LoadAtStartup for all installers (#90)
- Updated code signing timestamp URL (#96)


### **Customer Portal** (GoInterject/ids-portal)

🐛 Bug Fixes:
- Fixed unauthorized logout on DataPortal modifications (#62)

🔧 Improvements:
- Active user filter on staff page (#61)
- Dynamic Auth API version retrieval (#61)
- Disabled autocomplete on user profile forms (#61)


### **Platform API** (GoInterject/ids-platform-api)

✨ Features:
- Multi-folder report API endpoints and schema (#31)

🐛 Bug Fixes:
- Fixed folder role count display (#64)
- Fixed identity provider display for federated logins (#63)

⚠️ Database Updates:
- Schema changes for multi-folder support (#31)
- Stored procedure update required (#63)
