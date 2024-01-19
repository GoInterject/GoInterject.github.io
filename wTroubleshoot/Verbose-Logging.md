---
title: Verbose Logging
filename: "Verbose-Logging.md"
layout: custom
keywords: [app, errors, reset, send report, verbose logging]
headings: ["Overview", "Turn on Verbose Logging"]
links: ["/wTroubleshoot/Reporting-A-Problem.html#send-report-to-interject"]
image_dir: "Verbose-Logging"
description: To help diagnose any errors, Interject uses a Verbose Logging feature. The ideal goal of Verbose Logging is to help recreate an error and send logs to Interject's support team, where it can be fixed.
---
* * *

## Overview

Errors can occur for many reasons. Sometimes they are related to the environment or computer running Interject. It is important you have tools to capture everything that is interacting with Excel so, it is easier diagnose the cause of errors. This leads to faster troubleshooting and repair. To help diagnose any errors, Interject uses a Verbose Logging feature. The ideal goal of Verbose Logging is to help recreate an error and send logs to Interject's support team, where it can be fixed.

Verbose Logging will do four things:

* Capture timed points so that slowdown issues can be isolated
* Log errors in real time
* Track activity so that, if Excel crashes, the exact events leading up to the crash are known
* Record general information about the system environment so that the context of the problem can be reproduced

To send the Verbose Logs to Interject, see [Send Report To Interject](/wTroubleshoot/Reporting-A-Problem.html#send-report-to-interject).

### Turn on Verbose Logging

**Step 1:** You will need to go to the diagnostic wizard. Click the **Advanced Menu** button on the Interject ribbon.

![](/images/Verbose-Logging/01.jpg)
<br>

Next click **Diagnostics**.

![](/images/Verbose-Logging/02.jpg)
<br>

**Step 2:** You need to **Turn On** **Verbose Logging**, because it is **Off** by default.

To turn it on, select the **Toggle Verbose Logging** option in the menu, then click **Execute Selected Action**.

![](/images/Verbose-Logging/ToggleVerboseLogging.png)
<br>

**Step 3:** Confirm that the logging is **Turned On**.

![](/images/Verbose-Logging/ConfirmVerboseLogging.png)
<br>

**Note: All activity will be logged for 16 hours**, but you can turn them off at any time with the same steps used to turn them on. While logging is on, the system will perform a little slower then usual. Multiple log files may be created, and they will be available for ten days. If Excel is closed, the logging process automatically begins once Excel is restarted. The Results section shows where the log file is located:

![](/images/Verbose-Logging/VerboseLoggingResults.png)
<br>