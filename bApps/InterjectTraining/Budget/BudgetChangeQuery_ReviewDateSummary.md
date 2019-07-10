---
title: Review Date Summary Tab
layout: custom
keywords: [Training, Budget, Budget Change Query]
description: 
---

## Overview

**Purpose**: This tab of the Budget Change Query tool provides a summarized view of the budget amounts across account groupings up to their own Review Date timestamps.

**Filter Options**:

* **Year** - *Optional*. Blank defaults to next Budget Year. Needs to be in YYYY format
* **District/Grouping** - *Optional*. Blank defaults to all districts in your rights. Allows individual district, district ranges, or groupings
* **Currency** - *Required*. Options are USD or CAD
* **Exclude IC** - *Required*. Drop-down options are FALSE or TRUE. If set to TRUE, then InterCompany accounts are removed from the pull

![](/images/WCNTraining/Budget/BudChangeQuery_ReviewDateSummary_FullView.png)

## District List

The districts pulled into this tab all have budget amounts. If you pull on a district range or grouping, the comma list of districts represented are shown in the screenshot below.

![](/images/WCNTraining/Budget/BudChangeQuery_ReviewDateSummary_DistrictList.png)

## Review Date Buckets

The summed budget amounts are divided into the Review Date Buckets: **Corp Review Thru**, **Reg Review Thru**, **Reg Cutoff**, **Corp Cutoff**, and **After Corp Cutoff**.

The Review Date columns (*Corp Review Thru*, *Reg Review Thru*, *Reg Cutoff*, *Corp Cutoff*, and *After Corp Cutoff*) show the aggregated amounts of *ALL* budget saves up to their own Review Date timestamps.

![](/images/WCNTraining/Budget/BudChangeQuery_ReviewDateSummary_ReviewDateBuckets.png)

The *Change From* columns (*Changes from Reg Review Thru*, *Changes from Reg Cutoff*, *Changes from Corp Cutoff*, *Changes from After Corp Cutoff*) show ONLY the aggregated amounts to their specific Review Date Bucket timestamps.

![](/images/WCNTraining/Budget/BudChangeQuery_ReviewDateSummary_ChangesFrom.png)

### Districts with Different Review Dates

Since the summed amounts include multiple districts, it is important to remember that the different districts could have different Review Dates. In the example below, Districts 2041 and 2050 have different **Reg Review Thru** and **Reg Cutoff** dates.

![](/images/WCNTraining/Budget/BudChangeQuery_ReviewDateSummary_ControlCenterReviewDates.png)

On the *Review Date Summary Tab* the summed amounts for **Reg Cutoff** show changes for both districts up to their respective **Reg Cutoff** dates in Control Center. For 2041, that would be all saves up to *8/30/19 7:00 PM* and for 2050 it would be all changes up to *8/20/19 3:00 PM*.

![](/images/WCNTraining/Budget/BudChangeQuery_ReviewDateSummary_RegCutoffAmounts.png)

