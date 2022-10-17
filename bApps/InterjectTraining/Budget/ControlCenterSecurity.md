---
title: Tools Controlled by the Control Center
layout: custom
keywords: [Training, Budget, Control Center]
description: 
---

## Overview

The Control Center handles access rights for the **Budget Template**, **Budget Upload**, **Capital Input**, **Projections Template**, and **Projections Upload** tools. This page details where to find the District Position Assignment, where in each tool you can find the tool's lock level, the messages you'll see if trying to save outside your access rights, and the special circumstance of Regional Controllers for the Budget Tool.


### Do I have security rights to use these tools?

Only people in the District Position Assignment (DPA) for the District in Toolbox can use the **Budget Template**, **Budget Upload**, and **Capital Input** tools. Your Division Controller can add you if you are not already in the DPA. This can be found in the toolbox at the following location:

![](/images/WCNTraining/Capital/CapitalInput_DPANavigation.png)

![](/images/WCNTraining/Capital/CapitalInput_DPAWindow.png)

### Budget Tools and the Control Center

Based on your position in the DPA for the district, you will have a certain level of access to these reports. Levels you may be on include: **A/C**, **Dist**, **Div**, **Reg**, or **Corp**.

Both **Budget** tools are locked in **column N** of the [Control Center](/bApps/InterjectTraining/Budget/ControlCenter.html). In the example below, District 2050 is locked at the Reg Level.

![](/images/WCNTraining/Budget/BudgetUpload_ControlCenter1District.png)

If an A/C level user tried saving to 2050 Budget, they would be stopped with one of the following messages.

![](/images/WCNTraining/Budget/BudgetTemplate_LockLevelError.png)
![](/images/WCNTraining/Budget/BudgetUpload_LockLevel1District.png)

You are able to save Budget as long as the Budget lock level is your level or below. Otherwise you will not be able to save Budget.

>**Budget Upload Tool - Region Controllers - Multiple Lock Levels**<br>
>As a Region Controller, you are able to save to multiple districts at once. However, it is possible to have one of the districts locked at Corp above you.
>![](/images/WCNTraining/Budget/BudgetUpload_ControlCenter2Districts.png)
>If a Region Controller tries saving to these two districts at the same time, the save will stop and they will see the following error:
>![](/images/WCNTraining/Budget/BudgetUpload_LockLevel2Districts.png)
>For the Region Controller to edit, 2041 would need to be unlocked to Reg. Otherwise, to edit 2050 they would need to remove the 2041 row(s).

## Capital Input Tool and the Control Center

Based on your position in the DPA for the district, you will have a certain level of access to this report. You may be on one of the following levels: **A/C**, **Dist**, **Div**, **Reg**, or **Corp**.

**Capital** locks are hidden in **column AH** of the [Control Center](/bApps/InterjectTraining/Budget/ControlCenter.html). In the example below, District 2050 is locked at the Corp Level.

![](/images/WCNTraining/Capital/CapitalInput_ControlCenterLockLevel.png)

If an A/C level user tries saving to 2050 Capital, they will be stopped with the following message.

![](/images/WCNTraining/Capital/CapitalInput_Error_LockLevel.png)

You are able to save Capital as long as the Capital lock level is your level or below. Otherwise you will not be able to save Capital.

## Projections Tools and the Control Center

Based on your position in the DPA for the district, you will have a certain level of access to these reports. Levels you may be on include: **A/C**, **Dist**, **Div**, **Reg**, or **Corp**.

Both **Projections** tools are locked in **column G** of the [Control Center](/bApps/InterjectTraining/Budget/ControlCenter.html). In the example below, District 2041 is locked at the Reg Level.

![](/images/WCNTraining/Projections/ProjectionUpload_ControlCenter1District.png)

If an A/C level user tried saving to 2041 Projections, they would be stopped with one of the following messages.

![](/images/WCNTraining/Projections/ProjectionTemplate_LockLevelError.png)
![](/images/WCNTraining/Projections/ProjectionUpload_LockLevel1District.png)

You are able to save Projections as long as the Projections lock level is your level or below. Otherwise you will not be able to save Projections.

>**Projections Upload Tool - Region Controllers - Multiple Lock Levels**<br>
>As a Region Controller, you are able to save to multiple districts at once. However, it is possible to have one of the districts locked at Corp above you.
>![](/images/WCNTraining/Projections/ProjectionUpload_ControlCenter2Districts.png)
>If a Region Controller tries saving to these two districts at the same time, the save will stop and they will see the following error:
>![](/images/WCNTraining/Projections/ProjectionUpload_LockLevel2Districts.png)
>For the Region Controller to edit, 2041 would need to be unlocked to Reg. Otherwise, to edit 2041 they would need to remove the 2050 row(s).