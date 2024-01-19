---
title: Interject Roles
filename: "INTERJECT-Roles.md"
layout: custom
keywords: [roles, user profile, admin, permissions, security]
headings: ["Overview", "Standard Role", "Approver Role", "Editor Role", "Corporate Role", "Protector Role", "CustomItems Role", "SchedulerAdmin Role", "ClientAdmin Role"]
links: ["https://docs.gointerject.com/wPortal/User-Profile.html", "https://docs.gointerject.com/wAbout/ReportLibraryLinks.html", "https://docs.gointerject.com/wAbout/ReportLibraryLinks.html", "https://docs.gointerject.com/wDeveloper/SetupjDataPortal.html#overriding-a-connection", "https://docs.gointerject.com/wAbout/Report-Library-Basics.html#status", "https://docs.gointerject.com/wAbout/ReportLibraryLinks.html", "https://docs.gointerject.com/wAbout/ReportLibraryLinks.html#updating-a-report-link", "https://docs.gointerject.com/wDeveloper/SetupjDataPortal.html#overriding-a-command", "https://docs.gointerject.com/wPortal/Data-Portals.html", "https://docs.gointerject.com/wPortal/Data-Portals.html#overview-of-parameters", "https://docs.gointerject.com/wGetStarted/L-Create-Protecting.html", "https://docs.gointerject.com/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#custom-commands", "/bApps/bFinancials/Configure.html", "https://docs.gointerject.com/wAbout/Report-Library-Basics.html#opening-a-report", "https://docs.gointerject.com/wAbout/ReportLibraryLinks.html", "https://docs.gointerject.com/wAbout/ReportLibraryLinks.html#updating-a-report-link", "https://docs.gointerject.com/wDeveloper/SetupjDataPortal.html#overriding-a-connection", "https://docs.gointerject.com/wIndex/MacroSecurity.html", "https://docs.gointerject.com/wDeveloper/SetupjDataPortal.html#overriding-a-command", "https://docs.gointerject.com/wGetStarted/L-Create-Protecting.html", "https://docs.gointerject.com/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#custom-commands", "/bApps/bFinancials/Configure.html", "https://docs.gointerject.com/wPortal/Data-Portals.html", "https://docs.gointerject.com/wPortal/Data-Portals.html#overview-of-parameters", "https://docs.gointerject.com/wPortal/Altering-User-Passwords.html", "https://docs.gointerject.com/wPortal/StaffPage.html", "https://docs.gointerject.com/wIndex/Diagnostics.html#system-tools", "https://docs.gointerject.com/wIndex/Diagnostics.html#support", "https://docs.gointerject.com/wIndex/Diagnostics.html#system-tools", "https://docs.gointerject.com/wIndex/Diagnostics.html#support"]
image_dir: "InterjectRoles"
description: At the bottom of the User Profile page are the roles you currently have assigned to your profile. There are a number of roles to choose from. Roles can stack, meaning each role adds the associated permissions to the user.
---
* * *

## Overview 

