---
title: Configure
filename: "Configure.md"
layout: custom
keywords: [Report, Epicor, Accounts]
headings: ["Schedule Manager", "Data Upload Tool", "Use Initial Config Tool to Perform the Initial Setup", "While logged into Interject, open the configuration tool from the report library.", "Navigate from the Welcome Screen through the initial steps", "Setup/Review Year Name", "Setup/Review Segments", "Account Rollup - Activate Seeded DEMO Config", "Governed Account Rollups", "Ad Hoc Account Rollups", "Other Rollups", "Converting FRx Row Definitions"]
links: ["/images/Config/Scheduler.png", "/images/Config/UploadTool.png", "/images/Config/ConfigReport.png", "/images/Config/ConfigWelcome.png", "/images/Config/YearNames.png", "/images/Config/ConfirmYears.png", "/images/Config/YearNames.png", "/images/Config/SegmentSetup.png", "/images/Config/RollUpRev.png", "/images/Config/RollupMg.png", "/images/Config/RollupVal.png", "/images/Config/PLVal.png"]
image_dir: "Config"
images: [
	{file: "Scheduler", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "UploadTool", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "ConfigReport", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "ConfigWelcome", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "YearNames", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "ConfirmYears", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "YearNames", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SegmentSetup", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "RollUpRev", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "RollupMg", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "RollupVal", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "PLVal", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}
	]
description: Step by step guide on setting up new and pre-packaged reports in the Interject for Financials App for Epicor Enterprise.
---

Interject Financials - Epicor Enterprise offers a simple, step-by-step configuration tool to set up and test the monthly import schedule as well as the configuration of financial reports.

#### Schedule Manager
Set up and manage active Scheduler jobs
> ![reportlib config](/images/Config/Scheduler.png){: .center-image }

#### Data Upload Tool
Use to upload budget data if required
> ![reportlib config](/images/Config/UploadTool.png){: .center-image }

### Use Initial Config Tool to Perform the Initial Setup

#### While logged into Interject, open the configuration tool from the report library. 
> ![reportlib config](/images/Config/ConfigReport.png){: .center-image }

#### Navigate from the Welcome Screen through the initial steps
> ![reportlib config](/images/Config/ConfigWelcome.png){: .center-image }

##### Setup/Review Year Name
> To-do
>
> **Step 1:** Select "Review Year Names Link". 
> ![reportlib config](/images/Config/YearNames.png){: .center-image }
>
> **Step 2:** Review and approve year names.
> **Note:** This is a one time setup and must be done before using the reporting. Once approved it cannot be changed.
> ![reportlib config](/images/Config/ConfirmYears.png){: .center-image }
> - Verify all years expected to be part of initial data load  have a “yes”, if not contact Interject
> - Optional: Change the “Year Name” to be more specific to client requirements. This will impact user filters and parameters used in reporting
> - Select “yes” from approved dropdown 
> - Hit Ctrl-Shift-U, or the Save button in the Interject ribbon, to save and approve configuration.


##### Setup/Review Segments
> To-do
>
> **Step 1:** Select the "Review Segments" link
> ![reportlib config](/images/Config/YearNames.png){: .center-image }
>
> **Step 2:** Review and approve Segment setup.
> **Note:** This is a one time setup and must be done before using the reporting. Once approved it cannot be changed.
>
> ![reportlib config](/images/Config/SegmentSetup.png){: .center-image }
> - Verify all segments are part of client Epicor Enterprise setup; if incorrect, contact Interject. This will be referenced in other setups describing how to Localize reports.
> - Optional: Change the “Segment Display Name” to be more specific to client requirements. This will impact user filters and parameters used in reporting.
> - Select “yes” from approved dropdown
> - Hit Ctrl-Shift-U, or the Save button in the Interject ribbon, to save & approve.

### Account Rollup - Activate Seeded DEMO Config
Account Rollups are important to ensuring the “Control” and “Validity” of the mappings required in Financial reporting sections. Interject for Financials - Epicor Enterprise provides two Seeded Rollups as samples of a configuration that can be used in initial client demos or other functions to illustrate the recommended use. They can be leveraged as a “reporting” control while building reports and can additionally support client demos or other preliminary reporting requirements. These seeded rollups are automatically generated using the Account Type mappings in the Epicor Enterprise client GL.

> To Do
>
> **Step 1:** Select the "Setup/Review Rollups" link
> ![reportlib config](/images/Config/RollUpRev.png){: .center-image }
>
> **Step 2:** In the Account Rollup Manager tab, select the BS_DEMO link
> ![reportlib config](/images/Config/RollupMg.png){: .center-image }
>
> **Step 3:** In the next screen, hit Ctrl-Shift-U, or the Save button in the Interject ribbon, after verifying Summary Message is "Rollup Validated - No Warnings"
> ![reportlib config](/images/Config/RollupVal.png){: .center-image }
>
> **Step 4:** Go back to the "Rollup Manager" tab and select the "PL_Demo" link
>
> **Step 5:** Hit Ctrl-Shift-U, or the Save button in the Interject ribbon, after verifying Summary Message is "Rollup Validated - No Warnings"
>  ![reportlib config](/images/Config/PLVal.png){: .center-image }
>


<!--
**PL1:** In the PL1 Rollup tab, change the account configurations as needed and hit Ctrl-Shift-U to save back the configuration. \(Note: Names used for detail code, rollup and summary section must all be unique as a group.\)

**BS1:** Configure BS1 using the same method described for PL1, then save back the configuration using Ctrl-Shift-U.

##### Governed Account Rollups
Each governed Account Rollup is defined by account numbers set by admins or implementers and published to the report library. As long as there is a governing definition in place for a given rollup, that report is secure and validated. Governing definitions can be changed by admins with secured access, but they will always pass through the validation/testing process before being published and available to users.
	
##### Ad Hoc Account Rollups
Admins and users both can create account rollups with for any account or transaction detail using the ad hoc rollup configuration tool. Simply create detail codes, order, and definitions if your report will be governed. Save the configuration using Ctrl-Shift-U.

##### Other Rollups
Other rollups can be easily created using the same process in the Other Rollups tab. For example, you can roll up by region, consol, or cost center. These will be non-natural segments, and they will not be created with governing definitions. As a result, they may not be supported.


### Converting FRx Row Definitions
Interject provides a custom template according to the Epicor Enterprise Segment Assessment. This is called the Report Conversion Template. To convert your FRx Row definitions follow the steps below:
> To-do
>
> **Step 1:** In the Initial Row Template Mgr tab, use Ctrl-Shift-K or the Drill button to add or edit new templates.
>
> **Step 2:** To delete, set the Action column drop-down to “Delete”.
>
> **Step 4:** Hit Ctrl-Shift-U to save and confirm changes
	
In the Row Template Detail tab, you can configure the row template detail. Note that natural acct segments are required. Once configured, hit Ctrl-Shift-U to save. (For easy reference, select an FRx row catalog and hit Ctrl-Shift-J to pull. Be sure to save your work beforehand.)

After configuring and saving your row templates, click the button “Click for report Template” and a report template will be generated. You can adjust this template further as needed, and save it back using Ctrl-Shift-U. Then follow the localization steps to publish the report in the Report Library.
 -->
