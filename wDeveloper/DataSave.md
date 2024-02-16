---
title: Data Save
filename: "DataSave.md"
layout: custom
keywords: [data, save, develop, build, create]
headings: ["Overview", "Editing Data Save", "Insert & Delete Data Save", "Changelog Data Save"]
links: ["/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#save-data", "/wDeveloper/L-Dev-EditingDataSave.html", "/wGetStarted/L-Dev-CustomerAging.html", "/wDeveloper/L-Dev-InsertDeleteDataSave.html", "/wDeveloper/L-Dev-ChangelogDataSave.html"]
image_dir: ""
images: []
description: 
---
* * *

## Overview

Interject allows for data transfer both between a data source and the Excel report. With the [Save Data](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#save-data), you can update the data source by editing the report and uploading the changes directly. In order to harness this feature, you will need to set up a number of things such as a data connection, data portal, and a stored procedure as well as the report itself. These examples will walk you through how to do this.

It is expected that these examples will be completed in order as they each build upon the other.

### [Editing Data Save](/wDeveloper/L-Dev-EditingDataSave.html)

In this example you will build from the previous [Data Pull report](/wGetStarted/L-Dev-CustomerAging.html). Here, you will walkthrough the steps in order to Save Data using the Interject function ReportSave. This function makes it convenient to modify the data source right inside of your Excel report without having to edit the data source directly. In this Editing Data Save example, you will set up a data save that will allow you to edit a customer's contact name and title right from within the Excel report.

### [Insert & Delete Data Save](/wDeveloper/L-Dev-InsertDeleteDataSave.html)

In this example you will modify the previous Editing Data Save, which was set up to edit a customer's contact name and title. In this Insert & Delete Data Save, you will walkthrough the steps to edit all the columns. In addition, you will also include the ability to insert or delete a customer from within the Excel report.

### [Changelog Data Save](/wDeveloper/L-Dev-ChangelogDataSave.html)

In this example you will modify the previous Insert & Delete Data Save, which was set up to insert and delete customers. In this Change Log Data Save, you will modify the Stored Procedure again to include a change log. A change log is basically an additional table in the database that will record all the changes that take place to the targeted table. This history table keeps track of what records and columns were changed, what type of change took place (e.g. update, insert, deleted, added), who performed the change and the date and time it took place. It also keeps track of the old values that were changed so you can compare the old with the new values and recover data if desired.
