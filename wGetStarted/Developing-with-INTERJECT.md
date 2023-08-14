---
title: Developing with Interject
layout: custom
keywords: [develop, database, build, create, SQL]
description: This section is for professional developers who create the data pathways for reports and applications that can edit data. To facilitate this section, we provide a sample database to assist in training.
---
* * *

## Overview

This section is for professional developers who create the data pathways for reports and applications that can edit data. To facilitate this section, we provide a sample database to assist in training. Please contact us for the files at [info@gointerject.com](mailto:info@gointerject.com).

The sample database is called **Interject_Example_v1**. This database is available for SQL Server versions 2008 to 2017 and works easily with the free express version. Download SQL Server Express [here](https://www.microsoft.com/en-us/sql-server/sql-server-editions-express){:target="_blank"}{:rel="noopener noreferrer"}.

To complete the developer training, you must have Client Admin permissions within an existing Interject account. Verify the correct role at the Interject Website Portal at [https://portal.gointerject.com](https://portal.gointerject.com) For help with logging in, see [Logging In to the Website Portal](/wPortal/Logging-In-to-Website-Portal.html).

Navigate by using the following links to continue with the training objectives:

### [Interject Website Portal](/wGetStarted/Interject-Website-Portal.html)

The Interject website portal is a central place to manage Interject client settings and user profiles. For an Interject developer, the most used areas of the Interject website portal are managing connections and data portals.

### [Defining Interject for Developers](/wGetStarted/Defining-Interject-for-Developers.html)

Developers often assume that Interject is useful only in building simple reports, not extending to workflow creation or collecting user inputs. However, Interject is truly an application platform that can extend reports into two-way interfaces, which have the impact and scalability of a website application.

### [Simple Data Pull](/wGetStarted/Simple-Data-Pull.html)

To clearly illustrate the end-to-end workflow of developing a report, you can begin with several simple data pull examples showing different report configurations. You will be reusing Interject reports used in previous sections, because these should be familiar to you if you read this documentation from the beginning. By the end of these sections, you will understand the process of creating spreadsheet friendly reports that can drill to other reports.

### [Advanced Data Pull](/wGetStarted/Advanced-Data-Pull.html)

Interject reports can handle a wide variety of complex reports. Up to this point you have seen simple reports where a single recordset is returned to single area of the spreadsheet. This topic will share advanced reporting configurations that use multiple recordsets and multiple Interject report formulas and supporting functions to construct advanced presentations.

### [Simple Data Save](/wGetStarted/Simple-Data-Save.html)

Interject allows for the editing of data and uploading those changes directly into the database it is connected to. This requires a different Data Portal.

### [Security Best Practices](/wGetStarted/Security-Best-Practices.html)

Managing security is a key component of the Interject platform, and there are several areas to understand. Security involves both the row level security that can exist in reports and apps and how the middle tier objects are secured. Security also includes which spreadsheet report template can be seen by which users. The paragraphs here discuss each of these areas, best practices in building, and methods to test user access.

### [Managing Settings Cache](/wGetStarted/Managing-Settings-Cache.html)

Interject optimizes speed by caching company settings, such as Data Portals, Connections, and Report Library templates. This information is received on login and is stored in memory for as long as the Excel session is open. This is an important topic for new deployments where these settings may need to change often. If there are any changes to these company settings, the Interject Excel add-in will check for changes at various actions.

### [Error Handling](/wGetStarted/L-Dev-Error-Handling.html)

There are two types of errors that Interject can display: unhandled and handled. Unhandled errors are system generated, whereas handled errors are anticipated and written by developers. For example, on a pull or save, an error may occur on the server which the report is trying to access. This error could be handled by the developer if the developer anticipates it, or it could be left as an unhandled error.