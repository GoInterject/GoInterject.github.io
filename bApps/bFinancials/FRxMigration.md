---
title: FRx Migration
layout: custom
keywords: [Report, Epicor, Accounts]
description: Step by step guide on data tier, initial data load, FRx Migration, and other key processes of installing of Interject for Financials Epicor Enterprise.
---

<table>
   <tr>
    <th><span style="font-weight:bold">Prerequisites</span></th>
   </tr>
            <tr>
                <td>
                    <ul>
                        <li>Verify ODBC connection to Microsoft Access (if you installed MS Office, the connection should exist)</li>
                        <li>Convert FRx file to Access file (see image below)</li>
                    </ul>    
                </td>
            </tr>
</table>

![Epicor Tools Connection Page](/images/A-InitialDataLoad/FRXAccess.png){: .center-image }

### Open SQL Server and Create a New Database

> To Do
>
> **Step 1:** In **SQL Management Studio** to connect to server where FRx database can reside in
>
> **Step 2:** Right Click New Database in the Object Explorer
> ![Epicor Tools Connection Page](/images/A-InitialDataLoad/ObjectEx.png){: .center-image }
>
> **Step 3:** Choose a name of database to be used to store the legacy FRx reporting definitions in the Database Name field, then press OK
> ![Epicor Tools Connection Page](/images/A-InitialDataLoad/DataBasename.png){: .center-image }
>

### Import MDB File To the New Database

> To Do
>
> **Step 1:** In **SQL Management Studio**, select and right-click your database, then choose "Import Data"
> ![Epicor Tools Connection Page](/images/A-InitialDataLoad/SelectDB.png){: .center-image }
> **Note:** If Access database is protected, you will need to remove the database password before going through with the import
>
> **Step 2:** Select Microsoft Access (Microsoft Jet Database Engine) in the Data Source field and specify the location of the access file in the File name, then hit "Next"
> ![Epicor Tools Connection Page](/images/A-InitialDataLoad/DBSource.png){: .center-image }
>
> **Step 3:** Destination should be the new database created. Check that the following information is correct, then hit "Next" 
 - Destination: “SQL Server Native Client” corresponding to the version of SQL Server 
 - Server Name: where the new Legacy Reporting Definitions database resides
 - Database: New database created for importing FRx Legacy Reporting Definitions from prior step
> 
> ![DB Destination](/images/A-InitialDataLoad/DBDestination.png){: .center-image }
>
> **Step 4:** Specify in the next window that you're copying data from a table, then hit "Next" 
>
> **Step 5:** In the "Select Source Tables and Views" screen, confirm that all tables are selected and hit "Next"
> ![DB Destination](/images/A-InitialDataLoad/SelectAll.png){: .center-image }
>
> **Step 6:** In the "Save and Run Package" screen, select "Run immediately"  
> ![DB Destination](/images/A-InitialDataLoad/RunImmediately.png){: .center-image }
>
> **Step 7:** Review that the import occured and hit "Finish"
>

### Execute FRx Migration Script

> To Do
>
> **Step 1:** In **SQL Management Studio**, point to the new database 
> ```SQL
> Use Client_FRX_Definition
> Go
>```
>
> **Step 2:** Execute the FRx Migration Script. This will create all DB Objects
>


### Interject Application Setup- DB Connection

> To Do
>
> **Step 1:** Now log in to [portal.gointerject.com](https://portal.gointerject.com) and select Data Connections on the left side menu. Change company to “Epicor Test III”.
>
> **Step 2:** Change Company to newly setup “Epicor Test III”  
>
> **Step 3:** Select "Data Connections" in the "My Data" section of the admin toolbar
>
> **Step 4:** Select “Database” in the Connection Type field.
>
> **Step 5:** Fill in the Connection Details page with the following inputs for new connections:
> - Name: A unique friendly name used when connecting a Data Portal to the Data Connection
> - Description (optional): A description of what the connection string is connecting to
> - Connection String: This is used by Interject to connect to the specified server & database
>
>  ![DB Destination](/images/A-InitialDataLoad/ConnectionDetails.png){: .center-image }
> **Example connection string:** Data Source=server-04; Initial Catalog=Client_FRX_Definition; Integrated Security=SSPI;
>
>

## Redirect DB Connection to New DB in Interject process

>To Do
> 
> **Step 1:** Go to “My Apps” on the left menu of the Interject Portal page select by clicking on link “Interject Financials - Epicor” offering  - Versions may change
> ![DB Destination](/images/A-InitialDataLoad/image3.png){: .center-image }
>
> **Step 2:** At the bottom of the page in the “Connection Redirect” section choose to replace any existing FRX Connection with “new connection”
>
> **Step 3:** Click "Save"
>
>
> ![DB Destination](/images/A-InitialDataLoad/image2.png){: .center-image } 
>
>
