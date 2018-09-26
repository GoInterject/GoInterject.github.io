---
title: Interject Documentation > Report Formula Reviews
layout: custom
---
##  Overview 

When a user is writing out the formula it can be difficult to get the parenthesis, commas and quotations correct.The Function Wizard defines how the function is used, but it will not expand upon the names of the parameters. In this page you will see how your parameters are set up for the report. To do so you need to head to the Validation Report bar to see the columns used for those parameters. 

  * ####  Getting Started 

  * ####  Reviewing Parameters 

  * ####  Working with Function Wizard 




### 

###  Getting Started 

Before anything you must begin by unfreezing the report you will be using for this exercise. For this wiki you will use the Customer Collections report previously used in the Real World Walk-through. 

![](attachments/127870833/128981431.png)

  


Now that you have the report ready, you should unfreeze the hidden rows which will allows you to access all of the formulas. 

![](attachments/127870833/128981521.png)

  


To unfreeze the rows you simply need to go to the View Ribbon and select Freeze panes or you can use the [ Quick Tools ](/wPortal/INTERJECT-Ribbon-Menu-Items_83689479.html) operation. Out of the three options given in the drop down list, you will use the first. 

![](attachments/127870833/128982049.png)

  


Now you can begin reviewing the parameters. 

![](attachments/127870833/128982117.png)

###  Reviewing Parameters 

When a user needs to see the parameters in detail, the Function Wizard does not give them that opportunity. Before diving into the Interject Ribbon, you must select the cell containing the ReportRange(). 

![](attachments/127870833/128982184.png)

  


To see the parameters and cell formula detail simply open the [ Advanced Menu ](https://interject.atlassian.net/wiki/spaces/ID/pages/83689479/Interject+Ribbon+Menu+Items#InterjectRibbonMenuItems-Advanced-Menu) in Interject. 

![](attachments/127870833/128982203.png)

  


Now that the Advanced Menu has been expanded, you can explore Validation Report. Open the _Validation report_ and select the **Cell Formula Review** near the bottom of the list. 

![](attachments/127870833/128982393.png)   


A window will open and if you expand it, you will see four options to check off: 

**_Indent Data Cell Function_ ** and  **_Indent All Others_ ** should already be checked off, you will have to check off  **Show Param Names** ourselves. This will bring to light the names of the parameters. 

![](attachments/127870833/128982447.png)

  


**_Show Formula References_ ** allows you to see where some of the parameters are stationed 

![](attachments/127870833/128982478.png)

  


The Source Code for the Report range is on the left while the parameters are on the right which allows you to connect the values to the parameters. 

_NorthwindCustomer_ is the Portal used for the Parameter ( _DataPortal_ ) 

_Market_ is used for (@ _CompanyName_ ) 

Now that this has been completed you can move on to the Function Wizard. 

###  Working with Function Wizard 

  


If you have not seen the function wizard before, you will begin at the point where you have the Customer Collections Report Unfrozen and ReportRange() selected. 

![](attachments/127870833/128982728.png)   


  
After you find report range or [ create one of your own ](https://interject.atlassian.net/wiki/display/ID/Creating+Reports) , you can give it commands by simply selecting the F() button. 

In order to access the formula cells for the report range first the user must select the report range cell.   
![](https://lh3.googleusercontent.com/DFtbNdULS8UkupyTsprQVhPuYhN6rFHNNKG6bmlU13X_umFJrZ_fQsMSonpyJEjJiTC4GzdnIGriOyiZ_0uGi1g3xZRrbabvkafPIcZzc3xsX2aSPQjBGdG6olX9saIYq8dyYGWY)

Once the cell is selected then the user can push the Fx button   
![](https://lh5.googleusercontent.com/A_7Gb-g8QP8FoQEEnN1nUkcSY489FwM9WjGnz5rvy8U152j0W6gmgRT58yJs_Xtpn8pzQ9Orzjkadb2TTxHExbZ_JRhQicGYSc70DmLn2oGeJgGiDIfnwZdStYTjs6lzTs-UOeNv)

When they select Fx It will bring up the box with the Cell formulas. Cell formulas are the boxes that hold the ranges you wish to add:   
![](attachments/127870833/127871369.png)

Add the values you need for the formula and it will format it correctly for you. 
