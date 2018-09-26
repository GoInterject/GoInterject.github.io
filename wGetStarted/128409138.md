---
title: Interject Documentation > L4.2 Drill> Inventory Report
layout: custom
---
* * *

##  **Overview**

In this example, you will view drilling between reports using the same Inventory reports created during the [ Real World Inventory Walk-through ](/wAbout/Inventory-Reports_128091499.html) . You will setup a drill between the **Inventory by Category** and **Inventory by Detail** pages of the workbook, then you will set up a hyperlink so the drill can be more intuitive to users. 

Jump to any section of this walk-through by clicking the links below. 

    * ####  Unfreezing the Report 

    * ####  Setting up the Drill 

    * ####  Creating Hyperlinks 




###  Unfreezing the Report 

**Step 1:** First, download the Inventory Report Template, [ Interject_InventoryDemo.xlsx ](/wGetStarted/128409138.html) . This file has been prepared specifically for this exercise. Once opened, it should look like the screenshot below. 

![](attachments/128409138/128880125.png)

**  
**

**Step 2:** Now unfreeze the panes to access the report formulas. 

![](attachments/128409138/128748653.png)

  


###  Setting Up The Drill 

**Step 1:** Type **=** [ **ReportDrill()** ](/wIndex/61702556.html) into cell C5. Then, click the **fx** button to bring up the Function Wizard. 

![](attachments/128409138/128748854.png)

**  
**

**Step 2:** Now type **InventoryByDetail!C4** into the ReportCellToRun argument to specify the range you want to navigate to. You will skipping the ReportCodeToRun argument since that is only used for drilling to other workbooks in the Report Library. 

![](attachments/128409138/128748915.png)

  


**Step 3:** Next use the  TransferPairs argument to note which cell values in the source worksheet will be transferred to the target worksheet during the drill operation. To do this, use special functions to pair the source cells to the target cells. Type  **[ PairGroup(Pair()) ](/wIndex/81756186.html) ** in the TransferPairs argument to get it started. 

![](attachments/128409138/128749450.png)

  


**Step 4:** In the Formula Bar, click within the word **Pair()** inside the text **PairGroup(Pair())** while the Function Wizard is open. See the illustration below. Once this is done, the Function Wizard will automatically change to help with the Pair() function. Type **B15:B23** in the From argument as shown below. Column B is where the CustomerID will be shown in the source report. By noting a range from row 22 to 24 in column B, INTERJECT will expand that range to the data that is presented in this source report. 

![](attachments/128409138/128749484.png)

**  
**

**Step 5:** Next, select the Target argument and navigate to the **InventoryByDetail** tab. You want to place the CustomerID in cell E11 during the drill operation. Excel will fill in the formula automatically based on where you click. Click **OK** to finish updating the function and it will take you back to the source report. 

![](attachments/128409138/128749597.png)

  


After pressing OK, the report formula should look as it does in the image below. 

![](attachments/128409138/128749630.png)

###  Creating Hyperlinks 

**Step 1:** Now you are going to create hyperlinks for the drill. First, highlight the cells you want to setup the hyperlink, then right click and choose **Link** . In some versions of Excel it will show as **Hyperlink** . 

![](attachments/128409138/327417870.jpg?width=720)

**  
**

****Note:** ** Each drill will need to be linked individually, not all at once. If they are linked all at once then the drills will not work as it will drill everything at once, rather than one at a time. 

**Step 2:** In the Hyperlink pop-up window, you will select **Place in This Document** . Then select **ScreenTip** , type **Interject Drill** , and press OK. Although this technically sets up a hyperlink to cell A1 in the same tab, INTERJECT will override the event so the INTERJECT drill will activate. 

![](attachments/128409138/128750025.png)

  


Once you select **OK** , the cells will be linked to the drill, as shown below. 

![](attachments/128409138/128750079.png)

  


When the panes are refrozen, the report should look like the image below. 

![](attachments/128409138/128750112.png)

  


**Step 3:[ Pull Data ](/wPortal/INTERJECT-Ribbon-Menu-Items_83689479.html) ** to see data for each category you just linked. 

![](attachments/128409138/129048733.png)

  


Here, you have the report pulled and are ready to go. 

![](attachments/128409138/129048764.png)

  


**Step 4:** Now that you have the data, and can click the hyperlink. As shown in the animated GIF below, click on **Totals for Grains/Cereals** and INTERJECT will drill to the detail of that category in the target worksheet. Hyperlinks only show the Drill window when there is more than one drill option setup. In this case, you only setup one drill and it goes there automatically. 

![](attachments/128409138/129077986.gif)

  


Hyperlinking Drills is a simple way to make INTERJECT reports faster and more user-friendly. Click [ here ](/wGetStarted/128409219.html) for the Financial Report Drill walk-through. 

  


##  Related Links:   


  


[ L1.2 Modify: Inventory Report ](/wGetStarted/128429185.html)

[ L3.2 Inventory Variable Report ](/wGetStarted/L3.2-Inventory-Variable-Report_127872532.html)

[ L4.3 Drill: Financial Report ](/wGetStarted/128409219.html)

[ INTERJECT Ribbon Menu Items ](INTERJECT-Ribbon-Menu-Items_83689479.html)

  

