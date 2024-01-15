---
title: Enterprise Login Setup
layout: custom
keywords: [login, ribbon, credentials, accounts, Enterprise, setup, oidc, auth, code]
headings: ["Overview", "Provide OIDC Details", "Enterprise Login Code", "IP Whitelisting", "Setup Data Connections"]
links: ["https://openid.net/developers/how-connect-works/", "https://www.oasis-open.org/standard/saml/", "https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-protocols-oidc", "https://developer.okta.com/docs/concepts/auth-servers/", "https://auth0.com/docs/get-started/authentication-and-authorization-flow", "https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-protocols-oidc#enable-id-tokens", "/wAbout/Logging-In-Enterprise.html", "https://portal.gointerject.com/"]
description: Interject supports federated logins for enterprise allowing a single sign on (SSO) experience for Interject users within an organization.
---
* * *

## Overview

Interject supports federated logins for enterprise allowing a single sign on (SSO) experience for Interject users within an organization. Currently, [Open ID Connect](https://openid.net/developers/how-connect-works/){:target="_blank"}{:rel="noopener noreferrer"} (OIDC) is the primary protocol Interject supports but more federated authentication systems are planned to be supported, including [Security Assertion Markup Language](https://www.oasis-open.org/standard/saml/){:target="_blank"}{:rel="noopener noreferrer"} (SAML).

There are other identity provider services on the cloud that support OIDC. The following are especially easy for Interject to work with, but any system supporting OIDC will work:

* [Azure AD](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-protocols-oidc){:target="_blank"}{:rel="noopener noreferrer"}
* [Okta](https://developer.okta.com/docs/concepts/auth-servers/){:target="_blank"}{:rel="noopener noreferrer"}
* [Auth0](https://auth0.com/docs/get-started/authentication-and-authorization-flow){:target="_blank"}{:rel="noopener noreferrer"}

<blockquote class=highlight_note>
<b>Note:</b> Users will need Interject version 2.5.0.14 or above to use federated logins. Interject can be set up to accommodate federated and non-federated users existing on the same system, so we can migrate/update users individually if that makes it smoother to upgrade.
</blockquote>

The steps for setting up your Interject organization with federated logins include:

* [Providing Interject OIDC Details](#provide-oidc-details)
* [Acquiring an Enterprise Login Code](#enterprise-login-code)
* [Whitelisting Interject domain URLs](#ip-whitelisting)

### Provide OIDC Details

Interject uses a set of URLs for your identity system to configure your Interject company with an identity provider for Interject to federate to. The following URLs need to be provided to the Interject development team for federated logins to be setup:

* Authority URL - e.g. https://login.microsoftonline.com/{tenant}/v2.0 
* Discovery Endpoint - e.g.  https://login.microsoftonline.com/{tenant}/v2.0/.well-known/openid-configuration  

If a discovery endpoint is not available we will need the following URLs:

* Authorization URL - e.g. https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize  
* Token URL - e.g. https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token  
* User Info URL - e.g. https://graph.microsoft.com/oidc/userinfo  

<blockquote class=highlight_note>
<b>Note:</b> For AzureAD, we are aware of a possible extra step to get federation working. It is possible your Azure AD service may need ID Tokens enabled. Learn more <a href="https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-protocols-oidc#enable-id-tokens" target="_blank" rel="noopener noreferrer">here</a> to see if this applies to your setup.
</blockquote>

### Enterprise Login Code

After the Interject team configures the identity provider for your Interject company, you will be sent an Enterprise Login Code that users will need to use in the Interject login page to navigate to their federated login page. See [Logging In/Out - Enterprise User](/wAbout/Logging-In-Enterprise.html) for a walkthrough on how to log in with your enterprise token and federated login.

Once set up, the Enterprise Login Codes will be shown for all identity providers associated with a company in the "Organization Profile" on the [Interject portal site](https://portal.gointerject.com/).

![](/images/Enterprise-Login-Setup/OrganizationProfile.png)
<br>

### IP Whitelisting

If your network uses a firewall, it might be necessary that you will need to whitelist Interject domains when users attempt to use federated logins with Interject. If this is the case, then it is important that key domains used by Interject are whitelisted on your network.

The following are the IPs to whitelist that are used by the Interject product:

```
https://platform-api.gointerject.com/
https://live-interject-authapi.azurewebsites.net/
```

You will need to ascertain the proper steps in whitelisting these domains on your particular system.

### Setup Data Connections

Some data connections need to use a federated login for data access (e.g. often an API authenticating requests against the same federated identity provider). These data connections should be configured in the Interject portal site by selecting the desired Enterprise Login Code from the drop down on the data connection page. All identity providers configured for the selected company will show up in this drop down.

![](/images/Enterprise-Login-Setup/DataConnection.png)
<br>
