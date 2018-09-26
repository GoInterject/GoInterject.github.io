---
title: Interject Documentation > L7 Special Column Definitions
layout: custom
---
* * *

##  **Overview:**

Special column definitions provide additional features to your reports  . There are three options: 

  1. ** Adding a cell comment  **
  2. **Adding a hyperlink to a web address**
  3. **Adding a custom drop down validation to each row**
  4. ** Adding multiple cell values stacked on a single cell  **



These additional features are added by editing the Column Definition Row. The Column Definition Row is a row that designates, and filters, the placement of information. For example, if your report is presenting the field “Company Name”, your Column Definition would have a cell with the value “Company Name”. To add one of these features to the cells in a column where the report is populated you use an identifier such as  **AddComm** for comments,  **hLink** for hyperlinks, and  **Valuelist** for a drop down list. This lab uses the **Customer Credits** report. 

### 

###  Special Cell Value Comment 

A comment is often used to note more detailed information about the data in a cell. Comments are useful when the information contained within them are not required but need to be referenced when you put your mouse over the cell. In this example you will add comments to the credit limit column to note who last changed the credit. 

To start, unfreeze the panes 

![](attachments/335183945/346194026.jpg)

  


In the Company Name field in cell  **C21** input  **Market** and  Pull the data 

![](attachments/335183945/346259541.jpg)

  


The report looks like this 

![](attachments/335183945/346194031.jpg)

  


Select cell  **H2** and input  **CreditLimit Addcomm:LastCredit**

![](attachments/335183945/346062917.jpg)

**Note:** **Addcomm** designates the type of special column that you are using and  **LastCredit** is the actual content in the comment 

  


Pull the data 

![](attachments/335183945/346095732.jpg)

  


Place your cursor over cell  **H27** and review the comment that is placed in the cell. Notice that the  **Credit Limit** column was pulled as it was before the changes but it has a comment associated with it that now details the changes made to that column. 

![](attachments/335183945/346194036.jpg)

**Note:** Not all of the cells have been changed, and so there is no comment created for those cells. 

### 

###  Special Cell Value Hyperlink 

Excel has two types of hyperlinks, the hyperlink property and the Hyperlink() spreadsheet function. This feature uses the spreadsheet function in the report so users can click to open specific web pages. In this example you will use INTERJECT to add hyperlinks to the address column of the report that links the address to a google map search. 

Select cell  **C2** and input  **CompanyName hlink:MapsURL**

![](attachments/335183945/346357890.jpg)

**Note:** The  **MapsURL** segment of the  **hlink** string designates a column built in the SQL stored procedure. The hlink string only links to a whole column of data you cannot concatenate values in excel, but can in the SQL stored procedure as long as it results in a single column. 

  


Pull the data 

![](attachments/335183945/346259546.jpg)

  


**CompanyName** is still pulled normally but instead of the normal dataset look, it will create a hyperlink formula. The  **Link Location** goes to Google Maps and searches for the full address for that company.concatenated with the address associated with each company. This way the location data is accessible but does not overcrowd the information while the  **Friendly Name** of the URL is the  **Company Name** . 

![](attachments/335183945/348684292.jpg)

Select cell  **C27** and notice that it takes you to Google Maps 

![](attachments/335183945/346161326.jpg)

**Note:** The addresses may not be valid as they are fabricated data from the Northwind Database. 

### 

###  Special Cell Value Validation List 

Inserting data validation dropdown lists are similar to the other special column definitions.  When used they create dropdown lists using comma delimited strings, with each value inside the string separated by commas.  In this example you will add data validation to the account freeze column to limit possible input values. 

For this example, use  **AccountFreeze** in cell  **K2** . 

Select the cell, then input  **AccountFreeze valuelist:FreezeOptions**

![](attachments/335183945/346259551.jpg)

  


**AccountFreeze** will be shown as a blank value but upon selecting the cell, you can see that there is a drop down list with the options  **Yes** or  **No** . If there was a comma separated list instead of  **FreezeOptions** , the value list would only include what is in the comma separated list. 

![](attachments/335183945/346062922.jpg)

Through using this feature with INTERJECT, you can have a different validation list for every row in your report. Even though this is not shown in this example, if you wanted to select a city name inside of a state, it is possible to have the validation list only show the cities available within the state which would have to change based on the row the data is on. 

### 

###  Stacking Special Cell Types 

Excel allows users to have multiple special cell values attributed to a single cell. This is also the case when using INTERJECT integration. You can add multiple cell value types in the column definitions of the report. 

For this example, use  **Company Name** cell  **C2**

Select the cell, then input  **CompanyName hlink:MapURL** **addcomm:AddressLong**

![](attachments/335183945/346357895.jpg)

  


Pull the data 

![](attachments/335183945/346194044.jpg)

  


Hover your mouse over cell  **C27** and it will have a comment attributed to the cell along with the hyperlink. 

![](attachments/335183945/346128491.jpg)

  


Click on the hyperlink in cell  **C27** and  notice that the functionality of the hyperlink is unaltered and that the comment brought back the address that is used in the google map search. 

![](attachments/335183945/346161326.jpg)

If there are any additional special column features that are not listed here or you have any questions, please contact INTERJECT at info@gointerject.com 

  

