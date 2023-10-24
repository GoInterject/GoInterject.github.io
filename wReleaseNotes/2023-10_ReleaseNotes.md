---
title: Release Notes
layout: custom
keywords: [change log, updates, versions, history, what's new]
description: Release notes for the previous month's updates
---
* * *

## October 2023

### Excel Addin v2.5.0.22

* ✅ `jDataPortal` DataResultNumber now supports Indexing from the end of the results - [See docs](/wDeveloper/SetupjDataPortal.html)

* ✅ Update source of identity providers displayed in the connection manager to all id providers in current client (includes overrides)

* ✅ Refresh user company list on activate/deactivate client

* ♻️ Legacy auth token is refreshed every 2 days instead of 19

* ♻️ Inactive clients no longer show up in the company ddl

* 🐞 Opening report library now checks for legacy idsSession token refresh

<br>

### Portal Site

* ✅ Added MFA config model to staff page in portal - [[URL to MFA in Interject]]

* ✅ Added Checksum added next to the installer download button on portal site - [See docs](/wDeveloper/InstallerValidation.html)

* ♻️ Improved default description box size for data connections

* ♻️ Removed Unsubscribe button from portal site until functionality for it exists

* ♻️ New Interject companies are no longer automatically subscribed to the "Interject Tools" published app

* 🐞 Create user profile no longer populates logged in users information

* 🐞 Fixed header bleeding through company dropdown

<br>

### Interject Platform

* ✅ Added conditional access for user logins to allow control federated user logins to Interject - [See docs](/wDeveloper/ConditionalAccess.html)