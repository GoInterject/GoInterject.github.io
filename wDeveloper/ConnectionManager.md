---
title: Connection Manager
filename: "ConnectionManager.md"
layout: custom
keywords: [id providers, identity providers, login, tokens, federated, enterprise]
headings: ["Overview", "Logging In and Out of a Connection"]
links: ["/wAbout/Federated-Login-Design.html", "/wAbout/Enterprise-Login-Setup.html", "/wAbout/Logging-In-Enterprise.html#clearing-login-cookies"]
image_dir: "ConnectionManager"
description: The Interject Connection Manager displays the current Web API connections associated with a company and that use a federated login.
---
* * *

## Overview

The Interject Connection Manager displays all Web API connections that are secured with a [federated login](/wAbout/Federated-Login-Design.html). When a company is [set up](/wAbout/Enterprise-Login-Setup.html) with a federated login, an Enterprise Login Code will be associated with that login in order to direct the user to their federation's login page. Once logged in, the access token issued by that federated identity provider will be used when making calls to that connection.

![](/images/ConnectionManager/ConnectionsWindow.png)
<br>

<blockquote class=highlight_note>
<b>Note:</b> Connections using Interject credentials will not be displayed in the Connection Manager as their access token is managed separate from federated logins.
</blockquote>
<br>

The Connection Manger is accessed from the Interject ribbon.

![](/images/ConnectionManager/Connections.png)
<br>

### Logging In and Out of a Connection

The Connection Manager displays the status for all federated login Web API connections. A connection is automatically connected when the associated federated login is used to log into Interject. You can logout of a particular connection by clicking the Log Out link for that connection. This will not log you out of Interject, however it will disable access to that connection.

![](/images/ConnectionManager/Auth0Logout.png)
<br>

You can connect by clicking the linked name of the connection. You will be directed to your federated login screen if your credentials need to be entered. Some federated identity providers offer a 'remember me' type feature that will automatically log you back in using browser cookies. For enhanced security, Interject provides a method to [Clear External Login Cookies](/wAbout/Logging-In-Enterprise.html#clearing-login-cookies).

![](/images/ConnectionManager/Auth0Login.png)
<br>
