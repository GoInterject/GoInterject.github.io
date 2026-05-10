---
title: "Develop: jJoin"
filename: "L-Dev-jJoin.md"
layout: custom
keywords: [jJoin, sql, helper, function, develop, join, combine, data sources]
headings: ["Overview", "Understanding jJoin", "Join Types Explained", "Basic jJoin Syntax", "INNER JOIN Examples", "LEFT JOIN Examples", "RIGHT JOIN Examples", "OUTER JOIN Examples", "Multi-Column Joins", "Real-World GL Join Examples"]
links: ["/wFunctions/jJoin.html", "/wDeveloper/L-Dev-jDataSource.html", "/wDeveloper/L-Dev-SQL-in-Excel.html"]
image_dir: "L-Dev-SQL-in-Excel"
images: [
	{file: "10-Join-District-Lookup", type: "png", site: "Excel", cat: "General Ledger", sub: "Lookup Table", report: "", ribbon: "", config: ""}, 
	{file: "11-Join-Formula", type: "png", site: "Excel", cat: "General Ledger", sub: "Join Formula", report: "", ribbon: "", config: ""}, 
	{file: "12-Join-Results", type: "png", site: "Excel", cat: "General Ledger", sub: "Join Results", report: "", ribbon: "", config: ""}
	]
description: Learn how to use jJoin to combine two jDataSource results based on a common column.
---
* * *

## Overview

The jJoin function combines two separate data sources based on a common column. This is powerful when you need to bring together related data from different places—like customers with their orders, products with their inventory levels, or employees with their departments.

## Understanding jJoin

### Why Join Data?

In database design, data is often separated to avoid duplication:

* **Customers Table** - Contains customer information
* **Orders Table** - Contains orders with customer IDs

To answer "What orders did customer ABC place?" you need to join these tables.

### When to Use jJoin

Use jJoin when you:

* Have two data sources with a common column (like CustomerID)
* Need to combine them in a spreadsheet
* Want to avoid complex formulas or stored procedures
* Need one of the four SQL join types

### The Join Types

| Join Type | Returns | Use Case |
|-----------|---------|----------|
| **INNER** | Matching rows only | Customers with orders |
| **LEFT** | All from first, matching from second | All customers, with orders if they have any |


Supported joins are "INNER", "LEFT", "LEFT OUTER", "CROSS", "NATURAL INNER", "NATURAL LEFT", "NATURAL LEFT OUTER", "NATURAL CROSS"

## Join Types Explained

### INNER JOIN

Returns only rows where the join column matches in both sources.

**Venn Diagram Concept:**
```
    DS1         DS2
   ------      ------
   | A |   \  /| A |
   | B | ---\/---| B |
   | C |  INNER | D |
         Result: A, B
```

**Example:** Customers who have placed orders
- Customers table: ALFKI, ANATR, ANTON
- Orders table: ALFKI, ALFKI, ANATR
- Result: ALFKI, ANATR (only customers with orders)

### LEFT JOIN

Returns all rows from the first (left) source, plus matching rows from the second.

**Venn Diagram Concept:**
```
    DS1         DS2
   ------      ------
   | A |  \    /| A |
   | B |   \--/--| B |
   | C |  LEFT   | D |
         Result: A, B, C (all from DS1)
```

**Example:** All customers, showing their orders if available
- Returns all customers, even those without orders (NULL for order fields)



## Basic jJoin Syntax

```Excel
=jJoin(FirstDataSource, SecondDataSource, JoinType, FirstJoinColumn, SecondJoinColumn)
```

| Parameter | Description | Example |
|-----------|-------------|---------|
| **FirstDataSource** | First tag or range | "Customers" |
| **SecondDataSource** | Second tag or range | "Orders" |
| **JoinType** | "INNER", "LEFT" | "INNER" |
| **FirstJoinColumn** | Column name in first source | "CustomerID" |
| **SecondJoinColumn** | Column name in second source | "CustomerID" |

### Basic Example

