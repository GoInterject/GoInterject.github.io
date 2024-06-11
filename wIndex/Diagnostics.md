---
title: Diagnostics
filename: "Diagnostics.md"
layout: custom
keywords: [Diagnostics, Tools, Settings, Configurations, Config]
headings: ["Overview", "Diagnostic Pane Fields", "Public", "System Tools", "Support"]
links: ["/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#advanced-menu-items", "/wIndex/Diagnostics-SpecialFeatures.html", "/wIndex/Diagnostics-ShortKey.html"]
image_dir: "Diagnostics"
images: [{file: "Ribbon", type: "png", site: "Addin", cat: "Ribbon", sub: "", report: "", ribbon: "Advanced", config: ""}, {file: "DiagnosticsPaneFields2", type: "png", site: "Addin", cat: "Diagnostics", sub: "", report: "", ribbon: "", config: ""}, {file: "Public2", type: "png", site: "Addin", cat: "Diagnostics", sub: "Public", report: "", ribbon: "", config: ""}, {file: "SystemTools2", type: "png", site: "Addin", cat: "Diagnostics", sub: "System Tools", report: "", ribbon: "", config: ""}, {file: "Support2", type: "png", site: "Addin", cat: "Diagnostics", sub: "Support", report: "", ribbon: "", config: ""}]
description: The Diagnostics feature of Interject allows users to set and change numerous configurations within Excel as well as utilize various tools for diagnostics and debugging.
---
* * * 

## Overview

