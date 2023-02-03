---
title: Diagnostics
layout: custom
keywords: [Diagnostics, Tools, Settings, Configurations, Config]
description: The Diagnostics feature of Interject allows users to set and change numerous configurations within Excel as well as utilize various tools for diagnostics and debugging.
---
* * * 

## Overview

The Diagnostics feature of Interject allows users to set and change numerous configurations within Excel as well as utilize various tools for diagnostics and debugging. It is located in the Advanced Menu of Interject:

![](/images/Diagnostics/Ribbon.png)
<br>

Depending on your company's settings, you will have access to a number of tools.

There are 3 fields within the Diagnostic pane:

<**Execute Selected Action**>: Execute the selected tool
Navigation: Shows a hierarchy list of tools
Instructions: Displays information about the currently selected tool
Input: Put your input code here. Some tools require an input for execution.
Results: The results of the execution are displayed here

Most tools can be executed by simply clicking the <**Execute Selected Action**> button. Others require an input
 
### Public

The Public tools involves Logging, Cache, and Bug Fixes.

![](/images/Diagnostics/Public.png)
<br>

| Setting | Description |
|----|----|
| Toggle Verbose Logging | Click Execute Selected Action to toggle Verbose Logging. This adds very detailed logs on hundreds of application events for detailed analysis by support folks. |
| Toggle Memory Logging | Click Execute Selected Action to toggle Verbose Logging. This adds very detailed logs on hundreds of application events for detailed analysis by support folks.<br><br>No input required.  You may change the default 3000 millisecond delay by replacing this text with the number of milliseconds required.  The setting must be between 1000 and 30000 milliseconds. |
| Toggle DataCell Audit Mode | Click 'Execute Selected Action' to Enable or Disable the Formula Auditing Mode for DataCell calculations.  This will provide you exact cell address data for errors noted when you re-run the reports. |
| Reset Settings Cache | This will reset the user setting cache so the system will be forced to repull from the central database. |
| Open User Folders | Click Execute to open the folders for user application data, client shared data and report file cache. |
| [Apply Special Features](/wIndex/Diagnostics-SpecialFeatures.html) | This allows a user to enable special features that may be needed for their environment.<br><br>Codes to use:<br>Workaround for Microsoft Animations Bug: BugFix1=ON or BugFix1=OFF <br>Workaround for Microsoft Repaint Bug: BugFix2=ON or BugFix2=OFF <br> Macro security features must be setup in the Portal Website or through Interject Support |

### System Tools

The System Tools involve various systems settings.

![](/images/Diagnostics/SystemTools.png)
<br>

