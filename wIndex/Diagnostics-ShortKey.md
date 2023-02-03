---
title: Diagnostics - Change ShortKey
layout: custom
keywords: [Diagnostics, Shortkey Changes, Configuration, Config]
description: 
---
* * *   

## Overview

The "Change ShortKey" feature allows users to change the shortcut key for certain Interject actions. 

![](/images/Diagnostics/ChangeShortKey.png)
<br>

These settings are found in the IdsSettings.xml file. For example, an entry in that file may have an entry such as:

\<ShortkeyChanges\>True\</ShortkeyChanges\>

\<ReportLibrary\>Ctrl+Shift+A\</ReportLibrary\>.

This means that the shortkeys changes are active and the Report Library is assigned to the shortkey Ctrl+Shift+A.

Multiple inputs are allowed. For example, you can reassign multiple actions by listing them in the input field and they will be executed in order. Note: You cannot change a shortkey that is currently in use. You must first reassign the action that is set to that shortkey. Also, shortkey changes here will override Excel's shortkey assignments.

**Input Examples:**

| Input | Description |
|----|----|
| DisableAll | Disables all shortkey changes. This will make the default shortkeys active. (Requires Excel restart) |
| EnableAll | Enables all shortkey changes (Requires Excel restart) |
| ReportLibrary=Ctrl+Shift+A | Changes the shortkey of the Report Library to Ctrl-Shift+A |
| Diagnostics=Ctrl+Shift+A<br>DrillOnData=Ctrl+Shift+D<br>Diagnostics=Ctrl+Shift+K | First changes Dianostics, then DrillOnData, and then Diagnostics again |

**Defaults:**

*  Diagnostics=Ctrl+Shift+D

*  Distribution=Ctrl+Shift+E

*  DoLogin=Ctrl+L

*  DrillOnData=Ctrl+Shift+K

*  NavigateBack=Ctrl+Shift+B

*  PullData=Ctrl+Shift+J

*  QuickTools=Ctrl+Shift+T

*  ReportHelper=Ctrl+Shift+H

*  ReportLibrary=Ctrl+Shift+L

*  SaveData=Ctrl+Shift+U
