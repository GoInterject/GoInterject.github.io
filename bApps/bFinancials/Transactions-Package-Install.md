---
title: Transactions Package Install
filename: "Transactions-Package-Install.md"
layout: custom
keywords: [Epicor, SQL MGT Studio, tools]
headings: ["Steps Required for Transactions Package"]
links: ["/bApps/bFinancials/Technical-Install.html", "/images/A-SQL-Installation/newDB.png", "/images/A-SQL-Installation/01.png", "/images/A-SQL-Installation/MgtStudioPointTo.png", "https://drive.google.com/file/d/1hmX-cbVzp-pbqPChEBWKkO-DS2752-Jo/view?usp=sharing"]
image_dir: "A-SQL-Installation"
images: [
	{file: "newDB", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "01", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "MgtStudioPointTo", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}
	]
description: The following setup instructions will walk you through installation of the slim package of the Financials - Epicor Enterprise package which contains only transactions tools by Interject.
---

The following setup instructions will walk you through installation of the slim package of the Financials - Epicor Enterprise package which contains only transactions tools by Interject. For installation of the full package, please go [here](/bApps/bFinancials/Technical-Install.html).

### Steps Required for Transactions Package

> To-do
>
> **Step 1:** Connect to your Epicor server as **SysAdmin** in **SQL MGT Studio**
>
> **Step 2:** Create Interject Reporting Database
>
> - Right Click New Database in the Object Explorer
>   ![New database](/images/A-SQL-Installation/newDB.png){: .center-image }
> - Enter the desired DB name into the Database Name field. The default is "Interject_Reporting", but you can name it as needed
>   ![New database](/images/A-SQL-Installation/01.png){: .center-image }
> - Press OK
>
> **Step 3:** Point the script window to the new database
> ![Mgt Studio Point](/images/A-SQL-Installation/MgtStudioPointTo.png){: .center-image }
>
> **Step 4:** Execute initial deploy script on the new Database
> [1.1.1_Initial.Interject_Reporting.sql](https://drive.google.com/file/d/1hmX-cbVzp-pbqPChEBWKkO-DS2752-Jo/view?usp=sharing)
>
> **Step 5:** Create security objects and grant read-only access to Epicor tables by passing the following parameters using the following script as an example:
>
> ```SQL
> EXEC [Setup].[Interject_SetupScript1_Security]
>        @MasterEpicorDatabase      = '[<INSERT Master DB Name>]'
>       ,@CertificatePassword       = 'myPassword1234'
> ```
>
> **Step 6:** Execute the following script DB to initialize data from Epicor for the Transactions "Slim" Package
>
> ```SQL
> -- Import configuration setup from Epicor and initial setup of Interject
> EXEC [Setup].[ERP_InstallScript1_DatabaseConfig_Slim]
>        @MasterEpicorDatabase          = '[<INSERT Master DB NAME>]'
>       ,@DefaultDatabaseNameSource     = '[<INSERT Default DB name>]'
> ```