| Setting | Description |
|----|----|
| List DataPortals | Click Execute Selected Action to show the DataPortal List for the active user.  |
| Toggle Double Click Events | Click 'Execute Selected Action' to enable or disable the Interject_DoubleClick custom property in the current workbook [TestsTypes.xlsx].  By setting to true it will enable the double click events for the drill. The in-memory setting is set to False. |
| Set RunOnOpen For Workbook | Click 'Execute Selected Action' to enable or disable the Interject_RunOnOpen custom property in the current workbook [TestsTypes.xlsx].  By setting this property the workbook can automatically pull data when opened.<br><br>Input allowed:<br>No input will toggle between true and false. True will pull data on the activesheet when opened.<br>'Prompt' = will show Pull Data form when file is opened.<br>'T:Sheet1\|F:!A5' = will pull data for the tab Sheet1 but will exclude A5 from the report action, but will run the rest.<br>'F:A5' = will pull data for the active sheet for only the report formula in cell A5.<br>'T:Sheet1' = will pull data for the tab Sheet1 for all report formulas.<br>'RunOnce,T:Sheet1' = Will do the same as above, but the setting will be cleared afterwards.<br>'T:Sheet1,T:Sheet2\|F:CellName' = will pull for all of Sheet1, then pull for Sheet2 but for only the report formulas in the range name 'CellName'.<br><br>To test various settings against the current workbook, and view a sample execution plan, use: 'Test=' and then the instructions<br>    Test= T:Sheet1\|F:A5'  <br>    Test= true  <br>    Test= T:Sheet1  <br>    Test= F:A5  <br>    ... then click Execute Selected Action|
| Toggle Log Truncation | Click 'Execute Selected Action' to Enable or Disable the truncation of logs. |
| Reset Settings Cache - All Users | This will mark all users in the client to repull their settings cache from the central database at the next opportunity.  Only users with the ClientAdmin role can execute this action. |
| Reset File Cache | This will remove all files that were previously downloaded and cached as well as reset the users settings cache. |
| Open Application Folders | Click Execute to open the folders for AppData, UserData, and UserConfig<br>Click once installations use a subdirectory of: C:\Users\MyUserName\AppData\Local\Apps\2.0 |
| Set Enterprise Connection | Paste a Connection String in the Input box. Click Execute Selected Action to save this connection string encrypted for use in Enterprise installations. To clear the connection string, leave the 'Input' box empty and then Execute.  If 'Encrypted:' is shown at the start of the connection string, it is currently stored encrypted.<br>Example: "server=My_Server_Name;database=My_Database_Name;integrated security=true";<br>or "server=My_Server_Name;database=My_Database_Name;User Id=myUsername;Password=myPassword;" |
| Reset Cursor | Click 'Execute Selected Action' to reset a wait cursor that has not reset properly. |
| Open Install Configuration | Click Execute Action to open the configuration window |
| Force Garbage Collector on Dead Memory | Click Execute to clear unused RAM memory (aka Garbage Collection) |
| Find All Workbook Formulas | Click 'Execute Selected Action' to Find all formulas in the active workbook. |
| Search the Report Library | Use this command to search for many kinds of data within the Report Library. <br>Below, enter the exact text to locate. Then click 'Execute Selected Action'<br>It will search the names and descriptions of Report Library folders, files (links), versions and drill codes. |
| Replace Data Portal Codes | Click 'Execute Selected Action' to Replace all DataPortalCodes in the current workbook<br>input text should contain<br>oldName_One = NewName_One<br>anotherOldName = anotherNewName |

### Support

The Support tools involve tools that support the Interject/Excel environment.

![](/images/Diagnostics/Support.png)
<br>

| Setting | Description |
|----|----|
| Clear Data Cell Cache | This will clear the Data Cells cache in memory.  It is used for troubleshooting only. |
| [Change ShortKey](/wIndex/Diagnostics-ShortKey.html) | Allows you to reassign a shortkey. After a shortkey is reassigned you must close and reopen Excel.<br><br>Changes create configurations to your local IdsSettings.xml file such as<br><ShortkeyChanges>True</ShortkeyChanges><br><ReportLibrary>Ctrl+Shift+A</ReportLibrary>.<br><br>Input reassignments here such as 'ReportLibrary=Ctrl+Shift+A'.<br>To disable or re-enable all shortkey reassignments input 'DisableAll' or 'EnableAll'<br>Currently shortkey reassignments are enabled.<br>Allows for multiple lines of commands to be input. |
| Clear Error Log | Click Execute Selected Action to clear the error log at C:\Users\test\AppData\Local\Interject\Settings\ErrorLog.xml. |
| Re-Initiate Interject | Click Execute Selected Action to make sure that basic setup information is in place for Interject to run. If Interject has already been initiated, this process will reset and clear certain settings. |
| Set Application Data Source | Click Execute Selected Action to set Interject's application data source. NOTE: Which data sources are available to you will depend on your Interject subscription. Possible sources are:<br>EnterpriseDatabase<br>InterjectPlatform |
| Launch the License Management Form | Click Execute Selected Action to open the License management form. |

### Setup

The Setup tools involve settings that setup Interject.

![](/images/Diagnostics/Setup.png)
<br>

| Setting | Description |
|----|----|
| View Select Globals | Click 'Execute Selected Action' to view global variable settings.  Input options are Globals(or leave blank), GlobalsXML, DataLogCache, DataLogCacheXML, DataLogSent, DataLogSentXML, Diagnostics, DiagnosticsXML |
| Get Diagnostics Login Password | Type here the reference code that is shown in the diagnostics login screen and click 'Execute Selected Action' |
| Set Release Flags | Select Release Target: Production, Test, Development<br><br>Select Release Install Method: MSI Install, Click Once Install<br><br>API/WS URL Options:<br>URL Type for Services: https, http<br>URL Prefix for Services: blank, QA-, Test-, Dev-<br><br>Select Release Install Scope: Per User, Per Machine<br><br>(Must re-login after changes) |
| View Report Library Data | Use this command to view a textual list of all Report Library data. Shorten the report by using these numbers in the 'input' box<br>1=show only sources<br>2=show categories (folders)<br>3=also show links<br>4=also show drills<br>5=also show versions |

