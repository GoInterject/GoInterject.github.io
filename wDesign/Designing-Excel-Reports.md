---
layout: custom
title:  "Interject Report Layout and Design Standards - Update"
date:   2018-10-14 9:03:02 -0700
categories: Excel Layout
keywords: [reports, layouts, design, guidelines]
description: Guidelines for designing and laying out reports.
---
---
**Theme File:** [HERE]()

**Example Excel Workbook:** [HERE]()

[comment]: <> (Directory for Theme Work (Located on TS 13589):)
[comment]: <> (D:\Data\Interject\ThemeWork)

Based on Stock 2010 'Austin' theme.
Theme file can be applied to Excel 2007 and 2010 Workbooks.  Not compatible with Excel 2003.
Example Excel Workbook compares our theme to standard office theme.  Some colors will look "terrible" if the user does not have our theme present and the default theme applies.  If the worksheet/workbook you are creating will be used by the customer to copy/paste values into other workbooks, please be aware that there are some bad conversions (like the Purple in the Office standard).  Avoid using those colors if you know users will copy and paste into other workbooks.
Please review and try to utilize on future templates.  This is still a work in process so feel free to contribute further direction.



[comment]: <> (### How to format and organize complicated reports.)
[comment]: <> (Example Report: Projections Template)

### Hidden Report Sections
The blue section at the top of this image is hidden, and contains several sections used to help the report. The sections shown below may not be used with every report, but you can use these as a guide on how to organize your own report.


### Fincube Column Definitions

Has all of the column names used in the final SQL SELECT statement from the called stored procedure.
Additional data ReportFixed Column Definitions: Column definitions for the second pull in the report. Like above, but seperated out here to clearly identify that these column headers come from two different sources.

### Formatting Range 

Used by the Pull used in the Fincube formula. Has some straight forward formatting, but also some conditional formatting. For example, there is a hidden column saying if the Account is editable or not, and the resulting row is Yellow or Gray depending on what that column says.

### Month Column to be used in JE Query Drill 

This is intended to only apply to Actuals. Like the sections above for the Pull columns, just used for the Drill formulas. If there is a value on this row, Interject will think that column is drillable within the range of values.

### Report Formulas

Has all of the report formulas. The formulas shown are executed in the order that they are listed, and all of the formulas are labeled with what they do.

### ReportSave Column Definitions

The column headers used by the called stored procedure save process. Usually, the column headers are column names in the resulting XML. 

### Hidden Parameters and Notes

All of the parameters and calculations, used in the Report Formulas and in the report below. It is good to use this section for any complex calculations or formatting you need to consider, to keep your formulas and visible report clean. In many cases, it is is easier to maintain this section instead of all of the logic within each of the formulas or the visible report section.

### Hidden Parameters

Fincube formulas and other Interject Data Portals have the potential to take several inputs, and become complicated. To help in their legibility, it is best to organize your input parameters in the hidden section like the image above shows. You can then customize those input parameters with Excel logic, which is easier to manage outside of the actual Interject Formula. The highlighted portions of the screenshot are examples of how to handle this.

For example, the Retain Rows cell on F41 is fed into the Interject formula. The contents of F41 looks at two of the filter options in the visible portion of the report, Retain Rows and Syst. If Retain Rows is set to Yes, then Fincube here will retain the rows on the Pull. If Syst is set to Yes, it will retain on the columns Acct, Syst, and Sbst, and on No it will only retain on Acct. All the logic for both of them are done in F41, and the formula only needs to look at the result of the calculation.

### Customizing Columns Shown

This report is actually very wide. There are over 8 sections, each with 12 columns for all of the month. When combined with the row headers on the left, spaces, and smaller sections, that makes the report over 100 columns wide.
 
To help with this, we hide the columns we do not need to see. The columns shown or hidden can change though, depending on the Year-Month. To help make this dynamic, we use an additional tab called Lookups. The 
 


