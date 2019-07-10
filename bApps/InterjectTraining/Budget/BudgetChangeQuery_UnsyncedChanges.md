---
title: Unsynced Changes Tab
layout: custom
keywords: [Training, Budget, Budget Change Query, Unsynced]
description: 
---

## Overview

**Purpose**:  This new tab highlights all budget changes that have not been synced to Interject yet, either because they are saved after Corp Cutoff or BOD.

**Filter Options**:

* **District** - *Required*. Restricted to one District only. No groupings or ranges allowed
* **Year** - *Required*. Needs to be in YYYY format
* **Currency** - *Optional*. Blank defaults to your home district currency. Other options are USD or CAD
* **Exclude IC** - *Required*. Drop-down options are FALSE or TRUE. If set to TRUE, then In-terCompany accounts are removed from the pull

![](/images/WCNTraining/Budget/BudChangeQuery_Unsynced_FullView.png)

The budget numbers pulled in are grouped into three sections. On the far left are all the numbers synced to Interject, the middle are the amounts not yet in Interject, and the far right is the delta in between.

## Latest Unsynced Change Info

The latest save change info is brought into the tool in a hidden section near the top filters. It provides information on the saves that have not yet been synced to Interject, including how many saves are queued up to sync.

![](/images/WCNTraining/Budget/BudChangeQuery_Unsynced_ChangeInfo.png)