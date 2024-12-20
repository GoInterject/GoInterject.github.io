---
title: Add-in Errors
filename: "App-Errors.md"
layout: custom
keywords: [app, addin, errors]
headings: ["Overview", "Excel Drill Animations", "Add-ins Missing", "Web Proxy Configuration", "Cloud File Uploads Incorrectly", "AdxLoader Don't Match", "WebView2 Installation", "RowDef Data Clear", "Transport Errors", "Corrupted Interject Installation"]
links: ["/wTroubleshoot/Drill-Animations.html", "/wTroubleshoot/Addin-Missing.html", "/wTroubleshoot/WebProxy.html", "/wTroubleshoot/Cloud-File.html", "/wTroubleshoot/AdxLoader.html", "/wTroubleshoot/WebView2.html", "/wTroubleshoot/RowDefClear.html", "/wTroubleshoot/Transport-Errors.html", "/wTroubleshoot/CorruptedInstallation.html"]
image_dir: ""
images: []
description: Errors can occur for many reasons. Sometimes they are related to the environment or computer running Interject. It is important you have tools to capture everything that is interacting with Excel so, it is easier diagnose the cause of errors. This leads to faster troubleshooting and repair.
---
* * *

## Overview

Errors with Excel Add-ins or the Interject Add-in can occur for many reasons. Sometimes they are related to the environment or computer running Interject. It is important you have tools to capture everything that is interacting with Excel so it is easier diagnose the cause of the errors. This leads to faster troubleshooting and repair.

### [Excel Drill Animations](/wTroubleshoot/Drill-Animations.html)

It is important to disable the animations feature of Excel. Running animations while working with data may slow performance and interfere with Interject events, such as Drill on Data events. Depending on the version of Excel you have installed, and the Windows operating system on your computer, there are several ways to disable Excel animation.

### [Add-ins Missing](/wTroubleshoot/Addin-Missing.html)

If your Excel Add-ins go missing, you can follow these steps to reset them.

### [Web Proxy Configuration](/wTroubleshoot/WebProxy.html)

The Interject Add-in allows users to authenticate using Windows authentication. For this Interject uses System.Net.CredentialCache.DefaultCredential library to set up a proxy. Interject's default Windows proxy at the application level can prevent a client's machine level proxy. This will prevent a user from being able to log in. To get around this, there is an Interject setting where users and clients can disable the Windows proxy.

### [Cloud File Uploads Incorrectly](/wTroubleshoot/Cloud-File.html)

The Report Library provides a central hub where you can upload and download reports. Sometimes uploading a report from a cloud drive (e.g. OneDrive, SharePoint) results in errors. This guide helps you identify cloud files, reveals possible errors that may occur, and covers a few work-arounds.

### [AdxLoader Don't Match](/wTroubleshoot/AdxLoader.html)

This issue results in an error message upon opening Excel. The most likely cause of this error is that the bit version of Excel is out of sync with the Interject Add-in bit version. This will happen if the bitness of Microsoft Excel/Office is changed (e.g. 32 and 64 bit).

### [WebView2 Installation](/wTroubleshoot/WebView2.html)

Interject uses WebView2 for its login screen. If WebView2 is not installed, nothing will appear when you click the login button. Most systems have WebView2 already installed. If, however, it is not, you can install WebView2 [manually](https://developer.microsoft.com/en-us/microsoft-edge/webview2/){:target="_blank"}{:rel="noopener noreferrer"}.

### [RowDef Data Clear](/wTroubleshoot/RowDefClear.html)

Data does not clear when multiple columns are defined as the RowDefRange for a ReportVariable. This happens only when the first column of the RowDefRange is missing from the ColDefRange.

### [Transport Errors](/wTroubleshoot/Transport-Errors.html)

The transport layer of a network is responsible for ensuring reliable data transmission between devices. It is commonly implemented using protocols like TCP (Transmission Control Protocol) or UDP (User Datagram Protocol). However, during communication between a client and server, transport errors may occasionally occur.

### [Corrupted Interject Installation](/wTroubleshoot/CorruptedInstallation.html)

There are some instances where Interject may be left in an incomplete or corrupted state after installation. This can happen, for example, if the Interject installer was executed from within a zipped folder, without being properly extracted first. In such cases, the installation process may only partially complete, leading to issues such as being unable to uninstall or reinstall Interject properly. When this happens, manual intervention is required to fully remove the corrupted installation.
