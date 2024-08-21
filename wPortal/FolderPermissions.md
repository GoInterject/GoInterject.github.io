---
title: Folder Permissions
filename: "FolderPermissions.md"
layout: custom
keywords: []
headings: ["Overview", ""]
links: ["/wPortal/Roles.md#custom-roles"]
image_dir: "FolderPermissions"
images: [
    {file: "FolderPermissionsPage", type: "png", site: "Portal", cat: "Folder permissions", sub: "", report: "", ribbon: "", config: ""},
    {file: "FolderCustomRole", type: "png", site: "Portal", cat: "Folder permissions", sub: "", report: "", ribbon: "", config: ""}
]
description: 
---
* * *

## Overview

The Folder Permissions page allows you to assign roles to folders in the Report Library. The role count shows how many roles have been assigned to that particular folder. A folder with roles assigned to it is only viewable by users with those roles. If no roles have been assigned to the folder, then the they are viewable to all roles.

<blockquote class=highlight_note>
<b style='color:red;'><strong>Note: Assigning a folder to a role may leave it inaccessible to some users. For example, if a folder is assigned to the Standard role and users only have the ClientAdmin role, they will not be able to view that folder.</strong></b>
</blockquote>
<br>


![](/images/FolderPermissions/FolderPermissionsPage.png)
<br>

[Custom roles](/wPortal/Roles.md#custom-roles) can be used in conjunction with folder permissions to give a folder viewable rights only to a selected users.

![](/images/FolderPermissions/FolderCustomRole.png)
<br>
