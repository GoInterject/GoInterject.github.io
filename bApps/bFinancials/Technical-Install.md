---
title: Data Tier Install
layout: custom
keywords: []
description: 
---

After you get access to Interject, there are three parts to installing Interject Financials - Epicor Enterprise. First is the initial data tier install, then the data load from Epicor Enterprise and FRx, then the actual report configurations in the Interject application. 


<table>
   <tr>
    <th><span style="font-weight:bold">Prerequisites</span></th>
   </tr>
            <tr>
                <td>
                    <ul>
                        <li>VPN Connectivity (if install is Remote)</li>
                        <li>Verify and Download Interject Install Scripts</li>
                    </ul>    
                </td>
            </tr>
</table>

<table>
   <tr>
    <th><span style="font-weight:bold">Script</span></th>
    <th><span style="font-weight:bold">Version</span></th>
    <th><span style="font-weight:bold">Link</span></th>
   </tr>
            <tr>
                <td> 
                  Base Install and data transfer
                </td>
                <td>
                1.4.1
                </td>
                <td>
                <a href="https://drive.google.com/file/d/1GnOSqp0mQvvg-6AE1LxFaIQ6MFolrJl5/view?usp=sharing">Initial.Interject_Reporting.sql.</a> 
                </td>
            </tr>
            <tr>
                <td> 
                   FRX Migration
                </td>
                <td>
                1.0.6
                </td>
                <td>
                <a href="https://drive.google.com/file/d/1UcSwEf_oKjr3eVSSUJKyzZyB60YGJsaM/view?usp=sharing">Migration Script</a>
                </td>
            </tr>
</table>


### Steps Required for Technical Install


> To-do
>
> **Step 1:** Connect to your Epicor server as SysAdmin in **SQL MGT Studio**
>
>**Step 2:** Create Interject Reporting Database
> - Right Click New Database in the Object Explorer
> ![New database](/images/A-SQL-Installation/newDB.png){: .center-image }
> - Enter the desired DB name into the Database Name field. The default is "Interject_Reporting", but you can name it as needed
> ![New database](/images/A-SQL-Installation/01.png){: .center-image }
> - Press OK
>
> **Step 3:** Point the script window to the new database
> ![Mgt Studio Point](/images/A-SQL-Installation/MgtStudioPointTo.png){: .center-image }
> 
> **Step 4:** Execute the Initial.Interject_Reporting.sql script
>
> **Step 5:** Create security objects and grant read-only access to Epicor tables by passing the following parameters using the following script as an example:
>
> ```SQL
> EXEC [Custom].[Interject_SetupScript1_Security]
>	@MasterEpicorDatabase = '<Epicor Controlling Database Name>'
>	,@CertificatePassword =  'myPassword1234'
>```
>
> - 5a: MasterEpicorDatabase \(specify master Epicor DB\)
> - 5b: CertificatePassword \(create a certificate with a custom password\)
>

**Technical Note:** This will create \[LocalDomain\]/InterjectUser group and provide it with a new db_Interject role. This role will have execute rights to 3 schemas \[Client\], \[Custom\], and \[Report\]. This script also creates a certificate and signs store procedures that have dynamic code. The certificate provides read only access to the sign store procedures on the already-used tables of your Epicor databases. If at any point these store procedures are changed, the certificate will be invalidated and will need to be reapplied.


   











