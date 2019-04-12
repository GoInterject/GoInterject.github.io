---
title: Localize
layout: custom
keywords: [Report, Epicor, Accounts]
description: Step by step guide on publishing custom-made reports to your company's report library in the Interject for Financials App for Epicor.
---


A subscription to Interject Financial - Epicor will provide a "Subscriptions" folder in the **Report Library** within the “Interject Financial Epicor” folder. The folder contains the latest versions of your transactional reports. A company or implementer may also choose to customize the parameters of these reports to better reflect company naming conventions. Following are the localization steps required to localize all transactional reports.

> To-do
>
> **Step 1:** Open the Interject Report Library and find the report to be localized. Right-click the Report Link and "View Details" of the report.
>
> ![Open Library](/images/Localize/01.png){: .center-image }
>
> **Step 2:** Write down the current "Data Drills for Link". You will need these links in a later step.
>
>  ![Record Drill Links](/images/Localize/02.png){: .center-image }
>
> **Step 3:** Exit the View Detail window and open the Report Link from the Interject Report Library.
>
> ![Exit Detail Window](/images/Localize/03.png){: .center-image }
>
> **Step 4:**  With the report open, go back to the Report Library, open the "Configuration Manager" in the Admin folder, and click on the "Review Segements" link to open that report.
>
>  **Step 5:** Now change the "Segment" filters in the report to match the Segment names in the Configuration screen. 
>
> ![Open Library](/images/Localize/SegNames.png){: .center-image }
> ![Exit Detail Window](/images/Localize/03.png){: .center-image }
>
> **Step 6:** After changing the Segment names in the report, save the file to your local drive.
>
>  **Step 7:** With the Excel file still open, go to the Report Library. Select the company folder, right click, and select “Add Subfolder”. Name the subfolder with the report name and press Enter to Save New Folder.
>  ![Open Library](/images/Localize/FileSave.png){: .center-image }
>
>  **Step 8:** Now select the new folder and right click in the “Report Links” area white space. Click on "Save Current Workbook", then select the "Create New Link (Save Required)" option.
>
> ![Open Library](/images/Localize/08.png){: .center-image }
>
>  **Step 9:** Create a report link by filling in the required fields: "Link Path", "Link Name", and "Status".  
> - Link Path is the file path of the locally saved report
> - Link Name is the name that will show in the Report Library
> - Status determines whether the report will be live or not
>
>
> **Step 10:** Now fill in the "Drill Code" and "Target Tab Name" using the information your wrote down in step # 2. Click "Save
> 
> ![Open Library](/images/Localize/CopyDrillCodes.png.png){: .center-image }
>
> **Step 11:** From the Interject Ribbon, click "Login" and enter your credentials if they are not saved. **It is important that you "reset" your login after each report localization**
>
> **Step 12:** Open the report library and check for the report under your company name folder.
>

