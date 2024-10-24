---
title: test
headings: []
links: ["/wDeveloper/L-Dev-EditingDataSave", "#setting-up-the-data-connection", "/wDeveloper/L-Dev-CustomerAging.html#setting-up-the-data-connection", "https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/downloading-sample-databases", "https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/downloading-sample-databases", "https://docs.gointerject.com/wLabs/LabSetup.html#step-1-setting-up-the-database"]
---

## Overview

text ![](/images/L-Dev-InsertDeleteDataSave/AddIsDeletedToPullSP.png) text
text /wDeveloper/L-Dev-EditingDataSave.html.
text
[text](#setting-up-the-data-connection) text
terx[text](/wDeveloper/L-Dev-CustomerAging.html#setting-up-the-data-connection). text
text [text](https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/downloading-sample-databases).
<blockquote class=highlight_note>
<b>Note:</b> text <a href="https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/downloading-sample-databases">Northwind Database</a>. text <a href="https://docs.gointerject.com/wLabs/LabSetup.html#step-1-setting-up-the-database">here</a>.
</blockquote>

```sql
CREATE OR ALTER PROC [dbo].[NorthwindInsertDeleteDataSaveSP]

	-- System Params not in formula
	@Interject_RequestContext nvarchar(max)
	,@TestMode bit = 0 -- used only for testing the stored procedure directly. It will show more results when set to 1.
```
