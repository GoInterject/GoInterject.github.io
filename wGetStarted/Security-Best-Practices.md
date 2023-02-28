---
title: Security Best Practices
layout: custom
---
* * *

##  **Overview**

Managing security is a key component of the Interject platform, and there are several areas to understand. Security involves both the row level security that can exist in reports and apps and how the middle tier objects are secured. Security also includes which spreadsheet report template can be seen by which users. The paragraphs below discuss each of these areas, best practices in building, and methods to test user access.

###  Database Connections and Windows Authentication 

When setting up Data Connections to connect to a database it is best to use connection strings that use windows authentication instead of a username and password. Although Interject encrypts the connection string value when saved, it is better practice to use a custom website API when a username and password must be used for a database connection. 

###  Row Level Security for Reports and Apps 

The Interject platform connects the spreadsheet interface to a middle-tier and makes the request under the user context of the session. In this way, a stored procedure can leverage Windows authentication to identify the user. In SQL Server the function to retrieve the username is sysname(). Other database engines that support windows authentication will have other methods. Windows authentication can also be used for website API that connects to Interject over SSL using standard coding practices. 

Using a stored procedure and windows authentication, built in row level security features of a database, such as SQL Server, can be used. 

In addition to leveraging windows authentication to identify the user, Interject can pass user identity information along with each request to the middle tier. This is useful if windows authentication is not available. If a data portal is configured with the following system parameters, select user context will be provided to each request to the data portal. 

System Parameters Related to User Identity:   
  
<table>  
<tr>  
<th>

Parameter 
</th>  
<th>

Description 
</th> </tr>  
<tr>  
<td>

@Interject_NTLogin  
</td>  
<td>

Windows authentication user name (Domain excluded)  
</td> </tr>  
<tr>  
<td>

@Interject_LoginName  
</td>  
<td>

Interject user name logged in  
</td> </tr>  
<tr>  
<td>

@Interject_UserID  
</td>  
<td>

Interject user id  
</td> </tr>  
<tr>  
<td>

@Interject_ClientID  
</td>  
<td>

The client id that is current in the Interject addin. Note that Company and Client may be used interchangeably.  
</td> </tr>  
<tr>  
<td>

@Interject_RequestContext  
</td>  
<td>

Is XML that includes a UserContext node as illustrated below  
</td> </tr> </table>

  


```XML

<UserContext>

<MachineLoginName>jeffh</MachineLoginName>

<MachineName>.</MachineName>

<FullName> </FullName>

<UserId>UohmLThif</UserId>

<ClientId>HKdmUuWT</ClientId>

<LoginName>user@email.com</LoginName>

<LoginAuthTypeId>10</LoginAuthTypeId>

<LoginDateUtc>04/20/2018 2:04:34</LoginDateUtc>

<UserRoles 

<Role>ClientAdmin</Role>

</UserRoles>

</UserContext>
```

When the above system parameters are used, it is important for the middle tier object to be configured to receive it. Stored procedures must have the additional parameters added or Interject will show an error to the user when pulling the report. Using an API as a middle tier will not likely create an error when additional parameters are added. Since you control the code for an API, you would need to add additional code in the API before the additional parameters would be utilized. 

It is critical to note that it is best practice that stored procedures be configured with **execute** rights for the network group of users that will be using the report. This is so the data tables can be hidden to the users, and their only access is through the stored procedures used in data portals. This configuration, however, provides opportunity for a knowledgeable IT users to execute the procedure with different parameters including user context. For this reason, it is best practice to verify the user context when using windows authentication for stored procedures. 

An additional user token is provided by Interject when the Data Portal connects to a website API. The token can be used by the website API to verify the identity of the user against the Interject Authorization API. The use of this token will be described further in the **Using an API with Interject** example that is currently under construction. 

In addition to the UserContext node above, there is a node in the data portal parameter @Interject_RequestContext. The XML node  <UserContextEncrypted></UserContextEncrypted> can be leveraged to trust the user context provided by the data portal parameters. This feature is not enabled, but when available will provide will allow use of client encryption keys and common encryption practices to parse the content. 

When considering all the above regarding row level security, you have the ability to specifically identify the user for every data transaction going through the Interject Platform. This identity that can be leveraged in your middle tier code, stored procedure or website API, to be aware of the user’s row level security. 

###  Template Security 

The spreadsheet files themselves act as reports or application templates. These files are normally uploaded to the Interject Report Library where they are versioned and unable to be changed without the proper Interject security roles. The Report Library was built to contain empty templates where users pull their data after opening the file template. Due to this design, the allowed file size that can be uploaded to the Report Library is 30 MB in size. When reports or apps are opened from the Report Library, they are locally cached and opened in read only mode. The user will in most cases use the template and when done will close the file without saving. 

The user may choose to save a copy of the file, such as for auditing purposes or to add personalized changes. It is by design to allow this, even though the user takes the risk of having an outdated version. To assist in management of older versions, Interject does log activity, including the file path and name, so the locations of these copies are known. 

The Report Library is built to provide a development cycle status to the report to help with vetting and documenting the approval of new reports. The statuses include, **In Development**, **In Test**, **Live**. See [ Report Library ](/wPortal/INTERJECT-Ribbon-Menu-Items.html) for additional information on using the Report Library. The ability to see templates in each status is controlled through Interject user roles. Standard users only see templates that are set to **Live**. 

It is best practice to consider the spreadsheet template insecure, since it can easily be shared with other users without proper credentials. Building each report or application with row level security is key to keeping security around your data. 

The Report Library has folders where templates are placed, and there is currently only one folder (called **Corporate** ) that has visibility rights for users that have been given the Corporate role. Although it is best practice for every report to have row level security, we recognized it may be advantageous to keep some reports out of view from users when they have no use for them. It is on the road map to provide additional visibility controls to all Report Library folders. 

###  Testing User Access 

As with all developed applications and row level reports, the testing plan should be built in based on the requirements. In many cases an end-user will want to verify the row level security code is properly implemented. 

A best practice method to handle this situation is to add a dataportal parameter such as **@UserTestMode**. In the middle tier code, the existence of a value provided can trigger the following code steps: 

**Step 1:** Using windows authentication or verifying the user token in an API, check to be sure the user can test another user’s security context. This may be hard coded in the middle tier code, can use a lookup list in a database, or even better, verify the correct group in active directory. 

**Step 2:** Next, verify the value provided in @UserTestMode represents a valid user. 

**Step 3:** If the user is allowed to test another user’s security context, change switch the identity so the row level security code is using the identity from @UserTestMode. This operation may be logged for later audit purposes. 

**Step 4:** In some cases in production, enabling this test mode can be helpful to a support team but the ability to save data changes (if provided in the app) should be prohibited. 

It is recognized the above will not work if row level security is using the database engine row level security features based on windows authentication. In this case other test methods must be implemented. 

  


  


  


  


  


  


  


  


  

