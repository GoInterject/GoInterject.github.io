---
title: Release Notes
filename: "2026-08_ReleaseNotes.md"
layout: custom
keywords: [change log, updates, versions, history, what's new, report scheduler, subscriptions]
headings: ["August 2026", "Report Scheduler", "Excel Add-in v2.5.7.0", "Portal Site", "Platform and Security"]
links: ["/wAbout/Report-Library-Basics.html", "/wDeveloper/InternalSupportSetup.html", "/wFunctions/PairGroup.html", "/wIndex/SettingsCache.html", "/wPortal/OrganizationProfile.html", "/wDeveloper/MacroSecurity.html", "/wPortal/StaffPage.html", "/wPortal/DownloadInterject.html"]
image_dir: ""
images: []
description: Release notes for this month's updates
---
* * *

## August 2026

### Report Scheduler

_Released 8/28/26_

The headline feature of this release: schedule an Interject report to run on its own and arrive in your inbox — no need to open Excel, and no need to be at your desk.

<blockquote class=highlight_note>
<b>Note:</b> Report scheduling must be enabled for your organization before the Subscriptions page appears in the Portal. Contact Interject to get set up.
</blockquote>
<br>

* ✅ Create a subscription straight from the Excel ribbon under **Schedule Report → New**. Pick your report parameters, then set the schedule.

* ✅ Flexible recurrence — choose any combination of months, days of the week, day of the month (or a week-and-day pattern such as "the third Friday"), hours, and minutes, with an optional start and end date. Times are entered and displayed in your own time zone.

* ✅ Scheduled reports run on the server and pull fresh data, then the finished workbook is emailed to the recipient you choose. Excel is not required for the run, and macro-enabled workbooks are supported.

* ✅ Manage everything from the new **Subscriptions** page in the Portal — search by report or user, switch between your reports and all reports, edit, pause and resume, delete, or trigger an immediate run with **Run Now**.

* ✅ Every subscription shows its last run result, next due time, and status at a glance. A run that ends in error is flagged with a warning icon, with the error message and logs one click away.

* ✅ Administrators get a new **Scheduler Dashboard** summarizing run counts, failures, and on-time delivery for the last 24 hours.

### Interject Add-in v2.5.7.0

_Released 8/28/26_

* ✅ [Report Library](/wAbout/Report-Library-Basics.html) now resolves OneDrive and SharePoint links to local file paths — paste a synced URL and the add-in fills in the local path for you.

* ✅ Report Library downloads are now validated on open, and files with trailing or corrupted bytes are repaired automatically.

* ✅ [PairGroup](/wFunctions/PairGroup.html) formulas now support up to 64 pair groups, raised from 34, reducing ReportDefaults errors on reports that use many Pair formulas.

* ♻️ The Pull Data, Report Library, and Support windows now remember their size — resize from the footer grip and the size persists.

* ♻️ **Check for Updates** in the add-in now uses the same logic as the Add-in Manager, so both report the same available versions.

* ♻️ The Add-in Manager now detects per-user versus per-machine install scope automatically from the install location, folder permissions, and registry.

* ♻️ Diagnostics Data Portal list output is now plain text, making it easier to read and copy.

* 🐞 Numerous bug fixes and security improvements.

### Portal Site

_Released 8/28/26_

* ✅ New **Subscriptions** page for managing scheduled reports, plus an admin **Scheduler Dashboard** — see [Report Scheduler](#report-scheduler) above.

* ✅ Support contact details — email, phone, and website — can now be set on the [Organization Profile](/wPortal/OrganizationProfile.html) page and are shown to your users inside the Interject Add-in.

* ✅ New Report Library sort order setting on the Organization Profile page to adjust how the Interject Add-in sorts Report Library files.

* ✅ New Cache Refresh on Pull and Save setting is available on the Organization Profile page.

* ✅ Documentation links and hover-over descriptions added to the [Macro Security](/wDeveloper/MacroSecurity.html) and Report Library settings.

* ♻️ Rebuilt the [installer download](/wPortal/DownloadInterject.html) experience with progress and status modals, correct version selection, checksum retrieval, and clearer error messages.

* ♻️ The downloads page now lists the latest version alongside previous versions.

* ♻️ User options in the company dropdown have been reorganized, with your name and avatar at the top and My Profile and Log Out beneath. The menu now behaves correctly on mobile.

* ♻️ The [Staff page](/wPortal/StaffPage.html) now shows only active users.

* ♻️ Inactive roles are no longer offered when assigning roles to a user.

* ♻️ Attempting an action without the required role now shows a clear message instead of logging you out.

* ♻️ Release Manager visibility now matches the roles required by the API.

* 🐞 Numerous bug fixes and security improvements.

