---
title: INTERJECT Financials - Epicor -Update Manager
layout: custom
keywords: [Account, Epicor, Companies]
description: INTERJECT™ Financials for Epicor Enterprise (This would cover topics that are specific to integration with Epicor Enterprise, and would potentially be different for each ERP) 
---

<table>
    <tr>
        <th><span style="font-weight:bold">Current for Inital Install:</span> <a href="https://drive.google.com/file/d/16E2th5xN__y7gyBiJ4HHbxAD1kjcuufi/view">Initial.Interject_Reporting_1.1.0.SQL</a></th>
    </tr>
    <tr>
        <th><span style="font-weight:bold">Update for Previous Install:</span> <a href="https://drive.google.com/file/d/1rDImgOqW1-4J5xfzDkga_ahV79EWkdqL/view">from1.0.11to1.1.0_Update.Interject_Reporting.SQL</a></th>
    </tr>
    <tr>
        <th><span style="font-weight:bold">Rollback to 1.0.10:</span> <a href="hhttps://drive.google.com/file/d/1ZaDnrP-v40aTh7NBH8mbvO3oDIY230G3/view">from1.1.0to1.0.11_Rollback.Interject_Reporting.SQL</a></th>
    </tr>
</table>

### Current Version Notes
<table>
    <tr>
        <th><span style="font-weight:bold">Interject for Financials - Current Verion: </span><a href="https://drive.google.com/file/d/1rDImgOqW1-4J5xfzDkga_ahV79EWkdqL/view">Initial.Interject_Reporting_1.1.0.SQL</a></th>
    </tr>
        <tr>
        <th><span style="font-weight:bold">Features</span></th>
        <th><span style="font-weight:bold">Bugs Fixed</span></th>
        </tr>
        <tr>
            <td>
                <ul>
                    <li>Generate report templates on segments other than natural account</li>
                    <li>Simplified Distribution tab</li>
                    <li>Added Binder feature to report templates</li>
                    <li>Separate Validated Rollup add non-account option in the Config Mgr</li>
                    <li>Add Posted and Unposted options in the Trial Balance</li>
                    <li>Add Reference Code to JEQuery tool</li>
                    <li>Add sign reversal to templates and fincube</li>
                </ul>    
            </td>
            <td>
                <ul>
                    <li>Rollup dropdown in Trial Balance report shows only validated rollups. Presentation of rollup hierarchy simplified.</li>
                    <li>Formatted columns in Distribution as Text</li>
                    <li>Reduced column definitions in Report Templates to not use all columns</li>
                    <li>Drill to Rollups tab clears out filters to start with blank template</li>
                    <li>Reduced column definitions in Report Templates to not use all columns</li>
                    <li>Various formatting changes in the subscription</li>
                    <li>Add prefix in summary rollup 2 to include rollup name</li>
                    <li>Remove FRx parameter from Template</li>
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
>	@MasterEpicorDatabase = 'samplemasterdb'
>	,@CertificatePassword =  'myPassword1234'
>  ```
>

### Rolling Back One Version

The following steps must be taken to roll back one version. Note that this will only roll to the previous version.

> To Roll Back
>
> In SQL Management Studio, run the script labeled **Rollback to 1.0.10** at the top of this page.
>
> Run \[Interject_SetupScript1_Security\], as shown below, to re-enable security.
>
>  ```SQL
> EXEC [Custom].[Interject_SetupScript1_Security]
>	@MasterEpicorDatabase = 'samplemasterdb'
>	,@CertificatePassword =  'myPassword1234'
>  ```
>

### To Check for the Most Current Version

After the inital instal, applying an update, or performing a rollback, you can confirm that your version is correct by:
- Going to the **Report Library**
- Opening the **Configuration Manager**
- Checking the **Database Version** in the upper right of the report
<br>
![Database Version](/images/A-InitialDataLoad/VersionConfirm.png){: .center-image }