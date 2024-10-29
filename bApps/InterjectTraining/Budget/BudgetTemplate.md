---
title: Budget Template
filename: "BudgetTemplate.md"
layout: custom
keywords: [Training, Budget, Budget Template]
headings: ["Overview", "Filters", "Template Setup", "Build Based On", "Account Level", "Other Required Filters", "Additional Filters", "Input Field Explanations", "Base Year and Fincube", "How Templates Work", "Summary and Detail level accounts", "Pulling Summary and Detail levels together", "Saving Summary and Detail levels together", "The Autocalcs", "Do I have security rights to Save from the Budget Template?", "After Corp Cutoff and after BOD", "After Corp Cutoff", "After BOD", "Common Save Errors"]
links: ["#base-year-and-fincube", "/bApps/InterjectTraining/Budget/ControlCenterSecurity.html#budget-tools-and-the-control-center", "/bApps/InterjectTraining/Budget/BudgetChangeQuery_UnsyncedChanges.html", "/bApps/InterjectTraining/Budget/BudgetChangeQuery_Summary.html", "/bApps/InterjectTraining/Budget/BudgetChangeQuery_UnsyncedChanges.html", "/bApps/InterjectTraining/Budget/BudgetChangeQuery_Summary.html"]
image_dir: "WCNTraining"
images: [
	{file: "Budget/FilterOptions1", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/FilterOptions_BuildBaseOn", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/FilterOptions_AccountLevel", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/FilterOptions2", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/FilterOptions3", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_BaseYear01", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_BaseYear02", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_InsertAtEndNo", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_SummaryDetailPullStart", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_SummaryDetail_SummaryPull", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_SummaryDetailSaveStart", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_SummaryDetail_ZeroOutNo", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_SummaryDetail_ZeroOutYes", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_Autocalcs", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetUpload_CCAfterCorpCutoff", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_AfterCorpCutoffSave", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_AfterCorpCutoff", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_AfterCorpCutoffBudChangeQuery", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_Error_TemplateOutofDate", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_Error_LockLevel", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_Error_LastPullFor", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_Error_DistrictRequired", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_Error_YearMonthRequired", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_Error_AfterCorpCutoff", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_Error_MissingColumns", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_Error_InvalidAccount", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_Error_InvalidSyst", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_Error_InvalidSbst", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_Error_NonumericAmount", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_Error_ExponentialAmount", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_Error_Duplicates", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Budget/BudgetTemplate_Error_BrokenFormula", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}
	]
description: This is the primary tool used for managing Budgets. This tool can be downloaded and customized in your local environment.
---

## Overview

**Purpose**: This is the primary tool used for managing Budgets. This tool can be downloaded and customized in your local environment.

## Filters
### Template Setup
The **Build Based On** and **Account Level** filters are used to set up the template. They determine where initial data is pulled from and at what level the district will be budgeted. Once data is pulled, filters will be hidden from the report. 

![](/images/WCNTraining/Budget/FilterOptions1.png)


#### Build Based On 
*Required*. There is a drop-down filter that includes *Retain User Input*, *Last Saved/Upload*, *Base Year* and "Reset(Clear All Data)". This parameter controls what data is pulled and what is cleared on a pull in the **YYYY Budget Input** section. Each selection is explained in detail below.

![](/images/WCNTraining/Budget/FilterOptions_BuildBaseOn.png)

* **Retain User Input** - After the initial run/pull, the **Build Based On** parameter will automatically be set to *Retain User Input*, preserving any file changes. Values in the  **YYYY Budget Input** section and formulas entered by the user will not be overridden. This is the default parameter after an initial run/pull.    
* **Last Saved/Upload** - This will bring the last saved amounts into the  **YYYY Budget Input** section. It will replace and/or clear values and formulas that haven't been saved. 
* **Base Year** - This will bring in the "Base Year" amounts just as the **YYYY Actuals & Projections** section does into the  **YYYY Budget Input** section. It will replace and/or clear any values and formulas that haven't been saved. 
* **Reset (Clear All Data)** - This will clear all data related to the distict, including from the budget user input section. When running this option, select "Clear" in the "Pull Datal Control" window. 
 
#### Account Level 

*Required*. Used in pulling data to determine the default account level at which the detail is summarized. The drop-down filter includes the choice of *Summary (xxxxx)* or *Full GL Account (xxxxx-xxx-xx)*. 

![](/images/WCNTraining/Budget/FilterOptions_AccountLevel.png)

* **Summary (xxxxx)** will summarize detail at the natural account level. 
* **Full GL Account (xxxxx-xxx-xx)** will show Account, System, and Sub-System. 

### Other Required Filters 

The following additional *required* and *optional* filters are described below:  

![](/images/WCNTraining/Budget/FilterOptions2.png)

* **District** - *Required*. Designates the individual district. You cannot use district ranges or groupings.
* **Budget Year** - *Required*. The year currently being budgeted for.
* [**Base Year**](#base-year-and-fincube) - *Required*. Used in the pull. The drop-down filter ranges from *Aug Proj -> Dec Act*<br><br>

### Additional Filters

![](/images/WCNTraining/Budget/FilterOptions3.png)

* **Retain Comments** - *Required*. This drop-down filter includes *Yes* and *No*. If you choose *Yes*, pulling on the report will not clear unsaved comments.
* **Currency** - *Optional*. Blank defaults to your home district currency. Other options are USD and CAD.
* **Insert at End** - *Required*. Drop-down filter includes *Yes* and *No*. If set to *Yes*, new accounts get added at the bottom of their grouping.<br><br>

## Input Field Explanations

### Base Year and Fincube

The **Base Year** drop-down filter changes how Actuals and Projections for the current year are pulled in from Fincube. For example, the screenshot below shows the *Aug Proj* option, which pulled in Actuals from January -> July, and Projections from August -> December.

![](/images/WCNTraining/Budget/BudgetTemplate_BaseYear01.png)

If we change the **Base Year** to *Aug Act*, August will pull in as Actual instead.

![](/images/WCNTraining/Budget/BudgetTemplate_BaseYear02.png)


## How Templates Work

When coming into the template, users will have the option to set the starting point by selecting how data is popuated into **YYYY Budget Inputs**, as well as the Account Level at which the detail is populated. Once the report is pulled these filter options will no longer be avalible. 

If a new account is added to the Template, how **Insert at End** is set dictates whether the account gets placed normally, in order, or gets inserted at the end.

For example, if *50045-600-00* is added to the Template while **Insert at End** is set to *No*, it is placed between the 50036 and 50050 accounts.

![](/images/WCNTraining/Budget/BudgetTemplate_InsertAtEndNo.png)



### Summary and Detail level accounts

A new feature to the Budget Template is the ability to pull/save to Detail and Summary level accounts at the same time.

#### Pulling Summary and Detail levels together
Since rows are retained by default, even after you've chosen the *Summary* template you can still add detail rows. Simply insert additional rows beneath the account, copy the row to include the formulas and enter the system and subsystem values in thier respective columns. The data will populate when the report is pulled again.

In the screenshot below, we see four account combinations for the 36009 account. And after the data is pulled, we see those rows populated

![](/images/WCNTraining/Budget/BudgetTemplate_SummaryDetailPullStart.png)

<!-- Now when we pull, the two detail rows 36009-000-00 and 36009-600-00 are summarized into one row, with the account header of 36009 alone. 36009-000-00 had $1,000 amounts for all months, and 36009-600-00 had $2,000 for all months. Together they have $3,000 for all months. -->

![](/images/WCNTraining/Budget/BudgetTemplate_SummaryDetail_SummaryPull.png)


#### Saving Summary and Detail levels together

When saving with Summary and Detail level accounts on the same template, the Summary level accounts are saved to the *000-00* version of the summarized account. Any missing detail level accounts already in the database will be zeroed out.

<!-- Using the example accounts from above, let's update the summarized account for 36009 to $3,500 for all months.

![](/images/WCNTraining/Budget/BudgetTemplate_SummaryDetailSaveStart.png)

First we save with **Zero Out Missing Accts** set to *No*, and pull in all detail rows by setting **Retain Rows** to *No* and **Insert By Full Acct** to *Yes*.

![](/images/WCNTraining/Budget/BudgetTemplate_SummaryDetail_ZeroOutNo.png)

The Budget saved to 36009-000-00 is the *offset* of $3,500 per month (summarized amount) and $2,000 per month for 36009-600-00 (amounts in database). This updated the $1,000 in the database 36009-000-00 to $1,500, so that the summarize amount matches what was saved AND preserves the amount already assigned to 36009-600-00.

If we had set **Zero Out Missing Accts** to *Yes*, the pull on detail would have looked like this instead.

![](/images/WCNTraining/Budget/BudgetTemplate_SummaryDetail_ZeroOutYes.png)

Now 36009-000-00 has the full $3,500 for each month, and 36009-600-00 has been zeroed out because it was not in the template. -->

>**Things to Remember**
>* If you delete other accounts from the template, they will be zeroed out as well (even if they do not have a summary level account present in the template).
>* When saving with a Summary level account (only Acct is present), you cannot also save to the same account with *000-00* included. The save thinks the two accounts are the same, and they will be marked as duplicates.

## The Autocalcs

The majority of accounts in your template will be marked **Manual Input** in the *Bud Method* column (column J). Some of the other accounts will have something different in this column and are considered **Autocalcs**.

![](/images/WCNTraining/Budget/BudgetTemplate_Autocalcs.png)

There are many different types of Autocalcs, but the main thing to know is that you cannot edit them with the **Budget Template**. These accounts are managed by Corporate. Notice also that any Manual Input account is highlighted yellow, and the Autocalcs are grayed out.

>**Autocalc Handling**<br>
>It is best practice to set your Autocalc input columns to equal the last saved columns from Interject. That way your your inputs will automatically update when assumptions are changed, and your EBITDA will tie out.

## Do I have security rights to Save from the Budget Template?

To find if you can save to the Budget Template, please check out the [Tools Controlled by the Control Center](/bApps/InterjectTraining/Budget/ControlCenterSecurity.html#budget-tools-and-the-control-center) page.

## After Corp Cutoff and after BOD

### After Corp Cutoff
If you save to Budget **After Corp Cutoff**, the numbers will still be updated in Target Center 2.0. However, they will not be synced through to Interject.

In this example, the *Corp Cutoff* date in Control Center is set to 11/3/2018.

![](/images/WCNTraining/Budget/BudgetUpload_CCAfterCorpCutoff.png)

We then try and upload a change to Budget using the **Budget Template** tool (after this date), and get the following popup message.

<!-- ![](/images/WCNTraining/Budget/BudgetTemplate_AfterCorpCutoffSave.png) -->
![](/images/WCNTraining/Budget/BudgetTemplate_AfterCorpCutoff.png)

Notice our changes have been saved to Target Center 2.0, but they are not yet synced to Interject. Once the *Corp Cutoff* date is set to a Date/Time after our change or BOD, this change will be synced to Interject.

We can use the the new [UnsyncedChanges](/bApps/InterjectTraining/Budget/BudgetChangeQuery_UnsyncedChanges.html) in the [Budget Change Query Tool](/bApps/InterjectTraining/Budget/BudgetChangeQuery_Summary.html) tab to see our changes in Target Center 2.0.

![](/images/WCNTraining/Budget/BudgetTemplate_AfterCorpCutoffBudChangeQuery.png)

### After BOD
Once **BOD** for a Budget Year has been created, any save from the **Budget Template** will not automatically sync to Interject again, just like *After Corp Cutoff*. While it is not in Interject, it is in Target Center 2.0 and can be checked using the [UnsyncedChanges](/bApps/InterjectTraining/Budget/BudgetChangeQuery_UnsyncedChanges.html) tab in the [Budget Change Query Tool](/bApps/InterjectTraining/Budget/BudgetChangeQuery_Summary.html). 

Once Corporate has versioned your change, the Budget amount will be sycned through to Interject.

## Common Save Errors

![](/images/WCNTraining/Budget/BudgetTemplate_Error_TemplateOutofDate.png)

*The template you are using is not current. You need to get a new template from the Report Library.*

___
![](/images/WCNTraining/Budget/BudgetTemplate_Error_LockLevel.png)

*The district is locked at a level higher than what you have access to. Work with your supervisor to unlock the file to your level.*


<button class="collapsible">Other Possible Save Errors</button>
<div markdown="1" class="panel">
![](/images/WCNTraining/Budget/BudgetTemplate_Error_LastPullFor.png)

*You last pulled for a district different from the one you are trying to save to. You need to repull for the district you want to save for with Retain Rows set to No. Be sure to make a copy to transfer your notes/amounts over.*
        
___
![](/images/WCNTraining/Budget/BudgetTemplate_Error_DistrictRequired.png)

*You need to use a valid District in the District parameter.*
       
___
![](/images/WCNTraining/Budget/BudgetTemplate_Error_YearMonthRequired.png)

*The YearMonth is required and needs to be in the YYYY-MM format.*

___
![](/images/WCNTraining/Budget/BudgetTemplate_Error_AfterCorpCutoff.png)

*Your save updated Target Center 2.0 but is not synced to Interject yet. Once Corp Cutoff is updated to after your change or BOD is created, it will then be synced to Interject.*
        
___
![](/images/WCNTraining/Budget/BudgetTemplate_Error_MissingColumns.png)

*Your local template is missing some of the required columns. Get a fresh copy of the template for the library, or reach out to support to fix your template.*

___
![](/images/WCNTraining/Budget/BudgetTemplate_Error_InvalidAccount.png)

*The Account on the specified row is not a valid Account.*

___
![](/images/WCNTraining/Budget/BudgetTemplate_Error_InvalidSyst.png)

*The Syst on the specified row is not a valid Syst.*
        
___
![](/images/WCNTraining/Budget/BudgetTemplate_Error_InvalidSbst.png)

*The Sbst on the specified row is not a valid Sbst.*

___
![](/images/WCNTraining/Budget/BudgetTemplate_Error_NonumericAmount.png)

*The amount in the provided column for the given row is non-numeric and needs to be fixed (Proj12 = Bud12)*
        
___
![](/images/WCNTraining/Budget/BudgetTemplate_Error_ExponentialAmount.png)

*There is a rounding error in the provided column for the given row, and needs to be fixed (Proj12 = Bud12)*

___
![](/images/WCNTraining/Budget/BudgetTemplate_Error_Duplicates.png)

*Two of your rows have the same Account combination listed. It could be that one row is on the summarized level and you have the detail version 000-00 as well.*
        
___
![](/images/WCNTraining/Budget/BudgetTemplate_Error_BrokenFormula.png)

*There is a broken formula in the provided column for the given row, and needs to be fixed (Period 1 = Bud1)*
</div>
