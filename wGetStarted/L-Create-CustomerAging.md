---
title: "Lab Create: Customer Aging"
layout: custom
keywords: [ range, report, build, example]
description: In this page you will see the process of building a Customer Aging report from scratch to better understand reports and also get a clearer illustration of the Interject Report Range data function
---
* * *

##  **Overview**

In this page you will see the process of building a Customer Aging report from scratch to better understand reports and also get a clearer illustration of the Interject [ ReportRange() ](/wIndex/ReportRange.html) data function. 

<blockquote class=lab_info>
  If you are following the Training Labs, this is Lab 3.1. Note: The Report Library at Training Labs for this lab will be blank as you are creating a report from a new blank Excel sheet.
</blockquote>

###  Building the Report 

**Step 1:** This process begins with the Interject [ Report Builder ](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#report-builder) . Open the Report Build as illustrated below. There is a drop down list of  [ Dataportals ](/wApps/Common-Dataportal-Index.html) that can be chosen  . An Interject Dataportal is a pre-configured data query that is setup so spreadsheet users can easily direct data into their own spreadsheet reports. Dataportals can be setup to access databases or cloud data and are either setup by Interject developers or the IT team. 

![](/images/L-Create-CustAging/01.png)   

**Step 2:** For this Customer Aging report, use the NorthwindCustomers Dataportal. Once chosen, click the **Build Report Formula** button. 

![](/images/L-Create-CustAging/02.png)


A new sheet should be added that looks like the screenshot below. Now the report is ready for further customization. 

![](/images/L-Create-CustAging/03.png)


###  Getting Started 

**Step 1:** Begin by putting the filter value **Market** in C16 so you can limit the data pulled to just a few records that have a Company Name that contains the word **Market** . 
<br>
![](/images/L-Create-CustAging/08.png)
<br>


Next, use the [ **Pull Data** ](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) menu item. 
<br>
 ![](/images/L-Create-CustAging/09.png)
<br> 


You can see below, that all the columns available in the Dataportal will be shown by default with the column names on the first row.
<br>
![](/images/L-Create-CustAging/10.png)   
<br>

**Step 2:** Select a few columns for our report by copying a few of the column names to the Column Definition area on row 2. Follow the animated GIF below to multi-select CustomerID, CompanyName, ContactName, ContactTitle, City, Country, Phone, 30Days, 60Days, and 90Days. You can select them all individually while holding the Ctrl key. Then you can copy and paste the values all at once in cell B2. 

![](/images/L-Create-CustAging/11.gif)

  


**Step 3:** Now that you have the columns, move the **Phone** column title to column F instead of H. First select the entire column H. Then hold the Shift key and hover your cursor over the left border of Column H. Left-drag the column left until the pop-up says "F:F" and then let go.
<br>
![](/images/L-Create-CustAging/12.png)     
<br>

**Step 4:** Now that the Column Definitions are set, clear the report for the next step. 
<br>
![](/images/L-Create-CustAging/13.png)
<br>
  


The cleared report should look like the screenshot below. 
<br>
![](/images/L-Create-CustAging/14.png)
<br>
  


**Step 5:** Now set up the ReportRange() formula to look to the Column Definition area that was just set. Select cell C6.  
<br>
![](/images/L-Create-CustAging/15.png) 
<br>

**Step 6:** Click the **fx** button as noted below to open the Function Wizard and add a ColDefRange. The ColDefRange argument should be empty at first. 


<br>
![](/images/L-Create-CustAging/16.png)
<br>
  


For this report, you will set the ColDefRange to the entire second row, 2:2.  
<br>
![](/images/L-Create-CustAging/17.png)
<br>
  


**Step 7:** Next, scroll down in the Function Wizard to view the **UseEntireRow** argument. Change from FALSE to TRUE. This is an optional step but is certainly a best practice. 
<br>
![](/images/L-Create-CustAging/18.png) 
<br>

**Step 8:** Before closing the Function Arguments, continue to scroll down so you can change the **PutFieldNamesAtTop** argument from True to False. This is not required but is a good practice. 
<br>
![](/images/L-Create-CustAging/19.png)
<br>
  


**Step 9:** When you re-pull the report, the selected 11 columns in the Column Definition should be the only columns showing. 
<br>
![](/images/L-Create-CustAging/19.png)
<br>

###  Final Result  

The data pulled should look like below. 

**Note** : Although not illustrated in the below steps, you can save typing in the column labels for later. Copy the Column Definition values in B2:L2 and **Paste Values** in B22:L22. These are the labels you can customize for users to view. 
<br>
![](/images/L-Create-CustAging/21.png)
<br>
  


**Step 1:** Do some quick formatting to clean up the report. Delete rows 21 through 22. 
<br>
![](/images/L-Create-CustAging/22.png)
<br>
  


**Step 2:** Next, you need to freeze the panes to hide the configuration area from the users. This can be done manually with the Excel menu item for freezing panes. But this is a good time to illustrate Interject's jFreezePanes() feature. First, setup the [ jFreezePanes ](/wIndex/jFreezePanes.html) function by entering **=jFreezePanes()** in F6 and click the **fx** button. 
<br>
![](/images/L-Create-CustAging/23.png)
<br>
  


In the FeezePanesCell argument, input A21 to mark that row as the top of the visible report. This sets the top of the report that will be visible to the user. For the AnchorViewCell argument, type in A15. This will set the row that will be frozen above A21, where you will place the column headers. 
<br>
<img src="/images/L-Create-CustAging/24.png" height="550px" width="773px">
<br>
  


Use the [ **Quick Tools** ](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#quick-tools) menu item in the Interject Ribbon so you can easily freeze the panes using the jFreezePanes formula you just configured. 
<br>
<img src="/images/L-Create-CustAging/25.png" height="750px" width="750px">
<br>
  


**Step 3:** The following should be the result after the panes are frozen. 
<br>
![](/images/L-Create-CustAging/26.png)
<br>
  


**Step 4:** This last view shows what the final report can look like when the report is complete. Add the column labels in row 20, the filter helper text in column D, and match the formatting. The data can be cleared and shared with other users as a search tool for customers. 
<br>
![](/images/L-Create-CustAging/27.png)
<br>
  


Finally, clear the report, refreeze the panes, and upload it to the [ Report Library ](/wGetStarted/L-Create-UpdatingReportLibrary.html).

  

