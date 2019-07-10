---
title: Control Center
layout: custom
keywords: [Training, Budget, Control Center]
description: 
---

## Overview

**Purpose**: This tool controls who has ability to save to Budgets and when the data will flow from the Budget Module into Interject. It also controls the Projections and Capital lock levels.

**Report Location**<br>
(Attach Report Location Image here)

**Filter Options**:

* **District(s)** - *Optional*. Blank defaults to show all districts you have rights to. It can be individual district, district range, or groupings
* **Year Month** - *Optional*. Blank defaults to the current Year-Month. Must be in YYYY-MM format

![](/images/WCNTraining/Budget/ControlCenter_FullView.png)

## Accessing Templates from Control Center

Control Center pulls in data showing who last saved to the Budget and Projections Templates, when they saved, and where they saved from. The file location is clickable, and if you have access to the folder location you can open it up.

![](/images/WCNTraining/Budget/ControlCenter_BudgetFileLink.png)

![](/images/WCNTraining/Budget/ControlCenter_BudgetFileOpened.png)

If a file has not been saved to a given Budget or Projections Template, or you want to make a fresh one, you can drill on either section to create a new Template.

![](/images/WCNTraining/Budget/ControlCenter_DrillNewTemplates.png)

## Lock Levels and District Position Assignment

The Control Center manages the lock levels for the *Budget*, *Capital*, and *Projections* modules. The possible lock levels are: **Ops**, **A/C**, **Dist**, **Div**, **Reg**, or **Corp**.

Your level of access is determined by your position in the **District Position Assignment** (DPA). This can be found in the toolbox at the following location:

![](/images/WCNTraining/Capital/CapitalInput_DPANavigation.png)

![](/images/WCNTraining/Capital/CapitalInput_DPAWindow.png)

In the screenshot below, notice the lock level for Budget is **Dist Level**.

![](/images/WCNTraining/Budget/ControlCenter_CurrentLockLevel.png)

**IF** your permissions are high enough, you can change the Lock Level for Budgets. In this case, since it is locked at **Dist Level**, you need to be at *Dist* level or higher in the DPA.

If you have a high enough level, the Lock Level drop-down will show all levels up to your yours, plus one more to send it up once you are done. The screenshot below is for a Dist level user who can lock the Budget up to the **Div Level**.

![](/images/WCNTraining/Budget/ControlCenter_LockLevelOptions.png)

If a Dist level user locks the Budget up to **Div level** (usually done once Budget is ready for review), they will be locked out. If more changes are needed, they will need to work with a supervisor to unlock it back down to Dist level.

![](/images/WCNTraining/Budget/ControlCenter_LockedOut.png)

## Contract Center Lock Status

The **Contract Center** in Toolbox is locked based on the Budget Lock Level for the District in Control Center. If the Budget Lock Level is **Reg Level** or higher, Contract Center will be locked and you will not be able to edit.

![](/images/WCNTraining/Budget/ControlCenter_ContractCenterUnlocked.png)
![](/images/WCNTraining/Budget/ControlCenter_ContractCenterLocked.png)

## Budget Review Dates

The **Budget Review Dates** are used to version the budget amounts from Target Center 2.0 as they are synced into Interject. The four Budget Review Date options are: *Corp Review Thru*, *Reg Review Thru*, *Reg Cutoff*, and *Corp Cutoff*.

![](/images/WCNTraining/Budget/ControlCenter_ReviewDates.png)

When a budget amount is synced to Interject, it will fall into one of these four *Review Date Buckets*. If an amount is saved *before or at 7/1/2019 5:00 PM*, that amount will be placed in the *Corp Review Thru Bucket*. If a budget amount is saved after that time but *before or at 7/31/2019 5:00 PM*, it will be placed in the *Corp Cutoff Bucket*. This organization is repeated for the two remaining buckets.

>**AFTER CORP CUTOFF**
>If a budget amount is saved **AFTER** *Corp Cutoff*, it will **NOT** be synced to Interject. It will remain only in Target Center 2.0.

>**Do I have rights to change the Review Dates?**
>If you have **Reg Level** access to a district, you can update the **Reg Review Thru** and **Reg Cutoff** dates. If you have **Corp Level** access to a district, you can update all of the Review Dates.

### Review Dates Example

To see how this works in real time, we'll save an amount to a Budget Template. For this example, we'll save $100 to an account on *10/1/2019 3:30 PM*.

![](/images/WCNTraining/Budget/ControlCenter_BudTemplateSave01.png)

