---
title: Bud Capital Input Tab
layout: custom
keywords: [Training, Capital, Capital Input]
description: 
---

## Overview

**Purpose**:  Save new Capital PO Items for a specific District, and pull in existing Capital PO information.

**Filter Options**:

* **District** - *Required*. Individual District, no Groupings
* **Budget Year** - *Required*. Needs to be in YYYY format

![](/images/WCNTraining/Capital/CapitalInput_FullView.png)

## To Delete PO Items

To delete a PO Item, select *Delete!* from the **Delete on Save** drop-down in the column farthest to the left. The PO Item will be deleted on the Save.

![](/images/WCNTraining/Capital/CapitalInput_Delete.png)

## Asset Information

All PO items require the following attributes: Asset Type, SubType, Life, A/R, N/U, and in some cases a Truck #. The drop-downs for the various columns are dependent on one another. For example, when you select an Asset Type, the Subtype dropdown will regenerate to the available options.

![](/images/WCNTraining/Capital/CapitalInput_AssetInfo.png)

The **A/R** column stands for *Add* or *Replace*, and **N/U** stands for *New* or *Used*.

>**Things to Remember**
>* If you change the Asset Type of an existing PO Item, be sure to change the SubType and other information correctly. Otherwise, validation on the Save will stop you and give a warning to update your PO Item options.
>* If the Asset Type is a Truck, you need to include a Truck Ctr. # with the PO Item. On the pull, the drop-down options will automatically provide all available Truck numbers.

## Replacement Info

This hidden grouped section is for the Replacement Information. You will need to unhide this section if you selected *R* in the **A/R** column earlier. Specifically, the **FAS #** and **Replacements Notes** are required.

![](/images/WCNTraining/Capital/CapitalInput_ReplacementInfo.png)

## Do I have security rights to Save from this Input File?

To find if you can save to the Capital Input Tool, please check out the [ Tools Controlled by the Control Center ](/bApps/InterjectTraining/Budget/ControlCenterSecurity.html#the-capital-input-tool) page.

## Drills

You can drill on any row to bring up more detailed information for the Capital amounts belonging to the PO Item in the Capital Change Query.

![](/images/WCNTraining/Capital/CapitalInput_DrillWindow.png)

**Drill to CC Query for Change History** opens the [ Capital Change Query report ](/bApps/InterjectTraining/Capital/CCQuery.html).
![](/images/WCNTraining/Capital/CapitalInput_CapitalChangeDrill.png)

## Common Save Errors

![](/images/WCNTraining/Capital/CapitalInput_Error_TypeSubType.png)

*The chosen SubType does not belong to the Asset Type selected. Please select a valid Subtype from the available drop-down list.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_ReplacementReqs.png)

*If the PO Item is a Replacement (R in A/R), both an FAS # and Replacement Note are required (in the hidden Replacement Info section)*

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

*The local version of the report has been been changed and will no longer save correctly. Get the newest version of the report from the library.*

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

*The selected Truck # New/Used status does not match the N/U column. Either update the N/U column accordingly, or select a different valid Truck #.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_DuplicateTruck.png)

*A Truck # is restricted to one PO Item at a time.*

___
![](/images/WCNTraining/Capital/CapitalInput_Error_TruckForBody.png)

*A Truck # should not be assigned to a Chassis SubType.*

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
