---
title: Interject Documentation > L4.4 The Three Ways to Drill
layout: custom
---
* * *

##  **Overview**

INTERJECT facilitates three different ways to drill. Each method is easy to choose the best one different situations. 

Click on the links below to go to any section of this walk-through. 

    * ####  The Menu Method 

    * ####  The Hyperlink Method 

    * ####  The Double Click Method 




###  The Menu Method: 

The **[ Drill on Data ](/wPortal/INTERJECT-Ribbon-Menu-Items_83689479.html) ** menu item is available in every report containing a drill function. For this example, you will drill using the [ Customer Aging demo ](https://interject.atlassian.net/wiki/display/ID/Customer+Aging) . 

![](attachments/128510906/128510963.png)

  


There are four steps to using the menu. 

  1. First, select the cell to drill on. In this example you will chose the Save-a-lot Markets customer's 90 days balance. 
  2. Select the **Drill on Data** menu in the INTERJECT ribbon.   

  3. Select the drill option in the Data Drill window.  In this example, chose **Drill to Aging Detail** .    

  4. Complete the drill by clicking **Do Drill** . 



![](attachments/128510906/128510969.png)

  


This automatically takes you to the desired destination and usually pulls the data as well. 

![](attachments/128510906/128510980.png)

###  The Hyperlink Method: 

The hyperlink drill method is another option. It is one of the simplest ways for a user to drill in INTERJECT and makes it intuitive for the user to know where drills are available. For this example, you will drill using the [ Inventory Reports Demo ](https://interject.atlassian.net/wiki/display/ID/Inventory+Reports) seen below. 

![](attachments/128510906/128511030.png?width=720)

  


By clicking the hyperlink cell, it will automatically trigger the INTERJECT drill. Since there is only one drill option, the Data Drill window will not appear as in previously shown examples. If multiple drill options are present, the Data Drill window will appear so the user can select which drill option to use. The animated GIF below illustrates how the hyperlink drill works in INTERJECT. 

![](attachments/128510906/128511040.gif)

  


It is that simple. To know how to setup a hyperlink drill for one of the reports, [ click here ](https://interject.atlassian.net/wiki/display/ID/Drill%3A+Inventory+Report) to see how it was setup in the example above. 

###  The Double Click Method: 

The double click method is similar to the hyperlink method in that it reduces the number of button clicks. But there is a configuration step to activate it for a workbook. For this example, you will be using the [ Customer Aging ](https://interject.atlassian.net/wiki/display/ID/Customer+Aging) Summary to do the drill. 

![](attachments/128510906/128511050.png)

  


The animated GIF below illustrates how the double click method works. The user simply double clicks on the cell to drill on and the Data Drill window appears. In this example, there are multiple drill options so the Data Drill window appears to let the user choose which to use. If only one drill option was available, INTERJECT would have went directly to the target. 

![](attachments/128510906/128514695.gif)

  


Again, you should see the target report as shown below. 

![](attachments/128510906/128511069.png)

  


To enable a workbook with the double click method, the custom properties of the Excel workbook must include a property **Interject_DoubleClick** , and it must be set to **True** . To update custom properties, refer to the following link. [ https://support.office.com/en-us/article/View-or-change-the-properties-for-an-Office-file-21D604C2-481E-4379-8E54-1DD4622C6B75 ](https://support.office.com/en-us/article/View-or-change-the-properties-for-an-Office-file-21D604C2-481E-4379-8E54-1DD4622C6B75)

  


##  Related Links: 

[ L4.1 Drill: Customer Aging ](/wGetStarted/128421015.html)

[ L4.2 Drill: Inventory Report ](/wGetStarted/128409138.html)

[ L4.3 Drill: Financial Report ](/wGetStarted/128409219.html)

[ INTERJECT Ribbon Menu Items ](INTERJECT-Ribbon-Menu-Items_83689479.html)

  

