---
title: Data Connections
layout: custom
---

##  **Overview**

A Connection is used with Data Portals so INTERJECT can connect to certain stored procedures within a database or to a custom website API. A single connection can be used by many Data Portals.  The database connection can support MS SQL Server OLEDB as well as ODBC. ODBC allows connection to any other relational database. Currently, INTERJECT only supports direct connections with databases that support stored procedures. This includes Oracle, MySQL, MariaDB and many others.   
For all other data sources, a custom website API can be created to connect the data to INTERJECT. This is very similar to how a website application accesses its data layer. Using an API you can connect to PostgreSQL and noSQL databases like MongoDB. You can also use an API to connect to other cloud data APIs such as provided by SalesForce, Intacct, Netsuite, Quicken and many other cloud software services.   
Go directly to any topic below by clicking one of the links below. 

###  [ Lab 15.1 API Connections ](/wPortal/Lab-15.1-API-Connections_324665359.html)

An API can be used with a Data Connection to connect to any database, including noSQL databases, using standard development practices that are used to develop website applications. You can also connect to other website APIs such as those from Salesforce, Netsuite, Intacct and many others.   
In this lab, you will set up a simple connection to an example API. Detailed documentation on using a custom data API’s are currently under development. Please contact us for more information if needed 

###  [ Lab 15.2 Database Connection ](/wPortal/Lab-15.2-Database-Connection_136249415.html)

A Connection can be set up to connect directly to a database using a OLEDB or a .Net Adapter connection string for MS SQL Server or using a ODBC connection string to connect to Oracle, MySQL, or others that support stored procedures. For other databases, including noSQL databases, a customer website API can be used to connect the datasource to INTERJECT, which is covered in a later section. 
