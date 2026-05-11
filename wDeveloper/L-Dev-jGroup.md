---
title: "Develop: jGroup"
filename: "L-Dev-jGroup.md"
layout: custom
keywords: [jGroup, sql, helper, function, develop, group]
headings: ["Overview", "Basic Syntax", "Core Examples", "Grouping and Filtering", "Real-World GL Grouping Examples", "Best Practices", "Troubleshooting"]
links: ["/wFunctions/jGroup.html", "/wDeveloper/L-Dev-jDataSource.html", "/wDeveloper/L-Dev-SQL-in-Excel.html"]
image_dir: "L-Dev-SQL-in-Excel"
images: [
	{file: "13-Aggregate-Formula", type: "png", site: "Excel", cat: "General Ledger", sub: "Group Formula", report: "", ribbon: "", config: ""},
	{file: "14-RevByType-Results", type: "png", site: "Excel", cat: "General Ledger", sub: "Revenue by Type", report: "", ribbon: "", config: ""},
	{file: "15-PL-Dashboard", type: "png", site: "Excel", cat: "General Ledger", sub: "Financial Dashboard", report: "", ribbon: "", config: ""}
	]
description: Learn how to use jGroup to organize and summarize data into readable report structures.
---
* * *

## Overview - What is jGroup?


jGroup is a powerful feature that **transforms raw transactional data into grouped, aggregated reports** with pivoted columns. Think of it as creating a custom pivot table directly in your Excel sheet.

### What It Does

Imagine you have thousands of sales records with dates, amounts, and product categories. jGroup lets you:
- **Group** data by specific dimensions (e.g., Product Category)
- **Sum** amounts for each group (e.g., Total Sales)
- **Pivot** the data into time periods or other breakdowns (e.g., Jan, Feb, Mar columns)
- **Display** it all organized in your Excel sheet

### When Should You Use jGroup?

✅ **Use jGroup when you need to:**
- Create pivot tables from raw data automatically
- Group transactions by customer, product etc
- Show multiple time periods (Jan, Feb, Mar) as columns
- Combine multiple grouping dimensions


## Basic Syntax

```Excel
=jGroup(DataSource, ColumnDefs, GroupingColumn, GroupingType)
```

| Parameter | Description | Example |
|-----------|-------------|---------|
| **DataSource** | Source table or source reference | `"JE_Data!A2:K793,JE_Data!A1:K1"` or  `"F12"` |
| **ColumnDefs** | Output column definitions for grouped output | `2:2` |
| **GroupingColumn** | Column name used to aggregate and calculate the SUM | `"Amount"` |
| **GroupingType** | Grouping mode, now only supports cube type | `"Cube"` |

# jGroup Rules and Constraints

## 1. Required Data Source Columns

The datasource finally resolved by **jGroup** must contain one or more of the following columns (exact match required, in order for functionality to work):


- Source  
- Period  
- Year  
- Version  
- Segment1  
- Segment2  
- Segment3  
- Segment4  
- Segment5  
- Segment6  
- Segment7  
- Segment8  
- BalanceType  

---

## 2. Grouping Column Rules

The grouping column for **jGroup** is derived from the `ColumnDefs` parameter.

- Only the following columns are used for grouping:
  - Segment1 to Segment8

### Important Behavior

If `ColumnDefs` contains values such as:
- Product
- Amount
- ProductDescription
- Any non-Segment fields

👉 These will be ignored for grouping purposes.

---

## 3. Aggregation Rules

- Only **SUM** aggregation is supported.
- Aggregation conditions are derived from `jColumnDef`.
- Aggregation filters are allied only to 11 sgement columns (`Period`, `Year`, `Version`, `Segment1`, `Segment2`, `Segment3`, `Segment4`, `Segment5`, `Segment6`, `Segment7`, `Segment8`)
- `BalanceType` and `Source` are never included in aggregation filter conditions.

### Example

If `jColumnDef` is:

```json
{
  "P": "1",
  "Y": "2023",
  "B": "MTD"
}
```

Then:

- `jColumnDef_1` will:
  - SUM the `AMOUNT` (which will be resolved from `GroupingColumn` parameter of `jGroup`) column
  - Apply filters:
    - Period = 1
    - Year = 2023
  - Grouping is applied using Segment1–Segment8

  - If the resolved datasource doesn't have the Segment Columns in jColumnDef then it will not be added to the filter conditions. Also `BalanceType` and `Source` will be excluded from filter conditions even if they are preset in the datasource.

  If `jColumnDef` is:

```json
{
  "P": "1",
  "Y": "2023",
  "B": "MTD",
  "S1":"7001"
}
```

Then:

- `jColumnDef_1` will:
  - SUM the `AMOUNT` column
  - Apply filters:
    - Period = 1
    - Year = 2023
    - Segment1 = 7001
  - Grouping is applied using Segment1–Segment8


---


## Real-World GL Grouping Examples

The [jGroupSample.xlsx](/download/SQL%20in%20Excel%20Examples/jGroupSample.xlsx) file demonstrates practical grouped reporting examples.

## Next Steps

Explore more:

* [Combine grouped data with jJoin](/wDeveloper/L-Dev-jJoin.html)
* [Filter source rows with jFilter and jWhere](/wDeveloper/L-Dev-jFilter-jWhere.html)
* [Create dataset slices with jQuery](/wDeveloper/L-Dev-jQuery.html)
* [Return to SQL in Excel overview](/wDeveloper/L-Dev-SQL-in-Excel.html)
