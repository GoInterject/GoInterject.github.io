---
title: "Lab Create: INTERJECT Run On Open"
layout: custom
keywords: [auto-run, run-on-open, run, pull, property ]
description: Use this property to auto-pull the report when opening for the first tab that appears. No VBA required.
---

##  **Overview:**

Some reports require default values, settings, or have summary pages that must be pulled before others in order for the report to function properly. Using the Run on Open INTERJECT property will auto-run the first tab that appears. This can save time and helps streamline INTERJECT processes. 

We will walk through Run on Open using the [ Customer Aging Report ](/wGetStarted/L-Create-CustomerAging.html).

<blockquote class=lab_info>
  If you are following the Training Labs, this report file can be found in the Report Library at Training Labs > Lab 6 Special Features > Lab 6.4 Interject Run On Open.
</blockquote>

## Setting up Run on Open

**Step 1:** To begin, open the **Customer Collections** report in the [ Report Library ](/wAbout/Report-Library-Basics.html). 

![](/images/L-Create-RunOnOpen/01.png)
<br> 

**Step 2** Click on **File** in the Excel Ribbon to bring up the file screen.

![](/images/L-Create-RunOnOpen/02.png)
<br>

**Step 3** Under Info, select **Advanced Properties** in the Properties dropdown. The Properties window will open.

![](/images/L-Create-RunOnOpen/03.png)
<br>

**Step 4** Under the **Custom** tab find the **Name** textbox and type **Interject_RunOnOpen.** The **Type** field should be **Text.**

![](/images/L-Create-RunOnOpen/04.png)
<br>

**Step 5** The **Value** box below takes two options: **True** or **T:*TabName***. **True** will will cause Excel to run on the first tab seen on open. Specify the tab name to default to that tab.

**Option 1** If you would like to run on the first tab seen, set value to **True** and click **Add**.
![](/images/L-Create-RunOnOpen/05.png)
<br>

**Option 2** If you would like to run on a specific tab, set the value to **T:*TabName*** and click **Add**.

In this case, we want to pull CustomerAging on open, so type **T:CustomerAging** and that tab will be pulled. 
![](/images/L-Create-RunOnOpen/06.png)
<br> 

**Step 6** Save the file, and [ Update the report library ](/wGetStarted/L-Create-UpdatingReportLibrary.html) with the new file

![](/images/L-Create-RunOnOpen/07.png)
<br>

**Step 7** Close and reopen the file through the Report Library, and Excel will auto-pull the report

![](/images/L-Create-RunOnOpen/08.png)
<br>
