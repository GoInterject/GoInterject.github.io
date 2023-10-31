---
layout: custom
title:  .NET API Setup
keywords: [data api, web api, c#, setup, .NET framework, IIS, server]
description: Shows how to setup an INTERJECT .Net data api.
---

##  Overview

Interject allows data flow from custom sources through a web API. The Interject Java API is built upon C# and the [.Net Framework](https://learn.microsoft.com/en-us/dotnet/framework/){:target="_blank"}{:rel="noopener noreferrer"}.

### Requirements

-  [Internet Information Services (IIS)](https://www.iis.net/){:target="_blank"}{:rel="noopener noreferrer"}
- [.NET Framework >= 4.5.2](https://dotnet.microsoft.com/en-us/download/dotnet-framework){:target="_blank"}{:rel="noopener noreferrer"}
- [.NET SDK](https://dotnet.microsoft.com/download){:target="_blank"}{:rel="noopener noreferrer"}

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

![](/images/API/DotNetDownloadZip.png)
<br>

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

### Setup Website in IIS

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
| Physical path | Location where the website folder is (contains "web.config") | Enter the directory you set up in [deployment](#deployment) |
| Pass-through authentication | Authentication used for protected resources | Keep the default setting "Application user" |
| Binding Type | Internet Security Protocol | HTTP or HTTPS<sup>2</sup> |
| IP Address | Addresses the server will listen to | Keep the default setting "All Unassigned"<sup>3</sup> |
| Port | Select a port for your website to run on | Unused port<sup>4</sup> |
| Host name | (Optional) Enter a name for the website | Enter the name of the host |

---
**<sup>1</sup>** _Upon creation of the website, the default IIS behavior is a custom Application Pool is created matching the name of the website. This App Pool is preferred instead of the default App Pool._

**<sup>2</sup>** _If HTTPS is selected you will need to set up an SSL Certificate (not covered in this documentation)_

**<sup>3</sup>** _This setting can be left as the default or a Specific IP address can be used if this web server responds to multiple IP addresses. It is more common to use a specific IP address when dealing with multiple SSL certificates on the same web server._

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

You will need to modify the security permissions of the App Pool.

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

**Step 7:** Ensure the **Modify** permission is checked.

![](/images/dot-net-api/Modify.png)
<br>

Finally click **Apply** and then **OK** twice to save the changes.

### Firewall

when setting up a website in Internet Information Services (IIS), you may need to edit your firewall permissions to allow incoming traffic to the web server. This is an important step in making your website accessible to users over the network. 

### Testing

At this point, the server in IIS should be running.

![](/images/dot-net-api/IISServerRunning.png)
<br>

To confirm the API is working, navigate to the host name or port you set up [previously](#setup-website-in-iis) and access the status endpoint ("api/v1/status"). You should see "true" if the API is working.

![](/images/dot-net-api/ApiRunning.png)
<br>

### Connection Strings



![](/images/dot-net-api/)
<br>
