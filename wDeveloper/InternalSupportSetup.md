---
title: Internal Support Setup
filename: "InternalSupportSetup.md"
layout: custom
keywords: [settings, config, app.config, tech support, contact]
headings: ["Overview", "Setup"]
links: []
image_dir: "InternalSupportSetup"
images: [
{file: "SupportForm", type: "png", site: "Addin", cat: "Support", sub: "", report: "", ribbon: "", config: ""},
{file: "InterjectFolder", type: "png", site: "Windows", cat: "Explorer", sub: "", report: "", ribbon: "", config: ""},
{file: "OpenAppConfig", type: "png", site: "Windows", cat: "Explorer", sub: "", report: "", ribbon: "", config: ""},
{file: "AddEntries", type: "png", site: "External", cat: "Notepad", sub: "", report: "", ribbon: "", config: ""},
{file: "UserSupport", type: "png", site: "Addin", cat: "Ribbon", sub: "", report: "", ribbon: "Simple", config: ""},
{file: "SupportForm", type: "png", site: "Addin", cat: "Support", sub: "", report: "", ribbon: "", config: ""},
]
description: Interject provides a way to add your own internal support contact information to the Interject User Support form.
---
* * *

## Overview

Interject provides a way to add your own internal support contact information to the Interject User Support form:

![](/images/InternalSupportSetup/SupportForm.png)
<br>

### Setup

**Step 1:** Ensure Excel is not running.

**Step 2:** Navigate to the program directory for Interject:

![](/images/InternalSupportSetup/InterjectFolder.png)
<br>

**Step 3:** Open the `app.config` file with a text editor:

![](/images/InternalSupportSetup/OpenAppConfig.png)
<br>

**Step 4:** In the &lt;appSettings&gt; node, add the following entries:

```xml
	<add key="InternalSupport_Email" value="support@northwinddata.com" />
	<add key="InternalSupport_Phone" value="123-456-7890" />
	<add key="InternalSupport_Website" value="www.northwinddatacompany.com" />
```

![](/images/InternalSupportSetup/AddEntries.png)
<br>

**Step 5:** Open up Excel and click the **User Support** button:

![](/images/InternalSupportSetup/UserSupport.png)
<br>

See your new internal support tab:

![](/images/InternalSupportSetup/SupportForm.png)
<br>