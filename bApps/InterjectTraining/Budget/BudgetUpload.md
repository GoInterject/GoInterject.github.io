---
title: Budget Upload Tab
layout: custom
keywords: [Training, Budget, Budget Upload Tab]
description: 
---

## Overview

**Purpose**:  Bulk upload multiple Budget accounts at the same time, in a simple list format.

**Filter Options**:

* **Year** - *Required*. Needs to be in YYYY format
* **District** - *Optional*. Individual district, district ranges, or groupings allowed. *Required* if **Account** is *blank*
* **Account** - *Optional*. Individual account, account ranges, or groupings allowed. *Required* if **District** is *blank*
* **System** - *Optional*. Needs to be numeric, 3 digits long
* **SubSystem** - *Optional*. Needs to be numeric, 2 digits long

![](/images/WCNTraining/Budget/BudgetUpload_FullView.png)

## Uploading to more than one district at a time

Region Controllers can upload Budget amounts to more than one district at a time. To do so, a Regional Controller can pull on the Region and make changes to the Budget amounts across multiple districts.

If do not have Region Controller access, you will not be able to pull or or save on multiple Districts. You will get the following validation errors:

**Pull**

![](/images/WCNTraining/Budget/BudgetUpload_MultipleDistrictsPull.png)

**Save**

![](/images/WCNTraining/Budget/BudgetUpload_MultipleDistrictsSave.png)

## Drop Budget numbers in without pulling first

When you first open the Budget Upload tab, there will be a range of blank rows available for you to drop Budget values immediately. 

![](/images/WCNTraining/Budget/BudgetUpload_BlankRowsDefault.png)

If you need to add more blank rows, insert new rows in the middle of the blank rows. This will automatically copy the formatting, and include the new rows in the Save formula range.

![](/images/WCNTraining/Budget/BudgetUpload_InsertNewRowsMiddle.png)

If you are starting with an empty sheet, you can insert new rows like before. You will need to check the Save formula to make sure the save range includes all of the new rows.

![](/images/WCNTraining/Budget/BudgetUpload_InsertNewRowsFromEmpty.png)

After you add the rows, access the *Quick Tools* by hitting **CTRL + T**, and select *Freeze/UnFreeze Panes (current tab)*.

![](/images/WCNTraining/Budget/BudgetUpload_QuickTools.png)

Navigate up to the hidden formulas section and click on the Save formula in cell D9.

![](/images/WCNTraining/Budget/BudgetUpload_SaveFormula.png)

Click within the formula bar the top, and it will bring up all of the cell references. The blue range of cells under the District column will need to be extended to include all of the rows above it.

![](/images/WCNTraining/Budget/BudgetUpload_SmallSaveRange.png)
![](/images/WCNTraining/Budget/BudgetUpload_BigSaveRange.png)

Now you will be able to drop in whatever Budget values you want into this tab, and save them up!

## Do I have security rights to Save from the Budget Upload tab?

Only people in the District Position Assignment (DPA) for the District in Toolbox can save to this file. Your Division Controller can add you if you are not already in the DPA.

![](/images/WCNTraining/Capital/CapitalInput_DPANavigation.png)

![](/images/WCNTraining/Capital/CapitalInput_DPAWindow.png)

## Budget Upload and the Control Center

Based on your position in the DPA for the district, you will have a certain level of access to this report. The types of levels you may be on are: **A/C**, **Dist**, **Div**, **Reg**, or **Corp**.

Budget is locked at these levels in the **Control Center**, in the N column. In the example below, District 2050 is locked at the Reg Level.

![](/images/WCNTraining/Budget/BudgetUpload_ControlCenter1District.png)

If an A/C level user tried saving to 2050 Budget, they would be stopped with the following message.

![](/images/WCNTraining/Budget/BudgetUpload_LockLevel1District.png)

You are able to save Budget as long as the Budget lock level is your level or below. Otherwise you will not be able to save Budget.

>**Region Controllers - Multiple Lock Levels**<br>
>As a Region Controller, you are able to save to multiple districts at once. It is possible though to have one of the districts locked at Corp above you.
>![](/images/WCNTraining/Budget/BudgetUpload_ControlCenter2Districts.png)
>If a Region Controller tried saving to these two districts at the same time, the save would be stopped and they would get the following error message:
>![](/images/WCNTraining/Budget/BudgetUpload_LockLevel2Districts.png)
>2041 would need to be unlocked to Reg for the Region Controller to edit. Otherwise if they wanted to edit 2050 still, they would need to remove the 2041 row(s).

## After Corp Cutoff and after BOD

If you save to Budget **After Corp Cutoff**, the numbers will still be updated in Target Center 2.0. However, they will not be synced through to Interject.

In this example, the Corp Cutoff date in Control Center is set to 11/3/2018.

![](/images/WCNTraining/Budget/BudgetUpload_CCAfterCorpCutoff.png)

We then try and upload a change to Budget using the **Budget Upload** tool, and get the following popup and in-row messages.

![](/images/WCNTraining/Budget/BudgetUpload_AfterCorpCutoffMessage.png)
![](/images/WCNTraining/Budget/BudgetUpload_AfterCorpCutoffRowMessage.png)

You can verify that the Budget amount was updated 