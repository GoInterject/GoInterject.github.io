---
title: Detail Tab
layout: custom
keywords: [Training, Budget, Budget Change Query]
description: 
---

## Overview

**Purpose**: This tab of the Budget Change Query tool provides a detailed overview of budgets with several filtering options.

**Filter Options**:

* **Year** - *Optional*. Blank defaults to next Budget Year. must be YYYY format
* **District/Grouping** - *Optional*. Blank defaults to all districts in your rights. Allows individual district, district ranges, or groupings
* **Account/Grouping** - *Optional*. Blank defaults to all accounts. Allows individual account, account ranges, or groupings
* **Currency** - *Required*. Options are USD or CAD
* **Exclude IC** - *Required*. Drop-down options are FALSE or TRUE. If set to TRUE, then InterCompany accounts are removed from the pull
* **Use Last Save** - *Optional*. Blank defaults to No. If set to Yes, only the latest ChangeID will pull in
* **Begin Date** - *Optional*. Blank defaults to the start of the budget season. If used, no data will pull in before the datetime stamp
* **End Date** - *Optional*. Blank defaults to the end of the budget season. If used, no data will pull in after the datetime stamp

![](/images/WCNTraining/Budget/BudChangeQuery_Detail_FullView.png)