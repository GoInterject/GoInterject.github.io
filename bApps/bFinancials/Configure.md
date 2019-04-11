---
title: Configure
layout: custom
keywords: [Report, Epicor, Accounts]
description: Step by step guide on setting up new and pre-packaged reports in the Interject for Financials App for Epicor.
---

Interject Financials - Epicor offers a simple, step-by-step configuration tool to set up and test the monthly import schedule as well as the configuration of financial reports.

### Using Initial Config Tool for Financial Reporting

##### Setup Year Name
> To-do
>
> **Step 1:** While logged into Interject, open the configuration tool from the report library. 
>
> **Step 2:** In the configuration tool, change all year names where needed in the table.
>
> **Step 4:** Hit Ctrl-Shift-U, or the Save button in the Interject ribbon, to save back the configuration.

##### Setup Segments
> To-do
>
> **Step 1:** In the Segment tab of the configuration tool, you can change:
> - Segment Names
> - Enabled/Disabled status
> - Natural Acct Status
>
> **Step 2:** Hit Ctrl-Shift-U to save configuration, or hit Save on the Interject ribbon.

### Account Rollup Management
There are a number of Account Rollup tabs to manage account aggregation in Interject Financials - Epicor. Governed Rollups are cesure, tested, and published with validated field definitions by system admins ro implementers.

**PL1:** In the PL1 Rollup tab, change the account configurations as needed and hit Ctrl-Shift-U to save back the configuration. \(Note: Names used for detail code, rollup and summary section must all be unique as a group.\)

**BS1:** Configure BS1 using the same method described for PL1, then save back the configuration using Ctrl-Shift-U.

##### Governed Account Rollups
Each governed Account Rollup is defined by account numbers set by admins or implementers and published to the report library. As long as there is a governing definition in place for a given rollup, that report is secure and validated. Governing definitions can be changed by admins with secured access, but they will always pass through the validation/testing process before being published and available to users.
	
##### Ad Hoc Account Rollups
Admins and users both can create account rollups with for any account or transaction detail using the ad hoc rollup configuration tool. Simply create detail codes, order, and definitions if your report will be governed. Save the configuration using Ctrl-Shift-U.

##### Other Rollups
Other rollups can be easily created using the same process in the Other Rollups tab. For example, you can roll up by region, consol, or cost center. These will be non-natural segments, and they will not be created with governing definitions. As a result, they may not be supported.


### Converting FRx Row Definitions
Interject provides a custom template according to the Epicor Segment Assessment. This is called the Report Conversion Template. To convert your FRx Row definitions follow the steps below:
> To-do
>
> **Step 1:** In the Initial Row Template Mgr tab, use Ctrl-Shift-K or the Drill button to add or edit new templates.
>
> **Step 2:** To delete, set the Action column drop-down to “Delete”.
>
> **Step 4:** Hit Ctrl-Shift-U to save and confirm changes
	
In the Row Template Detail tab, you can configure the row template detail. Note that natural acct segments are required. Once configured, hit Ctrl-Shift-U to save. (For easy reference, select an FRx row catalog and hit Ctrl-Shift-J to pull. Be sure to save your work beforehand.)

After configuring and saving your row templates, click the button “Click for report Template” and a report template will be generated. You can adjust this template further as needed, and save it back using Ctrl-Shift-U. Then follow the localization steps to publish the report in the Report Library.
