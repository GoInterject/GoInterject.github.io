---
title: Interject Documentation > Excel Function Index
layout: custom
---
* * *

##  **Interject Function Index**

INTERJECT provides features by leveraging spreadsheet formulas that are familiar to many users. These formulas can be used to direct data into a spreadsheet, creating practical and adaptable reports. By adding report drills and navigation through additional spreadsheet formulas, these reports become a comprehensive reporting solution.

## Data Funcions

Data Functions are focused on getting specific data to the report in the right way and placed inside the spreadsheet. There are a variety of functions and options therein to give flexibility in what data is displayed.

| Forumula                                                | Description                                                         |
|---------------------------------------------------------|---------------------------------------------------------------------|
| [ReportDrill()](wIndex\ReportDrill_61702556.html)       | Drilling down on data and Navigating between reports                |
| [ReportFixed()](wIndex\ReportFixed_61702203.html)       | Pulling in data to a predetermined fixed point.                     |
| [ReportLookup()](wIndex\ReportLookup_127973727.html)    | Insert a specific data value into a cell based on certain criteria. |
| [ReportMacro](wIndex\ReportMacro_61702548.html)         | Call VBA macros on Save, Pull, Clear, or Run events.                |
| [ReportRange()](wIndex\ReportRange_61702199.html)       | Inserts data into a single range of a spreadsheet                   |
| [ReportRun()](wIndex\ReportRun_61702558.html)           | Execute Report functions in other sheets.                           |
| [ReportSave()](wIndex\ReportSave_61702554.html)         | Save data on the sheet back to the database.                        |
| [ReportVariable()](wIndex\ReportVariable_61702201.html) | Insert data into rows that include multiple ranges or sections      |


## Formatting Functions

Formatting Functions are focused on the report itself and does not impact or direct data in the report. These functions can improve the speed and presentation of which data can be understood, manipulated and seen in the report. Once formatting functions are fully understood, reports can be dissected, analysed, and assessed at a much more rapid pace with a very low amount of impact on report run times.

| Formula                                                                | Description                                                                                        |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [JFocus()](wIndex\jFocus.html)                                         | Sets the excel focus (active cell selection) upon a freeze panes action                            |
| [JFreezePanes()](wIndex\jFreezePanes_128552956.html)                   | Used with the QuickTools option for freeze/unfreeze panes.                                         |
| [ReportCalc()](wIndex\ReportCalc_137265163.html)                       | Executes a calculation on a worksheet or workbook.                                                 |
| [ReportDefaults()](wIndex\ReportDefaults_61702546.html)                | Utilized to capture and send values from one cell(s) to another.                                   |
| [ReportHideRowOrColumn()](wIndex\ReportHideRowOrColumn_341147669.html) | Hides rows and columns on report events                                                            |
| [ReportMerge()](wIndex\ReportMerge_110723133.html)                     | Merge multiple Excel reports into one based on [jMergePoints()](wIndex\jMergePoint_110723143.html) |


## Helper Functions

Helper Functions are often embedded into other parent functions (listed above) to be leveraged into more specific and accurate functions or enhance their capabilities. Some can also be used in stand-alone fashion to add functionality to the page.

| Formula                                                       | Description                                                                                                  |
|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [jBinder()](wIndex\jBinder_61702552.html)                     | Assists the Binder feature mark worksheets                                                                   |
| [jColumnDef()](wIndex\jColumnDef_127965411.html)              | Assists financial reports using the FinCube DataPortal to specify segment filters for each amount column.    |
| [jCombineIf()](wIndex\jCombine_IF_139526244.html)             | Uses a conditional statement to determine which values should be included into a single concatenated string. |
| [jCombine()](wIndex\jCombine_61702542.html)                   | Concatenate the values of cells while simultaneously skipping any empty cell.                                |
| [jDataPortal()](wIndex\jDataPortal_61702544.html)             | Helpful function for developers to further leverage DataPortals.                                             |
| [jMergePoint()](wIndex\jMergePoint_110723143.html)            | Acts as a reference point for [ReportMerge](/wIndex/ReportMerge_110723133.html) .                            |
| [jRangeTag()](wIndex\jRangeTag_138772490.html)                | Used to label or tag a range or a single cell with a custom name.                                            |
| [jWorkbookProperty()](wIndex\jWorkbookProperty_61702550.html) | Provides context and information about a workbook in a report.                                               |
| [Pair()](wIndex\Pair_81756188.html)                           | Used with a variety of report functions to specify a from value or range to a target location or range.      |
| [PairGroup()](wIndex\PairGroup_81756186.html)                 | Used to string multiple [Pair()](Pair_81756188.html) functions together into one comma delimited string      |
| [Param()](wIndex\Param_81756199.html)                         | Used to help select one or multiple parameters for each of your report formulas                              |

## Data Cell Functions

Data Cells are focused on a single formula which can be placed anywhere in the spreadsheet and can ask for any financial number or summary from it. Once this single formula approach is understood, there is no limit to the combinations that can be created. This is typically an easier method to start writing custom reports. However, given their flexibility the report run times can take more than just a few seconds to complete, sometimes up to 5 minutes. Larger reports, such as one with 70,000 formulas, can take up to 10 minutes to complete. Fortunately, users may continue working with a spreadsheet while waiting for Data Cell reports to finish calculating.

| Formula                                      | Description                                                        |
|----------------------------------------------|--------------------------------------------------------------------|
| [jAcct()](wIndex\jAcct_61702534.html)        | Specifies filters for up to six segments of a Chart of Accounts    |
| [jCell/jCellN()](wIndex\jCell_61702532.html) | Retrieves data based on the provided parameters                    |
| [jDesc()](wIndex\jDesc_61702536.html)        | Used to look up a context description based on a specific segment. |
