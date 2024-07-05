---
title: Install
filename: "PrepSpecFile.md"
layout: custom
keywords: [Report, Epicor, Accounts]
headings: ["Preparing the FRx Report Specification File for Migration", "Finding the FRx Report Specification File", "Converting the .F32 file to an MS Access .MDB File", "Remove the Database Password"]
links: []
image_dir: "A-InitialDataLoad"
images: [
	{file: "FRXCompanyInfo", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "F32File", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SaveLocalFRX", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "ClickThroughErrors", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SaveNewFile", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "EnableContent", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "OpenOtherFiles", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "BrowseFile", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "OpenExclusive", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "UnsetPW", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}
	]
description: Step by step guide on data tier, initial data load, FRx Migration, and other key processes of installing of Interject for Financials Epicor Enterprise.
---

## Preparing the FRx Report Specification File for Migration
Before completing the FRx migration, you will likely need to find your FRx Report Specification file, convert it to an MS Access file type, and release any database password permissions. 


### Finding the FRx Report Specification File

> To Do
>
> **Step 1:** Open FRx Report Designer. Under the **Company** menu choose **Information**. Choose your company and write down the **Specification Set** used.
> ![](/images/A-InitialDataLoad/FRXCompanyInfo.png){: .center-image }
>
> **Step 2:** Go back to the **Company Menu** and select **Specification Sets**. Then, choose the specification set noted above and write down the **Location** of the .f32 file.
> ![](/images/A-InitialDataLoad/F32File.png){: .center-image }
>
> 

### Converting the .F32 file to an MS Access .MDB File 

> To Do
>
> **Step 1:** Copy the .F32 file to a temporary work directory on your local machine. Rename the file extension to .MDB, then open the file in MS Access.
>
> **Step 2:** Enter the database password \(contact your implementor for the password\). Click "Save As," then click OK on "Invalid Password" message. Re-enter password.
> ![](/images/A-InitialDataLoad/SaveLocalFRX.png){: .center-image }
>
> **Step 3:** Click through all "missing or broken references" messages.
> ![](/images/A-InitialDataLoad/ClickThroughErrors.png){: .center-image }
>
> **Step 4:** Select a path and provide a new file name, for example "FRxDemo_Interject.mdb." Click save.
> ![](/images/A-InitialDataLoad/SaveNewFile.png){: .center-image }
>
> **Step 5:** Click OK on the “Not a valid password” error and re-enter password. **Note:** You will be prompted to do this twice. Then enable content.
> ![](/images/A-InitialDataLoad/EnableContent.png){: .center-image }
>
> **Step 6:** Close MS Access.
>

### Remove the Database Password
**Note:** This requires the database to be opened in "Exclusive" mode.

> To Do
>
> **Step 1:** Open MS Access and choose to "Open Other Files."
> ![](/images/A-InitialDataLoad/OpenOtherFiles.png){: .center-image }
>
> **Step 2:** Choose "Browse."
> ![](/images/A-InitialDataLoad/BrowseFile.png){: .center-image }
>
> **Step 3:** Locate the file you renamed, select the drop-down next to "Open," and select "Open Exclusive."
> ![](/images/A-InitialDataLoad/OpenExclusive.png){: .center-image }
>
> **Step 4:** Under File, choose "Unset Database Password."
>
> ![](/images/A-InitialDataLoad/UnsetPW.png){: .center-image }
>
> **Step 5:** Re-enter the password, then close MS Access
>

You have now converted the .F32 file to an .MDB and removed the password requirement. Proceed now to the FRx Migration page.
