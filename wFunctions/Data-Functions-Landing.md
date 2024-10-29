---
title: Data Pull Functions
filename: "Data-Functions-Landing.md"
layout: custom
keywords: [data pull functions, range, fixed, variable, lookup]
headings: ["Overview", "ReportRange", "ReportFixed", "ReportVariable", "ReportLookup"]
links: ["/wFunctions/ReportRange.html", "/wFunctions/ReportFixed.html", "/wFunctions/ReportVariable.html", "/wFunctions/ReportLookup.html"]
image_dir: ""
images: []
description: Data Pull Functions are focused on getting specific data to the report in the right way and placed inside the spreadsheet. There are a variety of functions and options therein to give flexibility in what data is displayed.
---
* * *

## Overview

Data Pull Functions are focused on getting specific data to the report in the right way and placed inside the spreadsheet. There are a variety of functions and options therein to give flexibility in what data is displayed.

### [ReportRange](/wFunctions/ReportRange.html)

The ReportRange function pulls data from a data source and inserts it into a single range within a spreadsheet.

### [ReportFixed](/wFunctions/ReportFixed.html)

The ReportFixed function pulls data from a data source and inserts it into a spreadsheet. It is similar to the ReportRange function but with the addition of receiving row names as input in addition to column names. Only data that is mapped to both these row and column names from the data source will be inserted.

### [ReportVariable](/wFunctions/ReportVariable.html)

The ReportVariable function pulls data from a data source and inserts it into a spreadsheet. It is similar to the ReportFixed function because it takes row names as input in addition to column names. Only data that is mapped to both these row and column names from the data source will be inserted. This function differs from the ReportFixed function in that it will group the data based on the values defined in the RowDefRange argument. The grouping feature allows the data to be collapsed and expanded by category.

### [ReportLookup](/wFunctions/ReportLookup.html)

The ReportLookup function pulls a single piece of data from a data source and inserts it into a single cell within a spreadsheet.
