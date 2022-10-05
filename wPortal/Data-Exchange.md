---
title: INTERJECT Data Exchanges
layout: custom
keywords: [API Communicationa, Security, Privacy]
description: Interject's data exchanges and active API endpoints. 
---

The following document is intended to communicate and overview of what data is handled by the Interject Addin, what data passes through the Interject Platform API, and what data passes through any other API within Interject's ecosystem. Interject provides this information for internal and external audit guidance, and for clients or prospective clients to check against their own data security and privacy protocols.


#### API Communication Domain: platform.api.gointerject.com

## API Communication Summary for On-Prem Application

### \[POST\] /api/errorlog

**Used Infrequently**. Used to "report a problem" and assist support team when on-prem users access the support menu.
**Passed Info:**
- User ID
- Client ID
- Error XML

### \[POST\] /api/IdsTokenAndClients

Used each time a user logs into Interject and is used to confirm auto-login from on-prem app.
**Passed Info:**

Authentication Package:
- Authentication Object (Json)
- Authentication Object (Encryption)
- Authentication Type ID

    User Context:
    - NT Login
    - Machine Name
    - Full Name
    - Domain Name:
    - User ID
    - Client ID
    - User Roles
    - IDS (Interject Data Systems) Login Name
    - IDS Login Auth Type ID
    - IDS Login Date UTC
- User Name
- UTC Expiration Date

### \[POST\] /api/online

Confirms connectivity to the platform API on various actions of the on-prem application. **No Parameters.**

### \[POST\] /api/InterjectRequest/Anonymous

Acquires the base contents of the settings file and initiates defaults prior to first login. Addin displays message "Updating Configuration" during this process.

**Passed Info:**
- Data Portal Name
- Request Parameter List
- Pass Through Command
- Connection String Name
- Command Type
- Command Text
- Command Timeout
- On Connection String Lookup
- Supplemental Data

**Following is an example of post:**

```xml
        InterjectRequestDTO {
            DataPortalName: null,
            RequestParameterList: [
                { Name: "@ClientPublicID", InputValue: "" },
                { Name: "@SettingNames", InputValue: "AppConfig,SessionConfig" },
                { Name: "@InstallCode", InputValue: "Interject Cloud" },
                { Name: "@ReturnValuesXML", InputValue: "" },
            ],
            PassThroughCommand: {
                ConnectionStringName: "",
                CommandType: IdsDataModel.CommandType.StoredProcedure,
                CommandText: "[app].[Client.Setting.Get]",
                CommandTimeout: 20,
                OnConnectionStringLookup: <func>,
            },
            SupplementalData: <dict<string,string>>, <- count 0
        }
``` 

**Example of returned output** 

```xml
        <?xml version="1.0" encoding="utf-8"?>
        <root>
        <Global>
            <AppDataSource>InterjectPlatform</AppDataSource>
            <DataCellTimeOutSeconds>600</DataCellTimeOutSeconds>
            <DefaultAuthTypeId>10</DefaultAuthTypeId>
            <Initiated>True</Initiated>
            <InstallCode></InstallCode>
            <InstallCodeOption>InterjectCloud</InstallCodeOption>
            <LastSaved>4/15/2022 11:05:20 AM</LastSaved>
            <RetainPriorDataCellValuesInMemory>True</RetainPriorDataCellValuesInMemory>
            <ShowAdvancedMenu>false</ShowAdvancedMenu>
            <TurnOnDiagnosticsLogging>False</TurnOnDiagnosticsLogging>
            <WebProxyBehavior>3</WebProxyBehavior>
        </Global>
        <Clients></Clients>
        <Users></Users>
        <Other></Other>
        </root>
``` 

### \[GET\] /api/download/update

Supports the update checking process

**Info Passed:**
- Version type

### \[GET\] /api/cachedsettings

Retrieves user configuration settings for logged-in user.

**Info Passed:**

- Header
    - ID Session Token
- Query String
    - Public Client ID
    - Local Cached Data

Example of returned data:

```
table(0)  Last Update Time
table(1)  CacheCategoryID 1   ReportLibraryRoot
table(2)  CacheCategoryID 2   ReporLibraryFolders
table(3)  CacheCategoryID 3   ReportLinks
table(4)  CacheCategoryID 4   ReportLinkVersions
```

## Platform API Endpoints

<details>
<summary>Click to expand</summary>

1. https://platform-api.gointerject.com/api/AddinManagerLog

2. https://platform-api.gointerject.com/api/Admin/Client/Secret

3. https://platform-api.gointerject.com/api/Admin/DiagnosticsCode

4. https://platform-api.gointerject.com/api/Admin/ValidateDiagnosticsToken

5. https://platform-api.gointerject.com/api/ApplicationCache

6. https://platform-api.gointerject.com/api/AuthType

7. https://platform-api.gointerject.com/api/AuthType/Anonymous

8. https://platform-api.gointerject.com/api/CachedSettings

9. https://platform-api.gointerject.com/api/CachedSettings/Date

10. https://platform-api.gointerject.com/api/CachedSettings/Offering/Refresh

11. https://platform-api.gointerject.com/api/CachedSettings/Client/Refresh

12. https://platform-api.gointerject.com/api/Client

