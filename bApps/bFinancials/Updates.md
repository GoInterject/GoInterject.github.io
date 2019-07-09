---
title: INTERJECT Financials - Epicor -Update Manager
layout: custom
keywords: [Account, Epicor, Companies]
description: INTERJECT™ Financials for Epicor Enterprise (This would cover topics that are specific to integration with Epicor Enterprise, and would potentially be different for each ERP) 
---

<h2>Interject Financials - Epicor <br>
<a href="https://drive.google.com/file/d/1KW0iw7OTpVWN0SHFIxXjHs5-mGj5T4pI/view?usp=sharing">Latest Version 1.2.0</a></h2>

Depending on which version of Interject Financials you're running, there are different update and rollback scripts. Before updating or rolling back a version, follow the procedure below. Once you know the version you're currently running, click on the appropriate dropdown below for the update release notes, the correct scripts for updating and rolling back versions, as well as procedures for running those scripts.

### To Check for Your Current Version

After the inital instal, applying an update, or performing a rollback, you can confirm that your version is correct by:
- Going to the **Report Library**
- Opening the **Configuration Manager**
- Checking the **Database Version** in the upper right of the report
<br>
![Database Version](/images/A-InitialDataLoad/VersionConfirm.png){: .center-image } 

### Click Your Version Below for Release Notes and Update Scripts

<button class="collapsible"><strong>For Users With Version 1.1.0</strong></button>
<div markdown="1" class="panel">

<table>
    <tr>
        <th>No database changes, update script increments version in  database to track</th>
    </tr>
    <tr>
        <th><span style="font-weight:bold">Update for Previous Install:</span> <a href="https://drive.google.com/file/d/1-CCCQUt_TBsTMtv64Z2Vg5SBFQSk8Zkq/view?usp=sharing">from1.1.0to1.2.0_Update.Interject_Reporting.SQL</a></th>
    </tr>
    <tr>
        <th><span style="font-weight:bold">Rollback to 1.1.0:</span> <a href="https://drive.google.com/file/d/1bgSg2a-IqPFe5HQWTbbB8QXZiYUFaWGA/view?usp=sharing">from1.2.0to1.1.0_Rollback.Interject_Reporting.SQL</a></th>
    </tr>
</table>

### Current Version Notes
<table>
    <tr>
        <th><span style="font-weight:bold">Interject for Financials - Current Version 1.2.0 </span></th>
    </tr>
        <tr>
        <th><span style="font-weight:bold">Features</span></th>
        <th><span style="font-weight:bold">Bugs Fixed</span></th>
        </tr>
        <tr>
            <td>
                <ul>
                    <li>Distributions will allow users to combinate full account with another segment.</li> 
                </ul>     
            </td>
            <td>
                <ul>
                    <li>Drill-down from Fincube reports to Trial Balance reports will work with full account groupings.</li> 
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
### Rolling Back One Version

The following step must be taken to roll back one version. Note that this will only roll to the previous version.

> To Roll Back
>
> In SQL Management Studio, run the script labeled **Rollback to 1.1.0** at the top of this page.
>

</div>


<button class="collapsible"><strong>For Users With Version 1.0.12</strong></button>
<div markdown="1" class="panel">

<table>
    <tr>
        <th><span style="font-weight:bold">Update for Previous Install:</span> <a href="https://drive.google.com/file/d/1zGg71HR5_po0zOEXWgnm9HllYevY3L_V/view?usp=sharing">from1.0.12to1.1.0_Update.Interject_Reporting.SQL</a></th>
    </tr>
    <tr>
        <th><span style="font-weight:bold">Rollback to 1.0.12:</span> <a href="https://drive.google.com/file/d/1PTApwLyucygqaFT16DvhwUv0FpRTLe-b/view?usp=sharing">from1.1.0to1.0.12_Rollback.Interject_Reporting.SQL</a></th>
    </tr>
</table>

