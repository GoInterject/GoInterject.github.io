---
title: INTERJECT Financials - Epicor -Update Manager
layout: custom
keywords: [Account, Epicor, Companies]
description: INTERJECT™ Financials for Epicor Enterprise (This would cover topics that are specific to integration with Epicor Enterprise, and would potentially be different for each ERP) 
---

<h2>Interject Financials - Epicor <br>
<<<<<<< HEAD
<a href="https://drive.google.com/file/d/1LcWA2kEjOglb8U52reS5api4D9XzG0Xx/view?usp=sharing">Latest Version 1.2.1</a></h2>
=======
<a href="https://drive.google.com/file/d/1uNCX3lv0AjI4K23gRG2sL3VfCH6B971y/view?usp=sharing">Latest Version 1.2.3</a></h2>
>>>>>>> ab08e03f810ace9a20ff4023b63a8d204bc4eee0

Depending on which version of Interject Financials you're running, there are different update and rollback scripts. Before updating or rolling back a version, follow the procedure below. Once you know the version you're currently running, click on the appropriate dropdown below for the update release notes, the correct scripts for updating and rolling back versions, as well as procedures for running those scripts.

### To Check for Your Current Version

After the inital instal, applying an update, or performing a rollback, you can confirm that your version is correct by:
- Going to the **Report Library**
- Opening the **Configuration Manager**
- Checking the **Database Version** in the upper right of the report
<br>
![Database Version](/images/A-InitialDataLoad/VersionConfirm.png){: .center-image } 

### Click Your Version Below for Release Notes and Update Scripts


<<<<<<< HEAD
<button class="collapsible"><strong>For Users With Version 1.2.0</strong></button>
=======
<button class="collapsible"><strong>For Users With Version 1.2.2</strong></button>
>>>>>>> ab08e03f810ace9a20ff4023b63a8d204bc4eee0
<div markdown="1" class="panel">

<table> 
    <tr>
<<<<<<< HEAD
        <th><span style="font-weight:bold">Update for Previous Install:</span> <a href="https://drive.google.com/file/d/1yqfod_Ggds7PjZPPf_UdnrIOh9_zfJlU/view?usp=sharing">from1.2.0to1.2.1_Update.Interject_Reporting.SQL</a></th>
    </tr>
    <tr>
        <th><span style="font-weight:bold">Rollback to 1.2.0:</span> <a href="https://drive.google.com/file/d/16Sy5BFKh-egNY_D1cuJgkJAjFeSjTpAI/view?usp=sharing">from1.2.1to1.2.0_Rollback.Interject_Reporting.SQL</a></th>
=======
        <th><span style="font-weight:bold">Update for Previous Install:</span> <a href="https://drive.google.com/file/d/1HRY_AnEd--GAvGsQOOwk39rSR9flZz3N/view?usp=sharing">from1.2.2to1.2.3_Update.Interject_Reporting.SQL</a></th>
    </tr>
    <tr>
        <th><span style="font-weight:bold">Rollback to 1.2.2:</span> <a href="https://drive.google.com/file/d/1nx6lc3oI3frgSGgz7o1Zm8eRxWLUTi9f/view?usp=sharing">from1.2.3to1.2.2_Rollback.Interject_Reporting.SQL</a></th>
>>>>>>> ab08e03f810ace9a20ff4023b63a8d204bc4eee0
    </tr>
</table>

### Current Version Notes
<table>
    <tr>
<<<<<<< HEAD
        <th><span style="font-weight:bold">Interject for Financials - Current Version 1.2.1 </span></th>
    </tr>
        <tr> 
        <th><span style="font-weight:bold">Bugs Fixed</span></th>
        </tr>
        <tr> 
            <td>
                <ul>
                    <li>Fix security certificate.</li> 
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
> In SQL Management Studio, run the script labeled **Rollback to 1.2.0** at the top of this page.
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



<button class="collapsible"><strong>For Users With Version 1.1.0</strong></button>
<div markdown="1" class="panel">

<table> 
    <tr>
        <th><span style="font-weight:bold">Update for Previous Install:</span> <a href="https://drive.google.com/file/d/1yqfod_Ggds7PjZPPf_UdnrIOh9_zfJlU/view?usp=sharing">from1.1.0to1.2.1_Update.Interject_Reporting.SQL</a></th>
    </tr>
    <tr>
        <th><span style="font-weight:bold">Rollback to 1.1.0:</span> <a href="https://drive.google.com/file/d/16Sy5BFKh-egNY_D1cuJgkJAjFeSjTpAI/view?usp=sharing">from1.2.1to1.1.0_Rollback.Interject_Reporting.SQL</a></th>
    </tr>
</table>

### Current Version Notes
<table>
    <tr>
        <th><span style="font-weight:bold">Interject for Financials - Current Version 1.2.1 </span></th>
=======
        <th><span style="font-weight:bold">Interject for Financials - Current Version 1.2.3 </span></th>
