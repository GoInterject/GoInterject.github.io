---
title: Interject | Lab Basic Distribution
layout: custom
---
* * *

##  **Overview**

The distribution process provides extensive control when creating and distributing reports. You can create one or more report workbooks and choose which worksheet tabs to include, create copies by iterating through different filters, and choose export targets like File Location, Email, Print, PDF, etc. 

  * ####  Create a Distribution from an Existing Report 

  * ####  Distributing to a Folder 

  * ####  Distributing With Email 




###  Create a Distribution from an Existing Report 

**Step 1:** First you are going to open a report. The example for this walk-through will use the same PL Trend Report seen in the [ Financial Walk-through ](/KB/HowToUse/Walkthroughs/Financial.html) lab. If needed, download the document here: [ Interject_PLTrendDemo.xlsx ](/wGetStarted/L11.2-Basic-Distribution_128719024.html) . 

![](https://interject.atlassian.net/wiki/download/thumbnails/128719024/7.2BasicDistributionCreateDistributionFromExistingStep1.jpg?version=1&modificationDate=1525197501577&cacheVersion=1&api=v2&width=720&height=326)

  


**Step 2:** When creating a distribution, you are normally taking a worksheet and making a copy for different cost centers. To accomplish this, you need to mark which filter will change for each copy. Do this by adding a Range Tag formula. Type **=jRangeTag()** into cell 26 and hit the **Fx** button. It does not matter where you place this formula since it will be removed automatically as the worksheet is used to create the distribution. 

![](https://interject.atlassian.net/wiki/download/attachments/128719024/7.2BasicDistributionCreateDistributionFromExistingStep2.jpg?version=1&modificationDate=1525197544508&cacheVersion=1&api=v2)

  


**Step 3:** The Function Wizard will open. You want to change the Location filter for each worksheet copy, so type **Location** in the Tag argument. For the Range argument, select cell M22, the Location filter, as shown below. 

![](https://interject.atlassian.net/wiki/download/attachments/128719024/7.2BasicDistributionCreateDistributionFromExistingStep3.jpg?version=1&modificationDate=1525197588649&cacheVersion=1&api=v2)

  


**Step 4:** You need to add a Range Tag for the month as well. In cell O27, type another jRangeTag() formula and click the **Fx** button. 

![](https://interject.atlassian.net/wiki/download/attachments/128719024/image2017-7-20_16-25-47.png?version=1&modificationDate=1500593148624&cacheVersion=1&api=v2)

  


**Step 5:** With the Function Wizard window open, enter **Month** for the Tag argument and **M23** into the Range argument. This will allow us to change the month within the distribution setup. 

![](https://interject.atlassian.net/wiki/download/attachments/128719024/image2017-7-24_10-2-12.png?version=1&modificationDate=1500915733236&cacheVersion=1&api=v2)

  


Once this is completed, the Range Tag formulas should summarize what was setup as seen in the screenshot below. 

![](https://interject.atlassian.net/wiki/download/attachments/128719024/image2017-7-24_10-3-2.png?version=1&modificationDate=1500915783338&cacheVersion=1&api=v2)

  


**Step 6:** Now it is time to create the Distribution worksheet that generates the distribution. You can create this by using the **Export Book** menu item in the INTERJECT ribbon. The Export and Distribution window will appear and click **Create Distribution Sheet** . 

![](https://interject.atlassian.net/wiki/download/attachments/128719024/image2017-7-25_12-58-5.png?version=1&modificationDate=1501012686520&cacheVersion=1&api=v2)

  


INTERJECT will create the Distribution worksheet in the existing workbook and will search for existing Range Tag formulas in the workbook. The screenshot below illustrates the typical defaults that will be used when initially created. 

  *     1. The worksheet names for those that have Range Tag formulas should be added to the Tab Selection columns by default. 
    2. A filter is created for each jRangeTag found in the workbook in the Report Filters columns. 
    3. The Book column should default to 1, noting the first workbook build to be created. More can be added if needed to the same distribution sheet. 



![](https://interject.atlassian.net/wiki/download/attachments/128719024/image2017-7-24_10-48-50.png?version=1&modificationDate=1500918531791&cacheVersion=1&api=v2)

**Note:** The **Enabled?** column contains a drop down list of options that can be applied to the tabs, on an individual basis, which are being created. 

  * **Blank** \- **** When the enabled column is set to blank, INTERJECT interprets this as a **Yes** value and automatically pulls the data after the report is created. 
  * **Yes -** When this column value is set to **Yes** then distribution report builder will automatically create the reports **And** pull the data. 
  * **No -** In the instance that the value is set to **No,** INTERJECT will not build that report tab. 
  * **Prep -** When set to **Prep** the report tabs will be built out, however, the data will not be pulled automatically. 



  


**Step 7:** Edit the distribution defaults further. In this example, you want to create three copies of the **ProfitAndLoss** worksheet, one for each location **7001** , **7002** , and **7120** . And you want to use the month **2002-05** . Use the screenshot below as a guide, and type in the values for columns **Worksheet Tabs** , **Location** , and **Month** . 

![](https://interject.atlassian.net/wiki/download/attachments/128719024/image2017-7-24_10-50-49.png?version=1&modificationDate=1500918650159&cacheVersion=1&api=v2)

  


**Step 8:** You are ready to create a new workbook of reports, but first you need a destination for this distribution. There are many options for the Distribution Target (open, save, print, email, etc.). In this example, you will use the default, **Open** , which creates a new workbook without saving. 

![](https://interject.atlassian.net/wiki/download/attachments/128719024/image2017-7-24_10-51-50.png?version=1&modificationDate=1500918711478&cacheVersion=1&api=v2)

  


**Step 9:** To run the distribution, from the Distribution worksheet click the **Export Book** menu item in the INTERJECT ribbon. Click the **Run Distribution** button that appears in the next window. 

![](https://interject.atlassian.net/wiki/download/attachments/128719024/image2017-7-25_12-26-25.png?version=1&modificationDate=1501010786763&cacheVersion=1&api=v2)

  


As the distribution process is running, it will display its activity and progress as seen below. 

![](https://interject.atlassian.net/wiki/download/attachments/128719024/image2017-7-20_16-33-16.png?version=1&modificationDate=1500593597842&cacheVersion=1&api=v2)

  


When the process is complete, the new workbook opens and the the original workbook is unchanged. Looking closer at what you created, the workbook below has 3 worksheets, and each worksheet has its own filter values as configured. You will notice that the worksheet names are simply incrementally numbers. You will cover how to custom name each tab in the next  [ L11.3 Advanced Distribution ](/KB/HowToCreate/ExportReport/Grouping.html) page. 

![](https://interject.atlassian.net/wiki/download/attachments/128719024/image2017-7-13_10-46-57.png?version=1&modificationDate=1499968015033&cacheVersion=1&api=v2)

  


###  Distributing to a Folder 

Now you are going to do the same distribution, but this time you will save to a specific file folder. 

**Step 1:** To do this, navigate back to the distribution worksheet and change the output to **Excel** in cell E28. 

![](https://interject.atlassian.net/wiki/download/attachments/128719024/image2017-7-24_11-52-56.png?version=1&modificationDate=1500922377119&cacheVersion=1&api=v2)

  


**Step 2:** Now you can name the file and select its destination. 

![](https://interject.atlassian.net/wiki/download/attachments/128719024/image2017-7-24_12-30-31.png?version=1&modificationDate=1500924632752&cacheVersion=1&api=v2)

  


**Step 3:** Now run the distribution. 

** ![](https://interject.atlassian.net/wiki/download/attachments/128719024/image2017-7-25_13-47-40.png?version=1&modificationDate=1501015661928&cacheVersion=1&api=v2) **

****

**Step 4:** After you run the distribution, navigate to its folder to see that the file has been saved correctly. 

![](https://interject.atlassian.net/wiki/download/attachments/128719024/image2017-7-24_12-39-36.png?version=1&modificationDate=1500925177689&cacheVersion=1&api=v2)

###  Distributing With Email 

Navigate back to the page to distribute the workbook via email. 

**Step 1:** First, you need to make sure the email is set up properly. The email distribution requires an SMTP server set up in the [ INTERJECT Portal Website. ](https://portal.gointerject.com/organization-profile.html) The Organizational Profile settings area contains the SMTP information that must be completed beforehand. 

![](https://interject.atlassian.net/wiki/download/attachments/128719024/image2017-7-20_16-41-5.png?version=1&modificationDate=1500594065983&cacheVersion=1&api=v2)

  


Assuming the SMTP information is entered, continue demonstrating email distribution. 

**Step 2:** In the Distribution Target rows of the Distribution worksheet, click the drop down in the Output column. Choose **Email** . 

![](https://interject.atlassian.net/wiki/download/attachments/128719024/image2017-7-24_13-39-46.png?version=1&modificationDate=1500928787718&cacheVersion=1&api=v2)

  


**Step 3:** Now you can type in where the email is going, where the email is from, the subject, and the email message. You will need to work with your IT department to work through email configuration matters to avoid the delivered email being flagged as spam in your corporate email server. This can occur if the From email is any different than configured earlier with the SMTP settings. 

![](https://interject.atlassian.net/wiki/download/attachments/128719024/image2017-7-24_13-21-55.png?version=1&modificationDate=1500927716669&cacheVersion=1&api=v2)

  


Now run the distribution again and the email will be sent to the destination. 

![](https://interject.atlassian.net/wiki/download/attachments/128719024/image2017-7-25_13-49-13.png?version=1&modificationDate=1501015754524&cacheVersion=1&api=v2)

  


Continue learning about distribution in the  [ L11.3 Advanced Distribution ](/KB/HowToCreate/ExportReport/Grouping.html) page. 

  


##    


##  Related Links: 

[ Customer Aging ](/KB/HowToUse/Walkthroughs/CustomerAging.html)

[ INTERJECT Ribbon Menu Items ](/KB/InterjectRibbon.html)

[ L11.3 Advanced Distribution ](/KB/HowToCreate/ExportReport/Grouping.html)
