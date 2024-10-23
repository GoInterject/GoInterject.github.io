---
title: Request Context Parse
filename: "Request-Context-Parse.md"
layout: custom
keywords: [request context, parse, system parameter, stored procedure, XML]
headings: ["Overview", "Procedure Variables", "The RequestContext_Parse Code", "Testing the Procedure", "An Example Using the Procedure"]
links: []
image_dir: ""
images: []
description: This page that lists the interject request context parse stored procedure
---
* * *

## Overview

The RequestContext_Parse stored procedure is used as a callable helper procedure when utilizing the Interject_RequestContext system parameter. It converts the XML nodes that are brought in by the system parameter into variable values. These variable values correspond to all the other system parameters that Interject offers.

### Procedure Variables

When a Data Portal is setup with the System Parameter "Interject_RequestContext", Interject will send context information which can be accessed and parsed to local variables in the the Stored Procedure or command:

| Variable | Data Type | Description |
|-----|-----|-----|
| ExcelVersion | nvarchar(100) | The version of Excel being used |
| IdsVersion | nvarchar(100) | The version of Interject being used |
| FileName | nvarchar(1000) | The name of the file |
| FilePath | nvarchar(1000) | The path of the file |
| TabName | nvarchar(1000) | The name of the Excel tab of the report formula |
| CellRange | nvarchar(100) | The cell reference of the report formula |
| SourceFunction | nvarchar(100) | The type of report formula |
| UtcOffset | decimal(6,4) | The number of hours UTC needs to offset to get to the current local time |
| ColDefItems | nvarchar(max) | A list of Column Definition items |
| ResultDefItems | nvarchar(max) | A list of Result Definition items |
| RowDefItems | nvarchar(max) | A list of Row Definition items |
| RowDefItems2 | nvarchar(max) | A list of Row Definition items that include a unique RowDefName |
| MachineLoginName | nvarchar(100) | The login name of the user |
| MachineName | nvarchar(100) | The name of the machine being used |
| FullName | nvarchar(100) | The full name of the user |
| UserId | nvarchar(100) | The User ID of the user |
| ClientId | nvarchar(100) | The Client ID of the user |
| LoginName | nvarchar(100) | The login name or email of the user |
| LoginAuthTypeID | int | &lt;Not used&gt; |
| LoginDateUTC | datetime | The UTC date and time of the user's login |
| UserRoles | nvarchar(max) | A list of roles of the user |
| UserContextEncrypted | nvarchar(4000) | &lt;Not used&gt; |
| XMLDataToSave | nvarchar(max) | The data from the report to be processed/saved |

### The RequestContext_Parse Code

<button class="collapsible">Get The Stored Procedure</button>
<div markdown="1" class="panel">

