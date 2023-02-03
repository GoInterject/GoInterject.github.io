---
title: Diagnostics - Apply Special Features
layout: custom
keywords: [Diagnostics, Apply Special Features, Configuration, Config]
description: 
---
* * *   

## Overview

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
