---
title: "Develop: Error Handling with RAISERROR and UserNotice"
filename: "L-Dev-Error-Handling.md"
layout: custom
keywords: [error, handling, RAISERROR, UserNotice, return message]
headings: ["Overview", "Understanding Error Handling", "Error Handling With RAISERROR", "Error Handling With UserNotice", "Unhandled Error Behavior"]
links: ["https://docs.microsoft.com/en-us/sql/t-sql/language-elements/raiserror-transact-sql?view=sql-server-2017", "https://docs.microsoft.com/en-us/sql/t-sql/language-elements/raiserror-transact-sql?view=sql-server-2017"]
image_dir: "Error-Handling"
images: [
	{file: "01", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "02", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "03", type: "png", site: "Add-in", cat: "Progress Bar", sub: "Error Popup", report: "", ribbon: "Simple", config: ""}, 
	{file: "04", type: "png", site: "Add-in", cat: "Progress Bar", sub: "", report: "", ribbon: "Simple", config: ""}
	]
description: Explains how Interject handles errors in Data Portals using T-SQL RAISERROR and UserNotice.
---
* * *

## Overview

This page will cover error handling in Interject development using T-SQL's RAISERROR and Interject's UserNotice flag.

### Understanding Error Handling

There are two types of errors that Interject can display: unhandled and handled. Unhandled errors are system generated, whereas handled errors are anticipated and written by developers. For example, on a pull or save, an error may occur on the server which the report is trying to access. This error could be handled by the developer if the developer anticipates it, or it could be left as an unhandled error.

### Error Handling With RAISERROR

Interject leverages the T-SQL statement RAISERROR in its Data Portals to process errors.

RAISERROR is designed to generate error messages and initiate error processing in the session (Source: [Microsoft RAISERROR Documentation](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/raiserror-transact-sql?view=sql-server-2017){:target="_blank"}{:rel="noopener noreferrer"}). It is used as follows:

![](/images/Error-Handling/01.png)
<br>

**@ErrorMessageToUser** - a string containing a description of the error, with or without a prefix of ‘UserNotice:'.

**severity** - generally a number from 0-18 ranking the severity of the error, typically 18 if you want to stop the execution of a stored procedure.

**state** - number, 0-255, used to locate where errors occur in your code.

* See [Microsoft RAISERROR Documentation](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/raiserror-transact-sql?view=sql-server-2017){:target="_blank"}{:rel="noopener noreferrer"} from more detailed information on using RAISERROR and its parameters.

### Error Handling With UserNotice

**UserNotice:** is an Interject-defined identifying string that we append to the beginning of the @ErrorMessageToUser argument at the time of passing to RAISERROR to indicate that we would like a popup to appear to the user in Excel when the error occurs. It is used as follows:

![](/images/Error-Handling/02.png)
<br>

When **UserNotice:** is added to your @ErrorMessageToUser before being passed to RAISERROR, it enables the option of having a popup window appear, alerting the user of the error in Excel.

![](/images/Error-Handling/03.png)
<br>

Errors can quickly be handled (as opposed to leaving them unhandled) by developers simply by using the UserNotice string.

### Unhandled Error Behavior

If you opt not to use UserNotice, your error will still be reported by the Interject Add-in, but no popup window will appear for the user:

![](/images/Error-Handling/04.png)
<br>
