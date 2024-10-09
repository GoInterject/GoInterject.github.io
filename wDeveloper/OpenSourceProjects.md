---
title: Open Source Projects
filename: "OpenSourceProjects.md"
layout: custom
keywords: []
headings: ["Overview", "BeetleETL", "Data-Latinizer", "Financial Data Engineering", "ScriptMySQLServer", "Powershell DB Tools GUI"]
links: ["#beetleetl", "#data-latinizer", "#financial-data-engineering", "#scriptmysqlserver", "#powershell-db-tools-gui", "https://pypi.org/project/BeetleETL/", "https://gitlab.com/Open-Interject/Beetle-ETL", "https://gitlab.com/Open-Interject/Data-Latinizer", "https://gitlab.com/Open-Interject/interview-projects", "https://gitlab.com/Open-Interject/ScriptMySQLServer", "https://gitlab.com/Open-Interject/PowershellDBToolsGui"]
image_dir: ""
images: []
description: Interject hosts a variety of open-source projects aimed at providing useful tools for data handling, automation, and database management.
---
* * *

## Overview

Interject hosts a variety of open-source projects aimed at providing useful tools for data handling, automation, and database management.

- [BeetleETL](#beetleetl) : Transfer data from a MongoDB to a SQL Server DB
- [Data-Latinizer](#data-latinizer) : Sanitize data in a DB using Latin text
- [Financial Data Engineering](#financial-data-engineering) : Build a DB for analyzing securities
- [Script My SQL Server](#scriptmysqlserver) : Set of scripts to automate MySQL server interactions
- [Powershell DB Tools GUI](#powershell-db-tools-gui) : Simplify scripting out DB objects and executing SQL scripts

### BeetleETL

Beetle is a Python3 package with tools necessary for transferring data from a MongoDB database to a SQL Server Database. A well defined configuration file allows the user to define the exact way data from MongoDB should be transferred to SQL Server, making Beetle a powerful tool for ETL solutions where transferring data from databases is necessary. The package comes equipped with a standalone executable as well as a modular execution setup enabling easy API or custom script integration.

[Pypi](https://pypi.org/project/BeetleETL/)

[Project Repo](https://gitlab.com/Open-Interject/Beetle-ETL)

### Data-Latinizer

This project provides a tool to sanitize data in a database using Latin text. It includes PowerShell scripts to easily execute SQL scripts on a specified database.

To use Data-Latinizer, download or clone the repository, navigate to the Powershell Scripts folder, and run the ExecuteAllSqlScripts.ps1 script, providing your server instance and database details. This script will loop through and execute all SQL files in the project on the given database. If script execution is blocked, the project provides instructions for adjusting the PowerShell execution policy to bypass restrictions.

[Project Repo](https://gitlab.com/Open-Interject/Data-Latinizer)

### Financial Data Engineering

This project focuses on building a foundational database for analyzing securities, similar to an investment firm’s approach. Using public data, such as an energy fund’s holdings combined with SEC filings, the goal is to create a small reporting app that can query stock information by SEC Accession Number. The project leverages the `yfinance` Python package to tie holdings data (containing ticker symbols) to security information.

Key tasks include:

- Integrating unrelated datasets (holdings, SEC data, and stock data).
- Designing a SQL database for storing and querying stock data.
- Building a web app (using Streamlit) to retrieve and display financial information.

[Project Repo](https://github.com/GoInterject/interview-projects/tree/main/financials-example)

### ScriptMySQLServer

This project includes two PowerShell scripts for automating MySQL server interactions:

ScriptMySQLServer.ps1: Connects to a MySQL server to export stored procedures and functions from databases into individual SQL files, organized by database and object type. It supports exporting from all or specific databases and generates SQL DROP and CREATE statements for each object.

ExecuteSqlScripts.ps1: Executes SQL scripts from a specified folder on a MySQL server. It uses provided credentials and can run in test mode for debugging by printing variable values.

[Project Repo](https://gitlab.com/Open-Interject/ScriptMySQLServer)

### Powershell DB Tools GUI

The Powershell DB Tools GUI is a tool designed for database administrators and developers to simplify the process of scripting out database objects and executing SQL scripts on one or more databases. The program offers a user-friendly interface with two main functionalities: the Script Out DB and Execute SQL Scripts tabs.

[Project Repo](https://gitlab.com/Open-Interject/PowershellDBToolsGui)
