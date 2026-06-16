---
title: Diagnostics - Apply Special Features
filename: "Diagnostics-SpecialFeatures.md"
layout: custom
keywords: [Diagnostics, Apply Special Features, Configuration, Config, animations, bug fix]
headings: ["Overview", "BugFix1: Microsoft Animations", "BugFix2: Microsoft Repaint", "Macro Security Settings", "Webview2/Browser Login"]
links: ["/wDeveloper/MacroSecurity.html"]
image_dir: "DiagnosticsSpecialFeatures"
images: [
    {file: "ApplySpecialFeatures", type: "png", site: "Add-in", cat: "Diagnostics", sub: "Apply Special Features", report: "", ribbon: "", config: ""}, 
    {file: "BugFix1On", type: "png", site: "Add-in", cat: "Diagnostics", sub: "Apply Special Features", report: "", ribbon: "", config: ""}, 
    {file: "BugFix1Off", type: "png", site: "Add-in", cat: "Diagnostics", sub: "Apply Special Features", report: "", ribbon: "", config: ""}, 
    {file: "BugFix2On", type: "png", site: "Add-in", cat: "Diagnostics", sub: "Apply Special Features", report: "", ribbon: "", config: ""}, 
    {file: "BugFix2Off", type: "png", site: "Add-in", cat: "Diagnostics", sub: "Apply Special Features", report: "", ribbon: "", config: ""},
    {file: "MacroSecuritySettings", type: "png", site: "Add-in", cat: "Diagnostics", sub: "Apply Special Features", report: "", ribbon: "", config: ""},
	{file: "LoginCompare", type: "png", site: "Add-in", cat: "Login", sub: "", report: "", ribbon: "", config: ""},
	{file: "Webview2True", type: "png", site: "Add-in", cat: "Diagnostics", sub: "Apply Special Features", report: "", ribbon: "", config: ""},
	{file: "Webview2False", type: "png", site: "Add-in", cat: "Diagnostics", sub: "Apply Special Features", report: "", ribbon: "", config: ""}
    ]
description: The "Apply Special Features" in the Interject Diagnostics Pane allows users to apply certain configurations and bug fixes.
---
* * *   

## Overview

The "Apply Special Features" in the Interject Diagnostics Pane allows users to apply certain configurations and bug fixes.

![](/images/DiagnosticsSpecialFeatures/ApplySpecialFeatures.png)
<br>

### BugFix1: Microsoft Animations

The Microsoft Animations Bug caused certain screen issues due to Microsoft's Animation settings. This bug has been fixed in recent Interject versions but the setting remains here for users to be able to turn on/off animations.

**Turn Off Animations:** To turn off animations, enter the following in the Input field and press &lt;Execute Selected Action&gt;:

```
BugFix1=ON
```

![](/images/DiagnosticsSpecialFeatures/BugFix1On.png)
<br>

**Turn On Animations:** To turn on animations, enter the following in the Input field and press &lt;Execute Selected Action&gt;:

```
BugFix1=OFF
```

![](/images/DiagnosticsSpecialFeatures/BugFix1Off.png)
<br>

### BugFix2: Microsoft Repaint

The Microsoft Repaint Bug causes screen issues when an Excel Add-In programmatically switches focus to another tab. This bug is present for some users starting with Excel versions 2210. If you are experiencing issues with slow-down and screen issues when drilling data, this bug fix may help.

**Turn On Repaint Bug Fix:** To enable this bug fix, enter the following in the Input field and press &lt;Execute Selected Action&gt;:

```
BugFix2=ON
```

![](/images/DiagnosticsSpecialFeatures/BugFix2On.png)
<br>

**Turn Off Repaint Bug Fix:** To disable this bug fix, enter the following in the Input field and press &lt;Execute Selected Action&gt;:

```
BugFix2=OFF
```

![](/images/DiagnosticsSpecialFeatures/BugFix2Off.png)
<br>

## Macro Security Settings

These are displayed for your reference here. For more on information, see [Macro Security](/wDeveloper/MacroSecurity.html)

![](/images/DiagnosticsSpecialFeatures/MacroSecuritySettings.png)
<br>

## Webview2/Browser Login

Interject provides an alternative to the standard Webview2 login form. Your default web browser can be used instead by setting the UseWebView2 switch in Diagnostics.

<blockquote class=highlight_note>
<b>Note:</b> Web browser login is explicitly supported for Edge, Firefox, Chrome, Opera, Safari, Brave, Vivaldi, and Internet Explorer, but may also work on other browsers.
</blockquote>
<br>

![](/images/DiagnosticsSpecialFeatures/LoginCompare.png)
<br>

```
UseWebView2=TRUE
```

![](/images/DiagnosticsSpecialFeatures/Webview2True.png)
<br>

```
UseWebView2=FALSE
```

![](/images/DiagnosticsSpecialFeatures/Webview2False.png)
<br>
