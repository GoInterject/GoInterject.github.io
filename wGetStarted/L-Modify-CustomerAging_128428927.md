---
title: Interject Documentation > L1.1 Modify> Customer Aging
layout: custom
---
* * *

##  ** Overview  **

Here, you will modify the Customer Aging Demo used in the [ Customer Aging Walk-through ](/wAbout/Customer-Aging_128091294.html) to show the total of invoices due from companies. You will filter for companies with the word **Market** in their name to keep the list short. You will build a **Total** column to receive the sum of each individual company's unpaid invoices. Once complete you will use these totals to build a Report total, which allows us to see all invoices  due  .   


Go directly to any section of this walk-through by clicking one of the links below. 

  *     * ####  Opening the Report and Pulling Data 

    * ####  Creating a Total Column 

    * ####  Creating a Report Total Cell 




###  Opening the Report and Pulling Data 

**Step 1:** Use the [ Report Library ](/wAbout/Report-Library-Basics_61702517.html) to find the Customer Aging Summary titled **Interject Customer Collections** . 

![](attachments/128428927/128781338.png)



Once open, it should look like this:   


![](attachments/128428927/128431844.png)

**  
**

**Step 2:** Type **Market** in the Company Name field. 

![](attachments/128428927/128455133.png)

  


Now run the **[ Pull Data ](/wPortal/INTERJECT-Ribbon-Menu-Items_83689479.html) ** , which will pull the invoice data for all companies with the word **Market** in their name. 

![](attachments/128428927/128455197.png)

  


Once it is populated with the data, the report should look like the image below. 

![](attachments/128428927/128455311.png)

Back to Top 

###  Creating a Total Column 

**Step 1:** In order to add a **Totals** report, you need a column to accept the data. Here you will add it at the end, after the **90 Days** column. 

![](attachments/128428927/128455422.png)

  


It is easier to copy the format used for one of the existing columns, then paste it to the new **Total** Column. To accomplish this, select the **90 Days** column. 

![](attachments/128428927/128460545.png?width=782)

  


Then select the **Format Painter** in the Home Ribbon. 

![](attachments/128428927/128429661.png?width=400)

  


**Step 2:** Once you are prepared to copy the format, select the columns you want to total. Make sure to select the same number of rows used in the rest of the report. Once the format has been copied over add the column name **Total** . 

**Before:**

![](attachments/128428927/128455701.png?width=782)

**  
**

**After:**

![](attachments/128428927/128455677.png?width=782)

  


Now that the report is formatted for the new data, you need to add formulas for calculating the total values. 

  


**Step 3:** In this instance, you are going to write a SUM Formula to get our totals. A simple example of this formula is shown in the image below. 

**Note:** This report is setup to place data starting in row 23, and that same row is considered the Formatting Range. You must put the formula on this row to be copied down with the data. 

![](attachments/128428927/128455653.png?width=782)

  


Remember to include the **=** in our formula, otherwise Excel will simply read this as plain text. **I23** tells Excel where the first column value is, and **L23** designates the last value. The colon represents all the cells in between. When we have this written out, our Excel sheet shows where we will be summing values. 

**  
**

**Step 4:** Instead of copying this formula to each row once step 3 is completed, pull the entire report again. 

![](attachments/128428927/128456062.png)

  


Notice that when you pull the data, the new formula is applied to all the new rows. 

![](attachments/128428927/128456139.png)

Back to Top 

###  Creating Totals on top of the Report 

**Step 1:** For this example, you need more than just the individual totals; you need a Report Total of these invoices. To build this, you have to add more SUM Formulas. You will format the cells above the table, making it clearly visible. To do this, select cell H19 and label it **Report Total:** . 

** ![](attachments/128428927/128502083.png) **

**  
**

**Step 2:** Once you select the cell you want for the Report Total, write a formula for the Total column and work your way left. Make sure to select down to the anchor row, one row below the existing data. The anchor row will always be the row below the data and will move up and down as data is cleared and pulled. **  
![](attachments/128428927/128502338.png?width=782) **

  


**Step 3:** Once the Total column is done you can copy the formula to the left until you reach **Current** . Once the paste is complete, we can view the Report Total for each column. 

** ![](attachments/128428927/128563170.gif?width=782) **

  


**Step 4:** To remain consistent with other formatting, shade the **Report Total** row gray.   
![](attachments/128428927/128503084.png?width=782)

**  
**

**Step 5:** When the formatting is done, the report should look like the screenshot below. 

![](attachments/128428927/128503112.png)

  


By clearing and re-pulling, you ensure that the changes worked. 

![](attachments/128428927/128503235.png)

  


You can see in the screenshot below that even though you cleared the report, the formula is still there in cell N23. 

![](attachments/128428927/128508830.png)

  


**Step 6:** Once the report has been cleared, re-pull the report. 

![](attachments/128428927/128508888.png)

  


The report is complete, you have added a total for each client and a summary total on the top by column.  ![](attachments/128428927/128508923.png)

  


You can continue learning by reading how to save these changes back to Report Library [ here ](https://interject.atlassian.net/wiki/display/ID/Updating+the+Report+Library) . 

Back to Top 

##  Related Links: 

  


[ Customer Aging ](Customer-Aging_128091294.html)

[ L2.1 Create: Customer Aging ](/wGetStarted/128429314.html)

[ L10 Updating the Report Library ](/wGetStarted/L10-Updating-the-Report-Library_62849583.html)

[ INTERJECT Ribbon Menu Items ](INTERJECT-Ribbon-Menu-Items_83689479.html)
