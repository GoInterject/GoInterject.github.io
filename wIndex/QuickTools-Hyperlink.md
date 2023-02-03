---
title: Quick Tools - Hyperlink Tools
layout: custom
keywords: [Quick Tools, Hyperlink Tools, Reset Hyperlink Targets for Selection, Create/Edit Interject Hyperlink]
description: The Hyperlink Tools within Quick Tools deal with Interject Hyperlinks.
---
* * *

## Overview

The Hyperlink Tools within Quick Tools deal with [Interject Hyperlinks](/wIndex/INTERJECT-Link-Index.html).

![](/images/QuickTools/HyperlinkTools.png)
<br>

### Reset Hyperlink Targets for Selection

Sets the scope to the current sheet for hyperlinks in the current cell or all selected cells.

**Step 1:** First select a hyperlink in the current sheet:

![](/images/QuickTools/HyperlinkScopeBefore.png)
<br>

**Step 2:** Next paste it to another sheet:

![](/images/QuickTools/HyperlinkScopeBefore2.png)
<br>

**Step 3:** Right click the cell and select Link>Edit Link:

![](/images/QuickTools/HyperlinkScopeEditLink.png)
<br>

Notice the scope of this Hyperlink is still set to the original sheet:

![](/images/QuickTools/HyperlinkScopeBadScope.png)
<br>

**Step 4:** Click on Quick Tools > "Reset Hyperlink Targets for Selection":

![](/images/QuickTools/HyperlinkScopeClick.png)
<br>

Notice the scope has been set correctly to the current sheet:

![](/images/QuickTools/HyperlinkScopeAfter.png)
<br>

### Create/Edit Interject Hyperlink

Opens a window to create an Interject Hyperlink.

**Step 1:** First setup a [jDropdown](/wIndex/jDropdown.html) function and select the cell you want to create a Hyperlink (see [here](/wGetStarted/L-Create-Dropdowns.html#adding-a-named-range) for an example of how to set up a jDropdown):

![](/images/QuickTools/CreateHyperlinkBefore.png)
<br>

**Step 2:** Click on Quick Tools "Create/Edit Interject Hyperlink":

![](/images/QuickTools/CreateHyperlinkClick.png)
<br>

You can select the type of Hyperlink you want to add. In this case select Dropdown:

![](/images/QuickTools/CreateHyperlinkType.png)
<br>

**Step 3:** Next either enter a defined name for the jDropdown function or the cell it is found in:

![](/images/QuickTools/CreateHyperlinkByName.png)
<br>

![](/images/QuickTools/CreateHyperlinkByCell.png)
<br>

The Hyperlink is created!:

![](/images/QuickTools/CreateHyperlinkAfter.png)
<br>

**Step 4:** You can set up a predetermined styling for the Hyperlinks by using a defined name. Select a cell that matches the formatting you wish the Hyperlinks to have and define the cell with the name "InterjectStyle_Hyperlink":

![](/images/QuickTools/HyperlinkStyle.png)
<br>

Now after you create a Hyperlink, the styling will automatically be set:

![](/images/QuickTools/HyperlinkStyleAfter.png)
<br>
