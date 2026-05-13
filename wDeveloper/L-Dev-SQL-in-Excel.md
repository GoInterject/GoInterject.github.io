---
title: "Develop: SQL in Excel"
filename: "L-Dev-SQL-in-Excel.md"
layout: custom
keywords: [SQL in Excel, jDataSource, jQuery, jFilter, jWhere, jJoin, jGroup, jAggregate, helper functions, develop, build]
headings: ["Overview", "SQL Helper Functions", "Getting Started"]
links: ["/wDeveloper/L-Dev-jDataSource.html", "/wDeveloper/L-Dev-jQuery.html", "/wDeveloper/L-Dev-jFilter-jWhere.html", "/wDeveloper/L-Dev-jJoin.html", "/wDeveloper/L-Dev-jGroup.html"]
image_dir: ""
images: []
description: Learn how to use Interject SQL helper functions to query, filter, and aggregate data directly in Excel without writing complex SQL or VBA.
---
* * *

## Overview

Interject provides a powerful set of SQL helper functions that allow you to perform complex data operations directly within Excel. These functions enable you to cache data from Data Portals or worksheet ranges and then manipulate that data using familiar SQL-like operations—all without writing complex SQL queries or VBA macros.

The SQL helper function suite is designed to make data transformation simple and intuitive for business users and developers alike. Whether you need to filter data, join datasets, aggregate values, or run custom queries, these functions provide the flexibility you need.

### Key Benefits

* **SQL-Like Syntax** - Use familiar SQL concepts like WHERE, JOIN, and GROUP BY
* **Combined with Excel** - Leverage the power of SQL alongside Excel's native functions and formatting
* **Reduced Complexity** - Avoid complex stored procedures for simple data transformations
* **Performance Optimization** - Minimize database calls by processing data in-memory

## SQL Helper Functions

The complete suite of SQL helper functions includes:

### [jDataSource()](/wDeveloper/L-Dev-jDataSource.html)

The foundation of all SQL helper functions. Caches data from a worksheet range or Data Portal into memory for use by other SQL helper functions.

**Example Use:**
- Cache customer data from a Data Portal
- Create datasource from a range from another worksheet


### [jQuery()](/wDeveloper/L-Dev-jQuery.html)

Runs a custom SQL query against a jDataSource. Use this when you need specific control over the data selection and projection.

**Example Use:**
- Filter and select specific columns from data source
- Create views of data without returning to the database

### [jFilter() & jWhere()](/wDeveloper/L-Dev-jFilter-jWhere.html)

Simple filtering functions that restrict rows based on conditions. jWhere defines the filter criteria while jFilter applies it to the data source.

**Example Use:**
- Filter customer data by country or region
- Apply multiple filter conditions
- Filter based on user selections or cell values

### [jJoin()](/wDeveloper/L-Dev-jJoin.html)

Combines two data sources based on a common column (INNER, LEFT etc).

**Example Use:**
- Join customers with their orders
- Combine product data with sales data
- Merge lookup tables with transaction data

### [jGroup()](/wDeveloper/L-Dev-jGroup.html)

Groups data by a column and aggregates values.

**Example Use:**
- Summarize sales by customer
- Calculate totals by product category
- Count transactions by region

## Getting Started

To help you understand how these functions work together, this section includes detailed examples for each function. Each example includes:

* Step-by-step instructions
* Real-world scenarios using the Northwind database and General Ledger data
* Excel screenshots showing the formula setup
* Explanation of the results

### Download the Example File

We provide a comprehensive Excel example file that demonstrates all SQL helper functions in action:

**File:** [LocalReportingExamples.xlsx](/download/SQL%20in%20Excel%20Examples/LocalReportingExamples.xlsx)

This file contains 11 sheets showing practical General Ledger reporting patterns:
- **GLData** - Master data source with 2,800+ GL transactions
- **Pull** - Basic jDataSource caching
- **Filtered** - Simple and parameter-driven jFilter examples
- **Aggregate** - jQuery aggregation and grouping
- **JoinDist** - jJoin with lookup tables
- **RevByType** - jGroup and jAggregate summaries

### Start with the [jDataSource](/wDeveloper/L-Dev-jDataSource.html) documentation to learn how to cache data, then explore the other functions to see how they work together.

### Prerequisites

To complete these examples, you should have:

* Access to Interject with a configured Data Portal
* Familiarity with the Northwind database (or your own data source)
* Basic understanding of SQL concepts (WHERE, JOIN, GROUP BY, etc.)
* Excel with the Interject add-in installed

### Recommended Learning Path

1. **Start with jDataSource** - Understand how to create data source
2. **Learn jFilter & jWhere** - Filter that data source  
3. **Explore jQuery** - Write custom queries
4. **Try jJoin** - Combine multiple data sources
5. **Master jGroup** - Summarize your results

Each function builds on the concepts from the previous ones, so we recommend following this order.
