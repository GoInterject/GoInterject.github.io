---
title: Adding Notes To A Report
layout: custom
keywords: [Report, Epicor, Notes, Comments]
headings: ["Report Setup", "Adding Summary Level Comments"]
links: ["/images/bFinancials-AddingNotes/01.png", "/images/bFinancials-AddingNotes/02.png", "/images/bFinancials-AddingNotes/03.png", "/images/bFinancials-AddingNotes/04.png", "/images/bFinancials-AddingNotes/05.png", "/images/bFinancials-AddingNotes/06.png", "/images/bFinancials-AddingNotes/07.png", "/images/bFinancials-AddingNotes/08.png", "/images/bFinancials-AddingNotes/09.png", "/images/bFinancials-AddingNotes/10.png", "/images/bFinancials-AddingNotes/11.png", "/images/bFinancials-AddingNotes/11.1.png", "/images/bFinancials-AddingNotes/12.png", "/images/bFinancials-AddingNotes/13.png", "/images/bFinancials-AddingNotes/14.png"]
description: Step by step guide on adding comment columns to your report templates.
---

Adding a notes column that saves back to a database is a multi-step process. First, you'll set up a column for the data will be placed. Then, you'll add two report formulas to manipulate the data, and lastly, you'll structure the report formulas to point to the various data within the report so it saves and pulls comments.

## Report Setup
First, unfreeze the panes for your report.



![Unfreeze Panes](/images/bFinancials-AddingNotes/01.png)



Now expand the top grouping to show columns A-C.



![Group Expansion](/images/bFinancials-AddingNotes/02.png)



Then, if a comments column doesn't exist in your report, insert a column as the rightmost column of your report.



![Insert a column](/images/bFinancials-AddingNotes/03.png)



Label it **Comments**.



![Labeling the column](/images/bFinancials-AddingNotes/04.png)



Insert a column to the right of Column B (or the row definitions column) and insert **RowDefName** in row 2.

> **NOTE:** The RowDefName Column must be one column to the right of the Row Definitions for your main report pull function.



![Inserting RowDefName](/images/bFinancials-AddingNotes/05.png)



Then, insert 4 rows above the report formulas row. Make rows 10 and 12 dark blue and label them "Column Definitions - Notes - Get", and "Column Definitions - Notes - Save", respectively.



![Inserting Notes Column Definitionst](/images/bFinancials-AddingNotes/06.png)



In cells C11, E11, M11 and N11 insert **Segment5**, **Segment1**, **NoteText**, **[Clear]** respectively.



![Column Definitions Pull](/images/bFinancials-AddingNotes/07.png)



Next, in cells C13, E13, M13, and N13 insert **Segment5**, **Segment1**, **NoteText**, and **MessageToUser** respectively.



![Column Definitions Save](/images/bFinancials-AddingNotes/08.png)



> **NOTE:**
> If you usehave other dimensions in the report, you can use Segment2, Segment3, Segment4 respectively.
> Additionally, the cells in which these column definitions are placed **MUST** align with the column definitions in row 2.

Now, insert two rows below row 19.

![Insert two new rows](/images/bFinancials-AddingNotes/09.png)



In cell E20 input **Notes Get:** and in cell G20 input **=ReportFixed()**.



![Insert report fixed formula](/images/bFinancials-AddingNotes/10.png)



Then, select cell G20, and select the **fx** button. Now input the following values for each field:
    
     DataPortal  = ERP_Note_Fixed_Get
     RowDefRange = C70:E171
     ColDefRange = 11:11
     Parameters  = Param(,G64,,,,,,G65,MONTH(FiscalPeriod),YEAR(FiscalPeriod))



![Insert report fixed fields](/images/bFinancials-AddingNotes/11.png)



This uses a two column approach to the RowDefRange for this specific formula, which means it will create a unique combined key for the data to be searched on. Ultimately, it forces each record to be indexed by that unique key for each row within the ReportFixed() function.



![Insert report fixed fields v2](/images/bFinancials-AddingNotes/11.1.png)



> **NOTE:**
> The param function and the param field the values represented are one-to-one ordered mappings from a segment 
> to a filter on the report. This means that the first parameter in the Param function represents segment1. So 
> what you are passing to the segment is the filter value for your report. Your report may have different filters
> and will need to be ordered according to your report specifically. The values given here are suitable for the 
> example report. 


In cell E21 insert **Notes Save:** and in cell G21 **=ReportSave()**.

![Insert report save formula](/images/bFinancials-AddingNotes/12.png)



Next, select cell G21, then select the **fx** button and input the following values for each field:

    DataPortal   = ERP_Note_Save
    RowDefRange  = C71:C169
    ColDefRange  = 13:13
    ResultsRange = N13
    Parameters   = Param(,G64,,,,,,G65,MONTH(FiscalPeriod),YEAR(FiscalPeriod))

![Insert report save fields](/images/bFinancials-AddingNotes/13.png)



As opposed to the ReportFixed() function, the ReportSave() only uses a singular column for the RowDefRange. This is because a save does not need the unique key to save values back, since it has the capability to save data that has a many-to-one relationship between row identifiers and the data. However, when pulling that data back out, the pull function (in this case the ReportFixed) does need a unique identifier to determine which data belongs to which key, as well as where to place it.

> **NOTE:**
> The param function in the param field the values represented are one-to-one ordered mappings from a segment 
> to a filter on the report. This means that the first parameter in the Param function represents segment1. So 
> what you are passing to the segment is the filter value for your report. Your report may have different filters
> and will need to be ordered according to your report specifically. The values given here are suitable for the 
> example report. 
>
> Be aware that Param position 9 is typically used for the month of the fiscal period, and 
> Param position 10 is typically used for the year of the fiscal period.

### Adding Summary Level Comments

To be able to add comments on your summary level labels, you will need to add into column C Excel formulas that link the summary level rows to the grouping/row definitions in column B. As seen in the example below, cell C78 points to cell B76.



![Insert combo keys for fixed pull](/images/bFinancials-AddingNotes/14.png)
