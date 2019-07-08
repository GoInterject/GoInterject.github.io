---
title: Control Center
layout: custom
keywords: [Training, Budget, Control Center]
description: 
---

## Overview

**Purpose**: This tool controls who has access to save to Budgets and when the data will flow from the Budget Module into Interject. Also controls lock levels of Projections and Capital.

**Report Location**<br>
(Attach Report Location Image here)

**Filter Options**:

* **District(s)** - *Optional*. Blank defaults to all you have rights to. Can be individual district, district range, or groupings
* **Year Month** - *Optional*. Blank defaults to the current Year-Month. Needs to be in YYYY-MM format

![](/images/WCNTraining/Budget/ControlCenter_FullView.png)

## Accessing Templates from Control Center

Control Center pulls in information on who last saved to the Budget and Projections Templates, when they saved, and where they saved from. The file location can be clicked on, and if you have access to the folder location you can open it up.

![](/images/WCNTraining/Budget/ControlCenter_BudgetFileLink.png)

![](/images/WCNTraining/Budget/ControlCenter_BudgetFileOpened.png)

If a file has not been saved to the given Budget or Projections Template, or you want to make a fresh one you can drill on either section to create a new Template.

![](/images/WCNTraining/Budget/ControlCenter_DrillNewTemplates.png)

## Lock Levels and District Position Assignment

The Control Center manages the lock levels for the *Budget*, *Capital*, and *Projections* modules. The possible lock levels are: **Ops**, **A/C**, **Dist**, **Div**, **Reg**, or **Corp**.

The level of access you are permitted is determined by your position in the **District Position Assignment** (DPA). This can be found in toolbox at the following location:

![](/images/WCNTraining/Capital/CapitalInput_DPANavigation.png)

![](/images/WCNTraining/Capital/CapitalInput_DPAWindow.png)

In the screenshot below, we see that the lock level for Budget is **Dist Level**.

![](/images/WCNTraining/Budget/ControlCenter_CurrentLockLevel.png)

The Lock Level for Budget can be changed with the Control Center, **IF** you have high enough permissions. In this case, since it is locked at **Dist Level**, you need to be at *Dist* or higher level in the DPA.

If you have a high enough level, the drop-down for the Lock Level will show all levels up to your level, plus one more to send it up once you are done. The screenshot below is for a Dist level user, who can lock the Budget up to **Div Level**.

![](/images/WCNTraining/Budget/ControlCenter_LockLevelOptions.png)

If the Dist level user locks the Budget up to **Div Level** (usually done once Budget is ready for review), they lock themselves out. If you need to make changes again, you will need to work with your supervisor to unlock it back down to your level.

![](/images/WCNTraining/Budget/ControlCenter_LockedOut.png)

## Contract Center Lock Status

The **Contract Center** in Toolbox is locked based on the Budget Lock Level for the District in Control Center. If the Budget Lock Level is **Reg Level** or higher, Contract Center will be locked and you will not be able to make any edits.

![](/images/WCNTraining/Budget/ControlCenter_ContractCenterUnlocked.png)
![](/images/WCNTraining/Budget/ControlCenter_ContractCenterLocked.png)

## Budget Review Dates

The **Budget Review Dates** are used to version the budget amounts from TC 2.0 as they are synced into Interject. The four Budget Review Date options are: *Corp Review Thru*, *Reg Review Thru*, *Reg Cutoff*, and *Corp Cutoff*.

![](/images/WCNTraining/Budget/ControlCenter_ReviewDates.png)

When a budget amount is synced to Interject, it will fall into one of these four *Review Date Buckets*. If an amount is saved *before or at 7/1/2019 5:00 PM*, that amount will be placed in the *Corp Review Thru Bucket*. If a budget amount is saved after that time but *before or at 7/31/2019 5:00 PM*, it will be placed in the *Corp Cutoff Bucket*. This organization is repeated for the two remaining buckets.

>**AFTER CORP CUTOFF**
>If a budget amount is saved **AFTER** *Corp Cutoff*, then it will **NOT** be synced to Interject. It will remain only in Target Center 2.0.

>**Do I have rights to change the Review Dates?**
>If you have **Reg Level** access to a district, you can update the **Reg Review Thru** and **Reg Cutoff** dates. If you have **Corp Level** access to a district, you can update all of the Review Dates.

### Review Dates Example

Let's save an amount to a Budget Template, and examine how this works in real time. For our example, let's say we save $100 to an account on *10/1/2019 3:30 PM*.

![](/images/WCNTraining/Budget/ControlCenter_BudTemplateSave01.png)

According to our Control Center *Budget Review Dates* (see earlier screenshot), *10/1/2019 3:30 PM* is after *Reg Cutoff* but before *Corp Cutoff*. This means that the $100 will be placed in the **Corp Cutoff Bucket**.

To double check this, we can look in two places: The [ **Budget Change Query Tool** ](/bApps/InterjectTraining/Budget/BudgetChangeQuerySummary.html) and the **Budget Book**.

In [ **Budget Change Query Tool** ](/bApps/InterjectTraining/Budget/BudgetChangeQuerySummary.html), we look on the first tab *ReviewDateSummary*, pulling on the same District and Year.

![](/images/WCNTraining/Budget/ControlCenter_BudChangeQueryReviewDates01.png)

