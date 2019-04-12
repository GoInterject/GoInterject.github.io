
/**********************************************************************************
** SCRIPT VARIABLES
*********************************************************************************/

SET NOCOUNT ON;

DECLARE @schema VARCHAR(100) 

DECLARE @CertificatePassword	VARCHAR(50) = 'myPassword1234' --*** Update if needed
DECLARE @CertificateName		VARCHAR(50) = 'InterjectCertificate' 
DECLARE @CertificateUser		VARCHAR(50) = 'InterjectCertificateUser'

/*********************************************************************************/


PRINT ( 'CREATE CERTIFICATE: ' + @CertificateName )
IF ( SELECT COUNT(*)FROM [sys].[certificates] WHERE [name] = @CertificateName ) = 0
	BEGIN
		PRINT SPACE(5) + '    -- creating certificate... '
		EXEC ( 'CREATE CERTIFICATE [' + @CertificateName + ']
					ENCRYPTION BY PASSWORD = ''' + @CertificatePassword + '''
					WITH SUBJECT = ''Certificate for signing stored procedures'',
					EXPIRY_DATE = ''21001231'';
				   ' )
	END
ELSE PRINT SPACE(5) + '    -- certificate exists. '
	
					   
PRINT ( 'CREATE CERTIFICATE USER: ' + @CertificateUser )
IF (   SELECT COUNT(*)
	   FROM	  [sys].[database_principals]
	   WHERE  [name] = @CertificateUser ) = 0
	BEGIN
		PRINT SPACE(5) + '    -- creating certificate user... '
		EXEC ( 'CREATE USER ' + @CertificateUser + ' FROM CERTIFICATE ' + @CertificateName )
	END
ELSE
	PRINT SPACE(5) + '    -- certificate user exists. '



/**********************************************************************************
** ADD CERTIFICATE TO STORE PROCEDURES WITH DYNAMIC CODE
*********************************************************************************/
PRINT ( 'ADD SIGNATURE TO [Custom].[GL_COA_withBalances]	' )
IF NOT EXISTS (	  SELECT 1
				  FROM	 [sys].[crypt_properties] AS [cp]
				  WHERE	 OBJECT_NAME([major_id]) = 'GL_COA_withBalances'
						 AND OBJECT_SCHEMA_NAME([major_id]) = 'Custom' )
	BEGIN
		PRINT SPACE(5) + '    -- adding signature... '
		EXEC ( 'ADD SIGNATURE TO [Custom].[GL_COA_withBalances]			BY CERTIFICATE ' + @CertificateName + ' WITH PASSWORD = ''' + @CertificatePassword + ''' ;' )
	END
ELSE PRINT SPACE(5) + '    -- signature exists. '



PRINT ( 'ADD SIGNATURE TO  [Custom].[Live_EpicorData]	' )
IF NOT EXISTS (	  SELECT 1
				  FROM	 [sys].[crypt_properties] AS [cp]
				  WHERE	 OBJECT_NAME([major_id]) = 'Live_EpicorData'
						 AND OBJECT_SCHEMA_NAME([major_id]) = 'Custom' )
	BEGIN
		PRINT SPACE(5) + '    -- adding signature... '
		EXEC ( 'ADD SIGNATURE TO  [Custom].[Live_EpicorData]			BY CERTIFICATE ' + @CertificateName + ' WITH PASSWORD = ''' + @CertificatePassword + ''' ;' )
	END
ELSE PRINT SPACE(5) + '    -- signature exists. '


PRINT ( 'ADD SIGNATURE TO [Custom].[GL_JEQuery]	' )
IF NOT EXISTS (	  SELECT 1
				  FROM	 [sys].[crypt_properties] AS [cp]
				  WHERE	 OBJECT_NAME([major_id]) = 'GL_JEQuery'
						 AND OBJECT_SCHEMA_NAME([major_id]) = 'Custom' )
	BEGIN
		PRINT SPACE(5) + '    -- adding signature... '
		EXEC ( 'ADD SIGNATURE TO [Custom].[GL_JEQuery]					BY CERTIFICATE ' + @CertificateName + ' WITH PASSWORD = ''' + @CertificatePassword + ''' ;' )
	END
ELSE PRINT SPACE(5) + '    -- signature exists. '

PRINT ( 'ADD SIGNATURE TO [Custom].[GL_JELookup]	' )
IF NOT EXISTS (	  SELECT 1
				  FROM	 [sys].[crypt_properties] AS [cp]
				  WHERE	 OBJECT_NAME([major_id]) = 'GL_JELookup'
						 AND OBJECT_SCHEMA_NAME([major_id]) = 'Custom' )
	BEGIN
		PRINT SPACE(5) + '    -- adding signature... '
		EXEC ( 'ADD SIGNATURE TO [Custom].[GL_JELookup]					BY CERTIFICATE ' + @CertificateName + ' WITH PASSWORD = ''' + @CertificatePassword + ''' ;' )
	END
ELSE PRINT SPACE(5) + '    -- signature exists. '

PRINT ( 'ADD SIGNATURE TO [FinCube].[FinalCalculation]	' )
IF NOT EXISTS (	  SELECT 1
				  FROM	 [sys].[crypt_properties] AS [cp]
				  WHERE	 OBJECT_NAME([major_id]) = 'FinalCalculation'
						 AND OBJECT_SCHEMA_NAME([major_id]) = 'FinCube' )
	BEGIN
		PRINT SPACE(5) + '    -- adding signature... '
		EXEC ( 'ADD SIGNATURE TO [FinCube].[FinalCalculation]			BY CERTIFICATE ' + @CertificateName + ' WITH PASSWORD = ''' + @CertificatePassword + ''' ;' )
	END
ELSE PRINT SPACE(5) + '    -- signature exists. '

PRINT ( 'ADD SIGNATURE TO [Note].[Note_Save]	' )
IF NOT EXISTS (	  SELECT 1
				  FROM	 [sys].[crypt_properties] AS [cp]
				  WHERE	 OBJECT_NAME([major_id]) = 'Note_Save'
						 AND OBJECT_SCHEMA_NAME([major_id]) = 'Note' )
	BEGIN
		PRINT SPACE(5) + '    -- adding signature... '
		EXEC ( 'ADD SIGNATURE TO [Note].[Note_Save]						BY CERTIFICATE ' + @CertificateName + ' WITH PASSWORD = ''' + @CertificatePassword + ''' ;' )
	END
ELSE PRINT SPACE(5) + '    -- signature exists. '

PRINT ( 'ADD SIGNATURE TO [FinCube].[FinalCalculation]	' )
IF NOT EXISTS (	  SELECT 1
				  FROM	 [sys].[crypt_properties] AS [cp]
				  WHERE	 OBJECT_NAME([major_id]) = 'FinalCalculation'
						 AND OBJECT_SCHEMA_NAME([major_id]) = 'FinCube' )
	BEGIN
		PRINT SPACE(5) + '    -- adding signature... '
		EXEC ( 'ADD SIGNATURE TO [FinCube].[FinalCalculation]			BY CERTIFICATE ' + @CertificateName + ' WITH PASSWORD = ''' + @CertificatePassword + ''' ;' )
	END
ELSE PRINT SPACE(5) + '    -- signature exists. '

PRINT ( 'ADD SIGNATURE TO [Note].[Note_Fixed_Get]	' )
IF NOT EXISTS (	  SELECT 1
				  FROM	 [sys].[crypt_properties] AS [cp]
				  WHERE	 OBJECT_NAME([major_id]) = 'Note_Fixed_Get'
						 AND OBJECT_SCHEMA_NAME([major_id]) = 'Note' )
	BEGIN
		PRINT SPACE(5) + '    -- adding signature... '
		EXEC ( 'ADD SIGNATURE TO [Note].[Note_Fixed_Get]					BY CERTIFICATE ' + @CertificateName + ' WITH PASSWORD = ''' + @CertificatePassword + ''' ;' )
	END
ELSE PRINT SPACE(5) + '    -- signature exists. '

PRINT ( 'ADD SIGNATURE TO [Note].[Note_Save]	' )
IF NOT EXISTS (	  SELECT 1
				  FROM	 [sys].[crypt_properties] AS [cp]
				  WHERE	 OBJECT_NAME([major_id]) = 'Note_Save'
						 AND OBJECT_SCHEMA_NAME([major_id]) = 'Note' )
	BEGIN
		PRINT SPACE(5) + '    -- adding signature... '
		EXEC ( 'ADD SIGNATURE TO [Note].[Note_Save]						BY CERTIFICATE ' + @CertificateName + ' WITH PASSWORD = ''' + @CertificatePassword + ''' ;' )
	END
ELSE PRINT SPACE(5) + '    -- signature exists. '

PRINT ( 'ADD SIGNATURE TO [Report].[MembersByCategory_Pull]	' )
IF NOT EXISTS (	  SELECT 1
				  FROM	 [sys].[crypt_properties] AS [cp]
				  WHERE	 OBJECT_NAME([major_id]) = 'MembersByCategory_Pull'
						 AND OBJECT_SCHEMA_NAME([major_id]) = 'Report' )
	BEGIN
		PRINT SPACE(5) + '    -- adding signature... '
		EXEC ( 'ADD SIGNATURE TO [Report].[MembersByCategory_Pull]		BY CERTIFICATE ' + @CertificateName + ' WITH PASSWORD = ''' + @CertificatePassword + ''' ;' )
	END
ELSE PRINT SPACE(5) + '    -- signature exists. '

PRINT ( 'ADD SIGNATURE TO [Client].[FinCube_DynamicRow]	' )
IF NOT EXISTS (	  SELECT 1
				  FROM	 [sys].[crypt_properties] AS [cp]
				  WHERE	 OBJECT_NAME([major_id]) = 'FinCube_DynamicRow'
						 AND OBJECT_SCHEMA_NAME([major_id]) = 'Client' )
	BEGIN
		PRINT SPACE(5) + '    -- adding signature... '
		EXEC ( 'ADD SIGNATURE TO [Client].[FinCube_DynamicRow]			BY CERTIFICATE ' + @CertificateName + ' WITH PASSWORD = ''' + @CertificatePassword + ''' ;' )
	END
ELSE PRINT SPACE(5) + '    -- signature exists. '

PRINT ( 'ADD SIGNATURE TO [Custom].[EPR_Grouping_Import]	' )
IF NOT EXISTS (	  SELECT 1
				  FROM	 [sys].[crypt_properties] AS [cp]
				  WHERE	 OBJECT_NAME([major_id]) = 'EPR_Grouping_Import'
						 AND OBJECT_SCHEMA_NAME([major_id]) = 'Custom' )
	BEGIN
		PRINT SPACE(5) + '    -- adding signature... '
		EXEC ( 'ADD SIGNATURE TO [Custom].[EPR_Grouping_Import]			BY CERTIFICATE ' + @CertificateName + ' WITH PASSWORD = ''' + @CertificatePassword + ''' ;' )
	END
ELSE PRINT SPACE(5) + '    -- signature exists. '

PRINT ( 'ADD SIGNATURE TO [Custom].[GL_Segment]	' )
IF NOT EXISTS (	  SELECT 1
				  FROM	 [sys].[crypt_properties] AS [cp]
				  WHERE	 OBJECT_NAME([major_id]) = 'GL_Segment'
						 AND OBJECT_SCHEMA_NAME([major_id]) = 'Custom' )
	BEGIN
		PRINT SPACE(5) + '    -- adding signature... '
		EXEC ( 'ADD SIGNATURE TO [Custom].[GL_Segment]					BY CERTIFICATE ' + @CertificateName + ' WITH PASSWORD = ''' + @CertificatePassword + ''' ;' )
	END
ELSE PRINT SPACE(5) + '    -- signature exists. '


PRINT ( 'ADD SIGNATURE TO [Sync].[InvalidateCacheOnAmounts]	' )
IF NOT EXISTS (	  SELECT 1
				  FROM	 [sys].[crypt_properties] AS [cp]
				  WHERE	 OBJECT_NAME([major_id]) = 'InvalidateCacheOnAmounts'
						 AND OBJECT_SCHEMA_NAME([major_id]) = 'Sync' )
	BEGIN
		PRINT SPACE(5) + '    -- adding signature... '
		EXEC ( 'ADD SIGNATURE TO [Sync].[InvalidateCacheOnAmounts]		BY CERTIFICATE ' + @CertificateName + ' WITH PASSWORD = ''' + @CertificatePassword + ''' ;' )
	END
ELSE PRINT SPACE(5) + '    -- signature exists. '



/**********************************************************************************
** APPLY PERMISSIONS TO SCHEMAS
*********************************************************************************/

SET @schema = 'FSGroup'
		PRINT 'APPLY PERMISSIONS ON SCHEMA	[' + @schema + ']	TO [' + @CertificateUser + '] | SELECT'
		EXEC	('GRANT SELECT ON SCHEMA::	[' + @schema + ']	TO [' + @CertificateUser + ']')
				
SET @schema = 'FSData'
		PRINT 'APPLY PERMISSIONS ON SCHEMA [' + @schema + ']	TO [' + @CertificateUser + '] | SELECT'
		EXEC	('GRANT SELECT ON SCHEMA:: [' + @schema + ']	TO [' + @CertificateUser + ']')
		

SET @schema = 'ImportERP'
		PRINT 'APPLY PERMISSIONS ON SCHEMA [' + @schema + ']	TO [' + @CertificateUser + '] | SELECT'
		EXEC	('GRANT SELECT ON SCHEMA:: [' + @schema + ']	TO [' + @CertificateUser + ']')




------------------------------------------------------------------------
--Loop through epicor databases and add rights to database
------------------------------------------------------------------------
DECLARE @DatabaseID			INT
DECLARE @DatabaseName		VARCHAR(50)


DECLARE @BinaryCertificate NVARCHAR(MAX) 



DECLARE @BusinessCursor as CURSOR;

	SET @BusinessCursor = CURSOR FOR
		SELECT 
			 [DatabaseID]
			,[DatabaseName]
		--select *
		FROM [ImportERP].[SourceDatabaseList]
		WHERE [MasterDatabase] = 0 


OPEN @BusinessCursor;

FETCH NEXT FROM @BusinessCursor INTO 
	 @DataBaseID	
	,@DatabaseName;


DECLARE @SQLDyn			VARCHAR(MAX);
DECLARE @certExist		BIT 
DECLARE @DynSQL_CheckIfCertExists NVARCHAR(MAX) 


--Loop through epicor databases 
WHILE @@FETCH_STATUS = 0
BEGIN

	SET @certExist = 0	
	SET @DynSQL_CheckIfCertExists = 'SELECT @x = 1 FROM '+ @DatabaseName + '.[sys].[certificates] WHERE [name] = ''' + @CertificateName + ''''

	

	EXEC sp_executesql 
		 @DynSQL_CheckIfCertExists
		,N'@x int out'
		,@certExist out

	
	IF @certExist = 1
	BEGIN
		
		PRINT ('----------------------------------------------------------------------------------------')
		PRINT ('--' + @DatabaseName + '    -- certificate exists. ')
		GOTO SkipInterjectCertificate
	END
	

	SET @BinaryCertificate = 'USE ' + @DatabaseName + CHAR(10) + REPLICATE(CHAR(10),2);


	SELECT @BinaryCertificate  = @BinaryCertificate + 'CREATE CERTIFICATE ' +
		   QUOTENAME(c.[name]) + CHAR(10) + CHAR(9) +
		   ' FROM BINARY = ' + 
		   CONVERT(NVARCHAR(MAX),CERTENCODED(C.certificate_id),1) + 
		   ';' 
	FROM [sys].[certificates] AS c
	WHERE c.[name] = @CertificateName;

	

	SELECT @BinaryCertificate  = @BinaryCertificate + REPLICATE(CHAR(10),2) + 
		'CREATE USER [' + @CertificateUser + '] 	FROM CERTIFICATE [' +  @CertificateName + '];' 

	--PRINT(@BinaryCertificate)
	
	PRINT ('----------------------')
	PRINT ('--' + @DatabaseName + '    --create certificate and user. ')

	EXEC (@BinaryCertificate) 


	SET @SQLDyn = CHAR(10) + 'USE	' + @DatabaseName + CHAR(10) 
				+ CHAR(10)

	SET @SQLDyn = @SQLDyn + CHAR(10) 
				+ '--add rights on glbal' + CHAR(10) 
				+ 'GRANT SELECT ON ' + @DatabaseName + '.[dbo].[glbal]			TO [' + @CertificateUser + ']'
	SET @SQLDyn = @SQLDyn + CHAR(10) 
				+ '--add rights on gltrxdet' + CHAR(10) 
				+ 'GRANT SELECT ON ' + @DatabaseName + '.[dbo].[gltrxdet]		TO [' + @CertificateUser + ']'
	SET @SQLDyn = @SQLDyn + CHAR(10)
				+ '--add rights on gltrx_all' + CHAR(10) 
				+ 'GRANT SELECT ON ' + @DatabaseName + '.[dbo].[gltrx_all]		TO [' + @CertificateUser + ']'
	SET @SQLDyn = @SQLDyn + CHAR(10) 
				+ '--add rights on glchart' + CHAR(10) 
				+ 'GRANT SELECT ON ' + @DatabaseName + '.[dbo].[glchart] 		TO [' + @CertificateUser + ']'
	SET @SQLDyn = @SQLDyn + CHAR(10) 
				+ '--add rights on gltrxtyp' + CHAR(10) 
				+ 'GRANT SELECT ON ' + @DatabaseName + '.[dbo].[gltrxtyp]		TO [' + @CertificateUser + ']'
	SET @SQLDyn = @SQLDyn + CHAR(10) 
				+ '--add rights on apvohdr_all' + CHAR(10) 
				+ 'GRANT SELECT ON ' + @DatabaseName + '.[dbo].[apvohdr_all]   TO [' + @CertificateUser + ']'
	SET @SQLDyn = @SQLDyn + CHAR(10) 
				+ '--add rights on glactype' + CHAR(10) 
				+ 'GRANT SELECT ON ' + @DatabaseName + '.[dbo].[glactype]		TO [' + @CertificateUser + ']'

	
	PRINT ('----------------------------------------------------------------------------------------')
	PRINT ('--' + @DatabaseName + '    --grand rights to certificate user. ')
	--PRINT(@SQLDyn);
	EXEC(@SQLDyn);

SkipInterjectCertificate:

	FETCH NEXT FROM @BusinessCursor 
		INTO 
			 @DataBaseID	
			,@DatabaseName;

END






