---
title: Interject Hyperlinks
layout: custom
keywords: [links, hyperlinks]
description: Interject provides a way to perform some of the basic Interject functions by clicking on a link within the report.
---
* * *

##  **Overview**

Interject provides a way to perform some of the basic Interject functions and commands by clicking on a link within the report. This makes it convenient to customize your report to preform commonly used functions and commands by the click of a button. 

### **Hyperlink List**

This feature only works if the correct Screen Tip is entered for the link. The following lists the types of operations this feature supports:

| Screen Tip | Function to Reference | Details |
|------|------|------|
| "Interject Dropdown" | [jDropdown Function](/wIndex/jDropdown.html) | Executes a jDropdown Function (see [here](/wGetStarted/L-Create-Dropdowns.html) for an example)|
| "Interject Drill" | [Data Drill Function](/wIndex/ReportDrill.html) | Opens up the [Data Drill](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#drill-on-data) window |
| "Interject Return From Drill" | n/a | [Returns From Drill](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#return-from-drill) |
| "Interject Pull" | [Data Pull Function](/wIndex/Data-Functions-Landing.html) | Opens up the [Pull Data](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#pull-data) window |
| "Interject Save" | [Data Save Function](/wIndex/ReportSave.html) | Opens up the [Data Save](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#save-data) window |
| "Interject Report Library" | n/a | Opens up the [Report Library](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#report-library) window |

<!---
| "Interject Execute jAction" | jAction Function | Executes jAction Function |
--->

For a convenient way to create an Interject Hyperlink via the Quick Tools menu, see [QuickTools - Hyperlink](/wIndex/QuickTools-Hyperlink.html).

### **Creating An Example Pull Link**

To see how this feature works, open up a report and type "Pull Data" into an empty cell.

![](/images/Link-Index/00.png)   
<br>

Next, right click that cell and click on "Link" and then "Insert Link".

![](/images/Link-Index/01.png)   
<br>

In the Insert Hyperlink window, click "Place in This Document" and type in the cell reference to the Report Function within the report. Finally click "ScreenTip".

![](/images/Link-Index/02.png)   
<br>

In the ScreenTip text, enter "Interject Pull" and click "OK" to get back to the report.

![](/images/Link-Index/03.png)   
<br>

Now when you click on the link, it opens up the Pull Data window.

![](/images/Link-Index/04.png)   
<br>
