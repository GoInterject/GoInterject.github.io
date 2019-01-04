---
title: "Lab Export: Basic Distribution"
layout: custom
keywords: [ basic, distribution, email, report, export, file, pdf]
description: The distribution process provides extensive control when creating and distributing reports. You can create one or more report workbooks and choose which worksheet tabs to include, create copies by iterating through different filters, and choose export targets like File Location, Email, Print, PDF.
---
* * *

##  **Overview**

The distribution process provides extensive control when creating and distributing reports. You can create one or more report workbooks and choose which worksheet tabs to include, create copies by iterating through different filters, and choose export targets like File Location, Email, Print, PDF, etc. 


###  Create a Distribution from an Existing Report 

**Step 1:** First you are going to open a report. The example for this walk-through will use the same PL Trend Report seen in the [ Financial Walk-through ](/KB/HowToUse/Walkthroughs/Financial.html) lab. If needed, download the document here: [ Interject_PLTrendDemo.xlsx ](/wGetStarted/L11.2-Basic-Distribution_128719024.html). 

![](/images/L-Export-BasicDist/01.jpg)

<br> 


**Step 2:** When creating a distribution, you are normally taking a worksheet and making a copy for different cost centers. To accomplish this, you need to mark which filter will change for each copy. Do this by adding a Range Tag formula. Type **=jRangeTag()** into cell 26 and hit the **Fx** button. It does not matter where you place this formula since it will be removed automatically as the worksheet is used to create the distribution. 

![](/images/L-Export-BasicDist/02.jpg)

<br> 


**Step 3:** The Function Wizard will open. You want to change the Location filter for each worksheet copy, so type **Location** in the Tag argument. For the Range argument, select cell M22, the Location filter, as shown below. 

![](/images/L-Export-BasicDist/03.jpg)

<br> 


**Step 4:** You need to add a Range Tag for the month as well. In cell O27, type another jRangeTag() formula and click the **Fx** button. 

![](/images/L-Export-BasicDist/04.png)

<br> 


**Step 5:** With the Function Wizard window open, enter **Month** for the Tag argument and **M23** into the Range argument. This will allow us to change the month within the distribution setup. 

![](/images/L-Export-BasicDist/05.png)

<br> 


Once this is completed, the Range Tag formulas should summarize what was setup as seen in the screenshot below. 

![](/images/L-Export-BasicDist/06.png)

<br> 


**Step 6:** Now it is time to create the Distribution worksheet that generates the distribution. You can create this by using the **Export Book** menu item in the INTERJECT ribbon. The Export and Distribution window will appear and click **Create Distribution Sheet**. 

![](/images/L-Export-BasicDist/07.png)

<br> 


INTERJECT will create the Distribution worksheet in the existing workbook and will search for existing Range Tag formulas in the workbook. The screenshot below illustrates the typical defaults that will be used when initially created. 

1. The worksheet names for those that have Range Tag formulas should be added to the Tab Selection columns by default. 
2. A filter is created for each jRangeTag found in the workbook in the Report Filters columns. 
3. The Book column should default to 1, noting the first workbook build to be created. More can be added if needed to the same distribution sheet. 



![](/images/L-Export-BasicDist/08.png)

<br>

**Note:** The **Enabled?** column contains a drop down list of options that can be applied to the tabs, on an individual basis, which are being created. 

* **Blank** \- **** When the enabled column is set to blank, INTERJECT interprets this as a **Yes** value and automatically pulls the data after the report is created. 
* **Yes -** When this column value is set to **Yes** then distribution report builder will automatically create the reports **And** pull the data. 
* **No -** In the instance that the value is set to **No,** INTERJECT will not build that report tab. 
* **Prep -** When set to **Prep** the report tabs will be built out, however, the data will not be pulled automatically. 


**Step 7:** Edit the distribution defaults further. In this example, you want to create three copies of the **ProfitAndLoss** worksheet, one for each location **7001**, **7002**, and **7120**. And you want to use the month **2002-05**. Use the screenshot below as a guide, and type in the values for columns **Worksheet Tabs**, **Location**, and **Month**. 

![](/images/L-Export-BasicDist/09.png)

<br> 


**Step 8:** You are ready to create a new workbook of reports, but first you need a destination for this distribution. There are many options for the Distribution Target (open, save, print, email, etc.). In this example, you will use the default, **Open**, which creates a new workbook without saving. 

![](/images/L-Export-BasicDist/10.png)

<br> 


**Step 9:** To run the distribution, from the Distribution worksheet click the **Export Book** menu item in the INTERJECT ribbon. Click the **Run Distribution** button that appears in the next window. 

![](/images/L-Export-BasicDist/11.png)

<br> 


As the distribution process is running, it will display its activity and progress as seen below. 

![](/images/L-Export-BasicDist/12.png)

<br> 


When the process is complete, the new workbook opens and the the original workbook is unchanged. Looking closer at what you created, the workbook below has 3 worksheets, and each worksheet has its own filter values as configured. You will notice that the worksheet names are simply incrementally numbers. You will cover how to custom name each tab in the next  [ L11.3 Advanced Distribution ](/KB/HowToCreate/ExportReport/Grouping.html) page. 

![](/images/L-Export-BasicDist/13.png)

<br> 


###  Distributing to a Folder 

Now you are going to do the same distribution, but this time you will save to a specific file folder. 

**Step 1:** To do this, navigate back to the distribution worksheet and change the output to **Excel** in cell E28. 

![](/images/L-Export-BasicDist/14.png)

<br> 


**Step 2:** Now you can name the file and select its destination. 

![](/images/L-Export-BasicDist/15.png)

<br> 


**Step 3:** Now run the distribution. 

![](/images/L-Export-BasicDist/16.png)

<br>

**Step 4:** After you run the distribution, navigate to its folder to see that the file has been saved correctly. 

![](/images/L-Export-BasicDist/17.png)

<br>

###  Distributing With Email 

Navigate back to the page to distribute the workbook via email. 

**Step 1:** First, you need to make sure the email is set up properly. The email distribution requires an SMTP server set up in the [ INTERJECT Portal Website. ](/images/L-Export-BasicDist/01.png) The Organizational Profile settings area contains the SMTP information that must be completed beforehand. 

![](/images/L-Export-BasicDist/18.png)

<br> 


Assuming the SMTP information is entered, continue demonstrating email distribution. 

**Step 2:** In the Distribution Target rows of the Distribution worksheet, click the drop down in the Output column. Choose **Email**. 

![](/images/L-Export-BasicDist/19.png)

<br> 


**Step 3:** Now you can type in where the email is going, where the email is from, the subject, and the email message. You will need to work with your IT department to work through email configuration matters to avoid the delivered email being flagged as spam in your corporate email server. This can occur if the From email is any different than configured earlier with the SMTP settings. 

![](/images/L-Export-BasicDist/20.png)

<br> 


Now run the distribution again and the email will be sent to the destination. 

![](/images/L-Export-BasicDist/21.png)

<br> 


Continue learning about distribution in the  [ L11.3 Advanced Distribution ](/KB/HowToCreate/ExportReport/Grouping.html) page. 
