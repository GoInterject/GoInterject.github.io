---
title: The Interject Website Portal
layout: custom
keywords: [website portal, account, connection strings]
headings: ["Overview", "Logging In to the Interject Website Portal", "Data Connections", "Data Portals", "User Profile"]
links: ["/wPortal/Logging-In-to-Website-Portal.html", "/wPortal/Data-Connections.html", "/wPortal/Data-Portals.html", "https://www.connectionstrings.com/", "/wPortal/User-Profile.html"]
description: The Interject website portal is a central place to manage Interject client settings and user profiles.
---
* * *

## Overview

For all other data sources, a custom website API can be created to connect the data to Interject. This is very similar to how a website application accesses its data layer. Using an API you can connect to PostgreSQL and noSQL databases like MongoDB. You can also use an API to connect to other cloud data APIs such as provided by SalesForce, Intacct, Netsuite, Quicken and many other cloud software services.

![](/images/InterjectWebsitePortal/PortalSite.png)
<br>

### [Logging In to the Interject Website Portal](/wPortal/Logging-In-to-Website-Portal.html)

This section details how to log in to the Interject website portal to get access to Interject features.

### [Data Connections](/wPortal/Data-Connections.html)

A Connection is used with Data Portals so Interject can connect to certain stored procedures within a database or to a custom website API. A single connection can be used by many Data Portals.

### [Data Portals](/wPortal/Data-Portals.html)

In this section you will quickly set up a connection to SQL Server and test it using the security context of the user from their Excel session.

A Connection can be set up to connect directly to a database using a OLEDB or a .Net Adapter connection string for MS SQL Server or using a ODBC connection string to connect to Oracle, MySQL, or others that support stored procedures. For other databases, including noSQL databases, a customer website API can be used to connect the datasource to Interject, which is covered in a later section.

The following lists are examples of connection strings for SQL Server:

 * Example .Net Adapter connection string:

 > Server=myServerAddress;
 > Database=myDataBase;
 > Trusted_Connection=True;

 * Example OLEDB connection string:

 > Provider=SQLNCLI11;
 > Server=myServerAddress;
 > Database=myDataBase;
 > Trusted_Connection=yes;

 * Example of an ODBC connection string:

 > Driver={SQL Server Native Client 11.0};
 > Server=myServerAddress;
 > Database=myDataBase;
 > Trusted_Connection=yes;

See [https://www.connectionstrings.com/](https://www.connectionstrings.com/) for additional information on connection strings.

### [User Profile](/wPortal/User-Profile.html)

Managing Users and User Profiles is another commonly used area of the Interject Website Portal. The role of Client Admin, has the ability to open the profile of a user by clicking on their name. The menu to the left includes the link **User Profile** as a shortcut to get to your own user profile.


