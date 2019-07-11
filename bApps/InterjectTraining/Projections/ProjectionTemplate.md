---
title: Projection Template
layout: custom
keywords: [Training, Projections, Projection Template]
description: 
---

## Overview

**Purpose**: The Local Projections Template is used to save to a district's Projections for a given month. This template closely matches the Local Budget Template in design and function.

**Report Location**<br>
(Attach Report Location Image here)

**Filter Options**:

* **District** - *Required*. Individual district. Cannot use district ranges or groupings
* **YYYY-MM** - *Required*. Must be in YYYY-MM format
* **Currency** - *Optional*. Blank defaults to your home district currency. Other options are USD and CAD.<br><br>
[ *Retain Rows - Related Parameters (used in the pull)* ](#retain-rows-and-how-it-works)
* **Retain Rows** - *Required*. Drop-down filter includes *Yes*, *No-Show Last Saved*, *No-Show Prior Bud*. If *Yes*, the Input columns will not clear on the pull.
* **Retain Comments** - *Required*. Drop-down filter includes *Yes* and *No*. If *Yes*, pulling on the report will not clear comments not yet saved to the database.
* **Insert at End** - *Required*. Drop-down filter includes *Yes* and *No*. If *Yes* and **Retain Rows** is also *Yes*, then new accounts get added at the bottom of their grouping.<br><br>
[ *Summary and Detail Accounts - Related Parameters* ](#summary-and-detail-level-accounts)
* **Insert By Full Acct** - *Required*. Used in the pull. Drop-down filter includes *Yes* and *No*. For *No*, new accounts are aggregated at the summary level and dropped in.
* **Zero Out Missing Accts** - *Required*. Used in the save. Drop-down filter includes *Yes* and *No*. For *Yes*, accounts missing from the template are zeroed out. For *No*, missing accounts will keep their amounts, and any Summary level accounts are offset to include the missing accounts automatically.

![](/images/WCNTraining/Projections/ProjectionTemplate_FullView.png)

## Input Field Explanations

### Retain Rows and how it works

With **Retain Rows** on *Yes*, any inputs in the Input columns will remain when the template is refreshed, or even if the report is cleared. If it is *No*, the Input columns will copy the Projections saved to either the current year month or the last month (depending on the alternative option).

For an example with **Retain Rows** *Yes*, the screenshot below shows a formula used on the *36000-600-00* account.

![](/images/WCNTraining/Projections/ProjectionTemplate_RetainRowsBeforeClear.png)

Clear the report, and afterwards notice that not only have all of the rows remained, but the formula is still there as well.

![](/images/WCNTraining/Projections/ProjectionTemplate_RetainRowsAfterClear.png)

Setting **Retain Comments** to *Yes* will keep any comments saved in the template, even if there are different comments saved in the database.

If a new account is added to the Template with **Retain Rows** set to *Yes*, the setting for **Insert at End** dictates whether the account gets placed normally, in order, or gets inserted at the end.

For example, if *36002-000-00* is added to the Template while **Insert at End** is set to *No*, the added account is placed between the 36000 and 36009 accounts.

![](/images/WCNTraining/Projections/ProjectionTemplate_InsertAtEndNo.png)

Otherwise, if **Insert at End** is set to *Yes*, the added account is at the bottom. Use this if you use formulas, so that newly added accounts do not interfere with them.

![](/images/WCNTraining/Projections/ProjectionTemplate_InsertAtEndYes.png)

>**Things to Remember**
>* After the first pull, **Retain Rows** will automatically be set to *Yes*, to preserve your file changes.

### Summary and Detail level accounts

A new feature to the Projections Template is the ability to pull/save to Detail and Summary level accounts at the same time.

#### Pulling Summary and Detail levels together
On the pull, the **Insert By Full Acct** drop-down option dictates if the missing accounts are added on the Summary or Detail level. When **Retain Rows** is set to *Yes*, you can pull in accounts on a different level than the ones you already have in your template.

In the screenshot below, we see five account combinations for the 36009 account.

![](/images/WCNTraining/Projections/ProjectionTemplate_SummaryDetail_PullStart.png)

With **Retain Rows** set to *Yes* and **Insert By Full Acct** set to *No*, delete the 36009-000-00 and 36009-600-00 rows.

![](/images/WCNTraining/Projections/ProjectionTemplate_SummaryDetail_SummaryPrep.png)

Now when we pull, the two detail rows 36009-000-00 and 36009-600-00 are summarized into one row, with the account header of 36009 alone. 36009-000-00 had $1,000 amounts for all months, and 36009-600-00 had $2,000 for all months. Together they have $3,000 for all months.

![](/images/WCNTraining/Projections/ProjectionTemplate_SummaryDetail_SummaryPull.png)

>**Things to Remember**<br>
>For this to work, **Retain Rows** MUST be set to *Yes*. Otherwise, if **Retain Rows** is set to *No* and you pull, ALL accounts will be pulled on the Detail Level.

#### Saving Summary and Detail levels together

When saving with Summary and Detail level accounts on the same template, the Summary level accounts are saved to the *000-00* version of the summarized account. Depending on the **Zero Out Missing Accts** setting, the Detail level accounts already in the database will either be zeroed out or remain unaltered.

Using the example accounts from above, let's update the summarized account for 36009 to $3,500 for all months.

![](/images/WCNTraining/Projections/ProjectionTemplate_SummaryDetailSaveStart.png)

First we save with **Zero Out Missing Accts** set to *No*, and pull in all detail rows by setting **Retain Rows** to *No* and **Insert By Full Acct** to *Yes*.

![](/images/WCNTraining/Projections/ProjectionTemplate_SummaryDetail_ZeroOutNo.png)

The Projection saved to 36009-000-00 is the *offset* of $3,500 per month (summarized amount) and $2,000 per month for 36009-600-00 (amounts in database). This updated the $1,000 in the database 36009-000-00 to $1,500, so that the summarize amount matches what was saved AND preserves the amount already assigned to 36009-600-00.

If we had set **Zero Out Missing Accts** to *Yes* instead, the pull on detail would have looked like example below.

![](/images/WCNTraining/Projections/ProjectionTemplate_SummaryDetail_ZeroOutYes.png)

Now 36009-000-00 has the full $3,500 for each month, and 36009-600-00 has been zeroed out because it was not in the template.

>**Things to Remember**
>* If you delete other accounts from the template, they will be zeroed out as well, if **Zero Out Missing Accts** is set to *Yes* (even if they do not have a summary level account present in the template).
>* When saving with a Summary level account (only Acct is present), you cannot also save to the same account with *000-00* included. The save thinks the two accounts are the same, and they will be marked as duplicates.

## Dynamic Projection Columns

Depending on the Projection fiscal period, the number of months you project to can change. For the majority of the fiscal period, it will be three months. For August you project out to five months, and for September it is four months.

The template will update automatically based on the Year Month when you pull on the tool. Notice the screenshots below, which show the last saved data changing the columns dynamically (this applies to the other sections of the tool as well).

![](/images/WCNTraining/Projections/ProjectionTemplate_3Months.png)
![](/images/WCNTraining/Projections/ProjectionTemplate_4Months.png)
![](/images/WCNTraining/Projections/ProjectionTemplate_5Months.png)

## The Autocalcs

The majority of accounts in your template will be marked **Manual Input** in the *Proj Method* column (column J). Some of the other accounts will have something different in this column and are considered **Autocalcs**.

![](/images/WCNTraining/Projections/ProjectionTemplate_Autocalcs.png)

There are many different types of Autocalcs, but it's important to know that you cannot edit them with the **Projections Template**. These accounts are managed by Corporate. Notice also that any Manual Input account is highlighted yellow, and the Autocalcs are grayed out.

>**Autocalc Handling**<br>
>It is best practice to set your Autocalc input columns to equal the last saved columns from Interject. That way your your inputs will automatically update when assumptions are changed, and your EBITDA will tie out.

## Do I have security rights to Save from the Projections Template?

To check whether you can save to the Projections Template, please see the [ Tools Controlled by the Control Center ](/bApps/InterjectTraining/Budget/ControlCenterSecurity.html#projections-tools-and-the-control-center) page.

## Common Save Errors

![](/images/WCNTraining/Projections/ProjectionTemplate_Error_LockLevel.png)

*The district is locked at a level higher than what you have access to. Work with your supervisor to unlock the file to your level.*


<button class="collapsible">Other Possible Save Errors</button>
<div markdown="1" class="panel">
![](/images/WCNTraining/Projections/ProjectionTemplate_Error_LastPullFor.png)

*You last pulled for a district different from the one you are trying to save to. You need to repull for the district you want to save for with Retain Rows set to No. Be sure to make a copy to transfer your notes/amounts over.*
        
___
![](/images/WCNTraining/Projections/ProjectionTemplate_Error_DistrictRequired.png)

*You need to use a valid District in the District parameter.*
       
___
![](/images/WCNTraining/Projections/ProjectionTemplate_Error_YearMonthRequired.png)

*The YearMonth is required and must be in the YYYY-MM format.*

___
![](/images/WCNTraining/Projections/ProjectionTemplate_Error_MissingColumns.png)

*Your local template is missing some of the required columns. Get a fresh copy of the template for the library, or reach out to support to fix your template.*

___
![](/images/WCNTraining/Projections/ProjectionTemplate_Error_InvalidAccount.png)

*The Account on the specified row is not a valid Account.*

___
![](/images/WCNTraining/Projections/ProjectionTemplate_Error_InvalidSyst.png)

*The Syst on the specified row is not a valid Syst.*
        
___
![](/images/WCNTraining/Projections/ProjectionTemplate_Error_InvalidSbst.png)

*The Sbst on the specified row is not a valid Sbst.*

___
![](/images/WCNTraining/Projections/ProjectionTemplate_Error_NonumericAmount.png)

*The amount in the provided column for the given row is non-numeric and needs to be fixed (Proj12 = Bud12)*
        
___
![](/images/WCNTraining/Projections/ProjectionTemplate_Error_ExponentialAmount.png)

*There is a rounding error in the provided column for the given row, and needs to be fixed (Proj12 = Bud12)*

___
![](/images/WCNTraining/Projections/ProjectionTemplate_Error_Duplicates.png)

*Two of your rows have the same Account combination listed. It could be that one row is on the summarized level and you have the detail version 000-00 as well.*
        
___
![](/images/WCNTraining/Projections/ProjectionTemplate_Error_BrokenFormula.png)

*There is a broken formula in the provided column for the given row, and needs to be fixed.*
</div>