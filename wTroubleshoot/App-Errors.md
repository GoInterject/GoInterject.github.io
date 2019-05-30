---
title: Troubleshooting App Errors
layout: custom
keywords: [app, errors, reset, send report, verbose logging]
description: Errors can occur for many reasons. Sometimes they are related to the environment or computer running Interject. It is important you have tools to capture everything that is interacting with Excel so, it is easier diagnose the cause of errors. This leads to faster troubleshooting and repair.
---



##  **Overview**

Errors can occur for many reasons. Sometimes they are related to the environment or computer running Interject. It is important you have tools to capture everything that is interacting with Excel so, it is easier diagnose the cause of errors. This leads to faster troubleshooting and repair. To help diagnose any errors, Interject uses a Verbose Logging feature. The ideal goal of Verbose Logging is to help recreate an error and send logs to INTERJECT's support team, where it can be fixed. 
 

###  Turning On Verbose Logging 

Verbose Logging will do four things: 

* **Capture timed points so that slowdown issues can be isolated** 
* **Log errors in real time**
* **Track activity so that, if Excel crashes, the exact events leading up to the crash are known**
* **Record general information about the system environment so that the context of the problem can be reproduced**



**Step 1:** You will need to go to the diagnostic wizard. Select the **Advanced Menu** and click **Diagnostics**.

![](/images/App-Errors/01.jpg)

<br>

![](/images/App-Errors/02.jpg)

<br> 


**Step 2:** You need to **Turn On** **Verbose Logging**, because it is **Off** by default. 

To turn it on, select the **Toggle Verbose Logging** option in the menu, then click **Execute Selected Action**.

![](/images/App-Errors/03.jpg)

<br> 


**Step 3:** Confirm that the logging is **Turned On**. 

![](/images/App-Errors/04.jpg)

<br>

**Note: All activity will be logged until 12am the day of activation**, but you can turn them off at any time with the same steps used to turn them on. While logging is on, the system will perform slower then usual. Multiple log files may be created, and they will be available for ten days. If Excel is closed, the logging process automatically begins once Excel is restarted. All logs are saved to the following file locaton: 

C:\Users\ **MyUserName** \Appdata\Local\Interject\Settings\ErrorContextTrace_ **20180611091456602**.txt 

###  Sending Verbose Logs 

**Step 1:** To send logs to INTERJECT support, select the **User Support** button, then select **Report a Problem**. 

![](/images/App-Errors/05.jpg)

<br> 


**Step 2:** Enter your information and a detailed note about what happened 

![](/images/App-Errors/06.jpg)

<br>

**Step 3:** Click **Send Report** to send logs to the INTERJECT support team. 

**Note:** If Verbose Logging is still on, INTERJECT will ask if you would like to turn it off. 


