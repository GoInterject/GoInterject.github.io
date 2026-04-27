---
title: "Develop: jFilter and jWhere"
filename: "L-Dev-jFilter-jWhere.md"
layout: custom
keywords: [jFilter, jWhere, sql, helper, function, develop, filter, where clause]
headings: ["Overview", "Understanding jFilter and jWhere", "Basic Filter Syntax", "Comparison Operators", "Single Filter Examples", "Multiple Filters", "Dynamic Filters with Cell References", "Filter Operators Guide", "Common Filtering Scenarios", "Real-World GL Filtering Examples"]
links: ["/wFunctions/jFilter.html", "/wFunctions/jWhere.html", "/wDeveloper/L-Dev-jDataSource.html", "/wDeveloper/L-Dev-SQL-in-Excel.html"]
image_dir: "L-Dev-SQL-in-Excel"
images: [
	{file: "04-Filtered-Formula", type: "png", site: "Excel", cat: "General Ledger", sub: "Filter Formula", report: "", ribbon: "", config: ""}, 
	{file: "05-Filtered-Results", type: "png", site: "Excel", cat: "General Ledger", sub: "Filter Results", report: "", ribbon: "", config: ""}, 
	{file: "06-Filtered2-Parameters", type: "png", site: "Excel", cat: "General Ledger", sub: "Dynamic Filter", report: "", ribbon: "", config: ""}
	]
description: Learn how to use jFilter and jWhere to filter data based on conditions.
---
* * *

## Overview

jFilter and jWhere work together to restrict data to specific rows based on conditions. jWhere defines the criteria, and jFilter applies it to your data source. This combination provides a simple, intuitive way to filter without writing complex SQL queries.

## Understanding jFilter and jWhere

### How They Work Together

**jWhere** defines what to filter:
```Excel
jWhere("Country", "USA", "=")
```
"Find rows where the Country column equals USA"

**jFilter** applies the filter:
```Excel
=jFilter(F1, jWhere("Country", "USA", "="))
```
"Filter the data using this condition"

### When to Use jFilter

You should use jFilter when:

* Filtering by a single criterion or a few simple criteria
* You need quick, readable formulas
* Your filter values come from cells the user controls
* You want to avoid writing SQL

If you need complex conditions with multiple AND/OR combinations, consider using [jQuery](/wDeveloper/L-Dev-jQuery.html) instead.

## Basic Filter Syntax

### Single Filter

```Excel
=jFilter(DataSource, jWhere(Column, Value, Operator))
```

**Example:**

```Excel
=jFilter(F1, jWhere("Country", "USA", "="))
```

Returns all customers where Country equals USA.

### Multiple Filters (AND)

Combine multiple jWhere conditions within Param():

```Excel
=jFilter(DataSource, AND(jWhere(...), jWhere(...), jWhere(...)))
```

**Example:**

```Excel
=jFilter(F1, AND(
    jWhere("Country", "USA", "="),
    jWhere("Status", "Active", "=")
))
```

Returns customers from USA AND with Status = Active.

## Comparison Operators

jWhere supports the following operators:

| Operator | Name | Example | Description |
|----------|------|---------|-------------|
| **=** or **==** | Equal | `jWhere("Country", "USA", "=")` | Exact match |
| **<>** or **!=** | Not Equal | `jWhere("Status", "Inactive", "<>")` | Does not match |
| **>** | Greater Than | `jWhere("Amount", 1000, ">")` | Value is greater |
| **<** | Less Than | `jWhere("Amount", 100, "<")` | Value is less |
| **>=** | Greater or Equal | `jWhere("Amount", 1000, ">=")` | Value is greater or equal |
| **<=** | Less or Equal | `jWhere("Amount", 5000, "<=")` | Value is less or equal |
| **like** | Pattern Match | `jWhere("CompanyName", "A%", "like")` | Contains pattern |


## Single Filter Examples

### Example 1: Filter by Text Value

**Goal:** Show only customers from Germany

```Excel
=jFilter(F1, jWhere("Country", "Germany", "="))
```

**Result:** Returns all customer rows where Country = "Germany"

### Example 2: Filter by Number

**Goal:** Show only orders over $1,000

```Excel
=jFilter(F1, jWhere("Amount", 1000, ">"))
```

**Result:** Returns all orders with Amount greater than 1000

### Example 3: Filter by Date

**Goal:** Show orders from 2024 and later

