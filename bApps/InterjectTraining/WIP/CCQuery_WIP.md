---
title: Capital Change Query - CC Query Tab
filename: "CCQuery_WIP.md"
layout: custom
keywords: [Training, Capital, Capital Change Query]
headings: ["Overview", "Summary Level Drop-Down"]
links: []
image_dir: "WCNTraining"
images: [
	{file: "Capital/CCQuery_FullView", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Capital/CCQuery_SummaryByDay", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Capital/CCQuery_SummaryByChange", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}
	]
description: Pull in change history details for Capital.
---

## Overview

**Purpose**:  Pull in change history details for Capital.

**Filter Options**:

* **Budget Year** - *Required*. Needs to be in YYYY format
* **District** - *Optional*. Blank gives the default view of all districts you have rights to. Works with individual districts, district ranges, and groupings
* **PO #** - *Optional*. Blank pulls all POs. The format must be XXXX-X
* **Summary Level** - *Required*. Drop-down filter is restricted to show changes *By Day* or *By Change*
**From Date of Change** - *Optional* - Blank defaults to beginning of time. Format needs to be *MM/DD/YYYY HH:MM*
**To Date of Change** - *Optional* - Blank defaults to today. Format needs to be *MM/DD/YYYY HH:MM*
**Sort By** - *Required*. Drop-down filter is restricted to order results by *Change Date* or *PO #*

![](/images/WCNTraining/Capital/CCQuery_FullView.png)

## Summary Level Drop-Down

The *Summary Level* drop-down input parameter shows the Capital changes, grouped by either the day or the ChangeIDs. 

If a PO changes multiple times in one day, the *By Day* option will show the final PO change for the day. If *By Change* is selected, it would show all of the changes made on that day.

*Summary Level By Day*
![](/images/WCNTraining/Capital/CCQuery_SummaryByDay.png)

*Summary Level By Change*
![](/images/WCNTraining/Capital/CCQuery_SummaryByChange.png)
