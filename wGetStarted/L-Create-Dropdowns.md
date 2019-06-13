---
title: "Lab Create Parameter Dropdowns"
layout: custom
keywords: [jDropdown, function]
description: The jDropdown formula is used for filtering on multiple parameters at once.
---

### Overview

The jDropdown formula helps developers simplify the use of parameters in a data pull or save. It can reduce the rows of data in a report, speeding the report process, sparing server resources, and pulling data more efficiently. 

###  Setting Up The Data Connection

**Step 1:** Navigate to [ https://portal.gointerject.com ](https://portal.gointerject.com) and log in. Set up a data connection by clicking the **Data Connections** icon. 

![](/images/L-Dev-CustAging/01.jpg)
<br>

**Step 2:** On the Data Connections page, click the **New Connection** button. 

![](/images/L-Dev-CustAging/02.jpg)
<br>

**Step 3:** In the Connection Type field, verify that **Database** is selected. 

![](/images/L-Dev-CustAging/03.jpg)
<br>

**Step 4:** The Connection Details page needs to contain the following information for the new connection: Type **NorthwindExampleDB_MyName** in Connection Name, but include your own name in the suffix. Each connection name must be unique. For the connection string, type **Server=myServerAddress;Database=myDataBase;Trusted_Connection=True;**. You are using Windows authentication, so username and password are not required. Make sure the server name and database name match the ones you are using for this walkthrough. 

![](/images/L-Dev-CustAging/04.jpg)
<br>
  
**Step 5:** In the Description field, include details about how the data connection will be used. 

![](/images/L-Dev-CustAging/05.jpg)
<br>

**Step 6:** Click the Save button to create the new data connection. 

![](/images/L-Dev-CustAging/06.jpg)
<br>

The Database Data Connection is now ready to be used in a Data Portal. You should always test a new connection with your security context. Follow the steps in the [ Data Connections ](/wPortal/Data-Connections.html) walkthrough to test your connection string. 

### Setting up the Data Portal

**Step 1:** To add a new data portal, return to [ https://portal.gointerject.com  ](https://portal.gointerject.com) and select Data Portals from the sidebar menu. 

![](/images/L-Dev-CustAging/07.jpg)
<br>

**Step 2:** Select New Data Portal. 

![](/images/L-Dev-CustAging/08.jpg)
<br>

**Step 3:** Type **NorthwindCustomersDropdown_MyName** for the Data Portal Code. Since this field must be unique, add your name to the suffix. Select the connection that was made in the previous step, **NorthwindExampleDB_MyName**. Also enter a name for the stored procedure **\[demo\].\[Northwind_CustomerDropdown\]**, which will be created later. 

![](/images/L-Create-Dropdowns/04.png)
<br>

**Step 4:** Click **Create Data Portal** to save the new data portal. Additional options for adding parameters will show after selecting the Create Data Portal button. 

![](/images/L-Create-Dropdowns/05.png)
<br>

**Step 5:** To add your first formula parameter, click **Click here to add a Formula Parameter**. For this parameter, enter **Filter** for Name, **varchar** for Type, and **input** for Direction to input, as shown below. 

![](/images/L-Create-Dropdowns/06.png)

<br>

### Creating the Formula

**Step 1:** Open the report **INTERJECT Customer Collections** under the INTERJECT Demos in the [ Report Library ](/wAbout/Report-Library-Basics.html). 

![](/images/Walkthrough-CustAging/01.png)

This will bring up the Customer Aging Summary. 

![](/images/Walkthrough-CustAging/02.png)

**Step 2:** First, right click each hyperlinked paramter in the report, and then choose "Remove Hyperlink."

![](/images/L-Create_Dropdowns/RemoveHyperlinks.png)

**Step 3:** Next, unfreeze panes by going into [ Quick Tools ](/wPortal/INTERJECT-Ribbon-Menu-Items.html) and selecting **Freeze/Unfreeze Panes**.

![](/images/L-Create-Dropdowns/07.png)
<br>

**Step 4:** Delete the existing jDropDown formulas from cells C7, C8, and C9. You will be rebuilding these formulas from scratch, so we have to remove them from this report.

![](/images/L-Create_Dropdowns/RemovejDropDown.png)

**Step 5:** Now create a new report formula. In cell F7 type [ **=jDropdown()** ](/wIndex/jDropdown.html). 

![](/images/L-Create-Dropdowns/08.png)
<br>

**Step 4:** Next, select the **DataPortal** argument section, and using a [jDataPortal](/wIndex/jDataPortal.html) insert **"jDataPortal(NorthwindCustomersDropdown_MyName,1)"**.

![](/images/L-Create-Dropdowns/09.jpg)
<br>

**Step 7:** For this example, there are no parameters. Select **MultiSelect** and type **FALSE**. Then, in **Target Cell**, type **C17**. 

![](/images/L-Create-Dropdowns/10.jpg)
<br>

**Step 8:** Scroll down to **Value Column Name** and **Display Column Name** and input **CompanyName** and **DisplayText** respectively.

![](/images/L-Create-Dropdowns/11.jpg)
<br>

**Step 9:** Scroll to the bottom of the function wizard and select the **Instruction Text** argument. Type **Select a Customer**. Then click **OK** to confirm the changes.

![](/images/L-Create-Dropdowns/12.jpg)
<br>

**Step 10:** While still selected on cell F7. Click on **Name Box** and change the name to **compDLL**

![](/images/L-Create-Dropdowns/12.5.jpg)
<br>

**Step 11:** Right click cell B17 where the text **Company Name** is located. Then select **Hyperlink** to create a hyperlink.

![](/images/L-Create-Dropdowns/13.png)
<br>

**Step 12:** Click on **Place in This Document** and point the **Defined Names** to the [jDropdown()](/wIndex/jDropdown.html). In this case, it is in cell **compdll**.

![](/images/L-Create-Dropdowns/14.png)
<br>

**Step 13:** Select **ScreenTip**. Then, in the textbox, type **Interject Dropdown**. Select **OK** in both open windows to save the hyperlink.

![](/images/L-Create-Dropdowns/15.png)
<br>

**Step 14:** Now select the hyperlink you just made and type **Market** into the search options. Notice that there are 4 options. Select **BOTTM - Bottom-Dollar Markets**.

![](/images/L-Create-Dropdowns/16.png)
<br>

**Step 15:** Now that a Company has been selected, **Pull** the report.

![](/images/L-Create-Dropdowns/17.png)
<br>

**Step 16:** The pull will only return the **Bottom-Dollar Markets** data.

![](/images/L-Create-Dropdowns/18.png)
<br>

To build the stored procedure that allows this formula to work, continue to the [developer section of this lab](/wGetStarted/L-Dev-jDropdowns.html).
