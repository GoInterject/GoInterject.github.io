---
layout: custom  
title:  "Capital Input User Training - Bud Capital Input"
date:   2019-06-25 15:43:02 -0700
categories: Training, Capital
---

## Overview

**Purpose**:  Save new Capital PO Items for a specific District. Also pulls in Capital PO information to update existing POs

**Filter Options**:

* **District** - *Required*. Individual District, no Groupings
* **Budget Year** - *Required*. Needs to be in YYYY format

![](/images/WCNTraining/Capital/CapitalInput_FullView.png)

## PO Information

This first section of the report holds all of the key PO Information. Here you will see the PO Number, the PO Item, and the Descriptions/Explanations of the PO/Item.

![](/images/WCNTraining/Capital/CapitalInput_POInfo.png)

**On Save**
* Change the Delete on Save column drop-down to Delete! to remove an existing PO Item
* The PO Items cannot equal one another in the same PO. These will be marked as Duplicates on the Save and be rejected

## Asset Information

This section displays the Asset Type/Subtype information for the PO Item. Depending on the Asset Type/SubType selected, the other drop-down options will automatically update to the available choices.

**A/R** = *Add* or *Replace*

**N/U** = *New* or *Used*

![](/images/WCNTraining/Capital/CapitalInput_AssetInfo.png)

**On Save**
* If you change the Asset Type of an existing PO Item. be sure to change the SubType and other information correctly. Otherwise on the Save the validation may stop you and tell you to update your PO Item options
* If the Asset Type is connected with a Truck, you need to link the PO Item to the Truck in the Truck Ctr. # column. On the pull the drop-down options will automatically provide all available Truck numbers

## Period Amounts

This section is for the periodic Capital amounts.

![](/images/WCNTraining/Capital/CapitalInput_PeriodAmounts.png)

## Replacement Info

This hidden grouped section is for the Replace Information. You will need to unhide this section if you selected R in the A/R column earlier.

![](/images/WCNTraining/Capital/CapitalInput_ReplacementInfo.png)

**On Save**
* If PO Item is marked R in the A/R column, then it will require a FAS # and Replacement Notes
* The Model Year is NOT uploaded to DMS

## Folder/File Link & Save Messages

Save the file/location of the PO Item documentation you want recorded. On Save, the Successful Save/Updates will show up here. If there are any validation errors, they will be presented here on the Save.

![](/images/WCNTraining/Capital/CapitalInput_FilePathMessage.png)

**On Save**
* The Folder/File Link is NOT uploaded to DMS

## Do I have security rights to Save from this Input File?

Only people in the District Position Assignment (DPA) for the District in Toolbox can save to this file. Your Division Controller can add you if you are not already in the DPA.

![](/images/WCNTraining/Capital/CapitalInput_DPANavigation.png)

![](/images/WCNTraining/Capital/CapitalInput_DPAWindow.png)

## Common Save Errors

![](/images/WCNTraining/Capital/CapitalInput_Error_LockLevel.png)

*Your highest level in the District Position Assignment window of the District is lower than what the District is locked at in the Control Center. If you need to make Capital Changes while it is locked above your level, coordinate with your Division Controller to make the needed changes.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_TypeSubType.png)

*The chosen SubType does not belong to the Asset Type selected. Please select a valid Subtype from the available drop-down list.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_ReplacementReqs.png)

*If the PO Item is a Replacement (R in A/R), both a FAS # and Replacement Note are required (in the hidden Replacement Info section)*

___
<button class="collapsible">Other Possible Save Errors</button>
<div markdown="1" class="panel">
![](/images/WCNTraining/Capital/CapitalInput_Error_RePull.png)

*If you pull for a District and Budget Year, you can only save Capital PO changes for that District/Budget Year. If you want to save to a new District/Budget Year, you need to pull for that combination first.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_InvalidYear.png)

*The Budget Year input requires a valid Year, format YYYY.*
        
___
![](/images/WCNTraining/Capital/CapitalInput_Error_InvalidDistrict.png)

*The District input requires a valid District, singular. Does **NOT** permit Groupings*

___
 ![](/images/WCNTraining/Capital/CapitalInput_Error_YearNotSetup.png)

*Capital may not be unlocked yet for your District. Please contact WCN Support to confirm if this is the case.*

___
 ![](/images/WCNTraining/Capital/CapitalInput_Error_MissingColumns.png)

*The local version of the report has been been changed and will not longer save correctly. Get the newest version of the report from the library.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_MissingFields.png)

*The PO Item row requires information in the associated column.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_PONumReq.png)

*A PO # is needed for any non-deleted rows.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_PODescriptionReq.png)

*A PO Description is needed for any non-deleted rows.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_PODescriptionMatching.png)

*The PO Description for all PO Items within a PO must be the same.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_PONumRange.png)

*The PO # needs to be a valid number within that range.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_InvalidPOItem.png)

*The PO Item # needs to be a valid number within that range.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_DuplicatePOItem.png)

*Items belonging to the same PO must be different numbers.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_InvalidAssetType.png)

*Please use only the options available in the Asset drop-down list.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_InvalidLife.png)

*The Life value is not correct for the Asset Type/Subtype combination. Please select a valid Life option from the available drop-down list.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_TruckNum.png)

*The Truck # needs to be a valid, available Truck number found in the Truck Center. Please select a valid Truck # option from the available drop-down list.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_NewUsed.png)

*The selected Truck # New/Used status does not match the N/U column. Either updated the N/U column accordingly, or select a different valid Truck #.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_DuplicateTruck.png)

*A Truck # is restricted to one PO Item at a time.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_TruckForBody.png)

*A Truck # should not be assigned to a Chassis Asset Type.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_TruckNumReq.png)

*A Truck # is required for the given Asset Type.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_InvalidModelYear.png)

*The supplied Model Year is not valid.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_InvalidMonthly.png)

*The Monthly Capital amounts need to be numeric and in whole dollars.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_ExportedPO.png)

*The PO you are trying to edit has already been exported. This PO cannot be edited in this tool. Please make any changes you want in Toolbox.*
</div>