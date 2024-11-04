---
title: Diagnostics - Change ShortKey
filename: "Diagnostics-ShortKey.md"
layout: custom
keywords: [Diagnostics, Shortkey Changes, Configuration, Config, hotkey, keystrokes, shortcut, keyboard]
headings: ["Overview", "Input Examples", "Defaults", "Multiple Input Example"]
links: ["/wIndex/INTERJECT-Hotkey-Index.html#default-shortkey-index"]
image_dir: "DiagnosticsShortKeys"
images: [
    {file: "ChangeShortKey", type: "png", site: "Add-in", cat: "Diagnostics", sub: "Change ShortKey", report: "", ribbon: "", config: ""}, 
    {file: "ChangeShortKey", type: "png", site: "Add-in", cat: "Diagnostics", sub: "Change ShortKey", report: "", ribbon: "", config: ""}, 
    {file: "MultipleInputsShortKey", type: "png", site: "Add-in", cat: "Diagnostics", sub: "Change ShortKey", report: "", ribbon: "", config: ""}, 
    {file: "MultipleInputsShortKeyExecute", type: "png", site: "Add-in", cat: "Diagnostics", sub: "Change ShortKey", report: "", ribbon: "", config: ""}
    ]
description: The "Change ShortKey" feature allows users to change the shortcut key for certain Interject actions.
---
* * *

## Overview

The "Change ShortKey" feature allows users to change the shortcut key for certain Interject actions.

![](/images/DiagnosticsShortKeys/ChangeShortKey.png)
<br>

These settings are found in the IdsSettings.xml file. For example, an entry in that file may have an entry such as:

\<ShortkeyChanges\>True\</ShortkeyChanges\> (Shortkey changes are active)

\<ReportLibrary\>Ctrl+Shift+A\</ReportLibrary\> (Report Library is assigned to the shortkey Ctrl+Shift+A)

<blockquote class=highlight_note>
<b>Note:</b> You cannot change a shortkey that is currently in use. You must first reassign the action that is set to that shortkey. Also, shortkey changes here will override Excel's shortkey assignments.
</blockquote>
<br>

### Input Examples

| Input | Description |
|----|----|
| DisableAll | Disables all shortkey changes. This will make the default shortkeys active. (Requires Excel restart) |
| EnableAll | Enables all shortkey changes (Requires Excel restart) |
| ReportLibrary=Ctrl+Shift+A | Changes the shortkey of the Report Library to Ctrl-Shift+A |
| Diagnostics=Ctrl+Shift+A<br>DrillOnData=Ctrl+Shift+D<br>Diagnostics=Ctrl+Shift+K | First changes Dianostics, then DrillOnData, and then Diagnostics again |

### Defaults

For a list of ShortKey defaults, see [here](/wIndex/INTERJECT-Hotkey-Index.html#default-shortkey-index).

### Multiple Input Example

Multiple inputs are allowed. For example, you can reassign multiple actions by listing them in the input field and they will be executed in order.

**Step 1:** Open the Diagnostics window and navigate to the "Change ShortKey" section:

![](/images/DiagnosticsShortKeys/ChangeShortKey.png)
<br>

**Step 2:** Input the following in the "Input" field:

```
EnableAll
Diagnostics=Ctrl+Shift+A
DrillOnData=Ctrl+Shift+D
Diagnostics=Ctrl+Shift+K
```

![](/images/DiagnosticsShortKeys/MultipleInputsShortKey.png)
<br>

**Step 3:** Click on &lt;Execute Selected Action&gt;:

![](/images/DiagnosticsShortKeys/MultipleInputsShortKeyExecute.png)
<br>

**Result:** Shortkey changes are enabled, Diagnostics command is set to Ctrl+Shift+K and DrillOnData command is set to Ctrl+Shift+D.
