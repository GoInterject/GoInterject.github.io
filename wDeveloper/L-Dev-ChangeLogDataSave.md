---
title: "Develop: Change Log Data Save"
layout: custom
keywords: [developer, example, walkthrough, SQL, SSMS, Data Portal, data connection, data save, history]
description: In this example you will modify the simple data save using the Customer Aging Detail report and the Northwind Customers data source to add or delete a customer.
---
* * *

## Overview

In this example you will modify the previous [save](/wDeveloper/L-Dev-AdvancedDataSave.html), which was modified to insert and delete customers. In this Change Log Data Save, you will modify the Stored Procedure (SP) again to include a change log.

<blockquote class=highlight_note>
<b>Note:</b> This example uses Microsoft's Northwind Database. You can download this database <a href="https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/downloading-sample-databases">here</a> or you can use this example as a guide for your own data source.
</blockquote>

## Setting up the Data Connection

For the Data Connection for this example, you will use the connection previously set up [here](/wGetStarted/L-Dev-CustomerAging.html#setting-up-the-data-connection).

