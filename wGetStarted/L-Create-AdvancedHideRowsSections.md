---
title: Advanced Hide Row/Section Lab
layout: custom 
keyword: hide rows, sections, report formulas, conditional formula
description: Full instructions for hiding sections based on conditional values
sitemap: True
---

##  **Overview**

In this example of the **ReportHideRowsOrColumns()** function, we will hide an entire section of a report based on the condition that the section is empty. You would typically use this in a report when data is pulled in with zero values. By hiding the zero value rows, and the entire section when all the rows within it are zero vale, the reporting area will be more usable. 

For this lab, find the Interject Inventory Demo in the Interject Demo folder within the [ Report Library ](/wAbout/Report-Library-Basics.html). Once open, you'll use the **InvByCategory_WithDetail** tab.


###  **Hiding Rows**

**Step 1:** Start by using the [ Quick Tools ](/wPortal/INTERJECT-Ribbon-Menu-Items.html) button in the ribbon menu and selecting **Freeze/Unfreeze Panes.
![](/images/L-Create-AdvancedHideRow/AdvanceRowHide1.png)

<br> 

**Step 2:** Insert a row above row above row **6**, so that there are 2 blank rows, and then expand the collapsed columns by clicking the plus sign in the upper left.
![](/images/L-Create-AdvancedHideRow/AdvanceRowHide2.png)

<br>

**Step 3:** Click into cell **C4** and open the Function Wizard by clicking **fx**. Then scroll down in the Report Variable section of the wizard until you see **UseTopSpacerRow**, and type **True** into the empty field. Click **OK**.
![](/images/L-Create-AdvancedHideRow/AdvanceRowHide3.png)

<br>

**Step 4:** In cell **B5**, type "For Backward Compatibility:". Then, in cell **C5** enter **=ReportCalc()** or double click it from the formula menu. Once it's entered, open the Function Wizard and input the following and click OK:
- **OnPullSaveOrBoth:** Pull
- **OnClearRunOrBoth:** Both
- **SheetOrWorkbook:** Sheet
- **Disabled:** Leave blank

![](/images/L-Create-AdvancedHideRow/AdvanceRowHide4.png)

<br>

**Step 5:** In cell **B6** type "Hide/Show Section:". In cell **C6** type **=ReportHideRowOrColumn()** or begin typing and double click the formula from the menu. Next, open the Function Wizard by clicking **fx**, enter the following information and click OK:
- **OnPullSaveOrBoth:** Pull
- **OnClearRunOrBoth:** Both
- **RowOrColumnRange:** C19:C56
- **Disabled:** Leave blank

![](/images/L-Create-AdvancedHideRow/AdvanceRowHide5.png)

<br>

**Step 6:** In cell **A20** enter **=Rows(A19:A56)**.
![](/images/L-Create-AdvancedHideRow/AdvanceRowHide6.png)

<br>

**Step 7:** In cell **C8**, enter **=C7**, to reference the cell above.

![](/images/L-Create-AdvancedHideRow/AdvanceRowHide7.png)

<br>

**Step 8:** Now, in cell **C19** of the report area, write the formula **=IF(AND(I22=0,$A$20<>38),"Hide","Show")**. Write the formula **=C19** in both **C20** and **C21**.

![](/images/L-Create-AdvancedHideRow/AdvanceRowHide8.png)

**Step 9:** Select cells **C19:C21** and copy to the clipboard by pressing **CTL-C**. Navigate to cell **C23** and paste the formulas by pressing **CTL-V**.

![](/images/L-Create-AdvancedHideRow/AdvanceRowHide9.png)

<br>

Continue to navigate to each category and paste the formulas in cells in **C27**, **C31**, **C35**, **C39**, **C43**, **C47**. The final result should look like the screenshot below.

![](/images/L-Create-AdvancedHideRow/AdvanceRowHide10.png)

<br>

**Step 10:** To test that the function and formulas are working correctly, click into cell **B20**, which contains the category name "Beverages" and add and "X". Now freeze the panes using the Quick Tools menu, hide the leftmost columns, and pull the report.

![](/images/L-Create-AdvancedHideRow/AdvanceRowHide13.png)

<br>

You should see that the empty category comes in collapsed, the other category detail is expanded, and the original "Beverages" category comes in at the bottom as "Items Not Included."

![](/images/L-Create-AdvancedHideRow/AdvanceRowHide14.png)
