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

1. https://platform-api.gointerject.com/api/AddinManagerLog <br>

2. https://platform-api.gointerject.com/api/Admin/Client/Secret <br>

3. https://platform-api.gointerject.com/api/Admin/DiagnosticsCode <br>

4. https://platform-api.gointerject.com/api/Admin/ValidateDiagnosticsToken <br>

5. https://platform-api.gointerject.com/api/ApplicationCache <br>

6. https://platform-api.gointerject.com/api/AuthType <br>

7. https://platform-api.gointerject.com/api/AuthType/Anonymous <br>

8. https://platform-api.gointerject.com/api/CachedSettings <br>

9. https://platform-api.gointerject.com/api/CachedSettings/Date <br>

10. https://platform-api.gointerject.com/api/CachedSettings/Offering/Refresh <br>

11. https://platform-api.gointerject.com/api/CachedSettings/Client/Refresh <br>

12. https://platform-api.gointerject.com/api/Client <br>

13. https://platform-api.gointerject.com/api/Client/Users <br>

14. https://platform-api.gointerject.com/api/Client/Invite/Accept <br>

15. https://platform-api.gointerject.com/api/Client/StatusChange <br>

16. https://platform-api.gointerject.com/api/Clients <br>

17. https://platform-api.gointerject.com/api/Credentials/IsValid <br>

18. https://platform-api.gointerject.com/api/DataPortalConnection <br>

19. https://platform-api.gointerject.com/api/DataPortalConnection/SelectOptions <br>

20. https://platform-api.gointerject.com/api/DataPortalConnection/Active <br>

21. https://platform-api.gointerject.com/api/DataPortalConnection/Redirect <br>

22. https://platform-api.gointerject.com/api/DataPortal <br>

23. https://platform-api.gointerject.com/api/DataPortal/Clone <br>

24. https://platform-api.gointerject.com/api/DataPortal/Active <br>

25. https://platform-api.gointerject.com/api/DataPortalParameter <br>

26. https://platform-api.gointerject.com/api/DataPortalParameter/SortOrders <br>

27. https://platform-api.gointerject.com/api/DataPortalParameter/CustomCommandDefaultSystemParameters <br>

28. https://platform-api.gointerject.com/api/DataPortalParameter/SchedulerDefaultSystemParameters <br>

29. https://platform-api.gointerject.com/api/Download <br>

30. https://platform-api.gointerject.com/api/Download/Links <br>

31. https://platform-api.gointerject.com/api/Download/PreviousVersion <br>

32. https://platform-api.gointerject.com/api/Download/Update <br>

33. https://platform-api.gointerject.com/api/Download/InstallerFile <br>

34. https://platform-api.gointerject.com/api/Download/Installer/Anonymous <br>

35. https://platform-api.gointerject.com/api/Download/Installer <br>

36. https://platform-api.gointerject.com/api/EffectiveClient <br>

37. https://platform-api.gointerject.com/api/Email/Send <br>

38. https://platform-api.gointerject.com/api/Email/Queue <br>

39. https://platform-api.gointerject.com/api/ErrorLog <br>

40. https://platform-api.gointerject.com/api/Eula <br>

41. https://platform-api.gointerject.com/api/ExternalAdmin <br>

42. https://platform-api.gointerject.com/api/IdsToken <br>

43. https://platform-api.gointerject.com/api/IdsTokenAndClients <br>

44. https://platform-api.gointerject.com/api/IdsToken/PlainText <br>

45. https://platform-api.gointerject.com/api/Installer/Updates <br>

46. https://platform-api.gointerject.com/api/InterjectRequest/Anonymous <br>
 
47. https://platform-api.gointerject.com/api/Invite <br>

48. https://platform-api.gointerject.com/api/Invite/Request <br>

49. https://platform-api.gointerject.com/api/License <br>

50. https://platform-api.gointerject.com/api/License/Token <br>

51. https://platform-api.gointerject.com/api/Logging <br>

52. https://platform-api.gointerject.com/api/Logging/DllErrors <br>

53. https://platform-api.gointerject.com/api/Logging/DataCallLogs <br>

54. https://platform-api.gointerject.com/api/Logging/BatchLogs <br>

55. https://platform-api.gointerject.com/api/Logging/RAMReadingLogs <br>

56. https://platform-api.gointerject.com/api/Logging/TimerLogs <br>

57. https://platform-api.gointerject.com/api/Logging/ReportLibraryDataPortal <br>

58. https://platform-api.gointerject.com/api/NLog <br>

59. https://platform-api.gointerject.com/api/NLog/IsConnected <br>

60. https://platform-api.gointerject.com/api/OAuthToken <br>

61. https://platform-api.gointerject.com/api/Offering <br>

62. https://platform-api.gointerject.com/api/Password <br>

63. https://platform-api.gointerject.com/api/Password/Admin <br>

64. https://platform-api.gointerject.com/api/PasswordReset <br>

65. https://platform-api.gointerject.com/api/PasswordReset/Admin <br>

66. https://platform-api.gointerject.com/api/PasswordReset/Welcome <br>

67. https://platform-api.gointerject.com/api/Online <br>

68. https://platform-api.gointerject.com/api/ReportCategory <br>

69. https://platform-api.gointerject.com/api/ReportCategory/Link <br>

70. https://platform-api.gointerject.com/api/ReportLink <br>

71. https://platform-api.gointerject.com/api/ReportLink/File <br>

72. https://platform-api.gointerject.com/api/ReportLink/Disable <br>

73. https://platform-api.gointerject.com/api/ReportLinkVersion <br>

74. https://platform-api.gointerject.com/api/ReportLinkVersion/File <br>

75. https://platform-api.gointerject.com/api/Role <br>

76. https://platform-api.gointerject.com/api/Role/IsClientAdmin <br>

77. https://platform-api.gointerject.com/api/ScheduledJob <br>

78. https://platform-api.gointerject.com/api/ScheduledJob/Instructions <br>

79. https://platform-api.gointerject.com/api/ScheduledJob/NextExecutionDates <br>

80. https://platform-api.gointerject.com/api/Settings <br>

81. https://platform-api.gointerject.com/api/Subscription <br>

82. https://platform-api.gointerject.com/api/Subscription/DataPortal <br>

83. https://platform-api.gointerject.com/api/ClientLinkOfferingUpdate <br>

84. https://platform-api.gointerject.com/api/Subscriber <br>

85. https://platform-api.gointerject.com/api/User <br>

86. https://platform-api.gointerject.com/api/User/Generic <br>

87. https://platform-api.gointerject.com/api/User/IsLockedOut <br>

88. https://platform-api.gointerject.com/api/User/IsValid <br>

89. https://platform-api.gointerject.com/api/User/Enabled <br>
