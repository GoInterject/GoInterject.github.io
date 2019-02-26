---
title: jRangeTag()
layout: custom
keywords: [jrangetag, function]
description: The jRangeTag() function is used to label or tag a range or a single cell with a custom name.
---
##  Function Summary 

The jRangeTag() function is used to label or tag a range or a single cell with a custom name. It is possible to use jRangeTag() to insert specific data into the specified region. It is also possible to use jRangeTag() to locate setting on a worksheet 

###  Function Arguments   

| Parameter Name | Description                                                                 | Default | Optional |
| -------------- | --------------------------------------------------------------------------- | ------- | -------- |  
| Tag            | The user defined name for a cell range or address                           |         | NO       |
| Range          | This is the cell area or address that is selected from within the worksheet |         | NO       |

### Excel Formula Bar Example

```Excel
jRangeTag("Location",M22)
```

To see an example of this function in use, visit the [Lab Create: Basic Distribution](/wGetStarted/L-Export-BasicDist.html)

###  Function Composition   

| Formula       | Example      | Explanation                                                          |
| ------------- | ------------ | -------------------------------------------------------------------- |
| Function Name | =jRangeTag() | The name of the report formula                                       |
| Tag           | "Location"   | The custom name for the range (see below).                           |
| Range         | M22          | The set of cells in the worksheet that will be identified by the tag |