13. https://platform-api.gointerject.com/api/Client/Users

14. https://platform-api.gointerject.com/api/Client/Invite/Accept

15. https://platform-api.gointerject.com/api/Client/StatusChange

16. https://platform-api.gointerject.com/api/Clients

17. https://platform-api.gointerject.com/api/Credentials/IsValid

18. https://platform-api.gointerject.com/api/DataPortalConnection

19. https://platform-api.gointerject.com/api/DataPortalConnection/SelectOptions

20. https://platform-api.gointerject.com/api/DataPortalConnection/Active

21. https://platform-api.gointerject.com/api/DataPortalConnection/Redirect

22. https://platform-api.gointerject.com/api/DataPortal

23. https://platform-api.gointerject.com/api/DataPortal/Clone

24. https://platform-api.gointerject.com/api/DataPortal/Active

25. https://platform-api.gointerject.com/api/DataPortalParameter

26. https://platform-api.gointerject.com/api/DataPortalParameter/SortOrders

27. https://platform-api.gointerject.com/api/DataPortalParameter/CustomCommandDefaultSystemParameters

28. https://platform-api.gointerject.com/api/DataPortalParameter/SchedulerDefaultSystemParameters

29. https://platform-api.gointerject.com/api/Download

30. https://platform-api.gointerject.com/api/Download/Links

31. https://platform-api.gointerject.com/api/Download/PreviousVersion

32. https://platform-api.gointerject.com/api/Download/Update

33. https://platform-api.gointerject.com/api/Download/InstallerFile

34. https://platform-api.gointerject.com/api/Download/Installer/Anonymous

35. https://platform-api.gointerject.com/api/Download/Installer

36. https://platform-api.gointerject.com/api/EffectiveClient

37. https://platform-api.gointerject.com/api/Email/Send

38. https://platform-api.gointerject.com/api/Email/Queue

39. https://platform-api.gointerject.com/api/ErrorLog

40. https://platform-api.gointerject.com/api/Eula

41. https://platform-api.gointerject.com/api/ExternalAdmin

42. https://platform-api.gointerject.com/api/IdsToken

43. https://platform-api.gointerject.com/api/IdsTokenAndClients

44. https://platform-api.gointerject.com/api/IdsToken/PlainText

45. https://platform-api.gointerject.com/api/Installer/Updates

46. https://platform-api.gointerject.com/api/InterjectRequest/Anonymous

47. https://platform-api.gointerject.com/api/Invite

48. https://platform-api.gointerject.com/api/Invite/Request

49. https://platform-api.gointerject.com/api/License

50. https://platform-api.gointerject.com/api/License/Token

51. https://platform-api.gointerject.com/api/Logging

52. https://platform-api.gointerject.com/api/Logging/DllErrors

53. https://platform-api.gointerject.com/api/Logging/DataCallLogs

54. https://platform-api.gointerject.com/api/Logging/BatchLogs

55. https://platform-api.gointerject.com/api/Logging/RAMReadingLogs

56. https://platform-api.gointerject.com/api/Logging/TimerLogs

57. https://platform-api.gointerject.com/api/Logging/ReportLibraryDataPortal

58. https://platform-api.gointerject.com/api/NLog

59. https://platform-api.gointerject.com/api/NLog/IsConnected

60. https://platform-api.gointerject.com/api/OAuthToken

61. https://platform-api.gointerject.com/api/Offering

62. https://platform-api.gointerject.com/api/Password

63. https://platform-api.gointerject.com/api/Password/Admin

64. https://platform-api.gointerject.com/api/PasswordReset

65. https://platform-api.gointerject.com/api/PasswordReset/Admin

66. https://platform-api.gointerject.com/api/PasswordReset/Welcome

67. https://platform-api.gointerject.com/api/Online

68. https://platform-api.gointerject.com/api/ReportCategory

69. https://platform-api.gointerject.com/api/ReportCategory/Link

70. https://platform-api.gointerject.com/api/ReportLink

71. https://platform-api.gointerject.com/api/ReportLink/File

72. https://platform-api.gointerject.com/api/ReportLink/Disable

73. https://platform-api.gointerject.com/api/ReportLinkVersion

74. https://platform-api.gointerject.com/api/ReportLinkVersion/File

75. https://platform-api.gointerject.com/api/Role

76. https://platform-api.gointerject.com/api/Role/IsClientAdmin

77. https://platform-api.gointerject.com/api/ScheduledJob

78. https://platform-api.gointerject.com/api/ScheduledJob/Instructions

79. https://platform-api.gointerject.com/api/ScheduledJob/NextExecutionDates

80. https://platform-api.gointerject.com/api/Settings

81. https://platform-api.gointerject.com/api/Subscription

82. https://platform-api.gointerject.com/api/Subscription/DataPortal

83. https://platform-api.gointerject.com/api/ClientLinkOfferingUpdate

84. https://platform-api.gointerject.com/api/Subscriber

85. https://platform-api.gointerject.com/api/User

86. https://platform-api.gointerject.com/api/User/Generic

87. https://platform-api.gointerject.com/api/User/IsLockedOut

88. https://platform-api.gointerject.com/api/User/IsValid

89. https://platform-api.gointerject.com/api/User/Enabled