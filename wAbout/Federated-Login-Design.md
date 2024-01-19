---
title: Federated Login Design
filename: "Federated-Login-Design.md"
layout: custom
keywords: [login, credentials, accounts, Enterprise, setup]
headings: ["Overview", "Enterprise Login Code", "Web Pages with Webview2", "Tokens and Refresh Cycle", "How Tokens are Stored", "Legacy Interject Logins"]
links: ["https://duendesoftware.com/products/identityserver", "/wAbout/logging-in-enterprise.html", "https://learn.microsoft.com/en-us/microsoft-edge/webview2/", "https://openid.net/developers/how-connect-works/", "https://auth0.com/intro-to-iam/what-is-oauth-2", "https://learn.microsoft.com/en-us/dotnet/standard/security/how-to-use-data-protection", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#advanced-menu-items"]
image_dir: "Federated-Login-Design"
description: Interject uses a Duende (previously Identity Server 4) API to handle authentication for federated user logins.
---
* * *

## Overview

Interject uses a [Duende](https://duendesoftware.com/products/identityserver){:target="_blank"}{:rel="noopener noreferrer"} (previously Identity Server 4) API to handle authentication for federated user logins. The following diagram shows the relationship between the Interject Excel Add-in and the Auth API when users login to a federated identity system.

![](/images/Federated-Login-Design/FederatedLoginFlowchart.png)
<br>

### Enterprise Login Code

The Enterprise Login Code is a text string given to each Interject company that is used to navigate a user from the general login page to the federation's login page. The login code can be set to any text string that is not currently in use by another Interject company.

![](/images/Federated-Login-Design/EnterpriseLoginFlowchart.png)
<br>

See [Logging In/Out: Enterprise User](/wAbout/logging-in-enterprise.html) for a walkthrough on how to login with your Enterprise token.

### Web Pages with Webview2

In order for the Interject Addin to show the login page and redirect properly to federated login pages, a web browser environment is needed. Webview2 is a framework for embedding web technologies like HTML and JavaScript in native windows apps of various kinds. 

To learn more about Webview2, refer to this [documentation](https://learn.microsoft.com/en-us/microsoft-edge/webview2/).

### Tokens and Refresh Cycle

[Open ID Connect](https://openid.net/developers/how-connect-works/){:target="_blank"}{:rel="noopener noreferrer"} (OIDC) is built on top of [OAuth2](https://auth0.com/intro-to-iam/what-is-oauth-2){:target="_blank"}{:rel="noopener noreferrer"} which uses an access token for authorized requests and a refresh token to get new access tokens when they expire. Both of these tokens expire after the following durations:

* Refresh token - expires every 30 days (this requires the user to login again)
* Access token - expires every hour 

### How Tokens are Stored

Login access and refresh tokens are stored in a .dat file using [Microsoft's Windows data protection API](https://learn.microsoft.com/en-us/dotnet/standard/security/how-to-use-data-protection). It is located in the user's AppData folder for Interject/Settings.

![](/images/Federated-Login-Design/FileExplorer.png)
<br>

You can open this folder easily by clicking on **Diagnostics** on the [Advanced Interject ribbon](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#advanced-menu-items), select **Open User Folders** and then click **Execute Selected Action**.

![](/images/Federated-Login-Design/DiagnosticsRibbon.png)
<br>

![](/images/Federated-Login-Design/Diagnostics.png)
<br>

### Legacy Interject Logins

Users can be configured to continue using their existing Interject basic Auth accounts while also having access to federated logins. The Interject Login Manager will show all your logins:

![](/images/Federated-Login-Design/DualLogins.png)
<br>
