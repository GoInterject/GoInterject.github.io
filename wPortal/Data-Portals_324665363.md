---
title: Data Portals
layout: custom
---

## **Overview**
---
A Data Portal uses a Data Connection to connect to either a stored procedure within a database or to a website API controller in a customer website API. In this section, you will quickly set up a Data Portal for a database to pull data into our spreadsheet.  
Setting up an Data Portal to connect to a website API is not covered in this documentation yet as the sections are currently under construction. Please contact us directly for assistance with Website APIs.

### Setting Up a Data Portal

**Step 1** : To setup a Data Portal click on the **Data Portals** icon.  
**Step 2** : In the Data Portals page, select the **New Data Portal** button in the top right corner.

![](attachments/324665363/328270037.jpg)

The new page will look like below

![](attachments/324665363/328335738.jpg)

**Step 3** : The Data Portal Details page will contain the following information for the new data portal:

- **Data Portal Code** : A unique name used when setting up report formulas. At this time this is a unique name across the INTERJECT community.
- **Description (optional)** : Description of what the Data Portal is doing
- **Category (optional)** : Text that can be used to group Data Portals for easy searches later.

![](attachments/324665363/328302932.jpg)

- **Connection** : Data Connection that will be used for connecting to the database or API. Website provides a dropdown of data connections that have been created.
- **Command Type** : The type of command that will be executed. By default, the Data Portal uses the **Stored Procedure Name** command option. This field is not required for Data Portals using an API connection.
- **Stored Procedure / Command** : Full name (including schema) of stored procedure to be executed by this Data Portal. This field is not required for Data Portals connecting to an API connection. Since this field is part of the request object that is provided to an API, the developer can choose to use it within the API they create.

![](attachments/324665363/328532271.jpg)