```sql

SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[RequestContext_Parse]') AND type in (N'P', N'PC'))
BEGIN
EXEC dbo.sp_executesql @statement = N'CREATE PROCEDURE [dbo].[RequestContext_Parse] AS' 
END
GO
/*************************************************************************
 * Interject DATA SYSTEMS, INC CONFIDENTIAL
 *
 *  © 2016 Interject Data Systems, Inc.
 *  All Rights Reserved.
 * 
 * NOTICE:  All information contained herein is, and remains the property of Interject Data Systems, Incorporated. 
 * The intellectual and technical concepts contained herein are proprietary to Interject Data Systems, Incorporated
 * and may be covered by U.S. and Foreign Patents, patents in process, and are protected by trade secret or copyright law.
 * Dissemination of this information or reproduction of this material is strictly forbidden unless prior written permission is obtained
 * from Interject Data Systems, Incorporated.
 */
/*
TEST CODE
declare 
	@Interject_RequestContext		nvarchar(max)
	,@ExcelVersion					nvarchar(100)	 
	,@IdsVersion					nvarchar(100)	 
	,@FileName						nvarchar(1000)	 
	,@FilePath						nvarchar(1000)	 
	,@TabName						nvarchar(1000)	 
	,@CellRange						nvarchar(100)	 
	,@SourceFunction				nvarchar(100)	 
	,@UtcOffset						decimal(6,4)	 
	,@ColDefItemsDelimited			nvarchar(max)	 
	,@ResultDefItemsDelimited		nvarchar(max)	
	,@RowDefItemsDelimited			nvarchar(max)	 
	,@MachineLoginName				nvarchar(100)	 
	,@MachineName					nvarchar(100)	 
	,@Interject_UserID				nvarchar(100)	 
	,@Interject_ClientID			nvarchar(100)	 
	,@Interject_LoginName			nvarchar(100)	 
	,@Interject_LoginAuthTypeID		int				 
	,@Interject_LoginDateUTC		datetime		 
	,@Interject_UserRolesDelimited	nvarchar(max)	 
	,@UserContextEncrypted			nvarchar(4000)	 
	,@Interject_XMLDataToSave		nvarchar(max)	 

set @Interject_RequestContext = 
'<?xml version="1.0" encoding="utf-16" standalone="yes"?>
<RequestContext>
    <ExcelVersion>14.0</ExcelVersion>
    <IdsVersion>2.2.5.13</IdsVersion>
    <FileName>Interject_TestFile (version 1).xlsb</FileName>
    <FilePath>C:\Users\jeffh-high\AppData\Roaming\Microsoft\Excel</FilePath>
    <TabName>DB_ReportRangeShort</TabName>
    <CellRange>C6</CellRange>
    <SourceFunction>Range</SourceFunction>
    <UtcOffset>7</UtcOffset>
    <ColDefItems></ColDefItems>
    <ResultDefItems>
        <Value>customerid</Value>
        <Value>companyname</Value>
	</ResultDefItems>
    <RowDefItems>
        <Value Row="1">customerid</Value>
        <Value Row="2">companyname</Value>
	</RowDefItems>
    <UserContext>
        <MachineLoginName>myusername</MachineLoginName>
        <MachineName> </MachineName>
        <UserId>jxR2bDnk4jg</UserId>	
        <ClientId>CKKCYyCtT</ClientId>
        <LoginName>my@email.com</LoginName>
        <LoginAuthTypeId>10</LoginAuthTypeId>
        <LoginDateUtc>06/16/2014 11:04:08</LoginDateUtc>
        <UserRoles>
            <Role>ClientAdmin</Role>
        </UserRoles>
    </UserContext>
    <UserContextEncrypted>KAJeycwLWiy0t4Xe4GxPiI0sskc=</UserContextEncrypted>
    <XMLDataToSave>
  <c Column="Row" OrigValue="Row" />
  <c Column="Start" OrigValue="Start" />
  <c Column="CodeInputs" OrigValue="CodeInputs" />
  <c Column="Description" OrigValue="Description" />
  <c Column="End" OrigValue="End" />
  <c Column="Duration" OrigValue="Duration" />
  <c Column="Client" OrigValue="Client" />
  <c Column="Code1" OrigValue="Code1" />
  <c Column="Code2" OrigValue="Code2" />
  <c Column="Code3" OrigValue="Code3" />
  <c Column="Code4" OrigValue="Code4" />
  <c Column="ChargeCategory" OrigValue="ChargeCategory" />
  <r>
    <Row>18</Row>
    <Start>0.291666666666667</Start>
    <CodeInputs>.ids.dev..</CodeInputs>
    <Description>upgrade timelook</Description>
    <End />
    <Duration>15.4</Duration>
    <Client>ids</Client>
    <Code1>dev</Code1>
    <Code2 />
    <Code3 />
    <Code4 />
    <ChargeCategory>NB</ChargeCategory>
  </r>
    </XMLDataToSave>
</RequestContext>
'
exec [dbo].[RequestContext_Parse]
	@Interject_RequestContext		= @Interject_RequestContext
	,@ExcelVersion					 = @ExcelVersion			 output
	,@IdsVersion					 = @IdsVersion				 output
	,@FileName						 = @FileName				 output
	,@FilePath						 = @FilePath				 output
	,@TabName						 = @TabName					 output
	,@CellRange						 = @CellRange				 output
	,@SourceFunction				 = @SourceFunction			 output
	,@UtcOffset						 = @UtcOffset				 output
	,@ColDefItemsDelimited			 = @ColDefItemsDelimited	 output
	,@ResultDefItemsDelimited		 = @ResultDefItemsDelimited	 output
	,@RowDefItemsDelimited			 = @RowDefItemsDelimited	 output
	,@MachineLoginName				 = @MachineLoginName		 output
	,@MachineName					 = @MachineName				 output
	,@Interject_UserID				 = @Interject_UserID		 output
	,@Interject_ClientID			 = @Interject_ClientID		 output
	,@Interject_LoginName			 = @Interject_LoginName		 output
	,@Interject_LoginAuthTypeID		 = @Interject_LoginAuthTypeID output
	,@Interject_LoginDateUTC		 = @Interject_LoginDateUTC	 output
	,@Interject_UserRolesDelimited	 = @Interject_UserRolesDelimited	output
	,@UserContextEncrypted			 = @UserContextEncrypted	 output
	,@Interject_XMLDataToSave		 = @Interject_XMLDataToSave			 output

Select
	@ExcelVersion					as '@ExcelVersion'
	,@IdsVersion					as '@IdsVersion'
	,@FileName						as '@FileName'
	,@FilePath						as '@FilePath '
	,@TabName						as '@TabName'
	,@CellRange						as '@CellRange'
	,@SourceFunction				as '@SourceFunction'
	,@UtcOffset						as '@UtcOffset'
	,@ColDefItemsDelimited			as '@ColDefItemsDelimited'
	,@ResultDefItemsDelimited		as '@ResultDefItemsDelimited'
	,@RowDefItemsDelimited			as '@RowDefItemsDelimited'
	,@MachineLoginName				as '@MachineLoginName'
	,@MachineName					as '@MachineName'
	,@Interject_UserID				as '@Interject_UserID'
	,@Interject_ClientID			as '@Interject_ClientID'
	,@Interject_LoginName			as '@Interject_LoginName'
	,@Interject_LoginAuthTypeID		as '@Interject_LoginAuthTypeID'
	,@Interject_LoginDateUTC		as '@Interject_LoginDateUTC'
	,@Interject_UserRolesDelimited	as '@Interject_UserRolesDelimited'
	,@UserContextEncrypted			as '@UserContextEncrypted'
	,@Interject_XMLDataToSave		as '@XMLDataToSave'


-- since all paramters are optional, you can also just ask for the values you need like below

exec [dbo].[RequestContext_Parse]
	@Interject_RequestContext		= @Interject_RequestContext
	,@Interject_LoginName			= @Interject_LoginName			 output
	,@Interject_UserID				= @Interject_UserID				 output

Select
	@Interject_UserID							as '@Interject_UserID'
	,@Interject_LoginName						as '@Interject_LoginName'
*/
ALTER proc [dbo].[RequestContext_Parse]

	@Interject_RequestContext		nvarchar(max)
	,@ExcelVersion					nvarchar(100)	 = '' output
	,@IdsVersion					nvarchar(100)	 = '' output
	,@FileName						nvarchar(1000)	 = '' output
	,@FilePath						nvarchar(1000)	 = '' output
	,@TabName						nvarchar(1000)	 = '' output
	,@CellRange						nvarchar(100)	 = '' output
	,@SourceFunction				nvarchar(100)	 = '' output
	,@UtcOffset						decimal(6,4)	 = 0 output
	,@ColDefItemsDelimited			nvarchar(max)	 = '' output
	,@ResultDefItemsDelimited		nvarchar(max)	 = '' output
	,@RowDefItemsDelimited			nvarchar(max)	 = '' output
	,@MachineLoginName				nvarchar(100)	 = '' output
	,@MachineName					nvarchar(100)	 = '' output
	,@Interject_UserID				nvarchar(100)	 = '' output
	,@Interject_ClientID			nvarchar(100)	 = '' output
	,@Interject_LoginName			nvarchar(100)	 = '' output
	,@Interject_LoginAuthTypeID		int				 = 0 output
	,@Interject_LoginDateUTC		datetime		 = null output
	,@Interject_UserRolesDelimited	nvarchar(max)	 = '' output
	,@UserContextEncrypted			nvarchar(4000)	 = '' output
	,@Interject_XMLDataToSave		nvarchar(max)	 = null output

	
as
/*
This SP is a helper to pull all data from the RequestContext that is passed from Interject. Below
are examples to pull all the data or just a couple values that you need (which is much less typing)

*/

		set nocount on 

	declare @Interject_RequestContextXML as xml
	set @Interject_RequestContextXML = @Interject_RequestContext 
	
	select
		@ExcelVersion				= T.c.value('./ExcelVersion[1]',						'nvarchar(100)') 
		,@IdsVersion				= T.c.value('./IdsVersion[1]',							'nvarchar(100)') 
		,@FileName					= T.c.value('./FileName[1]',							'nvarchar(1000)') 
		,@FilePath					= T.c.value('./FilePath[1]',							'nvarchar(1000)') 
		,@TabName					= T.c.value('./TabName[1]',								'nvarchar(1000)') 
		,@CellRange					= T.c.value('./CellRange[1]',							'nvarchar(100)') 
		,@SourceFunction			= T.c.value('./SourceFunction[1]',						'nvarchar(100)') 
		,@UtcOffset					= T.c.value('./UtcOffset[1]',							'decimal(6,4)') 
		,@MachineLoginName			= T.c.value('./UserContext[1]/MachineLoginName[1]',		'nvarchar(100)')
		,@MachineName				= T.c.value('./UserContext[1]/MachineName[1]',			'nvarchar(100)') 
		,@Interject_UserID			= T.c.value('./UserContext[1]/UserId[1]',				'nvarchar(100)') 
		,@Interject_ClientID		= T.c.value('./UserContext[1]/ClientId[1]',				'nvarchar(100)') 
		,@Interject_LoginName		= T.c.value('./UserContext[1]/LoginName[1]',			'nvarchar(100)') 
		,@Interject_LoginAuthTypeID	= T.c.value('./UserContext[1]/LoginAuthTypeId[1]',		'int') 
		,@Interject_LoginDateUTC	= T.c.value('./UserContext[1]/LoginDateUtc[1]',			'datetime') 
		,@UserContextEncrypted		= T.c.value('./UserContextEncrypted[1]',				'nvarchar(100)') 
	from @Interject_RequestContextXML.nodes('/RequestContext') T(c)

	set @Interject_XMLDataToSave = cast(@Interject_RequestContextXML.query('/RequestContext/XMLDataToSave') as nvarchar(max))

	-- UserRolesDelimited
	Select @Interject_UserRolesDelimited =
		STUFF
		(
			(
				SELECT ',' + T.c.value('.', 'nvarchar(100)') 
				from @Interject_RequestContextXML.nodes('RequestContext/UserContext[1]/UserRoles[1]/Role') T(c)
				ORDER BY T.c.value('.', 'nvarchar(100)') 
				FOR XML PATH ('')
			)
			,1
			,1
			,''
		)


	-- ColDefItemsDelimited
	Select @ColDefItemsDelimited =
		STUFF
		(
			(
				SELECT ',' + T.c.value('.', 'nvarchar(500)') 
				from @Interject_RequestContextXML.nodes('RequestContext/ColDefItems/Value') T(c)
				ORDER BY T.c.value('.', 'nvarchar(500)') 
				FOR XML PATH ('')
			)
			,1
			,1
			,''
		)

	-- ResultDefItemsDelimited
	Select @ResultDefItemsDelimited =
		STUFF
		(
			(
				SELECT ',' + T.c.value('.', 'nvarchar(500)') 
				from @Interject_RequestContextXML.nodes('RequestContext/ResultDefItems/Value') T(c)
				ORDER BY T.c.value('.', 'nvarchar(500)') 
				FOR XML PATH ('')
			)
			,1
			,1
			,''
		)

	-- RowDefItemsDelimited
	Select @RowDefItemsDelimited =
		STUFF
		(
			(
				SELECT ',' + isnull(T.c.value('.', 'nvarchar(500)'),'') 
				+ isnull('|' + T.c.value('./@Row', 'nvarchar(500)'),'')
				from @Interject_RequestContextXML.nodes('RequestContext/RowDefItems/Value') T(c)
				ORDER BY T.c.value('.', 'nvarchar(500)') 
				FOR XML PATH ('')
			)
			,1
			,1
			,''
		)




GO

```
</div>

