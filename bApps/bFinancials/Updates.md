---
title: INTERJECT Financials - Epicor -Update Manager
layout: custom
keywords: [Account, Epicor, Companies]
description: INTERJECT™ Financials for Epicor Enterprise (This would cover topics that are specific to integration with Epicor Enterprise, and would potentially be different for each ERP) 
---

<h2>Interject Financials - Epicor <br>
<a href="https://drive.google.com/file/d/1OaVEIOeZu05wwl6Lh4mJdFE0W9_ah90p/view?usp=sharing">Latest Version 1.3.1</a></h2>

Depending on which version of Interject Financials you're running, there are different update and rollback scripts. Before updating or rolling back a version, follow the procedure below. Once you know the version you're currently running, click on the appropriate dropdown below for the update release notes, the correct scripts for updating and rolling back versions, as well as procedures for running those scripts.

### To Check for Your Current Version

After the inital instal, applying an update, or performing a rollback, you can confirm that your version is correct by:
- Going to the **Report Library**
- Opening the **Configuration Manager**
- Checking the **Database Version** in the upper right of the report
<br>
![Database Version](/images/A-InitialDataLoad/VersionConfirm.png){: .center-image } 

### Click Your Version Below for Release Notes and Update Scripts


<button class="collapsible"><strong>For Users With Version 1.2.3</strong></button>
<div markdown="1" class="panel">

<table> 
    <tr>
        <th><span style="font-weight:bold">Update for Previous Install:</span> <a href="https://drive.google.com/file/d/1jMi31pLmykz2UyxDY8MURUPmnyCrXsqI/view?usp=sharing">from1.2.3to1.3.1_Update.Interject_Reporting.SQL</a></th>
    </tr>
    <tr>
        <th><span style="font-weight:bold">Rollback to 1.2.3:</span> <a href="https://drive.google.com/file/d/1eZm7Oj2PEtA-HaOBsOvi7zNLzsYaap-2/view?usp=sharing">from1.3.1to1.2.3_Rollback.Interject_Reporting.SQL</a></th>
    </tr>
</table>

### Current Version Notes
<table>
    <tr>
        <th><span style="font-weight:bold">Interject for Financials - Current Version 1.3.1 </span></th>
    </tr>
        <tr>
        <th><span style="font-weight:bold">Features</span></th>
        <th><span style="font-weight:bold">Bugs Fixed</span></th>
        </tr>
        <tr>
            <td>
                <ul>
                    <li>Added <strong>Rollup View</strong> tab and drills from Rollup in <strong>Configuration Manager</strong></li> 
                </ul>     
            </td>
            <td>
                <ul> 
                    <li>Fixed open month <strong>FinCube Epicor</strong> live pull for companies with more then 3 segments</li>  
                    <li>Fixed <strong>FinCube</strong> column definition syntax for Unposted</li> 
                    <li>Removed SPs related to client-specific custom reports</li> 
                    <li>Fixed <strong>Exclusion</strong> issue in summary columns in <strong>Configuration Manager Validated Rollup</strong> tab</li> 
                    <li>Fixed <strong>COA Segment Report</strong> and settings when account doesn't exist in Default company</li> 
                    <li>Centralized segment settings in Account_Add SP</li> 
                    <li>Fixed <strong>Configuration Manager Year</strong> tab</li> 
                    <li>Added validation message when <strong>Rollup Name</strong> over 50 characters in <strong>Validate Rollup</strong> tab</li> 
                    <li><strong>COA Segment Report</strong> allow FullAccount listing in InterjectSegment tab</li> 
                    <li><strong>COA Segment Report</strong> allow to filter by Company in EpicorToInterject tab</li> 
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


