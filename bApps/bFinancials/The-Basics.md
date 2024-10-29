---
title: Train
filename: "The-Basics.md"
layout: custom
keywords: [Report, Epicor, Accounts]
headings: ["Interject for Financials Quick Reference", "Important Interject Hotkeys", "Important Formulas", "Important Actions on the Interject Ribbon Menu", "The Basics of Working with Interject for Financials", "Using the Report Library", "Pull Data", "Drilling Between Reports"]
links: []
image_dir: "Interject-Financials"
images: [
	{file: "Pull", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "InterjectFinancialsRbnMnu", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}
	]
description: A quick guide to get users started navigating Interject for Financials Epicor Enterprise.
---

## Interject for Financials Quick Reference

### Important Interject Hotkeys 

> To Know
>
> <span class="hotkey">Ctrl+Shift+J:</span> Pulls data into your report after selecting parameters from the dropdowns in the parameter section.
>
> <span class="hotkey">Ctrl+Shift+K:</span> Drills through a selected value to a more detailed report \(drills are available only in predefined cells).
>
> <span class="hotkey">Ctrl+Shift+U:</span> Saves data or configurations back to a database.
>
> <span class="hotkey">Ctrl+Shift+L:</span> Opens the report library, where you can access your organization's published reports.
>

### Important Formulas

> To Know
>
> **=JCombineSmart\(\):** Concatenates, orders, and removes duplicates of selected range to enter validation definitions or detail row definitions when building financials reports.
>
> **=EDate\(\):** Use to set the period of interest as an absolute reference to the fiscal period filter when building financial reports. Pass ",-\[chosen cell\]" when building subsequent columns from the period of interest.
>
>

### Important Actions on the Interject Ribbon Menu 

>To Know
>
> **1:** Use to access and share report in your organization.
>
> **2:** Use to pull data into the report after selecting parameters from the dropdowns in the parameter fields. You may also use the <img class="logo" style="height: 22px; width:84px; vertical-align: middle; border:none; display:inline; " src="/images/Interject-Financials/Pull.png"> button in the report parameter area.
>
> **3:** Use to save data or configurations back to a database.
>
> **4:** Use to Drill through data into more detailed reports. You can go back one drill by pressing the **Return From Drill** button to the right of the drill button.
>
> ![Open report link button](/images/Interject-Financials/InterjectFinancialsRbnMnu.png){: .center-image }
>
