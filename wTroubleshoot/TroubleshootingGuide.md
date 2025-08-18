---
title: Troubleshooting Guide
filename: "TroubleshootingGuide.md"
layout: custom
keywords: [errors, solutions, fix]
headings: ["Overview", "Error: Add-in Not Completely Loaded", "Error: Incompatible FIPS", "Error: Interject Web API Offline", "Error: Can't Install or Uninstall Interject", "Error: Interject Add-in Ribbon is Gone", "Error: Cannot Connect or Communicate With Interject Platform", "Error: Login Page Not Showing (ver 2.5+)", "Error: File Not Uploading Correctly to Report Library", "Error: Report Showing Incorrect Data or Data Missing"]
links: ["https://portal.gointerject.com/download-interject.html", "/wDeveloper/TLS.html", "/wDeveloper/Enterprise-Login-Setup.html#ip-whitelisting", "https://support.microsoft.com/en-us/topic/fix-problems-that-block-programs-from-being-installed-or-removed-cca7d1b6-65a9-3d98-426b-e9f927e1eb4d", "/wTroubleshoot/CorruptedInstallation.html", "/wTroubleshoot/Addin-Missing.html", "/wDeveloper/Enterprise-Login-Setup.html#ip-whitelisting", "/wTroubleshoot/WebView2.html", "/wIndex/Diagnostics-SpecialFeatures.html#webview2browser-login", "/wDeveloper/Enterprise-Login-Setup.html#ip-whitelisting", "https://live-interject-authapi.azurewebsites.net/", "https://live-interject-authapi.azurewebsites.net/.well-known/openid-configuration", "https://live-interject-authapi.azurewebsites.net/", "/wTroubleshoot/Cloud-File.html#solution-saving-to-local-drive", "/wTroubleshoot/Cloud-File.html#solution-uploading-as-a-website-link", "/wFunctions/Excel-Function-Index.html", "https://portal.gointerject.com/download-interject.html#additionalInstallers"]
image_dir: ""
images: []
description: This is a troubleshooting guide for the Interject Add-in. This resource is designed to help you navigate and resolve a variety of common issues you might encounter while using the Interject Add-in.
---
* * *

## Overview

This is a troubleshooting guide for the Interject Add-in. This resource is designed to help you navigate and resolve a variety of common issues you might encounter while using the Interject Add-in. 

### Error: Add-in Not Completely Loaded

- <span style="color: red;">ISSUE:</span> Difference in bitness between Excel\Office and Interject
    
    <span style="color: green;">SOLUTION:</span> Ensure Excel\Office and Interject are operating on the same bit

- <span style="color: red;">ISSUE:</span> Other Excel Add-ins may be causing issues with the Interject XLL\COM Add-in

    <span style="color: green;">SOLUTION:</span> Restart Interject Add-in, upgrade Add-ins, deactivate conflicting Add-ins

- <span style="color: red;">ISSUE:</span> Excel running in background locked up

    <span style="color: green;">SOLUTION:</span> Restart Microsoft Excel

### Error: Incompatible FIPS

_"This implementation is not part of the Windows Platform FIPS validated cryptographic algorithms"_

- <span style="color: red;">ISSUE:</span> Your windows machine is configured to use FIPS 140-2 (or higher) encryption

    <span style="color: green;">SOLUTION:</span> Install Interject 2.5 or greater to use 140-2 compatible encryption methods

### Error: Interject Web API Offline

_"One or more of the Interject web apis are offline or could not be reached. The app can continue to function while offline, for a limited amount of time, with limited functionality"_

