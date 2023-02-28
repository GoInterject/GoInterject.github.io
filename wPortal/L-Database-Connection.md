---
title: "Portal: Database Connection"
layout: custom
keywords: [database connection, example, walkthrough]
description: This example shows how to connect to a database using a pre-existing dataportal.
---

###  Data Connection for a Database 

**Step 1:** Start off by navigating to [ https://portal.gointerject.com ](https://portal.gointerject.com). Once [ logged in ](/wPortal/Logging-In-to-Website-Portal.html) you can setup a data connection by clicking on the **Data Connections** icon. 

![](/images/Database/01.png)

**Step 2:** In the Data Connections page select the **New Connection** button in the top right-hand corner. 

![](/images/Database/02.png)

**Step 3:** In the Connection Type field, make sure **Database** is selected. 

![](/images/Database/03.png)

**Step 4:** The Connection Details page will contain the following information for the new connection. 

  * **Name:** A unique friendly name used when connecting a Data Portal to the Data Connection 
  * **Description (optional):** description of what the connection string is connecting to 
  * **Connection String:** used by Interject to connect to the specified server  & database 

![](/images/Database/04.png)

**Step 5:** After adding the required information, click on the Save button to create the new data connection 

![](/images/Database/05.png)

The Database Data Connection is now ready to be used in a Data Portal. 

###  Testing Connection String from within Excel 

Before setting up a Data Connection to a Database, you can verify that the connection can be established within Excel. 

**Step 1:** With Excel open, go to the [ Interject Ribbon ](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html) menu and click **Advanced Menu** (Skip this step if already at Advanced menu) 

![](/images/Database/06.png)

**Step 2:** Click **System** drop-down and select **Check Connection**

![](/images/Database/07.png)

**Step 3:** Paste the database connection string you will be using to configure the Data Connection into the text-box. 

![](/images/Database/08.png)

When the connection functions it will display a message such as the one below. 

![](/images/Database/09.png)

<br>
