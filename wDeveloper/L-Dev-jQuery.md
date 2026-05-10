---
title: "Develop: jQuery"
filename: "L-Dev-jQuery.md"
layout: custom
keywords: [jQuery, sql, helper, function, develop, query, sql query]
headings: ["Overview", "Understanding jQuery", "Basic jQuery Syntax", "Common SQL Query Patterns", "Filtering with WHERE", "Selecting Specific Columns", "Ordering Results", "Joining Data Sources", "Aggregating Data", "Real-World GL Query Examples"]
links: ["/wFunctions/jQuery.html", "/wDeveloper/L-Dev-jDataSource.html", "/wDeveloper/L-Dev-SQL-in-Excel.html"]
image_dir: "L-Dev-SQL-in-Excel"
images: [
	{file: "07-Aggregate-Query", type: "png", site: "Excel", cat: "General Ledger", sub: "Group Query", report: "", ribbon: "", config: ""}, 
	{file: "08-Aggregate-Results", type: "png", site: "Excel", cat: "General Ledger", sub: "Query Results", report: "", ribbon: "", config: ""}, 
	{file: "09-PL-Example-Trends", type: "png", site: "Excel", cat: "General Ledger", sub: "Trend Analysis", report: "", ribbon: "", config: ""}
	]
description: Learn how to use the jQuery function to run custom SQL queries against cached jDataSource data.
---
* * *

## Overview

The jQuery function gives you complete control over data retrieval from a cached jDataSource. Unlike jFilter which uses simple criteria, jQuery lets you write actual SQL SELECT statements to query your data with advanced filtering, joins, aggregations, and more.

## Understanding jQuery

### When to Use jQuery vs jFilter

| Scenario | Use |
|----------|-----|
| Simple equality filter (Country = "USA") | jFilter |
| Multiple conditions with AND/OR | jQuery |
| Complex WHERE clauses | jQuery |
| Specific column selection | jQuery |
| Sorting results | jQuery |
| Aggregations in query | jQuery |

### Basic Syntax

```Excel
=jQuery(DataSource, SQLQuery)
```

| Parameter | Description |
|-----------|-------------|
| **DataSource** | Range or tag of cached jDataSource |
| **SQLQuery** | SQL SELECT statement as text |

## Basic jQuery Syntax

### Simple SELECT All

To return all data from a cache:

```Excel
=jQuery(F1, "SELECT * FROM @")
```

### SELECT Specific Columns

To return only certain columns:

```Excel
=jQuery(F1, "SELECT CustomerID, CompanyName, Country FROM @")
```

## Common SQL Query Patterns

### Pattern 1: Simple Selection

**Query:** Get customer IDs and names

```Excel
=jQuery(F1, "SELECT CustomerID, CompanyName FROM @")
```

**Scenario:** Display a quick list of customers in a report

### Pattern 2: WHERE Filtering

**Query:** Get USA customers only

```Excel
=jQuery(F1, "SELECT * FROM @ WHERE Country = 'USA'")
```

**Scenario:** Filter to a specific region

**Query with Cell Reference:**

First, let's say cell C6 contains "USA"

```Excel
=jQuery(F1, "SELECT * FROM @ WHERE Country = '" & C6 & "'")
```

### Pattern 3: Multiple Conditions

**Query:** Get USA customers with names starting with 'A'

```Excel
=jQuery(F1, "SELECT CustomerID, CompanyName FROM @ WHERE Country = 'USA' AND CompanyName LIKE 'Al%'")
```

### Pattern 4: ORDER BY Sorting

**Query:** Get customers ordered by company name

```Excel
=jQuery(F1, "SELECT CustomerID, CompanyName, City FROM @ ORDER BY CompanyName")
```

**Query:** Order by multiple columns

```Excel
=jQuery(F1, "SELECT * FROM @ WHERE Country = 'USA' ORDER BY City, CompanyName")
```

### Pattern 5: DISTINCT Results

**Query:** Get unique countries

```Excel
=jQuery(F1, "SELECT DISTINCT Country FROM @ ORDER BY Country")
```

## Filtering with WHERE

### Comparison Operators

```Excel
-- Equal
WHERE Country = 'USA'

-- Not equal
WHERE Status <> 'Inactive'

-- Greater than
WHERE Amount > 1000

-- Less than or equal
WHERE OrderDate <= '2024-01-01'

-- LIKE (pattern matching)
WHERE CompanyName LIKE 'Alfreds%'
WHERE CompanyName LIKE '%Ltd%'
```

### Combining Conditions

**AND - All conditions must be true:**

```Excel
=jQuery(F1, "SELECT * FROM @ WHERE Country = 'USA' AND City = 'New York'")
```

**OR - At least one condition must be true:**

```Excel
=jQuery(F1, "SELECT * FROM @ WHERE Country = 'USA' OR Country = 'Canada'")
```

**Complex Combinations:**

```Excel
=jQuery(F1, "SELECT * FROM @ WHERE Year = 2024 AND (Status = 'Completed' OR Status = 'Pending') AND Amount > 500")
```

### IS NULL / IS NOT NULL

**Query:** Get customers with no contact email

```Excel
=jQuery(F1, "SELECT * FROM @ WHERE CustomerID IS NULL")
```

**Query:** Get customers with contact email

```Excel
=jQuery(F1, "SELECT * FROM @ WHERE CustomerID IS NOT NULL")
```

## Selecting Specific Columns

### Reduce Clutter

Instead of returning all columns:

