---
title: INTERJECT Financials - Epicor - Update Manager
layout: custom
keywords: [Account, Epicor, Companies]
description: INTERJECT™ Financials for Epicor Enterprise (This would cover topics that are specific to integration with Epicor Enterprise, and would potentially be different for each ERP) 
---

<h2>Interject Financials - Epicor Enterprise<br>
<a href="https://drive.google.com/file/d/10l98VIbU0QgeBzRk6wzCQENTcgVzM8qi/view?usp=sharing">Latest Version 1.5.4</a></h2>

Depending on which version of Interject Financials you're running, there are different update and rollback scripts. Before updating or rolling back a version, follow the procedure below. Once you know the version you're currently running, click on the appropriate dropdown below for the update release notes, the correct scripts for updating and rolling back versions, as well as procedures for running those scripts.

### To Check for Your Current Version

After the inital install, applying an update, or performing a rollback, you can confirm that your version is correct by:
- Going to the **Report Library**
- Opening the **Configuration Manager**
- Checking the **Database Version** in the upper right of the report
<br>
![Database Version](/images/A-InitialDataLoad/VersionConfirm.png){: .center-image } 

### Click Your Version Below for Release Notes and Update Scripts


<button class="collapsible"><strong>For Users With Version 1.4.3-1.5.3</strong></button>
<div markdown="1" class="panel">

<table> 
    <tr>
        <th><span style="font-weight:bold">Update for Previous Install:</span> <a href="https://drive.google.com/file/d/1jcotjzfZnS9Pn7lR2BguVpzhfoSYzBGa/view?usp=sharing">from1.4.3-1.5.3to1.5.4_Update.Interject_Reporting.SQL</a></th>
    </tr>  
     <tr>
        <th><span style="font-weight:bold">Rollback to 1.5.3:</span> <a href="https://drive.google.com/file/d/1Ol_mK9cseyhOwuzZ45FQiIuJAA75ETNt/view?usp=sharing">from1.5..4to1.5.0_Rollback.Interject_Reporting.SQL</a></th>
    </tr>  
     <tr>
        <th><span style="font-weight:bold">Rollback to 1.5.2:</span> <a href="https://drive.google.com/file/d/1QE_3izgZQwMjCFgWubGv0C5wKAgiTAUV/view?usp=sharing">from1.5..4to1.5.0_Rollback.Interject_Reporting.SQL</a></th>
    </tr>
     <tr>
        <th><span style="font-weight:bold">Rollback to 1.4.3:</span> <a href="https://drive.google.com/file/d/18nGnIljPN9mgxxUaQRGMj5G7t1MBiUtH/view?usp=sharing">from1.5..4to1.4.3_Rollback.Interject_Reporting.SQL</a></th>
    </tr> 
</table>

### Current Version Notes
<table>
    <tr>
        <th><span style="font-weight:bold">Interject for Financials - Current Version 1.5.3 </span></th>
    </tr>
        <tr>
        <th><span style="font-weight:bold">Features</span></th>
        <th><span style="font-weight:bold">Bugs Fixed</span></th>
        </tr>
        <tr>
            <td>
                <ul>   
                    <li>Add better dropdown options in the journal entry upload tool limit full account options to originating company.</li>
                </ul>     
            </td>
            <td>
                <ul> 
                    <li>In Journal entry tool fix multi-currency balancing validation when entry are in mix currencies.</li>
                    <li>In fincube fix range for numeric ranges.</li>  
                    <li>Fix multi-currency balancing when entries are in multiple currencies.</li> 
                    <li>Fix range for numeric ranges.</li> 
                    <li>Fix security.</li> 
                    <li>Remove old objects.</li> 
                    <li>Clear budget amounts for deleted accounts in epicor.</li> 
                </ul>
            </td>
        </tr>
</table>


### Updating

Whenever an update of Interject for Financials is released, an update script must be run on your server. With each new update, the initial install script located on the [Technical Install](https://docs.gointerject.com/bApps/bFinancials/Technical-Install.html) page will be updated. If you initally installed the most current version listed above, you will not need to run the Update Script. If you orginally installed a version older than the most current, take the following steps to update your implementation. 

> To Upgrade
> 
> In SQL Management Studio, run the script labeled **Update for Previous Install** at the top of this page.
>
> Run \[Interject_SetupScript1_Security\], as shown below, to re-enable security.
>
>  ```SQL
> EXEC [Custom].[Interject_SetupScript1_Security]
>	@MasterEpicorDatabase = '<Epicor Controlling Database Name>'
>	,@CertificatePassword =  'myPassword1234'
>  ```
>

### Rolling Back One Version

The following steps must be taken to roll back one version. Note that this will only roll to the previous version.

> To Roll Back
>
> In SQL Management Studio, run the script labeled **Rollback to 1.3.1** at the top of this page.
>
> Run \[Interject_SetupScript1_Security\], as shown below, to re-enable security.
>
>  ```SQL
> EXEC [Custom].[Interject_SetupScript1_Security]
>	@MasterEpicorDatabase = '<Epicor Controlling Database Name>'
>	,@CertificatePassword =  'myPassword1234'
>  ```
>

</div>
 

