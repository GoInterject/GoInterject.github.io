---
title: jWorkbookProperty()
filename: "jWorkbookProperty.md"
layout: custom
keywords: [jWorkbookProperty, helper, function, formula]
headings: ["Function Summary", "Function Arguments", "Excel Formula Bar Example", "Function Composition", "Workbook Property List"]
links: ["/wGetStarted/L-Create-InventoryFixed.html#jworkbookproperty", "/wAbout/Report-Library-Basics.html#using-the-report-library"]
image_dir: ""
images: []
description: The jWorkbookProperty function extracts information from the properties of the workbook.
---
* * *

##  Function Summary

The jWorkbookProperty function extracts information from the properties of the workbook.

This function can be used as a standalone function and does not need to be embedded in another function.

For an example of this function, see [Lab Create: Inventory Fixed](/wGetStarted/L-Create-InventoryFixed.html#jworkbookproperty).

###  Function Arguments

<button class="collapsible-parameter">**PropertyName**<br>A string value indicating which property to extract.</button>
<div markdown="1" class="panel-parameter">
<table>
  <tbody>
    <tr>
		<td class="pph"><b>Type</b></td>
		<td>String</td>
    </tr>
    <tr>
		<td class="pph"><b>Constraints</b></td>
		<td>Max 255 char</td>
    </tr>
    <tr>
		<td class="pph"><b>If Blank</b></td>
		<td>Nothing is extracted</td>
    </tr>
  </tbody>
</table>
</div>

###  Excel Formula Bar Example

```Excel
=jWorkbookProperty("Interject_LinkVersion")
```

###  Function Composition

| Argument Name  |  Example Mapping  |  Explanation   |  
|------|------|------|
|  Function Name  |  =jWorkbookProperty  |  The name of this function.  |  
|  PropertyName  |  Interject_LinkVersion  |  This function will return the value of the custom property "Interject_LinkVersion".  |  

###  Workbook Property List

**Native Excel Properties**

These are properties that can be extracted using this function. They are native to every Excel workbook and can be edited on the workbook's info page in settings. They can be extracted with the following values (case-insensitive):

* Title
* Comments
* Category
* Subject
* Author
* Company
* Keywords
 
**Custom Workbook Properties**

In addition to the native Excel properties, this function can also extract custom workbook properties. You can add or edit these properties in the Advanced Properties on the workbook's info page in settings. Interject utilizes these custom properties to store information about the workbook. These custom properties are displayed in the [Report Library](/wAbout/Report-Library-Basics.html#using-the-report-library) and can be extracted with this function (case-sensitive).
