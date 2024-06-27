---
title: Organization Profile
filename: "OrganizationProfile.md"
layout: custom
keywords: [company, details, information, smtp, cache]
headings: ["Overview", "Organization Details", "Settings"]
links: ["/wPortal/INTERJECT-Roles.html#clientadmin-role", "/wAbout/Enterprise-Login-Setup.html#enterprise-login-code", "/wIndex/SettingsCache.html", "https://support.microsoft.com/en-us/office/pop-imap-and-smtp-settings-for-outlook-com-d088b986-291d-42b8-9564-9c414e2aa040", "https://help.socketlabs.com/docs/getting-started-with-smtp"]
image_dir: "OrganizationProfile"
images: [
	{file: "OrganizationProfile", type: "png", site: "Portal", cat: "Organization Profile", sub: "", report: "", ribbon: "", config: ""},
	{file: "OrganizationDetails", type: "png", site: "Portal", cat: "Organization Profile", sub: "", report: "", ribbon: "", config: ""},
	{file: "Settings", type: "png", site: "Portal", cat: "Organization Profile", sub: "", report: "", ribbon: "", config: ""}
]
description: The Organization Profile allows ClientAdmins to change their organization's details.
---
* * *

## Overview

The Organization Profile allows [ClientAdmins](/wPortal/INTERJECT-Roles.html#clientadmin-role) to change their organization's details.

![](/images/OrganizationProfile/OrganizationProfile.png)
<br>

### Organization Details

ClientAdmins can change details of their organization here.

- [Enterprise Login Codes](/wAbout/Enterprise-Login-Setup.html#enterprise-login-code): These are login codes that have been set up for your company by Interject.
- Authorization Type ID: This is unchangeable. Interject sets auth ID 10 for Interject authentication.
- License Renew Date: This is unchangeable. Displays the current license's expiration date.
- Created Dated: Optional field to display the company's created date of Interject.
- Last Modified Date: Optional field to display when the organization Profile was last updated.

![](/images/OrganizationProfile/OrganizationDetails.png)
<br>

### Settings

Under the Settings section, ClientAdmins can force a reset of every user's [cache](/wIndex/SettingsCache.html) on their next log in by clicking on the **cache** button.

In addition, they also have the ability to configure essential SMTP (Simple Mail Transfer Protocol) settings to enable email communications from the system. This includes setting up the SMTP server, which is the address of the server that handles outgoing emails, and the SMTP username, which is the login credential for the server. The SMTP password, securely encrypted to ensure data protection, must also be provided to authenticate the connection. Additionally, administrators can specify a default sender email address, which will appear as the sender for all outgoing emails unless overridden. These configurations ensure seamless and secure email delivery from the organization’s system.

For information on specific SMTP setup, see [SMTP settings for Outlook](https://support.microsoft.com/en-us/office/pop-imap-and-smtp-settings-for-outlook-com-d088b986-291d-42b8-9564-9c414e2aa040){:target="_blank"}{:rel="noopener noreferrer"} or [Setup for SocketLabs](https://help.socketlabs.com/docs/getting-started-with-smtp){:target="_blank"}{:rel="noopener noreferrer"}.

![](/images/OrganizationProfile/Settings.png)
<br>
