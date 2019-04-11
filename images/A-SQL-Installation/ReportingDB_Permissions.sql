USE Interject_Reporting
GO
/**********************************************************************************
** SCRIPT VARIABLES
*********************************************************************************/
DECLARE @varAppName varchar(128) = 'Interject'
DECLARE @varAppDB_Reporting varchar(128) = 'Interject_Reporting'		
DECLARE @varAppDBRole VARCHAR(128) = 'db_Interject'
DECLARE @varAuthType varchar(10) = 'WINDOWS'							--'Options: SQL | WINDOWS

--If @varAuthType=SQL
	DECLARE @varAppLogin_Name varchar(128) = 'InterjectAppUser'	

--If @varAuthType = 'WINDOWS'
	DECLARE @varAppDomainGroupName varchar(128) = 'InterjectUsers'	
	DECLARE @varAppDomainName varchar(128) = DEFAULT_DOMAIN()
	IF @varAuthType = 'WINDOWS' SET @varAppLogin_Name = @varAppDomainName + '\'+@varAppDomainGroupName

/*********************************************************************************/

PRINT '[' + DB_NAME() + '] ON [' + @@SERVERNAME + ']'
PRINT REPLICATE('-',80)
DECLARE @schema sysname

/**********************************************************************************
** CREATE DATABASE ROLE(S)
*********************************************************************************/
BEGIN
DECLARE @dbrole NVARCHAR(50)
SET @dbrole = @varAppDBRole
		
		PRINT 'CREATE DATABASE ROLE [' + @dbrole + ']'
		IF NOT EXISTS(SELECT 1 FROM sys.database_principals WHERE name = @dbrole AND type = 'R')
		BEGIN
			PRINT SPACE(5) + '    -- adding database role... '
			EXEC ('CREATE ROLE [' + @dbrole +'] AUTHORIZATION [dbo]')
		END
		ELSE 
			PRINT space(5) + '    -- database role exists. '
END
/**********************************************************************************
** CREATE DATABASE USERS & PERMISSIONS
*********************************************************************************/
BEGIN
DECLARE @dbuser NVARCHAR(128) = @varAppLogin_Name

	PRINT 'CREATE DATABASE USER [' + @dbuser + ']'
	IF EXISTS (SELECT name 
					FROM master.sys.server_principals
					WHERE name = @dbuser
					)
		BEGIN
			IF NOT EXISTS (
							SELECT [name]
							FROM   [sys].[database_principals]
							WHERE  [name] = @dbuser
								   AND [type_desc] = CASE WHEN @varAuthType = 'SQL' THEN 'SQL_USER'
														  WHEN @varAuthType = 'WINDOWS' THEN 'WINDOWS_GROUP'
													 END
							)
				BEGIN
					PRINT space(5) + '    -- creating user in [' + db_name() + '] database... '
					EXEC ('CREATE USER [' + @dbuser + ']')
				END
				ELSE
					PRINT space(5) + '    -- user exists in [' + db_name() + '] database. '

				IF isnull(IS_ROLEMEMBER(@dbrole,@dbuser),0) = 0
				BEGIN
						PRINT space(5) + '    -- adding to [' + @dbrole + '] database role... '
						EXEC sp_addrolemember @dbrole, @dbuser
				END
				ELSE
						PRINT space(5) + '    -- is member of [' + @dbrole + '] database role. '

		END
		ELSE
			 PRINT space(5) + '    -- login ' + QUOTENAME(@dbuser) + ' does not exist. '
END

/**********************************************************************************
** APPLY PERMISSIONS TO SCHEMAS
*********************************************************************************/
BEGIN

--SET @dbrole = 'db_Interject'
	SET @schema = 'Client'
		PRINT 'APPLY PERMISSIONS ON SCHEMA [' + @schema + '] TO DATABASE ROLE [' + @dbrole + '] | EXECUTE'
		EXEC('GRANT EXECUTE ON SCHEMA::[' + @schema + '] TO [' + @dbrole + ']')

	SET @schema = 'Custom'
		PRINT 'APPLY PERMISSIONS ON SCHEMA [' + @schema + '] TO DATABASE ROLE [' + @dbrole + '] | EXECUTE'
		EXEC('GRANT EXECUTE ON SCHEMA::[' + @schema + '] TO [' + @dbrole + ']')

	SET @schema = 'Report'
		PRINT 'APPLY PERMISSIONS ON SCHEMA [' + @schema + '] TO DATABASE ROLE [' + @dbrole + '] | EXECUTE'
		EXEC('GRANT EXECUTE ON SCHEMA::[' + @schema + '] TO [' + @dbrole + ']')

END

GO