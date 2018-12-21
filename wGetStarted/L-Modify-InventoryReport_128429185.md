---
title: Interject Documentation > L1.2 Modify> Inventory Report
layout: custom
---
* * *

##  **Overview**

In this example you ill be modifying a fixed report, going over how to add a row to the report as well as add an extra column. 

  *     * ####  Setting up the Report 

    * ####  Adding a Row 

    * ####  Adding a Definition Column 

    * ####  Closing up the Report 




###  Setting up the Report 

**Step 1:** First, go to the [ Report Library ](/wAbout/Report-Library-Basics_61702517.html) and select the Interject Inventory Demo report. 

![](attachments/128429185/129012106.png)

  


It should look like this when opened. 

![](attachments/128429185/128487782.png)

**  
**

Because the report is already complete, it is necessary for the example to delete a row before starting. This will simulate a fixed report that has a missing row. 

**Step 2:** Right click row 18, **Dairy Products** , and choose delete. 

![](attachments/128429185/128494299.png)

  


With the row deleted, the report should now be structured as shown. 

![](attachments/128429185/128463111.png)

  


You can now begin modifying the report for this lesson. 

Back to Top 

###  Adding a Row to the Report 

**Step 1:** First, use [ **Pull Data** ](https://interject.atlassian.net/wiki/display/ID/Interject+Ribbon+Menu+Items#InterjectRibbonMenuItems-PullData) menu item so you can see how this report has been configured and to show that a row is missing from the main section. 

![](attachments/128429185/128509994.png)

  


Here you can see that the category **Dairy Products** is below the main body of the report. This is considered a **Leftovers** section and will present rows that were not included in the fixed report area above between rows 15 and 22. 

![](attachments/128429185/128463268.png)

  


Add **Dairy Products** back to the main body of the report. 

** Step 2:  ** To add another category, unfreeze the panes. Open the View Ribbon in Excel and select the **Freeze Panes** drop-down. Then choose **Unfreeze Panes** . 

![](attachments/128429185/128463293.png)

  


By unfreezing the report, the formulas and parameters that were hidden before can now be viewed. If this is the first time seeing these, go to [ Basics of Report Formula's ](https://interject.atlassian.net/wiki/display/ID/Basics+of+Report+Formulas) to learn more. 

You can see this by opening these sections that **Dairy Products** is being pulled in the **Leftovers** section configured in cell B25. Since you want Dairy Products with the other categories in the main report, you will need to add it. 

![](attachments/128429185/128463332.png?width=880)

  


**Step 3:** To move **Dairy Products** into the main section, insert a row. Right click a row anywhere between 15 and 23 and copy it.  By copying a row, it will ensure that the new row inserted keeps the same formatting as the other rows. 

![](attachments/128429185/128494351.png)   


  


**Step 4:** Now, right click again anywhere in the same range and insert the copied row.   


![](attachments/128429185/128494398.png)

  


This will temporarily create two **Grains/Cereals** sections and you will edit the new one. 

![](attachments/128429185/128487333.png)

**  
**

**Step 5:** Once you have the new row inserted, you will need to change the category name in the new row to **Dairy Products** in column B. This is called the **Row Definition** and is how INTERJECT knows what data to place in that row. In this example, the column E formula references column B, but this does not have to be the case. You can control what the user sees in column E. 

Below, you changed the definition for row 18 to **Dairy Products** and are ready to pull data again so that the row has correct data. 

![](attachments/128429185/128487378.png)

**  
**

**Step 6:** Because you copied an existing row, the data for Row 18 is still duplicated from Grains/Cereals, [ Pull ](https://interject.atlassian.net/wiki/display/ID/INTERJECT+Add-In+Menu+Items#INTERJECTAdd-InMenuItems-PullData) the Report to refresh the data and check your work. Data should update for row 18, and **Dairy Products** should disappear from leftovers area. 

![](attachments/128429185/128487447.png)   


Back to Top 

###  Adding a New Definition Column 

As it is, the report does not describe what each of the categories contains, so add a description column to the report so you know exactly what is in each category. 

**Step 1:** First, add the column to the report. Call it **Description.** Be sure to make it wide enough to contain the longer description text as shown below. 

![](attachments/128429185/128593093.png)

  


**Step 2:** Now add the Column Definition value in the top part of the report so that INTERJECT knows to bring in data to that column. 

![](attachments/128429185/128593158.png)

  


**Step 3:** Pull the data to make sure everything works as expected. 

** ![](attachments/128429185/128781487.png) **

  


This will refresh the data and pull in the new description data, placing it in the specified column. 

![](attachments/128429185/128594005.png)

Back to Top 

###  Preparing the Report To Share 

Before saving back changes to the Report Library, clear the data so the next user does not see data that may not be relevant to their cost center. 

**Step 1:** Here clear the report of all of the data. 

![](attachments/128429185/129012288.png)

  


Now that the data is cleared, use the [ jFreezePanes ](/wIndex/128552956.html) function to re-freeze the panes on the report so that only the main report area is visible. This report has the jFreezePanes formula in cell G4. 

jFreezePanes is not configured for all the example reports, but it is easy to setup when needed. 

![](attachments/128429185/128552501.png)

  


**Step 2:** To use the [ jFreezePanes ](/wIndex/128552956.html) , click the Quick Tools button in the INTERJECT Ribbon and select **Freeze/UnFreeze Panes** . 

![](attachments/128429185/129012329.png)

  


This will automatically freeze the panes to the pre-configured position. 

![](attachments/128429185/128552850.png)

  


And that is all there is to it. You have now modified the Inventory Report with an additional column and row. To know how to save report changes to the Report Library, [ click here ](https://interject.atlassian.net/wiki/display/ID/Updating+the+Report+Library) . 

Back to Top 

##  Related Links: 

[ Inventory Reports ](/wAbout/Inventory-Reports_128091499.html)

[ L3.1 Inventory Fixed ](/wGetStarted/L3.1-Inventory-Fixed_128429456.html)

[ Basics of Report Formulas ](/wAbout/Basics-of-Report-Formulas_61702189.html)

[ L10 Updating the Report Library ](/wGetStarted/L10-Updating-the-Report-Library_62849583.html)

[ INTERJECT Ribbon Menu Items ](/wPortal/INTERJECT-Ribbon-Menu-Items_83689479.html)
