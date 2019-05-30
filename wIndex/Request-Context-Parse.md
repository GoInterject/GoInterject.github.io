---
title: Request Context Parse
layout: custom
keywords: [request context, parse, system parameter, stored procedure]
description: This page that lists the interject request context parse stored procedure
---

### Stored Procedure Summary

The Request Context Parse stored procedure is used as a callable helper procedure when utilizing the Interject_RequestContext system parameter. It converts the XML nodes that are brought in by the system parameter into variable values. These variable values correspond to all the other system parameters that INTERJECT offers.


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
 * INTERJECT DATA SYSTEMS, INC CONFIDENTIAL
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
	,@ColDefItemsDelimited			xml				 = '' output
	,@ResultDefItemsDelimited		xml				 = '' output
	,@RowDefItemsDelimited			xml				 = '' output
	,@MachineLoginName				nvarchar(100)	 = '' output
	,@MachineName					nvarchar(100)	 = '' output
	,@Interject_UserID				nvarchar(100)	 = '' output
	,@Interject_ClientID			nvarchar(100)	 = '' output
	,@Interject_LoginName			nvarchar(100)	 = '' output
	,@Interject_LoginAuthTypeID		int				 = 0 output
	,@Interject_LoginDateUTC		datetime		 = null output
	,@Interject_UserRolesDelimited	nvarchar(max)	 = '' output
	,@UserContextEncrypted			nvarchar(4000)	 = '' output
	,@Interject_XMLDataToSave		xml				 = null output

	
as
/*
This SP is a helper to pull all data from the RequestContext that is passed from Interject. Below
are examples to pull all the data or just a couple values that you need (which is much less typing)

*/

	set nocount on 

	declare @Interject_RequestContextXML as xml
	set @Interject_RequestContextXML = @Interject_RequestContext 
	
	select
		@ExcelVersion							= T.c.value('./ExcelVersion[1]',						'nvarchar(100)') 
		,@IdsVersion							= T.c.value('./IdsVersion[1]',							'nvarchar(100)') 
		,@FileName								= T.c.value('./FileName[1]',							'nvarchar(1000)') 
		,@FilePath								= T.c.value('./FilePath[1]',							'nvarchar(1000)') 
		,@TabName								= T.c.value('./TabName[1]',								'nvarchar(1000)') 
		,@CellRange								= T.c.value('./CellRange[1]',							'nvarchar(100)') 
		,@SourceFunction						= T.c.value('./SourceFunction[1]',						'nvarchar(100)') 
		,@UtcOffset								= T.c.value('./UtcOffset[1]',							'decimal(6,4)') 
		,@MachineLoginName						= T.c.value('./UserContext[1]/MachineLoginName[1]',		'nvarchar(100)')
		,@MachineName							= T.c.value('./UserContext[1]/MachineName[1]',			'nvarchar(100)') 
		,@Interject_UserID						= T.c.value('./UserContext[1]/UserId[1]',				'nvarchar(100)') 
		,@Interject_ClientID					= T.c.value('./UserContext[1]/ClientId[1]',				'nvarchar(100)') 
		,@Interject_LoginName					= T.c.value('./UserContext[1]/LoginName[1]',			'nvarchar(100)') 
		,@Interject_LoginAuthTypeID				= T.c.value('./UserContext[1]/LoginAuthTypeId[1]',		'int') 
		,@Interject_LoginDateUTC				= T.c.value('./UserContext[1]/LoginDateUtc[1]',			'datetime') 
		,@UserContextEncrypted					= T.c.value('./UserContextEncrypted[1]',				'nvarchar(100)') 
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

```
</div>