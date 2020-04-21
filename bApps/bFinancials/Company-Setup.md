---
title: Install
layout: custom
keywords: [Report, Epicor, Accounts]
description: Step by step guide on data tier, initial data load, FRx Migration, and other key processes of installing of Interject for Financials Epicor.
---

Shortly after signing a Client contract, please submit specific client information to your assigned account manager at Interject. You will receive communication on each individual project based who your account manager is.

Please provide the following information:

<table style="max-width: 60%;">
  <tr>
    <th>Field</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Company Name</td>
    <td>Client Company Legal Name</td>
  </tr>
  <tr>
    <td>First Name</td>
    <td>Name of Desired Interject admin/ Contact</td>
  </tr>
  <tr>
    <td>Last Name</td>
    <td>Name of Desired Interject admin/ Contact</td>
  </tr>
  <tr>
    <td>Email Address</td>
    <td>Email address of Admin contact</td>
  </tr>
  <tr>
    <td>Phone Number</td>
    <td>Phone # of Admin Contact</td>
  </tr>
  <tr>
    <td>Address</td>
    <td>Client Address</td>
  </tr>
  <tr>
    <td>City</td>
    <td>Client City</td>
  </tr>
  <tr>
    <td>State</td>
    <td>Client State</td>
  </tr>
  <tr>
    <td>Zip</td>
    <td>Client Zip</td>
  </tr>
  <tr>
    <td>Country</td>
    <td>Client Address</td>
  </tr>
  <tr>
    <td>Industry</td>
    <td>Client Industry</td>
  </tr>
  <tr>
    <td># of Employees</td>
    <td>-50, 50-500, 500+</td>
  </tr>
  <tr>
    <td>Yearly Revenue</td>
    <td>Small Cap, Mid Cap, Large cap</td>
  </tr>
  <tr>
    <td>Company Description</td>
    <td>Simple Description of Company</td>
  </tr>
  <tr>
    <td>Planned Use of Interject</td>
    <td>Interject for Financials</td>
  </tr>
</table>



> To Do
>
> **Step 1:** Verify Client's SQL Server is a Compatible Version
> SQL Server 2008 or greater is required. It is recommended that a Client provide at least a test and production environment in which they will to deploy Interject Financials - Epicor.  
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

Within a week, you will receive verification from Interject that your company setup and subscription is complete.