```Excel
=jFilter(F1, jWhere("OrderDate", "2024-01-01", ">="))
```

**Result:** Returns orders where OrderDate is greater than or equal to 2024-01-01

### Example 4: Pattern Matching

**Goal:** Show companies starting with "Alfreds"

```Excel
=jFilter(F1, jWhere("CompanyName", "Alfreds%", "like"))
```

**Result:** Returns customers whose CompanyName starts with "Alfreds"

### Example 5: Check for Missing Values

**Goal:** Find customers with no email address

```Excel
=jFilter(F1, jWhere("Email", "", "="))
```

**Result:** Returns customers where Email is blank/NULL

## Multiple Filters

### Two Conditions (AND)

**Goal:** Find active USA customers

```Excel
=jFilter(F1, AND(
    jWhere("Country", "USA", "="),
    jWhere("Status", "Active", "=")
))
```

**Result:** Returns customers where BOTH conditions are true

### Three or More Conditions

```Excel
=jFilter(F1, AND(
    jWhere("OrderDate", "2024-01-01", ">="),
    jWhere("Amount", 500, ">"),
    jWhere("Status", "Completed", "=")
))
```

**Result:** Returns orders from 2024, over $500, that are completed

## Dynamic Filters with Cell References

Instead of hard-coding values, reference cells so users can change filters dynamically.

### Single Dynamic Filter

**Setup:**
- Cell C5 contains: USA
- Cell C6 contains: Active

**Formula:**

```Excel
=jFilter(F1, jWhere("Country", C5, "="))
```

**How it Works:**
1. User enters "Germany" in C5
2. Formula automatically filters to Germany customers
3. When user changes C5 to "France", results update instantly

### Multiple Dynamic Filters

```Excel
=jFilter(F1, AND(
    jWhere("Country", C5, "="),
    jWhere("Status", C6, "=")
))
```

**Setup:**
- C5 = "USA" (country dropdown)
- C6 = "Active" (status dropdown)


### Numeric Dynamic Filters

```Excel
=jFilter(F1, jWhere("Amount", C5, ">"))
```

**Setup:**
- C5 = 1000 (user enters minimum order amount)

Returns orders greater than the amount entered in C5.

## Filter Operators Guide

### Equals (=)

Used for exact matches:

```Excel
jWhere("Status", "Active", "=")
jWhere("Region", "North", "=")
```

### Not Equal (<> or !=)

Exclude specific values:

```Excel
jWhere("Status", "Inactive", "<>")
jWhere("Country", "USA", "!=")
```

### Greater Than (>)

Numeric comparisons:

```Excel
jWhere("Amount", 1000, ">")
jWhere("Quantity", 5, ">")
```

### Less Than (<)

Numeric comparisons:

```Excel
jWhere("Days", 30, "<")
```

### Greater or Equal (>=)

Includes boundary:

```Excel
jWhere("Age", 18, ">=")
```

### Less or Equal (<=)

Includes boundary:

```Excel
jWhere("TotalAmount", 50000, "<=")
```

### LIKE (Pattern Matching)

Use % for wildcards:

```Excel
-- Starts with "A"
jWhere("CompanyName", "A%", "like")

-- Ends with "Ltd"
jWhere("CompanyName", "%Ltd", "like")

-- Contains "tech"
jWhere("CompanyName", "%tech%", "like")
```

## Common Filtering Scenarios

### Scenario 1: Geographic Filter

**Goal:** Let users filter customers by country

**Setup:**

Cell A1: "Select Country:"
Cell C1: Dropdown with countries (using data validation)

**Formula (in A3):**

```Excel
=jFilter(F1, jWhere("Country", C1, "="))
```

**Result:** Displays customers from selected country. Users can change C1 and click pull using a ReportRange function to see different countries instantly.

### Scenario 2: Date Range Filter

**Goal:** Show orders within a date range

**Setup:**

Cell C2: Start date
Cell C3: End date

**Approach:** Use jQuery for better date range handling:

```Excel
=jQuery(F1, "SELECT * FROM @ WHERE OrderDate >= '" & C2 & "' AND OrderDate <= '" & C3 & "'")
```

### Scenario 3: Numeric Range Filter

**Goal:** Find products in a price range

**Setup:**

Cell C4: Minimum price
Cell C5: Maximum price

**Formula:**

