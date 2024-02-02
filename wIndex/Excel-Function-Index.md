---
title: Excel Function Index
filename: "Excel-Function-Index.md"
layout: custom
keywords: [functions, formulas, index, data, pull, save, drill, event, helper, data cell]
headings: ["Overview", "Data Pull Functions", "Data Save Functions", "Data Drill Functions", "Event Functions", "Helper Functions", "Data Cell Functions"]
links: ["/wIndex/ReportRange.html", "/wIndex/ReportFixed.html", "/wIndex/ReportVariable.html", "/wIndex/ReportLookup.html", "/wIndex/ReportSave.html", "/wIndex/ReportDrill.html", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#save-data", "/wIndex/ReportMacro.html", "/wIndex/ReportRun.html", "/wIndex/ReportCalc.html", "/wIndex/ReportDefaults.html", "/wIndex/ReportGrouping.html", "/wIndex/ReportHideRowOrColumn.html", "/wIndex/jDropdown.html", "/wIndex/jFocus.html", "/wIndex/jFreezePanes.html", "/wIndex/jCombine.html", "/wIndex/jCombine_IF.html", "/wIndex/jDataPortal.html", "/wIndex/jColumnDef.html", "/wIndex/jRangeTag.html", "/wIndex/jWorkbookProperty.html", "/wIndex/Pair.html", "/wIndex/PairGroup.html", "Pair.html", "/wIndex/Param.html", "/wIndex/jAcct.html", "/wIndex/jCell.html", "/wIndex/jDesc.html"]
image_dir: ""
images: []
description: Interject provides features by leveraging spreadsheet formulas that are familiar to many users. These formulas can be used to direct data into a spreadsheet, creating practical and adaptable reports. By adding report drills and navigation through additional spreadsheet formulas, these reports become a comprehensive reporting solution.
---
* * *

##  Overview

Interject provides features by leveraging spreadsheet formulas that are familiar to many users. These formulas can be used to direct data into a spreadsheet, creating practical and adaptable reports. By adding report drills and navigation through additional spreadsheet formulas, these reports become a comprehensive reporting solution.

### Data Pull Functions

Data Pull Functions are focused on getting specific data to the report in the right way and placed inside the spreadsheet. There are a variety of functions and options therein to give flexibility in what data is displayed.

| Forumula                                                | Description                                                         |
|---------------------------------------------------------|---------------------------------------------------------------------|
| [ReportRange()](/wIndex/ReportRange.html)       | Inserts data into a single range of a spreadsheet                   |
| [ReportFixed()](/wIndex/ReportFixed.html)       | Pulling in data to a predetermined fixed point.                     |
| [ReportVariable()](/wIndex/ReportVariable.html) | Insert data into rows that include multiple ranges or sections      |
| [ReportLookup()](/wIndex/ReportLookup.html)    | Insert a specific data value into a cell based on certain criteria. |

### Data Save Functions

The Data Save Function ReportSave is designed to save data within the sheet back to the data source, making it easy to manipulate the data without having to edit the database directly.

| Forumula                                                | Description                                                         |
|---------------------------------------------------------|---------------------------------------------------------------------|
| [ReportSave()](/wIndex/ReportSave.html)         | Save data on the sheet back to the database.                        |

### Data Drill Functions

The Data Drill Function ReportDrill provides a convenient way to run another targeted function while at the same time, transferring contextual data for filtering to that function. It is widely used as a way to connect and pass information between workbooks and worksheets.

| Forumula                                                | Description                                                         |
|---------------------------------------------------------|---------------------------------------------------------------------|
| [ReportDrill()](/wIndex/ReportDrill.html)       | Drilling down on data and Navigating between reports                |

### Event Functions

Event Functions are functions designed to run when a designated event triggers them. An Interject event is a Clear Data or Run event. A Run event can be a [Pull Data](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) action or a [Save](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#save-data) action. The values defined within the event trigger function will determine when it is executed. These functions allow synchronization and data precision witin the report.

| Formula                                                                | Description                                                                                        |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [ReportMacro](/wIndex/ReportMacro.html)         | Call VBA macros.                |
| [ReportRun()](/wIndex/ReportRun.html)           | Execute Report functions in other sheets.                           |
| [ReportCalc()](/wIndex/ReportCalc.html)                        | Executes a calculation on a worksheet or workbook.                                 |
| [ReportDefaults()](/wIndex/ReportDefaults.html)                | Captures and send values from one cell(s) to another.                   |
| [ReportGrouping()](/wIndex/ReportGrouping.html)  | Expands or collapses groups.                                         |
| [ReportHideRowOrColumn()](/wIndex/ReportHideRowOrColumn.html)  | Hides rows or columns.                                            |

### Helper Functions

Helper Functions are functions that help streamline the report generation process and offer additional customization. They are often embedded into other parent functions to be leveraged into more specific and accurate functions or enhance their capabilities. Some can also be used as stand-alone functions to add functionality to the page. Other Helper Functions are focused on the report itself and does not impact or direct data in the report. These functions can improve the speed and presentation of which data can be understood, manipulated and viewed in the report.

| Formula                                                       | Description                                                                                                  |
|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [jDropdown()](/wIndex/jDropdown.html)                         | Returns a set of data in a dropdown list for easy insertion into the sheet.            |
| [jFocus()](/wIndex/jFocus.html)                                | Sets the Excel focus (active cell selection) upon a freeze panes action.            |
| [jFreezePanes()](/wIndex/jFreezePanes.html)                    | Used with the QuickTools option for freeze/unfreeze panes.                         |
| [jCombine()](/wIndex/jCombine.html)                   | Concatenate the values of cells while simultaneously skipping any empty cell.              |
| [jCombineIf()](/wIndex/jCombine_IF.html)             | Uses a conditional statement to determine which values should be included into a single concatenated string. |
| [jDataPortal()](/wIndex/jDataPortal.html)             | Helpful function for developers to further leverage DataPortals.                           |
| [jColumnDef()](/wIndex/jColumnDef.html)              | Assists financial reports using the FinCube DataPortal to specify segment filters for each amount column.    |
| [jRangeTag()](/wIndex/jRangeTag.html)                | Used to label or tag a range or a single cell with a custom name.                           |
| [jWorkbookProperty()](/wIndex/jWorkbookProperty.html) | Provides context and information about a workbook in a report.                             |
| [Pair()](/wIndex/Pair.html)                           | Used with a variety of report functions to specify a from value or range to a target location or range.      |
| [PairGroup()](/wIndex/PairGroup.html)                 | Used to string multiple [Pair()](Pair.html) functions together into one comma delimited string      |
| [Param()](/wIndex/Param.html)                         | Used to help select one or multiple parameters for each of your report formulas.            |

### Data Cell Functions

Data Cells are focused on a single formula which can be placed anywhere in the spreadsheet and can ask for any financial number or summary from it. Once this single formula approach is understood, there is no limit to the combinations that can be created. This is typically an easier method to start writing custom reports. However, given their flexibility the report run times can take more than just a few seconds to complete, sometimes up to 5 minutes. Larger reports, such as one with 70,000 formulas, can take up to 10 minutes to complete. Fortunately, users may continue working with a spreadsheet while waiting for Data Cell reports to finish calculating.

| Formula                              | Description                                                        |
|--------------------------------------|------------------------------------------------------------------- |
| [jAcct()](/wIndex/jAcct.html)        | Specifies filters for up to six segments of a Chart of Accounts    |
| [jCell/jCellN()](/wIndex/jCell.html) | Retrieves data based on the provided parameters                    |
| [jDesc()](/wIndex/jDesc.html)        | Used to look up a context description based on a specific segment. |
