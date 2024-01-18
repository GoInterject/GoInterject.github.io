---
title: Conditional Access
filename: "ConditionalAccess.md"
layout: custom
keywords: [policy, statements, user claims, rules]
headings: ["Overview", "Conditional Statements", "User Claims", "Conditional Rules", "Configuring Conditional Access"]
links: []
description: Conditional access is a feature to control and validate user provisioning via policies that act on the claims issued by your identity server. These are known as Conditional Access policies. Interject's identity server exposes an interface for allowing the provisioning of users in Interject via claims provided by third party identity providers.
---
* * *

## Overview

Conditional access is a feature to control and validate user provisioning via policies that act on the claims issued by your identity server. These are known as Conditional Access policies. Interject's identity server exposes an interface for allowing the provisioning of users in Interject via claims provided by third party identity providers.

### Conditional Statements

Conditional Access policies at their simplest are if-then statements. That is, if a user wants access to Interject, then they must satisfy a condition.

Example:

1. If a user wants access, then the user role should be within a list of available roles
2. If a user wants access, then the user-name should end with @gointerject.com
3. If a user wants access, then the user-name should be available in the list of valid users
4. If a user wants access, then the user department should be within a list of available departments

Here are the various conditional checks available in the system:

- Equals
- Not Equals
- Contains
- Not Contains
- Ends With
- Starts With
- Regular Expression

### User Claims

All the conditional checks are against the user claims. Claims are key value pairs. We get these claims from external providers.

**Note:** Claim keys are not case sensitive.

Here are a few examples of user claims:

|Claim| Claim Key | Claim Value |
|---|---|---|
|Role| http://schemas.microsoft.com/ws/2008/06/identity/claims/role | Admin |
|Email| http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress | user@example.com |

### Conditional Rules

Here is an example of how the conditional rules mapping is applied:

|Id|ProviderClaimKey| ProviderClaimValue| Condition | Regular Expression|
|---|---|---|---|---|
|Rule1|http://schemas.microsoft.com/ws/2008/06/identity/claims/role|Admin|Equals||
|Rule2|http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress|1@example.com,2@example.com,3@example.com|Contains||
|Rule3|http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress||RegularExpression|^[A-Za-z0-9._%+-]+@gointerject\.com$|

**Rule1**: The user is allowed access only when the Claim value for http://schemas.microsoft.com/ws/2008/06/identity/claims/role (Role) is equal to 'Admin'

**Rule2**: The user is allowed access only when the Claim value for http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress (Email) is either 1@example.com, 2@example.com or 3@example.com

**Rule3**: The user is allowed access only when the Claim value for http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress (Email) satisfies the regular expression. Regular expression will satisfy only when the user name ends with @gointerject.com

We can define any number of conditional access rules. If any of the rules fail, user access is restricted.

### Configuring Conditional Access

To configure conditional access, provide us with the following for each rule you would like configured: 

* Claim Key
* Claim Value
* Condition
* Regular Expression (only required for Regular Expression condition)
