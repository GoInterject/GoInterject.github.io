---
title: "Lab Developer: Error Handling with RAISERROR and UserNotice"
layout: custom
keywords: [error, handling, RAISERROR, UserNotice]
description: Explains how INTERJECT handles errors in Data Portals using T-SQL RAISERROR and UserNotice
---

### Introduction

This page will cover error handling in INTERJECT development using T-SQL’s RAISERROR and INTERJECT’s UnderNotice flag.

### Understanding Error Handling

There are two types of errors that INTERJECT can display: unhandled and handled. Unhandled errors are system generated, whereas handled errors are anticipated and written by developers. For example, on a pull or save, an error may occur on the server which the report is trying to access. This error could be handled by the developer if the developer anticipates it, or it could be left as an unhandled error. 

### Error Handling with RaiseError and UserNotice

#### RAISERROR

INTERJECT leverages the T-SQL statement RAISERROR in its Data Portals to process errors.

RAISERROR is designed to generate error messages and initiate error processing in the session (Source: [Microsoft RAISERROR Documentation][microsoft doc]). It is used as follows:


![](/images/Error-Handling/01.png)


**@ErrorMessageToUser** - a string containing a description of the error, with or without a prefix of ‘UserNotice:’.

**severity** - generally a number from 0-18 ranking the severity of the error, typically 18 if you want to stop the execution of a stored procedure.

**state** - number, 0-255, used to locate where errors occur in your code.

*See [Microsoft RAISERROR Documentation][microsoft doc] from more detailed information on using RAISERROR and its parameters.

#### UserNotice

**‘UserNotice:’** is an INTERJECT-defined identifying string that we append to the beginning of the @ErrorMessageToUser argument at the time of passing to RAISERROR to indicate that we would like a popup to appear to the user in Excel when the error occurs. It is used as follows:


![](/images/Error-Handling/02.png)


When ‘UserNotice:’ is added to your @ErrorMessageToUser before being passed to RAISERROR, it **enables the option of having a popup window appear**, alerting the user of the error in Excel.

![](/images/Error-Handling/03.png)

Errors can quickly be *handled* (as opposed to leaving unhandled) by developers simply by using the UserNotice string.

### Unhandled Error Behavior with RAISERROR

If you opt not to use UserNotice, you error will still be reported by the INTERJECT addin, but no popup window will appear for the user:

![](/images/Error-Handling/04.png)

[microsoft doc]: https://docs.microsoft.com/en-us/sql/t-sql/language-elements/raiserror-transact-sql?view=sql-server-2017
