---
title: Published Apps
filename: "PublishedApps.md"
layout: custom
keywords: [offerings, subscribers, publish, data portals, apps]
headings: ["Overview", "App Details", "Data Portals", "Portals in App", "Portals in App Reports", "Client Data Portals", "Download Report Information"]
links: ["/wPortal/MyApps.html#connection-redirection"]
image_dir: "PublishedApps"
images: [
	{file: "PublishedAppsPage", type: "png", site: "Portal", cat: "Published Apps", sub: "", report: "", ribbon: "", config: ""},
	{file: "AppDetails", type: "png", site: "Portal", cat: "Published Apps", sub: "App Details", report: "", ribbon: "", config: ""},
	{file: "DataPortalsInApp", type: "png", site: "Portal", cat: "Published Apps", sub: "App Details", report: "", ribbon: "", config: ""},
	{file: "EditDataPortal", type: "png", site: "Portal", cat: "Published Apps", sub: "App Details", report: "", ribbon: "", config: ""},
	{file: "DataPortalsInAppReports", type: "png", site: "Portal", cat: "Published Apps", sub: "App Details", report: "", ribbon: "", config: ""},
	{file: "AddDataPortalToApp", type: "png", site: "Portal", cat: "Published Apps", sub: "App Details", report: "", ribbon: "", config: ""},
	{file: "DownloadReportInformation", type: "png", site: "Portal", cat: "Published Apps", sub: "App Details", report: "", ribbon: "", config: ""}
]
description: The "Published Apps" page on the Portal site displays all of your company's published apps. A published app is a collection of data portals, connections and Report Library links. Published apps are configured by Interject for a company to allow them to distribute the app to subscribers.
---
* * *

## Overview

The "Published Apps" page on the Portal site displays all of your company's published apps. A published app is a collection of data portals, connections and Report Library links. Published apps are configured by Interject for a company to allow them to distribute the app to subscribers.

![](/images/PublishedApps/PublishedAppsPage.png)
<br>

The Published App page displays the app, how many data portals are included in the app as well as how many are subscribed to the app. 

### App Details

Clicking on the app in the list will open the App Details page.

- **Name:** The app name
- **Description:** App description
- **Data Portal:** The number of data portals included in this app
- **Status:** Active or trial
- **IsPublic:** This field is not functional
- **Register Date:** Date this app was registered
- **Sort Order:** A number that will sort the Report Library Folder in relation to other folders
- **Renew Date:** The app's expiration date
- **IsPremium:** This field is not functional
- **App Report Folder:** This is the name of the folder that will appear in the Report Library

![](/images/PublishedApps/AppDetails.png)
<br>

### Data Portals

#### Portals in App

This section allows management of what data portals are available in the published app. The table on the left displays all data portals that are currently made available to subscribers of the app. 

![](/images/PublishedApps/DataPortalsInApp.png)
<br>

When you click **Edit**, you can choose to make the data portal [overridable](/wPortal/MyApps.html#connection-redirection). Clicking on the garbage **<font size="+1">&#x1F5D1;</font>** icon will remove the data portal from the app. (Be sure to click **Save**.)

![](/images/PublishedApps/EditDataPortal.png)
<br>

#### Portals in App Reports

The table on the right displays any data portal that is contained in the report library for this app but is not included in the list of data portals. As such, a subscriber who attempts to use this data portal in the report will not be able to access any data with this data portal.

![](/images/PublishedApps/DataPortalsInAppReports.png)
<br>

#### Client Data Portals

The Client Data Portals list on the bottom lists all data portals in the company that are not currently in the list of data portals for the app. You can add these portals to the app by selecting the portal and clicking **Add Portal To App**.

![](/images/PublishedApps/AddDataPortalToApp.png)
<br>

#### Download Report Information

The **Download Report Information** link will download a csv file of all the links contained in the app.

![](/images/PublishedApps/DownloadReportInformation.png)
<br>

![](/images/PublishedApps/DownloadReportInformationCSV.png)
<br>
