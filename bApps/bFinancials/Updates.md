---
title: Interject Financials - Epicor - Update Manager
filename: "Updates.md"
layout: custom
keywords: [Account, Epicor, Companies]
headings: ["To Check for Your Current Version", "Click Your Version Below for Release Notes and Update Scripts", "Current Version Notes", "Updating", "Rolling Back One Version"]
links: ["https://drive.google.com/file/d/1yqewNlhX4tm5jDo-J1lnEjz8qe-w9gqO/view?usp=sharing", "/images/A-InitialDataLoad/VersionConfirm.png", "https://drive.google.com/file/d/1b6VJploEafuftn9UP9Mqdt4F7ywbsqju/view?usp=sharing", "https://drive.google.com/file/d/1jcotjzfZnS9Pn7lR2BguVpzhfoSYzBGa/view?usp=sharing", "https://drive.google.com/file/d/1Ol_mK9cseyhOwuzZ45FQiIuJAA75ETNt/view?usp=sharing", "https://drive.google.com/file/d/1QE_3izgZQwMjCFgWubGv0C5wKAgiTAUV/view?usp=sharing", "https://drive.google.com/file/d/18nGnIljPN9mgxxUaQRGMj5G7t1MBiUtH/view?usp=sharing", "https://docs.gointerject.com/bApps/bFinancials/Technical-Install.html"]
image_dir: "A-InitialDataLoad"
images: [
	{file: "VersionConfirm", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}
	]
description: Interject™ Financials for Epicor Enterprise (This would cover topics that are specific to integration with Epicor Enterprise, and would potentially be different for each ERP)
---

<h2>Interject Financials - Epicor Enterprise<br>
<a href="https://github.com/GoInterject/FinancialPackage/releases/tag/v1.7.9">Latest Version 1.7.9</a></h2>

Depending on which version of Interject Financials you're running, there are different update and rollback scripts. Before updating or rolling back a version, follow the procedure below. Once you know the version you're currently running, click on the appropriate dropdown below for the update release notes, the correct scripts for updating and rolling back versions, as well as procedures for running those scripts.

### To Check for Your Current Version

After the inital install, applying an update, or performing a rollback, you can confirm that your version is correct by:

- Going to the **Report Library**
- Opening the **Configuration Manager**
- Checking the **Database Version** in the upper right of the report
  <br>
  ![Database Version](/images/A-InitialDataLoad/VersionConfirm.png){: .center-image }

### Click Your Version Below for Release Notes and Update Scripts

<button class="collapsible"><strong>For Users With Version 1.6.X-1.7.9</strong></button>

<div markdown="1" class="panel">
<table> 
    <tr>
        <th><span style="font-weight:bold">Update for Previous Install:</span> <a href="https://drive.google.com/file/d/1b6VJploEafuftn9UP9Mqdt4F7ywbsqju/view?usp=sharing">from1.6.X-1.7.8to1.7.9_Update.Interject_Reporting.SQL</a></th>
    </tr>  
    <tr>
        <th><i>There are currently no rollback scripts available for 1.7.*</i></th>
    </tr>
</table>
</div>

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

</div>

### Current Version Notes

<table>
    <tr>
    <th><span style="font-weight:bold">Interject for Financials - Current Version 1.7.9 </span></th>
    <tr>
        <th><span style="font-weight:bold">Features</span></th>
        <th><span style="font-weight:bold">Bugs Fixed</span></th>
    </tr>
    <tr>
        <td>
            <ul>
                <li>Enhance the speed of the trial balance through optimization.</li>
                <li>Improve the process of adding new rollups for increased efficiency.</li>
                <li>Add option for alternative segment names in dropdowns.</li>
                <li>Introduce an Onhold option for Journal Entry Query.</li>
                <li>Implement a daily reset for the change queue.</li>
                <li>Expanded the upload field and trimmed blank spaces in the JE Export tool.</li>
            </ul>
        </td>
        <td>
            <ul>
                <li>Resolve the issue related to fiscal year period alignment in live pull.</li>
                <li>Fix recursion issue for JE upload.</li>
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
> ```SQL
> EXEC [Setup].[Interject_SetupScript1_Security]
> 	@MasterEpicorDatabase = '<Epicor Controlling Database Name>'
> 	,@CertificatePassword =  'myPassword1234'
> ```

### Rolling Back One Version

The following steps must be taken to roll back one version. Note that this will only roll to the previous version.

> To Roll Back
>
> In SQL Management Studio, run the script labeled **Rollback to 1.3.1** at the top of this page.
>
> Run \[Interject_SetupScript1_Security\], as shown below, to re-enable security.
>
> ```SQL
> EXEC [Setup].[Interject_SetupScript1_Security]
> 	@MasterEpicorDatabase = '<Epicor Controlling Database Name>'
> 	,@CertificatePassword =  'myPassword1234'
> ```
