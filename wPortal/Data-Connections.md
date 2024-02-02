---
title: Data Connections
filename: "Data-Connections.md"
layout: custom
keywords: [data connections, data portals, api, database]
headings: ["Overview", "API Connections", "Database Connection"]
links: ["/wPortal/L-Api-Connections.html", "/wPortal/L-Database-Connection.html"]
image_dir: ""
images: []
description: A Connection is used with Data Portals so Interject can connect to certain stored procedures within a database or to a custom website API.
---
* * *

## Overview

A Connection is used with Data Portals so Interject can connect to certain stored procedures within a database or to a custom website API. A single connection can be used by many Data Portals. The database connection can support MS SQL Server OLEDB as well as ODBC. ODBC allows connection to any other relational database. Currently, Interject only supports direct connections with databases that support stored procedures. This includes Oracle, MySQL, MariaDB and many others.

For all other data sources, a custom website API can be created to connect the data to Interject. This is very similar to how a website application accesses its data layer. Using an API you can connect to PostgreSQL and noSQL databases like MongoDB. You can also use an API to connect to other cloud data APIs such as provided by SalesForce, Intacct, Netsuite, Quicken and many other cloud software services.

### [API Connections](/wPortal/L-Api-Connections.html)

An API can be used with a Data Connection to connect to any database, including noSQL databases, using standard development practices that are used to develop website applications. You can also connect to other website APIs such as those from Salesforce, Netsuite, Intacct and many others.

### [Database Connection](/wPortal/L-Database-Connection.html)

A Datat Connection can be set up to connect directly to a database using a OLEDB or a .Net Adapter connection string for MS SQL Server or using a ODBC connection string to connect to Oracle, MySQL, or others that support stored procedures.