```Excel
-- Returns all columns (verbose)
=jQuery(F1, "SELECT * FROM @")

-- Return only needed columns (clean)
=jQuery(f1, "SELECT OrderID, CustomerID, Amount, OrderDate FROM @")
```

### Column Aliases

Rename columns in the output:

```Excel
=jQuery(F1, "SELECT OrderID AS 'Order Number', CustomerID AS 'Customer', Amount AS 'Total' FROM @")
```

### Calculated Columns

Add calculated values:

```Excel
=jQuery(F1, "SELECT CustomerID, Amount, Amount * 0.1 AS TaxAmount FROM @")
```

## Ordering Results

### Single Column Sort

```Excel
-- Ascending (default)
=jQuery(F1, "SELECT * FROM @ ORDER BY CompanyName")

-- Descending
=jQuery(F1, "SELECT * FROM @ ORDER BY Amount DESC")
```

### Multiple Column Sort

```Excel
=jQuery(F1, "SELECT * FROM @ ORDER BY Country ASC, City ASC, CompanyName ASC")
```

## Joining Data Sources

To join multiple cached data sources, reference both in your SQL:


## Aggregating Data

While jGroup is typically used for aggregation, jQuery can perform simple aggregations:

### COUNT

```Excel
=jQuery(F1, "SELECT COUNT(*) AS TotalOrders FROM @")
```

### SUM

```Excel
=jQuery(F1, "SELECT SUM(Amount) AS TotalAmount FROM @ WHERE Country = 'USA'")
```

### GROUP BY

```Excel
=jQuery(F1, "SELECT Country, SUM(Amount) AS TotalAmount FROM @ GROUP BY Country")
```

## Practical Examples

### Example 1: Sales Dashboard

**Scenario:** Create a dashboard showing sales by country

**Step 1:** Sales data source formula in cell F1
```Excel
=jDataSource(B2:F250, B1:F1, , "SalesData")
```

**Step 2:** Query for USA sales
```Excel
=jQuery(F1, "SELECT OrderMonth, SUM(Amount) AS Sales FROM @ WHERE Country = 'USA' GROUP BY OrderMonth ORDER BY OrderMonth")
```

**Step 3:** Format results with conditional formatting

### Example 2: Active Customers Report

**Scenario:** List all active customers in a specific city

**Data contains:** CustomerID, CompanyName, City, Status, LastOrderDate

```Excel
=jQuery(f1, "SELECT CompanyName, LastOrderDate FROM @ WHERE Status = 'Active' AND City = '" & C5 & "' ORDER BY CompanyName")
```

Where C5 contains the city name selected by the user.

### Example 3: High-Value Orders

**Scenario:** Show orders totaling more than $5,000

```Excel
=jQuery(F1, "SELECT OrderID, CustomerID, CompanyName, OrderAmount FROM @ WHERE OrderAmount > 5000 ORDER BY OrderAmount DESC")
```

## Best Practices

1. **Use Meaningful Aliases** - Makes outputs clearer
2. **Always ORDER BY** - Results are more usable when sorted
3. **Start with Simple Queries** - Build complexity gradually
4. **Test in Steps** - Verify each part of complex queries
5. **Use Cell References** - Make queries dynamic with filters based on user input
6. **Limit Results** - When possible, filter to reduce output size
7. **Comment Your Formulas** - Use text beside complex queries explaining purpose

## Troubleshooting

### Common Issues

**Issue:** "Query Error" message
- **Solution:** Check SQL syntax and ensure column names match data source

**Issue:** No results returned
- **Solution:** Verify WHERE clause conditions are correct; test with SELECT *

**Issue:** Too much data returned
- **Solution:** Add WHERE clause to filter, or select specific columns only
## Real-World GL Query Examples

The [LocalReportingExamples.xlsx](/download/SQL%20in%20Excel%20Examples/LocalReportingExamples.xlsx) file demonstrates how jQuery can aggregate GL data. Here are the patterns used in the "Aggregate" sheet:

### Example 1: GROUP BY with Aggregation

In the "Aggregate" sheet, GL transactions are grouped and summed by Description and District:

```Excel
=jQuery(B5, "SELECT Description, Dist, SUM(Amount) AS Total FROM @1 GROUP BY Description, Dist")
```

**Screenshot 1: Revenue Summary Query Formula**

![](/images/L-Dev-SQL-in-Excel/07-Aggregate-Query.png)

**Breaking it down:**
- **B5** - References the jDataSource formula cell
- **SELECT Description, Dist, SUM(Amount)** - Selects description, district, and sum
- **GROUP BY Description, Dist** - Groups results by both columns

Click on pull and see the filtered data

**Screenshot 2: Query Results Display**

![](/images/L-Dev-SQL-in-Excel/08-Aggregate-Results.png)

### Key Insights from GL Examples

- **GROUP BY** - Essential for creating summaries from detailed GL data
- **WHERE Clauses** - Filter before aggregating for performance
- **ORDER BY** - Makes results scannable and insightful
- **SUM() Function** - Combines like values for reporting
- **LIKE Operator** - Combines related descriptions (all "Revenue*" items together)
## Next Steps

Explore advanced techniques:

* [Learn jGroup for summary layouts](/wDeveloper/L-Dev-jGroup.html)
* [Use jJoin to combine multiple data sources](/wDeveloper/L-Dev-jJoin.html)
* [Return to SQL in Excel overview](/wDeveloper/L-Dev-SQL-in-Excel.html)
