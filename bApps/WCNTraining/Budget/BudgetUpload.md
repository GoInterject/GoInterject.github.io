
---
layout: custom  
title:  "Budget Template - Budget Upload Tab"
date:   2019-06-25 15:43:02 -0700
keywords: Training, Budget, Budget Upload
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

Region Controllers can upload Budget amounts to more than one district at a time

To delete a PO Item, toggle the **Delete on Save** drop-down in the furthest left column to *Delete!*. The PO Item will be deleted on the Save.

![](/images/WCNTraining/Capital/CapitalInput_Delete.png)

## Asset Information

All PO items require the following attributes: Asset Type, SubType, Life, A/R, N/U, and in some cases a Truck #. The drop-downs for the various columns are dependent on one another. For example, when you select an Asset Type, the Subtype dropdown will regenerate to the available options.

![](/images/WCNTraining/Capital/CapitalInput_AssetInfo.png)

The **A/R** column stands for *Add* or *Replace*, and **N/U** stands for *New* or *Used*.

>**Things to Remember**
>* If you change the Asset Type of an existing PO Item, be sure to change the SubType and other information correctly. Otherwise on the Save the validation will stop you and tell you to update your PO Item options.
>* If the Asset Type is a Truck, you need to include a Truck Ctr. # with the PO Item. On the pull the drop-down options will automatically provide all available Truck numbers.