### Current Version Notes
<table>
    <tr>
        <th><span style="font-weight:bold">Interject for Financials - Current Version 1.1.0 </span></th>
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
                    <li>Separate Validated Rollup add non-account option in the Config Mgr</li>
                    <li>Add Posted and Unposted options in the Trial Balance</li>
                    <li>Add Reference Code to JEQuery tool</li>
                    <li>Add sign reversal to templates and fincube</li>
                    <li>Added Last Run indication in generated templates</li>
                    <li>Added 3 drills to the Trial Balance from generated templates</li>
                </ul>     
            </td>
            <td>
                <ul>
                    <li>Rollup dropdown in Trial Balance report shows only validated rollups. Presentation of rollup hierarchy simplified.</li>
                    <li>Formatted columns in Distribution as Text</li>
                    <li>Reduced column definitions in Report Templates to not use all columns</li>
                    <li>Drill to Rollups tab clears out filters to start with blank template</li>
                    <li>Various formatting changes in the subscription</li>
                    <li>Add prefix in summary rollup 2 to include rollup name</li>
                    <li>Remove FRx parameter from Template</li>
                    <li>Added 10 char. limit to Row Template Code name and validation</li>
                    <li>Remove double line subtotals in generated templates</li>
                    <li>Added Data Pull on Distribution filter to Distribution tab (prep or run), unhide some columns</li>
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
> In SQL Management Studio, run the script labeled **Rollback to 1.0.12** at the top of this page.
>
> Run \[Interject_SetupScript1_Security\], as shown below, to re-enable security.
>
>  ```SQL
> EXEC [Custom].[Interject_SetupScript1_Security]
>	@MasterEpicorDatabase = 'samplemasterdb'
>	,@CertificatePassword =  'myPassword1234'
>  ```
>

</div>


<button class="collapsible"><strong>For Users With Version 1.0.11</strong></button>
<div markdown="1" class="panel">

<table>
    <tr>
        <th><span style="font-weight:bold">Update for Previous Install:</span> <a href="https://drive.google.com/file/d/1Dq5lMgoDbV5LlviI4RxhLqY6z3Ptd3tY/view?usp=sharing">from1.0.11to1.1.0_Update.Interject_Reporting.SQL</a></th>
    </tr>
    <tr>
        <th><span style="font-weight:bold">Rollback to 1.0.11:</span> <a href="https://drive.google.com/file/d/17xmsrzussLdzXtyTaWZy9IWnbr28SBUM/view?usp=sharing">from1.1.0to1.0.11_Rollback.Interject_Reporting.SQL</a></th>
    </tr>
</table>

### Current Version Notes
<table>
    <tr>
        <th><span style="font-weight:bold">Interject for Financials - Current Version 1.1.0 </span></th>
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
                    <li>Separate Validated Rollup add non-account option in the Config Mgr</li>
                    <li>Add Posted and Unposted options in the Trial Balance</li>
                    <li>Add Reference Code to JEQuery tool</li>
                    <li>Add sign reversal to templates and fincube</li>
                    <li>Added Last Run indication in generated templates</li>
                    <li>Added 3 drills to the Trial Balance from generated templates</li>
                </ul>     
            </td>
            <td>
                <ul>
                    <li>Rollup dropdown in Trial Balance report shows only validated rollups. Presentation of rollup hierarchy simplified.</li>
                    <li>Formatted columns in Distribution as Text</li>
                    <li>Reduced column definitions in Report Templates to not use all columns</li>
                    <li>Drill to Rollups tab clears out filters to start with blank template</li>
                    <li>Various formatting changes in the subscription</li>
                    <li>Add prefix in summary rollup 2 to include rollup name</li>
                    <li>Remove FRx parameter from Template</li>
                    <li>Added 10 char. limit to Row Template Code name and validation</li>
                    <li>Remove double line subtotals in generated templates</li>
                    <li>Added Data Pull on Distribution filter to Distribution tab (prep or run), unhide some columns</li>
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
> In SQL Management Studio, run the script labeled **Rollback to 1.0.11** at the top of this page.
>
> Run \[Interject_SetupScript1_Security\], as shown below, to re-enable security.
>
>  ```SQL
> EXEC [Custom].[Interject_SetupScript1_Security]
>	@MasterEpicorDatabase = 'samplemasterdb'
>	,@CertificatePassword =  'myPassword1234'
>  ```
>

</div>


<button class="collapsible"><strong>For Users With Version 1.0.10</strong></button>
<div markdown="1" class="panel">