According to our Control Center *Budget Review Dates* (see earlier screenshot), *10/1/2019 3:30 PM* is after *Reg Cutoff* but before *Corp Cutoff*. This means that the $100 will be placed in the **Corp Cutoff Bucket**.

We can double check this in two places: The [ **Budget Change Query Tool** ](/bApps/InterjectTraining/Budget/BudgetChangeQuerySummary.html) and the **Budget Book**.

In [ **Budget Change Query Tool** ](/bApps/InterjectTraining/Budget/BudgetChangeQuerySummary.html), we look on the first tab *ReviewDateSummary*, pulling on the same District and Year.

![](/images/WCNTraining/Budget/ControlCenter_BudChangeQueryReviewDates01.png)

The [ **Budget Change Query Tool** ](/bApps/InterjectTraining/Budget/BudgetChangeQuerySummary.html) pulls in amounts saved to TC 2.0, and here we see the amount in the correct bucket. 

Next, look at the **Budget Book**, which shows the amounts saved to Interject. First, on the *Summary* tab we set *Versions* to **Corp Cutoff**. We also set the *In Districts* and *Budget Year* to correspond with what we are using.

![](/images/WCNTraining/Budget/ControlCenter_BudgetBookCorpCutoffSetting.png)

Now go to the *4_BudSumByMonth* tab and pull. Since we're pulling on the **Corp Cutoff** version, we see the $100 go into the correct account grouping.

![](/images/WCNTraining/Budget/ControlCenter_BudgetBookCorpCutoffAmount01.png)

Going back to the *Summary* tab, we change the *Versions* filter to **Reg Cutoff**.

![](/images/WCNTraining/Budget/ControlCenter_BudgetBookRegCutoffSetting.png)

Back on the *4_BudSumByMonth* tab, pull and notice that the $100 is gone. This is because the amount is *NOT* in the **Reg Cutoff Bucket**.

![](/images/WCNTraining/Budget/ControlCenter_BudgetBookRegCutoffAmount02.png)

Now, review dates will change throughout the budget season as Region/Corporate complete their reviews. For example, here Region has gone through a series of reviews and updated **Reg Review Thru** and **Reg Cutoff** to the values below.

![](/images/WCNTraining/Budget/ControlCenter_ReviewDates02.png)

The save we completed at *10/1/2019 3:30 PM* now falls into the **Reg Cutoff Bucket**. When this review date is updated, the amounts in Interject will be updated to move this amount automatically. We'll confirm using the same tools we did in previous steps.

![](/images/WCNTraining/Budget/ControlCenter_BudChangeQueryReviewDates02.png)

In the [ **Budget Change Query Tool** ](/bApps/InterjectTraining/Budget/BudgetChangeQuerySummary.html) we see the $100 has moved to the **Reg Cutoff** column. Also notice that the $100 is still in the **Corp Cutoff** column, because **Corp Cutoff** shows **ALL** the amounts leading up to the **Corp Cutoff** date, which is *11/1/2019 5:00 PM* in this case.

With this in mind, check the **Budget Book** for both **Reg Cutoff** and **Corp Cutoff** versions. We should see the $100 in both, because it fits in the **Reg Cutoff Bucket** and happens before **Corp Cutoff**.

![](/images/WCNTraining/Budget/ControlCenter_BudgetBookRegAndCorpCutoffAmounts.png)

To make sure, update the *Versions* on the *Summary* tab to **Reg Review Thru** and pull again. The $100 will be gone, because the save was after **Reg Review Thru**.

![](/images/WCNTraining/Budget/ControlCenter_BudgetBookRegReviewThruSetting.png)
![](/images/WCNTraining/Budget/ControlCenter_BudgetBookRegReviewThruAmounts.png)

### **AFTER CORP CUTOFF**

Now if an amount is saved **AFTER** the **Corp Cutoff** date, it will *NOT* be synced to Interject. Take the following example: we saved at *11/2/2019 5:00 PM* (after the **Corp Cutoff** date used in earlier example).

![](/images/WCNTraining/Budget/ControlCenter_BudTemplateSave02.png)

Let's check the two tools we used before to see how this shows up.

![](/images/WCNTraining/Budget/ControlCenter_BudChangeQueryReviewDates03.png)

Notice that the $5,000 is in the **After Corp Cutoff** column. It is also *NOT* included in the *Change From Corp Cutoff* column, because that includes only data *BEFORE* **Corp Cutoff**.

