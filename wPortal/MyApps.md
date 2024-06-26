---
title: My Apps
filename: "MyApps.md"
layout: custom
keywords: [redirect, override, offerings, subscriptions, portals, connections, links]
headings: ["Overview", "Expiration", "App Offering", "Connection Redirection"]
links: ["mailto:info@gointerject.com"]
image_dir: "MyApps"
images: [
	{file: "MyAppsPage", type: "png", site: "Portal", cat: "My Apps", sub: "", report: "", ribbon: "", config: ""},
	{file: "Expiration", type: "png", site: "Portal", cat: "My Apps", sub: "", report: "", ribbon: "", config: ""},
	{file: "InterjectDemoApp", type: "png", site: "Portal", cat: "My Apps", report: "", ribbon: "", config: ""},
	{file: "ReportLibrarySubscriptions", type: "png", site: "Addin", cat: "Report Library", sub: "", report: "", ribbon: "", config: ""},
	{file: "ConnectionRedirect", type: "png", site: "Portal", cat: "My Apps", sub: "Connection Redirect", report: "", ribbon: "", config: ""},
	{file: "RedirectionDisplayed", type: "png", site: "Portal", cat: "My Apps", sub: "Connection Redirect", report: "", ribbon: "", config: ""},
	{file: "DeleteRedirection", type: "png", site: "Portal", cat: "My Apps", sub: "Connection Redirect", report: "", ribbon: "", config: ""}
]
description: The My Apps page on the Portal site displays all the apps you are currently subscribed to. 
An app (sometimes called "Offering") is a set of reporting solutions that include Report Library links, data portals, and data connections. They are published by a publisher company and made available to subscribers. Currently, Interject handles all published apps so first contact us to get a published app set up for your company.
---
* * *

## Overview

The My Apps page on the Portal site displays all the apps you are currently subscribed to. 
An app (sometimes called "Offering") is a set of reporting solutions that include Report Library links, data portals, and data connections. They are published by a publisher company and made available to subscribers. Currently, Interject handles all published apps so first contact us to get a published app set up for your company.

![](/images/MyApps/MyAppsPage.png)
<br>

### Expiration

Depending on your subscription, there may be an expiration date for the App. [Contact us](mailto:info@gointerject.com) if it needs to be extended.

![](/images/MyApps/Expiration.png)
<br>

### App Offering

Clicking on an app in the My Apps page will show you a list of data portals along with their connections that are included in the App. Some connections can be configured to be [overridden](#connection-redirection) (i.e. redirected). If it is currently set up to be redirected, the redirect is also displayed.

![](/images/MyApps/InterjectDemoApp.png)
<br>

Once you are subscribed to an app, they will appear in the Report Library and all the associated links will be accessible:

![](/images/MyApps/ReportLibrarySubscriptions.png)
<br>

### Connection Redirection

ClientAdmins are allowed to redirect a data connection. A Connection Redirect is used to override a default connection with one that is catered to your own company. This is common with some App subscriptions so that it can access custom data for your company.

To override a connection, select the data connection you want to redirect in the "Default Offering Connection" and change the redirect in the "Your Company Connection" list and click **Save**:

![](/images/MyApps/ConnectionRedirect.png)
<br>

The redirection is displayed on the bottom and now appears for each data portal that uses the default connection. Any data portal that uses the default data connection will now be redirected and use the redirected connection.

![](/images/MyApps/RedirectionDisplayed.png)
<br>

To delete an override, simply hover the cursor over the garbage **<font size="+1">&#x1F5D1;</font>** icon and click "Delete Redirect":

![](/images/MyApps/DeleteRedirection.png)
<br>
