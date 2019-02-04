---
title: jDataPortal()
layout: custom
keywords: [jdataportal, function, dataportal]
description: jDataPortal() function is a helper function used by developers to further leverage DataPortals. It can reduce the number of data connections used by INTERJECT in a report, speeding the report process and conserving server resources. 
---

---

## Function Summary

jDataPortal() function is a helper function used by developers to further leverage DataPortals. It can reduce the number of data connections used by INTERJECT in a report, speeding the report process and conserving server resources. It allows DataPortals to be re-used in the same report pull event, so multiple report functions can access the data in memory and place specific data in the tab using different methods. jDataPortal() can also be used to adjust the sort order and filter the data in memory before the it is presented. jDataportal can only be used inside of an [ INTERJECT data function ](Data-Functions-Landing.html) as a helper function.

For users with the [ ClientAdmin ](/wPortal/INTERJECT-Roles.html) user role, jDataPortal() can also be used to redirect the connection, stored procedure, or API during testing.

### Function Arguments

| Parameter Name     | Description | Default | Optional |
|:---|:---|:---|:---|
| DataPortalName     | The name of the INTERJECT DataPortal set up to connect with data.                                                                                                                                                                                                                                              |         | NO       |
| DataResultNumber   | This controls the data set from a stored procedure that is returned based on the order of the data sets in the SQL stored procedure.                                                                                                                                                                           |         | YES      |
| Filter             | Filter using syntax that would normally follow a WHERE statement in SQL. For example, if only filtering customers that contain an s, see the below example. OR as well as AND SQL operators can be used. Additionally, other advanced SQL filter syntax is able to be utilized. |         | YES      |
| OrderBy            | A sort can be added using syntax that would normally follow an "Order By" statement in SQL.                                                                                                                                                                                                                    |         | YES      |
| CommandOverride    | Directs the data call to a different Stored Procedure or API command. This is used only for testing and can only be done by ClientAdmin or Editor roles.                                                                                                                                                       |         | YES      |
| ConnectionOverride | Changes the Data Connection name used for testing. Only available for ClientAdmin or [Editor](/wPortal/INTERJECT-Roles.html) roles.|| YES      |

### Excel Formula Bar Example

```Excel
jDataPortal("NorthwindMultiRecord_Pull",2,"[CompanyName] Like '%s%'","[CustomerID] ASC")
```
A simpler form of this example can be found in our [ Lab Dev: Customer Aging Detail ](/wGetStarted/L-Dev-CustomerAgingDetail.html).

### Example Function Composition

| Argument Name      | Example Mapping           | Explanation |
|--------------------|---------------------------|----------|
| Function Name      | `=jDataPortal`              | This is the excel name used to call the function. It is not meant to standalone and is meant to be embedded inside of an [ Interject Data Function ](Data-Function-Landing.html)                                                                                                                                                                                           |
| Data Portal Name   | NorthwindMultiRecord_Pull | The DataPortalName argument is used to define the name of a created data portal that is to be called by a data function.                                                                                                                                                                                                                                                   |
| Data Result Number | 2                         | This is the identifying number ID of a record result set from a stored procedure. In the event that a single stored procedure contains two record sets from two different select statements the first record set to be created by the stored procedure is designated with the result number 1. The second result set to be created is designated with the result number 2. |
| Filter             | [CompanyName] Like '%s%'  | The filter argument refines the data. This has to be a valid SQL Where statement. In this example the data is filtered by selecting only records where the CompanyName column contains an "S" in any record value.                                                                                                                                                          |
| OrderBy            | [CustomerID] Desc         | This orders the CustomerID column results in descending alphabetical order. This has to be a valid SQL statement.                                                                                                                                                                                                                                                          |
| CommandOverride    | ""                        | This is left blank since there is no need to create a call to a different stored procedure. If you need to call a different stored procedure you would change this value from "" to the entire name of a stored procedure. For example "demo.NorthwindCustomer"                                                                                                            |
| ConnectionOverride | ""                        | This is left blank since there is no need to call a different database connection.                                                                                                                                                                                                                                                                                         |

### Usable In These Data Functions

* [ReportRange()](ReportRange.html)
* [ReportVariable()](ReportVariable.html)
* [ReportFixed()](ReportFixed.html)
