---
title: Troubleshooting Guide
filename: "TroubleshootingSolutions.md"
layout: custom
keywords: []
headings: ["Overview"]
links: []
image_dir: ""
images: [
    {file: "", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}
]
description: This is a troubleshooting guide for the Interject Add-in. This resource is designed to help you navigate and resolve a variety of common issues you might encounter while using the Add-in.
---
* * *

## Overview

This is a troubleshooting guide for the Interject Add-in. This resource is designed to help you navigate and resolve a variety of common issues you might encounter while using the Add-in. 

### Error: Add-in Not Completely Loaded

- <span style="color: red;">ISSUE:</span> Difference in bitness between Excel\Office and Interject
    
    <span style="color: green;">SOLUTION:</span> Ensure Excel\Office and Interject are operating on the same bit

- <span style="color: red;">ISSUE:</span> Other Excel Add-ins may be causing issues with the Interject XLL\COM Add-in

    <span style="color: green;">SOLUTION:</span> Restart Interject Add-in, upgrade Add-ins, deactivate conflicting Add-ins

### Error: Incompatible FIPS 

_"This implementation is not part of the Windows Platform FIPS validated cryptographic algorithms"_

- <span style="color: red;">ISSUE:</span> Your windows machine is configured to use FIPS 140-2 (or higher) encryption

    <span style="color: green;">SOLUTION:</span> Install Interject 2.5 or greater to use 140-2 compatible encryption methods

### Error: Interject Web API Offline

_"One or more of the Interject web apis are offline or could not be reached. The app can continue to function while offline, for a limited amount of time, with limited functionality"_

- <span style="color: red;">ISSUE:</span> Interject TLS does not meet the system requirements (<2.5 uses TLS 1.0, >=2.4 uses 1.2)

    <span style="color: green;">SOLUTION:</span> [Upgrade Interject](https://portal.gointerject.com/download-interject.html)

    <span style="color: green;">SOLUTION:</span> Override TLS protocol with [System settings](/wAbout/TLS.html)

- <span style="color: red;">ISSUE:</span> The network may have a firewall policy blocking requests to Interject cloud services

    <span style="color: green;">SOLUTION:</span> Review the URL's that must be [whitelisted](/wAbout/Enterprise-Login-Setup.html#ip-whitelisting) for Interject to work

### Error: Interject Add-in Ribbon is Gone

- <span style="color: red;">ISSUE:</span> Windows can have loading issues with XLL\COM Add-ins sometimes

    <span style="color: green;">SOLUTION:</span> Use the Interject Addin manager to [reset the Add-in](/wTroubleshoot/Addin-Missing.html)


### Error: Cannot Connect or Communicate With Interject Platform

- <span style="color: red;">ISSUE:</span> Proxy network is blocking outgoing traffic

    <span style="color: green;">SOLUTION:</span> [Whitelist](/wAbout/Enterprise-Login-Setup.html#ip-whitelisting) our auth API URL

### Error: Login Page Not Showing (ver 2.5+)

- <span style="color: red;">ISSUE:</span> Webview2 is not installed (installed by default normally but sometimes it is missing in rare cases)

    <span style="color: green;">SOLUTION:</span> Manually install [Webview2](/wTroubleshoot/WebView2.html)

- <span style="color: red;">ISSUE:</span> VDI software (e.g. Citrix) is on an old version that does not support Webview2

    <span style="color: green;">SOLUTION:</span> Use the alternative login form setting in 2.5.2+

- <span style="color: red;">ISSUE:</span> Firewall does not allow access to unapproved external services

    <span style="color: green;">SOLUTION:</span> [Whitelist](/wAbout/Enterprise-Login-Setup.html#ip-whitelisting) our auth API URL
