---
title: Troubleshooting
layout: custom
keywords: [troubleshooting, issues, installation, drill, report, app]
description: INTERJECT optimizes speed by caching company settings such as Data Portals, Connections, and Report Library templates. This information is received on login and stored in memory for as long as the Excel session is open. Troubleshooting is therefore important for new deployments where these settings may need to change often.  If there are any changes to company settings, the INTERJECT Excel add-in will check for changes at various actions. Opening the Report Library or the Report Builder automatically checks for setting changes. Other actions like Pull, Save, or Drill check only every two hours, since these actions occur often and could create excess communication. The next three pages are dedicated to understanding how these different actions and environments interact for troubleshooting purposes. 
---

## **Overview**

INTERJECT optimizes speed by caching company settings such as Data Portals, Connections, and Report Library templates. This information is received on login and stored in memory for as long as the Excel session is open. Troubleshooting is therefore important for new deployments where these settings may need to change often.  If there are any changes to company settings, the INTERJECT Excel add-in will check for changes at various actions. Opening the Report Library or the Report Builder automatically checks for setting changes. Other actions like Pull, Save, or Drill check only every two hours, since these actions occur often and could create excess communication. The next three pages are dedicated to understanding how these different actions and environments interact for troubleshooting purposes. 

###  [ Troubleshooting App Errors ](/wTroubleshoot/App-Errors.html)

App Errors can occur for many reasons which are sometimes related to the environment or system running INTERJECT. One of the best tools for diagnosing these errors is INTERJECT's Verbose Logging. This allows for real-time error logging after setup, which can then be used to send error reports to INTERJECT's support team. This way, the INTERJECT support team is able to diagnose problems quickly and accurately. 

###  [ Troubleshooting Excel Animations ](/wTroubleshoot/Drill-Animations.html)

It is important to disable the animations feature of Excel. Running animations while working with data may slow performance and interfere with INTERJECT events, such as Drill on Data events. Depending on the version of Excel you have installed, and the Windows operating system on your computer, there are several ways to disable Excel animation. 

###  [ Troubleshooting Report Errors ](/wTroubleshoot/Reports.html)

Report errors occur for many reasons, some of which relate to how the server handles data and moves it to the report. Other reasons may include the report's direct configuration within Excel. INTERJECT provides various tools and features to help quickly and accurately diagnose report errors.

  


  