```Excel
=jQuery(F1, "SELECT * FROM @ WHERE Price >= " & C4 & " AND Price <= " & C5)
```

### Scenario 4: Status Filter

**Goal:** Show only active orders

```Excel
=jFilter(F1, jWhere("Status", "Active", "="))
```

### Scenario 5: exclude Specific Values

**Goal:** Show customers except those from a specific country

```Excel
=jFilter(F1, jWhere("Country", "UK", "<>"))
```

### Scenario 6: Multiple Criteria Dashboard

**Goal:** Sales dashboard filtering by region, year, and status

**Setup in Cells:**
- C10: Region (dropdown)
- C11: Year (dropdown)
- C12: Status (dropdown)

**Formula:**

```Excel
=jFilter(F1, AND(
    jWhere("Region", C10, "="),
    jWhere("Year", C11, "="),
    jWhere("Status", C12, "=")
))
```
## Best Practices

1. **Use Meaningful Cell Labels** - Makes your filters self-documenting
2. **Use Data Validation** - Put dropdowns in filter cells for consistency
3. **Order Filter Results** - Add sorting for better readability
4. **Test Edge Cases** - Try filters with blank cells, special characters, etc.
5. **Use Dynamic Filters** - Cell references are better than hard-coded values
6. **For Complex Logic** - Use jQuery for multiple AND/OR combinations

## Combining jFilter with Other Functions

### Filter + Sort

Use jQuery for sorting:

```Excel
=jQuery(F1, "SELECT * FROM @ WHERE Country = 'USA' ORDER BY CompanyName")
```

### Filter + Count

Count filtered results:

```Excel
=COUNTA(jFilter(F1, jWhere("Country", "USA", "=")))
```

### Filter + Sum (Use jAggregate)

```Excel
=jAggregate(jFilter(F1, jWhere("Status", "Completed", "=")), "SUM", "Amount", "")
```

## Real-World GL Filtering Examples

The [LocalReportingExamples.xlsx](/download/SQL%20in%20Excel%20Examples/LocalReportingExamples.xlsx) file demonstrates practical filtering of General Ledger data. Here's how it works in the "Filtered" and "Filtered2" sheets:

### Example 1: Filter by Description (Like Pattern)

In the "Filtered" sheet, GL transactions are filtered to show only with Year as 2002-01 and description contains the text "Other":

```Excel
=jFilter(GLData!B3, AND(jWhere("Year Mth", "2002-01"), jWhere("Description", "%Other%", "LIKE")))
```

**Screenshot 1: Filtered Description Formula**

![](/images/L-Dev-SQL-in-Excel/04-Filtered-Formula.png)

**Result:** Shows only transactions with Year as 2002-01 and description contains the text "Other":

**Screenshot 2: Filtered Results Display**

![](/images/L-Dev-SQL-in-Excel/05-Filtered-Results.png)

### Example 2: Parameter-Driven Dynamic Filter

In the "Filtered2" sheet, the filter uses cell parameters to allow user selection:

**Setup:**
- Cell F5: User selects which Account to filter
- Cell F6: User selects which district to filter

**Formula:**

```Excel
=jFilter(GLData!B3, AND(jWhere("Account", F5, E5), jWhere("Dist", F6, E6)))
```

**Screenshot 3: Dynamic Filter with Parameters**

![](/images/L-Dev-SQL-in-Excel/06-Filtered2-Parameters.png)

**How It Works:**
1. When user changes F5 (Account), the filter updates
2. When user changes F6 (District), the filter updates  
3. Both conditions apply (AND logic)
4. Results display only matching GL transactions

### Key Insights from GL Example

- **Pattern Matching:** "Revenue*" uses LIKE to find descriptions starting with "Revenue"
- **Dynamic Parameters:** Cell-based filters allow users to explore data interactively
- **Multiple Filters:** Combining multiple jWhere clauses creates more specific reports
- **Performance:** Filtering cached GL data is instantaneous, even with thousands of rows

## Next Steps

Explore advanced techniques:

* [Learn jQuery for complex queries](/wDeveloper/L-Dev-jQuery.html)
* [Use jJoin to combine data sources](/wDeveloper/L-Dev-jJoin.html)
* [Aggregate filtered data with jAggregate](/wDeveloper/L-Dev-jGroup-jAggregate.html)
* [Return to SQL in Excel overview](/wDeveloper/L-Dev-SQL-in-Excel.html)
