---
title: Custom Items
filename: "CustomItems.md"
layout: custom
keywords: [custom commands, execute, sql]
headings: ["Overview", "Setup Data Portal", "System Parameters", "Formula Parameters", "Description and Status", "Running the Custom Item", "Example Stored Procedure"]
links: ["/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#custom-commands", "https://docs.gointerject.com/wPortal/INTERJECT-Roles.html#clientadmin-role", "https://docs.gointerject.com/wPortal/INTERJECT-Roles.html#customitems-role", "/wPortal/Data-Portals.html", "https://docs.gointerject.com/wPortal/Data-Portals.html#system-parameters-options", "/wPortal/Data-Portals.html#overview-of-parameters"]
image_dir: "CustomItems"
images: [
	{file: "CustomItems", type: "png", site: "Add-in", cat: "Custom Commands", sub: "Custom Items", report: "", ribbon: "", config: ""}, 
	{file: "IsCustomCommand", type: "png", site: "Portal", cat: "Data Portals", sub: "Details", report: "", ribbon: "", config: ""}, 
	{file: "SystemParameters", type: "png", site: "Portal", cat: "Data Portals", sub: "Details", report: "", ribbon: "", config: ""}, 
	{file: "FormulaParameterMore", type: "png", site: "Portal", cat: "Data Portals", sub: "Details", report: "", ribbon: "", config: ""}, 
	{file: "FormulaParameterDefault", type: "png", site: "Portal", cat: "Data Portals", sub: "Details", report: "", ribbon: "", config: ""}, 
	{file: "Prompt", type: "png", site: "Add-in", cat: "Popup", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "GettingDescriptionStatus", type: "png", site: "Add-in", cat: "Custom Commands", sub: "Custom Items", report: "", ribbon: "", config: ""}, 
	{file: "CustomItemsInformation", type: "png", site: "Add-in", cat: "Custom Commands", sub: "Custom Items", report: "", ribbon: "", config: ""}
	]
description: The Custom Item feature of Interject allows a user to interact with a database stored procedure or web service to trigger an event.  It could be used to trigger a special data update process, toggle a switch such as temporarily turning off a report tool for standard users, or running a data maintenance routine.
---
* * *

## Overview

