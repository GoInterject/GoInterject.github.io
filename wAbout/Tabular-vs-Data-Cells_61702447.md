---
title: Tabular vs Data Cells
layout: custom
---

INTERJECT supplies two very different ways to pull data into spreadsheets: **Tabular** and **Data Cells.** These two approaches help cover the variety of today's industry needs. 

In most of the user documentation, the instruction is focused on **Tabular** because they run much faster, can access real-time data, and utilize server resources more efficiently. As a result, they are used more frequently in large organizations. Although **Data Cells** have limitations (detailed below), they are more flexible for ad hoc reports and are easier to get started with. 

###  Tabular 

Tabular reporting is closely associated with standard reporting tools. Simply choose fields for each column, setup the level of detail, specify the rows to receive data, and the results populate the spreadsheet. Results can be broken into subtotaled sections, which are common to financial statements. 

Understanding how rows and columns intersect to place data is important and requires some training. The result is an extremely fast report that can be published or distributed and easily read by users who desire reports in spreadsheets without any additional work. They are also instantly shareable to users who don't have INTERJECT installed.

###  Data Cells 

Data Cells are focused on a single formula that can be placed anywhere in the spreadsheet and can ask for any financial number for a summary thereof. For example, you can set up a Data Cell to retrieve Net Income for YTD July 2017 for the Western Division excluding the NW districts and excluding inter-company accounts. 

Once this single formula approach is understood, there is no limit to creating needed combinations. Typically, this is an easier method to start writing custom reports. However, they must be exported to share with non-INTERJECT users. Given their greater flexibility, report run times are higher than Tabular reports, and more server resources are required. Fortunately, users can continue to work with spreadsheets while Data Cell reports finish calculating. 

###  What is Common Between Data Lists and Data Cells 

Tabular reporting and Data Cells were designed to work together for the most flexibility. These are some of their common traits: 

  1. Both will pull data using the same [ "Pull Data" ](/wPortal/INTERJECT-Ribbon-Menu-Items_83689479.html) menu action. There is nothing new to learn when changing from one method to the other. 
  2. Data Cells can be used with Tabular methods to create custom columns that aren't easily available from the data source. 
  3. Both can be shared with users that do not have  INTERJECT  installed, however Data Cell reports must be exported with the [ "Export Book" ](https://interject.atlassian.net/wiki/content-only/viewpage.action?pageId=83689479&iframeId=fallback-mode&user_key=ff8080814d41a454014d440734dd0001&user_id=MariaH&xdm_e=https://interject.atlassian.net/&xsm_c=fallback-mode-fake-key__7191363262446606&cp=/wiki&cv=0.0.0-fallback-mode&lic=none#InterjectRibbonMenuItems-ExportBook) menu item before they can be shared. 



  

