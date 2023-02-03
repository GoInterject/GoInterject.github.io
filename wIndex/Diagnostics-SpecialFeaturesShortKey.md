---
title: Diagnostics - Special Features and Change ShortKey
layout: custom
keywords: [Diagnostics, Apply Special Features, Shortkey Changes, Configuration, Config]
description: 
---
* * *   

## Apply Special Features

The "Apply Special Features" in the Interject Diagnostics Pane allows users to apply certain bux fixes:

![](/images/Diagnostics/ApplySpecialFeatures.png)
<br>

### BugFix1: Microsoft Animations

The Microsoft Animations Bug was a bug that caused certain screen issues due to Microsoft's Animation settings. This bug has been fixed in recent Interject versions but the setting remains here for users to be able to turn on/off animations.

**Input:**

'BugFix1=ON' to turn _off_ animations

'BugFix1=OFF' to turn _on_ animations

### BugFix2: Microsoft Repaint

The Microsoft Repaint Bug is a bug that causes screen issues when an Excel Add-In programatically switches focus to another tab. This bug is present for some users starting with Excel versions 2210. If you are experiencing issues with slow-down and screen issues when drilling data, this bug fix may help.

**Input:**

'BugFix2=ON' to apply bug fix

'BugFix2=OFF' to unapply bug fix

## Change ShortKey

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
