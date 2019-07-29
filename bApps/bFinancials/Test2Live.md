---
title: Moving From Test to Live
layout: custom
keywords: [Report, Epicor, Accounts]
description: Step by step guide on converting reports in test environments to reports in live environments.
---
There are two options available when moving your Interject Financials report templates and roll ups from a test environment to the live environment, where your users can interact with them.

### Option 1: Moving the Entire Database

> To Do
>
> **Step 1:** Create a backup of the "Test" database and restore it on the "Live" server.
>
> **Step 2:** To reapply security to the live DB, execute the **Interject_SetupScript1_Security** stored procedure, seen below.
> ```SQL
> EXEC [Custom].[Interject_SetupScript1_Security]
>       @MasterEpicorDatabase = '<Epicor Controlling Database Name>'
>      ,@CertificatePassword = 'myPassword1234'
> ```
> **Step 3:** Execute **ERP_InstallScript5_SetupJobs**, as seen below, to create sync jobs
> ```SQL
> --Setup SQL Agent Jobs to seed "nightly" sync of Interject data store
> EXEC [Custom].[ERP_InstallScript5_SetupJobs]
> ```
> **Step 4:** Go through the steps required for [Interject Application Setup - Data Connection](https://docs.gointerject.com/bApps/bFinancials/InitialDataLoad.html#steps-required-for-interject-application-setup---data-connection).
>
> **Step 5:** After following the Data Connection Setup, do an initial smoke test on all the stock reports, checking for drill, pull, and save functionality.
>
> **Step 6:** Contact Interject Support to request that your custom reports be migrated from "Test" comapany **Report Library** to your new "Live" company.
>
> **Step 7:** Review your Schedule to confirm Sync Jobs
> ![](/images/Config/SchedulerReportLib.png){: .center-image }
> ![](/images/Config/SchedulerTool.png){: .center-image }
>

### Option 2: Deploying A New Implementation From Scratch
This option involves installing an entirely new instance of Interject, as well as completing a new Initial Data Load. Once those are complete, you will have to manually "transfer" your Custom Rollups and Custom Reports from test to live environments.


#### Re-Deploy From Scratch

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
> **Step 6:** With the report still open, follow from **Step 8 through the end** of the [Report Localization Instructions](http://127.0.0.1:4000/bApps/bFinancials/Localize.html)
>
>