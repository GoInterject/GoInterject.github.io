---
title: Enterprise Capabilities
filename: "EnterpriseLandingPage.md"
layout: custom
keywords: [federated, configuration, integration]
headings: ["Overview"]
links: ["/wDeveloper/Diagnostics-InstallConfig.html", "/wDeveloper/Diagnostics-EnterpriseConnection.html", "/wDeveloper/TLS.html", "/wDeveloper/InstallerValidation.html", "/wDeveloper/ConditionalAccess.html", "/wDeveloper/MacroSecurity.html", "/wDeveloper/Enterprise-Login-Setup.html", "/wDeveloper/Federated-Login-Design.html", "/wDeveloper/ConnectionManager.html", "/wDeveloper/InternalSupportSetup.html"]
image_dir: ""
images: []
description: Interject's Enterprise Capabilities highlights a suite of features designed to enhance the security, customization, and management of Interject within enterprise environments. These capabilities allow organizations to configure custom installations, securely manage connections, and implement federated logins with single sign-on (SSO). Interject also supports enterprise-level support configuration, providing a seamless and secure experience for both users and administrators.
---
* * *

## Overview

Interject's Enterprise Capabilities highlights a suite of features designed to enhance the security, customization, and management of Interject within enterprise environments. These capabilities allow organizations to configure custom installations, securely manage connections, and implement federated logins with single sign-on (SSO). Interject also supports enterprise-level support configuration, providing a seamless and secure experience for both users and administrators.

### [Diagnostics - Open Install Configuration](/wDeveloper/Diagnostics-InstallConfig.html)

The "Open Install Configuration" from the Diagnostic form opens up the Configure Interject form where an enterprise can enter an install code for a custom installation. These custom installations are set up by Interject and made specific for an organization.

### [Diagnostics - Set Enterprise Connection](/wDeveloper/Diagnostics-EnterpriseConnection.html)

The Diagnostic "Set Enterprise Connection" allows an enterprise to store an encrypted connection string.

### [Interject TLS for HTTPS](/wDeveloper/TLS.html)

For Interject v2.3.34.0 and earlier, the default is TLS 1.1. This can be changed to TLS 1.2 by configuring the TLS Settings.

### [Checksums for Installers](/wDeveloper/InstallerValidation.html)

The data integrity of Interject installation files can be verified by comparing its checksum. Interject creates csv files containing the official checksum of the installation file. To verify an installer, you can generate a checksum for the file and compare it with the official checksum.

### [Conditional Access](/wDeveloper/ConditionalAccess.html)

Conditional access is a feature to control and validate user provisioning via policies that act on the claims issued by your identity server. These are known as Conditional Access policies. Interject's identity server exposes an interface for allowing the provisioning of users in Interject via claims provided by third party identity providers.

### [Macro Security](/wDeveloper/MacroSecurity.html)

Macro security involves mitigating the opening and uploading of Excel files that contain macros to ensure no malicious code affects any system. These macro files have the file extension of .xlsm, as opposed to a macro free file extension of .xlsx. These macro files can potentially contain malicious code that when opened via the Report Library, can execute harmful actions. New versions of the Interject Add-In (versions 2.4.x and above) will contain configurations that will mitigate this risk.

### [Enterprise Login Setup](/wDeveloper/Enterprise-Login-Setup.html)

Interject supports federated logins for enterprise allowing a single sign on (SSO) experience for Interject users within an organization. Currently, Open ID Connect (OIDC) is the primary protocol Interject supports but more federated authentication systems are planned to be supported, including Security Assertion Markup Language (SAML).

### [Federated Login Design](/wDeveloper/Federated-Login-Design.html)

Interject uses a Duende (previously Identity Server 4) API to handle authentication for federated user logins. The following diagram shows the relationship between the Interject Excel Add-in and the Auth API when users login to a federated identity system.

### [Connection Manager](/wDeveloper/ConnectionManager.html)

The Interject Connection Manager displays all Web API connections that are secured with a federated login. When a company is set up with a federated login, an Enterprise Login Code will be associated with that login in order to direct the user to their federation's login page. Once logged in, the access token issued by that federated identity provider will be used when making calls to that connection.

### [Internal Support Setup](/wDeveloper/InternalSupportSetup.html)

Interject provides a way to add your own internal support contact information to the Interject User Support form.
