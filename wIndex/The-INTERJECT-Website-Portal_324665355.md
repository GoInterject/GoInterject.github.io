---
title: Interject Documentation > The INTERJECT Website Portal
layout: custom
---
* * *

##  **Overview**

The INTERJECT website portal is a central place to manage INTERJECT client
settings and user profiles. The most common use is to manage users, data
portals, and data connections. Data portals and connections support the
INTERJECT reporting and save back functions. This section will review all
areas of the website portal. Go directly to any topic by clicking one of the
links below. The database connection can support MS SQL Server OLEDB as well
as ODBC. ODBC allows connection to any other relational database. Currently,
INTERJECT only supports direct connections with databases that support stored
procedures. This includes Oracle, MySQL, MariaDB and many others.  
For all other data sources, a custom website API can be created to connect the
data to INTERJECT. This is very similar to how a website application accesses
its data layer. Using an API you can connect to PostgreSQL and noSQL databases
like MongoDB. You can also use an API to connect to other cloud data APIs such
as provided by SalesForce, Intacct, Netsuite, Quicken and many other cloud
software services.  
  

###  [ Logging In to the Interject Website Portal ](/wPortal/Logging-In-to-
Website-Portal_142278762.html)

This section details how to log in to the INTERJECT website portal to get
access to INTERJECT features.

###  [ Data Connections ](/wPortal/Data-Connections_324403237.html)

A Connection is used with Data Portals so INTERJECT can connect to certain
stored procedures within a database or to a custom website API. A single
connection can be used by many Data Portals.

###  [ Data Portals ](/wPortal/Data-Portals_324665363.html)

In this section you will quickly set up a connection to SQL Server and test it
using the security context of the user from their Excel session.

A Connection can be set up to connect directly to a database using a OLEDB or
a .Net Adapter connection string for MS SQL Server or using a ODBC connection
string to connect to Oracle, MySQL, or others that support stored procedures.
For other databases, including noSQL databases, a customer website API can be
used to connect the datasource to INTERJECT, which is covered in a later
section.

The following lists are examples of connection strings for SQL Server:

  * Example .Net Adapter connection string: Server=myServerAddress;Database=myDataBase;Trusted_Connection=True; 
  * Example OLEDB connection string: Provider=SQLNCLI11;Server=myServerAddress;Database=myDataBase; Trusted_Connection=yes; 
  * Example of an ODBC connection string: Driver={SQL Server Native Client 11.0};Server=myServerAddress; 
  * Database=myDataBase;Trusted_Connection=yes; 

See  [ https://www.connectionstrings.com/
](https://www.connectionstrings.com/) for additional information on connection
strings.

###  [ User Profile ](/wPortal/User-Profile_324763687.html)

Managing Users and User Profiles is another commonly used area of the
INTERJECT Website Portal. The role of Client Admin, has the ability to open
the profile of a user by clicking on their name. The menu to the left includes
the link **User Profile** as a shortcut to get to your own user profile.  
  

