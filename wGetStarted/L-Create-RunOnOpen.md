---
title: "Lab Create: INTERJECT Run On Open"
layout: custom
keywords: [auto-run, run-on-open, run, pull, property ]
description: Use this property to auto-pull the report when opening for the first tab that appears. No VBA required.
---

##  **Overview:**

Some reports require defaults or have summary pages that must be pulled before others in order for the report to function properly. Using the Run on Open INTERJECT property will auto-run the first tab that appears. This can save time and helps streamline INTERJECT processes. 

For this walkthrough, we will be using the [ Customer Aging Report ](/wGetStarted/L-Create-CustomerAging.html).

## Setting up Run on Open

**Step 1:** To begin, open the **Customer Collections** report in the [ Report Library ](/wAbout/Report-Library-Basics.html). 

![](/images/L-Create-RunOnOpen/01.png)

<br> 

**Step 2** In the excel Ribbon, click on "File" to bring up the file screen.

![](/images/L-Create-RunOnOpen/02.png)
<br>
**Step 3** In the Info section, select "Advanced properties" in the properties dropdown to bring up the properties window.

![](/images/L-Create-RunOnOpen/03.png)
<br>
**Step 4** Navigate to the "Custom" page and in the "Name" textbox, input "Interject_RunOnOpen" and the type field should be "Text"

![](/images/L-Create-RunOnOpen/04.png)
<br>
**Step 5** In the "Value" box, there are two options: Run on the first tab that is seen on open, or run on a specific tab.
**Option 1** If you would like to run on the first tab seen, set value to "True" and click "Add".
![](/images/L-Create-RunOnOpen/05.png)
<br>
**Option 2** If you would like to run on a specific tab, set the value to "T:*TabName*" and click "Add".

In this case, type, "T:CustomerAging" to specify the tab CustomerAging to be pulled on open. 
![](/images/L-Create-RunOnOpen/06.png)
<br> 

**Step 6** Save the file and [ Update the report library ](/wGetStarted/L-Create-UpdatingReportLibrary.html) with the new file

![](/images/L-Create-RunOnOpen/07.png)
<br>

**Step 8** Close and reopen the file through the report library and it will auto-pull the report

![](/images/L-Create-RunOnOpen/08.png)
<br>