At the bottom of the [User Profile](https://docs.gointerject.com/wPortal/User-Profile.html) page are the roles you currently have assigned to your profile. There are a number of roles to choose from. Roles can stack, meaning each role adds the associated permissions to the user.

You can add roles by selecting the role name from the drop down list. Then click **Add New Role** to add the role to the user's profile. Remove roles by clicking the small garbage **<font size="+1">&#x1F5D1;</font>** icon for each role.

![](/images/InterjectRoles/SelectRole.png)
<br>

<blockquote class=highlightnote>
<br><b>Note:</b> Changes will take place on the next successful login from the user.<br><br>
</blockquote>

### Standard Role

<button class="collapsible-expanded">Grants standard permissions to use Interject core features and open live reports.</button>
<div markdown="1" class="panel-expanded">
<table>
<tbody>

<td class="ith" style="width: 60%;"><b>Permission</b></td>
<td class="ith" style="width: 20%;"><b>Location</b></td>
<td class="ith" style="width: 20%;"><b>Docs</b></td>

<tr>
<td> View and open live reports in the Report Library </td>
<td> Report Library </td>
<td> <a href="https://docs.gointerject.com/wAbout/ReportLibraryLinks.html">Learn more</a></td>
</tr>
<tr>
<td> Upload reports to the MyFavorites folder in the Report Library (Test and Dev status only) </td>
<td> Report Library </td>
<td> <a href="https://docs.gointerject.com/wAbout/ReportLibraryLinks.html">Learn more</a> </td>
</tr>
<tr>
<td> Override data connection in jDataPortal </td>
<td> Report Formulas </td>
<td> <a href="https://docs.gointerject.com/wDeveloper/SetupjDataPortal.html#overriding-a-connection">Learn more</a> </td>
</tr>

</tbody>
</table>
</div>

### Approver Role

<button class="collapsible-expanded">Grants a user permission to approve reports by changing their status in the Report Library.</button>
<div markdown="1" class="panel-expanded">
<table>
<tbody>

<td class="ith" style="width: 60%;"><b>Permission</b></td>
<td class="ith" style="width: 20%;"><b>Location</b></td>
<td class="ith" style="width: 20%;"><b>Docs</b></td>

<tr>
<td> Change report status</td>
<td> Report Library </td>
<td> <a href="https://docs.gointerject.com/wAbout/Report-Library-Basics.html#status">Learn more</a> </td>
</tr>

</tbody>
</table>
</div>

### Editor Role

<button class="collapsible-expanded">Grants a user permission to edit and upload reports to the Report Library and Data Portals.</button>
<div markdown="1" class="panel-expanded">
<table>
<tbody>

<td class="ith" style="width: 60%;"><b>Permission</b></td>
<td class="ith" style="width: 20%;"><b>Location</b></td>
<td class="ith" style="width: 20%;"><b>Docs</b></td>

<tr>
<td> Upload reports to the Report Library (Test and Dev status only) </td>
<td> Report Library </td>
<td> <a href="https://docs.gointerject.com/wAbout/ReportLibraryLinks.html">Learn more</a> </td>
</tr>
<tr>
<td> Edit report details in the Report Library </td>
<td> Report Library </td>
<td> <a href="https://docs.gointerject.com/wAbout/ReportLibraryLinks.html#updating-a-report-link">Learn more</a> </td>
</tr>
<tr>
<td> Override Data Portal command in jDataPortal </td>
<td> Report Formulas </td>
<td> <a href="https://docs.gointerject.com/wDeveloper/SetupjDataPortal.html#overriding-a-command">Learn more</a> </td>
</tr>
<tr>
<td> Create, Update, Delete, Clone, and Enabled/Disable Data Portals </td>
<td> Portal Site </td>
<td> <a href="https://docs.gointerject.com/wPortal/Data-Portals.html">Learn more</a> </td>
</tr>
<tr>
<td> Create, Update, and Delete Data Portal parameters </td>
<td> Portal Site </td>
<td> <a href="https://docs.gointerject.com/wPortal/Data-Portals.html#overview-of-parameters">Learn more</a> </td>
</tr>

</tbody>
</table>
</div>

### Corporate Role

<button class="collapsible-expanded">Grants permission to view and access restricted Corporate folders in the Report Library.
</button>
<div markdown="1" class="panel-expanded">
<table>
<tbody>

<td class="ith" style="width: 60%;"><b>Permission</b></td>
<td class="ith" style="width: 20%;"><b>Location</b></td>
<td class="ith" style="width: 20%;"><b>Docs</b></td>

<tr>
<td> Corporate abilities and access to any restricted Corporate folders </td>
<td> Report Library </td>
<td> Coming soon </td>
</tr>

</tbody>
</table>
</div>

### Protector Role

<button class="collapsible-expanded">Grants permission to use the Interject Sheet Protector.
</button>
<div markdown="1" class="panel-expanded">
<table>
<tbody>

<td class="ith" style="width: 60%;"><b>Permission</b></td>
<td class="ith" style="width: 20%;"><b>Location</b></td>
<td class="ith" style="width: 20%;"><b>Docs</b></td>

<tr>
<td> Use the Interject Sheet Protector to protect and unprotect sheets or workbooks </td>
<td> Sheet Protector </td>
<td> <a href="https://docs.gointerject.com/wGetStarted/L-Create-Protecting.html">Learn more</a> </td>
</tr>

</tbody>
</table>
</div>

### CustomItems Role

<button class="collapsible-expanded">Grants permissions to execute Custom Commands.
</button>
<div markdown="1" class="panel-expanded">
<table>
<tbody>

<td class="ith" style="width: 60%;"><b>Permission</b></td>
<td class="ith" style="width: 20%;"><b>Location</b></td>
<td class="ith" style="width: 20%;"><b>Docs</b></td>

<tr>
<td> Execute items (non-scheduled) in Custom Commands </td>
<td> Custom Commands </td>
<td> <a href="https://docs.gointerject.com/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#custom-commands">Learn more</a> </td>
</tr>

</tbody>
</table>
</div>

### SchedulerAdmin Role

<button class="collapsible-expanded">Grants permission of schedule items in Custom Commands.
</button>
<div markdown="1" class="panel-expanded">
<table>
<tbody>

<td class="ith" style="width: 60%;"><b>Permission</b></td>
<td class="ith" style="width: 20%;"><b>Location</b></td>
<td class="ith" style="width: 20%;"><b>Docs</b></td>

<tr>
<td> Full control of the scheduled items in Custom Commands </td>
<td> Custom Commands </td>
<td> <a href="/bApps/bFinancials/Configure.html">Learn more</a> </td>
</tr>

</tbody>
</table>
</div>

### ClientAdmin Role

<button class="collapsible-expanded">Grants all Interject permissions with the exception of the Corporate role.
</button>
<div markdown="1" class="panel-expanded">
<table>
<tbody>

<td class="ith" style="width: 60%;"><b>Permission</b></td>
<td class="ith" style="width: 20%;"><b>Location</b></td>
<td class="ith" style="width: 20%;"><b>Docs</b></td>

<tr>
<td> View and open reports in the Report Library </td>
<td> Report Library </td>
<td> <a href="https://docs.gointerject.com/wAbout/Report-Library-Basics.html#opening-a-report">Learn more</a> </td>
</tr>
<tr>
<td> Upload reports to the Report Library </td>
<td> Report Library </td>
<td> <a href="https://docs.gointerject.com/wAbout/ReportLibraryLinks.html">Learn more</a> </td>
</tr>
<tr>
<td> Edit report details in the Report Library </td>
<td> Report Library </td>
<td> <a href="https://docs.gointerject.com/wAbout/ReportLibraryLinks.html#updating-a-report-link">Learn more</a> </td>
</tr>
<tr>
<td> Override data connection in jDataPortal </td>
<td> Report Formulas </td>
<td> <a href="https://docs.gointerject.com/wDeveloper/SetupjDataPortal.html#overriding-a-connection">Learn more</a> </td>
</tr>
<tr>
<td> Download file whose checksum did not match original checksum </td>
<td> Report Library </td>
<td> <a href="https://docs.gointerject.com/wIndex/MacroSecurity.html">Learn more</a> </td>
</tr>
<tr>
<td> Override Data Portal command in jDataPortal </td>
<td> Report Formulas </td>
<td> <a href="https://docs.gointerject.com/wDeveloper/SetupjDataPortal.html#overriding-a-command">Learn more</a> </td>
</tr>
<tr>
<td> Use the Interject Sheet Protector to protect and unprotect sheets or workbooks </td>
<td> Sheet Protector </td>
<td> <a href="https://docs.gointerject.com/wGetStarted/L-Create-Protecting.html">Learn more</a> </td>
</tr>
<tr>
<td> Execute items in Custom Commands </td>
<td> Custom Commands </td>
<td> <a href="https://docs.gointerject.com/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#custom-commands">Learn more</a> </td>
</tr>
<tr>
<td> Full control of the scheduled items in Custom Commands </td>
<td> Custom Commands </td>
<td> <a href="/bApps/bFinancials/Configure.html">Learn more</a> </td>
</tr>
<tr>
<td> Create, Update, Delete, Clone, and Enabled/Disable Data Portals </td>
<td> Portal Site </td>
<td> <a href="https://docs.gointerject.com/wPortal/Data-Portals.html">Learn more</a> </td>
</tr>
<tr>
<td> Create, Update, and Delete Data Portal parameters </td>
<td> Portal Site </td>
<td> <a href="https://docs.gointerject.com/wPortal/Data-Portals.html#overview-of-parameters">Learn more</a> </td>
</tr>
<tr>
<td> Create password reset emails with password reset link </td>
<td> Portal Site </td>
<td> <a href="https://docs.gointerject.com/wPortal/Altering-User-Passwords.html">Learn more</a> </td>
</tr>
<tr>
<td> View Staff Page and Add, Edit, Delete, and Activate/Deactivate users </td>
<td> Portal Site </td>
<td> <a href="https://docs.gointerject.com/wPortal/StaffPage.html">Learn more</a> </td>
</tr>
<tr>
<td> Force refresh of cache data for all users </td>
<td> Diagnostics </td>
<td> <a href="https://docs.gointerject.com/wIndex/Diagnostics.html#system-tools">Learn more</a> </td>
</tr>
<tr>
<td> Set application data source </td>
<td> Diagnostics </td>
<td> <a href="https://docs.gointerject.com/wIndex/Diagnostics.html#support">Learn more</a> </td>
</tr>
<tr>
<td> Set Enterprise Connection </td>
<td> Diagnostics </td>
<td> <a href="https://docs.gointerject.com/wIndex/Diagnostics.html#system-tools">Learn more</a> </td>
</tr>
<tr>
<td> Launch the License Management Form </td>
<td> Diagnostics </td>
<td> <a href="https://docs.gointerject.com/wIndex/Diagnostics.html#support">Learn more</a> </td>
</tr>

</tbody>
</table>
</div>
