---
title: Installing - Shared Computer
filename: "SharedComputer.md"
layout: custom
keywords: [install, Multiple Users, Server, network]
headings: ["Overview", "Installing Interject on Multi-User Systems"]
links: ["https://portal.gointerject.com/login.html", "https://portal.gointerject.com/invite.html?mode=create", "https://docs.gointerject.com/wAbout/Logging-In.html", "mailto:help@gointerject.com"]
image_dir: "SharedComputer"
images: [{file: "15", type: "jpg", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "16", type: "png", site: "Portal", cat: "Download", sub: "Main", report: "", ribbon: "", config: ""}, {file: "17", type: "png", site: "Portal", cat: "Download", sub: "Main", report: "", ribbon: "", config: ""}, {file: "22", type: "png", site: "Windows", cat: "Explorer", sub: "Extract All", report: "", ribbon: "", config: ""}, {file: "24", type: "jpg", site: "Windows", cat: "Explorer", sub: "Folder", report: "", ribbon: "", config: ""}, {file: "25", type: "jpg", site: "Windows", cat: "Explorer", sub: "Extract", report: "", ribbon: "", config: ""}, {file: "31", type: "png", site: "Windows", cat: "Explorer", sub: "Folder", report: "", ribbon: "", config: ""}, {file: "33", type: "png", site: "Addin", cat: "Installation", sub: "Setup Wizard", report: "", ribbon: "", config: ""}, {file: "34", type: "png", site: "Addin", cat: "Installation", sub: "Installation Type", report: "", ribbon: "", config: ""}, {file: "37", type: "png", site: "Addin", cat: "Installation", sub: "End-User License Agreement", report: "", ribbon: "", config: ""}, {file: "38", type: "png", site: "Addin", cat: "Installation", sub: "Select Installation Folder", report: "", ribbon: "", config: ""}, {file: "39", type: "png", site: "Addin", cat: "Installation", sub: "Ready to Install", report: "", ribbon: "", config: ""}, {file: "40", type: "png", site: "Addin", cat: "Installation", sub: "Completed Install", report: "", ribbon: "", config: ""}]
description: This is the multi-user to one computer installation of Interject.
---
* * *

## Overview

Shared Computer installation installs a multi-user instance of Interject on one computer, such as a shared server. Since Interject's Addin Manager is used to manage independent settings for multiple users, this installation is dependant on the Add-in Manager. In order to run Per-Computer installation, you must have administrative-elevated rights.

### Installing Interject on Multi-User Systems

**Step 1:** Log in to the [**Interject website portal**](https://portal.gointerject.com/login.html). If you do not have an account go [here.](https://portal.gointerject.com/invite.html?mode=create) <!--best practices for documentation say to avoid pointing users to a url using a "click here" type of method. Instead, link directly to descriptive text within a sentence, as I've done above. (http://www.writethedocs.org/guide/writing/docs-principles/ > under Skimmable) -->

**Step 2:** Once logged in, go to the **download page.**.

![](/images/SharedComputer/15.jpg)
<br>

**Step 3:** Select **View other installers >>**.

![](/images/SharedComputer/16.png)
<br>

**Step 4:** Click the **Zip File for IT Admins Multiple-Users** option. This installer is only available on **Windows Server** machines. **Admin** privileges are also required for this install.

![](/images/SharedComputer/17.png)
<br>

**Step 5:** When the download is complete, **extract** the **zip file**. <!--is this step necessary? At this stage, I think it probably a given, or at least could be added onto another step.-->

![](/images/SharedComputer/22.png)
<br>

**Step 6:** Determine your **Destination Folder**.

![](/images/SharedComputer/24.jpg)
<br>

**Step 7:** Confirm your **Destination Folder**.

![](/images/SharedComputer/25.jpg)
<br>

**Step 8:** Navigate back to your **Extracted Zip Folder** and run the **InterjectSetup_Production_40_Standard_\[version\].exe** file **As Administrator**.

![](/images/SharedComputer/31.png)
<br>

**Step 9:** Step 9: Select "Next" when the **Interject Excel Add-In Setup Wizard** launches.

![](/images/SharedComputer/33.png)
<br>

**Step 10:** Read and accept the **End-User License Agreement** and select **Next**.

![](/images/SharedComputer/34.png)
<br>

**Step 11:** Two options will be available when installing on Windows Server.

1. Install as 'per-user' (current user)
2. Install as 'per-machine' (everybody)

To install for everybody on the server, make sure the **Everybody** button is selected then click **Next**.

![](/images/SharedComputer/37.png)
<br>

**Note:** Other Install features are available. For instructions on advanced installs, click on the readme located in the ZIP file or refer to the text file in the dropdown below.

<button class="collapsible">ReadMe File</button>
<div markdown="1" class="panel">

```
--------------- Advanced Installation by the Command Line --------------
The installer can be run silently from the command line by targeting the InterjectSetup_Production_40_Standard_[version].exe file. This will install as 'per-machine':
-Run the Command Prompt as administrator.
-Update the path so it targets the .exe file.
 C:\[Path_To_Exe]\InterjectSetup_Production_40_Standard_[version].exe /i // /qn ALLUSERS=1

key:
/i = install -or- /x = uninstall
/qn = quiet mode
// = Used by Advanced Installers .exe file to automatically replace with <path_to_msi>.
ALLUSERS = installs as 'per-machine' when set to 1. set to 0 to install as 'per-user'

to uninstall use a similar command with /x: (point to the .exe file of the current installation)
 C:\[Path_To_Exe]\InterjectSetup_Production_40_Standard_[version].exe /x // /qn ALLUSERS=1

--------------- Installation Logs --------------------------
Advanced Installer is the technology used to create the installer.
To see the install log (generated by the Advanced Installer InterjectSetup_Production_40_Standard_[version].exe), run the install command with an additional parameter /L* from the command line:
(update the path to the exe and also where to save the install log)
 C:\[Path_To_Exe]\InterjectSetup_Production_40_Standard_[version].exe /i // /qn /L* "C:\[Path_To_Exe]\install.log" <!--should the second "path_to_exe" bracket be "path_to_save" or something like that?-->

Add-In-Express is the technology used to register the application as an Excel Addin
To see the Add-In-Express install log, go to this file: (update the path for the current user)
 C:\Users\[UserName]\AppData\Local\Interject\App\adxregistrator.log
 or here (for per-machine install):
 C:\Program Files (x86)\Interject\adxregistrator.log
```

</div>

**Step 12:** Select the desired install location by clicking **Browse...**. By default a folder will be made inside the **Programs(x86)** folder.

Hit **Next** once the location is selected.

![](/images/SharedComputer/38.png)
<br>

**Step 13:** Click **Install** to begin the install process.

![](/images/SharedComputer/39.png)
<br>

**Step 14:** Click **Finish** once the setup wizard tells you the installation is complete.

![](/images/SharedComputer/40.png)
<br>


[Click here for login information](/wAbout/Logging-In.html)

If you run into any issues, email us at [help@gointerject.com](mailto:help@gointerject.com).

### File Locations

The following are the file locations for Interject for a Windows Server install:

- Application: C:\Program Files (x86)\Interject\
- File Cache: AppData\local\Interject
- Config & Auth: AppData\roaming\Interject