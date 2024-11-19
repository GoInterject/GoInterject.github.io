---
title: Data Portals
filename: "Data-Portals.md"
layout: custom
keywords: [data portals, data connection, setup, parameters, input, output, system parameters]
headings: ["Overview", "Setting up a Data Portal", "Overview of Parameters", "Formula Parameters", "System Parameters", "Adding New Parameters", "System Parameters Options"]
links: ["/wIndex/ReportBuilder.html", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#custom-commands", "/wIndex/ReportBuilder.html", "https://docs.gointerject.com/wDeveloper/Request-Context-Parse.html"]
image_dir: "DataPortals"
images: [
    {file: "NewDataPortalButton", type: "png", site: "Portal", cat: "Data Portals", sub: "", report: "", ribbon: "", config: ""}, 
    {file: "01", type: "jpg", site: "Portal", cat: "Data Portals", sub: "Details", report: "", ribbon: "", config: ""}, 
    {file: "02", type: "jpg", site: "Portal", cat: "Data Portals", sub: "Details", report: "", ribbon: "", config: ""}, 
    {file: "03", type: "jpg", site: "Portal", cat: "Data Portals", sub: "Details", report: "", ribbon: "", config: ""}, 
    {file: "04", type: "jpg", site: "Portal", cat: "Data Portals", sub: "Details", report: "", ribbon: "", config: ""}, 
	{file: "ParameterFlow", type: "png", site: "External", cat: "Flow Chart", sub: "Input/Output Parameters", report: "", ribbon: "", config: ""},
	{file: "ParamsInReport", type: "png", site: "Excel", cat: "Report", sub: "", report: "Customer Aging Detail", ribbon: "", config: ""},
	{file: "ParamsInPortal", type: "png", site: "Portal", cat: "Data Portals", sub: "Details", report: "", ribbon: "", config: ""},
	{file: "ParamsInProcedure", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""},
    {file: "05", type: "jpg", site: "Portal", cat: "Data Portals", sub: "Details", report: "", ribbon: "", config: ""}, 
    {file: "06", type: "jpg", site: "Portal", cat: "Data Portals", sub: "Details", report: "", ribbon: "", config: ""}, 
    {file: "07", type: "jpg", site: "Portal", cat: "Data Portals", sub: "Details", report: "", ribbon: "", config: ""}, 
    {file: "08", type: "jpg", site: "Portal", cat: "Data Portals", sub: "Details", report: "", ribbon: "", config: ""}, 
    {file: "09", type: "jpg", site: "Portal", cat: "Data Portals", sub: "Details", report: "", ribbon: "", config: ""}
    ]
description: A Data Portal uses a Data Connection to connect to either a stored procedure within a database or to a website API controller in a customer website API.
---
* * *

## Overview

A Data Portal uses a Data Connection to connect to either a stored procedure within a database or to a website API controller in a customer website API. In this section, you will quickly set up a Data Portal for a database to pull data into our spreadsheet.
Setting up a Data Portal to connect to a website API is not covered in this documentation yet as the sections are currently under construction. Please contact us directly for assistance with Website APIs.

### Setting up a Data Portal

**Step 1** : To setup a Data Portal click on the **Data Portals** button.

![](/images/DataPortals/NewDataPortalButton.png)
<br>

**Step 2** : In the Data Portals page, select the **New Data Portal** button in the top right corner.

The new page will look like below:

![](/images/DataPortals/01.jpg)
<br>

**Step 3** : The Data Portal Details page will contain the following information for the new data portal:

- **Data Portal Code** : A unique name used when setting up report formulas. At this time this is a unique name across the Interject community.
- **Description (optional)** : Description of what the Data Portal is doing
- **Category (optional)** : Text that can be used to group Data Portals for easy searches later.

![](/images/DataPortals/02.jpg)
<br>

- **Connection** : Data Connection that will be used for connecting to the database or API. Website provides a dropdown of data connections that have been created.
- **Command Type** : The type of command that will be executed. By default, the Data Portal uses the **Stored Procedure Name** command option. This field is not required for Data Portals using an API connection.
- **Stored Procedure / Command** : Full name (including schema) of stored procedure to be executed by this Data Portal. This field is not required for Data Portals connecting to an API connection. Since this field is part of the request object that is provided to an API, the developer can choose to use it within the API they create.

![](/images/DataPortals/03.jpg)
<br>

- **Api Relative Url** : This setting indicates the rest of the API URL that will be concatenated with the root URL of an API Data Connection when a request is sent. For example, the root URL for the connection may be **https:[api.myapi.com]** . If your API controller name is CustomerData, then you would type **\CustomerData** in API Relative URL. The API request would be sent to **https:[api.myapi.com]\CustomerData**. This field is ignored when a Data Portal uses a database connection.
- **Helper Default Columns (optional)** : You can use a comma delimited list to set default columns that will appear when a new report is created using the [Report Builder](/wIndex/ReportBuilder.html).
- **Is Custom Command** : When set to yes, allows background jobs to run from the Custom Commands Window. Custom Commands require specific parameters to work with the Custom Commands window. See the [Interject Ribbon](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#custom-commands) on how to use Custom Commands.

![](/images/DataPortals/04.jpg)
<br>

### Overview of Parameters

Parameters are an important feature of Data Portals. Interject can send input parameters from the Excel report to the Stored Procedure through the use of Data Portals. Output parameters can also be sent from the Stored Procedure to Interject to be displayed in the Excel report.

The following diagram describes the flow of parameters to and from the data source:

![](/images/DataPortals/ParameterFlow.png)
<br>

There are two types of Interject parameters: Formula parameters and System parameters.

### Formula Parameters

Formula Parameters are passed into the Data Portal from the user inputs in the spreadsheet report or app. In setting up a spreadsheet using Report Formulas, each parameter input can be assigned to a spreadsheet cell so they are passed with the data request. Parameters are often used as filters but can be used for other things as well, depending on the imagination of the developer. They can determine the order that data is returned, or they can be output parameters that are returned from the data request. They are building blocks to create a useful experience to the end users.

The parameters must match in name in the Data Portal and the Stored Procedure. In addition, the order of the parameters must match between the report and the Data Portal.

Parameters in Report:

![](/images/DataPortals/ParamsInReport.png)
<br>

Parameters in Portal:

![](/images/DataPortals/ParamsInPortal.png)
<br>

Parameters in Stored Procedure:

![](/images/DataPortals/ParamsInProcedure.png)
<br>

### System Parameters

System Parameters are automatically passed into the Data Portal from the Interject Add-In. They are not considered in the Report Formulas since they are only passing user content data. Choose from a list of pre-configured system parameter types but note the data type that is shown. When adding the System Parameters to a stored procedure or website API, matching the data type is important.

### Adding New Parameters

Now that the Data Portal is created, you can set up our parameters for the Data Portal. These parameters correlate to the name of the parameters in the stored procedure. If a custom data API is used, the API will be coded to expect the specific parameter name.
**Step 1** : To add a Formula Parameter click on the **Click here to add a Formula Parameter** button.

![](/images/DataPortals/05.jpg)
<br>

**Step 2** : The input fields for the new Formula Parameter will be shown:

1. **Name** : name of parameter in stored procedure or API
2. **Type** : data type of parameter
3. **Direction** : configure the parameter as an input parameter or an output parameter that will be returned to the spreadsheet

![](/images/DataPortals/06.jpg)
<br>

**Step 3** : The **More** button can be used to show optional inputs. You can set a default value or the datatype length if it is required. You can also set additional fields that will be used with Report Builder. These Report Builder fields are used to help easily create a report within Excel based on a Data Portal. Below is a description of the fields:

- **Helper Name** : This adds a friendly name for the report parameter input in the Report Builder. Otherwise the parameter name is used, which has no spaces.
- **Helper Default** : This inserts a default value into the cell of the Excel report when using the Report Builder.
- **Options** : Use a comma separated list to provide the Excel user with a drop down list of options.
- **Comments** : This inserts an Excel comment, with our text, into the cell of the Excel report when using the Report Builder.

 To see how these fields are used when setting up a report, see [Report Builder](/wIndex/ReportBuilder.html).

![](/images/DataPortals/07.jpg)
<br>

**Step 4** : Once done defining a parameter, you can click on the save icon to save the changes.

**Step 5** : To add a System Parameter, click on the **Click here to add a System Parameter** button.

![](/images/DataPortals/08.jpg)
<br>

**Step 6** : Repeat the previous steps to add additional parameters as needed. 

<blockquote class=highlight_note>
<b>Note:</b> The order in which you add the Formula Parameters must match the order in the Param() formula used in the spreadsheet Report Formula.
</blockquote>
<br>

![](/images/DataPortals/09.jpg)
<br>

The Data Portal is now ready to be used with Report Builder and within Interject Report formulas.

### System Parameters Options

There are a number of options that can be used as system parameters. The list below provides a quick summary of the options:

| Name | Data Type | Description |
|-----|-----|-----|
| Interject_XMLDataToSave | varchar(max) | Required for saving data. It contains XML for the designated cells values | 
| Interject_ColDefItems | varchar(max) | Provides the Column Definitions in XML designated within the report formula. |
| Interject_RowDefItems | varchar(max) | Provides the Row Definitions in XML designated within the report formula. |
| Interject_SourceFileAndPath | varchar(500) | Provides the path and file name delimited by \| of the current file | 
| Interject_SourceFilePathAndTab | varchar(1000) | Provides the path, file name and active tab name delimited by \| of the current file. |
| Interject_NTLogin | varchar(50) | Provides the user’s computer login name for their current session. |
| Interject_UserID | varchar(50) | Provides the Interject User ID for their current session. |
| Interject_ClientID | varchar(50) | Provides the Interject Client ID for their current session. |
| Interject_LoginName | varchar(50) | Provides the Interject username for their current session. |
| Interject_ExcelVersion | varchar(50) | Provides the users Excel version. |
| Interject_UserRoles | varchar(1000) | Provides the Interject roles assigned to the user. |
| Interject_LocalTimeZoneOffset | money | Provides a number (0.000) that represents that offset of the user’s time to UTC time. |
| Interject_ReturnError | varchar(2000) | Is an output parameter that can be used to return an error back to the user. Pass empty string for no error. |
| <a href="https://docs.gointerject.com/wDeveloper/Request-Context-Parse.html">Interject_RequestContext</a> | nvarchar(max) | Provides all above request context and both the open text and encrypted version of the user context. |