```Excel
=jJoin(F1, F2, "INNER", "CustomerID", "CustomerID")
```

This joins:
- The "Customers" data source
- With the "Orders" data source
- Using an INNER JOIN
- Matching on CustomerID from Customers
- With CustomerID from Orders

## INNER JOIN Examples

### Example 1: Customers with Orders

**Goal:** Show which customers have placed orders

**Formula:**

```Excel
=jJoin(F1, F2, "INNER", "CustomerID", "CustomerID")
```

**Result:** Only customers who appear in the Orders table (those with orders)

### Example 2: Sales by Product

**Goal:** Show sales for each product

**Formula:**

```Excel
=jJoin(F1, F2, "INNER", "ProductID", "ProductID")
```

**Result:** Products with their sales (products not sold are excluded)

### Example 3: Employees in Departments

**Goal:** Show department for each employee

**Formula:**

```Excel
=jJoin(F1, F2, "INNER", "DepartmentID", "DepartmentID")
```

**Result:** Each employee with their department information

## LEFT JOIN Examples

### Example 1: All Customers with Their Orders (If Any)

**Goal:** See all customers, with order information where available

**Formula:**

```Excel
=jJoin(F1, F2, "LEFT", "CustomerID", "CustomerID")
```

**Result:** 
- All customers appear in the result
- Customers with no orders show NULL in order columns
- Customers with multiple orders appear multiple times (once per order)

### Example 2: All Products with Sales Data

**Goal:** Show all products, even those that haven't sold

**Formula:**

```Excel
=jJoin(F1, F2, "LEFT", "ProductID", "ProductID")
```

**Result:**
- All products appear
- Products with no sales show NULL
- Useful for identifying slow-moving inventory

### Example 3: All Employees with Department (Fill Missing)

**Goal:** Show all employees, matching with departments where data exists

**Formula:**

```Excel
=jJoin(F1, F2, "LEFT", "DepartmentID", "DepartmentID")
```

## Real-World GL Join Examples

The [LocalReportingExamples.xlsx](/download/SQL%20in%20Excel%20Examples/LocalReportingExamples.xlsx) file demonstrates joining GL transaction data with a District lookup table. Here's how it's implemented in the "JoinDist" sheet:

### GL Data with District Lookup

**Setup:**
- **Source 1:** GL transactions with a "Dist" column (7001, 7002, etc.)
- **Source 2:** District lookup table with Dist code and Type (Landfill, Hauling, etc.)

**Screenshot 1: District Lookup Table**

![](/images/L-Dev-SQL-in-Excel/10-Join-District-Lookup.png)

### The jJoin Formula

```Excel
=jJoin(GLData!D14, GLData!D15, "INNER", "Dist", "Dist")
```

**Breaking it down:**
- **GLData!D14** - jDataSource of GL transactions (first source)
- **GLData!D15** - jDataSource of district lookup (second source)
- **"INNER"** - Only return GL transactions that have a matching district
- **"Dist", "Dist"** - Both sources have a "Dist" column to join on

**Screenshot 2: jJoin Formula**

![](/images/L-Dev-SQL-in-Excel/11-Join-Formula.png)

### The Result

Each GL transaction now includes the district type information from the lookup table, go and click the pull button and see the results

**Screenshot 3: Joined Results with District Details**

![](/images/L-Dev-SQL-in-Excel/12-Join-Results.png)

**Result columns:**
- Original GL columns (Date, Account, Amount, etc.)
- Plus: District Type (Landfill, Hauling, etc.)

### Why This Matters

Instead of seeing just "7001" or "7002" in your GL data, you now see the meaningful district name. This makes reports:
- More readable for end users
- Better for analysis and grouping
- Suitable for sending to executives

## Next Steps

Explore advanced techniques:

* [Group joined data with jGroup](/wDeveloper/L-Dev-jGroup.html)
* [Use jQuery for complex joins](/wDeveloper/L-Dev-jQuery.html)
* [Return to SQL in Excel overview](/wDeveloper/L-Dev-SQL-in-Excel.html)
