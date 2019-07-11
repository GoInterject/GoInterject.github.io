---
title: Projection Upload Tool
layout: custom
keywords: [Training, Projections, Projections Upload]
description: 
---

## Overview

**Purpose**: The Projections Upload Tool allows controllers to upload projections for multiple accounts in a district at the same time. This upload tool closely matches the Budget Upload Tool in design and function.

**Filter Options**:

* **Year-Month** - *Required*. Must be in YYYY-MM format
* **District** - *Optional*. Individual district, district ranges, or groupings allowed. *Required* if **Account** is *blank*
* **Account** - *Optional*. Individual account, account ranges, or groupings allowed. *Required* if **District** is *blank*
* **System** - *Optional*. Must be numeric, 3 digits long
* **SubSystem** - *Optional*. Must be numeric, 2 digits long

![](/images/WCNTraining/Projections/ProjectionUpload_FullView.png)

## Uploading to more than one district at a time

Regional Controllers can pull on the Region, making Projections amount changes across multiple districts and uploading them all at once.

If you do not have Region Controller access, you will not be able to pull or save on multiple Districts. You will get the following validation errors:

**Pull**

![](/images/WCNTraining/Projections/ProjectionUpload_MultipleDistrictsPull.png)

**Save**

![](/images/WCNTraining/Projections/ProjectionUpload_MultipleDistrictsSave.png)

## Drop Projections numbers in without pulling first

On opening the Projection Upload Tool, there will be a range of blank rows available into which you can immediately drop Projection values. 

![](/images/WCNTraining/Projections/ProjectionUpload_BlankRowsDefault.png)

If you need to add more blank rows, insert new rows in the middle of the blank ones. Formatting will be copied automatically, and the new rows will be included in the Save formula range.

![](/images/WCNTraining/Projections/ProjectionUpload_InsertNewRowsMiddle.png)

If you're starting with an empty sheet, you can insert new rows like before. You will need to check the Save formula to make sure the save range includes all new rows.

![](/images/WCNTraining/Projections/ProjectionUpload_InsertNewRowsFromEmpty.png)

After you add the rows, access the *Quick Tools* by hitting **CTRL + T**, then select *Freeze/UnFreeze Panes (current tab)*.

![](/images/WCNTraining/Projections/ProjectionUpload_QuickTools.png)

Navigate up to the hidden formulas section and click on the Save formula in cell D9.

![](/images/WCNTraining/Projections/ProjectionUpload_SaveFormula.png)

Click within the formula to bring up the cell references. Extend the **blue** range of cells under the District column to include all rows above it.

![](/images/WCNTraining/Projections/ProjectionUpload_SmallSaveRange.png)
![](/images/WCNTraining/Projections/ProjectionUpload_BigSaveRange.png)

Now you will be able to drop in the desired Projections values and save them.

## Do I have security rights to Save from the Projections Upload tab?

To learn whether you can save to the Projections Upload Tool, please check the [ Tools Controlled by the Control Center ](/bApps/InterjectTraining/Budget/ControlCenterSecurity.html#projections-tools-and-the-control-center) page.

## Common Save Errors

![](/images/WCNTraining/Projections/ProjectionUpload_LockLevelError.png)

*Projections are locked above your level in the Control Center. If you need to make changes, work with your supervisor to unlock Projections back to your level.*

___
![](/images/WCNTraining/Projections/ProjectionUpload_DPAError.png)

*You need to be in the District Position Assignment at an approved position to use this tool for any saves. Your Division Controllers can add you to the DPA in Toolbox.*

___
<button class="collapsible">Other Possible Save Errors</button>
<div markdown="1" class="panel">
![](/images/WCNTraining/Projections/ProjectionUpload_InvalidYearMonth.png)

*Year-Month is required and must be in the YYYY-MM format.*
        
___
![](/images/WCNTraining/Projections/ProjectionUpload_IncompleteGLString.png)

*All segments are required to save from the Projections Upload Tool. Please add the missing segments.*

___
![](/images/WCNTraining/Projections/ProjectionUpload_InvalidAccount.png)

*Account is not an valid Account. Please update to a valid Account.*
        
___
![](/images/WCNTraining/Projections/ProjectionUpload_InvalidDistrict.png)

*District is not a valid District. Please update to a valid District.*

___
![](/images/WCNTraining/Projections/ProjectionUpload_InvalidSystem.png)

*System is not an valid System. Please update to a valid System.*
        
___
![](/images/WCNTraining/Projections/ProjectionUpload_InvalidSubSystem.png)

*SubSystem is not an valid SubSystem. Please update to a valid SubSystem.*

___
![](/images/WCNTraining/Projections/ProjectionUpload_DuplicateAccount.png)

*Duplicate account was found in the save list. Remove the duplicate and try saving again.*
        
___
![](/images/WCNTraining/Projections/ProjectionUpload_InvalidAmount.png)

*Non-numeric amounts were found in the Projections columns. Make sure there are no broken formulas or references.*

___
![](/images/WCNTraining/Projections/ProjectionUpload_DistrictNotinRightsRow.png)

*You are not in the Interject security for the District you are trying to save to.*

___
![](/images/WCNTraining/Projections/ProjectionUpload_RegCorpMultipleDistrictError.png)

*When saving to multiple districts at the same time, you need to be on Reg or Corp Level for both. Save to one district at a time with this tool.*
        
___
![](/images/WCNTraining/Projections/ProjectionUpload_NotinDPAforDistrict.png)

*You need to be in the DPA for the district you are trying to save to. Your Division Controller can add you to the District Position Assignment in Toolbox.*

___
![](/images/WCNTraining/Projections/ProjectionUpload_CannotUpdateAutocalcs.png)

*You cannot update Autocalc with this tool. Please remove the Account from your save.*
        
</div>
