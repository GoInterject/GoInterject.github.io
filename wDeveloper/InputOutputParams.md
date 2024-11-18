---
title: Interject Input/Output Parameters
filename: ""
layout: custom
keywords: []
headings: ["Overview"]
links: []
image_dir: ""
images: [
    {file: "", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}
]
description: 
---
* * *

## Overview

Interject can send parameters from the Excel report to the Stored Procedure through the use of Data Portals. Parameters can also be sent from the Stored Procedure to Interject to be displayed in the Excel report.

parameters can be set up in the Excel report. these parameters can be used to filter the data coming into the report.

Depending on the function, you can set up the cells that will be the parameters to be sent to the SP. for example, the ReportRange function has an argument called "Parameters" that you can list several cells as parameters. These cells need to be listed inside an Interject "Param" function.

Data portals are set up to connect the Interject Add-in to a data source. Parameters are set up in these portals to match the parameters in your Excel report. They must be set up in the same order as they are listed in your Interject function.


There are also system parameters that can be set up in the Portal that Interject will automatically send to the stored procedure.

The following diagram describes the flow of parameters to and from the data source:

![](/images/InputOutputParameters/ParameterFlow.png)
<br>


All the parameters must match.

Parameters in Report:

![](/images/InputOutputParameters/ParamsInReport.png)
<br>

Parameters in Portal:

![](/images/InputOutputParameters/ParamsInPortal.png)
<br>

Parameters in Stored Procedure:

![](/images/InputOutputParameters/ParamsInProcedure.png)
<br>


### Output Parameters