- <span style="color: red;">ISSUE:</span> Interject TLS does not meet the system requirements (<2.5 uses TLS 1.0, >=2.4 uses 1.2)

    <span style="color: green;">SOLUTION:</span> [Upgrade Interject](https://portal.gointerject.com/download-interject.html)

    <span style="color: green;">SOLUTION:</span> Override TLS protocol with [System settings](/wDeveloper/TLS.html)

- <span style="color: red;">ISSUE:</span> The network may have a firewall policy blocking requests to Interject cloud services

    <span style="color: green;">SOLUTION:</span> Review the URL's that must be [whitelisted](/wDeveloper/Enterprise-Login-Setup.html#ip-whitelisting) for Interject to work

### Error: Can't Install or Uninstall Interject

- <span style="color: red;">ISSUE:</span> A corrupted installation prevents reinstallation or uninstallation

    <span style="color: green;">SOLUTION:</span> Use the [Microsoft Troubleshooter](https://support.microsoft.com/en-us/topic/fix-problems-that-block-programs-from-being-installed-or-removed-cca7d1b6-65a9-3d98-426b-e9f927e1eb4d){:target="_blank"}{:rel="noopener noreferrer"} to [manual uninstall](/wTroubleshoot/CorruptedInstallation.html) Interject

### Error: Interject Add-in Ribbon is Gone

- <span style="color: red;">ISSUE:</span> Windows can have loading issues with XLL\COM Add-ins sometimes

    <span style="color: green;">SOLUTION:</span> Use the Interject Addin manager to [reset the Add-in](/wTroubleshoot/Addin-Missing.html)

### Error: Cannot Connect or Communicate With Interject Platform

- <span style="color: red;">ISSUE:</span> Proxy network is blocking outgoing traffic

    <span style="color: green;">SOLUTION:</span> [Whitelist](/wDeveloper/Enterprise-Login-Setup.html#ip-whitelisting) our auth API URL

### Error: Login Page Not Showing (ver 2.5+)

- <span style="color: red;">ISSUE:</span> Webview2 is not installed (installed by default normally but sometimes it is missing in rare cases)

    <span style="color: green;">SOLUTION:</span> Manually install [Webview2](/wTroubleshoot/WebView2.html)

- <span style="color: red;">ISSUE:</span> VDI software (e.g. Citrix) is on an old version that does not support Webview2

    <span style="color: green;">SOLUTION:</span> Use the [alternative login](/wIndex/Diagnostics-SpecialFeatures.html#webview2browser-login) form setting in 2.5.2+

- <span style="color: red;">ISSUE:</span> Firewall does not allow access to unapproved external services

    <span style="color: green;">SOLUTION:</span> [Whitelist](/wDeveloper/Enterprise-Login-Setup.html#ip-whitelisting) our auth API URL

- <span style="color: red;">ISSUE:</span> The firewall does not register the Interject auth API domain as secure because the SSL Certificate is being assigned to the domain from a proxy.

    <span style="color: blue;">TEST:</span> If you see an error when you navigate to (https://live-interject-authapi.azurewebsites.net/).

    <span style="color: blue;">TEST:</span> Open (https://live-interject-authapi.azurewebsites.net/.well-known/openid-configuration) in the browser. View and verify the SSL certificate details: "Issued to = *.azurewebsites.net" and "Issued By = Microsoft Azure RSA TLS Issuing CA 08". If you see something else, the network is passing traffic to this domain through a proxy and overriding the SSL.

    <span style="color: green;">SOLUTION:</span> Review your firewall and networking configuration to ensure (https://live-interject-authapi.azurewebsites.net/) is not blocked.

    <span style="color: green;">SOLUTION:</span> Review your firewall and networking configuration to ensure your proxy is correctly handling the SSL certificate passthroughs for the Interject auth API domain.

<blockquote class="highlight_note" style="margin-left: 40px;">
<b>Note:</b> As of version 2.5.3.5, the Interject Add-in uses the URL `auth.gointerject.com`.
</blockquote>
<br>

### Error: File Not Uploading Correctly to Report Library

- <span style="color: red;">ISSUE:</span> Cloud files or files on a shared network may not upload to Report Library correctly.

    <span style="color: green;">SOLUTION:</span> Save file to [local drive](/wTroubleshoot/Cloud-File.html#solution-saving-to-local-drive) before uploading.

    <span style="color: green;">SOLUTION:</span> Save cloud file as a [website link](/wTroubleshoot/Cloud-File.html#solution-uploading-as-a-website-link).

### Error: Report Showing Incorrect Data or Data Missing

- <span style="color: red;">ISSUE:</span> Report formulas not set up correctly.

    <span style="color: green;">SOLUTION:</span> Double check your formula is set up correctly using our [doc pages](/wFunctions/Excel-Function-Index.html).

- <span style="color: red;">ISSUE:</span> Data API not set up correctly.

    <span style="color: green;">SOLUTION:</span> Ensure the data API endpoint is configured correctly. Our API repos have docs and examples of how to access your data.

- <span style="color: red;">ISSUE:</span> Wrong Interject version. Each versions has different features and functionality. Upgrading may help and in some cases it may help to downgrade your version to isolate the issue.

    <span style="color: green;">SOLUTION:</span> Upgrade/Downgrade your [Interject version](https://portal.gointerject.com/download-interject.html#additionalInstallers).

### Error: Installation Fails Due to Missing Cached Installer or Residual Registry Keys

- <span style="color: red;">ISSUE:</span> Installation of the Interject Excel Add-in fails with error about missing cached installer package (e.g. .msi file missing), or the system incorrectly detects an existing installation blocking update.

- <span style="color: green;">SOLUTION:</span> [Manually remove](/wTroubleshoot/RegistryKeyRemoval.html) leftover registry keys related to Interject before uninstalling Interject.