In the **Budget Book** tool, we pull for the highest *Versions* setting, **Corp Cutoff**, to show EVERYTHING in Interject. Notice that the $5,000 is absent because it is not yet synced to Interject.

![](/images/WCNTraining/Budget/ControlCenter_BudgetBookCorpCutoffAmount02.png)

Once the **Corp Cutoff** date is extended beyond *11/1/2019 5:00 PM*, this amount will be synced to Interject.

>**BOD and Versioning**
>Once **BOD** is applied and versioning is enabled, the Review Dates no longer take effect. Budget amounts are not synced to Interject based on when they were saved but rather if their ChangeIDs are versioned by Corporate.

## Budget Cutoff Sync Dates

The Control Center also controls when PI and Depr accounts get synced to Interject.

![](/images/WCNTraining/Budget/ControlCenter_CutoffSyncDates.png)

When PI accounts are updated in the Contract Center, or Depr accounts in Capital, they will be synced through to Interject automatically as long as they are saved *BEFORE* their associated cutoff sync dates. If saved after, they will not be synced over. Once the cutoff sync dates are updated to a datetime after the updated account save, the unsynced changes will sync.

>**Do I have rights to change the Cutoff Sync Dates?**
>Only Corporate Admins have rights to update these dates.

## Drills

There are many drills availabe on this tool, depending on where you drill from.

**Create New Projection Template** opens a new [ Projection Template ](/bApps/InterjectTraining/Projections/ProjectionTemplate.html).
![](/images/WCNTraining/Budget/ControlCenter_ProjDrill.png)

**Create New Budget Template** opens a new [ Budget Template ](/bApps/InterjectTraining/Budget/BudgetTemplateSummary.html).
![](/images/WCNTraining/Budget/ControlCenter_BudDrill.png)

Drilling on the Review Date columns gives the following drill options:
![](/images/WCNTraining/Budget/ControlCenter_ReviewDateDrills.png)
* **Drill to Change History - Summary** opens the *Summary* tab on the [ Budget Change Query Tool ](/bApps/InterjectTraining/Budget/BudgetChangeQuery_Summary.html).
* **Drill to Change History - Detail** opens the *Detail* tab on the [ Budget Change Query Tool ](/bApps/InterjectTraining/Budget/BudgetChangeQuery_Detail.html).
* **Drill to Review Date Amounts** opens the *ReviewDateSummar* tab on the [ Budget Change Query Tool ](/bApps/InterjectTraining/Budget/BudgetChangeQuery_ReviewDateSummary.html).

Drilling on the Capital columns gives the following drill options:
![](/images/WCNTraining/Budget/ControlCenter_CapitalDrills.png)
* **Capital Report: Summary** opens the *Summary* tab on the [ Capital Input Tool ](/bApps/InterjectTraining/Capital/CapitalSummary.html).
* **Capital Report: Detail** opens the *Detail* tab on the [ Capital Input Tool ](/bApps/InterjectTraining/Capital/CapitalInput.html).

## Common Save Errors

![](/images/WCNTraining/Budget/ControlCenter_Errors_LockLevelTooHigh.png)

*You are either trying to lock a district to a level you do not have permissions for, or the district itself is already locked above your level*

___
![](/images/WCNTraining/Budget/ControlCenter_Errors_OneSecondOffsetReviewDates.png)

*The Review Dates cannot equal each other. The later of the review dates has been automatically offset by 1 second from the former by just one second to not create any sync conflicts.*

___
<button class="collapsible">Other Possible Save Errors</button>
<div markdown="1" class="panel">
![](/images/WCNTraining/Budget/ControlCenter_Errors_YearMonth.png)

*You need a valid Year Month, format YYYY-MM*

___
![](/images/WCNTraining/Budget/ControlCenter_Errors_InvalidDistricts.png)

*The district(s) you have manually added to the Control Center are either inactive or non-financial. You cannot save them, or they should not be handled in Control Center*

___
![](/images/WCNTraining/Budget/ControlCenter_Errors_InvalidLockLevel.png)

*The Lock Level you tried saving up is not valid. Please use one of the drop-down options pulled into the tool*
           
___
![](/images/WCNTraining/Budget/ControlCenter_Errors_InvalidReviewDate.png)

*The timestamp you tried saving to the Review Date is not a valid format. It needs to be MM/DD/YY HH:MM (AM/PM)*

___
 ![](/images/WCNTraining/Budget/ControlCenter_Errors_LowLevelReviewDates.png)

*You are below the level required to change the associated Review Dates*

</div>