The [ **Budget Change Query Tool** ](/bApps/InterjectTraining/Budget/BudgetChangeQuerySummary.html) pulls in amounts saved to TC 2.0, and here we see the amount in the correct bucket. 

Next let's check out the **Budget Book**, which will show the amounts saved to Interject. First, on the *Summary* tab we set *Versions* to **Corp Cutoff**. We also set the *In Districts* and *Budget Year* to what we are using.

![](/images/WCNTraining/Budget/ControlCenter_BudgetBookCorpCutoffSetting.png)

We go to the *4_BudSumByMonth* tab and pull. Since we are pulling on the **Corp Cutoff** version, we see the $100 pull into the correct account grouping.

![](/images/WCNTraining/Budget/ControlCenter_BudgetBookCorpCutoffAmount01.png)

Going back to the *Summary* tab, we change the *Versions* filter to **Reg Cutoff**.

![](/images/WCNTraining/Budget/ControlCenter_BudgetBookRegCutoffSetting.png)

Back on the *4_BudSumByMonth* tab, we pull and see that the $100 has disappeared. This is because the amount is *NOT* in the **Reg Cutoff Bucket**.

![](/images/WCNTraining/Budget/ControlCenter_BudgetBookRegCutoffAmount02.png)

Now, Review Dates will change throughout the Budget Season as Region/Corporate complete their reviews. So let's say that Region has gone through a series of reviews, and updates **Reg Review Thru** and **Reg Cutoff** to the values below.

![](/images/WCNTraining/Budget/ControlCenter_ReviewDates02.png)

The save we completed at *10/1/2019 3:30 PM* now falls into the **Reg Cutoff Bucket**. When this review date was updated, the amounts in Interject will be updated to move this amount automatically. Let's check the two tools we used before to confirm that this is the case.

![](/images/WCNTraining/Budget/ControlCenter_BudChangeQueryReviewDates02.png)

In the [ **Budget Change Query Tool** ](/bApps/InterjectTraining/Budget/BudgetChangeQuerySummary.html) we see the $100 has moved to the **Reg Cutoff** column. You will also notice that the $100 is still in the **Corp Cutoff** column, because **Corp Cutoff** shows **ALL** the amounts leading up to the **Corp Cutoff** date, which is *11/1/2019 5:00 PM* in this case.

With this in mind, we check the **Budget Book** for both **Reg Cutoff** and **Corp Cutoff** versions. We should see the $100 in both, because it fits in the **Reg Cutoff Bucket** and happens before **Corp Cutoff**.

![](/images/WCNTraining/Budget/ControlCenter_BudgetBookRegAndCorpCutoffAmounts.png)

Just to make sure, let's update the *Versions* on the *Summary* tab to **Reg Review Thru** and pull one last time. The $100 will not be there, because the save was after **Reg Review Thru**.

![](/images/WCNTraining/Budget/ControlCenter_BudgetBookRegReviewThruSetting.png)
![](/images/WCNTraining/Budget/ControlCenter_BudgetBookRegReviewThruAmounts.png)

### **AFTER CORP CUTOFF**

Now if an amounts is saved **AFTER** the **Corp Cutoff** date, it will *NOT* be synced to Interject. Let's take the following example, saying we saved it at *11/2/2019 5:00 PM* (after the **Corp Cutoff** date used in earlier example).

![](/images/WCNTraining/Budget/ControlCenter_BudTemplateSave02.png)

Let's check the two tools we used before to see how this shows up in them.

![](/images/WCNTraining/Budget/ControlCenter_BudChangeQueryReviewDates03.png)

We see that the $5,000 is in the **After Corp Cutoff** column. It is also *NOT* included in the *Change From Corp Cutoff* column, because that only includes everything *BEFORE* **Corp Cutoff**.

In the **Budget Book** tool, we pull for the highest *Versions* setting **Corp Cutoff** to show EVERYTHING in Interject. We see that the $5,000 is not there, because it is not yet synced to Interject.

![](/images/WCNTraining/Budget/ControlCenter_BudgetBookCorpCutoffAmount02.png)

Once the **Corp Cutoff** date is extended beyond *11/1/2019 5:00 PM*, this amount will be synced through to Interject.

>**BOD and Versioning**
>Once **BOD** is applied and versioning is in effect, the Review Dates no longer take effect. Budget amounts are not synced to Interject based on when they were saved, but on if their ChangeIDs are versioned by Corporate.

## Budget Cutoff Sync Dates

The Control Center also controls when PI and Depr accounts get synced to Interject.

![](/images/WCNTraining/Budget/ControlCenter_CutoffSyncDates.png)

When PI accounts are updated in the Contract Center or Depr accounts in Capital, they will be synced through to Interject automatically as long as they are saved *BEFORE* their associated cutoff sync dates. If saved after, they will not be synced over. Once the cutoff sync dates are updated to a datetime after the updated account save, the unsynced changes will then sync over.

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

## Drills

You can drill on any row to bring up more detailed information for the Capital amounts belonging to the PO Item in the Capital Change Query.

![](/images/WCNTraining/Capital/CapitalInput_DrillWindow.png)

**Drill to CC Query for Change History** opens the [ Capital Change Query report ](/bApps/InterjectTraining/Capital/CCQuery.html).
![](/images/WCNTraining/Capital/CapitalInput_CapitalChangeDrill.png)

## Common Save Errors

To be finished later...