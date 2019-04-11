---
title: Report Templates
layout: custom
keywords: [Report, Epicor, Accounts]
description: Step by step guide on using Interject Financials - Epicor financial report templates.
---

Aside from your seeded Transactional Reports, Interject Financials - Epicor allows you to build flexible financial statements from scratch using existing FRx row templates as a guide. **Note that you must complete the initial review and confirmation steps in the Configuration Manager before you can begin creating Rollups and Row Templates for financial reports**. Those steps are described in detail on the [Configure](docs.gointerject.com/bApps/bFinancials/Configure.html) page.

The following steps will walk through a single Balance Sheet creation, but the process will be the same for other sheets, such as a P and L.

> To Do
>
> **Step 1:** From the Configuration Manager screen, click on the "Setup/Review Rollups" link to go the Rollup Manager
>
> **Step 2:** On the Rollup Manager screen, click on "Segment" in the "Add New Rollup" section and select a segment from the list. We will choose "Accounts" for this example.
>
> **Step 3:** Click the "FRx Row Template" link and choose an FRx Row Template from the list. We'll choose "BALSHT04" for this example.
>
> **Step 4:** Hit the "Click to Add" button
>
> ![Transaction Report 1](/images/Train/BuildReport1.png){: .center-image }
>
>

### Account Rollup Screen

After hitting "Click to Add", a new sheet will open with the FRx row template reference on the left and an empty template on the right. This is where you'll set up the account rollup definitions and validation 

> To Do
>
> **Step 1:** Title your "Rollup Code" with something descriptive. Rollup code titles do not accept spaces and must be 8 characters or fewer
>
> **Step 2:** Type a brief description of the Rollup you're creating
>
> **Step 3:** Click the "Apply Validation" link and choose "Yes"
>
> **Step 4:** Click "Row Type" on the left sheet, and choose both "Detail" and "Subtotal", then click **Pull FRx**. This will help give you the "Detail Account Definitions" that define the rows of your report.
>
> **Step 5:** In the "Validation Definition" field, begin typing the formula **=JCombineSmart\(\)**, then double-click that formula from the menu
>
>  - **Step 5a:** With the formula open, select all of the "Row Definitions" under the FRx Template Reference and hit enter. This will populate the "Validation Definition" with every FRx Definition needed.
>
>  - **Step 5b:** Now select the the cell containing all the "Validation Definitions," copy the cell, and paste it back into the same cell as **Values** using the "Special Paste" option in Excel
>
> ![Account Rollup](/images/Train/AcctRollup1.png){: .center-image }
> 
>

### Building Your Rollups

> To Do
>
> **Step 1:** Now write the codes for each Rollup in the "Rollup Section" column of your template using the FRx Template References. These will correspond to the subtotals in the FRx Template Reference section. The necessary prefixes will be attached automatically.
>
> **Step 2:** In each row with a code, designate the "Order" in maganitudes of at least ten, then in the "Detail Account Definiton" column, use **=JCombineSmart\(\)** again, selecting all necessary rows for each subtotal section
>
> **Step 3:** Hit Ctrl+Shift+U or the "Save" Button to save
>
>  ![Account Rollup](/images/Train/AcctRollup2.png){: .center-image }
>

### Build Your Rows

> To Do
>
> **Step 1:** Go back to the Configuration Manager Welcome screen and then click the link to "Setup/Review Report Templates"
>
> **Step 2:** 
>
>
>
>