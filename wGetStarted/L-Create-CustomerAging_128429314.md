---
title: Interject Documentation > L2.1 Create> Customer Aging
layout: custom
---
* * *

##  **Overview**

In this page you will see the process of building a Customer Aging report from scratch to better understand reports and also get a clearer illustration of the INTERJECT report formula [ ReportRange() ](/wIndex/61702199.html) . 

There are three parts to building a simple report, click one of the links below to explore. 

  * ####  Building the Report 

  * ####  Customizing the Report 

  * ####  Final Result 




### 

###  Building the Report 

**Step 1:** This process begins with the INTERJECT [ Report Builder ](https://interject.atlassian.net/wiki/display/ID/Interject+Ribbon+Menu+Items#InterjectRibbonMenuItems-ReportBuilder) . Open the Report Build as illustrated below. There is a drop down list of  [ Dataportals ](/wApps/Common-Dataportal-Index_127795984.html) that can be chosen  . An INTERJECT Dataportal is a pre-configured data query that is setup so spreadsheet users can easily direct data into their own spreadsheet reports. Dataportals can be setup to access databases or cloud data and are either setup by INTERJECT developers or the IT team. 

** ![](attachments/128429314/128555750.png)   
**

**  
**

**Step 2:** For this Customer Aging report, use the NorthwindCustomers Dataportal. Once chosen, click the **Build Report Formula** button. 

** ![](attachments/128429314/128562892.png) **

**  
**

A new sheet should be added that looks like the screenshot below. Now the report is ready for further customization. 

![](attachments/128429314/128586565.png)

  


**   
**

###  Customizing the Report 

**Step 1:** Remove the parameter **IsMissingCRMID** that is noted below in cell B19. It is not necessary for this report example. 

** ![](attachments/128429314/128586510.png) **

**  
**

**Step 2:** Next, select **** the [ ReportRange() ](https://interject.atlassian.net/wiki/spaces/ID/pages/61702199/ReportRange) formula in order to delete its reference to **IsMissingCRMID** that you just removed above. Go to cell C6 and edit the formula. Remove the reference by removing C19 from the ReportRange formula. 

** ![](attachments/128429314/128586748.png) **

**  
**

This will remove the filter reference from the ReportRange(), and you can see the updated reference shown below. 

** ![](attachments/128429314/128586685.png) **

  


**Step 3** **:** Now clear the rest of the text you do not need for this report. Using the screenshot below as a guide, clear ranges encircled in red. 

![](attachments/128429314/129013931.png)

  


The report should look similar to the screenshot below. Now, put the filter value **Market** in C16 so you can limit the data pulled to just a few records that have a Company Name that contains the word **Market** . 

![](attachments/128429314/129013899.png)

###  Getting Started 

**Step 1:** Next, use the **[ Pull Data ](https://interject.atlassian.net/wiki/display/ID/Interject+Ribbon+Menu+Items#InterjectRibbonMenuItems-PullData) ** menu item. 

** ![](attachments/128429314/129014075.png) **

**  
**

You can see below, that all the columns available in the Dataportal will be shown by default with the column names on the first row. **  
**

** ![](attachments/128429314/129014131.png) **

**  
**

**Step 2:** Select a few columns for our report by copying a few of the column names to the Column Definition area on row 2. Follow the animated GIF below to multi-select CustomerID, CompanyName, ContactName, ContactTitle, City, Country, Phone, 30Days, 60Days, and 90Days. You can select them all individually while holding the Ctrl key. Then you can copy and paste them all at once in cell B2. 

** ![](attachments/128429314/129015366.gif) **

  


**Step 3:** Now that you have the columns, move the **Phone** column title to column F instead of H. Simply select the entire column H, then hold the Shift key while you move the column after column E. 

** ![](attachments/128429314/129015531.png)   
**

**  
**

**Step 4:** Now that the Column Definitions are set, clear the report for the next step. 

![](attachments/128429314/129042368.png)

  


The cleared report should look like the screenshot below. 

![](attachments/128429314/129042390.png)

  


**Step 5:** Now set up the ReportRange() formula to look to the Column Definition area that was just set. Select cell C6. 

** ![](attachments/128429314/129112240.png) **

**  
**

**Step 6:** Click the **fx** button as noted below to open the Function Wizard and add a ColDefRange. The ColDefRange argument should be empty at first. 

![](attachments/128429314/129113393.png)

  


For this report, you will set the ColDefRange to the entire second row, 2:2.  ![](attachments/128429314/129113795.png)

  


**Step 7:** Next, scroll down in the Function Wizard to view the **UseEntireRow** argument. Change from FALSE to TRUE. This is an optional step but is certainly a best practice. 

** ![](attachments/128429314/129112353.png) **

**  
**

**Step 8:** Before **** closing the Function Arguments, continue to scroll down so you can change the **PutFieldNamesAtTop** argument from True to False. This is not required but is a good practice. 

** ![](attachments/128429314/129112465.png) **

  


**Step 9:** When you re-pull the report, the selected 11 columns in the Column Definition should be the only columns showing. 

** ![](attachments/128429314/129113028.png) **

###  Final Result 

### 

The data pulled should look like below. 

**Note** : Although not illustrated in the below steps, you can save typing in the column labels for later. Copy the Column Definition values in B2:L2 and **Paste Values** in B26:L26. These are the labels you can customize for users to view. 

** ![](attachments/128429314/129113306.png) **

  


**Step 1:** Do some quick formatting to clean up the report. Delete rows 21 through 25. 

![](attachments/128429314/129042821.gif)

  


**Step 2:** Next, you need to freeze the panes to hide the configuration area from the users. This can be done manually with the Excel menu item for freezing panes. But this is a good time to illustrate INTERJECT's jFreezePanes() feature. First, setup the [ jFreezePanes ](/wPortal/INTERJECT-Ribbon-Menu-Items_83689479.html) function by entering **=jFreezePanes()** in F6 and click the **fx** button. 

![](attachments/128429314/129731976.png)

  


In the FeezePanesCell argument, input A21 to mark that row as the top of the visible report. This sets the top of the report that will be visible to the user. For the AnchorViewCell argument, type in A15. This will set the row that will be frozen above A21, where you will place the column headers. 

![](attachments/128429314/129731258.png?width=773)

  


Use the **[ Quick Tools ](https://interject.atlassian.net/wiki/spaces/ID/pages/83689479/Interject+Ribbon+Menu+Items#InterjectRibbonMenuItems-QuickTools) ** menu item in the INTERJECT Ribbon so you can easily freeze the panes using the jFreezePanes formula you just configured. 

![](attachments/128429314/129043495.png)

  


**Step 3:** The following should be the result after the panes are frozen. 

![](attachments/128429314/129732273.png)

  


**Step 4:** This last view shows what the final report can look like when the report is complete. Add the column labels in row 20, the filter helper text in column D, and match the formatting. The data can be cleared and shared with other users as a search tool for customers. 

![](attachments/128429314/129731354.png)

  


[ Click here ](https://interject.atlassian.net/wiki/display/ID/Report+Library+Basics) to learn how to upload the new report to the Report Library. 

  


##  Related Links: 

[ Customer Aging ](/wAbout/Customer-Aging_128091294.html)

[ L1.1 Modify: Customer Aging ](/wGetStarted/128428927.html)

[ L10 Updating the Report Library ](/wGetStarted/L10-Updating-the-Report-Library_62849583.html)

[ INTERJECT Ribbon Menu Items ](INTERJECT-Ribbon-Menu-Items_83689479.html)

[ Basics of Report Formulas ](/wAbout/Basics-of-Report-Formulas_61702189.html)

  

