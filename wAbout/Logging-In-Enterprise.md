---
title: "Logging In/Out: Enterprise User"
filename: "Logging-In-Enterprise.md"
layout: custom
keywords: [login, ribbon, logout, new login, credentials, accounts, enterprise, user]
headings: ["Overview", "Initial Enterprise Login", "New Login", "Logging Out", "Log Back In", "Switch Accounts", "Forgetting Login Credentials", "Clearing Login Cookies"]
links: ["#initial-enterprise-login"]
image_dir: "Login-Enterprise"
images: [
	{file: "interject-ribbon-advanced-menu-login-revised", type: "png", site: "Add-in", cat: "Ribbon", sub: "", report: "", ribbon: "Simple", config: ""}, 
	{file: "SignIntoInterjectClick", type: "png", site: "Add-in", cat: "Login Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "EnterpriseLoginCode", type: "png", site: "Add-in", cat: "Enter Credentials", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SelectProvider", type: "png", site: "Add-in", cat: "Enter Credentials", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "FederatedLogin", type: "png", site: "Add-in", cat: "Federated Login", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "EnterpriseLoggedIn", type: "png", site: "Add-in", cat: "Login Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "interject-ribbon-advanced-menu-login-revised", type: "png", site: "Add-in", cat: "Ribbon", sub: "", report: "", ribbon: "Simple", config: ""}, 
	{file: "NewLogin", type: "png", site: "Add-in", cat: "Login Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "Logout", type: "png", site: "Add-in", cat: "Login Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "RibbonLogout", type: "png", site: "Add-in", cat: "Ribbon", sub: "", report: "", ribbon: "Simple", config: ""}, 
	{file: "LogoutPrompt", type: "png", site: "Add-in", cat: "Popup", sub: "Logout", report: "", ribbon: "", config: ""}, 
	{file: "LogBackIn", type: "png", site: "Add-in", cat: "Login Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SwitchAccounts", type: "png", site: "Add-in", cat: "Login Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "LogoutForget", type: "png", site: "Add-in", cat: "Login Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "ClearLoginCookies", type: "png", site: "Add-in", cat: "Diagnostics", sub: "Clear External Login Cookies", report: "", ribbon: "Advanced", config: ""}
	]
description: Logging in is simple and fast! Interject will remember your login and sign you in automatically subsequent visits.You can also add multiple logins and switch accounts easily.
---
* * *

## Overview

Logging in is simple and fast! Interject will remember your login for 30 days. You can also add multiple logins and switch accounts easily.

Once a federated identity is configured for an Interject client, users can provide an accompanying enterprise login code and login to Interject with their federated identity. This page describes how to use the login from the Interject Excel Add-in.

<blockquote class=highlight_note>
<b>Note:</b> This page uses Interject version 2.5.0.19 for the content and screenshots.
</blockquote>

### Initial Enterprise Login

**Step 1:** Click the Login button on the Interject Ribbon to bring up the Login Manager.

![](/images/Login-Enterprise/interject-ribbon-advanced-menu-login-revised.png)
<br>

**Step 2:** Click **Sign into Interject**.

![](/images/Login-Enterprise/SignIntoInterjectClick.png)
<br>

**Step 3:** Enter your enterprise login code and click **Look Up Code**.

![](/images/Login-Enterprise/EnterpriseLoginCode.png)
<br>

**Step 4:** Click your Identity Provider in the list.

![](/images/Login-Enterprise/SelectProvider.png)
<br>

**Step 5:** Enter your federated Credentials and click **Continue**. 

![](/images/Login-Enterprise/FederatedLogin.png)
<br>

You can verify you are logged in by the Login Manager Window.

![](/images/Login-Enterprise/EnterpriseLoggedIn.png)
<br>

<blockquote class=highlight_note>
<b>Note:</b> Some login pages may have a "Remember Me" or a "Save Login" checkbox to save time the next time the user comes to the login page. These features are not guaranteed to work while logging in using the Interject federated login approach. The browser enabling these federated login pages is Webview2 and not the user's standard browser and is not accessible from within the Excel Add-in.
</blockquote>

### New Login

**Step 1:** To add a new login, first click the **Login** button on the Interject Ribbon.

![](/images/Login-Enterprise/interject-ribbon-advanced-menu-login-revised.png)
<br>

**Step 2:** Click the **New Login** button and proceed to enter your credentials the same as in [initial enterprise login](#initial-enterprise-login).

![](/images/Login-Enterprise/NewLogin.png)
<br>

### Logging Out

Logging out means Interject will delete the login tokens and not automatically log you in the next time you return.

To log out, you can click the ellipses on the account you wish to log out and click Log Out.

![](/images/Login-Enterprise/Logout.png)
<br>

You may alternatively click the Logout button on the Interject ribbon.

![](/images/Login-Enterprise/RibbonLogout.png)
<br>

![](/images/Login-Enterprise/LogoutPrompt.png)
<br>

### Log Back In

To log back in after you have been logged out, simply click the ellipses on the account you wish to log in and click **Log In**.

![](/images/Login-Enterprise/LogBackIn.png)
<br>

### Switch Accounts

To switch between accounts, simply click the link of the account you wish to switch to.

![](/images/Login-Enterprise/SwitchAccounts.png)
<br>

### Forgetting Login Credentials

Forgetting credentials means the login token is deleted from the cache and the profile removed from the Login Manger. 

To log out and forget your credentials, click the ellipses on the account you wish to log out and forget and click **Log Out & Forget**.

![](/images/Login-Enterprise/LogoutForget.png)
<br>

### Clearing Login Cookies

The Login cookies store the federated credentials so that the enterprise user can log back in without having to reenter their federated credentials. To clear these cookies, select **Diagnostics** from the Interject ribbon, click on **Clear External Login Cookies** and then select **Execute Selected Action**. On the next login, you will have to reenter your federated credentials.

![](/images/Login-Enterprise/ClearLoginCookies.png)
<br>
