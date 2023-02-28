---
title: "Create: Updating the Report Library"
layout: custom
keywords: [upload, report library, template, report]
description: The report library is a way to share reports with other users on the team. The reports are uploaded to the library and can be accessed from any other computer using Excel and Interject. 
---
* * *

##  **Overview**

The report library is a way to share reports with other users on the team. The reports are uploaded to the library and can be accessed from any other computer using Excel and Interject. Interject spreadsheets can still be organized within Sharepoint or network folders, but Interject provides an easy versioning and release system to help ensure adequate controls. And it is available directly from within Excel. 

**Note:** Before beginning this walk-through, it is important to review the [ Report Library Basics ](/wAbout/Report-Library-Basics.html). 

<blockquote class=lab_info>
  If you are following the Training Labs, do not upload files to the Report Library.
</blockquote>

###  Saving a New Version 

**Step 1:** To save a new version, you will first make sure the report is saved. Be sure the workbook is cleared of its data, since the Report Library is only designed to share blank report templates and not reports that have user data. Select the File menu shown below. 

![](/images/L-Create-RepLib/01.png)

<br> 


Click **Save As**, and  choose a location where the file will be saved. If this file has already saved, you can simply choose **Save**. It is recommend that when updating a new version of the report, the file name should be slightly different that the previous version. Although not shown in the below example, often a version suffix like **FileName_v2.xlsx** is considered best practice. 

![](/images/L-Create-RepLib/02.png)   

<br> 


**Step 2:** Next, choose the Report Library menu item in the Interject ribbon. In this example, you will be updating the **Interject Customer Collections** report with a new version. 

![](/images/L-Create-RepLib/03.png) 

<br>

**Step 3:** Right click on the report, then click **Save Current Workbook**, and choose **Create New Version of "Interject Customer Collections"** Note: Since this demo report is not within the security rights to update, you may want to follow these steps using another report. 

![](/images/L-Create-RepLib/04.png)

<br>


**Step 4:** If the current file is not saved, the computer's local folder window will open and prompt you to choose a save location. If the file has already been saved, skip to the next step. 

**Step 5:** After the file is selected, you can edit the details of the report in the Report Library Link detail window that is shown below. 

1. Select a status from the dropdown menu. 
  * _Live_ : Standard users can only see live reports, so only use this when the report is ready to be published. 
  * _Test_ : In testing means the development is complete and is in the testing status. 
  * _Dev_ : In development by the report writers. 
  * _Superseded_ : This is a report that is no longer used but still available to admin users for review. 
2. Optionally, you can choose to enter a Version Name  and make a small note on the changes made. The note only allows 30 characters. 
3. Notice the Link Path is the same as the current file that was saved in earlier steps. It is recommended that you use new file names for newer versions of the report. 


 ![](/images/L-Create-RepLib/05.png)

<br>      

**Step 6:** Click the **Save** button to complete the save process. Next time the file is opened, the new version will be in the Report Library. And for the rest of your users, the next time they open the report it will automatically open the newest version. 

![](/images/L-Create-RepLib/06.png)

<br>

###  Saving a New Report 

**Step 1:** To save a new version, you will first make sure the report is saved first. And be sure the workbook is cleared of it is data since the Report Library is only designed to share blank report templates and not reports that have user data. Select the File menu shown below. 

![](/images/L-Create-RepLib/07.png)

<br> 

Click **Save As**, and  choose a location where the file will be saved. If you have already saved the file, you can simply choose **Save**. It is recommend that when updating a new version of the report, the file name should be slightly different that the previous version. Although not shown in the below example, often a version suffix like **FileName_v2.xlsx** is considered best practice. 

![](/images/L-Create-RepLib/08.png)

<br> 


**Step 2:** Next, click the Report Library menu item in the Interject ribbon. In this example, you will be saving **Interject Customer Collections** as the new file. 

![](/images/L-Create-RepLib/09.png)

<br> 


**Step 3:** Right click anywhere in the Report Links section. Click **Save Current Workbook**, then **Create New Link**. 

![](/images/L-Create-RepLib/10.png)   

<br>

**Step 4:** **** If the current file is not saved, the computer's local folder window will open and prompt you to choose a folder. If the file has already been saved, skip to the next step. 

  


**Step 5:** After the file is selected, you can edit the details of the report. 

1. Give the link a relevant and clear name. 
2. Give the link a clear description for others to see what the report does. It's important to write description clear enough for users to understand what the report is for. 
3. Select a status from the dropdown menu. 
  * _Live_ : Standard users can only see live reports so only use this when the report is ready to be published. 
  * _Test_ : In testing means the development is complete and is in the testing status. 
  * _Dev_ : In development by the report writers. 
  * _Superseded_ : This is a report that is no longer used but still available by admin users for review. 
4. Optionally, you can choose to enter a Version Name  and make a small note on the changes made. The note only allows 30 characters. 
5. Notice the Link Path is the same as the current file that was saved in earlier steps. 
6. Select the desired format to save the file. In this case, you will be using a **Report Library File**. This option stores the file centrally so it an be versioned only through the Report Library. There are other options to select a file on the network, a folder in the network, or a website URL. 
7. Select a documentation link for the report from the drop-down. In the example, you are going to use a website link to the [ Customer Aging Walk-through ](/wAbout/Customer-Aging.html). If possible, it is always advisable to provide documentation on your reports. 



![](/images/L-Create-RepLib/11.png)

<br> 


**Step 6:** Now select save, and the next time the Report Library is opened, the new report will be there. 

![](/images/L-Create-RepLib/12.png)

<br> 


###  Adding a Drill Code to a Report 

Drill Codes are important when using the Interject report drill feature discussed in the section [ Drilling Between Reports ](/wGetStarted/Drilling-Between-Reports.html). Drill Codes are needed when a drill needs to go to a separate workbook, and that workbook is saved in the Report Library. 

**Step 1:** To add Drill Codes to a report, you can amend the above steps and add drill codes to the Report Link Details window, as seen below. The Drill Codes must be unique to others that were saved prior. A report can have up to three drill codes, each pointing to different worksheet tabs. More are allowed, but you must contact Interject for assistance. 

![](/images/L-Create-RepLib/13.png)