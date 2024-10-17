---
title: TLS Changes
filename: "TLSUsers.md"
layout: custom
keywords: []
headings: ["Overview"]
links: []
image_dir: ""
images: [
    {file: "", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}
]
description: 
---
* * *

## Overview

Microsoft [announced](https://learn.microsoft.com/en-us/lifecycle/announcements/tls-support-ending-10-31-2024){:target="_blank"}{:rel="noopener noreferrer"} that all TLS communications must use version 1.2 starting October 31, 2024. After that date, any communication using TLS 1.0 or 1.1 will not work.

This means users on versions of Interject that use TLS 1.1 will need to either:

- [Update Interject](https://portal.gointerject.com/download-interject.html)

- [Update TLS](/wAbout/TLS.html#set-tls-settings-via-idssettings-file) to TLS 1.2.

### Update Interject From Version 2.5+

When updating Interject from a 2.5 version and above, you simply have to click the **Check for Updates** button on the Interject ribbon. Then click **Get Update**:

![](/images/TLSUser/GetUpdate.png)
<br>

For detailed instructions about updating Interject, see [here](/wAbout/Updating-INTERJECT.html).


### Update Interject From Version 2.3.34

If you have Interject version 2.3.34, you will have to uninstall this version first.

1. [Uninstall](/wAbout/Uninstalling.html) Interject

2. [Download](/wPortal/DownloadInterject.html) Interject from the portal site

3. [Install](/wAbout/SharedComputer.html) Interject

### Updating TLS 1.2

For those who still want to use an older version of Interject, you can still update the Interject settings to use TLS 1.2. For more info, see [here](/wAbout/TLS.html).

### Contact Interject

If you are having difficulty in updating Interject or TLS, there are a number of ways to contact us:

- [Email us](mailto:help@gointerject.com)

- [Create a support ticket](/wTroubleshoot/Reporting-A-Problem.md#send-report-to-interject)

- Click **User Support** for options

![](/images/TLSUser/UserSupport.png)
