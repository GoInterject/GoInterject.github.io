---
title: Helper Functions
filename: "Helper-Functions.md"
layout: custom
keywords: [helper, functions, formula]
headings: ["Overview", "jDropdown", "jFocus", "jFreezePanes", "jCombine", "jCombineIf", "jDataPortal", "jColumnDef", "jRangeTag", "jWorkbookProperty", "jSetting", "Pair", "PairGroup", "Param"]
links: ["/wFunctions/jDropdown.html", "/wFunctions/jFocus.html", "/wFunctions/jFreezePanes.html", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#quick-tools", "/wFunctions/jFreezePanes.html", "/wFunctions/jCombine.html", "/wFunctions/jCombineIf.html", "/wFunctions/jDataPortal.html", "/wFunctions/jColumnDef.html", "/wFunctions/jRangeTag.html", "/wFunctions/jWorkbookProperty.html", "/wFunctions/jSetting.html", "/wFunctions/Pair.html", "/wFunctions/PairGroup.html", "/wFunctions/PairGroup.html", "/wFunctions/Pair.html", "/wFunctions/Param.html", "/wTroubleshoot/Reports.html#validation-report-for-interject-events"]
image_dir: ""
images: []
description: Helper Functions are functions that are often embedded into other parent functions to be leveraged into more specific and accurate functions or enhance their capabilities.
---
* * *

## Overview

Helper Functions are functions that help streamline the report generation process and offer additional customization. They are often embedded into other parent functions to be leveraged into more specific and accurate functions or enhance their capabilities. Some can also be used as stand-alone functions to add functionality to the page.

Other Helper Functions are focused on the report itself and does not impact or direct data in the report. These functions can improve the speed and presentation of which data can be understood, manipulated and viewed in the report.

### [jDropdown](/wFunctions/jDropdown.html)

The jDropdown function returns data from a Data Portal that can be displayed in a dropdown window for the user to select and insert into a designated cell within the spreadsheet. It is typically used to easily insert a valid parameter into the spreadsheet to filter the data returned by a report function after a pull action. When this function is linked to a hyperlink, the user can simply click on the hyperlink to display a list of valid parameters and insert one or more into the spreadsheet.

### [jFocus](/wFunctions/jFocus.html)

The jFocus function will move the cursor and select a targeted range after a freeze panes action using Interject's Freeze/UnFreeze Panes action. The [jFreezePanes](/wFunctions/jFreezePanes.html) function must be set up for this to trigger. The Freeze/UnFreeze Panes action can be found in [Quick Tools](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#quick-tools) on the Interject Ribbon Menu.

### [jFreezePanes](/wFunctions/jFreezePanes.html)

The jFreezePanes function freezes a designated pane so the user can scroll through data and still keep the frozen pane in view. The function also hides a designated range of the report, typically the configuration section of an Interject report. This provides the user with a more user-friendly simplified viewing experience.

### [jCombine](/wFunctions/jCombine.html)

The jCombine function concatenates a range or multiple ranges of cells into a single string using a designated delimiter. Blank cells are skipped.

### [jCombineIf](/wFunctions/jCombineIf.html)

The jCombineIF function concatenates a range or multiple ranges of cells into a single string using a designated delimiter if a certain condition is met. Blank cells are skipped.

### [jDataPortal](/wFunctions/jDataPortal.html)

The jDataPortal function establishes a connection to an Interject Data Portal that will be used as the data source for the function it is embedded in. Data sets accessed utilizing the jDataPortal are stored in memory. This allows the data set to be accessed later without having to query the data again via the Data Portal.

### [jColumnDef](/wFunctions/jColumnDef.html)

The jColumnDef function defines a column based on one or more parameters. Each parameter represents a segment. The segments can be set to filter the data that this column represents. Typically this function is used with a Data Pull function for a financial report.

### [jRangeTag](/wFunctions/jRangeTag.html)

The jRangeTag function simply tags a designated range with a name. This is used to support certain automated processes unique to Interject functions, for example report distribution.

### [jWorkbookProperty](/wFunctions/jWorkbookProperty.html)

The jWorkbookProperty function extracts information from the properties of the workbook.

### [jSetting](/wFunctions/jSetting.html)

The jSetting function is a simple way to create a JSON Tag/Value pair that can be used internally by the Interject system.

### [Pair](/wFunctions/Pair.html)

The Pair function transfers values from one cell to another. It is typically used in conjunction with the [PairGroup](/wFunctions/PairGroup.html) function. Values are transferred upon a designated Interject event (e.g. a drill or as defined in the function it is embedded in). It is best practice to use the PairGroup function even when only entering one Pair.

### [PairGroup](/wFunctions/PairGroup.html)

The PairGroup function will active all [Pair()](/wFunctions/Pair.html) functions defined within. It is best practice to use the PairGroup function even when only entering one Pair.

### [Param](/wFunctions/Param.html)

The Param function transfers values as parameters to the Data Portal. The values must match the order of the parameters in the data source (The order can be verified using the [Validation Report](/wTroubleshoot/Reports.html#validation-report-for-interject-events) ).

