---
title: Moving From Test to Live
filename: "Test2Live.md"
layout: custom
keywords: [Report, Epicor, Accounts]
headings: ["Option 1: Moving the Entire Database", "Option 2: Deploying A New Implementation From Scratch", "Re-Deploy From Scratch", "Transfer Custom Rollups and Report Templates", "Custom Rollups", "Custom Row Templates", "Custom Reports"]
links: ["/bApps/bFinancials/Test2Live.html#option-1-moving-the-entire-database", "/bApps/bFinancials/Test2Live.html#option-2-deploying-a-new-implementation-from-scratch", "https://docs.gointerject.com/bApps/bFinancials/InitialDataLoad.html#steps-required-for-interject-application-setup-data-connection", "https://docs.gointerject.com/bApps/bFinancials/Technical-Install.html", "https://docs.gointerject.com/bApps/bFinancials/InitialDataLoad.html#begin-data-load", "https://docs.gointerject.com/bApps/bFinancials/Localize.html"]
image_dir: "Config"
images: [
	{file: "SchedulerReportLib", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SchedulerTool", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "CompanyButton", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "ConfigMGR", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SetupRollups", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "CustomRollup", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "CompanyButton", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "ConfigMGR", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SetupRowTemp", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "CustomRowTemp", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "CompanyButton", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "OpenCustReport", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}
	]
description: Step by step guide on converting reports in test environments to reports in live environments.
---
There are two options available when moving your Interject Financials report templates and rollups from a test environment to the live environment, where your users can interact with them.

**Option 1:** [Moving the Entire Database](/bApps/bFinancials/Test2Live.html#option-1-moving-the-entire-database) – This option should only be used when "Live" and "Test" environment are similar. The following criteria must be met:

- [] Epicor test database(s) need to be snapshots of "Live". (Data in "Test" server can be older than what is on "Live") 
- [] Epicor data on "Test" was not changed since the snapshot from "Live" 
- [] All Epicor database(s) on “Live” should also be in “Test” 
- [] SQL Server version and setup of “Test” should match “Live”

**Option 2:** [Deploying A New Implementation from Scratch](/bApps/bFinancials/Test2Live.html#option-2-deploying-a-new-implementation-from-scratch) – This option will take more time, but it will be a from-scratch installation. The installation steps will mirror the initial deploy for a “Test” server.  Additional steps will include transferring rollups, templates, and reports from “Test” company to “Live”.   

### Option 1: Moving the Entire Database

This option details the steps in restoring a backup of Interject_Reporting from a "Test" to a "Live" environment and connecting the database so it imports and reporting work. Before using this option review the requirement listed above. 

> To Do
>
> **Step 1:** Create a backup of the "Test" database and restore it on the "Live" server.
>
> **Step 2:** To reapply security to the live DB, execute the **Interject_SetupScript1_Security** stored procedure, seen below.
> ```SQL
> EXEC [Setup].[Interject_SetupScript1_Security]
>       @MasterEpicorDatabase = '<Epicor Controlling Database Name>'
>      ,@CertificatePassword = 'myPassword1234'
> ```
> **Step 3:** Execute **ERP_InstallScript5_SetupJobs**, as seen below, to create sync jobs
> ```SQL
> --Setup SQL Agent Jobs to seed "nightly" sync of Interject data store
> EXEC [Setup].[ERP_InstallScript5_SetupJobs]
> ```
> **Step 4:** Go through the steps required for [Interject Application Setup - Data Connection](https://docs.gointerject.com/bApps/bFinancials/InitialDataLoad.html#steps-required-for-interject-application-setup-data-connection).
>
> **Step 5:** After following the Data Connection Setup, do an initial smoke test on all the stock reports, checking for drill, pull, and save functionality.
>
> **Step 6:** Contact Interject Support to request that your custom reports be migrated from "Test" company **Report Library** to your new "Live" company.
>
> **Step 7:** Review your Schedule to confirm Sync Jobs
> ![](/images/Config/SchedulerReportLib.png){: .center-image }
> ![](/images/Config/SchedulerTool.png){: .center-image }
>

### Option 2: Deploying A New Implementation From Scratch
This option involves installing an entirely new instance of Interject, as well as completing a new Initial Data Load. Once those are complete, you will have to manually "transfer" your Custom Rollups and Custom Reports from "Test" to "Live" environments.


#### Re-Deploy From Scratch
These steps repeat the Initial Install and Initial Data Load covered in the Install menu.  

> To Do
>
> **Step 1:** Complete all steps the [Data Tier Install](https://docs.gointerject.com/bApps/bFinancials/Technical-Install.html).
>
> **Step 2:** Next, complete all steps for the [Inital Data Load](https://docs.gointerject.com/bApps/bFinancials/InitialDataLoad.html#begin-data-load).
>
> **Step 3:** After completing both procedures above, do an initial smoke test on all the stock reports, checking for drill, pull, and save functionality.
>
> 

#### Transfer Custom Rollups and Report Templates

This details the transfer of Rollups, Templetes, and Reports from the "Test" company to the "Live" company. 

##### Custom Rollups

> To Do
>
> **Step 1:** Open Excel, locate the "Company" setting on the Interject Ribbon Menu, and switch to \<Your Test Company\>, or confirm you are already there. 
> ![](/images/Config/CompanyButton.png){: .center-image }
>
> **Step 2:** Use **Ctrl-Shift-L** to open the Interject Report Library, then go the **Configuration Manager Tool**.
> ![](/images/Config/ConfigMGR.png){: .center-image }
>
> **Step 3:** Click on **Setup/Review Rollups**
> ![](/images/Config/SetupRollups.png){: .center-image }
>
> **Step 4:** Drill into one of your custom rollups.
> ![](/images/Config/CustomRollup.png){: .center-image }
>
> **Step 5:** Now, clicking on **Company** again from the Interject Ribbon, switch back to <Your Live Company>.
>
> **Step 6:** With the rollup still open, hit **Ctrl-Shift-U** to save the report.
>
> **Step 7:** Switch back into \<Your Test Company\>, go to the **Configuration Manager Tool**, and repeat steps 3 through 5 for the remaining Rollups.
>
>

##### Custom Row Templates 

> To Do
>
> **Step 1:** Open Excel, locate the "Company" setting on the Interject Ribbon Menu, and switch to \<Your Test Company\>, or confirm you are already there. 
> ![](/images/Config/CompanyButton.png){: .center-image }
>
> **Step 2:** Use **Ctrl-Shift-L** to open the Interject Report Library, then go the **Configuration Manager Tool**.
> ![](/images/Config/ConfigMGR.png){: .center-image }
>
> **Step 3:** Click on **Setup/Review Row Report Templates**
> ![](/images/Config/SetupRowTemp.png){: .center-image }
>
> **Step 4:** Drill into one of your custom row templates.
> ![](/images/Config/CustomRowTemp.png){: .center-image }
>
> **Step 5:** Now, clicking on **Company** again from the Interject Ribbon, switch back to <Your Live Company>.
>
> **Step 6:** With the rollup still open, hit **Ctrl-Shift-U** to save the report.
>
> **Step 7:** Switch back into \<Your Test Company\>, go to the **Configuration Manager Tool**, and repeat steps 3 through 5 for the remaining Rollups.
>
>

##### Custom Reports 

> To Do
>
> **Step 1:** Open Excel, locate the "Company" setting on the Interject Ribbon Menu, and switch to \<Your Test Company\>, or confirm you are already there. 
> ![](/images/Config/CompanyButton.png){: .center-image }
>
> **Step 2:** Use **Ctrl-Shift-L** to open the Interject Report Library, then go the and open any of your custom reports.
> ![](/images/Config/OpenCustReport.png){: .center-image }
>
> **Step 3:** Now, save the report to a local folder.
>
> **Step 4:** Keeping the report open, click on **Company** and switch into your Live environment.
>
> **Step 5:** Now, clicking on **Company** again from the Interject Ribbon, switch back to \<Your Live Company\>.
>
> **Step 6:** With the report still open, follow from **Step 8 through the end** of the [Report Localization Instructions](https://docs.gointerject.com/bApps/bFinancials/Localize.html)
>
>
