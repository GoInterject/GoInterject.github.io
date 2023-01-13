---
layout: custom
title:  ".NET API Setup"
date:   2018-10-12 9:03:02 -0700
categories: API Developer
---


##  **Overview**

In this walkthrough we will setup an Interject Data API in C# which can be used to manage dataflow to and from Interject Reports. 


##  **Requirements**

**Minimum Requirements:**
- The machine should be running IIS as a web server
- The machine needs at least .Net framework 4.5.2

**Getting .Net**<br>
The first step is to install the .NET SDK that best fits your system. These downloads can be found on [Microsoft's .NET Downloads](https://dotnet.microsoft.com/download) page.


> **NOTE:** if you intend to use the data api on linux or macOS, it is necessary to [download mono](https://www.mono-project.com/), the cross platform open-source development platform based on the .NET Framework.


##  **Get The Code**
Once .NET is installed then clone or download the `SimpleDataApi` repository:

<!---
{% include codeHeader.html %}


<div class="code-header">
  <button class="copy-code-button">
    Copy
  </button>
</div>
--->

```git
git clone https://github.com/GoInterject/ids-dotnet-api
```

Note: If this repo is private and you need access, please [contact us](mailto:help@gointerject.com). It will be public soon.

## **Setup API**

### **1. Verify Available DNS**

Be sure there is a DNS name available for this API's website. Any standard DNS setting will work, so long as it resolves to the web server that you are using. 

### **2. Define Project Folder**

Choose a folder to hold the API.
The default for Windows is to use a subfolder in "inetpub" but any folder is OK. The API website files should be kept in their own folder, named accordingly.

<img class="img-modal" src="/images/dot-net-api/choose-folder.png" width="50%" onclick="zoom_img(this)" />


### **3. Copy API files**

Copy the API files into this folder. The root of the API file tree has the crucial "web.config" file.

<img class="img-modal" src="/images/dot-net-api/project-api-structure.png" width="45%" onclick="zoom_img(this)" />

- **a )**  It is possible to copy the source code files along with compiled code files. This is optional. 
- **b )**  For public facing sites, it is safer to use the Visual Studio "Deploy" process to package up a site so that peripheral files are removed. Certain files can be distributed by IIS if they exist in the website folder
- **c )**  The files you received may contain a parent folder of "development" files for Visual Studio. However, only the API files should be deployed on the webserver.
- **d )**  The root of the website can be identified by some of the core files that compose the site: 
    - App_Start 
    - Global.asax 
    - Web.config
- **e )** The Web.config file will be updated later.


### **4. Open IIS Manager on the web server.**

IIS (Internet Information Services) is the software which exposes a website to the rest of the network (or internet) 

> **NOTE:** If IIS has never been configured, it may require specific instructions based on the web server's specific operating system<br>
> External links:<br>
> [Windows server 2016](https://www.rootusers.com/how-to-install-iis-in-windows-server-2016/)<br>
> [Windows 10](https://www.betterhostreview.com/turn-on-iis-windows-10.html)

<img class="img-modal" src="/images/dot-net-api/iis-manager.png" width="40%" onclick="zoom_img(this)" />

### **6.  IIS Manager looks like this**

<img class="img-modal" src="/images/dot-net-api/iis-manager-view.png" width="45%" onclick="zoom_img(this)" />


### **7.  Create a new website by Right-Clicking on the "Site" node**

<img class="img-modal" src="/images/dot-net-api/site-add-website.png" width="40%" onclick="zoom_img(this)" />


- **a )**	<u>Site name</u>: seen only by the admin of the web server. Choose a meaningful name to identify this API. Eg. "Interject Data API"

- **b )**  Notice that when Choosing a Site Name, the <u>"Application Pool"</u> will use the new name by default. This is preferred. It is not the best practice to use the "DefaultAppPool" which is seen at first. Instead, each site should have its own app pool with a matching name. The App Pool basically acts like the Windows User for that particular site. Permissions assigned to the AppPool are the applicable permissions for the web site 

- **c )**  <u>Physical path</u>: Navigate to the root folder where the web.config file exists (see step #3) at the start of these instructions.

- **d )**  <u>Connect as</u>...: keep the default setting which is to use the "Application user" which is the same as the AppPool. 

<img class="img-modal" src="/images/dot-net-api/connect-as.png" width="50%" onclick="zoom_img(this)" />

- **e )** <u>Binding Type</u>: The binding can use either HTTP or HTTPS. This document does not describe how to set up an SSL certificate for HTTPS bindings. Any public facing site must use HTTPS. 

- **f )** <u>IP address</u>: This setting can be left as the default for "All Unassigned" a Specific IP address can be used if this web server responds to multiple IP addresses. It is more common to use a specific IP address when dealing with multiple SSL certificates on the same web server. 

- **g )** <u>Port</u> will normally follow the default 80 for Http and 443 for Https, unless a network administrator requires an override.

- **h )** <u>Host name</u>: The Host Name (aka Host Header) Is used to differentiate multiple websites that are hosted on the same web server. This should match the DNS setting that is configured for this API. (see step #1 at the start of this document)

An example of an API used within a company's intranet is here:
<img class="img-modal" src="/images/dot-net-api/api-intranet.png" width="60%" onclick="zoom_img(this)" />


### **8. If these settings need to be changed later. Select the site with IIS manager, and choose the "Bindings" or "Basic Settings" in the right margin**

<img class="img-modal" src="/images/dot-net-api/basic-and-bindings.png" width="70%" onclick="zoom_img(this)" />


### **9. Confirm settings for the App Pool**
The App Pool should have been created when the site was created.
You can see the specific information in the "Application Pools" area of the IIS Manager.

- **a )**	Make sure the AppPool is using .NET v4.0 and an "Integrated" pipeline (these are the defaults)
- **b )**	Make a note of the specific name of the App Pool (in this screenshot its "Interject Data API")

