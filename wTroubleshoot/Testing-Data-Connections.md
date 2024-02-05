---
title: Testing Data Connections
filename: "Testing-Data-Connections.md"
layout: custom
keywords: [report, test, data, connection, user support]
headings: ["Overview"]
links: []
image_dir: "TestingDataConnections"
images: [{file: "25", type: "jpg", site: "Addin", cat: "Report", sub: "", report: "", ribbon: "Simple", config: "Yes"},{file: "26", type: "jpg", site: "Addin", cat: "Ribbon", sub: "System", report: "Customer Aging Summary", ribbon: "Advanced", config: "Yes"},{file: "27", type: "jpg", site: "Addin", cat: "Check Connection", sub: "", report: "Customer Aging Summary", ribbon: "", config: "Yes"},{file: "28", type: "jpg", site: "Addin", cat: "Check Connection", sub: "", report: "Customer Aging Summary", ribbon: "", config: "Yes"},{file: "CheckConnectionError", type: "png", site: "Addin", cat: "Check Connection", sub: "", report: "", ribbon: "", config: ""}]
description: Before setting up a Data Connection to a Database, you can verify that the connection can be established within Excel by accessing the Check Connection window.
---
* * *

## Overview

Before setting up a Data Connection to a Database, you can verify that the connection can be established within Excel by accessing the **Check Connection** window.

**Step 1:** With Excel open, go to the Interject Ribbon menu and click **Advanced Menu** (Skip this step if Advanced menu is already showing):

![](/images/TestingDataConnections/25.jpg)
<br>

**Step 2:** Click **System** drop-down, and select **Check Connection**:

![](/images/TestingDataConnections/26.jpg)
<br>

**Step 3:** In the text-box, paste the database connection string you will be using to configure the Data Connection:

![](/images/TestingDataConnections/27.jpg)
<br>

When the connection functions properly, a message will be displayed, such as the one below:

![](/images/TestingDataConnections/28.jpg)
<br>

If there are errors, you will see a description of the error:

![](/images/TestingDataConnections/CheckConnectionError.png)
<br>

