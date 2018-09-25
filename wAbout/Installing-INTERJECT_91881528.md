---
title: Interject Documentation > Installing INTERJECT
layout: custom
---
* * *

##  The INTERJECT Excel Add-in has Two Installation Paths

There are 2 options when installing INTERJECT:

  *     * ** Installation Option 1:  ** Installing from the Portal Management Website using a ClickOnce installer for Windows™. This option is intended for single users to log into our portal to install INTERJECT. This option is quick, easy, and requires the fewest steps. 
    * ** Installation Option 2:  ** Installing via an Enterprise level MSI installer. This option is for large user bases that have standard configurations. This option is installed with a session controller who distributes the product to all necessary computers. While more technical, user set-up is still simple. 

###  Option 1: From Portal Management Website

**Step 1:** Navigate to [ https://portal.gointerject.com
](https://portal.gointerject.com/login.html)

**Step 2:  
**

  1. With an existing account, log in to the portal website with the same credentials used for the INTERJECT Excel Add-in. 
  2. If you do not have an account, create one in the portal site by **Requesting an Invite** . INTERJECT will review your business information and provide a trial experience. 

![](attachments/91881528/128370693.png)

**  
**

**Step 3:** Once logged in, visit the download page, and click the Install
button to begin.

![](attachments/91881528/128324411.png?width=960)

  

**Step 4:** Run the file after downloading. This will look slightly different
in every browser (see below).

Chrome:

![](attachments/91881528/128359191.png)

  

Firefox:

![](attachments/91881528/128359215.png)

  

Internet Explorer:

** ![](attachments/91881528/128359252.png) **

  

Microsoft Edge:

** ![](attachments/91881528/128359276.png) **

**  
**

**Step 5:** This file runs a Clickonce installer, which will ask for approval.

![](attachments/91881528/128407024.png?width=550)

  

Any additional files will be downloaded by the installer.

![](attachments/91881528/128406975.png?width=550)

  

INTERJECT will be **registered** within Excel as an Add-in. It will appear the
next time Excel is started.

![](attachments/91881528/128406994.png) **  
**

  

**Step 6 (For new installations):** If this is a new installation, then some
preliminary settings are chosen. These can be changed later through the [
INTERJECT ribbon menu ](/wPortal/INTERJECT-Ribbon-Menu-Items_83689479.html) .
Standard users will use the INTERJECT Cloud option. If a company has arranged
for unique configurations, a Custom Install Code might be used. Enterprise
clients using a central MSI installation might use a Network Folder.

![](attachments/91881528/128587447.png?width=550)

**  
**

**Step 7:** When Excel opens, a prompt to accept the User License Agreement
appears.

![](attachments/91881528/128406954.png?width=550)

  

You are now ready to go! Just look for the INTERJECT tab on the Excel ribbon
so you can use the [ Login
](https://interject.atlassian.net/wiki/display/ID/Logging+In) below.

![](attachments/91881528/92340235.png)

#####

###  Option 2: Enterprise level MSI installer

This method is for installing INTERJECT using the MSI-based installer package.
Since each MSI is tailored to an individual customer, this will be a general
overview of the steps for this option. The MSI-based installation also depends
on the Interject Session Controller. The Interject Session Controller needs to
run with elevated permissions, and it is used to manage the INTERJECT Add-in
on multi-user servers.

  

**Step 1:** Acquire the zip folder with the INTERJECT install files and
extract wherever you would like.

![](attachments/91881528/128240252.png?width=700)

  

Inside will be three files. An executable, an MSI and, a text file. Before
starting, take a look at the "readme.txt", which will have the most up-to-date
information on the installation.

![](attachments/91881528/128240360.png?width=700)

  

**Step 2:** With the INTERJECT MSI option, you have 2 possible methods to
install: One uses the Command Line (.cmd). The other uses the Executable
(.exe). For both options, you need to run the .cmd or .exe in administrator
mode.

  

**Method 1:** Command Line

Open the text file and copy the line that will install INTERJECT. **Note:**
Update the path to the MSI mid-way through the line.

![](attachments/91881528/128241211.png?width=920)

  

It will look like this in Command Prompt. Press enter to finish the
installation. Since you are installing in quiet mode, no other action is
needed.

![](attachments/91881528/128240796.png?width=920)

**Note:** Make sure to restart Excel after installing.

  

**Method 2:** The other option is using the executable

**Step 1:** Right click the executable and allow it to open as administrator.

![](attachments/91881528/128241834.png?width=550)

  

**Step 2:** Select the program to run as an unknown publisher (certifications
in progress). The following window will open. Click next.

![](attachments/91881528/128375146.png?width=550)

**  
**

**Step 3:** Read and agree to the End-User License Agreement.

![](attachments/91881528/128375187.png?width=550)

**  
**

**Step 4:** Determine where you would like INTERJECT to be installed.

![](attachments/91881528/128375279.png?width=550)

  

Click install to finish!

![](attachments/91881528/128375411.png?width=550)

  

The following window should open once successfully installed.

![](attachments/91881528/128380872.png?width=550)

  

**Note:** Please restart Excel after completing these steps.

If you run into any issues you can email us at [ help@gointerject.com
](mailto:help@gointerject.com) .

  

##  Related Links:

[ Logging In ](/wAbout/Logging-In_63275074.html)

[ Report Library Basics
](https://interject.atlassian.net/wiki/display/ID/Report+Library+Basics)

[ Real-World Walkthroughs ](/wAbout/Real-World-Walkthroughs_128091006.html)

[ Working with INTERJECT ](/wAbout/Working-with-INTERJECT_61702912.html)

  

