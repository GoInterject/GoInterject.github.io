---
title: Publishing and Updating in the Report Library
filename: "PubReports.md"
layout: custom
keywords: [Report, Epicor, Accounts]
headings: ["Publishing and Updating Report Templates in the Report Library", "Updating Existing Report Templates"]
links: []
image_dir: "Financials-TemplateSave"
images: [{file: "ReportSave1", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "ReportSave2", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "ReportSave3", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "ReportSave4", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "ReportSave5", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "ReportSave6", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "UpdateReport1", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "UpdateReport2", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "UpdateReport3", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "UpdateReport4", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}]
description: Step by step guide on using Interject Financials - Publishing Epicor Enterprise financial report templates.
---

### Publishing and Updating Report Templates in the Report Library

Once you have finished creating a report template using the Interject Financials for Epicor Enterprise configuration manager, you can publish the report template to your Interject Report Library. Each report template you publish will be versioned, so that you can track changes. You can also set the status of report templates to **Dev**, **Test**, **Live**, or **Superseded**. Once set to live, all users in your organization with access to the Report Library will see and can use the report template through their Report Library.

In this example, we'll use a template created internally by Interject developers. However, the same process will be applied once you've finished making your own report template following the steps in other pages of this training section.


> To Do:
>
> **Step 1:** Hit **Ctrl-Shift-J** or the pull button, and click **Clear**
> ![Save Report Temp](/images/Financials-TemplateSave/ReportSave1.png){: .center-image }
>
> **Step 2:** With the data cleared, save the Excel file on the local machine, either on the desktop or in a folder you've specified for this purpose.
>
> **Step 3:** Now open the Report Library, either using **Ctrl-Shift-L** or the Report Library button on the Interject Ribbon. If you need to create a new folder for your published report, you can right click in the **Folders** section and add a new subfolder. Otherwise, right click in the **Report Links** section and choose **Create a New Link**.
> ![Save Report Temp](/images/Financials-TemplateSave/ReportSave2.png){: .center-image }
>
> **Step 4:** In the "Create New Link" window, type in "Link Name" the name you want for the report template in the library. You should also add a description at this point, especially if your report template is an updated version.
> ![Save Report Temp](/images/Financials-TemplateSave/ReportSave3.png){: .center-image }
>
> **Step 5:** Set the version to **Dev**, **Test**, **Live**, or **Superseded**. We use live in this example. You can also give the template a version name and version notes to document what changed. 
> - **Live:** Standard users can only see live reports, so only use this when the report is ready to be published.
> - **Test:** Test means that development is complete, but the report is still in testing.
> - **Dev:** In development by the report writer.
> - **Superseded:** A report that is no longer used but is still available to admin users for review.
> ![Save Report Temp](/images/Financials-TemplateSave/ReportSave4.png){: .center-image }
>
> **Step 6:** Choose the link path by clicking **Browse** and locating the Excel file you just saved.
> ![Save Report Temp](/images/Financials-TemplateSave/ReportSave5.png){: .center-image }
>
> **Step 7:** If you've created documentation for your report template, you can add a link to it here using either a web-link, a local or network file, a local folder, or a Windows process. Additionally, you can attach a local file path.
> ![Save Report Temp](/images/Financials-TemplateSave/ReportSave6.png){: .center-image }
>
> **Step 8:** Click **Save**.
>

### Updating Existing Report Templates

The process for updating existing report teplates is largely similar to saving entirely new templates. We'll begin with the BALCONSOL report open.

> To Do:
>
> **Step 1:** While still in the report template you just saved, click **Save As**, and give the file an updated version name, such as "BALCONSOL_v2.6.3".
>
> **Step 2:** Hit **Ctrl-Shift-L** or the Report Library button on the Interject Ribbon.
>
> **Step 3:** Right click on the version of the report you have updated, choose **Save Current Workbook", and then choose "Create New Version of "\[name of your report\]"".
> ![Save Report Temp](/images/Financials-TemplateUpdate/UpdateReport1.png){: .center-image }
>
> **Step 4:** In the "Create New Version" window, you will complete the same information as the steps above for saving a new report. The difference is that you will want to include an updated **Version Name" and description** to identify the updated report as separate from previous versions.
> ![Save Report Temp](/images/Financials-TemplateUpdate/UpdateReport2.png){: .center-image }
>
> **Step 5:** You will be prompted to convert any other **Live** versions of the report to **Superseded**. Click **Yes**.
> ![Save Report Temp](/images/Financials-TemplateUpdate/UpdateReport3.png){: .center-image }
>
> Your new report version will now be saved and available in the Report Library.
> ![Save Report Temp](/images/Financials-TemplateUpdate/UpdateReport4.png){: .center-image }

