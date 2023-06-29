### TEST 16: Drill To An Altered Macro File

This drill is the same as the previous two tests. However, you will setup the TargetDrill file as a link/network file and then alter it before drilling to it.

**Actions:**

*  Login to Interject
*  Upload and setup drill for report
*  Alter the TargetDrill file
*  Open "ReportDrill.xlsx" file
*  Run drill

**Step 1:** Login to Interject with the following credentials:

![](/images/Testing/LoginAdminS.png)
<br>

**Step 2:** Open the Report Library and create a new link:

![](/images/Testing/UploadTargetDrillLink.png)
<br>

**Step 3:** Click &lt;Browse&gt; and navigate to "STargetDrillLink.xlsm" and click &lt;Open&gt; and then &lt;Save&gt; the link:

![](/images/Testing/BrowseTargetDrillLink.png)
<br>

**Step 4:** Open the file "STargeDrillLink.xlsm" and make a change:

![](/images/Testing/ChangeSTargetDrill.png)
<br>

**Step 5:** Save and close the file. Open the file "SReportDrillLink.xlsm". Ensure the cursor is in cell **E21** and run an Interject Drill:

![](/images/Testing/CustomerDrill.png)
<br>

_Verify_ the error message displays and take a screenshot:

![](/images/Testing/Error07Drill.png)
<br>

**Step 6:** Execute the same tests for the Macro Test Co - External API.

**Summary of Tests**

| ID | Company | Filename | Report Name | Test Description | Verify | 
|----|----|----|----|----|
| 16&#8209;1 | Macro Sign Key | STargetDrill.xlsm | TargetDrill | Drill to macro file link after it has been changed in cache | Unable to open macro file by drilling to it | 
| 16&#8209;2 | Macro API | ATargetDrill.xlsm | TargetDrill | Drill to macro file link after it has been changed in cache | Unable to open macro file by drilling to it | 

<br>