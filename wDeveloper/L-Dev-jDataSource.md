---
title: "Develop: jDataSource"
filename: "L-Dev-jDataSource.md"
layout: custom
keywords: [jDataSource, sql, helper, function, develop, cache, data source]
headings: ["Overview", "Understanding jDataSource", "Setting Up Your First jDataSource", "Caching Data from a Worksheet", "Caching Data from a Data Portal", "Tagging Your Data Cache", "Using Cached Data with Other Functions", "Real-World GL Example"]
links: ["/wFunctions/jDataSource.html", "/wDeveloper/L-Dev-jQuery.html", "/wDeveloper/L-Dev-jFilter-jWhere.html"]
image_dir: "L-Dev-SQL-in-Excel"
images: [
	{file: "01-GLData-Source", type: "png", site: "Excel", cat: "General Ledger", sub: "Data Setup", report: "", ribbon: "", config: ""}, 
	{file: "02-jDataSource-Formula", type: "png", site: "Excel", cat: "General Ledger", sub: "Formula", report: "", ribbon: "", config: ""}, 
	{file: "03-Cached-GL-Output", type: "png", site: "Excel", cat: "General Ledger", sub: "Result", report: "", ribbon: "", config: ""}
	]
description: Learn how to use the jDataSource function to cache worksheet data and Data Portal results for use with SQL helper formulas.
---
* * *

## Overview

The jDataSource function is the foundation of all SQL helper functions in Interject. It allows you to cache data in memory—either from a worksheet range or from a Data Portal—so you can use that data with other SQL helper functions like jQuery, jFilter, jJoin, jGroup, and jAggregate.

Think of jDataSource as creating a temporary database table in Excel that you can query without making repeated calls to your database.

## Understanding jDataSource

### Why Cache Data?

Caching data with jDataSource provides several benefits:

* **Performance** - Once data is cached, SQL helper functions operate on it without additional database calls
* **Efficiency** - Process data that's already in memory faster than requesting it repeatedly
* **Flexibility** - Combine data from multiple sources and manipulate it in-memory


### What Can You Cache?

jDataSource can cache data from two sources:

1. **Worksheet Ranges** - Any data in your Excel workbook
2. **Data Portals** - Data retrieved using Interject Data Portals

### Basic Syntax

The basic syntax for jDataSource is:

```Excel
=jDataSource(DataSource, ColDefRange, [Params], [CacheTag])
```

| Parameter | Description | Required |
|-----------|-------------|----------|
| **DataSource** | The range or Data Portal name to cache | Yes |
| **ColDefRange** | Header row defining column names and types | Yes |
| **Params** | Parameters to pass to a Data Portal | No |
| **CacheTag** | A label to identify this cache | No |


## Setting Up Your First jDataSource

### Example 1: Worksheet Range

Let's say you have customer data in your worksheet that you want to use with other SQL helper functions.

#### Step 1: Prepare Your Data

First, ensure your data has a header row with column names:

| CustomerID | CompanyName | City | Country |
|--|--|--|--|
| ALFKI | Alfreds Futterkiste | Berlin | Germany |
| ANATR | Ana Trujillo Emparedados y helados | México D.F. | Mexico |
| ANTON | Antonio Moreno Taquería | México D.F. | Mexico |

#### Step 2: Create the jDataSource Formula

In a new cell lets day F1, create a jDataSource formula that references this data:

```Excel
=jDataSource(A2:D4,A1:A4,,"CachedCustomers")
```

This formula:
- **A2:D4** - References the data range excluding headers
- **A1:A4** - References the data range for the headers
- **"CachedCustomers"** - Tags this cache as "CachedCustomers" for easy reference

#### Step 3: Use the Datasource

Once created, you can reference this DataSource in other SQL helper functions using the tag:
Place below function in F2 cell

```Excel
=jFilter(F1, jWhere("Country", C6, "="))
```

This formula:
- **F1** - Contains the datasource formula
- **C6** - Contains the country name to filter

To show the data in Excel, create a ReportRange function in cell F3



```
=ReportRange(F1,A9:D12,A8:D8)
or
=ReportRange(F2,A9:D12,A8:D8)
```

Where

- **F1** - Contains the datasource formula
- **F2** - Contains the jFilter formula.
- **A9:D12** - The target range for the data
- **A9:D12** - The column definition for the target data


When you pull the data through interject pull, the excel will show the datasource data or filtered data in the cell A9 to D12

