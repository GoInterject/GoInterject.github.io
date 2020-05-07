---
title: User Setup
layout: custom
keywords: [Report, Epicor, Accounts]
description: Step by step guide on data tier, initial data load, FRx Migration, and other key processes of installing of Interject for Financials Epicor Enterprise.
---

After submitting your company information, go through the following steps to activate users

> To Do
>
> **Step 1:** Verify Client's SQL Server is a Compatible Version
> SQL Server 2008 or greater is required. It is recommended that a Client provide at least a test and production environment in which they will to deploy Interject Financials - Epicor Enterprise.  
(run "SELECT @@VERSION" in a query window to check version)
>
> **Step 2:** Prepare for using Windows Authentication by creating the active directory user group “Interject Users” on Default SQL Server Domain. The Interject User group should include any and all users of Interject Financials for Epicor. Separate groups may need to be set up if client has other uses of interject and requires separate optional but recommended security and authorization.
>
> **2a:** You can find the value of the SELECT DEFAULT_DOMAIN() in SQL Management Studio
>
> ![Active User](/images/A-SQL-Installation/DDomain.png){: .center-image }
>
> **2b:** On your AD Server Match, find the name from step 2a by right clicking the values in the domain controller > Properties. Note, this is only required if  more than 1 Domain exists.
> ![Active User](/images/A-SQL-Installation/ADServer.png){: .center-image }
> ![Active User](/images/A-SQL-Installation/DDomain2.png){: .center-image }
>
>
> **2c:** Set up the relating active directory user group “Interject Users” on Default SQL Server Domain
>
>
> ![Active User](/images/A-SQL-Installation/ActiveUser.png){: .center-image }
> ![Active User](/images/A-SQL-Installation/ActiveUser2.png){: .center-image }
>
>
> **NOTE:** If you do not have SQL Management Studio, [download it here](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-2017)
> Please let an Interject account manager know if your client cannot enable Windows Authentication with the recommended settings as illustrated above.
>