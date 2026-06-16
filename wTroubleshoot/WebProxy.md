---
title: Web Proxy Configuration
filename: "WebProxy.md"
layout: custom
keywords: [config, settings, diagnostics, app.config]
headings: ["Overview", "Configure via Diagnostics Setting", "Configure via app.config File"]
links: ["https://learn.microsoft.com/en-us/dotnet/api/system.net.credentialcache.defaultcredentials", "https://learn.microsoft.com/en-us/dotnet/framework/configure-apps/file-schema/network/defaultproxy-element-network-settings"]
image_dir: "App-Errors"
images: [
	{file: "DiagnosticsButton", type: "png", site: "Add-in", cat: "Ribbon", sub: "", report: "", ribbon: "Advanced", config: ""}, 
	{file: "DiagnosticsSetProxyUsage", type: "png", site: "Add-in", cat: "Diagnostics", sub: "Set Proxy Usage", report: "", ribbon: "", config: ""}
	]
description: The Interject Add-in allows users to authenticate using Windows authentication. For this Interject uses the Microsoft DefaultCredentials library to set up a proxy.
---
* * *

## Overview

The Interject Add-in allows users to authenticate using Windows authentication. For this Interject uses [System.Net.CredentialCache.DefaultCredentials](https://learn.microsoft.com/en-us/dotnet/api/system.net.credentialcache.defaultcredentials){:target="_blank"}{:rel="noopener noreferrer"} library to set up a proxy. Interject's default Windows proxy at the application level can prevent a client's machine level proxy. This will prevent a user from being able to log in. To get around this, there is an Interject setting where users and clients can disable the Windows proxy.

### Configure via Diagnostics Setting

To access the setting, click on the **Diagnostics** button on the Interject ribbon:

![](/images/App-Errors/DiagnosticsButton.png)
<br>

The setting is called "Set Proxy Usage" found on the "Web Service" section:

![](/images/App-Errors/DiagnosticsSetProxyUsage.png)
<br>

The following values reflect the possible inputs:

- 1 = Do nothing (no change)
- 2 = use Default Credentials (recommended)
- 3 = Skip Proxy (Set To Null)
- 1 (Remember) = Change setting to 1 and do not revert back to the default 2 upon startup
- 2 (Remember) = Change setting to 2 and do not revert back to the default 2 upon startup
- 3 (Remember) = Change setting to 3 and do not revert back to the default 2 upon startup

To disable Interject's default web proxy, enter 3 in the Input section and click **Execute Selected Action**.

### Configure via app.config File

Another option for configuring Interject's proxy network behavior is to configure Interject's app.config file. For more information, see the [official documentation](https://learn.microsoft.com/en-us/dotnet/framework/configure-apps/file-schema/network/defaultproxy-element-network-settings){:target="_blank"}{:rel="noopener noreferrer"} at Microsoft.