>>>>>>> ab08e03f810ace9a20ff4023b63a8d204bc4eee0
    </tr>
        <tr>
        <th><span style="font-weight:bold">Features</span></th>
        <th><span style="font-weight:bold">Bugs Fixed</span></th>
        </tr>
        <tr>
            <td>
                <ul>
<<<<<<< HEAD
                    <li>Distributions will allow users to combinate full account with another segment.</li> 
                </ul>     
            </td>
            <td>
                <ul>
                    <li>Drill-down from Fincube reports to Trial Balance reports will work with full account groupings.</li> 
=======
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
>>>>>>> ab08e03f810ace9a20ff4023b63a8d204bc4eee0
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
<<<<<<< HEAD
>	@MasterEpicorDatabase = 'samplemasterdb'
=======
>	@MasterEpicorDatabase = '<Epicor Controlling Database Name>'
>>>>>>> ab08e03f810ace9a20ff4023b63a8d204bc4eee0
>	,@CertificatePassword =  'myPassword1234'
>  ```
>

### Rolling Back One Version

The following steps must be taken to roll back one version. Note that this will only roll to the previous version.

> To Roll Back
>
<<<<<<< HEAD
> In SQL Management Studio, run the script labeled **Rollback to 1.1.0** at the top of this page.
=======
> In SQL Management Studio, run the script labeled **Rollback to 1.2.3** at the top of this page.
>>>>>>> ab08e03f810ace9a20ff4023b63a8d204bc4eee0
>
> Run \[Interject_SetupScript1_Security\], as shown below, to re-enable security.
>
>  ```SQL
> EXEC [Custom].[Interject_SetupScript1_Security]
<<<<<<< HEAD
>	@MasterEpicorDatabase = 'samplemasterdb'
=======
>	@MasterEpicorDatabase = '<Epicor Controlling Database Name>'
>>>>>>> ab08e03f810ace9a20ff4023b63a8d204bc4eee0
>	,@CertificatePassword =  'myPassword1234'
>  ```
>

</div>


<<<<<<< HEAD
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
=======

<button class="collapsible"><strong>For Users With Version 1.2.1</strong></button>
<div markdown="1" class="panel">

<table> 
    <tr>
        <th><span style="font-weight:bold">Update for Previous Install:</span> <a href="https://drive.google.com/file/d/1PFeGtZrb4g1VBxslKK99RCoQLUgmNvZV/view?usp=sharing">from1.2.1to1.2.3_Update.Interject_Reporting.SQL</a></th>
    </tr>
    <tr>
        <th><span style="font-weight:bold">Rollback to 1.2.1:</span> <a href="https://drive.google.com/file/d/1ST6DTqqeaVakFJWz5B96fVbzS6cB1eH0/view?usp=sharing">from1.2.3to1.2.1_Rollback.Interject_Reporting.SQL</a></th>
>>>>>>> ab08e03f810ace9a20ff4023b63a8d204bc4eee0
    </tr>
</table>

### Current Version Notes
<table>
    <tr>
<<<<<<< HEAD
        <th><span style="font-weight:bold">Interject for Financials - Current Version 1.1.0 </span></th>
=======
        <th><span style="font-weight:bold">Interject for Financials - Current Version 1.2.3 </span></th>
>>>>>>> ab08e03f810ace9a20ff4023b63a8d204bc4eee0
    </tr>
        <tr>
        <th><span style="font-weight:bold">Features</span></th>
        <th><span style="font-weight:bold">Bugs Fixed</span></th>
        </tr>
        <tr>
            <td>
                <ul>
<<<<<<< HEAD
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
=======
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
>>>>>>> ab08e03f810ace9a20ff4023b63a8d204bc4eee0
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
<<<<<<< HEAD
>	@MasterEpicorDatabase = 'samplemasterdb'
=======
>	@MasterEpicorDatabase = '<Epicor Controlling Database Name>'
>>>>>>> ab08e03f810ace9a20ff4023b63a8d204bc4eee0
>	,@CertificatePassword =  'myPassword1234'
>  ```
>

### Rolling Back One Version

The following steps must be taken to roll back one version. Note that this will only roll to the previous version.

> To Roll Back
>
<<<<<<< HEAD
> In SQL Management Studio, run the script labeled **Rollback to 1.0.11** at the top of this page.
=======
> In SQL Management Studio, run the script labeled **Rollback to 1.2.1** at the top of this page.
>>>>>>> ab08e03f810ace9a20ff4023b63a8d204bc4eee0
>
> Run \[Interject_SetupScript1_Security\], as shown below, to re-enable security.
>
>  ```SQL
> EXEC [Custom].[Interject_SetupScript1_Security]
<<<<<<< HEAD
>	@MasterEpicorDatabase = 'samplemasterdb'
=======
>	@MasterEpicorDatabase = '<Epicor Controlling Database Name>'
>>>>>>> ab08e03f810ace9a20ff4023b63a8d204bc4eee0
>	,@CertificatePassword =  'myPassword1234'
>  ```
>

</div>

<<<<<<< HEAD

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
=======
>>>>>>> ab08e03f810ace9a20ff4023b63a8d204bc4eee0
