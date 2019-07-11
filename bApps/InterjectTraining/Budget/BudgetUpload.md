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

Regional Controller can pull on the Region, making Budget amount changes across multiple districts and uploading them all at once.

If you do not have Region Controller access, you will not be able to pull or save on multiple Districts. You will get the following validation errors:

**Pull**

![](/images/WCNTraining/Budget/BudgetUpload_MultipleDistrictsPull.png)

**Save**

![](/images/WCNTraining/Budget/BudgetUpload_MultipleDistrictsSave.png)

## Drop Budget numbers in without pulling first

On opening the Budget Upload tab, there will be a range of blank rows available for you to immediately drop Budget values. 

![](/images/WCNTraining/Budget/BudgetUpload_BlankRowsDefault.png)

If you need to add more blank rows, insert new rows in the middle of the blank rows. This will automatically copy the formatting and include the new rows in the Save formula range.

![](/images/WCNTraining/Budget/BudgetUpload_InsertNewRowsMiddle.png)

If you're starting with an empty sheet, you can insert new rows like before. You will need to check the Save formula to make sure the save range includes all new rows.

![](/images/WCNTraining/Budget/BudgetUpload_InsertNewRowsFromEmpty.png)

After you add the rows, access the *Quick Tools* by hitting **CTRL + T**, then select *Freeze/UnFreeze Panes (current tab)*.

![](/images/WCNTraining/Budget/BudgetUpload_QuickTools.png)

Navigate up to the hidden formulas section and click on the Save formula in cell D9.

![](/images/WCNTraining/Budget/BudgetUpload_SaveFormula.png)

Click within the formula to bring up the cell references. Extend the blue range of cells under the District column to include all rows above it.

![](/images/WCNTraining/Budget/BudgetUpload_SmallSaveRange.png)
![](/images/WCNTraining/Budget/BudgetUpload_BigSaveRange.png)

Now you will be able to drop in the desired Budget values and save them!

## Do I have security rights to Save from the Budget Upload tab?

To find if you can save to the Budget Upload Tool, please check out the [ Tools Controlled by the Control Center ](/bApps/InterjectTraining/Budget/ControlCenterSecurity.html#budget-tools-and-the-control-center) page.

## After Corp Cutoff and after BOD

If you save to Budget **After Corp Cutoff**, the numbers will still be updated in Target Center 2.0. However, they will not sync to Interject.

In this example, the *Corp Cutoff* date in Control Center is set to 11/3/2018.

![](/images/WCNTraining/Budget/BudgetUpload_CCAfterCorpCutoff.png)

Then try uploading a change to Budget using the **Budget Upload** tool (after this date), and get the following popup and in-row messages.

![](/images/WCNTraining/Budget/BudgetUpload_AfterCorpCutoffMessage.png)
![](/images/WCNTraining/Budget/BudgetUpload_AfterCorpCutoffRowMessage.png)

Notice the changes have been saved to Target Center 2.0, but they are not yet synced to Interject. This change will be synced to Interject once the *Corp Cutoff* date is set to a Date/Time after our change or BOD.

We can use the [Budget Change Query Tool](/bApps/InterjectTraining/Budget/BudgetChangeQueryToolSummary.html) to confirm that our save has been registered in Target Center 2.0. The new [UnsyncedChanges](/bApps/InterjectTraining/Budget/BudgetChangeQuery_UnsyncedChanges.html) tab is designed to pull in all amounts not yet synced to Interject, which neatly matches our inquiry. The screenshot below shows that our Budget save succeeded and is in the database.

![](/images/WCNTraining/Budget/BudgetUpload_UnsyncedChangesBCQuery.png)

Once **BOD** for a Budget Year has been created, any save from the **Budget Upload Tool** will not automatically sync to Interject again, just like *After Corp Cutoff*. However, while it is not in Interject, it is in Target Center 2.0 and can be checked using the [ UnsyncedChanges ](/bApps/InterjectTraining/Budget/BudgetChangeQuery_UnsyncedChanges.html) tab in the [ Budget Change Query Tool ](/bApps/InterjectTraining/Budget/BudgetChangeQueryToolSummary.html). Once Corporate has versioned your change, the Budget amount will be sycned to Interject.

## Common Save Errors

![](/images/WCNTraining/Budget/BudgetUpload_LockLevelError.png)

*Budget is locked above your level in the Control Center. If you need to make changes, work with your supervisor to unlock Budget back to your level.*

___
![](/images/WCNTraining/Budget/BudgetUpload_DPAError.png)

*You need to be in the District Position Assignment at an approved position to use this tool for any saves. Your Division Controllers can add you to the DPA in Toolbox.*

___
<button class="collapsible">Other Possible Save Errors</button>
<div markdown="1" class="panel">
![](/images/WCNTraining/Budget/BudgetUpload_InvalidSource.png)

*Please select Bud in the drop-down filter option and make sure your Source column says Budget.*

___
![](/images/WCNTraining/Budget/BudgetUpload_InvalidYear.png)

*Year is required and needs to be in the YYYY format.*
        
___
![](/images/WCNTraining/Budget/BudgetUpload_IncompleteGLString.png)

*All segments are required to save from the Budget Upload Tool. Please add the missing segments.*

___
![](/images/WCNTraining/Budget/BudgetUpload_InvalidAccount.png)

*Account is not an valid Account. Please update to a valid Account.*
        
___
![](/images/WCNTraining/Budget/BudgetUpload_InvalidDistrict.png)

*District is not a valid District. Please update to a valid District.*

___
![](/images/WCNTraining/Budget/BudgetUpload_InvalidSystem.png)

*System is not an valid System. Please update to a valid System.*
        
___
![](/images/WCNTraining/Budget/BudgetUpload_InvalidSubSystem.png)

*SubSystem is not an valid SubSystem. Please update to a valid SubSystem.*

___
![](/images/WCNTraining/Budget/BudgetUpload_DuplicateAccount.png)

*Duplicate account was found in the save list. Remove the duplicate and try saving again.*
        
___
![](/images/WCNTraining/Budget/BudgetUpload_InvalidAmount.png)

*Non-numeric amounts were found in the Budget columns. Make sure there are no broken formulas or references.*

___
![](/images/WCNTraining/Budget/BudgetUpload_DistrictNotinRightsRow.png)

*You are not in the Interject security for the District you are trying to save to.*

___
![](/images/WCNTraining/Budget/BudgetUpload_RegCorpMultipleDistrictError.png)

*When saving to multiple districts at the same time, you need to be on Reg or Corp Level for both. Save to one district at a time with this tool.*
        
___
![](/images/WCNTraining/Budget/BudgetUpload_NotinDPAforDistrict.png)

*You need to be in the DPA for the district you are trying to save to. Your Division Controller can add you to the District Position Assignment in Toolbox.*

___
![](/images/WCNTraining/Budget/BudgetUpload_CannotUpdateAutocalcs.png)

*You cannot update Autocalc with this tool. Please remove the Account from your save.*
        
___
![](/images/WCNTraining/Budget/BudgetUpload_AfterCorpCutoffMessage.png)
![](/images/WCNTraining/Budget/BudgetUpload_AfterCorpCutoffRowMessageSingle.png)

*The save succeeded, but it is After Corp Cutoff for this District. The number will not be updated in Interject until Corp Cutoff is updated or BOD.*
</div>