![](/images/L-Dev-SQL-in-Excel/jDataSourceExample.png)

### Example 2: Data from a Data Portal

To cache data from a Data Portal with parameters:

```Excel
=jDataSource("NorthwindCustomers", B2:M2,, "NorthwindCache")
```

This formula:
- **"NorthwindCustomers"** - The Data Portal name
- **B2:M2** - Header row defining column names
- **"NorthwindCache"** - Cache tag for later use

## Data from a Worksheet

### Scenario: Multi-City Sales Analysis

Suppose you have sales data in a worksheet and want to analyze sales by customer and city.

#### Setup

1. Place your sales data in cells A2:G100 without headers:

2. A1:G1 the header row details:
   - OrderID, CustomerID, CompanyName, OrderAmount, OrderDate, City, Country

3. Create the jDataSource formula in cell A102:

```Excel
=jDataSource(A2:G100,A1:G1,"","SalesData")
```

4. Now you can use "SalesData" throughout your workbook with other SQL helper functions

#### Usage

Once defined the JDataSource, you can:
- Filter to show only USA customers
- Join with product information
- Group by city and sum amounts
- Run custom queries

## Data from a Data Portal

### Scenario: Monthly Customer Order Summary

Customer order data that includes parameters:

#### Step 1: Identify Your Data Portal

Ensure you have a Data Portal configured called "CustomerOrders" with parameters for:
- DateStart
- DateEnd

#### Step 2: Create the Column Definition Range

In cells B1:F1, create column headers that match your Data Portal output:

```
OrderID | CustomerID | CompanyName | OrderAmount | OrderDate
```

#### Step 3: Create the jDataSource Formula

In cell B3, create the jDataSource formula:

```Excel
=jDataSource("CustomerOrders", B1:F1,, "OrderCache")
```

Where:
- C5 contains the start date
- D5 contains the end date


## Tagging Your Data Cache


### Tag Naming Best Practices

Use descriptive, consistent names:

* **GOOD**: "NorthwindCustomers", "SalesData", "ProductInventory"
* **AVOID**: "Cache1", "Data", "temp"

### Multiple Caches

You can create multiple caches in your worksheet:

```Excel
=jDataSource(A1:D50,A1:D1,"","Customers")
=jDataSource(E1:G50,E1:G1,"","Products")
=jDataSource(H1:K50,H1:K1,"","Orders")
```

## Best Practices

1. **Use Descriptive Tag Names** - Makes formulas more readable
2. **Place jDataSource Formulas in Consistent Locations** - Store them near the top of your worksheet
3. **Minimize Cache Sizes** - Only cache the data you need for better performance

## Real-World GL Example

The [LocalReportingExamples.xlsx](/download/SQL%20in%20Excel%20Examples/LocalReportingExamples.xlsx) file demonstrates how to cache General Ledger data for analysis. Here's how it works:

### Excel File Setup

In the "Pull" sheet of [LocalReportingExamples.xlsx](/download/SQL%20in%20Excel%20Examples/LocalReportingExamples.xlsx), GL transaction data is using jDataSource:

**Source Data:** GLData sheet contains 2,800+ transactions with columns:
- Posted Date, Year-Month
- Account hierarchy (Full Account, Account code, Amount)

**Screenshot 1: GLData Source**

![](/images/L-Dev-SQL-in-Excel/01-GLData-Source.png)

### The jDataSource Formula

```Excel
=jDataSource(B19:J2804, B18:J18,, "GL_Detail")
```

**Breaking it down:**
- **B19:J2804** - Range of GL transactions (2,800+ rows)
- **B18:J18** - Header row with column definitions
- **"GL_Detail"** - Tag to reference this cache in other formulas

**Screenshot 2: jDataSource Formula**

![](/images/L-Dev-SQL-in-Excel/02-jDataSource-Formula.png)

### The Result

This jDataSource can be used by other SQL helper functions without querying the database repeatedly.

## Next Steps

Now that you understand how to cache data with jDataSource, explore how to:

* [Filter cached data with jFilter and jWhere](/wDeveloper/L-Dev-jFilter-jWhere.html)
* [Query cached data with jQuery](/wDeveloper/L-Dev-jQuery.html)
* [Join multiple data sources with jJoin](/wDeveloper/L-Dev-jJoin.html)
* [Group data with jGroup](/wDeveloper/L-Dev-jGroup.html)
