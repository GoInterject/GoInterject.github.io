---
title: Diagnostics - Clear Data Cell Cache
filename: "Diagnostics-ClearDataCellCache.md"
layout: custom
keywords: [local, data source, cache, clear]
headings: ["Overview", "Caches"]
links: []
image_dir: "DiagnosticsClearDataCellCache"
images: [
	{file: "ClearDataCellCache", type: "png", site: "Addin", cat: "Diagnostics", sub: "Clear Data Cell Cache", report: "", ribbon: "", config: ""},
	{file: "LastPulledValues", type: "png", site: "Addin", cat: "Report", sub: "Interject_LastPulledValues", report: "", ribbon: "", config: ""},
	{file: "AccelerateDataCells", type: "png", site: "Addin", cat: "Pull Data", sub: "Accelerate Data Cells by Using Cache", report: "", ribbon: "", config: ""},
	{file: "DataCellsCleared", type: "png", site: "Addin", cat: "Diagnostics", sub: "Clear Data Cell Cache", report: "", ribbon: "", config: ""}
]
description: The "Clear Data Cell Cache" command in our Diagnostics form is essential for maintaining the accuracy and freshness of data in your reports. Data cells are individual cells in an Excel report that retrieve data directly from a source.
---
* * *

## Overview

The "Clear Data Cell Cache" command in our Diagnostics form is essential for maintaining the accuracy and freshness of data in your reports. Data cells are individual cells in an Excel report that retrieve data directly from a source. 

![](/images/DiagnosticsClearDataCellCache/ClearDataCellCache.png)
<br>

### Caches

There are two types of caches involved: a local cache stored in a hidden tab called "Interject_LastPulledValues" within the report, and another cache associated with the data source.

![](/images/DiagnosticsClearDataCellCache/LastPulledValues.png)
<br>

When a report is opened, the local cache is used to load initial values quickly. The "Accelerate Data Cells" command leverages the data source cache to speed up data retrieval. If "Accelerate Data Cells" is unchecked, data is pulled directly from the data source, bypassing the cache.

![](/images/DiagnosticsClearDataCellCache/AccelerateDataCells.png)
<br>

The "Clear Data Cell Cache" command clears the cache stored at the data source. This is particularly useful after changes have been made to the data source, ensuring that the most up-to-date data is pulled into the Excel report. By using this command, you can ensure that your reports reflect the latest data without any stale or outdated information from the cache.

![](/images/DiagnosticsClearDataCellCache/DataCellsCleared.png)
<br>
