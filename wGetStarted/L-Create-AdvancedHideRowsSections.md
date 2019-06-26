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

**Step 3:** Click into cell **C4** and open the Function Wizard by clicking **fx**. Then scroll down in the Report Variable section of the wizard until you see **UseTopSpacerRow**, and type **True** into the empty field.
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

**Step 8:** Now, in cell **C19** of the report area, write the formula **=IF(AND(I22=0,$A$20<>38),"Hide","Show")**. You will write this same formula in **C23**, **C27**, and so on, but you will change the cell reference **I22** to the subtotal cell corresponding to each section. For example, notice in the second screenshot below that the subtotal cell for "Condiments" is **I26**. You can do this by copying the orginal formula, then highlighting the cell reference in the formula window \(item 1 in the second screenshot\) and clicking into the corresponding subtotal cell \(item 2 in the second screenshot\).

![](/images/L-Create-AdvancedHideRow/AdvanceRowHide8.png)
![](/images/L-Create-AdvancedHideRow/AdvanceRowHide9.png)

<br>

**Step 9:** In column C on each row with a category name, enter a reference to the cell directly above. For example, in cell **C20** type **=C19**; in cell **C24** type **=C23**. Do this for all categories of the report.
![](/images/L-Create-AdvancedHideRow/AdvanceRowHide10.png)

<br>

**Step 10:** Now, type the same reference in the cells below each of the ones in which you just entered it. For example, in **C21** type **=C19**; in **C45** type **C43**.
![](/images/L-Create-AdvancedHideRow/AdvanceRowHide12.png)

<br>

**Step 11:** To test that the function and formulas are working correctly, click into cell **B20**, which contains the category name "Beverages" and add and "X". Now freeze the panes using the Quick Tools menu, hide the leftmost columns, and pull the report.

![](/images/L-Create-AdvancedHideRow/AdvanceRowHide13.png)

<br>

You should see that the empty category comes in collapsed, the other category detail is expanded, and the original "Beverages" category comes in at the bottom as "Items Not Included."

![](/images/L-Create-AdvancedHideRow/AdvanceRowHide14.png)