- **Api Relative Url** : This setting indicates the rest of the API URL that will be concatenated with the root URL of an API Data Connection when a request is sent. For example, the root URL for the connection may be **https:\\\[ api.myapi.com ](http://api.myapi.com) ** . If your API controller name is CustomerData, then you would type **\CustomerData** in API Relative URL. The API request would be sent to **https:\\\[ api.myapi.com ](http://api.myapi.com) \CustomerData ** . This field is ignored when a Data Portal uses a database connection.
- **Helper Default Columns (optional)** : You can use a comma delimited list to set default columns that will appear when a new report is created using the Report Builder.
- **Is Custom Command** : When set to yes, allows background jobs to run from the Custom Commands Window. Custom Commands require specific parameters to work with the Custom Commands window. See the [ INTERJECT Ribbon ](/wPortal/INTERJECT-Ribbon-Menu-Items_83689479.html) on how to use Custom Commands

![](attachments/324665363/328532276.jpg)

### Overview of Parameters

Parameters are an important feature of Data Portals. There are two types, Formula and System Parameters.

### Formula Parameters

Formula Parameters are passed into the Data Portal from the user inputs in the spreadsheet report or app. In setting up a spreadsheet using Report Formulas, each parameter input can be assigned to a spreadsheet cell so they are passed with the data request. Parameters are often used as filters but can be used for other things as well, depending on the imagination of the developer. They can determine the order that data is returned, or they can be output parameters that are returned from the data request. They are building blocks to create a useful experience to the end users.

### System Parameters

System Parameters are automatically passed into the Data Portal from the INTERJECT Add-In. They are not considered in the Report Formulas since they are only passing user content data. Choose from a list of pre-configured system parameter types but note the data type that is shown. When adding the System Parameters to a stored procedure or website API, matching the data type is important.

### Adding New Parameters

Now that the Data Portal is created, you can set up our parameters for the Data Portal. These parameters correlate to the name of the parameters in the stored procedure. If a custom data API is used, the API will be coded to expect the specific parameter name.  
**Step 1** : To add a Formula Parameter click on the **Click here to add a Formula Parameter** button.

![](attachments/324665363/328302950.jpg)

**Step 2** : The input fields for the new Formula Parameter will be shown:

1. **Name** : name of parameter in stored procedure or API
2. **Type** : data type of parameter
3. **Direction** : configure the parameter as an input parameter or an output parameter that will be returned to the spreadsheet

![](attachments/324665363/328270037.jpg)

**Step 3** : The **More** button can be used to show optional inputs. You can set a default value or the datatype length if it is required. You can also set additional fields that will be used with Report Builder. These Report Builder fields are used to help easily create a report within Excel based on a Data Portal. Below is a description of the fields:

- **Helper Name** : This adds a friendly name for the report parameter input in the Report Builder. Otherwise the parameter name is used, which has no spaces.
- **Helper Default** : This inserts a default value into the cell of the Excel report when using the Report Builder.
- **Options** : Use a comma separated list to provide the Excel user with a drop down list of options.
- **Comments** : This inserts an Excel comment, with our text, into the cell of the Excel report when using the Report Builder.  
  To see how these fields are used when setting up a report using Report Builder click here. (You will not be using any of these inputs in this example. )

![](attachments/324665363/328565027.jpg)

**Step 4** : Once done defining a parameter, you can click on the save icon to save the changes.

**Step 5** : To add a System Parameter, click on the **Click here to add a System Parameter** button.

![](attachments/324665363/328302964.jpg)

**Step 6** : Repeat the previous steps to add additional parameters as needed. Note: The order in which you add the Formula Parameters must match the order in the Param() formula used in the spreadsheet Report Formula.  
![](attachments/324665363/328565032.jpg)

The Data Portal is now ready to be used with Report Builder and within INTERJECT Report formulas.

### System Parameters Options

There are a number of options that can be used as system parameters. The list below provides a quick summary of the options

<table>  
  <tr>  
    <th>
    Name 
    </th>  
    <th>
    Data Type 
    </th>  
    <th>
    Description 
    </th> 
  </tr>  
  <tr>  
    <td>
    Interject_XMLDataToSave 
    </td>  
    <td>
    varchar(max)
    </td>  
    <td>
    Required for saving data. It contains XML for the designated cells values
    </td> 
  </tr>  
  <tr>  
<td>

Interject_ColDefItems

</td>  
<td>

varchar(max)

</td>  
<td>

Provides the Column Definitions in XML designated within the report formula.

</td> </tr>  
<tr>  
<td>

Interject_RowDefItems

</td>  
<td>

varchar(max)

</td>  
<td>

Provides the Row Definitions in XML designated within the report formula.

</td> </tr>  
<tr>  
<td>

Interject_SourceFileAndPath

</td>  
<td>

varchar(500)

</td>  
<td>

Provides the path and file name delimited by '|' of the current file

</td> </tr>  
<tr>  
<td>

Interject_SourceFilePathAndTab

</td>  
<td>

varchar(1000)

</td>  
<td>

Provides the path, file name and active tab name delimited by '|' of the current file.

</td> </tr>  
<tr>  
<td>

Interject_NTLogin

</td>  
<td>

varchar(50)

</td>  
<td>

Provides the user’s computer login name for their current session.

</td> </tr>  
<tr>  
<td>

Interject_UserID

</td>  
<td>

varchar(50)

</td>  
<td>

Provides the INTERJECT User ID for their current session.

</td> </tr>  
<tr>  
<td>

Interject_ClientID

</td>  
<td>

varchar(50)

</td>  
<td>

Provides the INTERJECT Client ID for their current session.

</td> </tr>  
<tr>  
<td>

Interject_LoginName

</td>  
<td>

varchar(50)

</td>  
<td>

Provides the INTERJECT username for their current session.

</td> </tr>  
<tr>  
<td>

Interject_ExcelVersion

</td>  
<td>

varchar(50)

</td>  
<td>

Provides the users Excel version.

</td> </tr>  
<tr>  
<td>

Interject_UserRoles

</td>  
<td>

varchar(1000)

</td>  
<td>

Provides the INTERJECT roles assigned to the user.

</td> </tr>  
<tr>  
<td>

Interject_LocalTimeZoneOffset

</td>  
<td>

money

</td>  
<td>

Provides a number (0.000) that represents that offset of the user’s time to UTC time.

</td> </tr>  
<tr>  
<td>

Interject_ReturnError

</td>  
<td>

varchar(2000)

</td>  
<td>

Is an output parameter that can be used to return an error back to the user. Pass empty string for no error.

</td> </tr>  
<tr>  
<td>

Interject_RequestContext

</td>  
<td>

nvarchar(max)

</td>  
<td>

Provides all above request context and both the open text and encrypted version of the user context.

</td> </tr> </table>
