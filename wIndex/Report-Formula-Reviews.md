---
title: Report Formula Reviews
layout: custom
keywords: [formula review, report formula]
description: In this page you will see how your parameters are set up for the report. To do so you need to head to the Validation Report bar to see the columns used for those parameters.
---
##  Overview 

When a user is writing out the formula it can be difficult to get the parenthesis, commas and quotations correct.The Function Wizard defines how the function is used, but it will not expand upon the names of the parameters. In this page you will see how your parameters are set up for the report. To do so you need to head to the Validation Report bar to see the columns used for those parameters. 

###  Getting Started 

Before anything you must begin by unfreezing the report you will be using for this exercise. For this wiki you will use the Customer Collections report previously used in the Real World Walk-through. 

![](/images/FormulasReviews/01.png)

<br>


Now that you have the report ready, you should unfreeze the hidden rows which will allows you to access all of the formulas. 

![](/images/FormulasReviews/02.png)

<br>


To unfreeze the rows you simply need to go to the View Ribbon and select Freeze panes or you can use the [ Quick Tools ](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#quick-tools) operation. Out of the three options given in the drop down list, you will use the first. 

![](/images/FormulasReviews/03.png)

<br>  


Now you can begin reviewing the parameters. 

![](/images/FormulasReviews/04.png)

<br>

###  Reviewing Parameters 

When a user needs to see the parameters in detail, the Function Wizard does not give them that opportunity. Before diving into the Interject Ribbon, you must select the cell containing the ReportRange(). 

![](/images/FormulasReviews/05.png)

<br>

To see the parameters and cell formula detail simply open the [ Advanced Menu ](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#advanced-menu) in Interject. 

![](/images/FormulasReviews/06.png)

<br>


Now that the Advanced Menu has been expanded, you can explore Validation Report. Open the _Validation report_ and select the <b>Cell Formula Review</b> near the bottom of the list. 

![](/images/FormulasReviews/07.png)   

<br>

A window will open and if you expand it, you will see four options to check off: 

<b>_Indent Data Cell Function_</b> and  <b>_Indent All Others_</b> should already be checked off, you will have to check off <b>Show Param Names</b> ourselves. This will bring to light the names of the parameters. 

![](/images/FormulasReviews/08.png)

<br>


**_Show Formula References_** allows you to see where some of the parameters are stationed 

![](/images/FormulasReviews/09.png)

<br>

The Source Code for the Report range is on the left while the parameters are on the right which allows you to connect the values to the parameters. 

_NorthwindCustomer_ is the Portal used for the Parameter ( _DataPortal_ ) 

_Market_ is used for (@ _CompanyName_ ) 

Now that this has been completed you can move on to the Function Wizard. 

###  Working with Function Wizard 

  


If you have not seen the function wizard before, you will begin at the point where you have the Customer Collections Report Unfrozen and ReportRange() selected. 

![](/images/FormulasReviews/10.png)   

<br>
  
After you find report range or create one of your own, you can give it commands by simply selecting the F() button. 

In order to access the formula cells for the report range first the user must select the report range cell.   
![](/images/FormulasReviews/11.png)

<br>

Once the cell is selected then the user can push the Fx button   
![](/images/FormulasReviews/12.png)

<br>

When they select Fx It will bring up the box with the Cell formulas. Cell formulas are the boxes that hold the ranges you wish to add:   
![](/images/FormulasReviews/13.png)

<br>

Add the values you need for the formula and it will format it correctly for you. 
