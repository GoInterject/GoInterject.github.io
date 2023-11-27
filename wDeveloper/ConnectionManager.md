---
title: Connection Manager
layout: custom
keywords: [id providers, identity providers, login, tokens, federated, enterprise]
description: The Interject Connection Manager displays the current Web API connections associated with a company and that use a federated login.
---
* * *

## Overview

The Interject Connection Manager displays the current Web API connections associated with a company and that use a [federated login](/wAbout/Federated-Login-Design.html). When a company is [set up](/wAbout/Enterprise-Login-Setup.html) with a federated login, an Enterprise Login Code will be set up in order to direct the user to the federation's login page. This code represents a connection to the ID provider used for the federated login. All codes set up for a company will be displayed in the Connection Manager.

![](/images/ConnectionManager/ConnectionsWindow.png)
<br>

<blockquote class=highlight_note>
<b>Note:</b> Non-federated logins using legacy Interject credentials will not be displayed in the Connection Manager.
</blockquote>
<br>

The Connection Manger is accessed from the Interject ribbon.

![](/images/ConnectionManager/Connections.png)
<br>

### Logging In and Out of a Connection

The Connection Manager displays all Enterprise Login Codes and their connection status. All connections will automatically be connected when connected to Interject with a federated login. You can logout of a particular connection by clicking the **Log Out** link for that connection.

![](/images/ConnectionManager/Auth0Logout.png)
<br>

You can connect by clicking the linked name of the connection (you may be directed to your federated login screen if your credentials need to be entered).

![](/images/ConnectionManager/Auth0Login.png)
<br>
