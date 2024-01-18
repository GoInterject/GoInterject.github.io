---
title: Data Cell Functions
filename: "Data-Cell-Functions.md"
layout: custom
keywords: [data cell, functions]
headings: ["Overview", "jAcct", "jCell/jCellN", "jDesc"]
links: ["/wIndex/jAcct.html", "/wIndex/jCell.html", "/wIndex/jAcct.html", "/wIndex/jDesc.html"]
description: Data Cells are focused on a single formula which can be placed anywhere in the spreadsheet and can ask for any financial number or summary from it. Once this single formula approach is understood, there is no limit to the combinations that can be created.
---
* * *

## Overview

Data Cells are focused on a single formula which can be placed anywhere in the spreadsheet and can ask for any financial number or summary from it. Once this single formula approach is understood, there is no limit to the combinations that can be created. This is typically an easier method to start writing custom reports. However, given their flexibility the report run times can take more than just a few seconds to complete, sometimes up to 5 minutes. Larger reports, such as one with 70,000 formulas, can take up to 10 minutes to complete. Fortunately, users may continue working with a spreadsheet while waiting for Data Cell reports to finish calculating.

### [jAcct](/wIndex/jAcct.html)

A helper function that specifies filters for up to six segments of a Chart of Accounts.

### [jCell/jCellN](/wIndex/jCell.html)

jCell retrieves data based on the provided parameters. The first argument is typically a [jAcct()](/wIndex/jAcct.html) lookup when a company has more than one segment to filter. The retrieved data is always summarized into a single value. 

### [jDesc](/wIndex/jDesc.html)

This function is used to look up a context description based on a specific segment. 
