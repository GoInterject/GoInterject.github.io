---
title: Interject Documentation > L4.1 Drill> Customer Aging
layout: custom
---
* * *

  


##  **Overview**

In this example, you will be setting up a simple drill to the customer orders history. It is a great use case for creating your first drill. 

By clicking one of the links below you  can go directly to any section of this walk-through. 

  *     * ####  Unfreezing the Tab 

    * ####  Building the Drill 

    * ####  Final Result




###  Unfreezing the Excel Sheet 

**Step 1:** You begin with a special version of the Customer Collections Report that has the drill removed. You can download with the file with the following link, [ Interject_CustomerDemo.xlsx ](attachments/128421015/129045397.xlsx) . 

![](attachments/128421015/128945869.png)

  


**Step 2:** Unfreeze the panes. Go to the **View** tab, find the **Freeze Pane** option, and select **Unfreeze Panes** .  ![](attachments/128421015/128945828.png)

  


**Step 3:** When you scroll up to rows 7 through 9, you will see where this file was set up to have 3 ReportDrill() functions. This is where you will create your first drill formula for this example. 

![](attachments/128421015/128945970.png)

###  Build the Drill 

**Step 1:** To begin, select cell C7 and type **=ReportDrill()** . Then click the _**fx** _ button to bring up the Function Wizard. 

![](attachments/128421015/128946249.png)

  


**Step 2:** Now select the ReportCellToRun argument and type in **CustomerOrderHistory!C10** . This is the cell location of the Report Formula in the target report that you will be drilling to.  In the screenshot below, you can see the specific cell you are drilling to in the CustomerOrderHistory tab. 

You are going to skip the ReportCodeToRun argument, since that is used only when drilling to a separate workbook from the Report Library. 

![](attachments/128421015/129051005.png)

  


**Step 3:** Next, we will use the  TransferPairs argument to note which cell values in the source worksheet will be transferred to the target worksheet during the drill operation. To do this we use special functions to pair the source cells to the target cells. Type **[ PairGroup(Pair()) ](wIndex/PairGroup_81756186.html) ** in the TransferPairs argument to get it started. You will return to add more to this argument. 

![](attachments/128421015/129051087.png)

  


**Step 4:** Then you will specify the name for the drill. In this case you will type **Drill to Customer Order History** . 

![](attachments/128421015/129051186.png)

  


**Step 5:** Complete the TransferPairs argument. In the Formula Bar, click inside the word **Pair()** within the text **PairGroup(Pair())** . See the illustration below. Once this is done, the Function Wizard will automatically change to help with the Pair() function. Type **B22:B24** in the **From** argument. This is the column where the CustomerID is going to be presented in the source report. By noting a range from row 22 to 24 in column B, INTERJECT will expand that range to the data presented in this source report. 

![](attachments/128421015/129051405.png)

  


**Step 6:** Select the Target input field and navigate to the **CustomerOrderHistory** tab, where you will choose which cell you want to receive the value. In this case you want C23. Excel should automatically fill in the argument with the text **CustomerOrderHistory!C23** . Click OK to finish updating the function, and it will automatically go back to the source worksheet. 

![](attachments/128421015/129051477.png)

  


**Step 7:** Now that you have created the drill, you can use **[ Pull Data ](/wPortal/INTERJECT-Ribbon-Menu-Items_83689479.html) ** to bring in the customers to the source worksheet. 

![](attachments/128421015/129244768.png)

  


Below is when the data is pulled. 

![](attachments/128421015/129732772.png)

  


###  **Final Results**

**Step 1:** To demonstrate the new drill, **right click** on one of the customer rows and select Drill on Data. The drill option **Drill to Customers Orders History** should be shown. 

![](attachments/128421015/129733323.png)

  


**Step 2:** Click on the button **Do Drill** and INTERJECT will navigate to the target worksheet, bring in the CustomerID selected by the filter, then run the report. The screenshot below should resemble the result. 

![](attachments/128421015/129733466.png)

  


You completed the drill. You can return to the source worksheet, **Customer Aging** , and re-freeze the panes, clear the report, and save it. Now it is ready to be published to the users. 

  


![](attachments/128421015/129733490.png)

##  Related Links: 

[ L1.1 Modify: Customer Aging ](wGetStarted/L-Modify-CustomerAging_128428927.html)

[ L2.1 Create: Customer Aging ](wGetStarted/L-Create-CustomerAging_128429314.md)

[ INTERJECT Ribbon Menu Items ](INTERJECT-Ribbon-Menu-Items_83689479.html)

  


  


  

