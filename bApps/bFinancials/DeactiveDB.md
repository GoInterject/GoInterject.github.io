---
title: Deactivate Databases
filename: "DeactiveDB.md"
layout: custom
keywords: [inactive, deactivate, databases, script, SQL]
headings: []
links: ["https://docs.gointerject.com/bApps/bFinancials/InitialDataLoad.html#begin-data-load"]
description: Following are the steps required to deactivate specified databases in your initial upload.
---

Following are the steps required to deactivate specified databases in your initial upload:

> To Do
>
>  - Run the script below to see a list of all databases Interject will import
>  ```SQL
> --List all imported DBs
> SELECT * FROM [ImportERP].[SourceDatabaseList]
>  ```
>
>  - You must mark as inactive the DBs you wish to exclude using the following script
> ```SQL
>  --Deactivate selected DB
> UPDATE [ImportERP].[SourceDatabaseList]
> SET [Inactive] = 1 
> WHERE [DatabaseName] = '[DeactivateDatabase2]'
>```
> If a database is made inactive after the initial load, data that was initially imported will still be in Interject and can be used to report from. However new data will stop flowing into interject.
>
> Continue following [these steps](https://docs.gointerject.com/bApps/bFinancials/InitialDataLoad.html#begin-data-load) to complete the upload