---
title: Quick Tools - Hyperlink Tools
layout: custom
keywords: [Quick Tools, Hyperlink Tools, Reset Hyperlink Targets for Selection, Create/Edit Interject Hyperlink]
headings: ["Overview", "Reset Hyperlink Targets for Selection", "Create/Edit Interject Hyperlink", "Create/Edit Interject Hyperlink : Preserving Styles"]
links: ["/wIndex/INTERJECT-Link-Index.html"]
description: The Hyperlink Tools within Quick Tools deal with Interject Hyperlinks.
---
* * *

## Overview

The Hyperlink Tools within Quick Tools deal with [Interject Hyperlinks](/wIndex/INTERJECT-Link-Index.html).

![](/images/QuickTools/HyperlinkTools.png)
<br>

### Reset Hyperlink Targets for Selection

Sets the scope for hyperlinks to the sheet they are contained in for all hyperlinks in the current cell or all selected cells.

When you paste a hyperlink into another sheet, Excel retains the scope for that hyperlink so it is not set to the sheet you are pasting it into. To demonstrate this, follow these steps:

**Step 1:** First select a hyperlink in the current sheet:

![](/images/QuickTools/HyperlinkScopeBefore.png)
<br>

**Step 2:** Next paste it to another sheet:

![](/images/QuickTools/HyperlinkScopeBefore2.png)
<br>

**Step 3:** Right click the cell and select "Edit Link":

![](/images/QuickTools/HyperlinkScopeEditLink.png)
<br>

Notice the scope of this Hyperlink is still set to the original sheet "Customer Aging":

![](/images/QuickTools/HyperlinkScopeBadScope.png)
<br>

**Step 4:** Click on "Reset Hyperlink Targets for Selection" in Quick Tools and "Run and Close":

![](/images/QuickTools/HyperlinkScopeClick.png)
<br>

Notice the scope has been set correctly to the current sheet "Example":

![](/images/QuickTools/HyperlinkScopeAfter.png)
<br>

### Create/Edit Interject Hyperlink

Opens a window to create or edit an Interject Hyperlink.

To demonstrate this, you will setup an Interject hyperlink that opens the Report Library.

**Step 1:** First select an empty cell and enter a name for the hyperlink:

![](/images/QuickTools/CreateHyperlinkBefore.png)
<br>

**Step 2:** Click on Quick Tools "Create/Edit Interject Hyperlink" and then "Run and Close":

![](/images/QuickTools/CreateHyperlinkClick.png)
<br>

You can select the type of Hyperlink you want to add. In this case select "Interject Report Library" from the dropdown:

![](/images/QuickTools/CreateHyperlinkType.png)
<br>

**Step 3:** Next you need to enter a reference for the hyperlink. You can either select a "Target Cell Name" or a "Cell Address". The "Target Cell Name" option will display a dropdown list of all the range names in the sheet. In this case, use the "Cell Address" option and enter the cell reference of your hyperlink name and "Set Hyperlink":

![](/images/QuickTools/CreateHyperlinkByCell.png)
<br>

The Hyperlink is created!:

![](/images/QuickTools/CreateHyperlinkAfter.png)
<br>

### Create/Edit Interject Hyperlink : Preserving Styles

You can set up a predetermined styling for the Hyperlinks by using a defined name. When a cell has the defined name of "InterjectConfig_HyperlinkStyle", Interject will use the styling of that cell to apply to a hyperlink that is created.

**Step 1:** Select a cell that matches the formatting you wish the Hyperlinks to have and define the cell with the name "InterjectConfig_HyperlinkStyle":

![](/images/QuickTools/HyperlinkStyle.png)
<br>

**Step 2:** Now create another hyperlink using the method in the previous section:

![](/images/QuickTools/HyperlinkStyleMiddle.png)
<br>

Notice the new hyperlink has the same style as the cell with the defined name "InterjectConfig_HyperlinkStyle":

![](/images/QuickTools/HyperlinkStyleAfter.png)
<br>
