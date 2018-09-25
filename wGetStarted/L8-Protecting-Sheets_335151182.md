---
title: Interject Documentation > L8 Protecting Sheets
layout: custom
---
* * *

##  Overview:

INTERJECT provides an improved method to handle protecting sheets. The Sheet
Protector window allows INTERJECT users with the Client Admin role to quickly
protect or unprotect the sheet without any need to know the password. The
password is default to a very long text string and is managed centrally by the
INTERJECT client profile. By doing this, users no longer have to remember
passwords and they can be more complex to improve security.

  

When a sheet is protected using the Sheet Protector window, it will first
attempt to use the current password. If that attempt fails it will try any
previous passwords that are on file. If those do not work, it will also
attempt to use a blank password.

  

In the following lab, you will protect a sheet and use the INTERJECT pull to
illustrate how protected sheets continues to function properly. In this lab
you use the Customer Aging report

  * ** Unprotecting Cells for User Input  **
  * ** Protecting the Sheet and Pulling Data  **
  * ** Multiple Sheets  **
  * ** Special Consideration for Column Groupings  **

  

###

###  Unprotecting Cells for User Input:

INTERJECT requires the user to have one of the following roles for your
company. This removes the need to set a password.

  * Client Admin 
  * Protector 
  * Editor 

Protecting the sheet still allows for pulls, drills, and many other types of
INTERJECT formulas and features. A crucial part of INTERJECT is to still allow
users to utilize the input fields built into reports. Protecting the sheet
with INTERJECT allows for user inputs to remain unlocked regardless of the
user’s role.

  

One way of doing this is to first select cells  **C17, C18, C19** .

![](attachments/335151182/353140737.jpg)

  

Right click and select  **Format Cells** .

![](attachments/335151182/353042452.jpg)

  

A new window will pop up. Select  **Protection** and u  ncheck  **Locked**
then click **OK.**

![](attachments/335151182/353042457.jpg)

  

Another way to leave filter cells unprotected is to use the  **Allow Users to
Edit Range** tool in the **Review** ribbon in Excel.

![](attachments/335151182/354582628.jpg)  

  

A window will appear, select  **New**

![](attachments/335151182/354713671.jpg)

  

In the title field, type  **Filters** then in the **Refers to cells** field,
select cells **C17, C18, C19** then click **Ok** then **Apply** .

![](attachments/335151182/354680872.jpg)

  

**Note:** If the password field is left empty for the named range then anyone
can use the filters for the report but they cannot change the data outside of
the filter range.

  

###

###  Protecting the Sheet and Pulling Data

INTERJECT’s Sheet Protection tool has three options,  **Unprotect, Protect** ,
and  **Cancel** .

  * **Protect** has additional options, which includes choosing to protect the current sheet or the whole workbook. 
  * **Unprotect** will unprotect the current spreadsheet if the user has the correct role within our company. 
  * **Cancel** will close INTERJECT’s Sheet Protection tool. 

  

  

Navigate to the Interject Ribbon and select  **Sheet Protector** then select
**Protect.**

![](attachments/335151182/354713676.jpg)

To verify that the filter cells are not locked, input Market into the Company
Name parameter t  hen pull the report.

![](attachments/335151182/353140789.jpg)

  

The speadsheet should look like this after.

![](attachments/335151182/353402903.jpg)

  

Now if someone were to try and alter your data, for instance, changing the
CustomerID of one of your records, they cannot since they do not have your
user role.

![](attachments/335151182/354844717.jpg)  

  

Now in cell  **C19** input  **SAVEA** to verify that the input filters are not
protected and pull the report.

![](attachments/335151182/354779186.jpg)

  

###

###  Multiple Sheets:

Setup a grouping for columns I:L by selecting the columns, then navigating to
the  **Data Ribbon** and select  **Group** .

![](attachments/335151182/354844722.jpg)  

  

Now, hold down the  **shift** key and select  **CustomerAccountDetail** to
select five different sheets.

![](attachments/335151182/354648106.jpg)  

  

With these selected, navigate back to the INTERJECT ribbon and protect the
sheet

![](attachments/335151182/354811977.jpg)  

  

This will protect all five of the sheets but leave sheets that were not
selected alone.

###

###  Special Consideration for Column Groupings

The INTERJECT Sheet Protector also allows for groupings to be expanded and
contracted

![](attachments/335151182/354680877.jpg)  

  

**Note:** INTERJECT leverages the existing sheet protector in native excel.
For this reason, most of the restrictions and rights are the same.

Directly after protecting a sheet, groupings are still operational.

![](attachments/335151182/354779191.jpg)

  

  

However, closing and reopening a protected sheet with groupings in it will
render the groupings locked. If you select the grouping toggle then it will be
protected.

![](attachments/335151182/354615363.jpg)  

  

There are two ways to fix this.

**Option 1:**

Pulling the report will refresh the protection settings. One of the settings
that are refreshed is the protection of groupings. After a pull, groupings are
unlocked while the rest of the report is still locked.

![](attachments/335151182/354779205.jpg)  

  

**Option 2:**

The other way is to navigate to the INTERJECT Ribbon and click on the
**Advanced** **Menu** to enter the advanced menu.

![](attachments/335151182/354615363.jpg)  

  

Select the  **system** dropdown and click  **Re-enable Protecting Groupings**

![](attachments/335151182/353861636.jpg)

  

Now, the sheet is still protected but groupings can function as normal.

