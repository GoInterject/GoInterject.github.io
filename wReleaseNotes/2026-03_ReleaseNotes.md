---
title: Release Notes
filename: "2026-03_ReleaseNotes.md"
layout: custom
keywords: [change log, updates, versions, history, what's new]
headings: ["March 2026", "Excel Add-in", "Customer Portal", "Platform API"]
links: []
image_dir: ""
images: []
description: Release notes for this month's updates
---

## March 2026

### **Excel Add-in** (GoInterject/ids-legacy)

✨ Features:
- Document validation for downloaded files (#94)

🔧 Improvements:
- Automatic release scope detection (#97)
- Disabled LoadAtStartup for all installers (#90)
- Updated code signing timestamp URL (#96)


### **Customer Portal** (GoInterject/ids-portal)

✨ Features:
- Scheduler Admin UI #(59)

🐛 Bug Fixes:
- Fixed unauthorized logout on DataPortal modifications (#66)

🔧 Improvements:
- Active user filter on staff page (#61)
- Dynamic Auth API version retrieval (#61)
- Disabled autocomplete on user profile forms (#61)
- Scheduler error visibility (#67)


### **Platform API** (GoInterject/ids-platform-api)

✨ Features:
- Scheduler API endpoints (#61)

🐛 Bug Fixes:
- Fixed folder role count display (#64)
- Fixed identity provider display for federated logins (#63)

⚠️ Database Updates:
- Stored procedure update required (#63)
