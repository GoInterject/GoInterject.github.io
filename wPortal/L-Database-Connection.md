---
title: "Portal: Database Connection"
filename: "L-Database-Connection.md"
layout: custom
keywords: [database connection, setting up, setup]
headings: ["Overview", "Setup for a Data Connection to a Database", "Testing the Connection String From Within Excel"]
links: ["https://portal.gointerject.com", "/wPortal/Logging-In-to-Website-Portal.html", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html"]
image_dir: "Database"
images: [{file: "01", type: "png", site: "Portal", cat: "Home", sub: "", report: "", ribbon: "", config: ""},{file: "02", type: "png", site: "Portal", cat: "Data Connections", sub: "", report: "", ribbon: "", config: ""},{file: "03", type: "png", site: "Portal", cat: "Data Connections", sub: "Details", report: "", ribbon: "", config: ""},{file: "04", type: "png", site: "Portal", cat: "Data Connections", sub: "Details", report: "", ribbon: "", config: ""},{file: "05", type: "png", site: "Portal", cat: "Data Connections", sub: "Details", report: "", ribbon: "", config: ""},{file: "06", type: "png", site: "Addin", cat: "Ribbon", sub: "", report: "", ribbon: "Simple", config: ""},{file: "07", type: "png", site: "Addin", cat: "Ribbon", sub: "System", report: "", ribbon: "Advanced", config: ""},{file: "08", type: "png", site: "Addin", cat: "Check Connection", sub: "", report: "", ribbon: "Advanced", config: ""},{file: "09", type: "png", site: "Addin", cat: "Check Connection", sub: "", report: "", ribbon: "Advanced", config: ""}]
description: This example shows how to connect to a database using a pre-existing data portal.
---
* * *

## Overview

A Data Connection can be set up to connect directly to a database using a OLEDB or a .Net Adapter connection string for MS SQL Server or using a ODBC connection string to connect to Oracle, MySQL, or others that support stored procedures.

### Setup for a Data Connection to a Database

**Step 1:** Start off by navigating to [https://portal.gointerject.com](https://portal.gointerject.com). Once [logged in](/wPortal/Logging-In-to-Website-Portal.html) you can setup a data connection by clicking on the **Data Connections** icon.

![](/images/Database/01.png)
<br>

**Step 2:** In the Data Connections page select the **New Connection** button in the top right-hand corner.

![](/images/Database/02.png)
<br>

**Step 3:** In the Connection Type field, make sure **Database** is selected.

![](/images/Database/03.png)
<br>

**Step 4:** The Connection Details page will contain the following information for the new connection.

 * **Name:** A unique friendly name used when connecting a Data Portal to the Data Connection
 * **Description (optional):** description of what the connection string is connecting to
 * **Connection String:** used by Interject to connect to the specified server & database

![](/images/Database/04.png)
<br>

**Step 5:** After adding the required information, click on the Save button to create the new data connection.

![](/images/Database/05.png)
<br>

The Database Data Connection is now ready to be used in a Data Portal.

### Testing the Connection String From Within Excel

Before setting up a Data Connection to a Database, you can verify that the connection can be established within Excel.

**Step 1:** With Excel open, go to the [Interject Ribbon](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html) menu and click **Advanced Menu** (Skip this step if already at Advanced menu).

![](/images/Database/06.png)
<br>

**Step 2:** Click **System** drop-down and select **Check Connection**.

![](/images/Database/07.png)
<br>

**Step 3:** Paste the database connection string you will be using to configure the Data Connection into the text-box.

![](/images/Database/08.png)
<br>

When the connection functions it will display a message such as the one below.

![](/images/Database/09.png)
<br>
