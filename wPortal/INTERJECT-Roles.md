---
title: Interject Roles
layout: custom
keywords: [roles, user profile, admin, permissions, security]
description: At the bottom of the User Profile page are the roles you currently have assigned to your profile. There are a number of roles to choose from. Roles can stack, meaning each role adds the associated permissions to the user.
---
* * *

## Overview 

At the bottom of the [User Profile](https://docs.gointerject.com/wPortal/User-Profile.html) page are the roles you currently have assigned to your profile. There are a number of roles to choose from. Roles can stack, meaning each role adds the associated permissions to the user.

You can add roles by selecting the role name from the drop down list. Then click **Add New Role** to add the role to the user's profile. Remove roles by clicking the small garbage **<font size="+1">&#x1F5D1;</font>** icon for each role.

![](/images/InterjectRoles/SelectRole.png)
<br>

<blockquote class=highlight_note>
<br><b>Note:</b> Changes will take place on the next successful login from the user.<br><br>
</blockquote>

### Standard Role

_Grants standard permissions to use Interject core features and open live reports._

| Permission | Location | Docs |
|---|---|---|
| View and open live reports in the Report Library | Report Library | [Learn more](/wAbout/Report-Library-Basics.html#opening-a-report) |
| Upload reports to the MyFavorites folder in the Report Library (Test and Dev status only) | Report Library | [Learn more](/wAbout/ReportLibraryLinks.html) |
| Override data connection in jDataPortal | Report Formulas | [Learn more](/wDeveloper/SetupjDataPortal.html#overriding-a-connection) |

### Approver Role

_Grants a user permission to approve reports by changing their status in the Report Library._

| Permission | Location | Docs |
|---|---|---|
| Change report status| Report Library | [Learn more](/wAbout/Report-Library-Basics.html#status) |

### Editor Role

_Grants a user permission to edit and upload reports to the Report Library and Data Portals._

| Permission | Location | Docs |
|---|---|---|
| Upload reports to the Report Library (Test and Dev status only) | Report Library | [Learn more](/wAbout/ReportLibraryLinks.html) |
| Edit report details in the Report Library | Report Library | [Learn more](/wAbout/ReportLibraryLinks.html#updating-a-report-link) |
| Override Data Portal command in jDataPortal | Report Formulas | [Learn more](/wDeveloper/SetupjDataPortal.html#overriding-a-command) |
| Create, Update, Delete, Clone, and Enabled/Disable Data Portals | Portal Site | [Learn more](/wPortal/Data-Portals.html) |
| Create, Update, and Delete Data Portal parameters | Portal Site | [Learn more](/wPortal/Data-Portals.html#overview-of-parameters) |

### Corporate Role

_Grants permission to view and access restricted Corporate folders in the Report Library._

| Permission | Location | Docs |
|---|---|---|
| Corporate abilities and access to any restricted Corporate folders | Report Library | Coming soon |

### Protector Role

_Grants permission to use the Interject Sheet Protector._

| Permission | Location | Docs |
|---|---|---|
| Use the Interject Sheet Protector to protect and unprotect sheets or workbooks | Sheet Protector | [Learn more](/wGetStarted/L-Create-Protecting.html) |

### CustomerItems Role

_Grants permissions to execute Custom Commands._

| Permission | Location | Docs |
|---|---|---|
| Execute items (non-scheduled) in Custom Commands | Custom Commands | [Learn more](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#custom-commands) |

### SchedulerAdmin Role

_Grants permission of schedule items in Custom Commands._

| Permission | Location | Docs |
|---|---|---|
| Full control of the scheduled items in Custom Commands | Custom Commands | [Learn more](/bApps/bFinancials/Configure.html) |

### ClientAdmin Role

_Grants all Interject permissions with the exception of the Corporate role._

| Permission | Location | Docs |
|---|---|---|
| View and open reports in the Report Library | Report Library | [Learn more](/wAbout/Report-Library-Basics.html#opening-a-report) |
| Upload reports to the Report Library | Report Library | [Learn more](/wAbout/ReportLibraryLinks.html) |
| Edit report details in the Report Library | Report Library | [Learn more](/wAbout/ReportLibraryLinks.html#updating-a-report-link) |
| Override data connection in jDataPortal | Report Formulas | [Learn more](/wDeveloper/SetupjDataPortal.html#overriding-a-connection) |
| Download file whose checksum did not match original checksum | Report Library | [Learn more](/wIndex/MacroSecurity.html) |
| Override Data Portal command in jDataPortal | Report Formulas | [Learn more](/wDeveloper/SetupjDataPortal.html#overriding-a-command) |
| Use the Interject Sheet Protector to protect and unprotect sheets or workbooks | Sheet Protector | [Learn more](/wGetStarted/L-Create-Protecting.html) |
| Execute items in Customer Commands | Custom Commands | [Learn more](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#custom-commands) |
| Full control of the scheduled items in Custom Commands | Custom Commands | [Learn more](/bApps/bFinancials/Configure.html) |
| Create, Update, Delete, Clone, and Enabled/Disable Data Portals | Portal Site | [Learn more](/wPortal/Data-Portals.html) |
| Create, Update, and Delete Data Portal parameters | Portal Site | [Learn more](/wPortal/Data-Portals.html#overview-of-parameters) |
| Create password reset emails with password reset link | Portal Site | [Learn more](/wPortal/Altering-User-Passwords.html) |
| Create, Update, Delete, and Enable/Disable users | Portal Site | Coming soon |
| Force refresh of cache data for all users | Diagnostics | [Learn more](/wIndex/Diagnostics.html#system-tools) |
| Set application data source | Diagnostics | [Learn more](/wIndex/Diagnostics.html#support) |
| Set Enterprise Connection | Diagnostics | [Learn more](/wIndex/Diagnostics.html#system-tools) |
| Launch the License Management Form | Diagnostics | [Learn more](/wIndex/Diagnostics.html#support) |
