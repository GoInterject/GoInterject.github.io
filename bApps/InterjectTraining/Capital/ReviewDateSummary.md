---
title: Capital Change Query - Review Date Summary
filename: "ReviewDateSummary.md"
layout: custom
keywords: [Training, Capital, Capital Change Query, Review Date]
headings: ["Overview", "Capital and the Control Center"]
links: ["/bApps/InterjectTraining/Budget/ControlCenter.html", "/bApps/InterjectTraining/Budget/ControlCenter.html"]
image_dir: "WCNTraining/Capital"
images: [
	{file: "Capital/ReviewDateSummary_FullView", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Capital/ReviewDateSummary_BuildingsDetail", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Capital/ControlCenter_SimpleExample", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}
	]
description: Pull in Capital amounts grouped by Asset group into the Review Date buckets.
---

## Overview

**Purpose**:  Pull in Capital amounts grouped by Asset group into the Review Date buckets.

**Filter Options**:

* **Budget Year** - *Optional*. Blank defaults to next year. Needs to be in YYYY format
* **District** - *Optional*. Blank gives the default view of all districts you have rights to. Works with individual districts, district ranges, and groupings
* **Currency** - *Optional*. Blank defaults to your home district currency. Otherwise options are USD or CAD

![](/images/WCNTraining/Capital/ReviewDateSummary_FullView.png)

## Capital and the Control Center

Capital gets synced to Interject according to the Review Date buckets defined in the [Control Center](/bApps/InterjectTraining/Budget/ControlCenter.html), as with Budget.

The screenshot above shows the Review Dates assigned to District 2041 and the Capital amounts in each bucket. This means that for the *Buildings* Asset, a total of **125,000** Capital changes have been saved before **07/01/2019 5:00 PM** (the *Corp Review Thru* date).

![](/images/WCNTraining/Capital/ReviewDateSummary_BuildingsDetail.png)

The screenshot below shows the Review Dates assigned to 2041 in the [Control Center](/bApps/InterjectTraining/Budget/ControlCenter.html). If the dates were to change here, it would also alter how the amounts get pulled into the *Review Date Summary* tab.

![](/images/WCNTraining/Capital/ControlCenter_SimpleExample.png)