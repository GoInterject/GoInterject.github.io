---
title: Diagnostics - Apply Special Features
layout: custom
keywords: [Diagnostics, Apply Special Features, Configuration, Config, animations, bug fix]
description: The "Apply Special Features" in the Interject Diagnostics Pane allows users to apply certain bux fixes.
---
* * *   

## Overview

The "Apply Special Features" in the Interject Diagnostics Pane allows users to apply certain bux fixes.

![](/images/Diagnostics/ApplySpecialFeatures.png)
<br>

### BugFix1: Microsoft Animations

The Microsoft Animations Bug caused certain screen issues due to Microsoft's Animation settings. This bug has been fixed in recent Interject versions but the setting remains here for users to be able to turn on/off animations.

**Turn Off Animations:** To turn off animations, enter the following in the Input field and press &lt;Execute Selected Action&gt;:

```
BugFix1=ON
```

![](/images/Diagnostics/BugFix1On.png)
<br>

**Turn On Animations:** To turn on animations, enter the following in the Input field and press &lt;Execute Selected Action&gt;:

```
BugFix1=OFF
```

![](/images/Diagnostics/BugFix1Off.png)
<br>

### BugFix2: Microsoft Repaint

The Microsoft Repaint Bug causes screen issues when an Excel Add-In programatically switches focus to another tab. This bug is present for some users starting with Excel versions 2210. If you are experiencing issues with slow-down and screen issues when drilling data, this bug fix may help.

**Turn On Repaint Bug Fix:** To enable this bug fix, enter the following in the Input field and press &lt;Execute Selected Action&gt;:

```
BugFix2=ON
```

![](/images/Diagnostics/BugFix2On.png)
<br>

**Turn Off Repaint Bug Fix:** To disable this bug fix, enter the following in the Input field and press &lt;Execute Selected Action&gt;:

```
BugFix2=OFF
```

![](/images/Diagnostics/BugFix2Off.png)
<br>
