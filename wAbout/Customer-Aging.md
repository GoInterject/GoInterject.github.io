---
title: Customer Aging
layout: custom
keywords: [customer aging, modify, drill, save, pivot table]
description: In this walk-through, you will open a basic aging summary and modify it to fit your specific needs. You will then drill into the details tab, take notes on any unpaid invoices, then save them back to the database.
---
##  **Overview**
---

This lab is a basic Customer Aging demonstration for tracking invoices for multiple customers. In this walk-through, you will open a basic aging summary and modify it to fit your specific needs. You will then drill into the details tab, take notes on any unpaid invoices, then save them back to the database. This Detail report will also provide the data needed to drill further into each order and customer. 

You can go directly to any part of this walk-through by clicking one of the links below.   


  * ####  Navigating to Aging Summary 

    * ####  Drilling to Detail 

    * ####  Saving the Data 

    * ####  Moving to a Pivot Table 

###  Navigating to the Aging Summary 

**Step 1:** Open the report **INTERJECT Customer Collections** under the INTERJECT Demos  in the [ Report Library ](wAbout/Report-Library-Basics.html) . 

![](attachments/128091294/129568273.png)

This will bring up the Customer Aging Summary. 

![](attachments/128091294/128404716.png)

**Step 2:** You can retrieve the data by clicking  [ **Pull Data** ](/wGetStarted/INTERJECT-Ribbon-Menu-Items_83689479.html#pull-data) in the INTERJECT menu and clicking **Pull Data** in the subsequent popup. 

![](attachments/128091294/128369916.png)

This will populate the data into the spreadsheet. 

![](attachments/128091294/128324822.png)

**Step 3:** Since you are not concerned with _all_ the customers right now-- you only need the status of those in the Market sector--filter **Market** in the **Company Name** filter. 

![](attachments/128091294/128361857.png)

Now use [ Pull Data ](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) again to refresh the data. 

![](attachments/128091294/128369955.png)

**Step 4:** Once the companies are pulled, you can see that **Save-a-lot-Markets** has invoices 90 days overdue! 

![](attachments/128091294/128222021.png)

Back to Top 

###  Drilling into the Aging Detail 

**Step 1** : Now, use the [ **Drill** ](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#drill-on-data) operation  on the Customer Aging Detail report for a closer look at the overdue invoices. Here you can select any cell on the row below because as long as you select a cell on the row with the overdue invoices the [ **Drill** ](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#drill-on-data)will take us to the details of that client's invoices.  

![](attachments/128091294/128363066.png)   

Once that cell is selected you can drill deeper into the data. Below are the descriptions for each step. 

  1. First, select cell or row to drill. 
  2. Select the Drill operation in the INTERJECT Ribbon.  
  3. Select the desired drill you would like to perform , in this case you are selecting **Drill to Aging Detail**.
  4. Complete the drill be selecting **Do Drill**.

![](attachments/128091294/128376566.png)   

This allows us to see which invoices have not been paid. As looking deeper into the report, notice that more recent invoices are paid, but the customer is struggling to pay past-dated invoices. 

![](attachments/128091294/128370262.png)

**Step 2:** Notice that Jose mailed a check for the first invoice and it should arrive on the 18th. However, you would still need to call about the other invoice and note what is discussed. 

![](attachments/128091294/128370300.png)

**Step 3:** Now that you have talked with Jose, you find out that he will be mailing the check with the overdue funds tomorrow. To keep from forgetting, you can add a note to your report. 

![](attachments/128091294/129568522.png)

Back to Top 

###  Saving the Data 

**Step 1:** Now that the notes are written down, you need click the [ **Save Data** ](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#save-data) operation to save the notes back to the database. 

![](attachments/128091294/129568557.png)

**Step 2:** To do this, click the [ **Save Data** ](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#save-data) menu in the INTERJECT Ribbon menu and the **Save Data** in the popup. 

![](attachments/128091294/128370470.png)

Notice the Save Results column and ensure that it was updated correctly and there were no errors.   

![](attachments/128091294/128370649.png)

**Step 3:** Once this is complete, use [ **Clear** ](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) and [ **Pull** ](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) the Customer Aging Detail report to ensure the note is saved in the database.    

![](attachments/128091294/128370922.png)

Clicking the [ **Clear** ](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) operation will remove any data that was pulled into the spreadsheet. 

![](attachments/128091294/128362550.png)   

Notice that the filters are not cleared, so a re-pull is easy. 

**Step 4:** Now you will use the [ **Pull Data** ](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) operation the data again to ensure it is completely refreshed. 

![](attachments/128091294/128371129.png)

You will see that the saved data was pulled back into the spreadsheet, confirming that it was saved correctly. 

![](attachments/128091294/128380536.png)

Now, you can move to a Pivot Table so that you can easily manipulate the data provided by the Customer Aging tab. 

Back to Top 

###  Moving to a Pivot Table 

**Step 1:** First, navigate to the Pivot table tab. 

To do this Click on the **PivotTableAndReportRun** tab. 

![](attachments/128091294/128362930.png)
  
For this example,you are going to use a Company Name **Market** filter to narrow our search just like you did for Customer Aging. 

![](attachments/128091294/128361333.png?width=880)   

**Step 2:** Now lets use [ **Pull Data** ](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) to retrieve the data. 

![](attachments/128091294/129568892.png?width=857)

From pulling, you can see that Save-a-lot-Markets has already paid their invoices for 1998 but are behind on previous invoices. 

![](attachments/128091294/128371693.png)

If you want even more specific detail though, such as month-to-month information. You can alter the Pivot table to accommodate this. 

**Step 3:** Click anywhere inside the Pivot table to bring up the table's field list. 

![](attachments/128091294/128361591.png)   

**Step 4:** Now you can drag the Year-Mth box in the Row Labels to the column labels. 

![](attachments/128091294/128298833.gif?width=200)

Notice that you do not need to use the[ **Pull Data** ](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) is needed to view the new layouts. 

![](attachments/128091294/128299178.png)

From here you can see that Save-a-lot Markets had large invoices in July and August that are not payed. However, you can also see the effort to pay off those invoices in the following months by the over-payments they have made.  Take note of this activity and proceed to the next report: [ Inventory Report Walk-Through. ](wAbout/Inventory-Reports.html)

##  Related Links: 

[ Lab 1.1 Modify: Customer Aging ](wGetStarted/L-Modify-CustomerAging.html)

[ Lab 2.1 Create: Customer Aging ](/wGetStarted/L-Create-CustomerAging.html)

[ INTERJECT Ribbon Menu Items ](INTERJECT-Ribbon-Menu-Items.html)

[ Inventory Reports ](/wAbout/Inventory-Reports.html)

  

