---
title: "Staff Page: Add, Edit, or Delete Users"
layout: custom
keywords: [users, new, roles, user passwords, credentials]
description: The Interject Portal site allows you to add, edit, or delete users from your organization via the Staff Page. This page will show you how to do this.
---
* * *

## Overview

The [Interject Portal](https://portal.gointerject.com/) site allows you to add, edit, or delete users from your organization via the Staff Page. Here you can also activate or deactivate a user. Viewing the Staff Page and all the functionally with it is only accomplished with the ClientAdmin [role](/wPortal/INTERJECT-Roles.html#clientadmin-role).

### The Staff Page

The staff page includes a list of all users that have access to Interject within your company. To get there, first navigate to your company in the top right corner of the Portal site.

![](/images/StaffPage/SelectCompany.png)
<br>

On the left navigation pane, click **Staff**.

![](/images/StaffPage/ClickStaff.png)
<br>

You should see a list of staff under your company. You can view various information pertaining to the users here in list format.

![](/images/StaffPage/Staff.png)
<br>

You can also set up multi factor authentication from here. For more information, see [MFA](/wPortal/MFA.html).

#### External Admins

You will also see a list of External Admins. These are Interject staff members who have been set up for your company to help manage your data.

![](/images/StaffPage/ExternalAdmins.png)
<br>

To add an External Admin, enter their email address and click **Add External Admin**.

![](/images/StaffPage/AddExternalAdmin.png)
<br>

### View, Edit, Activate/Deactivate, Delete User

From the Staff page, you can do the following by hovering the cursor over the user:

* **Profile:** View/Edit a user
* **Mark as Active/Inactive:** Enable or disable a user's access to Interject
* **<font size="+1">&#x1F5D1;</font>:** Delete a user

![](/images/StaffPage/ProfileActiveDelete.png)
<br>

### Add User

To add a user, click the **Add User** button.

![](/images/StaffPage/AddUser.png)
<br>

The User Profile page appears.

![](/images/StaffPage/UserProfile.png)
<br>

<blockquote class=highlight_note>
<b>Note:</b> If your browser is set up to auto fill user names and passwords, it may do so here. Be sure to clear these out when setting up the new user.
</blockquote>
<br>

#### Adding Details

Click **More Options** to view more optional fields you can add. 

![](/images/StaffPage/MoreOptions.png)
<br>

The first four fields (First Name, Last Name, Email Address, and Phone Number) are required, but the rest are optional. Add the information for the new user.

![](/images/StaffPage/FillInNewUser.png)
<br>

<blockquote class=highlight_note>
<b>Note:</b> The User Name is what the user will log in to Interject with. If it is blank, it will automatically get set to the user's email address. Otherwise you can enter a specific user name.
</blockquote>
<br>

#### Password

You have the option of setting an initial password for the user. (Be sure to fill in both the **New Password** and **Confirm Password** fields). If you leave these fields blank, you will need to send them a [welcome email](#welcome-email) to reset their password.

![](/images/StaffPage/SetPassword.png)
<br>

For more information, see [Changing &amp; Resetting User Passwords](/wPortal/Altering-User-Passwords.html).

#### Create User

When you are ready to save the user, click **Create**. 

![](/images/StaffPage/Create.png)
<br>

Your changes are saved.

![](/images/StaffPage/ChangesSaved.png)
<br>

### Welcome Email

After creating the new user, you can send them a welcome email with the option of resetting their password.

![](/images/StaffPage/SendEmail.png)
<br>

### Roles

All new users by default are assigned to the Standard Role. The Standard Role has basic Interject permissions, which include being able to view and open live reports from the Report Library. You will see an option to add other specific roles for the user. For more information about the different roles, see [Interject Roles](/wPortal/INTERJECT-Roles.html).

![](/images/StaffPage/Roles.png)
<br>
