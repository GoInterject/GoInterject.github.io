---
title: "Portal: API Connection"
layout: custom
keywords: [api, connection, setting up, create, example]
description: The Interject add-in is a client application that can send a request to a POST HTTP(s) REST API. As long as the response is properly structured, Interject will display the data in Excel. Interject is not a tool that communicates with all APIs, but by allowing users to build custom APIs, it can be connected to any data-source including other APIs that are not natively supported. We provide a customizable API, which can serve as the starting point for this translational API. 
---
* * *

##  **Overview**

The Interject add-in is a client application that can send a request to a POST HTTP(s) REST API. As long as the response is properly structured, Interject will display the data in Excel. Interject is not a tool that communicates with all APIs, but by allowing users to build custom APIs, it can be connected to any data-source including other APIs that are not natively supported. We provide a customizable API, which can serve as the starting point for this translational API. 

  


Another reason to use an API, instead of connecting directly to a data source, is to provide another layer of security. Since most data-sources are protected by a firewall, users outside a network, and/or without the correct credentials, are not able to access the data. An API can be that gatekeeper. Interject users can be validated in the pass-through API whether or not they are valid Interject users, and custom validation can be added to including row level security. 

In this example, you will set up a simple connection to an example API. Detailed documentation on using a custom data API’s is currently under development. Please contact us for more information if needed. 

  
**Step 1:** Navigate to [ https://portal.gointerject.com ](https://portal.gointerject.com) and [ login ](/wPortal/Logging-In-to-Website-Portal.html) to Interject.  To set up a data connection click on **Data Connections** in the menu on the left.

![](/images/L-Portal-API/01.png)

<br> 


**Step 2:** In the Data Connections page, select the **New Connection** button in the top right corner. 

![](/images/L-Portal-API/02.png)

<br> 


**Step 3:** In the Connection Type field, make sure **Web Api** is selected. 

![](/images/L-Portal-API/03.png)

<br> 


**Step 4:** The Connection Details page will contain the following information for the new connection. 

  * **Name:** A unique friendly name used when connecting a Data Portal to the Data Connection. 
  * **Description:** Description of the API connection 
  * **Api Root Url:** The root URL of the API you are connecting to, for example [ https://api.myDataApi.com ]
  * **Api Connection String Name (optional):** The name of the connection string within the configuration of your custom API. In many cases, an API may be hard-coded to use a specific database, so this setting is not needed. But you can build an API to use a different connection string, as indicated by this setting. If the developer uses this attribute, an API's use can be more flexible. Two options can be used here other than leaving it blank: 
    * In a web config, you can have a connection string with a name which will be used as the connection string name 
    * It is also possible to put the integrated security connection string here. This would be used to connect to data sources with extra security. 
  * **Authentication Type:** Each API may use a different type of authentication. 10 is the default for using the Interject authentication. Contact support for information about other types of Authentication. 



![](/images/L-Portal-API/04.png)

<br> 

**Step 5:** After adding the required information, click on the Save button to create the new data connection. 

![](/images/L-Portal-API/05.png)

<br>

The API Data Connection is now ready to be used in a Data Portal. 

  

