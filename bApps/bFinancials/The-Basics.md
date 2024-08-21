---
title: Train
filename: "The-Basics.md"
layout: custom
keywords: [Report, Epicor, Accounts]
headings: ["Interject for Financials Quick Reference", "Important Interject Hotkeys", "Important Formulas", "Important Actions on the Interject Ribbon Menu", "The Basics of Working with Interject for Financials", "Using the Report Library", "Pull Data", "Drilling Between Reports"]
links: []
image_dir: "Interject-Financials"
images: [
	{file: "InterjectFinancialsRbnMnu", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "InterjectFinancialsReportLib", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "InterjectFinancialsPull", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "09", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "11", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "InterjectFinancialsDrill", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}
	]
description: A quick guide to get users started navigating Interject for Financials Epicor Enterprise.
---

## Interject for Financials Quick Reference

### Important Interject Hotkeys 

> To Know
>
> <span class="hotkey">Ctrl+Shift+J:</span> Pulls data into your report after selecting parameters from the dropdowns in the parameter section.
>
> <span class="hotkey">Ctrl+Shift+K:</span> Drills through a selected value to a more detailed report \(drills are available only in predefined cells).
>
> <span class="hotkey">Ctrl+Shift+U:</span> Saves data or configurations back to a database.
>
> <span class="hotkey">Ctrl+Shift+L:</span> Opens the report library, where you can access your organization's published reports.
>

### Important Formulas

> To Know
>
> **=JCombineSmart\(\):** Concatenates, orders, and removes duplicates of selected range to enter validation definitions or detail row definitions when building financials reports.
>
> **=EDate\(\):** Use to set the period of interest as an absolute reference to the fiscal period filter when building financial reports. Pass ",-\[chosen cell\]" when building subsequent columns from the period of interest.
>
>

### Important Actions on the Interject Ribbon Menu 

>To Know
>
> **1:** Use to access and share report in your organization.
>
> **2:** Use to pull data into the report after selecting parameters from the dropdowns in the parameter fields. You may also use the <img class="logo" style="height: 22px; width:84px; vertical-align: middle; border:none; display:inline; " src="/images/Interject-Financials/RibbonQkRef/Pull.png"> button in the report paramter area.
>
> **3:** Use to save data or configurations back to a database.
>
> **4:** Use to Drill through data into more detailed reports. You can go back one drill by pressing the **Return From Drill** button to the right of the drill button.
>
> ![Open report link button](/images/Interject-Financials/InterjectFinancialsRbnMnu.png){: .center-image }
>




<!-- THIS DIRECTION HAS CHANGED. SEE ABOVE FOR MORE CURRENT METHOD
## The Basics of Working with Interject for Financials
The following basic steps will help you navigate through the Interject Financials - Epicor application including finding and opening your governed reports form Report Library, pulling and saving data, drilling through reports, and exporting static files when necessary.

#### Using the Report Library
Use the Report Library to access and share reports. Any computer on your network can access shared reports through Interject, provided users are authorized. Reports can also be versioned, so reverting to a previous report is simple.


> To-do
>
> **Step 1:** Use Ctrl-Shift-L or click the Report Library button on the Interject ribbon.
> Note: If not logged in already, you will be prompted to do so.
>
> **Step 2:** Select your desired folder on the left. 
>
>  **Step 3:** Pick a report link on the right.
>
> **Step 4:** Always check the **Link Version** before opening a report. **The most recent version is green**, and that’s the version you should typically open. Each report is described briefly in the Link Version window and its available versions are listed. 
>
> **Step 5:** Click Open Link to open the report.
>
>![Open report link button](/images/Interject-Financials/InterjectFinancialsReportLib.png){: .center-image }


### Pull Data


> To-do
>
> **Step 1:** Click a parameter hyperlink and choose a parameter from the dropdown list.
>
> **Step 2:** Hit **Ctrl-Shift-J** or click **Pull Data** to the right of the parameter section. You can also use the Pull Data button on the left of the Interject Ribbon.
>
> ![Interject pull data in ribbon menu](/images/Interject-Financials/InterjectFinancialsPull.png){: .center-image }
>

<!--#### Save Data
You can save data back to the database or web API with the key command **Crtl-Shift-U**. You can also use the Save-Data button in the Interject Ribbon.
![Interject ribbon save button](/images/InterjectRibbon/09.png){: .center-image }

You can also clear any saved notes using the **Clear Save Notes** button in the save window. This removes all saved notes from the spreadsheet, but not from the database. Pulling the data again will pull saved notes back in. 
![Interject save window, clear saved notes](/images/InterjectRibbon/11.png){: .center-image }
-->
<!--
### Drilling Between Reports
Drilling through reports allows for faster navigation to various levels of reporting detail without having to find and open new files or workbooks. To activate an Interject drill:

>To-do
>
> **Step 1:** Select the cell or data to drill through
>
> **Step 2:** Hit **Ctrl-Shift-K** \(or use the Drill on Data button on the Interject Ribbon\)
>
> **Step 3:** Select the drill option in the Data Drill Window
>
> **Step 4:** Click Do Drill, or hit enter
>
> ![Interject drill steps](/images/Interject-Financials/InterjectFinancialsDrill.png){: .center-image }


<!-- ### Exporting Reports
It is important to note that the Report Library is where all governed and versioned reports should be published. The reports in Report Library are interactive, moving data from the DB to the spreadsheet, so the Excel files do not need to be saved to your hard drive. Since Report Library is version controlled and governed, you will always work with the latest reports and they will always be supported and accurate provided they have governing definitions.

When you need to distribute a report or save it in a folder, Interject’s Quick Export and Report Distribution features facilitate this. 

**Click the Export Book button** in the center of the Interject ribbon. Exporting reports simply makes copies of a report after it has been populated with selected data. The output can be handled in a number of ways. It can be done on the fly with a single open workbook, or it can be set up to distribute a comprehensive reporting book with multiple tabs curated for each user or department. If there are any special Interject formulas in the spreadsheet, like Data Cells, these can be removed when distributed so non-Interject users can view the report. Reports can also be sent as PDFs when MS Excel is not practical.The following options are available for exporting reports.

**Quick Export** copies a workbook while removing unwanted Interject formulas.

**Quick PDF** saves and opens a PDF document of the existing workbook.

**Distribution** is a deeply customizable process for creating reports and distributing them in various ways.

**Reporting Through Grouping Segments** allows for easier importing of data for larger, dynamic reports.
-->


