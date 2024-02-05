---
title: "Create: Protecting Sheets"
filename: "L-Create-Protecting.md"
layout: custom
keywords: [password, protecting, unprotecting, locking, unlock, security]
headings: ["Overview", "Interject Sheet Protector Roles", "Unlocking Cells", "Protecting the Sheet and Pulling Data", "Protecting Multiple Sheets", "Special Consideration for Column Groupings"]
links: ["https://support.microsoft.com/en-au/office/protect-a-worksheet-3179efdb-1285-4d49-a9c3-f4ca36276de6", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#sheet-protector", "/wPortal/INTERJECT-Roles.html", "/wGetStarted/L-Create-CustomerAging.html"]
image_dir: "L-Create-Protecting"
images: [{file: "error", type: "png", site: "Addin", cat: "Popup", sub: "Sheet Protector", report: "", ribbon: "", config: ""},{file: "01", type: "jpg", site: "Addin", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""},{file: "02", type: "jpg", site: "Excel", cat: "Right Click Menu", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""},{file: "03", type: "jpg", site: "Excel", cat: "Format Cells", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""},{file: "04", type: "jpg", site: "Addin", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""},{file: "05", type: "jpg", site: "Excel", cat: "Allow Users to Edit Ranges", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""},{file: "06", type: "jpg", site: "Excel", cat: "Allow Users to Edit Ranges", sub: "New Range", report: "Customer Aging Summary", ribbon: "", config: ""},{file: "07", type: "jpg", site: "Addin", cat: "Sheet Protector", sub: "", report: "Customer Aging Summary", ribbon: "Advanced", config: ""},{file: "08", type: "jpg", site: "Addin", cat: "Pull Data", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""},{file: "09", type: "jpg", site: "Addin", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""},{file: "10", type: "jpg", site: "Excel", cat: "Popup", sub: "Protected", report: "Customer Aging Summary", ribbon: "", config: ""},{file: "11", type: "jpg", site: "Addin", cat: "Pull Data", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""},{file: "12", type: "jpg", site: "Addin", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""},{file: "13", type: "jpg", site: "Addin", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""},{file: "14", type: "jpg", site: "Addin", cat: "Sheet Protector", sub: "", report: "Customer Aging Summary", ribbon: "Advanced", config: ""},{file: "15", type: "jpg", site: "Addin", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""},{file: "16", type: "jpg", site: "Addin", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""},{file: "17", type: "jpg", site: "Excel", cat: "Popup", sub: "Protected", report: "Customer Aging Summary", ribbon: "", config: ""},{file: "18", type: "jpg", site: "Addin", cat: "Pull Data", sub: "", report: "Customer Aging Summary", ribbon: "Simple", config: ""},{file: "19", type: "png", site: "Addin", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "Simple", config: ""},{file: "20", type: "jpg", site: "Addin", cat: "System", sub: "", report: "Customer Aging Summary", ribbon: "Advanced", config: ""}]
description: Interject provides an improved method to handle protecting sheets. The Sheet Protector window allows Interject users with the Client Admin role to quickly protect or unprotect the sheet without any need to know the password.
---
* * *

## Overview

Excel provides a way to [protect sheets](https://support.microsoft.com/en-au/office/protect-a-worksheet-3179efdb-1285-4d49-a9c3-f4ca36276de6){:target="_blank"}{:rel="noopener noreferrer"} to prevent accidentally or deliberately changing, moving, or deleting data in a worksheet. You can mark the cells you want unlocked so that when you protect the sheet, those cells will be unlocked. Finally, Excel requires a password to protect/unprotect the sheet.

Interject provides a more convenient way to protect a sheet with the [Sheet Protector](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#sheet-protector). The Sheet Protector eliminates the need for a password. Interject uses a default password that is internally managed by the use of Interject [roles](/wPortal/INTERJECT-Roles.html). With the appropriate role, a user does not need to know the protect password and can easily protect/unprotect the sheet. When a sheet is protected using the Sheet Protector window, it will first attempt to use the current password. If that attempt fails it will try any previous passwords that are on file. If those do not work, it will also attempt to use a blank password.

Protecting the sheet still allows for pulls, drills, and many other types of Interject formulas and features. A crucial part of Interject is to still allow users to utilize the input fields built into reports. Protecting the sheet with Interject allows for user inputs to remain unlocked regardless of the user’s role.

In the following example, you will protect a sheet and use the Interject pull to illustrate how protected sheets continues to function properly. In this example you use the [Customer Aging](/wGetStarted/L-Create-CustomerAging.html) report.

<blockquote class=lab_info>
 If you are following the Training Labs, this report file can be found in the Report Library at Training Labs > Lab 6 Special Features > Lab 6.2 Protecting Sheets.
</blockquote>

### Interject Sheet Protector Roles

In order to use Interject's Sheet Protector feature, you must have an appropriate role, otherwise you will get an error showing you are unable:

![](/images/L-Create-Protecting/error.png)
<br>

The following roles allow the use of the Sheet Protector:

* ClientAdmin
* SysAdmin
* Protector

### Unlocking Cells

In order to allow certain cells to be unlocked when protecting a sheet, you must uncheck the "Locked" field before you protect the sheet. Doing so will allow you to edit these cells even though the sheet is protected.

One way of doing this is to first select cells **C17, C18, C19**.

![](/images/L-Create-Protecting/01.jpg)
<br>

Right click and select **Format Cells**.

![](/images/L-Create-Protecting/02.jpg)
<br>

A new window will pop up. Select **Protection** and uncheck **Locked** then click **OK**.

![](/images/L-Create-Protecting/03.jpg)
<br>

Another way to leave filter cells unprotected is to use the **Allow Users to Edit Range** tool in the **Review** ribbon in Excel.

![](/images/L-Create-Protecting/04.jpg)
<br>

A window will appear, select **New**.

![](/images/L-Create-Protecting/05.jpg)
<br>

In the title field, type **Filters** then in the **Refers to cells** field, select cells **C17, C18, C19** then click **Ok** then **Apply**.

![](/images/L-Create-Protecting/06.jpg)
<br>

**Note:** If the password field is left empty for the named range then anyone can use the filters for the report but they cannot change the data outside of the filter range.
<br>

### Protecting the Sheet and Pulling Data

Interject’s Sheet Protection tool has three options, **Unprotect, Protect**, and **Cancel**.

* **Protect** has additional options, which includes choosing to protect the current sheet or the whole workbook.
* **Unprotect** will unprotect the current spreadsheet if the user has the correct role within our company.
* **Cancel** will close Interject’s Sheet Protection tool.

Navigate to the Interject Ribbon and select **Sheet Protector** then select **Protect**.

![](/images/L-Create-Protecting/07.jpg)
<br>

To verify that the filter cells are not locked, input Market into the Company Name parameter then pull the report.

![](/images/L-Create-Protecting/08.jpg)
<br>

The speadsheet should look like this after.

![](/images/L-Create-Protecting/09.jpg)
<br>

Now if someone were to try and alter your data, for instance, changing the CustomerID of one of your records, they cannot since they do not have your user role.

![](/images/L-Create-Protecting/10.jpg)
<br>

Now in cell **C19** input **SAVEA** to verify that the input filters are not protected and pull the report.

![](/images/L-Create-Protecting/11.jpg)
<br>

### Protecting Multiple Sheets

First ensure the sheet is unprotected. Then setup a grouping for columns I:L by selecting the columns, then navigating to the **Data Ribbon** and select **Group**.

![](/images/L-Create-Protecting/12.jpg)
<br>

Now, hold down the **shift** key and select **CustomerAccountDetail** to select five different sheets.

![](/images/L-Create-Protecting/13.jpg)
<br>

With these tabs selected, navigate back to the Interject ribbon and protect the sheet. This will protect all five of the sheets but leave sheets that were not selected alone.

![](/images/L-Create-Protecting/14.jpg)
<br>

### Special Consideration for Column Groupings

The Interject Sheet Protector also allows for groupings to be expanded and contracted.

![](/images/L-Create-Protecting/15.jpg)
<br>

**Note:** Interject leverages the existing sheet protector in native Excel. For this reason, most of the restrictions and rights are the same.

Directly after protecting a sheet, groupings are still operational.

![](/images/L-Create-Protecting/16.jpg)
<br>

However, closing and reopening a protected sheet with groupings in it will render the groupings locked. If you select the grouping toggle then it will be protected.

![](/images/L-Create-Protecting/17.jpg)
<br>

There are two ways to fix this.

**Option 1:**

Pulling the report will refresh the protection settings. One of the settings that are refreshed is the protection of groupings. After a pull, groupings are unlocked while the rest of the report is still locked.

![](/images/L-Create-Protecting/18.jpg)
<br>

**Option 2:**

The other way is to navigate to the Interject Ribbon and click on the **Advanced** **Menu** to enter the advanced menu.

![](/images/L-Create-Protecting/19.png)
<br>

Select the **system** dropdown and click **Re-enable Protecting Groupings**.

![](/images/L-Create-Protecting/20.jpg)
<br>

Now, the sheet is still protected but groupings can function as normal.
