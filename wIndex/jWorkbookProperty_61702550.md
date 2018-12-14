---
title: jWorkbookProperty()
layout: custom
---

## Function Summary
The jWorkbookProperty is a standalone INTERJECT function. It's purpose is to provide context and information about a workbook in a report. It leverages native Excel workbook properties as well as INTERJECT workbook properties such as the version of the report set in the report library. 

### Function Arguments

|Argument Name|Description|Default|Optional|
|:---|:---|:---|:---|
|PropertyName|This is a string value that matches a workbook property. It can be a custom property or a native workbook property.||NO|

### Excel Formula Bar Example

```Excel
 jWorkbookProperty("Interject_LinkVersion")
```
An example of this function is currently in construction in our documentation labs. Check back soon for an example with more context.

### Example Function Composition

|Argument Name|Example Mapping|Explanation|
|:---|:---|:---|
|Function Name|`=jWorkbookProperty`|This is the excel name used to call the function. It is meant to be standalone and not embedded in other functions.|
|PropertyName|Interject_LinkVersion| This property name is created when an Interject report is uploaded to the [Report Library](/wAbout/Report-Library-Basics_61702517.html) and it will return the version of the report. Other workbook properties that can be called in this function can be found in the list below.|

### Workbook Property List

**Native Excel Properties**

* Title
* Comments
* Category
* Subject
* Author
* Company
* Keywords
 
**Custom Workbook Properties**

This function supports custom workbook properties, so any properties that you set in **Advanced Properties** for your workbook can be used by this function. This section is also where INTERJECT will define its own properties.