---
title: Training by Example
layout: custom
keywords: [Report, Epicor, Accounts]
description: Step by step guide on adding budget columns to your report templates.
---

<<<<<<< HEAD
In some cases you may want to hide from your financial reports the rows containing zeros and the subtotals which might result from them. Doing so will make your reports much cleaner, easier to read, and more manageable. Common Excel functionality provides a simple way to do so, with only a little help from Interject. In the following example, we'll use a prebuilt report template that we know contains a subtotaled section with zeros and a zero sum. The method and syntax used here can be applied to other situations as well, is it is mostly using Excel formulas.
=======
In some cases you may want to hide from your financial reports the rows containing zeros and the subtotals which might result from them. Doing so will make your reports cleaner, easier to read, and more manageable. Common Excel functionality provides a simple way to do so, with only a little help from Interject. In the following example, we'll use a prebuilt report template that we know contains a subtotaled section with zeros and a zero sum. The method and syntax used here can be applied to any other Excel reporting situations, as they leverage common Excel formulas and knowledge.
>>>>>>> ab08e03f810ace9a20ff4023b63a8d204bc4eee0

### Hiding Rows and Sections with Zero Values

> To Do
>
<<<<<<< HEAD
> **Step 1:** From the Report Library, open up the Configuration Manager
> ![](/images/bFinancialsHideZeros/HideZeros1.png){: .center-image }
>
> **Step 2:** Click on **Setup/Review Row Report Templates**
> ![](/images/bFinancialsHideZeros/HideZeros2.png){: .center-image }
>
> **Step 3:** From the Template Manager, click on **FRXBS**. Note that this is a sample report template, and you may not have this in your Interject for Financials offering.
> ![](/images/bFinancialsHideZeros/HideZeros3.png){: .center-image }
>
> **Step 4:** Once in the report template, click the **USE DISTRIBUTION?** parameter and choose **No**. Hit **Click to Create Report**
> ![](/images/bFinancialsHideZeros/HideZeros4.png){: .center-image }
>
> **Step 5:** When the Drill window opens, select **Drill to Create Detail Report - Collapse Detail Below**, then hit **Do Drill**.
> ![](/images/bFinancialsHideZeros/HideZeros5.png){: .center-image }
>
> **Step 5:** With the report template open, click the **Company** parameter, choose **INT**, then click **Apply**.
> ![](/images/bFinancialsHideZeros/HideZeros6.png){: .center-image }
>
> **Step 6:** Here you can pull data into the report to get a baseline against which to compare your results. Note the zero values pulled in for Total Long Term Liabilities.
> ![](/images/bFinancialsHideZeros/HideZerosInitial.png){: .center-image }
>
> **Step 7:** Hit **Ctrl-Shift-J** or the **Pull** button and **Clear** your data.
>
> **Step 8:** In cell **I47**, enter **=FiscalPeriod**, and in cell **H47** enter **=EDATE(FiscalPeriod,-1)**. This sets up the dynamic reference for your reporting period.
> ![](/images/bFinancialsHideZeros/HideZeros7.png){: .center-image }
>![](/images/bFinancialsHideZeros/HideZeros8.png){: .center-image }
>
> **Step 9:** Now, click the plus sign directly over column **D** to expand the collapsed columns, and add a column to the left of column **B**.
> ![](/images/bFinancialsHideZeros/HideZeros9.png){: .center-image }
>
> **Step 10:** Expand the **Report Formula** section, and in cell **K10**, type "Hide Zeroed Subtotals". This will label the formula you'll write in the cell to the right. In cell **L10** enter **=ReportHideRowOrColumn()**. Click **fx** to open the Function Wizard, and enter the following information:
> - OnPullSaveOrBoth: **Pull**
> - OnClearRunOrBoth: **Both**
> - RowOrColumnRange: **B48:B74**
> - Disabled: Leave blank
> ![](/images/bFinancialsHideZeros/HideZeros10.png){: .center-image }
>
> **Step 11:** In cell **K9** type "For Backward Compatibility". In cell **L9** enter **=ReportCalc()** and click **fx** to open the Function Wizard. Enter the following:
=======
> **Step 1:** If you would like to use our example report, download it first <a href="/images/bFinancialsHideZeros/HidingZeroValues_Download.xlsx" download>here</a> <!--[here]({file name='/images/bFinancialsHideZeros/HidingZeroValues_Download.xlsx'})-->
>
> **Step 2:** Open the Excel file and log in to Interject, then notice the subtotal in row 119 reading zero. Now hit **Ctrl+Shift+T** or the "Quick Tools" icon in the Interject Ribbon and press enter to **Unfreeze Panes**.
> ![](/images/bFinancialsHideZeros/ZeroRow.png){: .center-image }
> ![](/images/bFinancialsHideZeros/UnfreezePanes.png){: .center-image }
>
> **Step 3:** Now, click the plus sign directly over column **C** to expand the collapsed columns, and add a column to the left of column **B**.
> ![](/images/bFinancialsHideZeros/InsertColumn.png){: .center-image }
>
> **Step 10:** Expand the **Report Formula** section, and in cell **K11**, type "Hide Zero Subtotals". This will label the formula you'll write in the cell to the right. In cell **L11** enter **=ReportHideRowOrColumn()**. Click **fx** to open the Function Wizard, and enter the following information:
> - OnPullSaveOrBoth: **Pull**
> - OnClearRunOrBoth: **Both**
> - RowOrColumnRange: **B65:B140**
> - Disabled: Leave blank
> ![](/images/bFinancialsHideZeros/ReportRowHideParams.png){: .center-image }
>
> **Step 11:** In cell **K10** type "For Backward Compatibility". In cell **L10** enter **=ReportCalc()** and click **fx** to open the Function Wizard. Enter the following:
>>>>>>> ab08e03f810ace9a20ff4023b63a8d204bc4eee0
> - OnPullSaveOrBoth: **Pull**
> - OnClearRunOrBoth: **Both**
> - SheetOrWorkbook: **Sheet**
> - SheetName: **FRXBS** Note: This may not be the same in your template.
> - Disabled: Leave blank
<<<<<<< HEAD
> ![](/images/bFinancialsHideZeros/HideZeros11.png){: .center-image }
>
> **Step 12:** To collapse the zero-value sections, add a set of references to each section in the hidden column area. You'll write these references in the two rows directly above the subtotal row, as follows: Enter an **=** in cell **B48**, click into cell **B50**, and click **enter** to complete the reference. Do this also for the partailly collapsed row in cell **B49**.
> ![](/images/bFinancialsHideZeros/HideZeros12a.png){: .center-image }
> ![](/images/bFinancialsHideZeros/HideZeros12b.png){: .center-image }
>
> **Step 13:** Repeat the above step for every section, always in column **B**. In our example, you'll build references in cells **B52** and **B53**, **B57** and **B58**, **B61** and **B62**, and **B66** and **67** - always referenceing the row containing the section title. The following screenshots show the repeated process for rows **52** and **53**.
> ![](/images/bFinancialsHideZeros/HideZeros13a.png){: .center-image }
> ![](/images/bFinancialsHideZeros/HideZeros13a.png){: .center-image }
>
> **Step 14:** Now, in cell **B26** enter the formula **=IF(AND(K26=0,J26-0,I26=0),"Hide","Show")**
> ![](/images/bFinancialsHideZeros/HideZeros14.png){: .center-image }
>
> **Step 15:** Close up all the expanded sections, and run the report again, using "INT" as the Company parameter. Notice now that the row and section which previously had a zero value is now hidden. Note that the section is not gone or deleted; rather, it is hidden from your view.
> ![](/images/bFinancialsHideZeros/HideZerosResult.png){: .center-image }
=======
> ![](/images/bFinancialsHideZeros/ReportCalcParams.png){: .center-image }
>
> **Step 12:** To collapse the zero-value sections, add a set of references to each section in the hidden column area. You'll write these references in the two rows directly above the subtotal row, as well as the one above it. Enter an **=** in cell **B119**, click into cell **B121**, and click **enter** to complete the reference. Do this also for the partailly collapsed rows in cell **B120** and **B122**.
> ![](/images/bFinancialsHideZeros/CellRef1.png){: .center-image }
> ![](/images/bFinancialsHideZeros/CellRef2.png){: .center-image }
> ![](/images/bFinancialsHideZeros/CellRef2.png){: .center-image }
>
> **Step 13:** Repeat the above step for every section of the report, always in column **B**. In the example below, you would reference cells **B79**, **B80**, and **B96** to the title cell **B81**.
> ![](/images/bFinancialsHideZeros/CellRefExample2.png){: .center-image }
>
> **Step 14:** Now, in cell **B34** enter the formula **=IF(AND(H34=0,I34-0,J34=0),"Hide","Show")**
> ![](/images/bFinancialsHideZeros/FormatDetailRange.png){: .center-image }
>
> **Step 15:** Close up all the expanded sections, and pull the report again. Notice now that the row and section which previously had a zero value is now hidden. Note that the section is not gone or deleted; rather, it is hidden from your view.
> ![](/images/bFinancialsHideZeros/NoZeroResult.png){: .center-image }
>>>>>>> ab08e03f810ace9a20ff4023b63a8d204bc4eee0
>
