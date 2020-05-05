---
title: JE Upload Install
layout: custom
keywords: []
description: 
---

The following setup instructions will walk you through installation of the JE Upload tool by Interject. If you need to install the full Interject for Financials package, please go <a href src="https://docs.gointerject.com/bApps/bFinancials/Technical-Install.html">here</a>.





### Steps Required for JE Upload Install


> To-do
>
> **Step 1:** Connect to your Epicor server as **SysAdmin** in **SQL MGT Studio**
>
>**Step 2:** Create Interject Reporting Database
> - Right Click New Database in the Object Explorer
> ![New database](/images/A-SQL-Installation/newDB.png){: .center-image }
> - Enter the desired DB name into the Database Name field. The default is "Interject_Reporting", but you can name it as needed
> ![New database](/images/A-SQL-Installation/01.png){: .center-image }
> - Press OK
>
> **Step 3:** Point the script window to the new database
> ![Mgt Studio Point](/images/A-SQL-Installation/MgtStudioPointTo.png){: .center-image }
> 
> **Step 4:** Execute the  [1.0.1_Initial.Interject_JournalEntryUpload](https://drive.google.com/file/d/13rcfnl7TPD9IU-X2dw9TtAHVwYTncA9M/view?usp=sharing) script
>
> **Step 5:** Create security objects and grant read-only access to Epicor tables by passing the following parameters using the following script as an example:
>
> ```SQL
> EXEC [Setup].[Interject_SetupScript1_Security]
>	     @MasterEpicorDatabase      = '<Epicor Controlling Database Name>'
>       ,@CertificatePassword       =  'myPassword1234'
>```
>
>**Step 6:** Execute the following Script DB to initialize data from Epicor for Journal Entry Upload
> 
>* 6a
> ```SQL
> --Import configuration setup from Epicor and initial setup of Interject
> EXEC [Setup].[ERP_InstallScript1_DatabaseConfig]
>        @MasterEpicorDatabase          = '[<INSERT Master DB NAME>]'
>       ,@DefaultDatabaseNameSource     = '[<INSERT Default DB name>]'
> ```
>* 6b
> ```SQL
> --Import data
> EXEC [Setup].[ERP_InstallScript2_EpicorImport]
> ```