### Testing the Procedure

This stored procedure is auxiliary in nature and is intended to be used to split out each system parameter encapsulated by the RequestContext System parameter provided by an Interject data portal. The following is the standalone test code for the stored procedure:

<button class="collapsible">Get The Test Code</button>
<div markdown="1" class="panel">

```sql
declare 
	@Interject_RequestContext		nvarchar(max)
	,@ExcelVersion					nvarchar(100)	 
	,@IdsVersion					nvarchar(100)	 
	,@FileName						nvarchar(1000)	 
	,@FilePath						nvarchar(1000)	 
	,@TabName						nvarchar(1000)	 
	,@CellRange						nvarchar(100)	 
	,@SourceFunction				nvarchar(100)	 
	,@UtcOffset						decimal(6,4)	 
	,@ColDefItemsDelimited			nvarchar(max)	 
	,@ResultDefItemsDelimited		nvarchar(max)	
	,@RowDefItemsDelimited			nvarchar(max)	 
	,@MachineLoginName				nvarchar(100)	 
	,@MachineName					nvarchar(100)	 
	,@Interject_UserID				nvarchar(100)	 
	,@Interject_ClientID			nvarchar(100)	 
	,@Interject_LoginName			nvarchar(100)	 
	,@Interject_LoginAuthTypeID		int				 
	,@Interject_LoginDateUTC		datetime		 
	,@Interject_UserRolesDelimited	nvarchar(max)	 
	,@UserContextEncrypted			nvarchar(4000)	 
	,@Interject_XMLDataToSave					nvarchar(max)	 

set @Interject_RequestContext = 
'<?xml version="1.0" encoding="utf-16" standalone="yes"?>
<RequestContext>
    <ExcelVersion>14.0</ExcelVersion>
    <IdsVersion>2.2.5.13</IdsVersion>
    <FileName>Interject_TestFile (version 1).xlsb</FileName>
    <FilePath>C:\Users\jeffh-high\AppData\Roaming\Microsoft\Excel</FilePath>
    <TabName>DB_ReportRangeShort</TabName>
    <CellRange>C6</CellRange>
    <SourceFunction>Range</SourceFunction>
    <UtcOffset>7</UtcOffset>
    <ColDefItems></ColDefItems>
    <ResultDefItems>
        <Value>customerid</Value>
        <Value>companyname</Value>
	</ResultDefItems>
    <RowDefItems>
        <Value Row="1">customerid</Value>
        <Value Row="2">companyname</Value>
	</RowDefItems>
    <UserContext>
        <MachineLoginName>myusername</MachineLoginName>
        <MachineName> </MachineName>
        <UserId>jxR2bDnk4jg</UserId>	
        <ClientId>CKKCYyCtT</ClientId>
        <LoginName>my@email.com</LoginName>
        <LoginAuthTypeId>10</LoginAuthTypeId>
        <LoginDateUtc>06/16/2014 11:04:08</LoginDateUtc>
        <UserRoles>
            <Role>ClientAdmin</Role>
        </UserRoles>
    </UserContext>
    <UserContextEncrypted>KAJeycwLWiy0t4Xe4GxPiI0sskc=</UserContextEncrypted>
    <XMLDataToSave>
  <c Column="Row" OrigValue="Row" />
  <c Column="Start" OrigValue="Start" />
  <c Column="CodeInputs" OrigValue="CodeInputs" />
  <c Column="Description" OrigValue="Description" />
  <c Column="End" OrigValue="End" />
  <c Column="Duration" OrigValue="Duration" />
  <c Column="Client" OrigValue="Client" />
  <c Column="Code1" OrigValue="Code1" />
  <c Column="Code2" OrigValue="Code2" />
  <c Column="Code3" OrigValue="Code3" />
  <c Column="Code4" OrigValue="Code4" />
  <c Column="ChargeCategory" OrigValue="ChargeCategory" />
  <r>
    <Row>18</Row>
    <Start>0.291666666666667</Start>
    <CodeInputs>.ids.dev..</CodeInputs>
    <Description>upgrade timelook</Description>
    <End />
    <Duration>15.4</Duration>
    <Client>ids</Client>
    <Code1>dev</Code1>
    <Code2 />
    <Code3 />
    <Code4 />
    <ChargeCategory>NB</ChargeCategory>
  </r>
    </XMLDataToSave>
</RequestContext>
'
exec [dbo].[RequestContext_Parse]
	@Interject_RequestContext		= @Interject_RequestContext
	,@ExcelVersion					 = @ExcelVersion			 output
	,@IdsVersion					 = @IdsVersion				 output
	,@FileName						 = @FileName				 output
	,@FilePath						 = @FilePath				 output
	,@TabName						 = @TabName					 output
	,@CellRange						 = @CellRange				 output
	,@SourceFunction				 = @SourceFunction			 output
	,@UtcOffset						 = @UtcOffset				 output
	,@ColDefItemsDelimited			 = @ColDefItemsDelimited	 output
	,@ResultDefItemsDelimited		 = @ResultDefItemsDelimited	 output
	,@RowDefItemsDelimited			 = @RowDefItemsDelimited	 output
	,@MachineLoginName				 = @MachineLoginName		 output
	,@MachineName					 = @MachineName				 output
	,@Interject_UserID				 = @Interject_UserID		 output
	,@Interject_ClientID			 = @Interject_ClientID		 output
	,@Interject_LoginName			 = @Interject_LoginName		 output
	,@Interject_LoginAuthTypeID		 = @Interject_LoginAuthTypeID output
	,@Interject_LoginDateUTC		 = @Interject_LoginDateUTC	 output
	,@Interject_UserRolesDelimited	 = @Interject_UserRolesDelimited	output
	,@UserContextEncrypted			 = @UserContextEncrypted	 output
	,@Interject_XMLDataToSave		 = @Interject_XMLDataToSave	 output

Select
	@ExcelVersion					as '@ExcelVersion'
	,@IdsVersion					as '@IdsVersion'
	,@FileName						as '@FileName'
	,@FilePath						as '@FilePath '
	,@TabName						as '@TabName'
	,@CellRange						as '@CellRange'
	,@SourceFunction				as '@SourceFunction'
	,@UtcOffset						as '@UtcOffset'
	,@ColDefItemsDelimited			as '@ColDefItemsDelimited'
	,@ResultDefItemsDelimited		as '@ResultDefItemsDelimited'
	,@RowDefItemsDelimited			as '@RowDefItemsDelimited'
	,@MachineLoginName				as '@MachineLoginName'
	,@MachineName					as '@MachineName'
	,@Interject_UserID				as '@Interject_UserID'
	,@Interject_ClientID			as '@Interject_ClientID'
	,@Interject_LoginName			as '@Interject_LoginName'
	,@Interject_LoginAuthTypeID		as '@Interject_LoginAuthTypeID'
	,@Interject_LoginDateUTC		as '@Interject_LoginDateUTC'
	,@Interject_UserRolesDelimited	as '@Interject_UserRolesDelimited'
	,@UserContextEncrypted			as '@UserContextEncrypted'
	,@Interject_XMLDataToSave		as '@XMLDataToSave'


-- since all parameters are optional, you can also just ask for the values you need like below

exec [dbo].[RequestContext_Parse]
	@Interject_RequestContext		= @Interject_RequestContext
	,@Interject_LoginName			= @Interject_LoginName			 output
	,@Interject_UserID				= @Interject_UserID				 output

Select
	@Interject_UserID							as '@Interject_UserID'
	,@Interject_LoginName						as '@Interject_LoginName'

```
</div>

