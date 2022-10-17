---
title: INTERJECT Financials for Epicor
layout: custom
keywords: [Account, Epicor, Companies]
description: INTERJECT™ Financials for Epicor Enterprise (This would cover topics that are specific to integration with Epicor Enterprise, and would potentially be different for each ERP) 
---

## Overview

## My Apps

**Interject Financials:** Includes 44 data portals related to *Financials for Spreadsheets.* Data connection is redirected through ""

**Interject Demos:**  Includes 46 data portals related to demonstrating various Interject capabilities using a demo database connection pointing to Interject's cloud enviroment.

To learn more about DataPortals, and how to set them up, visit the [DataPortals](/wPortal/Data-Portals.html) page.

## Data Connections

**Name:** "Connection01"

**Connection String:**

For more information about Interject Connection Strings and how to set them up, visit the [Data Connections Labs](/wPortal/Data-Connections.html) and learn about API and Database connections.

For information about connecting to other sources, visit [Connectionstrings.com/sql-server](https://www.connectionstrings.com/sql-server/) and select what connection type is needed.

**PROD:** Data Source = "Database01"; Initial Catalog=""; Integrated Security=SSPI

**BETA:** Data Source = "Database02"; Initial Catalog=""; Integrated Security=SSPI 

**DEV:** Data Source = "Database03"; Initial Catalog=""; Integrated Security=SSPI

**Other Connections:** 
- "Connection02": Used for initial SYSDATA migration only in DEV.
- "Connection03": Used to point to Laminin DEV Lab.

## Data Portals

"DataPortal01"
- Import yearly numbers into the Interject Reporting DB from a list of Epicor DBs
- Connection: "Connection01"

"DataPortal02"
- Import yearly budget numbers into the Interject Reporting DB from a list of Epicor DBs
- Connection: "Connection01"

"DataPortal03"
- Summary & detail report of Epicor Chart of Accounts with balances
- Override of another DataPortal from offering
- Connection: "Connection01"