<img class="img-modal" src="/images/dot-net-api/app-pools.png" width="30%" onclick="zoom_img(this)" />

- **c )**	If the site gets frozen, you can restart it by "recycling" the App Pool (Right Click it), which clears out all memory and restarts the site

<img class="img-modal" src="/images/dot-net-api/app-pools-view.png" width="40%" onclick="zoom_img(this)" />


### **10. Set up website permissions using the App Pool. In IIS Manager, Right-Click the API website and choose "Edit Permissions" (this is the same as editing security permissions on the folder itself, within Windows)**

<img class="img-modal" src="/images/dot-net-api/edit-permissions.png" width="40%" onclick="zoom_img(this)" />

- **a )**	Choose the "Security" tab and then the "Edit" button, and then the "Add" button.
- **b )**	This is the process to "find" The App Pool
- **c )**	Make sure the "From this location" is the local computer (It may default to a company domain, if it in place)
- **d )**	Enter this into the text-box "IIS AppPool \ ..." where the actual App Pool name is used after the slash "IIS AppPool\Interject Data API" for example
- **e )**	Use the "Check Names" button. 


<img class="img-modal" src="/images/dot-net-api/edit-permissions-check-names.png" width="70%" onclick="zoom_img(this)" />

- **f )**	If the App Pool was identified successfully, then you should see the App Pool name as underlined

<img class="img-modal" src="/images/dot-net-api/app-pools-underline.png" width="40%" onclick="zoom_img(this)" />

- **g )**	Press OK and the App Pool will appear in the "Group or user names" box.

- **h )**	While it is selected, check the "Modify" setting of the permissions. This will allow the App Pool to have enough permissions over the API Website to behave normally.

<img class="img-modal" src="/images/dot-net-api/permissions-modify.png" width="40%" onclick="zoom_img(this)" />

- **i )**	Use the "Apply" button. And "OK" to close the windows.


### **11.	At this point, the website should be responding to browser requests. But it still needs a little more configuration in order to process Interject reports. First, confirm that the site is behaving by visiting it in a browser.**

- **a )**	Use the DNS setting from #1 at the start of these instructions, and paste them in a browser. (this was also added to the "Binding" of the site in IIS manager)
- **b )**	The default page of the API should appear. If it appears at all, then the entire API should be functioning normally.
- **c )**	The default page should look like the following image. This web page is normally not seen by users. It contains some notes for developers who may wish to customize the Data API. This web page is normally not seen by users. It contains some notes for developers who may wish to customize the Data API.

<img class="img-modal" src="/images/dot-net-api/default-page.png" width="60%" onclick="zoom_img(this)" />

- **d )**	If there is an error it may look something like this:


<img class="img-modal" src="/images/dot-net-api/server-error.png" width="40%" onclick="zoom_img(this)" />




### **12.  Set up Data Connection Strings for "Pass-Through" Interject requests**
The most common use of a Data API is for Intranet use. In this scenario a connection string can be shared by all users, while also protected within the web.config of the Data API.

Interject supports DataPortal connections for both: A)Direct DB access and B)API access
When using an API, you can tell the API code to perform certain DB actions by using "PassThrough" settings. These are configured in the DataPortal and DataPortal Connection. For these to work, they need to be able to find a connection string in the API.

If this API offers public access, then connection strings should not be shared in the web.config. Instead a custom validation lookup process should be implemented, which also requires some custom coding.

- **a )**	Determine a meaningful name for the connection string (preferably without spaces) This name will be used by an Interject DataPortal Connection, and it will reference the connection string within the web.config. Names must be unique.
- **b )**	Open the web.config file in any text editor or code IDE(you can find it in step #3 at the start of this document)
- **c )**	The contents are formatted as XML. Locate the section `<connectionStrings>`
- **d )**	Add a new line which uses the Name of the Connection String and its value.

```xml
<!--Windows Authentication to MSSqlServer Express-->
<add name="DataApi_NTAuth" connectionString="Server=.\sqlexpress; Database=MyDbName; integrated security=true"               providerName="System.Data.SqlClient" />

<!--Sql Server Authentication to MSSqlServer-->
<add name="DataApi_UsrPwd" connectionString="Server=MyServerName; Database=MyDbName; User ID=MyUserName; Password=MySecret;" providerName="System.Data.SqlClient" />

<!--Using the MySQL connector plugin   (note providerName="MySql.Data.MySqlClient") see http://dev.mysql.com/downloads/connector/net/--> 
<add name="DataApi_MySql"  connectionString="server=MyServerName; database=MyDbName; User Id=MyUserName; password=MySecret;" providerName="MySql.Data.MySqlClient" />
    
<!--ODBC driver to Oracle or MySQL-->
<add name="DataApi_ODBC"   connectionString="Driver={Oracle in Ora_32bit}; dbq=MyDbName; Uid=MyUserName; Pwd=MySecret;"      providerName="System.Data.SqlClient" />
```


### **13.  Additional settings in the web.config**
In the web.config file there are app.settings which affect the behavior of the API.
Double check that the web.config file has settings which match the ones below:

```xml
  <appSettings>
    <add key="IdsPlatformApi" value="https://platform-api.GoInterject.com" />
    <add key="Environment" value="Live" />
  </appSettings>
```

### **14.  Configure Data portals and Connections on the Portal Management site. The API is ready to test.**

