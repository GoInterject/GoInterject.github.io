---
title: Interject Documentation > L2.2 Create> Customer Orders
layout: custom
---
* * *

##  **Overview**

This page illustrates the process of building a Customer Order report from scratch and uses the multi-row option to provide a more advanced presentation. Here you will get a better understating of the  [ ReportRange() ](wIndex/ReportRange_61702199.html) as well as JfreezePanes() function. 

  * ####  Building the Report 

  * ####  Customizing the Report 

  * ####  Editing the Function 

  * ####  Adding a Multi-Row Range 

  * ####  Closing Up the Report 




###  Building the Report: 

**Step 1:** This process begins with the INTERJECT **[ Report Builder ](https://interject.atlassian.net/wiki/display/ID/Interject+Ribbon+Menu+Items#InterjectRibbonMenuItems-ReportBuilder) ** . Open the Report Build as illustrated below. There is a drop down list of  [ Dataportals ](/wApps/Common-Dataportal-Index_127795984.html) that can be chosen  . An INTERJECT Dataportal is a pre-configured data query that is setup so spreadsheet users can easily direct data into their own spreadsheet reports. Dataportals can be setup to access databases or cloud data and are either setup by INTERJECT developers or an IT team. 

![](attachments/128421638/129433048.png)

  


**Step 2:** For this Customer Orders report, use the NorthwindCustomerOrders Dataportal. Once chosen, click the **Build Report Formula** button. 

![](attachments/128421638/129241822.png)

  


A new sheet should be added that looks like the screenshot below. Now the report is ready for further customization. 

![](attachments/128421638/129082135.png?width=800)

  


  


###  Customizing the Report: 

**Step 1:** Before you pull in the data, type **SAVEA** in the CustomerID field to shorten the data-set and make it easier to work with. 

![](attachments/128421638/129211594.png?width=800)

  


**Step 2:** Now use the **[ Pull on Data ](/wPortal/INTERJECT-Ribbon-Menu-Items_83689479.html) ** menu item to grab the data.   
![](attachments/128421638/129211677.png)

  


You can now see all the columns available in the Dataportal will be shown by default with the column names on the first row. 

![](attachments/128421638/129211646.png)

  


**Step 3:** Select a few columns for our report by copying a few of the column names to the Column Definition area on row 2. Follow the animiated GIF below to multi-select CustomerID, CompanyName, ContactName, OrderID, OrderDate, OrderAmount, Freight, and TotalAmount. You can select them all individually while holding the Ctrl key. Then you can copy and paste them all at once in cell B2. 

![](attachments/128421638/129211838.gif)

  


**Step 4:** Once the Column Definitions are set, clear the report using the Pull Data menu item and choose the **[ Clear Data ](https://interject.atlassian.net/wiki/content-only/viewpage.action?pageId=83689479&iframeId=fallback-mode&user_key=ff8080814d41a454014d440734dd0001&user_id=MariaH&xdm_e=https://interject.atlassian.net/&xsm_c=fallback-mode-fake-key__15033515684256504&cp=/wiki&cv=0.0.0-fallback-mode&lic=none#InterjectRibbonMenuItems-PullData) ** button. 

![](attachments/128421638/129212023.png)

  


The cleared report should look like this. 

![](attachments/128421638/129212050.png?width=900)

  


  


###  Editing the Report Function 

**Step 1:** For easy editing, open the function wizard by clicking on the function in cell C6 and clicking the **fx** button. 

![](attachments/128421638/129212178.png?width=900)

  


**Step 2:** First, set the ColDefRange to the second row (2:2) so that INTERJECT knows which row is the Column Definition. 

![](attachments/128421638/129213799.png?width=900)

  


**Step 3:** Next, scroll down further in the argument list to change **UseEntireRow** from **FALSE** to **TRUE** . Also change **PutFieldNamesAtTop** from **TRUE** to **FALSE** . These are not required but are best practice. ****

![](attachments/128421638/129213828.png?width=900)

  


**Step 4:** Now pull the report to see the data. 

![](attachments/128421638/129213866.png)

  


It should pull only the data for the columns you requested in the column definitions. 

![](attachments/128421638/129214070.png?width=900)

  


**Step 4:** Now that you have the data, remove any access text and formatting not needed for the final report. Use the before and after screenshots to note what should be cleared. 

**Before:**

![](attachments/128421638/129214136.png?width=900)

  


**After:**

** ![](attachments/128421638/129214172.png?width=900) **

  


**Step 5:** With all the extra text gone, you can now remove the unneeded rows, 11:15 and 19:20. 

**Before:**

** ![](attachments/128421638/129214297.png) **

  


**After:**

** ![](attachments/128421638/129214391.png) **

  


###  Adding Multi-Row Range: 

Continue adding column labels and applying the multi-row feature. 

**Step 1:** To set up the column labels in row 17, copy the text from row 2 in the Column Definitions. You can change the column labels further, but the text is fairly descriptive. 

![](attachments/128421638/327123020.jpg)

  


Then you can add bold and underline the headers to add emphasis. 

** ![](attachments/128421638/129239395.png?width=900) **

  


**Step 2:** Now set up the report to use three rows for every record returned. Navigate to the top of the page and insert two rows between row 2 and 3. The end result should resemble the image below. 

** ![](attachments/128421638/129139254.png?width=900) **

  


Now add column definitions on row 3. You are going to add shipping information to the second row so the report does not have to be as wide. Leave the third row as a spacer between the next record. 

** ![](attachments/128421638/129139381.png?width=900) **

  


**Step 4:** Next, you need to add to our formatting Range. Before now, you have not needed to setup a Formatting Range since it defaults to the first row where the data is placed. With a multi-row report, a Formatting Range is required. Just like with column definitions, first add two more rows to the section, as shown below. Whatever the formatting, formulas or values placed in the Formatting Range will be copied first to new data rows before the data is placed on the worksheet. 

** ![](attachments/128421638/129139643.png?width=900)   
**

Below is an example of what a Formatting Range might look like. It is okay to leave values there to visualize the formatting as long as it is understood the columns noted in the Column Definition will override the cells with data. 

** ![](attachments/128421638/129140019.png?width=900) **

  


**Step 5:** Before pulling the data, you need to edit the [ ReportRange() ](https://interject.atlassian.net/wiki/spaces/ID/pages/61702199/ReportRange) Formula in C10 so that it uses the Column Definition and Formatting Range set in the previous steps. 

![](attachments/128421638/129240605.png)

  


Set the ColDefRange to **2:4** and FormatRange to **6:8** as illustrated below. 

![](attachments/128421638/129240976.png)

  


**Step 6:** Now pull the data to see how it looks! 

![](attachments/128421638/129243194.png)

  


The report should look something like this. Note that the text gets overwritten with the data pulled by INTERJECT. However, the formatting, row size, text type, and text that does not coincide with the column definitions stay the same. 

![](attachments/128421638/129140494.png)

###  Final Steps 

**Step 1:** Now setup a [ jFreezePanes ](/wIndex/128552956.html) function so you can quickly unfreeze and freeze the panes at the correct position. First, setup the jFreezePane function in cell F10 by going into the report formulas section and typing **=jFreezePanes()** , then click the **fx** button to open the Formula Wizard. 

![](attachments/128421638/129243135.png)

  


**Step 2:** In the FeezePanesCell argument, input **A22** . This will set the row that will be frozen above A22, and also where you will place the column headers. For the AnchorViewCell argument, type in A14 to mark that row as the top of the visible report. This sets the top of the report that will be visible to the user. 

![](attachments/128421638/129243159.png)

  


**Step 3:** Use JFreezePanes to toggle panes off and on. Go to the **[ Quick Tools ](https://interject.atlassian.net/wiki/spaces/ID/pages/83689479/Interject+Ribbon+Menu+Items#InterjectRibbonMenuItems-QuickTools) ** menu in the INTERJECT Ribbon, then click **Freeze/Unfreeze Panes.**

![](attachments/128421638/129243116.png)

  


This will freeze the panes, and the report will look something like below. 

![](attachments/128421638/129141350.png)

  


Every report will be specific to the company's needs and best practices, but a completed report should look like this: 

![](attachments/128421638/129241589.png)

  


  


##  Related Links: 

[ Customer Aging ](/wAbout/Customer-Aging_128091294.html)

[ Modify: Customer Aging ](/wGetStarted/128428927.html)

[ Updating the Report Library ](/wGetStarted/L10-Updating-the-Report-Library_62849583.html)

[ Interject Ribbon Menu Items ](https://interject.atlassian.net/wiki/spaces/ID/pages/83689479/Interject+Ribbon+Menu+Items)

[ Basics of Report Formulas ](/wAbout/Basics-of-Report-Formulas_61702189.html)

  

