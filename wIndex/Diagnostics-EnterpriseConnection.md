---
title: Diagnostics - Set Enterprise Connection
filename: "Diagnostics-EnterpriseConnection.md"
layout: custom
keywords: [connection string, encrypt, setup]
headings: ["Overview"]
links: ["https://docs.gointerject.com/wPortal/INTERJECT-Roles.html#clientadmin-role"]
image_dir: "DiagnosticsEnterpriseConnection"
images: [
	{file: "SetEnterpriseConnection", type: "png", site: "Addin", cat: "Diagnostics", sub: "Set Enterprise Connection", report: "", ribbon: "", config: ""},
	{file: "ExecuteCommand", type: "png", site: "Addin", cat: "Diagnostics", sub: "Set Enterprise Connection", report: "", ribbon: "", config: ""}
]
description: The Diagnostic "Set Enterprise Connection" allows an enterprise to store an encrypted connection string.
---
* * *

## Overview

The Diagnostic "Set Enterprise Connection" allows an enterprise to store an encrypted connection string.

![](/images/DiagnosticsEnterpriseConnection/SetEnterpriseConnection.png)
<br>

<blockquote class=highlight_note>
<b>Note:</b> Only <a href="https://docs.gointerject.com/wPortal/INTERJECT-Roles.html#clientadmin-role">ClientAdmins</a> can execute this command. The decrypted connection string is also hidden to non-ClientAdmins in the Diagnostic form.
</blockquote>
<br>

To use this feature, simply input your connection string in the **Input** field and click **Execute Selected Action**:

![](/images/DiagnosticsEnterpriseConnection/ExecuteCommand.png)
<br>
