---
layout: custom
title:  .NET API Setup
keywords: [data api, web api, c#, setup, .NET framework, IIS, server]
description: Shows how to setup an INTERJECT .Net data api.
---

##  Overview

Interject allows data flow from custom sources through a web API. The Interject Java API is built upon C# and the [.Net Framework](https://learn.microsoft.com/en-us/dotnet/framework/){:target="_blank"}{:rel="noopener noreferrer"}.

### Requirements

-  [Internet Information Services (IIS)](https://www.iis.net/){:target="_blank"}{:rel="noopener noreferrer"} (if hosting with IIS)
- [.NET >= 7.0](https://dotnet.microsoft.com/en-us/download/dotnet){:target="_blank"}{:rel="noopener noreferrer"}
- [.NET SDK](https://dotnet.microsoft.com/download){:target="_blank"}{:rel="noopener noreferrer"} (for developing)

<blockquote class=highlight_note>
<b>Note:</b> If you intend to use this API on Linux or macOS, it is necessary to download <a href="https://www.mono-project.com/" target="_blank" rel="noopener noreferrer">Mono</a>, the cross platform open-source development platform based on the .NET Framework.
</blockquote>

### Get The Code

With Git, you can clone the repository directly to your system. Navigate to the desired directory and run the following command:

```git
git clone https://github.com/GoInterject/ids-dotnet-api.git
```

**Note:** If this repo is private and you need access, please [contact us](mailto:help@gointerject.com). It will be public soon.

Alternatively you can download the [zip file](https://github.com/GoInterject/ids-dotnet-api/archive/refs/heads/main.zip){:target="_blank"}{:rel="noopener noreferrer"} and unpack manually:

![](/images/dot-net-api/DotNetDownloadZip.png)
<br>

### The Repo

The repo contains two code bases: the `interject.api` code and the `interject.data.api` code. The Interject.Api contains the code relating to the handling of Interject requests, formatting data, and returning responses to the Interject Addin. This package is available on Nuget, the central package repository. The code base is included in the repo for preview.

The Interject.Data.Api contains the code relating to controllers and endpoints. The Interject.Api package is imported from Nuget into the Interject.Data.Api with the using statement:

```c#
using Interject.Api
```

### Getting IIS

Internet Information Services ([IIS](https://learn.microsoft.com/en-us/iis/get-started/introduction-to-iis/iis-web-server-overview){:target="_blank"}{:rel="noopener noreferrer"}) for Windows Server is a flexible, secure and manageable Web server for hosting anything on the Web. For most cases, the default roles and features of IIS will suffice. For more information, see [Roles, Role Services, and Features](https://learn.microsoft.com/en-us/windows-server/administration/server-core/server-core-roles-and-services){:target="_blank"}{:rel="noopener noreferrer"}.

For detailed information on IIS installation, see [here](https://learn.microsoft.com/en-us/iis/application-frameworks/scenario-build-an-aspnet-website-on-iis/configuring-step-1-install-iis-and-asp-net-modules){:target="_blank"}{:rel="noopener noreferrer"}.

#### Windows

Open the Control Panel and click on **Turn Windows features on or off**:

![](/images/dot-net-api/TurnWindowsFeaturesOn.png)
<br>

Under IIS, select the components you which to install:

![](/images/dot-net-api/IISFeaturesOnOrOff.png)
<br>

#### Windows Server Manager

Click **Manage** and then **Add Roles and Features**:

![](/images/dot-net-api/AddRolesAndFeatures.png)
<br>

Follow the wizard that appears and under "Server Roles", select the Web Server (IIS) components you which to install:

![](/images/dot-net-api/ServerRoles.png)
<br>

### Publishing

Publishing the web API varies depending on your development environment:

* [Visual Studio](https://learn.microsoft.com/en-us/dotnet/core/tutorials/publishing-with-visual-studio){:target="_blank"}{:rel="noopener noreferrer"}
* [VS Code](https://learn.microsoft.com/en-us/dotnet/core/tutorials/publishing-with-visual-studio-code){:target="_blank"}{:rel="noopener noreferrer"}
* [.NET CLI](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-publish){:target="_blank"}{:rel="noopener noreferrer"}

### Deployment

Determine where you want your Web API files to reside. The default directory for Windows is "inetpub" located on the C drive but any folder will do. It is recommended to use a separate directory for the source rather than the published directory. 

For more information, see [Host ASP.NET](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/){:target="_blank"}{:rel="noopener noreferrer"}.

### Set Up Website in IIS

Begin by opening up IIS. With Windows, click the **Start** button and type in "IIS":

![](/images/dot-net-api/StartIIS.png)
<br>

With Windows Server Manager, click on **Tools** and then **IIS**:

![](/images/dot-net-api/ServerManagerIIS.png)
<br>

In the left explorer pane, right click "Sites" and then select "Add Website..."

![](/images/dot-net-api/AddWebsite.png)
<br>

The following IIS Settings will need to be setup for the website:

| Property | Description | Value |
|---|---|---|
| Site name | Identifies this site in IIS (only visible to the admin) | Enter a descriptive value |
| Application Pool | Set of configuration settings | Keep the default<sup>1</sup> |
| Physical path | Source folder for the website | Enter the directory you set up in [deployment](#deployment) |
| Pass-through authentication | Authentication used for protected resources | Keep the default setting "Application user" |
| Binding Type | Internet Security Protocol | HTTP or HTTPS<sup>2</sup> |
| IP Address | Addresses the server will listen to | Keep the default setting "All Unassigned"<sup>3</sup> |
| Port | Select a port for your website to run on | Unused port<sup>4</sup> |
| Host name | (Optional) Enter a name for the website | Enter the name of the host |

---
**<sup>1</sup>** _Upon creation of the website, the default IIS behavior is a custom Application Pool is created matching the name of the website. This App Pool is preferred instead of the default App Pool._

**<sup>2</sup>** _If HTTPS is selected you will need to set up an SSL Certificate (not covered in this documentation - see [here](https://learn.microsoft.com/en-us/iis/manage/configuring-security/how-to-set-up-ssl-on-iis){:target="_blank"}{:rel="noopener noreferrer"})_

**<sup>3</sup>** _This setting can be left as the default or a specific IP address can be used if this web server responds to multiple IP addresses. It is more common to use a specific IP address when dealing with multiple SSL certificates on the same web server._

**<sup>4</sup>** _Normally follows the default 80 for HTTP and 443 for HTTPS, unless a network administrator requires an override. If a used port is entered, you will need to enter a host name._

An example of an API set up within a company's intranet is here:

![](/images/dot-net-api/IISSettingsExample.png)
<br>

For more info about setting up a website in IIS, see [Add a Web Site](https://learn.microsoft.com/en-us/iis/get-started/getting-started-with-iis/create-a-web-site){:target="_blank"}{:rel="noopener noreferrer"}.

### Windows Host File

The Windows hosts file is typically used to manually map host names to IP addresses when DNS resolution is not available or when you want to test a website before making it publicly accessible. If you are testing locally (127.0.0.1) or want to use custom domains, you will need to edit this file.

The host file is located in the "System32" folder of your Windows installation:

C:\Windows\System32\drivers\etc\host

Open this file as an Administrator in order to save changes.

![](/images/dot-net-api/HostFile.png)
<br>

### App Pool

The Application Pools can be viewed by selecting it in the left hand explorer. Verify the pool being used is v4.0 for the .NET CLR Version and is using an integrated pipeline.

![](/images/dot-net-api/AppPool.png)
<br>

### Setting Security Permissions

Depending on your use case, you may need to give the App Pool "modify" permissions.

**Step 1:** Right click the website and select "Edit Permissions..."

![](/images/dot-net-api/EditPermissions.png)
<br>

**Step 2:** On the **Security** tab, click **Edit**.

![](/images/dot-net-api/EditSecurity.png)
<br>

**Step 3:** You will need to first add the App Pool to the list of groups. Click on **Add**.

![](/images/dot-net-api/AddPermission.png)
<br>

**Step 4:** To expand the search for the App Pool, you will need to select the root system. Click on **Location**.

![](/images/dot-net-api/Locations.png)
<br>

**Step 5:** Select the root system name and click **OK**.

![](/images/dot-net-api/SelectSystemName.png)
<br>

**Step 6:** For the object names to select, enter the following and click **Check Names**:

```
IIS AppPool\<Site Name>
```

![](/images/dot-net-api/CheckNames.png)
<br>

The App Pool name should appear underlined. Click **OK** to add the App Pool to the list of groups.

![](/images/dot-net-api/AppPoolNameUnderlined.png)
<br>

**Step 7:** Now that the App Pool has been added to the group entities, ensure the **Modify** permission is checked for it.

![](/images/dot-net-api/Modify.png)
<br>

Finally click **Apply** and then **OK** twice to save the changes.

### Firewall

When setting up a website in Internet Information Services (IIS), you may need to edit your firewall permissions to allow incoming traffic to the web server. This is an important step in making your website accessible to users over the network. 

### Testing

At this point, the server in IIS should be running.

![](/images/dot-net-api/IISServerRunning.png)
<br>

To confirm the API is working, navigate to the host name or port you set up [previously](#setup-website-in-iis) and access the status endpoint ("api/v1/status"). You should see "true" if the API is working.

![](/images/dot-net-api/ApiRunning.png)
<br>

### Connection Strings

The most common use of a Data API is for Intranet use. In this scenario a connection string can be shared by all users, while also protected within the Data API.

Interject supports DataPortal connections for both direct DB access and API access. When using an API, you can code the API to perform certain DB actions by using "PassThrough" settings. These are configured in the DataPortal and DataPortal Connection. For these to work, they need to be able to find a connection string in the API.

If this API offers public access, then connection strings should not be shared in the `web.config` file. Instead a custom validation lookup process should be implemented, which also requires some custom coding. This Data API uses a `appsettings.json` file for this purpose.

* Determine a meaningful name for the connection string (preferably without spaces) This name will be used by an Interject DataPortal Connection, and it will reference the connection string within the `appsettings.json`. Names must be unique.
* Open the `appsettings.json` file (in the `interject-dotnet-api` directory) in any text editor or code IDE.
* Add a new entry in the list of ConnectionStrings collection.

Example of a connection string entry:

```xml
"Connections": {
    "ConnectionStrings": [
        {
        "Name": "localhost",
        "ConnectionString": "Data Source=(local);Initial Catalog=interject_demos;Encrypt=False;Integrated Security=True"
        }
    ]
}
```

### Connecting to Interject

With the API running and connection strings stored in the `appsettings.json` file, you can connect the Interject Addin by setting up a Data Connection and Data Portal on the [Portal Site](https://portal.gointerject.com/).

For how to set up an API Data Connection, see [Portal: API Connection](/wPortal/L-Api-Connections.html). For Data Portals, see [Data Portals](/wPortal/Data-Portals.html).

### Interject Docs

For more information on the Data API, you can refer to the docs in the repo. These docs pertain to setting up Interject reports and functions. They are found in the `examples` directory:

| File | Description |
|---|---|
| example.xlsx | An example Excel workbook that interacts with the API endpoints |
| formula_jcolumndef | How to set up the [jColumnDef](/wIndex/jColumnDef.html) formula |
| portal_parameters | How to set up Interject [parameters](/wPortal/Data-Portals.html#overview-of-parameters) |
| report_fixed | How to set up an Interject [ReportFixed](/wIndex/ReportFixed.html) |
| report_range | How to set up an Interject [ReportRange](/wIndex/ReportRange.html) |
| report_save | How to set up an Interject [ReportSave](/wIndex/ReportSave.html) |
| report_variable | How to set up an Interject [ReportVariable](/wIndex/ReportVariable.html) |
| handler_pipeline | How to work with the `RequestHandler` pipeline to set up a SQL data connection and controller |
| user_message | How to send [messages](/wGetStarted/L-Dev-Error-Handling.html) back to the Interject from the API |
