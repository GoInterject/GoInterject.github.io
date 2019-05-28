---
title: "Lab Drill: Customer Aging"
layout: custom
keywords: [drill, create, build, example]
description: In this example, you will be setting up a simple drill to the customer orders history. It is a great use case for creating your first drill.
---
* * *

##  **Overview**

In this example, you will be setting up a simple drill to the customer orders history. It is a great use case for creating your first drill. 




###  Unfreezing the Excel Sheet 

**Step 1:** You begin with a special version of the Customer Collections Report that has the drill removed. 

![](/images/L-Drill-CustAging/01.png)
<br>
  


**Step 2:** Unfreeze the panes. Go to the **View** tab, find the **Freeze Pane** option, and select **Unfreeze Panes**.  

![](/images/L-Drill-CustAging/02.png)
<br>

  


**Step 3:** When you scroll up to rows 7 through 9, you will see where this file was set up to have 3 [ReportDrill()](/wIndex/ReportDrill.html) functions. This is where you will create your first drill formula for this example. 

![](/images/L-Drill-CustAging/03.png)
<br>

###  Build the Drill 

**Step 1:** To begin, select cell C7 and type **=ReportDrill()**. Then click the _**fx** _ button to bring up the Function Wizard. 

![](/images/L-Drill-CustAging/04.png)
<br>
  


**Step 2:** Now select the ReportCellToRun argument and type in **CustomerOrderHistory!C10** . This is the cell location of the Report Formula in the target report that you will be drilling to.  In the screenshot below, you can see the specific cell you are drilling to in the CustomerOrderHistory tab. 

You are going to skip the ReportCodeToRun argument, since that is used only when drilling to a separate workbook from the Report Library. 

![](/images/L-Drill-CustAging/05.png)
<br>
  


**Step 3:** Next, we will use the  TransferPairs argument to note which cell values in the source worksheet will be transferred to the target worksheet during the drill operation. To do this we use special functions to pair the source cells to the target cells. Type [ **PairGroup(Pair())** ](/wIndex/PairGroup.html) in the TransferPairs argument to get it started. You will return to add more to this argument. 

![](/images/L-Drill-CustAging/06.png)
<br>
  


**Step 4:** Then you will specify the name for the drill. In this case you will type **Drill to Customer Order History**. 

![](/images/L-Drill-CustAging/07.png)
<br>
  


**Step 5:** Complete the TransferPairs argument. In the Formula Bar, click inside the word **Pair()** within the text **PairGroup(Pair())**. See the illustration below. Once this is done, the Function Wizard will automatically change to help with the Pair() function. Type **B22:B24** in the **From** argument. This is the column where the CustomerID is going to be presented in the source report. By noting a range from row 22 to 24 in column B, INTERJECT will expand that range to the data presented in this source report. 

![](/images/L-Drill-CustAging/08.png)
<br>
  


**Step 6:** Select the Target input field and navigate to the **CustomerOrderHistory** tab, where you will choose which cell you want to receive the value. In this case you want C23. Excel should automatically fill in the argument with the text **CustomerOrderHistory!C23** . Click OK to finish updating the function, and it will automatically go back to the source worksheet. 

![](/images/L-Drill-CustAging/09.png)
<br>
  


**Step 7:** Now that you have created the drill, you can use [ **Pull Data** ](/wPortal/INTERJECT-Ribbon-Menu-Items.html) to bring in the customers to the source worksheet. 

![](/images/L-Drill-CustAging/10.png)
<br>
  


Below is when the data is pulled. 

![](/images/L-Drill-CustAging/11.png)
<br>
  


###  **Final Results**

**Step 1:** To demonstrate the new drill, **right click** on one of the customer rows and select Drill on Data. The drill option **Drill to Customers Orders History** should be shown. 

![](/images/L-Drill-CustAging/12.png)
<br>
  


**Step 2:** Click on the button **Do Drill** and INTERJECT will navigate to the target worksheet, bring in the CustomerID selected by the filter, then run the report. The screenshot below should resemble the result. 

![](/images/L-Drill-CustAging/13.png)
<br>
  


You completed the drill. You can return to the source worksheet, **Customer Aging** , and re-freeze the panes, clear the report, and save it. Now it is ready to be published to the users. 

  


![](/images/L-Drill-CustAging/14.png)
<br>

Finally, clear the reports, refreeze the panes, and upload it to the ![ Report Library ](/wGetStarted/L-Create-UpdatingReportLibrary.html).

  


  

