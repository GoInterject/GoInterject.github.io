---
title: Budget Reports
layout: custom
keywords: [Report, Epicor, Accounts]
headings: []
links: ["/images/Train/Budget1.png", "/images/Train/Budget2.png"]
description: Step by step guide on adding budget columns to your report templates.
---

If budgeting has been imported during the initial data load, you can easily add budget columns to your generated report templates using the following steps:


> To Do
>
> **Step 1:** Change the Source Cell to "Budget" by typing it into the cell.
>
> **Step 2:** Add a new description "Budget Code" and a placeholder cell for Budget Code. See row 36 below.
>
> **Step 3:** Expand the Column Definitions section.
>
> **Step 4:** Fill in the appropriate cell in the column definitions section. In the example below, it's row 7 column H. The formula should point to the Budget Code cell in the header. A good practice is to write the formula =IF(H36=””,””,H36).
> ![Account Rollup](/images/Train/Budget1.png){: .center-image }
>
> **Step 5:** Choose a Budget Code that will be used for the column. In the example below, the budget code B16 is used.
> ![Account Rollup](/images/Train/Budget2.png){: .center-image }
>
> **Note:** To see available Budget Codes, go to the COA Segment Lookup report from the Report lLibrary. Then choose the "InterjectSegment" tab, select the BudgetCode segment, and pull the data.
>
>
>
>
>
>
>
>
>
>
