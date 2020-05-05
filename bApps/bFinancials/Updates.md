---
title: INTERJECT Financials - Epicor -Update Manager
layout: custom
keywords: [Account, Epicor, Companies]
description: INTERJECT™ Financials for Epicor Enterprise (This would cover topics that are specific to integration with Epicor Enterprise, and would potentially be different for each ERP) 
---

<h2>Interject Financials - Epicor Enterprise<br>
<a href="https://drive.google.com/file/d/1GnOSqp0mQvvg-6AE1LxFaIQ6MFolrJl5/view?usp=sharing">Latest Version 1.4.1</a></h2>

Depending on which version of Interject Financials you're running, there are different update and rollback scripts. Before updating or rolling back a version, follow the procedure below. Once you know the version you're currently running, click on the appropriate dropdown below for the update release notes, the correct scripts for updating and rolling back versions, as well as procedures for running those scripts.

### To Check for Your Current Version

After the inital install, applying an update, or performing a rollback, you can confirm that your version is correct by:
- Going to the **Report Library**
- Opening the **Configuration Manager**
- Checking the **Database Version** in the upper right of the report
<br>
![Database Version](/images/A-InitialDataLoad/VersionConfirm.png){: .center-image } 

### Click Your Version Below for Release Notes and Update Scripts


<button class="collapsible"><strong>For Users With Version 1.3.1 or 1.4.0</strong></button>
<div markdown="1" class="panel">

<table> 
    <tr>
        <th><span style="font-weight:bold">Update for Previous Install:</span> <a href="https://drive.google.com/file/d/1vJXsTUWdDOK7S4Shk5RJsFWk68PcP8qb/view?usp=sharing">from1.3.1or1.4.0to1.4.1_Update.Interject_Reporting.SQL</a></th>
    </tr>
    <tr>
        <th><span style="font-weight:bold">Rollback to 1.4.0:</span> <a href="https://drive.google.com/file/d/1yLtQVLOYuQwLV3Ifquq4ZyYdus6LSnny/view?usp=sharing">from1.4.1to1.4.0_Rollback.Interject_Reporting.SQL</a></th>
    </tr>
    <tr>
        <th><span style="font-weight:bold">Rollback to 1.3.1:</span> <a href="https://drive.google.com/file/d/1BWfzw7ZZ4X-oExmEz_KxGu-ANdz1lGXc/view?usp=sharing">from1.4.1to1.3.1_Rollback.Interject_Reporting.SQL</a></th>
    </tr>
</table>

### Current Version Notes
<table>
    <tr>
        <th><span style="font-weight:bold">Interject for Financials - Current Version 1.4 </span></th>
    </tr>
        <tr>
        <th><span style="font-weight:bold">Features</span></th>
        <th><span style="font-weight:bold">Bugs Fixed</span></th>
        </tr>
        <tr>
            <td>
                <ul> 
                    <li>Add Journal Entry Upload Tool </li>
                    <li>Change the config manager FullAccount dropdown to include rollup only</li>
                    <li>Add FullAccount to COA Segment Lookup</li>
                </ul>     
            </td>
            <td>
                <ul> 
                    <li>Extend MemberDefinition_Delta table to allow greater range</li>
                    <li>Fix rollup detail grouping not calculated correctly due to ranges function</li>
                    <li>Fix rollup top definition when ranges are not numeric. Was not updating with new accounts</li>
                    <li>Use the CalcNet column in Segment table for YTD Calculation instead of BS_DEMO, which is not always accurate </li>
                    <li>Set correct default when YearMonth is blank and error when using future YearMonth with YTD</li>
                    <li>Remove custom tables and clean up database </li>
                    <li>Config Manager - Remove Merged Columns in Validated Rollup</li>
                    <li>Add Non-Validated Rollups back into dropdown list. Need the child definition to define the main rollup code. </li>
                    <li>Fix primary key violation in Build_Lookup_Import when looping through Change_Detail insert</li>
                    <li>Remove application role seucrity in TB and JEs and add segment security instead Fincube</li>
                    <li>Extend security for configuration tool</li>
                    <li>Validate RollUp code in Row Template (VBA fails on invalid characters) </li>
                    <li>Remove Seed Current Open Period / Reference column formula to Fiscal Period</li>
                    <li>Fiscal year month dropdown</li>
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
> In SQL Management Studio, run the script labeled **Rollback to ** previous install at the top of this page.
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