The Custom Item feature of Interject is a [Custom Command](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#custom-commands) that allows a user to interact with a database stored procedure or web service to trigger an event.  It could be used to trigger a special data update process, toggle a switch such as temporarily turning off a report tool for standard users, or running a data maintenance routine.

<blockquote class=highlight_note>
<b>Note:</b> The user must have either the <a href="https://docs.gointerject.com/wPortal/INTERJECT-Roles.html#clientadmin-role">ClientAdmin</a> or <a href="https://docs.gointerject.com/wPortal/INTERJECT-Roles.html#customitems-role">CustomItems</a> role to execute a custom command.
</blockquote>
<br>

![](/images/CustomItems/CustomItems.png)
<br>

### Setup Data Portal

When a [Data Portal](/wPortal/Data-Portals.html) is set up as a custom command, it will show up in the Custom Items tab. In order to designate the Portal as a custom item, ensure the **Is Custom Command?** checkbox is selected when creating the Portal.

![](/images/CustomItems/IsCustomCommand.png)
<br>

### System Parameters

After creating the Custom Command Data Portal, there are 4 system parameters that are automatically added:

![](/images/CustomItems/SystemParameters.png)
<br>

* **`Interject_CommandExecute`:** This variable is used to distinguish between displaying the description and status of the custom item and actually executing the command (see [Description and Status](#description-and-status) and [Running the Custom Item](#running-the-custom-item) for more info)

* **`Interject_CommandResult`:** Provides the results of the execution

* **`Interject_CommandDescription`:** Shows a description to the user in the Custom Items form (displays Data Portal name if not used)

* **`Interject_CommandStatus`:** Return a status such as details from the last time it was run. Interject will use this variable to display the status of the custom item.

<br>
<blockquote class=highlight_note>
<b>Note:</b> Any other <a href="https://docs.gointerject.com/wPortal/Data-Portals.html#system-parameters-options">System Parameter</a> can be set up for a Custom Item Data Portal and used in the Stored Procedure. For security, the Data Portal can be setup to use reserved Interject parameter names that can pass system information such as user identity, user time zone information, or user Interject roles.  In this way, further security requirements can be handled.
</blockquote>

### Formula Parameters

You can enter any [formula parameters](/wPortal/Data-Portals.html#overview-of-parameters) for your Data Portal. By clicking **More** you can set up additional details about the parameter:

![](/images/CustomItems/FormulaParameterMore.png)
<br>

Here you can set up a default prompt for the user to enter the parameter value to be sent to the Data Portal. This is achieved by entering a question mark `?` before the default text:

![](/images/CustomItems/FormulaParameterDefault.png)
<br>

When running the custom item, Interject will prompt the user for input:

![](/images/CustomItems/Prompt.png)
<br>

### Description and Status

When the **Custom Items** tab or **Refresh** button is selected, Interject automatically executes the custom items and sends the `Interject_CommandExecute` parameter to the stored procedure with the value of 0. This can signal the stored procedure to only set the `Interject_CommandDescription` and `Interject_CommandStatus` parameters instead of actually executing the entire code. These parameters are output parameters that Interject displays in the Custom Commands form. When selected or refreshed, Interject will fetch the description and status:

![](/images/CustomItems/GettingDescriptionStatus.png)
<br>

### Running the Custom Item

The custom items are defined by the stored procedure or web service. When **Run Selected** is clicked, Interject will set the `Interject_CommandExecute` variable to 1, which signals the stored procedure to execute the entire code.

The event is ran asynchronously. The user can cancel the event by clicking the **Cancel Selected** button.  The user should not exit the Interject spreadsheet session until the event is completed or it will be automatically aborted.

### Example Stored Procedure

An example stored procedure can be obtained by clicking the **i** on the **Custom Items** tab:

![](/images/CustomItems/CustomItemsInformation.png)
<br>

For your convenience, the procedure is posted here:

<button class = "collapsible"> CustomItems_Example </button>
<div markdown="1" class="panel">

```sql
*/

ALTER PROC [demo].[CustomItems_Example]

	-- Example optional parameter. There are two ways to set an initial value 
	--     1) set the default value below and not setup the parameter in the data portals.  
	--     2) set a default value in the data portal setup.
	-- 
	-- If in #2 the default value starts with a question mark like "?Enter Year Month (YYYY-MM)", this will cause Interject
	-- on execute to ask the user to "Enter Year Month (YYYY-MM)".  This must be validated by the stored procedure or 
	-- web service
	@YearMonthToUpdate VARCHAR(10) = ''

	-- System Parameters Required
	,@Interject_CommandExecute BIT = 0 -- This tells this SP to execute the command instead of only returning description and status
	,@Interject_CommandResult VARCHAR(200) OUTPUT -- This provides the result of the execute.  it is limited to 200 characters.

	-- System Parameters Optional
	,@Interject_CommandDescription VARCHAR(200) OUTPUT -- Shows friendly description to user. Shows Data Portal name if parameter not used.
	,@Interject_CommandStatus VARCHAR(200) OUTPUT -- Will return a status such as details from the last time it was run.

	-- The below are examples of Interject reserved parameters 
	,@Interject_LocalTimeZoneOffset MONEY -- Provides a number (0.000) the represents that offset of the users time to UTC time.
	,@Interject_NTLogin VARCHAR(50) -- Provides the users computer login name for their current session.
	,@Interject_UserRoles VARCHAR(1000) -- Provides the Interject user roles for the user

	--@Interject_UserID VARCHAR(50) -- Provides the Interject User ID for their current session.
	--@Interject_LoginName VARCHAR(50) -- Provides the Interject Full name for their current session.
	--@Interject_ExcelVersion VARCHAR(50) -- Provides the Excel Version of the current session.
	--@Interject_ClientID VARCHAR(50) -- Provides the Interject Client ID for their current session.

AS


/*
==================================================================================
	CREATED DATE: 12/11/2023
	CREATED BY: Interject Default
	DESCRIPTION: Example data pull to be used with Interject

	TEST Example: Use the below to test this stored procedure:

	Declare @Interject_CommandResult as varchar(200)
	declare @Interject_CommandDescription varchar(200)
	declare @Interject_CommandStatus varchar(200)

	Execute demo.[CustomItems_Example]
		@YearMonthToUpdate = '2013-10'
		,@Interject_CommandExecute = 0  -- Change this to 1 for execute, 0 to only bring status
		,@Interject_CommandResult=@Interject_CommandResult out
		,@Interject_CommandDescription=@Interject_CommandDescription out
		,@Interject_CommandStatus=@Interject_CommandStatus out
		,@Interject_LocalTimeZoneOffset = -8
		,@Interject_NTLogin = 'samuelr'
		,@Interject_UserRoles = 'ClientAdmin'

	Select @Interject_CommandResult as '@Interject_CommandResult'
		,@Interject_CommandDescription as '@Interject_CommandDescription'
		,@Interject_CommandStatus as '@Interject_CommandStatus'

==================================================================================
*/

---
---Set description of this custom item
---
	SET @Interject_CommandDescription = 'Update Reporting Database'


---
--- Prepare to provide status 
---

---Get an example date of when the update was last performed so a status can be prepared
	DECLARE @LastUpdated DATETIME
	SET @LastUpdated=  dateadd(month,-1,getutcdate())  -- This uses UTC date since log data will typically not reflect a time zone
	SET @LastUpdated = dateadd(hour,@Interject_LocalTimeZoneOffset,@LastUpdated)  -- convert UTC date to user's time zone


---Set current status of this custom item
	DECLARE @LastUpdateYearMonth VARCHAR(7)

	SET @LastUpdateYearMonth =  CAST(YEAR(DATEADD(m,0,@LastUpdated)) AS VARCHAR(10)) 
			+ '-' + RIGHT(CAST(MONTH(DATEADD(m,0,@LastUpdated)) + 100 AS VARCHAR(4)),2)

	SET @Interject_CommandStatus = 'Month ''' + @LastUpdateYearMonth + ''' was updated on ' 
		+ LEFT(convert(varchar, @LastUpdated, 1),5)  + ' ' 
		+ ltrim(right(convert(varchar(25), @LastUpdated, 100), 7))


---
---Do more if this is an execute event
---
	IF @Interject_CommandExecute = 1
	BEGIN
		DECLARE @NewUpdateDate DATETIME
		SET @NewUpdateDate =  GETDATE()

	--
	--Handle the input parameters
	--

	--This example will specify the current month if no input is received
		IF @YearMonthToUpdate = '' 
		BEGIN

			SET @YearMonthToUpdate =  CAST(YEAR(DATEADD(m,0,@NewUpdateDate)) AS VARCHAR(10)) 
				+ '-' + RIGHT(CAST(MONTH(DATEADD(m,0,@NewUpdateDate)) + 100 AS VARCHAR(4)),2)
		END
		ELSE
		BEGIN

			--Validate to ensure input was a valid date
			IF isdate(right(@YearMonthToUpdate,2) + '/1/' + left(@YearMonthToUpdate,4)) = 0  
			BEGIN
				SET @Interject_CommandResult = 'The value entered ''' + @YearMonthToUpdate + ''' does not represent a valid date'
				RAISERROR (@Interject_CommandResult, 18,1) 
				RETURN
			END

		END

	--
	--Execute the update and return the result
	--
		BEGIN TRY
			WAITFOR DELAY '00:00:05' -- Wait for 5 seconds to simulate an actual update event

			-- Set result response
			SET @Interject_CommandResult = 'Updated month ''' + @YearMonthToUpdate + ''' successfully on '  
				+ LEFT(CONVERT(VARCHAR,@NewUpdateDate, 1),5)  + ' ' 
				+ LTRIM(RIGHT(CONVERT(VARCHAR(25), @NewUpdateDate, 100), 7))

			-- Redo status reponse based on the successful update
			SET @Interject_CommandStatus = 'Month ''' + @YearMonthToUpdate + ''' was updated on ' 
				+ LEFT(convert(varchar, @NewUpdateDate, 1),5)  + ' ' 
				+ ltrim(right(convert(varchar(25), @NewUpdateDate, 100), 7))

		END TRY
		BEGIN CATCH
				SET @Interject_CommandResult = 'Error: ' + Error_Message()
		END CATCH


	END
```
</div>