<table>
    <tr>
        <th><span style="font-weight:bold">Update for Previous Install:</span> <a href="https://drive.google.com/file/d/16E2th5xN__y7gyBiJ4HHbxAD1kjcuufi/view?usp=sharing">from1.0.10to1.1.0_Update.Interject_Reporting.SQL</a></th>
    </tr>
    <tr>
        <th><span style="font-weight:bold">Rollback to 1.0.10:</span> <a href="https://drive.google.com/file/d/1ZaDnrP-v40aTh7NBH8mbvO3oDIY230G3/view?usp=sharing">from1.1.0to1.0.10_Rollback.Interject_Reporting.SQL</a></th>
    </tr>
</table>

### Current Version Notes
<table>
    <tr>
        <th><span style="font-weight:bold">Interject for Financials - Current Version 1.1.0: </span></th>
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
                    <li>Separate Validated Rollup add non-account option in the Config Mgr</li>
                    <li>Add Posted and Unposted options in the Trial Balance</li>
                    <li>Add Reference Code to JEQuery tool</li>
                    <li>Add sign reversal to templates and fincube</li>
                    <li>Added Last Run indication in generated templates</li>
                    <li>Added 3 drills to the Trial Balance from generated templates</li>
                </ul>    
            </td>
            <td>
                <ul>
                    <li>Rollup dropdown in Trial Balance report shows only validated rollups. Presentation of rollup hierarchy simplified.</li>
                    <li>Formatted columns in Distribution as Text</li>
                    <li>Reduced column definitions in Report Templates to not use all columns</li>
                    <li>Drill to Rollups tab clears out filters to start with blank template</li>
                    <li>Various formatting changes in the subscription</li>
                    <li>Add prefix in summary rollup 2 to include rollup name</li>
                    <li>Remove FRx parameter from Template</li>
                    <li>Added 10 char. limit to Row Template Code name and validation</li>
                    <li>Remove double line subtotals in generated templates</li>
                    <li>Added Data Pull on Distribution filter to Distribution tab (prep or run), unhide some columns</li>
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

</div>

<button class="collapsible"><strong>For Users With Version 1.0.9</strong></button>
<div markdown="1" class="panel">

<table>
    <tr>
        <th><span style="font-weight:bold">Update for Previous Install:</span> <a href="https://drive.google.com/file/d/1STLy6y3Nq07yf8EoAUk1dzuyTQgNpXTa/view?usp=sharing">from1.0.9to1.1.0_Update.Interject_Reporting.SQL</a></th>
    </tr>
    <tr>
        <th><span style="font-weight:bold">Rollback to 1.0.9:</span> <a href="https://drive.google.com/file/d/1fH515EWwaDaFO14ALGWCVyDOVZ-akSQD/view?usp=sharing">from1.1.0to1.0.9_Rollback.Interject_Reporting.SQL</a></th>
    </tr>
</table>

### Current Version Notes
<table>
    <tr>
        <th><span style="font-weight:bold">Interject for Financials - Current Version 1.1.0: </span></th>
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
                    <li>Separate Validated Rollup add non-account option in the Config Mgr</li>
                    <li>Add Posted and Unposted options in the Trial Balance</li>
                    <li>Add Reference Code to JEQuery tool</li>
                    <li>Add sign reversal to templates and fincube</li>
                    <li>Added Last Run indication in generated templates</li>
                    <li>Added 3 drills to the Trial Balance from generated templates</li>
                </ul>    
            </td>
            <td>
                <ul>
                    <li>Rollup dropdown in Trial Balance report shows only validated rollups. Presentation of rollup hierarchy simplified.</li>
                    <li>Formatted columns in Distribution as Text</li>
                    <li>Reduced column definitions in Report Templates to not use all columns</li>
                    <li>Drill to Rollups tab clears out filters to start with blank template</li>
                    <li>Various formatting changes in the subscription</li>
                    <li>Add prefix in summary rollup 2 to include rollup name</li>
                    <li>Remove FRx parameter from Template</li>
                    <li>Added 10 char. limit to Row Template Code name and validation</li>
                    <li>Remove double line subtotals in generated templates</li>
                    <li>Added Data Pull on Distribution filter to Distribution tab (prep or run), unhide some columns</li>
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
> In SQL Management Studio, run the script labeled **Rollback to 1.0.9** at the top of this page.
>
> Run \[Interject_SetupScript1_Security\], as shown below, to re-enable security.
>
>  ```SQL
> EXEC [Custom].[Interject_SetupScript1_Security]
>	@MasterEpicorDatabase = 'samplemasterdb'
>	,@CertificatePassword =  'myPassword1234'
>  ```
>

</div>
