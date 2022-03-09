---
title: "Lab Developer: Categories Pull and Save"
layout: custom
keywords: [save, example, walkthrough, customer aging,]
description:
---
##  **Overview:**

The lab will focus on how to create an Excel tool to be able to pull the data out of a Northwind Categories table into an Excel tab as well as to be able to add, edit, or delete categories to this table. Below you will find the list of requirements you will need to fulfill to have a minimal, fully-functioning data sheet using the Interject Add-in. 

###  NorthwindCategories SQL Table 

This lab focuses on the Northwind Categories table so please be sure you have access to a Northwind database to complete the lab.
For the purposes of this lab and learning how to work with an integer column, please add the TotalStock int column to the NorthwindCategories table.

IMAGE

## General Requirements

1. A data connection and at least two data portals (one for pulling and the other for saving)
    https://portal.gointerject.com/
IMAGE

2. A simple table in the connected database
3. A simple datasheet that
    a. Should be formatted with column definitions, formatting ranges, formulas, etc. at the top
    
    IMAGE

    b. Should have a title
    c. Can have a field or fields for entering filters for your pulls

    IMAGE
    d. Should have table header names for each field pulled from the database, e.g.
        [CategoryID]
        [CategoryName]
        [TotalStock]
        [Description]

        IMAGE
    
    e. Should have a field for getting output results from the save procedure (e.g. [MessageToUser])
    f. Data should be populated using one or more Report() functions
4. A stored procedure for pulling data from the table
    a. Should at least have RequestContext as an input parameter
    b. Returns table column required for testing in data sheet (e.g. name, stock, description)
5. A stored procedure for saving data to the table
    a. Parameters
        1. Interject_RequestContext should be a parameter to get information from the sheet. The RequestContext Parser helper procedure should unpack context values for you
        2. @CategoryName is used if data sheet has a filter for query result
        3. @HeaderMessage is used as a way to give confirmation that a delete was successful or       generally when changes are pushed successfully to the database
    b. Should execute RequestContext parser to obtain data from the sheet calling the procedure
        1. Information obtain should be stored in a temporary table variable (@DataToProcess) to help process and validate the information from RequestContext before updating the actual table itself
    c. Validation. You need to check every single input in the context by checking each value in the column, e.g.
        1. Make sure that new entries have [CategoryID] and [CategoryName] that are unique and have no duplicates and that [CategoryID] and [CategoryName] cannot be empty 
        2. Existing rows cannot have their [CategoryID] be modified
        3. [TotalStock] should be a completely valid INTEGER and cannot be less than 0.
        4. [CategoryName], [Description], etc. cannot exceed a specified amount of characters
    d. Debugging
        1. If there were any issues found during the validation procedure, the execution of the stored procedure should be halted and redirected to code that handles the return of all the errors found in each row back to the sheet (e.g. attach the error message on each row in @DataToProcess which contains any errors for that row and return that table instead)
        2. @HeaderMessage should be used to confirm any updates made to the table after validation is passed

### Specific Requirements

1. Adding general comments in unused cells is very helpful at telling the user what can and cannot be done in the sheet without the having them do guesswork

IMAGE

2. Configure jFreezePanes() such that the Interject header rows and the primary key columns are hidden away from the user’s view

3. Use GETUTCDATE() and @UtcOffset (obtained from RequestContext) to return error/debug messages that are relative to the user’s time

IMAGE

4. In the sheet, the last row of RowDefRange (for ReportSave()) and TargetRange (for ReportRange()) should be the same. It should have a line that has “End of list” or something similar. This will be important for when parsing through the request context in the code.

IMAGE
IMAGE

5. There should be thorough validation done on each input received by the save stored procedure. Any validation issue found should have the code short-circuit to code that returns all the errors/updates for each row and if errors exist, an error using “UserNotice” should be returned

IMAGE
IMAGE

    a. [CategoryID]
        1. Must be unique
        2. The user SHOULD NOT be able to modify the ID, but this step is necessary to ensure no pre-existing entries in the database are being overwritten
    b. [CategoryName]
        1. Must be unique
        2. Cannot be empty
        3. Cannot exceed a certain amount of characters
        4. If there is a filter applied in the sheet and the user tries to add an entry that already exists (but the filter hides the pre-existing item), there should be an error message returned. 
        5. A unique value for each CategoryName is important as it is used in several joining operations
    c. [TotalStock]
        1. This value is pulled in as a VARCHAR since there is no guarantee as to what the user enters in the datasheet is valid. But regardless, you should make sure that this value is a valid integer
        2. This value cannot be negative, cannot be a decimal/float number, cannot be alphanumeric, empty, etc.
    d. [Description]
        1. Can be empty
        2. Cannot exceed a certain amount of characters
6. Important; for delete capabilities in the save procedure to happen, make it so that any Category from the table that is not listed in the context will be deleted from the table.
    a. This deletion should happen when a row in @DataToProcess is not matched

IMAGE
    b. When a deletion occurs, make sure it is accounted for in the return message back to the user

IMAGE 
IMAGE

7. Alternatively, you can add another column called [Delete?] which holds a flag that determines whether the matched row should be removed from the table

8. Important; for adding capabilities, it is important that you run several checks on columns that should be unique.

9. If a user accidentally tries to add a duplicate Category while in a filtered view, make sure to return an error. Not doing this could result in overwriting pre-existing rows.

IMAGE
IMAGE

10. When adding/updating/deleting items in the datasheet, make sure that CategoryName is used as RowDefRange when calling the save stored procedure



IMAGE












