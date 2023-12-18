---
title: "Create: Building jDropdowns"
layout: custom
keywords: [jDropdown, function, hyperlink, custom list, walkthrough]
description: The jDropdown formula is used for filtering on multiple parameters.
---
* * *

## Overview

Interject reports typically have parameters that can be passed to a stored procedure that can filter the data. It can be difficult to remember what the exact filter names are and which are even available for the stored procedure. This is especially true in large reports with many filtering options. However, you can use Interject's [jDropdown](/wIndex/jDropdown.html) formula to automatically create hyperlinked lists of available filters. This makes filtering in large reports a much simpler task! 

In this example you will modify the [Customer Aging report](/wGetStarted/L-Create-CustomerAging.html) by adding the jDropdown functionality to one of the filters, while using an existing Data Portal.

<blockquote class=highlight_note>
<b>Note:</b> The jDropdown feature requires a Data Portal with a stored procedure to operate. In the event that you cannot create a stored procedure, you can reuse a Data Portal from the report formula that populates the report in which you want to use this feature. To learn how to build the Database Connection, Data Portal, and stored procedure used in this example, follow the instructions in the <a href="https://docs.gointerject.com/wGetStarted/L-Dev-jDropdowns.html">developer example</a>. Otherwise contact your IT department to help implement this functionality.
</blockquote>

<br>

<blockquote class=lab_info>
 If you are following the Training Labs, this report file can be found in the Report Library at Training Labs > Lab 5 Advanced Features > Lab 5.3 Building jDropdowns.
</blockquote>

### Preparing the Report

**Step 1:** Open the report **Interject Customer Collections** under the Interject Demos in the [Report Library](/wAbout/Report-Library-Basics.html).

![](/images/L-Create-Dropdowns/01.png)

**Step 2:** Next, unfreeze panes by going into [**Quick Tools**](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html) and selecting **Freeze/Unfreeze Panes**.

![](/images/L-Create-Dropdowns/02.png)
<br>

### Adding a Named Range

**Step 1:** Now select the **Formulas** ribbon tab and select **Name Manager**.

![](/images/L-Create-Dropdowns/03.png)
<br>

**Step 2:** Next, select **New...**.

![](/images/L-Create-Dropdowns/04.png)
<br>

**Step 3:** For the **Name:** field input **CompanyNameDDL**, and in the **Refers to:** field input **=CustomerAging!$H$7**. Click **OK** and **Close** the Name Manager window.

![](/images/L-Create-Dropdowns/05.png)

**Note:** A named range is used here so that upon the movement of the formula, the hyperlink that is created later will still reference the cell with the jDropdown() formula.
<br>

### Creating the Formula

**Step 1:** Next, in cell H7 insert **=jDropdown()** then select **fx**.

![](/images/L-Create-Dropdowns/06.png)
<br>

**Step 2:** For the Data Portal argument field, input **NorthwindCustomersDropdown**.

![](/images/L-Create-Dropdowns/07.png)
<br>

**Step 3:** For the **MultiSelect** argument field, input **False**. Then for the **Target Cell** Argument field, input **C17**.

![](/images/L-Create-Dropdowns/08.png)
<br>

**Step 4:** In the **Value Column Name** argument field, insert **CompanyName**.

![](/images/L-Create-Dropdowns/09.png)
<br>

**Step 5:** Scroll down in the function arguments until you see the **Display Column Name** argument field and insert **DisplayText**.

![](/images/L-Create-Dropdowns/10.png)
<br>

**Step 6:** Next, scroll down in the function arguments to find the **Instruction Text** argument field and input **Select A Customer**. Click **OK**.

![](/images/L-Create-Dropdowns/11.png)
<br>

<blockquote class=highlight_note>
<b>Important:</b> The Value Column Name and the Display Column Name arguments must exactly match the name of a column that is returned by the stored procedure. A good place to look for valid columns is in the <a href="https://docs.gointerject.com/wAbout/Basics-of-Report-Formulas.html#column-definitions">Column Definitions</a> section of the report. To learn more about the jDropdown() function and what each of its arguments do, review its <a href="https://docs.gointerject.com/wIndex/jDropdown.html">index page</a>.
</blockquote>

### Adding a Special Hyperlink

**Step 1:** Now select cell **B17** and right click. Then select the **Link** option in the menu.

![](/images/L-Create-Dropdowns/12.png)
<br>

**Step 2:** Click on **Place in This Document** then select the **CompanyNameDDL** defined name in the list of options. Then select the **ScreenTip...** button.

![](/images/L-Create-Dropdowns/13.png)
<br>

**Step 3:** In the **ScreenTip text:** field input **Interject Dropdown** (Note: The jDropdown function will not work without this).

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

To build the stored procedure and Data Portal, and database connection that allows this formula to work, continue to the [developer section of this example](/wGetStarted/L-Dev-jDropdowns.html).

### Creating a Custom jDropdown List

The jDropdown feature can be used to create a custom list of items in a dropdown list. Instead of a Data Portal, you can enter a list. For example, to create a dropdown list of 3 items: Yes, No, Maybe, use the following syntax:

```
list:Yes,No,Maybe
```

To display the list options in the dropdown window something different then the entry, use the following format:

```
list:Yes^This is Yes,No^This is No,Maybe^This is Maybe
```

**Step 1:** Find an empty cell and enter a heading:

![](/images/L-Create-Dropdowns/EnterYourResponse.png)
<br>

**Step 2:** On the cell above the heading, enter **=jDropdown(** and press the "**fx**" button to bring up the Function Wizard:

![](/images/L-Create-Dropdowns/EnterjDropdown.png)
<br>

**Step 3:** Enter the following for the jDropdown parameters and click **OK**:

* Data Portal: "list:Yes^This is Yes,No^This is No,Maybe^This is Maybe"
* Target Cell: &lt;Enter cell ref here&gt;
* Value Column Name: &lt;Enter anything here&gt;

![](/images/L-Create-Dropdowns/EnterFX.png)
<br>

**Step 4:** Right click the cell you wish to create a link and click **Link**:

![](/images/L-Create-Dropdowns/ClickLink.png)
<br>

Enter the cell reference of the jDropdown function and click **ScreenTip**:

![](/images/L-Create-Dropdowns/TypeTheCellReference.png)
<br>

Enter "Interject Dropdown" for the ScreenTip and click **OK** and then **OK** again to create the link:

![](/images/L-Create-Dropdowns/EnterScreenTipText.png)
<br>

**Step 5:** Click on the link to see the dropdown list:

![](/images/L-Create-Dropdowns/DropdownList.png)
<br>

Click on an entry to see it populated:

![](/images/L-Create-Dropdowns/EntryEntered.png)
<br>
