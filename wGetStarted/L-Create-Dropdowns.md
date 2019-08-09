---
title: "Lab Create: jDropdown"
layout: custom
keywords: [jDropdown, function]
description: The jDropdown formula is used for filtering on multiple parameters.
---

### Overview

The jDropdown formula simplifies the use of filters in a report by building a list of all the inputs that can be used with an individual filter. This method refines the options that a user can input into the filters and gives them options to choose from rather than leaving the filter inputs open ended. It is important to utilize this formula in large reports to assist in determining what data is most relevant to return when pulling the report. In this lab you will modify the [Customer Aging report](/wGetStarted/L-Create-CustomerAging.html) by adding the jDropdown functionality to one of the filters, while using an existing data portal. 

> **IMPORTANT:** The jDropdown feature requires a stored procedure to operate. In the event that you cannot create a stored procedure, you can reuse a data portal from the report formula that populates the data of the report you are trying to implement this feature on. To learn how to build the database connection, dataportal as well as the stored procedure used in this example, follow the instructions in the [developer lab](/wGetStarted/L-Dev-jDropdowns.html). Otherwise contact your IT department to help implement this functionality to your reports.

### Preparing the Report

**Step 1:** Open the report **INTERJECT Customer Collections** under the INTERJECT Demos in the [ Report Library ](/wAbout/Report-Library-Basics.html). 

![](/images/L-Create-Dropdowns/01.png)

This will open the Customer Aging Summary Report. 

**Step 2:** Next, unfreeze panes by going into [ **Quick Tools** ](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html) and selecting **Freeze/Unfreeze Panes**.

![](/images/L-Create-Dropdowns/02.png)
<br>

### Adding a Named Range

**Step 1:** Now select the **Formulas** ribbon tab and select **Name Manager**. 

![](/images/L-Create-Dropdowns/03.png)
<br>

**Step 2:** Next, select **New...**.

![](/images/L-Create-Dropdowns/04.png)
<br>

**Step 3:** For the **Name:** field input **CompanyNameDDL**, and in the **Refers to:** field input **=CustomerAging!$H$7** 

![](/images/L-Create-Dropdowns/05.png)

**Note:** A named range is used here so that upon the movement of formula, the hyperlink that is created later on will always reference the cell with the jDropdown() formula in it.
<br>

### Creating the Formula

**Step 1:** Next, in cell H7 insert **=jDropdown()** then select **fx**

![](/images/L-Create-Dropdowns/06.png)
<br>

**Step 2:** For the DataPortal argument field, input **NorthwindCustomersDropdown**.

![](/images/L-Create-Dropdowns/07.png)
<br>

**Step 3:** For the **MultiSelect** argument field, input **False**. Then for the **Target Cell** Argument field, input **C17**.

![](/images/L-Create-Dropdowns/08.png)
<br>

**Step 4:** In the **Value Column Name** argument field, insert **CompanyName**.

![](/images/L-Create-Dropdowns/09.png)
<br>


**Step 5:** Scroll down in the function arguments, then in the **Display Column Name** argument field insert **DisplayText**.

![](/images/L-Create-Dropdowns/10.png)
<br>

**Step 6:** Next, scroll down in the function arguments, then in the **Instruction Text** argument field input **Select A Customer**.

![](/images/L-Create-Dropdowns/11.png)
<br>

> **IMPORTANT:** The Value Column Name and the Display Column Name arguments must be an exact match to the name of a column that is returned by the stored procedure. A good place to look for valid columns is in the Column Definitions section of the report. To learn more about the jDropdown() function and what each of its arguments do, review its [index page](/wIndex/jDropdown.html).

### Adding a Special Hyperlink

**Step 1:** Now select cell **B17** and right click. Then select the **Link** option in the menu.

![](/images/L-Create-Dropdowns/12.png)
<br>

**Step 2:** Click on **Place in This Document** then select the **CompanyNameDDL** defined name in the list of options. Then select the **ScreenTip...** button.

![](/images/L-Create-Dropdowns/13.png)
<br>

**Step 3:** In the **ScreenTip text:** field input **Interject Dropdown**. 

![](/images/L-Create-Dropdowns/14.png)
<br>


### Reviewing the Report Changes

**Step 1:** Now select the hyperlink you just made and type **Market** into the search options. Notice that there are 4 options. Select **BOTTM - Bottom-Dollar Markets**.

![](/images/L-Create-Dropdowns/15.png)
<br>

**Step 2:** **Pull** the report.

![](/images/L-Create-Dropdowns/16.png)
<br>
**Step 3:** The pull will only return the **Bottom-Dollar Markets** data.

![](/images/L-Create-Dropdowns/17.png)
<br>

To build the stored procedure and dataportal, and database connection that allows this formula to work, continue to the [developer section of this lab](/wGetStarted/L-Dev-jDropdowns.html).
