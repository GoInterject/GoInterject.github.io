---
title: Install
layout: custom
keywords: [Report, Epicor, Accounts]
description: Step by step guide on data tier, initial data load, FRx Migration, and other key processes of installing of Interject for Financials Epicor.
---

Before installing Interject Financials - Epicor, you will need to request an invite at the [Interject Portal Site](https://portal.gointerject.com). Fill out every field fo the invite request form and click "Create and Account". The Interject team will review and grant access to the Interject Platform.

After gaining access as a new company, there are three parts to installing Interject Financials - Epicor. First is the initial data tier install, then the data load from Epicor and FRx, then the actual report configurations in the Interject application. 

\(Before installing Interject for Financials, check that your system meets all requirements noted in the [Product Sheet](https://docs.gointerject.com/bApps/bFinancials/Epicor-Financials.html).

### Data Tier Install

<table>
   <tr>
    <th><span style="font-weight:bold">Prerequisites</span></th>
   </tr>
            <tr>
                <td>
                    <ul>
                        <li>SQL Server 2008</li>
                        <li>SQL Management Studio</li>
                        <li>Initial Deploy Scripts</li>
                        <li>User Admin on SQL Server</li>
                        <li>Active Directory User Group "Interject Users"</li>
                    </ul>
                </td>
            </tr>
</table>

> To-do
>
> **Step 1:** Connect to your Epicor server as SysAdmin in **SQL MGT Studio**
>
>**Step 2:** Create a new data base and name it "Interject_Reporting@epicor3", then press OK
>
> **Step 3:** Make sure that the script is pointed to the database you just created, and execute the script
>
> ![Mgt Studio Point](/images/A-SQL-InitialDataLoad/MgtStudioPointTo.png)
>
> **Step 4:** Execute initial deploy script on New Interject Reporting Database
>
> - 4a: DB Object Creation
> - 4b: DB Permissions and roles
>
> **Step 5:** Execute read only access setup script
> - 5b: Apply security to specific tables and users


### Initial Data Load


> To-do	
> **Step 1:** Execute Script DB to initialize Epicor Enterprise Data
>
> **Step 2:** Execute Script SQL Agent Jobs
>
> **Step 3:** Set up DB connection in Interject Portal
>
> **Step 4:** Redirect DB connection to new Interject DB


### FRx Database Migration

<table>
   <tr>
    <th><span style="font-weight:bold">Prerequisites</span></th>
   </tr>
            <tr>
                <td>
                    <ul>
                        <li>Verify ODBC connection to access DB</li>
                        <li>Download Initial FRx Migration Script</li>
                        <li>SQL Management Studio</li>
                    </ul>
                </td>
            </tr>
</table>

> To-do
>
> **Step 1:** OPen SQL Server and create a new DB
>
>**Step 2:** Import MDB file to the new DB
>
> **Step 3:** Execute FRx Migration Script
>
> **Step 4:** Set up DB connection in Interject Portal
>
>**Step 5:** Redirect connection to new DB in Interject process



## Epicor Segment Assessment
> To-do
>
> **Step 1:**Review use of Group Sets in FRX
>
> **Step 2:** Design Grouping Strategy for interject groupings
>
> **Step 3:** Define use of Segments such as natural account, locations, etc…
>
> **Step 4:** Verify Consistent segments across all Databases
>
> **Step 5:** Verify any Epicor Databases excluded from Migration
>
> **Step 6:** Verify Periods are CALENDAR month
>
> **Step 7:** Verify  use is single  currency only



### Application Install
With the Interject Add-in installed and an Admin user logged in:

> To-do
>
> **Step 1:** Monthly import schedule setup and test
>
> **Step 2:** Financials Grouping configuration and 


### Security and Updates
Install scripting will be versioned with GIT and we will provide update scripts (and revert) scripts that have been fully QA tested on an on-going basis. We can even easily track customizations in a similar way and the database will have a version table for tracking.