The Diagnostics feature of Interject allows users to set and change numerous configurations within Excel as well as utilize various tools for diagnostics and debugging. It is located in the [Advanced Menu](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#advanced-menu-items) of Interject:

![](/images/Diagnostics/Ribbon.png)
<br>

Depending on your company's settings, you will have access to a number of tools.

### Diagnostic Pane Fields

There are 5 fields within the Diagnostic pane:

1.  <**Execute Selected Action**>: Execute the selected tool (some tools require an input first)
2.  Navigation: Shows a hierarchy list of tools
3.  Instructions: Displays information about the currently selected tool
4.  Input: Put your input code here. Some tools require an input for execution.
5.  Results: The results of the execution are displayed here

![](/images/Diagnostics/DiagnosticsPaneFields2.png)
<br>

### Public

The Public tools involves Logging, Cache, and Bug Fixes.

![](/images/Diagnostics/Public2.png)
<br>

| Setting | Description |
|----|----|
| [Clear External Login Cookies](/wAbout/Logging-In-Enterprise.html#clearing-login-cookies) | Click Execute to clear external login cookies. This will delete any saved form data in the login window as well.<br><br>If you log in with an external auth provider you may be offered an option to remember your login. This may create a security risk in some cases. You can use this feature to clear the data stored for your login so other users can not log in with your cached auth cookie.|
| Toggle Verbose Logging | Click Execute Selected Action to toggle Verbose Logging. This adds very detailed logs on hundreds of application events for detailed analysis by support folks. |
| Toggle Memory Logging | Click Execute Selected Action to toggle Verbose Logging. This adds very detailed logs on hundreds of application events for detailed analysis by support folks.<br><br>No input required.  You may change the default 3000 millisecond delay by replacing this text with the number of milliseconds required.  The setting must be between 1000 and 30000 milliseconds. |
| Toggle DataCell Audit Mode | Click 'Execute Selected Action' to Enable or Disable the Formula Auditing Mode for DataCell calculations.  This will provide you exact cell address data for errors noted when you re-run the reports. |
| Reset Settings Cache | This will reset the user setting cache so the system will be forced to repull from the central database. |
| [Open User Folders](/wIndex/SettingsCache.html#opening-the-folders) | Click Execute to open the folders for user application data, client shared data and report file cache. |
| [Apply Special Features](/wIndex/Diagnostics-SpecialFeatures.html) | This allows a user to enable special features that may be needed for their environment.<br><br>Codes to use:<br>Workaround for Microsoft Animations Bug: BugFix1=ON or BugFix1=OFF <br>Workaround for Microsoft Repaint Bug: BugFix2=ON or BugFix2=OFF <br> Macro security features must be setup in the Portal Website or through Interject Support |

### System Tools

The System Tools involve various systems settings.

![](/images/Diagnostics/SystemTools2.png)
<br>

| Setting | Description |
|----|----|
| List DataPortals | Click Execute Selected Action to show the DataPortal List for the active user.  |
| Toggle Double Click Events | Click 'Execute Selected Action' to enable or disable the Interject_DoubleClick custom property in the current workbook [TestsTypes.xlsx].  By setting to true it will enable the double click events for the drill. The in-memory setting is set to False. |
| [Set RunOnOpen For Workbook](/wGetStarted/L-Create-RunOnOpen.html#setting-up-run-on-open-via-diagnostics) | Click 'Execute Selected Action' to enable or disable the Interject_RunOnOpen custom property in the current workbook [TestsTypes.xlsx].  By setting this property the workbook can automatically pull data when opened.<br><br>Input allowed:<br>No input will toggle between true and false. True will pull data on the activesheet when opened.<br>'Prompt' = will show Pull Data form when file is opened.<br>'T:Sheet1\|F:!A5' = will pull data for the tab Sheet1 but will exclude A5 from the report action, but will run the rest.<br>'F:A5' = will pull data for the active sheet for only the report formula in cell A5.<br>'T:Sheet1' = will pull data for the tab Sheet1 for all report formulas.<br>'RunOnce,T:Sheet1' = Will do the same as above, but the setting will be cleared afterwards.<br>'T:Sheet1,T:Sheet2\|F:CellName' = will pull for all of Sheet1, then pull for Sheet2 but for only the report formulas in the range name 'CellName'.<br><br>To test various settings against the current workbook, and view a sample execution plan, use: 'Test=' and then the instructions<br>    Test= T:Sheet1\|F:A5'  <br>    Test= true  <br>    Test= T:Sheet1  <br>    Test= F:A5  <br>    ... then click Execute Selected Action|
| Toggle Log Truncation | Click 'Execute Selected Action' to Enable or Disable the truncation of logs. |
| Reset Settings Cache - All Users | This will mark all users in the client to repull their settings cache from the central database at the next opportunity.  Only users with the ClientAdmin role can execute this action. |
| Reset File Cache | This will remove all files that were previously downloaded and cached as well as reset the users settings cache. |
| Open Application Folders | Click Execute to open the folders for AppData, UserData, and UserConfig<br>Click once installations use a subdirectory of: C:\Users\MyUserName\AppData\Local\Apps\2.0 |
| Set Enterprise Connection | Paste a Connection String in the Input box. Click Execute Selected Action to save this connection string encrypted for use in Enterprise installations. To clear the connection string, leave the 'Input' box empty and then Execute.  If 'Encrypted:' is shown at the start of the connection string, it is currently stored encrypted.<br>Example: "server=My_Server_Name;database=My_Database_Name;integrated security=true";<br>or "server=My_Server_Name;database=My_Database_Name;User Id=myUsername;Password=myPassword;" |
| Reset Cursor | Click 'Execute Selected Action' to reset a wait cursor that has not reset properly. |
| Open Install Configuration | Click Execute Action to open the configuration window |
| Force Garbage Collector on Dead Memory | Click Execute to clear unused RAM memory (aka Garbage Collection) |
| Find All Workbook Formulas | Click 'Execute Selected Action' to Find all formulas in the active workbook. |
| Replace Data Portal Codes | Click 'Execute Selected Action' to Replace all DataPortalCodes in the current workbook<br>input text should contain<br>oldName_One = NewName_One<br>anotherOldName = anotherNewName |

### Support

The Support tools involve tools that support the Interject/Excel environment.

![](/images/Diagnostics/Support2.png)
<br>

| Setting | Description |
|----|----|
| Clear Data Cell Cache | This will clear the Data Cells cache in memory.  It is used for troubleshooting only. |
| [Change ShortKey](/wIndex/Diagnostics-ShortKey.html) | Allows you to reassign a shortkey. After a shortkey is reassigned you must close and reopen Excel.<br><br>Changes create configurations to your local IdsSettings.xml file such as<br><ShortkeyChanges>True</ShortkeyChanges><br><ReportLibrary>Ctrl+Shift+A</ReportLibrary>.<br><br>Input reassignments here such as 'ReportLibrary=Ctrl+Shift+A'.<br>To disable or re-enable all shortkey reassignments input 'DisableAll' or 'EnableAll'<br>Currently shortkey reassignments are enabled.<br>Allows for multiple lines of commands to be input. |
| Clear Error Log | Click Execute Selected Action to clear the error log at C:\Users\<YourName>\AppData\Local\Interject\Settings\ErrorLog.xml. |
| Re-Initiate Interject | Click Execute Selected Action to make sure that basic setup information is in place for Interject to run. If Interject has already been initiated, this process will reset and clear certain settings. |
| Set Application Data Source | Click Execute Selected Action to set Interject's application data source. NOTE: Which data sources are available to you will depend on your Interject subscription. Possible sources are:<br>EnterpriseDatabase<br>InterjectPlatform |
| Launch the License Management Form | Click Execute Selected Action to open the License management form. |
