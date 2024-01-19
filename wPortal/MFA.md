---
title: Multi-Factor Authentication (MFA)
filename: "MFA.md"
layout: custom
keywords: [2fa, login, credentials, security, email confirmation, authenticator app]
headings: ["Overview", "Enable MFA for a User", "Login With the Authenticator App", "Login With an Email Confirmation"]
links: ["https://docs.gointerject.com/wAbout/Federated-Login-Design.html", "https://portal.gointerject.com/login.html"]
image_dir: "MFA"
description: Multi-factor authentication (MFA), also known as two-factor authentication (2FA), is a security process that requires users to provide two or more authentication factors to verify their identity before gaining access to a system or resources.
---
* * *

## Overview

Multi-factor authentication (MFA), also known as two-factor authentication (2FA), is a security process that requires users to provide two or more authentication factors to verify their identity before gaining access to a system or resources. MFA is a critical security mechanism that has emerged to counter the cyber threats in today's digital age. Where personal and organizational information is constantly under siege from malicious actors, MFA stands as a robust defense, requiring users to provide two or more authentication factors before granting access to sensitive systems, accounts, or data.

Interject supports MFA via email confirmation or an Authenticator App and it can be set up for any user within your organization.

<blockquote class=highlight_note>
<b>Note:</b> Interject MFA only works for Interject credentials. Users that use a federated login are managed by their Identity Provider (see <a href="https://docs.gointerject.com/wAbout/Federated-Login-Design.html">here</a> for more info).
</blockquote>

### Enable MFA for a User

**Step 1:** To begin, login in to the [Portal site](https://portal.gointerject.com/login.html). On the top right of the site, select your company.

![](/images/MFA/SelectCompany.png)
<br>

**Step 2:** On the left navigation panel, select **Staff**.

![](/images/MFA/SelectStaff.png)
<br>

**Step 3:** An Organization Staff window opens up showing all current users within the company. Select a user's MFA to edit their settings.

![](/images/MFA/SelectMFA.png)
<br>

**Step 4:** Click **MFA Enabled** an authentication type. Click **Save**.

![](/images/MFA/ClickMFAEnabled.png)
<br>

The current type of MFA authentication for the user is displayed.

![](/images/MFA/MFASetUp.png)
<br>

### Login With the Authenticator App

When the Authenticator App is chosen for MFA, the next time the user logs in, they will receive a prompt to check their Authenticator app for a code.

![](/images/MFA/EnterCode.png)
<br>

The Authenticator App on your device will display a code. Enter this code to log in.

![](/images/MFA/AuthenticatorCode.png)
<br>

If you do not have an Authenticator app installed and registered with your email, you will receive a QR code that you can scan to set up the app. Scan the code, install the app, and then enter the verification code to verify the app with Interject.

![](/images/MFA/QRCode.png)
<br>

### Login With an Email Confirmation

When Email Confirmation is chosen, the user will be prompted to check their email for a code.

![](/images/MFA/EnterEmailCode.png)
<br>

The email will display the code needed to log in.

![](/images/MFA/Email.png)
<br>

**Note:** The email code expires in 5 minutes.
