---
title: Quick Tools - Hyperlink Tools
filename: "QuickTools-Hyperlink.md"
layout: custom
keywords: [Quick Tools, Hyperlink Tools, Reset Hyperlink Targets for Selection, Create/Edit Interject Hyperlink]
headings: ["Overview", "Reset Hyperlink Targets for Selection", "Create/Edit Interject Hyperlink", "Create/Edit Interject Hyperlink : Preserving Styles"]
links: ["/wIndex/INTERJECT-Link-Index.html"]
image_dir: "QuickToolsHyperlink"
images: [{file: "HyperlinkTools",type: "png",site: "Addin",cat: "Quick Tools",sub: "",report: "",ribbon: "",config: ""},{file: "HyperlinkScopeBefore",type: "png",site: "Addin",cat: "Report",sub: "",report: "Customer Aging Summary",ribbon: "",config: ""},{file: "HyperlinkScopeBefore2",type: "png",site: "Addin",cat: "Report",sub: "",report: "",ribbon: "",config: ""},{file: "HyperlinkScopeEditLink",type: "png",site: "Excel",cat: "Right Click Menu",sub: "",report: "",ribbon: "",config: ""},{file: "HyperlinkScopeBadScope",type: "png",site: "Excel",cat: "Edit Hyperlink",sub: "",report: "",ribbon: "",config: ""},{file: "HyperlinkScopeClick",type: "png",site: "Addin",cat: "Quick Tools",sub: "",report: "",ribbon: "",config: ""},{file: "HyperlinkScopeAfter",type: "png",site: "Excel",cat: "Edit Hyperlink",sub: "",report: "",ribbon: "",config: ""},{file: "CreateHyperlinkBefore",type: "png",site: "Addin",cat: "Report",sub: "",report: "",ribbon: "",config: ""},{file: "CreateHyperlinkClick",type: "png",site: "Addin",cat: "Quick Tools",sub: "",report: "",ribbon: "",config: ""},{file: "CreateHyperlinkType",type: "png",site: "Addin",cat: "Quick Tools",sub: "Set Hyperlink",report: "",ribbon: "",config: ""},{file: "CreateHyperlinkByCell",type: "png",site: "Addin",cat: "Quick Tools",sub: "Set Hyperlink",report: "",ribbon: "",config: ""},{file: "CreateHyperlinkAfter",type: "png",site: "Addin",cat: "Report",sub: "",report: "",ribbon: "",config: ""},{file: "HyperlinkStyle",type: "png",site: "Addin",cat: "Report",sub: "",report: "",ribbon: "",config: "Yes"},{file: "HyperlinkStyleMiddle",type: "png",site: "Addin",cat: "Quick Tools",sub: "Set Hyperlink",report: "",ribbon: "",config: "Yes"},{file: "HyperlinkStyleAfter",type: "png",site: "Addin",cat: "Report",sub: "",report: "",ribbon: "",config: "Yes"}]
description: The Hyperlink Tools within Quick Tools deal with Interject Hyperlinks.
---
* * *

## Overview

The Hyperlink Tools within Quick Tools deal with [Interject Hyperlinks](/wIndex/INTERJECT-Link-Index.html).

![](/images/QuickToolsHyperlink/HyperlinkTools.png)
<br>

### Reset Hyperlink Targets for Selection

Sets the scope for hyperlinks to the sheet they are contained in for all hyperlinks in the current cell or all selected cells.

When you paste a hyperlink into another sheet, Excel retains the scope for that hyperlink so it is not set to the sheet you are pasting it into. To demonstrate this, follow these steps:

**Step 1:** First select a hyperlink in the current sheet:

![](/images/QuickToolsHyperlink/HyperlinkScopeBefore.png)
<br>

**Step 2:** Next paste it to another sheet:

![](/images/QuickToolsHyperlink/HyperlinkScopeBefore2.png)
<br>

**Step 3:** Right click the cell and select "Edit Link":

![](/images/QuickToolsHyperlink/HyperlinkScopeEditLink.png)
<br>

Notice the scope of this Hyperlink is still set to the original sheet "Customer Aging":

![](/images/QuickToolsHyperlink/HyperlinkScopeBadScope.png)
<br>

**Step 4:** Click on "Reset Hyperlink Targets for Selection" in Quick Tools and "Run and Close":

![](/images/QuickToolsHyperlink/HyperlinkScopeClick.png)
<br>

Notice the scope has been set correctly to the current sheet "Example":

![](/images/QuickToolsHyperlink/HyperlinkScopeAfter.png)
<br>

### Create/Edit Interject Hyperlink

Opens a window to create or edit an Interject Hyperlink.

To demonstrate this, you will setup an Interject hyperlink that opens the Report Library.

**Step 1:** First select an empty cell and enter a name for the hyperlink:

![](/images/QuickToolsHyperlink/CreateHyperlinkBefore.png)
<br>

**Step 2:** Click on Quick Tools "Create/Edit Interject Hyperlink" and then "Run and Close":

![](/images/QuickToolsHyperlink/CreateHyperlinkClick.png)
<br>

You can select the type of Hyperlink you want to add. In this case select "Interject Report Library" from the dropdown:

![](/images/QuickToolsHyperlink/CreateHyperlinkType.png)
<br>

**Step 3:** Next you need to enter a reference for the hyperlink. You can either select a "Target Cell Name" or a "Cell Address". The "Target Cell Name" option will display a dropdown list of all the range names in the sheet. In this case, use the "Cell Address" option and enter the cell reference of your hyperlink name and "Set Hyperlink":

![](/images/QuickToolsHyperlink/CreateHyperlinkByCell.png)
<br>

The Hyperlink is created!:

![](/images/QuickToolsHyperlink/CreateHyperlinkAfter.png)
<br>

### Create/Edit Interject Hyperlink : Preserving Styles

You can set up a predetermined styling for the Hyperlinks by using a defined name. When a cell has the defined name of "InterjectConfig_HyperlinkStyle", Interject will use the styling of that cell to apply to a hyperlink that is created.

**Step 1:** Select a cell that matches the formatting you wish the Hyperlinks to have and define the cell with the name "InterjectConfig_HyperlinkStyle":

![](/images/QuickToolsHyperlink/HyperlinkStyle.png)
<br>

**Step 2:** Now create another hyperlink using the method in the previous section:

![](/images/QuickToolsHyperlink/HyperlinkStyleMiddle.png)
<br>

Notice the new hyperlink has the same style as the cell with the defined name "InterjectConfig_HyperlinkStyle":

![](/images/QuickToolsHyperlink/HyperlinkStyleAfter.png)
<br>
