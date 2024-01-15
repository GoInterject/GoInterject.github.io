---
title: Report Templates
layout: custom
keywords: [Report, Epicor, Accounts]
headings: ["Account Rollup Screen", "Building Your Rollups", "Build Your Rows", "The Report Template", "Adding Company Columns"]
links: ["/bApps/bFinancials/Configure.html", "/images/Train/BuildReport1.png", "/images/Train/AcctRollupNew.png", "/images/Train/AcctRollup2.png", "/images/Train/BuildRow.png", "/images/Train/RowTemp4.png", "/images/Train/FRxCatalogRowTemp.png", "/images/Train/rowtemp2c.png", "/images/Train/ReportTemp.png", "/images/Train/DropRow.png", "/images/Train/TypeName.png", "/images/Train/HeaderNames.png", "/images/Train/ShowDetail.png", "/images/Train/DetailShot.png"]
description: Step by step guide on using Interject Financials - Epicor Enterprise financial report templates.
---

Aside from your seeded Transactional Reports, Interject Financials - Epicor Enterprise allows you to build flexible financial statements from scratch using existing FRx row templates as a guide. **Note that you must complete the initial review and confirmation steps in the Configuration Manager before you can begin creating Rollups and Row Templates for financial reports**. Those steps are described in detail on the [Configure](/bApps/bFinancials/Configure.html) page.

The following steps walk through a single Balance Sheet creation, but the process will be the same for other sheets, such as P & Ls.

> To Do
>
> **Step 1:** From the Configuration Manager screen, click on the "Setup/Review Rollups" link to go to the Rollup Manager
>
> **Step 2:** On the Rollup Manager screen, click on "Segment" in the "Add New Rollup" section and select a segment from the list. We'll choose "Accounts" for this example.
>
> **Step 3:**  Hit "Click to Add".
>
> **Note:** If you're choosing to reference FRx row templates, it's best to have the FRx Catalog open in a separate window.
>
> ![Transaction Report 1](/images/Train/BuildReport1.png){: .center-image }
>
>

### Account Rollup Screen

After hitting "Click to Add", a new sheet will open with an empty template. This is where you'll set up the account rollup definitions and validation 

> To Do
>
> **Step 1:** Title your "Rollup Code" with something descriptive. Rollup code titles do not accept spaces and must be 8 characters or fewer
>
> **Step 2:** Type a brief description of the Rollup you're creating
>
> **Step 3:** Click the "Apply Validation" link and choose "Yes"
>
> **Step 4:** In the "Validation Definition" field, begin typing the formula **=JCombineSmart\(\)**, then double-click that formula from the menu
>
>  - **Step 5a:** With the formula open, select all of the "Row Definitions" in the FRx Row Format tab of the catalog, then hit enter. This will populate the "Validation Definition" with every FRx Definition needed.
>
>  - **Step 5b:** Now select the the cell containing all the "Validation Definitions," copy the cell, and paste it back into the same cell as **Values** using the "Special Paste" option in Excel
>
> ![Account Rollup](/images/Train/AcctRollupNew.png){: .center-image }
>

### Building Your Rollups

> To Do
>
> **Step 1:** Now write the codes for each Rollup in the "Rollup Section" of your template using the FRx Row Format screen. These will correspond to the subtotals in the FRx Row Template catalog report. The necessary prefixes will be attached automatically.
>
> **Step 2:** In each row with a code, designate the "Order" in magnitudes of at least ten, then in the "Detail Account Definiton" column, use **=JCombineSmart\(\)** again, selecting all necessary rows for each subtotaled section from the FRx Row Template report.
>
> **Step 3:** Hit Ctrl+Shift+U or the "Save" Button to save
>
>  ![Account Rollup](/images/Train/AcctRollup2.png){: .center-image }
>

### Build Your Rows

> To Do
>
> **Step 1:** Go back to the Configuration Manager Welcome screen and click the link to "Setup/Review Report Templates"
>
> **Step 2:** In the "Row Template Manager", click "Acct Rollup" to choose an account. Then hit "Click to Add."
>
> ![Account Rollup](/images/Train/BuildRow.png){: .center-image }
>
> **Step 3:** In the new sheet that opens, give the row template a name, a description, and choose the "Rollup Definition" that you created in the previous step.
>
> **Step 4:** Choose whether or not to enable distribution, pick a rollup segment and code, then choose the fiscal period to seed into the report template. 
> ![Account Rollup](/images/Train/RowTemp4.png){: .center-image }
>
> **Step 5:** From the Report library, open the FRx Catalog Report and go to the FRx Row Template tab.
>
> **Step 6:** Choose the FRx Row Format you need from the dropdown.
>
> **Step 7:** Click the "Pull FRx" button.
> ![Account Rollup](/images/Train/FRxCatalogRowTemp.png){: .center-image }
>
> **Step 8:** Now, using the rollup code prefix, enter into the Row Template configuration the detail codes corresponding to each of the subtotal sections in the FRx Row Template Report. You can click on "Row Type" to toggle between "Detail," "Subtotal," or both.
>
> **Note:** When there is a calculation, as noted by a "+" rather than "TO," you will need to build those claculation using the following syntax: ".." for ranges, "," for discreet additions, and ",-" for subtractions.
>
> **Step 9:** Add rows where necessary, and choose "detail," "subtotal," or "blank" to skip a row.
>
> **Step 10:** Enter your subtotal calculations in the "Subtotal Calc" column based on the row numbers you define for each entry.
>
> **Step 11:** Hit Ctrl+Shift+U or the Save button to save your work, then hit "Click to Create Report."
>
> ![Account Rollup](/images/Train/rowtemp2c.png){: .center-image }
>
>

### The Report Template

> To Do
>
> **Step 1:** Once the Report Template is open, choose "Open Period" from the "Fiscal Period" link. You can leave "Company" open if desired
>
> **Step 2:** Next, change the Actual columns from PTD to YTD
>
> **Step 3:** In the right Actual column, click into the date and enter **=EDate\(** then click the "Fiscal Period" you chose previously, and close the argument with ",0". This will make that column an absolute reference to your period of interest
>
> **Step 4:** In the date cell of the left column, enter **=EDate\(\133,-1\).** This will reference the period of interest and subtract one month. You can add further columns to the right, using this notation, to build out your report completely
> ![Account Rollup](/images/Train/ReportTemp.png){: .center-image }
>
> **Step 5:** Now hit Ctrl+Shift+J or the Pull Data button on the Interject Ribbon
>

### Adding Company Columns
You may easily add columns to your generated report templates 

> To Do
>
> **Step 1:** Expand the "Column Definition" row by clicking on the "+" sign at the top left of the report
> ![Account Rollup](/images/Train/DropRow.png){: .center-image }
> 
> **Step 2:** Right click a column and choose "Insert Columns". 
> 
> **Step 3:** In row 2 of the column you added, type in "Company", and in the row to its right, type "CompanyName." This will bring in the company code and the friendly company name next time you pull.
> ![Account Rollup](/images/Train/TypeName.png){: .center-image }
>
> **Step 4:** Add headings in the report area above where the data will come in.
>
> **Step 5:** Choose your parameters.
>
> ![Account Rollup](/images/Train/HeaderNames.png){: .center-image }
>
> **Step 6:** Pull the report, then expand any of the collapsed rows to see the company code and name in the detail rows.
> ![Account Rollup](/images/Train/ShowDetail.png){: .center-image }
>
> ![Account Rollup](/images/Train/DetailShot.png){: .center-image }
>