### View File

The View File tools allow users to directly open up various config and settings files.

![](/images/Diagnostics/ViewFile.png)
<br>

| Setting | Description |
|----|----|
| Setting Cache | This will decrypt by default.  Replace 'Input' text  with 'Skip Decrypt' to bypass decryption.  Will look for file here: C:\Users\test\AppData\Local\Interject\Settings\InterjectCKuWBCtTU7v4kuw3ICpl1.xml |
| Connect | This will decrypt by default.  Replace 'Input' text  with 'Skip Decrypt' to bypass decryption.  Will look for file here: C:\Users\test\AppData\Local\Interject\Settings\InterjectConnect.xml |
| Error Log | This will decrypt by default.  Replace 'Input' text  with 'Skip Decrypt' to bypass decryption.  Will look for file here: C:\Users\test\AppData\Local\Interject\Settings\ErrorLog.xml |
| Login Support | This will decrypt by default.  Replace 'Input' text  with 'Skip Decrypt' to bypass decryption.  Will look for file here: C:\Users\test\AppData\Local\Interject\Settings\InterjectSupport.xml |
| File Cache Versions | This will decrypt by default.  Replace 'Input' text  with 'Skip Decrypt' to bypass decryption.  Will look for file here: C:\Users\test\AppData\Local\Interject\Settings\C:\Users\test\AppData\Local\Interject\FileCache |
| File App Config | This will decrypt by default.  Replace 'Input' text  with 'Skip Decrypt' to bypass decryption.  Will look for file here: C:\Users\test\AppData\Local\Interject\Settings\C:\Users\test\AppData\Local\Interject\FileCache |
| File Ids Settings | This will show the contents of the IdsSettings.xml file. It Will look for file here: <br>C:\Users\test\AppData\Local\Interject\Settings\IdsSettings.xml<br>settings can be updated and saved by adding this syntax to the input: key = value |

### Error Handling

The Error Handling tools involve handling errors and tracing threads.

![](/images/Diagnostics/ErrorHandling.png)
<br>

| Setting | Description |
|----|----|
| Raise Error | This will throw a System Exception with the text provided in the 'Input'<br>!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!<br>While in DEBUG mode, UI Errors (Form errors) are handled differently . See notes in GlobalUIThreadException() |
| Toggle Admin View of Errors | Click 'Execute Selected Action' to change the setting for Admin View of Errors. |
| View Error Context | Click 'Execute Selected Action' to view the most recent Error Context items. |
| Do Startup Logging | Click 'Execute Selected Action' to set up Startup Logging.<br>Excel will need to be closed and re-opened to gather startup data, after clicking 'Execute Selected Action'.<br>Startup Logging will write startup data into a file with a date stamp (example: StartupLog_1605030127.txt). That file will be contained in the root folder of this application. That folder will also open when you click 'Execute Selected Action'.This file can be deleted once it is no longer needed. |
| Initialize FileLog Of RequestContext | Click 'Execute Selected Action' to set up Error Context Logging.<br>Error Context Logging will write data into a file with a date stamp (example: ErrorContextTrace_201708140232.txt). That file will be contained in the \AppData\Local\Interject\Settings folder.<br>This file can be deleted once it is no longer needed.<br>Enter "START" in the input area to begin logging.<br>Enter "STOP" in the input area to cancel logging.<br>Enter "STARTUP" in the input area to begin logging the next time Excel is started.<br>Enter "CancelStartup" in the input area to no longer log when Excel is started. |
| Trace Code Execution Threads | Traces all ErrorContext data, with indentation for following code paths. |
| View Current Threads | View all current (and background) threads for this app.<br><br>NOTE: some Excel Thread errors only reproduce in production, not in DEBUG<br>Recreate certain thread errors by entering the number of the test code scenario.<br>1 ... alter text from a background thread (no error)<br>3 ... Read Excel WB Name from background thread (Excel Hangs when closed) |

### Data Calls

The Data Calls Tools involve logs of data calls.

![](/images/Diagnostics/DataCalls.png)
<br>

