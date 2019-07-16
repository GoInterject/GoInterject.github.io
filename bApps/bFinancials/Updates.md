---
title: INTERJECT Financials - Epicor -Update Manager
layout: custom
keywords: [Account, Epicor, Companies]
description: INTERJECT™ Financials for Epicor Enterprise (This would cover topics that are specific to integration with Epicor Enterprise, and would potentially be different for each ERP) 
---

<h2>Interject Financials - Epicor <br>
<a href="https://drive.google.com/file/d/1uNCX3lv0AjI4K23gRG2sL3VfCH6B971y/view?usp=sharing">Latest Version 1.2.3</a></h2>

Depending on which version of Interject Financials you're running, there are different update and rollback scripts. Before updating or rolling back a version, follow the procedure below. Once you know the version you're currently running, click on the appropriate dropdown below for the update release notes, the correct scripts for updating and rolling back versions, as well as procedures for running those scripts.

### To Check for Your Current Version

After the inital instal, applying an update, or performing a rollback, you can confirm that your version is correct by:
- Going to the **Report Library**
- Opening the **Configuration Manager**
- Checking the **Database Version** in the upper right of the report
<br>
![Database Version](/images/A-InitialDataLoad/VersionConfirm.png){: .center-image } 

### Click Your Version Below for Release Notes and Update Scripts


<button class="collapsible"><strong>For Users With Version 1.2.2</strong></button>
<div markdown="1" class="panel">

<table> 
    <tr>
        <th><span style="font-weight:bold">Update for Previous Install:</span> <a href="https://drive.google.com/file/d/1HRY_AnEd--GAvGsQOOwk39rSR9flZz3N/view?usp=sharing">from1.2.2to1.2.3_Update.Interject_Reporting.SQL</a></th>
    </tr>
    <tr>
        <th><span style="font-weight:bold">Rollback to 1.2.2:</span> <a href="https://drive.google.com/file/d/1nx6lc3oI3frgSGgz7o1Zm8eRxWLUTi9f/view?usp=sharing">from1.2.3to1.2.2_Rollback.Interject_Reporting.SQL</a></th>
    </tr>
</table>

### Current Version Notes
<table>
    <tr>
        <th><span style="font-weight:bold">Interject for Financials - Current Version 1.2.3 </span></th>
    </tr>
        <tr>
        <th><span style="font-weight:bold">Features</span></th>
        <th><span style="font-weight:bold">Bugs Fixed</span></th>
        </tr>
        <tr>
            <td>
                <ul>
                   <li>Added Parallel/Serial filter in Distribution - Parallel create #1 build and serial creates builds for each row. Defaults to Parallel.</li>
                    <li>Added ability to reference columns to create dynamic file names and folder path using [] syntax</li>
                    <li>Added Global Variable Definitions and seeded with YYMM and MMYY</li>
                </ul>     
            </td>
            <td>
                <ul> 
                    <li>Re-named Seed Open Fiscal Period to Fiscal Period</li>
                    <li>Removed Open Period option in Fiscal Period dropdown</li>
                    <li>Updated Fiscal Period column to reference the Fiscal Period filter</li>
                    <li>Updated Expand/Collapse column to reference the Expand/Collapse filter</li>
                    <li>Removed Data Pull on Distribution Run filter</li>
                    <li>Re-named Tab Enabled label to Data Pull?</li>
                    <li>Re-named Settings Enabled lable to Publish?</li>
                    <li>Re-named Refresh Rollup Data to Refresh Data and modified formatting</li>
                    <li>Moved Run Distiribution button</li>
                    <li>Fix Run buttons when creating multiple Distribution tabs.</li>
                    <li>Add Trim to FullAccounts in Rollup Definition</li> 
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
> In SQL Management Studio, run the script labeled **Rollback to 1.2.3** at the top of this page.
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



<button class="collapsible"><strong>For Users With Version 1.2.1</strong></button>
<div markdown="1" class="panel">

<table> 
    <tr>
        <th><span style="font-weight:bold">Update for Previous Install:</span> <a href="https://drive.google.com/file/d/1PFeGtZrb4g1VBxslKK99RCoQLUgmNvZV/view?usp=sharing">from1.2.1to1.2.3_Update.Interject_Reporting.SQL</a></th>
    </tr>
    <tr>
        <th><span style="font-weight:bold">Rollback to 1.2.1:</span> <a href="https://drive.google.com/file/d/1ST6DTqqeaVakFJWz5B96fVbzS6cB1eH0/view?usp=sharing">from1.2.3to1.2.1_Rollback.Interject_Reporting.SQL</a></th>
    </tr>
</table>

### Current Version Notes
<table>
    <tr>
        <th><span style="font-weight:bold">Interject for Financials - Current Version 1.2.3 </span></th>
    </tr>
        <tr>
        <th><span style="font-weight:bold">Features</span></th>
        <th><span style="font-weight:bold">Bugs Fixed</span></th>
        </tr>
        <tr>
            <td>
                <ul>
                   <li>Added Parallel/Serial filter in Distribution - Parallel create #1 build and serial creates builds for each row. Defaults to Parallel.</li>
                    <li>Added ability to reference columns to create dynamic file names and folder path using [] syntax</li>
                    <li>Added Global Variable Definitions and seeded with YYMM and MMYY</li>
                </ul>     
            </td>
            <td>
                <ul> 
                    <li>Re-named Seed Open Fiscal Period to Fiscal Period</li>
                    <li>Removed Open Period option in Fiscal Period dropdown</li>
                    <li>Updated Fiscal Period column to reference the Fiscal Period filter</li>
                    <li>Updated Expand/Collapse column to reference the Expand/Collapse filter</li>
                    <li>Removed Data Pull on Distribution Run filter</li>
                    <li>Re-named Tab Enabled label to Data Pull?</li>
                    <li>Re-named Settings Enabled lable to Publish?</li>
                    <li>Re-named Refresh Rollup Data to Refresh Data and modified formatting</li>
                    <li>Moved Run Distiribution button</li>
                    <li>Fix Run buttons when creating multiple Distribution tabs.</li>
                    <li>Add Trim to FullAccounts in Rollup Definition</li>
                    <li>Fix Validation Definition for FullAccount (not allow invalid text) </li>
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
> In SQL Management Studio, run the script labeled **Rollback to 1.2.1** at the top of this page.
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