### An Example Using the Procedure

Additionally, the following code is a sample stored procedure that calls the request context parse helper stored procedure. It is an example for how to individually select the different variables returned by the request context parse stored procedure.

<button class="collapsible">Sample Stored Procedure</button>
<div markdown="1" class="panel">

```sql
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Sample_Request_Context_Call]') AND type in (N'P', N'PC'))
BEGIN
EXEC dbo.sp_executesql @statement = N'CREATE PROCEDURE [dbo].[Sample_Request_Context_Call] AS' 
END
/*
--------------------------------
--TEST CODE 
--------------------------------

DECLARE @Interject_RequestContext NVARCHAR(MAX)

set @Interject_RequestContext = 
'<?xml version="1.0" encoding="utf-16" standalone="yes"?>
<RequestContext>
    <ExcelVersion>14.0</ExcelVersion>
    <IdsVersion>2.2.5.13</IdsVersion>
    <FileName>Interject_TestFile (version 1).xlsb</FileName>
    <FilePath>C:\Users\jeffh-high\AppData\Roaming\Microsoft\Excel</FilePath>
    <TabName>DB_ReportRangeShort</TabName>
    <CellRange>C6</CellRange>
    <SourceFunction>Range</SourceFunction>
    <UtcOffset>7</UtcOffset>
    <ColDefItems></ColDefItems>
    <ResultDefItems>
        <Value>customerid</Value>
        <Value>companyname</Value>
	</ResultDefItems>
    <RowDefItems>
        <Value Row="1">customerid</Value>
        <Value Row="2">companyname</Value>
	</RowDefItems>
    <UserContext>
        <MachineLoginName>myusername</MachineLoginName>
        <MachineName> </MachineName>
        <UserId>jxR2bDnk4jg</UserId>	
        <ClientId>CKKCYyCtT</ClientId>
        <LoginName>my@email.com</LoginName>
        <LoginAuthTypeId>10</LoginAuthTypeId>
        <LoginDateUtc>06/16/2014 11:04:08</LoginDateUtc>
        <UserRoles>
            <Role>ClientAdmin</Role>
        </UserRoles>
    </UserContext>
    <UserContextEncrypted>KAJeycwLWiy0t4Xe4GxPiI0sskc=</UserContextEncrypted>
    <XMLDataToSave>
  <c Column="Row" OrigValue="Row" />
  <c Column="Start" OrigValue="Start" />
  <c Column="CodeInputs" OrigValue="CodeInputs" />
  <c Column="Description" OrigValue="Description" />
  <c Column="End" OrigValue="End" />
  <c Column="Duration" OrigValue="Duration" />
  <c Column="Client" OrigValue="Client" />
  <c Column="Code1" OrigValue="Code1" />
  <c Column="Code2" OrigValue="Code2" />
  <c Column="Code3" OrigValue="Code3" />
  <c Column="Code4" OrigValue="Code4" />
  <c Column="ChargeCategory" OrigValue="ChargeCategory" />
  <r>
    <Row>18</Row>
    <Start>0.291666666666667</Start>
    <CodeInputs>.ids.dev..</CodeInputs>
    <Description>upgrade timelook</Description>
    <End />
    <Duration>15.4</Duration>
    <Client>ids</Client>
    <Code1>dev</Code1>
    <Code2 />
    <Code3 />
    <Code4 />
    <ChargeCategory>NB</ChargeCategory>
  </r>
    </XMLDataToSave>
</RequestContext>
'
	exec [dbo].[Sample_Request_Context_Call]
		@Interject_RequestContext = @Interject_RequestContext
*/
ALTER PROCEDURE [dbo].[Sample_Request_Context_Call]
	@Interject_RequestContext nvarchar(MAX)
AS
BEGIN
	SET NOCOUNT ON;
	DECLARE 
		@Interject_NTLogin					NVARCHAR(100)
		,@UtcOffset							DECIMAL(6,4)
		,@NowUTC							AS DATETIME = GETUTCDATE()
		,@ErrorMessageToUser				VARCHAR(1000) = ''

    EXEC [dbo].[RequestContext_Parse]
         @Interject_RequestContext		= @Interject_RequestContext
		,@UtcOffset						= @UtcOffset				OUTPUT
        ,@MachineLoginName				= @Interject_NTLogin		OUTPUT
		
    
        SELECT
             @UtcOffset							AS '@UtcOffset'
            ,@Interject_NTLogin					AS '@Interject_NTLogin'
			,@NowUTC							AS '@NowUTC'
			,DATEADD(HOUR,@UtcOffset,@NowUTC)	AS '@NowLocal'
END
GO
```
</div>
