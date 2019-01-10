---
title: jFocus()
layout: custom
keywords: [jfocus, function]
description: The jFocus() formatting function is executed in conjunction with a freeze/unfreeze panes action performed in the Quick Tools menu. 
---

## Function Summary

The jFocus() formatting function is executed in conjunction with a freeze/unfreeze panes action performed in the [Quick Tools](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#quick-tools) menu. It sets the excel focus (active cell selection) upon a freeze panes action. This is often conducted before uploading a report to the INTERJECT [Report Library](/wAbout/Report-Library-Basics.html) and is often paired with a [jFreezePanes](/wIndex/jFreezePanes.html) formatting function.

### Function Arguments

| Argument Name | Description                                                                                      | Default | Optional |
|----------------|--------------------------------------------------------------------------------------------------|---------|----------|
| Target         | This is a cell address that upon a freeze panes action will place the excel active selection to. |         | NO       |

### Excel Formula Bar Example

```Excel
    =jFocus(C17)
```
An example of this function is currently in construction in our documentation labs. Check back soon for an example with more context.

### Example Function Composition

| Argument Name | Example Mapping | Explanation                                                                                                          |
|---------------|-----------------|----------------------------------------------------------------------------------------------------------------------|
| Function Name | `=jFocus`       | This is the excel function name used to call the function. It can only be used as a standalone function in a report. |
| Target        | C17             | Cell C17 is the cell that will be selected upon a freeze panes action.                                               |
