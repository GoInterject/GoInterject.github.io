---
title: Add-in Errors
filename: "App-Errors.md"
layout: custom
keywords: [app, addin, errors]
headings: ["Overview", "Excel Drill Animations", "Add-ins Missing", "Web Proxy Configuration", "Cloud File Uploads Incorrectly"]
links: ["/wTroubleshoot/Drill-Animations.html", "/wTroubleshoot/Addin-Missing.html", "/wTroubleshoot/WebProxy.html", "/wTroubleshoot/Cloud-File.html"]
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