| Setting | Description |
|----|----|
| Show Data Call Log | Click 'Execute Selected Action' to see logs recorded since recording has been turned on. |
| Show Timer Log | Click 'Execute Selected Action' to see the timer logs recorded since recording has been turned on. |
| Show Memory Log | Click 'Execute Selected Action' to see the memory monitor logs recorded since recording has been turned on. |
| Get ADO.NET Response | Enter XML Data in the format shown in 'Input'. Then Click Execute Selected Action |
| Test ADO.NET Connection | Enter XML Data in the format shown in 'Input'. Then Click Execute Selected Action |
| Show Data Cell Request XML | Click 'Execute Selected Action' to see what XML would be sent when requested data cell information. |
| Trace Sql Calls | The Diagnostics form must be left open while tracing SQL calls.<br>To begin, click the execute button. To end, click it again or just close this form. |
| Trace DataPortal Results | The Diagnostics form must be left open while tracing DataPortal Results.<br>To begin, click the execute button. To end, click it again or just close this form.<br><br>DataPortal Result Tracing is Off<br>Click the execute button to toggle this on or off.<br>these options are toggled in this order:<br>1. Trace with spaces<br>2. Trace with tabs<br>3. Tracing is Off |

### General Functionality

The General Functionality Tools involve the general functionality of Interject within Excel.

![](/images/Diagnostics/GeneralFunctionality.png)
<br>

| Setting | Description |
|----|----|
| Alterable Diagnostic Test | Click Execute Selected Action to execute the general code contained in the AlterableDiagnosticTest Sub. This sub may be altered for quick tests, and will not contain code that should be saved. |
| Test ActionEventHandler | Click Execute Selected Action to Build the ActionEventHandler and bring a prompt for whether to execute or not. Inputs can be <br>Drill	Pull	ClearPull<br>Save	GoBack	ClearSave |
| Log All Formulas in Files | Click Execute Selected Action to Open every Report Library file listed, and then save a log of Report Formulas<br>The list is populated with all files that are available to you.<br>Delete any files that are not applicable.<br>Updates will flash on the screen in the results window. |
| Get Clipboard Excel XML | Click execute to view what is in the clipboard using type 'XML Spreadsheet' |
| Set Clipboard Excel XML | Copy in XML Spreadsheet data and click execute set it to the clipboard. |
| Open Formula Parser | Click Execute to Open Parser Window |

### Web Service

The Web Services Tools involve logs and settings of Web services.

![](/images/Diagnostics/WebService.png)
<br>

| Setting | Description |
|----|----|
| Override Data WS URL | Set the 'Input' text to an empty string to trigger a reset. Or enter the url of your localhost instance. eg.  <br>http://localhost:54090/Interject_DataWS_Salesforce_DEV/rest.ashx<br>http://localhost:50037/Interject_DataWS_Salesforce_DEV/rest.ashx<br>http://localhost:50421/interject_dataws_salesforce_dev/rest.ashx  |
| Set Proxy Usage | Due to performance issues and firewall restrictions, the use of the default Web Proxy can be managed here.<br>This setting can be temporarily changed here. Or, stored in IdsSettings.xml as the ongoing default.<br>...possible inputs:                      (enter one of these inputs below, then click 'Execute')<br>1<br>1 (Remember)<br>2<br>2 (Remember)<br>3<br>3 (Remember)<br>Reset |
| Set TLS settings | Use this command to test TLS Https communication<br>Click Execute to set the ServicePointManager.SecurityProtocol to the topmost selection below. |
| Trace Web Calls | The Diagnostics form must be left open while tracing web calls.<br>To begin, click the execute button. To end, click it again or just close this form. |
| Enable Verbose HTTP Logs | The Diagnostics form must be left open while viewing verbose http logs.<br>To begin, click the execute button. To end, click it again or just close this form. |

### Debug Only

The Debug Tools involve tools used for debugging purposes.

![](/images/Diagnostics/DebugOnly.png)
<br>

| Setting | Description |
|----|----|
| View Memory Helper | Only for DEBUG. This looks at memory that is being tracked for object lifecycles. |
| Search Performance Test | Searches for formulas, recording elapsed time. |
| Throw Error in Background Thread | Causes catastrophic failure. |
| Impersonate | Enter the password on line 1 and the Session Token on line 2. |
| Test keys | |
| Test WCF To AddinManager | Executes the command in the input, passed to the Addin Manager |