---
title: "Logging In/Out: Individual User"
filename: "Logging-In.md"
layout: custom
keywords: [login, ribbon, logout, new login, credentials, accounts, user]
headings: ["Overview", "Initial Interject Login", "New Login", "Logging Out", "Log Back In", "Switch Accounts", "Forgetting Login Credentials"]
links: ["https://docs.gointerject.com/wIndex/Diagnostics-SpecialFeatures.html#webview2browser-login", "#initial-interject-login"]
image_dir: "LogginIn"
images: [
	{file: "interject-ribbon-advanced-menu-login-revised", type: "png", site: "Add-in", cat: "Ribbon", sub: "", report: "", ribbon: "Simple", config: ""}, 
	{file: "SignIntoInterjectClick", type: "png", site: "Add-in", cat: "Login Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "InterjectAccountCredentials", type: "png", site: "Add-in", cat: "Enter Credentials", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "LoginManager", type: "png", site: "Add-in", cat: "Login Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "interject-ribbon-advanced-menu-login-revised", type: "png", site: "Add-in", cat: "Login Manager", sub: "", report: "", ribbon: "Simple", config: ""}, 
	{file: "NewLoginClick", type: "png", site: "Add-in", cat: "Login Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "EllipsesLogout", type: "png", site: "Add-in", cat: "Login Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "RibbonLogout", type: "png", site: "Add-in", cat: "Ribbon", sub: "", report: "", ribbon: "Simple", config: ""}, 
	{file: "LogoutPrompt", type: "png", site: "Add-in", cat: "Popup", sub: "Logout", report: "", ribbon: "", config: ""}, 
	{file: "LogBackIn", type: "png", site: "Add-in", cat: "Login Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "SwitchAccounts", type: "png", site: "Add-in", cat: "Login Manager", sub: "", report: "", ribbon: "", config: ""}, 
	{file: "LogoutForget", type: "png", site: "Add-in", cat: "Login Manager", sub: "", report: "", ribbon: "", config: ""}
	]
description: Logging in is simple and fast! Interject will remember your login and sign you in automatically subsequent visits. You can also add multiple logins and switch accounts easily.
---
* * *

## Overview

Logging in is simple and fast! Interject will remember your login for 30 days. You can also add multiple logins and switch accounts easily.

<blockquote class=highlight_note>
<b>Note:</b> Interject uses Webview2 for its login form. For instructions on how to use your browser instead, see <a href="https://docs.gointerject.com/wIndex/Diagnostics-SpecialFeatures.html#webview2browser-login">Webview2/Browser Login</a>.
</blockquote>

### Initial Interject Login

**Step 1:** Click the Login button on the Interject Ribbon to bring up the Login Manager.

![](/images/LogginIn/interject-ribbon-advanced-menu-login-revised.png)
<br>

**Step 2:** Click **Sign into Interject**.

![](/images/LogginIn/SignIntoInterjectClick.png)
<br>

**Step 3:** Enter your credentials in the Interject Account form and click Login.

![](/images/LogginIn/InterjectAccountCredentials.png)
<br>

**Step 4:** If you click on Login again the Login Manager window appears where you can view the current logins.

![](/images/LogginIn/LoginManager.png)
<br>

### New Login

**Step 1:** To add a new login, first click the **Login** button on the Interject Ribbon.

![](/images/LogginIn/interject-ribbon-advanced-menu-login-revised.png)
<br>

**Step 2:** Click the **New Login** button and proceed to enter your credentials the same as in [Initial Interject Login](#initial-interject-login).

![](/images/LogginIn/NewLoginClick.png)
<br>

### Logging Out

Logging out means Interject will delete the login tokens and not automatically log you in the next time you return.

To log out, you can click the ellipses on the account you wish to log out and click Log Out.

![](/images/LogginIn/EllipsesLogout.png)
<br>

You may alternatively click the Logout button on the Interject ribbon.

![](/images/LogginIn/RibbonLogout.png)
<br>

![](/images/LogginIn/LogoutPrompt.png)
<br>

### Log Back In

To log back in after you have been logged out, simply click the ellipses on the account you wish to log in and click **Log In**.

![](/images/LogginIn/LogBackIn.png)
<br>

### Switch Accounts

To switch between accounts, simply click the link of the account you wish to switch to.

![](/images/LogginIn/SwitchAccounts.png)
<br>

### Forgetting Login Credentials

Forgetting credentials means the login token is deleted from the cache and the profile manager removed from the Login Manger. You will have to reenter your credentials the next time you wish to log in.

To log out and forget your credentials, click the ellipses on the account you wish to log out and forget and click **Log Out & Forget**.

![](/images/LogginIn/LogoutForget.png)
<br>

