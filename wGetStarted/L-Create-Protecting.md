---
title: "Lab Create: Protecting Sheets"
layout: custom
keywords: [password, protecting, unprotecting, lock, locking, protect]
description: INTERJECT provides an improved method to handle protecting sheets. The Sheet Protector window allows INTERJECT users with the Client Admin role to quickly protect or unprotect the sheet without any need to know the password.
---
* * *

##  Overview: 

INTERJECT provides an improved method to handle protecting sheets. The Sheet Protector window allows INTERJECT users with the Client Admin role to quickly protect or unprotect the sheet without any need to know the password. The password is default to a very long text string and is managed centrally by the INTERJECT client profile. By doing this, users no longer have to remember passwords and they can be more complex to improve security. 

When a sheet is protected using the Sheet Protector window, it will first attempt to use the current password. If that attempt fails it will try any previous passwords that are on file. If those do not work, it will also attempt to use a blank password. 

In the following lab, you will protect a sheet and use the INTERJECT pull to illustrate how protected sheets continues to function properly. In this lab you use the Customer Aging report 

<blockquote class=lab_info>
  If you are following the Training Labs, this report file can be found in the Report Library at Training Labs > Lab 6 Special Features > Lab 6.2 Protecting Sheets.
</blockquote>

###  Unprotecting Cells for User Input: 

INTERJECT requires the user to have one of the following roles for your company. This removes the need to set a password. 

* Client Admin 
* Protector 
* Editor 



Protecting the sheet still allows for pulls, drills, and many other types of INTERJECT formulas and features. A crucial part of INTERJECT is to still allow users to utilize the input fields built into reports. Protecting the sheet with INTERJECT allows for user inputs to remain unlocked regardless of the user’s role. 


One way of doing this is to first select cells  **C17, C18, C19**. 

![](/images/L-Create-Protecting/01.jpg)

<br> 


Right click and select  **Format Cells**. 

![](/images/L-Create-Protecting/02.jpg)

<br> 


A new window will pop up. Select  **Protection** and uncheck  **Locked** then click **OK.**

![](/images/L-Create-Protecting/03.jpg)

<br> 


Another way to leave filter cells unprotected is to use the  **Allow Users to Edit Range** tool in the **Review** ribbon in Excel. 

![](/images/L-Create-Protecting/04.jpg)   


<br> 


A window will appear, select  **New**

![](/images/L-Create-Protecting/05.jpg)

<br> 


In the title field, type  **Filters** then in the **Refers to cells** field, select cells **C17, C18, C19** then click **Ok** then **Apply**. 

![](/images/L-Create-Protecting/06.jpg)

<br> 


**Note:** If the password field is left empty for the named range then anyone can use the filters for the report but they cannot change the data outside of the filter range. 

<br> 


###  Protecting the Sheet and Pulling Data 

INTERJECT’s Sheet Protection tool has three options,  **Unprotect, Protect**, and  **Cancel**. 

* **Protect** has additional options, which includes choosing to protect the current sheet or the whole workbook. 
* **Unprotect** will unprotect the current spreadsheet if the user has the correct role within our company. 
* **Cancel** will close INTERJECT’s Sheet Protection tool. 

Navigate to the Interject Ribbon and select  **Sheet Protector** then select  **Protect.**

![](/images/L-Create-Protecting/07.jpg)

<br>

To verify that the filter cells are not locked, input Market into the Company Name parameter t  hen pull the report. 

![](/images/L-Create-Protecting/08.jpg)

<br> 


The speadsheet should look like this after. 

![](/images/L-Create-Protecting/09.jpg)

<br> 


Now if someone were to try and alter your data, for instance, changing the CustomerID of one of your records, they cannot since they do not have your user role. 

![](/images/L-Create-Protecting/10.jpg)   


<br> 


Now in cell  **C19** input  **SAVEA** to verify that the input filters are not protected and pull the report. 

![](/images/L-Create-Protecting/11.jpg)

<br>

###  Multiple Sheets: 

First ensure the sheet is unprotected. Then setup a grouping for columns I:L by selecting the columns, then navigating to the  **Data Ribbon** and select  **Group**. 

![](/images/L-Create-Protecting/12.jpg)   


<br> 


Now, hold down the  **shift** key and select  **CustomerAccountDetail** to select five different sheets. 

![](/images/L-Create-Protecting/13.jpg)   


<br> 


With these selected, navigate back to the INTERJECT ribbon and protect the sheet 

![](/images/L-Create-Protecting/14.jpg)   


<br> 


This will protect all five of the sheets but leave sheets that were not selected alone. 

###  Special Consideration for Column Groupings 

The INTERJECT Sheet Protector also allows for groupings to be expanded and contracted 

![](/images/L-Create-Protecting/15.jpg)   


<br> 


**Note:** INTERJECT leverages the existing sheet protector in native excel. For this reason, most of the restrictions and rights are the same. 

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

The other way is to navigate to the INTERJECT Ribbon and click on the **Advanced** **Menu** to enter the advanced menu. 

![](/images/L-Create-Protecting/19.png)   


<br> 


Select the  **system** dropdown and click  **Re-enable Protecting Groupings**

![](/images/L-Create-Protecting/20.jpg)

<br> 


Now, the sheet is still protected but groupings can function as normal. 
