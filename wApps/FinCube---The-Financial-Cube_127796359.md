---
title: Interject Documentation > FinCube - The Financial Cube
layout: custom
---

## **Overview**

The FinCube is a single Dataportal that supports a wide variety of reporting needs. It is included as part of the INTERJECT Financials for Spreadsheets application, and many of the segments can be customized for specific needs. In some ways, when combined with INTERJECT, this Dataportal report feature works like a pivot table with increased format and structure control. It is more manageable when scaling to hundreds of users.

Typically, FinCube is used for consolidated financial reports, including monthly trends, YTD comparisons, budgeting templates, and simple balance inquiries. Because of its scalability, FinCube may support up to 70% of a company's financial reporting formats.

<span style="color: rgb(0,0,0);">There are a number of components discussed on this page, and you can go directly to any part by clicking one of the links below.</span>

*   ### [Segment Filter Options](#FinCube-TheFinancialCube-SegFil)

*   ### [Dataportal Parameters](#FinCube-TheFinancialCube-DataParam)

*   ### [Segment Columns](#FinCube-TheFinancialCube-SegCol)

*   ### [Group Columns](#FinCube-TheFinancialCube-GroupCol)

*   ### [Amount Columns](#FinCube-TheFinancialCube-AmountCol)

    1.  #### [CYA Column Notation](#FinCube-TheFinancialCube-CYACol)

    2.  #### [ACT Column Notation](#FinCube-TheFinancialCube-ACTCol)

    3.  #### [jColumnDef() Column Notation](#FinCube-TheFinancialCube-JColDef)

<span class="confluence-anchor-link" id="FinCube-TheFinancialCube-SegFil"></span>

### Segment Filter Options

Before each parameter is described  that can be used in a spreadsheet report, it is important to discuss the common filters that can be used. The first 12 segments share a similar data filtering syntax. The following options are explained using an Account and Period segment.

**Filter for multiple items:** For account, use **21200,21300** to filter for both accounts 21200 and 21300\. For Period, use **1,2,3** to represent quarter 1\. There are groupings already set up for quarters, so Qtr1 also works (more detail follows). Using the comma, each addition is considered an **OR** , which means each element is not mutually exclusive. Every new element added with a comma will add more data to the filter.  

**Filter for a range of items:** For account, use **21000..22000** to filter for all accounts in that range. The same is true for periods, such as **1..3** .  

**Filter for multiple ranges:** Combine both #1 and #2 above and expand the filters, such as **21000..22000,30000..32000** . This will filter for both ranges noted.  

**Filter by excluding items:** In some cases, it may be easier to use a range and exclude a few items. With account, use **21000..22000** , then exclude account 21500 using the notation **21000..22000,!21500** . The exclamation excludes that element. A range may also be excluded using **21000..22000,!21050..21060** .  

**Filter using wildcards:** Use wildcards, such as ***** or **?** , to find matches for filters. For example, noting **21*** will retrieve all accounts beginning with 21, such as 21000 to 21999\. Using **21?00** as the filter will retrieve accounts like 21000, 21100, 21200, and 21300\. These wildcards can be used together with the methods noted in #1, #3, and #4 above. For example **2*,*09,!*08** would return all accounts starting with 2 and any accounts ending with 09 but exclude accounts that end with 08.  

**Filter with Groups:** Groups are an important feature that make filtering easier and more manageable. The management of groups will be covered in a different page, but they are defined as a text string representing a filter. For example, instead of using a filter for **21000..22000** , set up a group called **Accounts Payable** to represent that filter. And if you set up a group for the filter **30000..32000** , and call it **Long Term Liabilities** , you can use a filter like **Accounts Payable, Long Term Liabilities** to get the defined accounts. There are preset groups for the **Segment 9--Period** parameter for Qtr1, and more can be added for monthly periods. The exclude option in #4 above can also be used, such as when you want to see Revenue accounts but exclude Intercompany clearing accounts. This could be noted as **Revenue,!Intercompany** .

<span class="confluence-anchor-link" id="FinCube-TheFinancialCube-DataParam"></span>

### DataPortal Parameters

The table below summarizes parameters available for the FinCube DataPortal. Parameters can either be filters set up by spreadsheet users, or they can place data in the spreadsheet. Each parameter links to a spreadsheet cell, or they can be manually specified in the reporting formula if not used in the report. The first 8 parameters of FinCube represent customizable segments. They are typically set up to match a company's chart of account segments and may include other reporting dimensions like companies or currencies.

The table below explains each of the available parameters of the FinCube DataPortal. The example column shows what the typical segment signification, but note that these can be configured differently for every INTERJECT installation.

<div class="table-wrap">

<table class="relative-table wrapped confluenceTable" style="width: 90.7013%;"><colgroup><col style="width: 21.7304%;"> <col style="width: 9.12899%;"> <col style="width: 69.1406%;"></colgroup> 

<tbody>

<tr>

<th class="confluenceTh">Parameter Name</th>

<th class="confluenceTh" colspan="1">

Example

</th>

<th class="confluenceTh">Description</th>

</tr>

<tr>

<td class="confluenceTd">

Segment 1

</td>

<td class="confluenceTd" colspan="1">Account</td>

<td class="confluenceTd">This parameter can be used for filtering as noted in the above section.</td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">Segment 2</td>

<td class="confluenceTd" colspan="1">District</td>

<td class="confluenceTd" colspan="1">

<span>This parameter can be used for filtering as noted in the above section.</span>

</td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">Segment 3</td>

<td class="confluenceTd" colspan="1">System</td>

<td class="confluenceTd" colspan="1"><span>This parameter can be used for filtering as noted in the above section.</span></td>

</tr>

<tr>

<td class="confluenceTd" colspan="1"><span style="color: rgb(0,0,0);">Segment 4</span></td>

<td class="confluenceTd" colspan="1">SubSystem</td>

<td class="confluenceTd" colspan="1"><span>This parameter can be used for filtering as noted in the above section.</span></td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">Segment 5</td>

<td class="confluenceTd" colspan="1">Adjustments</td>

<td class="confluenceTd" colspan="1"><span>This parameter can be used for filtering as noted in the above section.</span></td>

</tr>

<tr>

<td class="confluenceTd" colspan="1"><span style="color: rgb(0,0,0);">Segment 6</span></td>

<td class="confluenceTd" colspan="1">  
</td>

<td class="confluenceTd" colspan="1"><span>This parameter can be used for filtering as noted in the above section.</span></td>

</tr>

<tr>

<td class="confluenceTd" colspan="1"><span style="color: rgb(0,0,0);">Segment 7</span></td>

<td class="confluenceTd" colspan="1">Company</td>

<td class="confluenceTd" colspan="1">

<span>This parameter can be used for filtering as noted in the above section.</span>

</td>

</tr>

<tr>

<td class="confluenceTd" colspan="1"><span style="color: rgb(0,0,0);">Segment 8</span></td>

<td class="confluenceTd" colspan="1">Currency</td>

<td class="confluenceTd" colspan="1">

<span>This parameter can be used for filtering as noted in the above section.</span>

</td>

</tr>

<tr>

<td class="confluenceTd"><span style="color: rgb(0,0,0);">Segment 9 - Period</span></td>

<td class="confluenceTd" colspan="1">  
</td>

<td class="confluenceTd">This segment is locked to represent a period (a month). It can be 1 through 12 or YTD1 through YTD12\. Groups can be used to define Quarters.</td>

</tr>

<tr>

<td class="confluenceTd">Segment 10 - Year</td>

<td class="confluenceTd" colspan="1">  
</td>

<td class="confluenceTd">This segment is locked to represent a year</td>

</tr>

<tr>

<td class="confluenceTd">Segment 11 - Version</td>

<td class="confluenceTd" colspan="1">  
</td>

<td class="confluenceTd">This segment is locked to a version. Versions are used to track changes that may occur to a budget or projection source over time. If configured, filters such as **BOD..V7** could be used to filter the data for changes that occurred from the version that was approved by the Board of Directors to Version 7.</td>

</tr>

<tr>

<td class="confluenceTd">

<span style="color: rgb(0,0,0);">Segment 12 - Source</span>

</td>

<td class="confluenceTd" colspan="1">  
</td>

<td class="confluenceTd">Segment 12 is locked to a source, which represents Actual, Budget, Projection, and other comparable financial sources. As data is imported into INTERJECT, sources can be setup for segmenting data. Segment 12 can also be used to separate out Actuals, which may be posted account balances and other types of entries unposted or considered proforma.</td>

</tr>

<tr>

<td class="confluenceTd">SegmentNumForRowDefs</td>

<td class="confluenceTd" colspan="1">  
</td>

<td class="confluenceTd">

This parameter is used only when the INTERJECT report function using the FinCube DataPortal has Row Definitions in a report. Row Definitions creates separate subtotal sections, such as Labor and Benefits in a spreadsheet report. Each of these sections could be collapsed to show the totals and then expanded to show all the account details. Financial reports normally have 20 to 50 subtotal sections.

If using groupings to define what a subtotal section will include, like **Labor** = **50000..52999** and **Benefits** = **53000..53200** , you can setup the Row Definitions using these groups. However, without the parameter <span>SegmentNumForRowDefs being setup, the FinCube DataPortal will not know which segment our groupings relate to. So if our Accounts are set to Segment1, <span>SegmentNumForRowDefs must be set to 1.</span></span>

<span>In most cases subtotals are based on Accounts, but that is not necessary.</span> If our subtotal sections are going to use groups related to a line of business, and our segment for line of business is Segment3, <span>SegmentNumForRowDefs must be 3.</span>

</td>

</tr>

<tr>

<td class="confluenceTd">ShowCredit</td>

<td class="confluenceTd" colspan="1">  
</td>

<td class="confluenceTd">This parameter can be used with the ReverseSigns parameter to show the required sign for an account segment. It will change the sign (+/-) displayed on accounts. For example, Revenue naturally shows as a credit in the general ledger data since it is a credit account. However, Revenue should show as a positive in a profit and lost report. See the example chart below.</td>

</tr>

<tr>

<td class="confluenceTd">

SkipLive

</td>

<td class="confluenceTd" colspan="1">  
</td>

<td class="confluenceTd">

This is a special INTERJECT feature allowing reports to access live data for the current open month being closed. If set to False, the amounts provided are based on the last scheduled or manually triggered import.

If this is configured in your INTERJECT installation and SkipLive is set to True, the FinCube DataPortal will directly access the current open month balances in real time. This features gives users up-to-the-second data while limiting the server resources needed to present live data during a financial close. It is a significant productivity improvement compared to data warehouses or data-marts that can only provide data updated on a set schedule.

</td>

</tr>

<tr>

<td class="confluenceTd">

ReverseSigns

</td>

<td class="confluenceTd" colspan="1">  
</td>

<td class="confluenceTd"><span><span>This parameter can be used in conjunction with the ShowCredit parameter to show the required sign for an account segment. By setting to True it will reverse the signs of the amounts returned. <span>See the example chart below.</span></span></span></td>

</tr>

<tr>

<td class="confluenceTd">Last Run</td>

<td class="confluenceTd" colspan="1">  
</td>

<td class="confluenceTd">This is an output parameter places in the spreadsheet the report's last run date and time. This will use the timezone settings of the windows session.</td>

</tr>

<tr>

<td class="confluenceTd">TimeLineFrom</td>

<td class="confluenceTd" colspan="1">  
</td>

<td class="confluenceTd">If configured, this will allows users run reports showing changes over time based on imported intervals. Using this feature shows the report as it would have been run the previous week. Alternately, it will show changes occuring in the last 12 hours. If this from date and time parameter is omitted, it defaults to 1/1/1900.</td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">TimeLineTo</td>

<td class="confluenceTd" colspan="1">  
</td>

<td class="confluenceTd" colspan="1">This parameter works with TimeLineFrom. If omitted it is defaulted to through the current week.</td>

</tr>

</tbody>

</table>

</div>

#### Examples using "Show Credits" and "Reverse Signs" Parameters

The **Show Credits** and **Reverse Signs** parameters work together to provide the output required in presenting positive or negative numbers for financial statements. The chart below shows + or - to signify output. The yellow row shows how Assets, Liability, Equity, Revenue, and Expense are naturally recorded in a general ledger. For example, Revenue is always negative by default, but is normally presented as a positive number in a profit and loss report. For certain reconciliations reports, these credit accounts may be specifically set up to show as a negative.

**<span class="confluence-embedded-file-wrapper confluence-embedded-manual-size">![](attachments/127796359/127963443.png?height=250) </span>** 

### Available Columns for the DataPortal

The FinCube DataPortal is unique because of its wide array of column options included in the column definitions of INTERJECT report formulas. There are three types of columns: Segment, Group, and Amounts.

<span class="confluence-anchor-link" id="FinCube-TheFinancialCube-SegCol"></span>

### Segment Columns

Segment columns relate to Segments 1 through 8 and any other groupings setup for the segments. In the configuration of INTERJECT segments, assigned names can be used as columns. For example, Acct (short for account) may be assigned to Segment 1 and Dist (short for district) can be assigned to Segment 2\. In this case both Acct and Dist can be used in columns to show the level of detail required. If only Acct is included in the column, the amounts will be summarized by Acct. If both Acct and Dist are included as columns, then both are shown, and the amounts are summarized by Acct and Dist. This will work for a combination of the first 8 segments.

In addition, the name of the segment may also be noted by adding **Name** as a suffix. For example, AcctName will show the account name.

<span class="confluence-anchor-link" id="FinCube-TheFinancialCube-GroupCol"></span>

### Group Columns

When Groups are set up for a segment, like Acct, they can also be used as columns. It is important to understand what a Segment Group is and which ones can be used. Groups are simply a text phrase assigned to a filter, the same filters explained above. A simple Group for Acct may be **Product Sales** (defined as accounts **32000...34000** ) and **Consulting Sales** (defined as accounts **34001...35000** ). Groups can also contain other Groups. For example, a Group called **Revenue** could contain different Group, like **Product Sales** and **Consulting Sales** .

When Group names are used as columns, the column will summarize the amounts by the Groups it contains. So, in the above example, if **Revenue** is used as column, then groups **Product Sales** and **Consulting Sales** would each show on a row, and the amounts would be summarized at that level.

In a coming release, there are two new features coming to Groups. A sort order will be assigned to a group so users can control the order. In the above example, **Product Sales** will be listed before **Consulting Sales** , since they would normally show in alphabetical order. A future release will also support a group name to add more descriptive names to groups. Currently, Groups are a single text string and may not be text desired in a report. In the above example, you could set up **Sales_Prod** and **Sales_Cons** as the Groups, and then make **Product Sales** and **Consulting Sales** the Group names. In using the parent group **Revenue** as the column, if you added **Name** to the end of the Group, like **RevenueName** , you would get the more descriptive names **Product Sales** and **Consulting Sales** in the report,

instead of **Sales_Prod** and **Sales_Cons** .

<span class="confluence-anchor-link" id="FinCube-TheFinancialCube-AmountCol"></span>

### Amount Columns

There are three methods to specify amount columns in the column definition of a report formula. These include CYA, ACT, and jColumnDef.

<span class="confluence-anchor-link" id="FinCube-TheFinancialCube-CYACol"></span>

### CYA Column Notation

This notation is deprecated but is still supported. Since these notations are relative to a year, it is important to specify the year in the above noted parameter <span>**Segment 10 - Year** . By noting a year, CYA defines what the current year is. CY is for current year, LY is for last year, and so on.</span>

<div class="table-wrap">

<table class="relative-table wrapped confluenceTable" style="width: 99.9206%;"><colgroup><col style="width: 41.184%;"> <col style="width: 58.816%;"></colgroup> 

<tbody>

<tr>

<th class="confluenceTh" colspan="2">CYA Notation</th>

</tr>

<tr>

<td class="confluenceTd">CYA1 through CYA12</td>

<td class="confluenceTd">

Current year actuals for a specific month. The number in the suffix specifies the month.

</td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">CYAYTD1 through CYAYTD12</td>

<td class="confluenceTd" colspan="1"><span>Current year actuals for year to date. The number in the suffix specifies the month.</span></td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">CYA_TOT</td>

<td class="confluenceTd" colspan="1">This is another to total a year. It is same as using CYAYTD12, which returns a total from January to December.</td>

</tr>

<tr>

<td class="confluenceTd" colspan="2">

Other prefixes can be used in place of CYA:

LYA = Last year actual

L2A = 2 years ago actual

L3A = 3 years ago actual

L4A = 4 years ago actual

NYB = Next year budget

CYB = Current year budget

LYB = Last year budget

</td>

</tr>

<tr>

<td class="confluenceTd" colspan="2">

#### Options for Forecast

This notation is more complex, because forecasts may need to retain not only the month forecast but also store when the forecast was completed. For example, you might forecast March twice in a year, first in January and again in February, then compare how that forecast changed over time.

Forecast notation can be set up to handle these changes over time. For example, above, CYFJan3 would represent the first time March was forecast. **CYF** means current year forecast, **Jan** signifies the projection was made in January, and the **3** notes the month from when the projection was completed, such as in a rolling forecast.

Forecasting March again in February, the notation would be CYFFeb2\. Forecasting March again during the month of March, the notation would be CYFMar1.

The examples below may help clarify.

</td>

</tr>

<tr>

<td class="confluenceTd">CYFJan1</td>

<td class="confluenceTd">

Forecast for January: Current year forecast completed in January for the first month of the projection period (January)

</td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">CYFJan2</td>

<td class="confluenceTd" colspan="1">Forecast for February: Current year forecast completed in January for the second month in the projection period (February.)</td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">LYFSep3</td>

<td class="confluenceTd" colspan="1">Forecast for November: Last year forecast completed in September for the 3rd month of the period (November).</td>

</tr>

<tr>

<td class="confluenceTd" colspan="2">

*Special Suffixes for Unposted Amounts: If configured, you may be able to use the _Unposted or _WithUnposted suffix to notations like CYA5 to see the amounts in our journal entries that are not yet posted.*

</td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">CYA3_Unposted</td>

<td class="confluenceTd" colspan="1">Shows only totals for unposted amounts in March of the current year.</td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">CYA_WithUnposted</td>

<td class="confluenceTd" colspan="1">Shows the total of posted and unposted amounts for March of the current year.</td>

</tr>

<tr>

<td class="confluenceTd" colspan="2"><span>*Special consideration for Staged journal entry Amounts: If configured, you may be able to show staged journal amounts not yet uploaded to the ERP. Examples below.*</span></td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">CYA3_Staged</td>

<td class="confluenceTd" colspan="1">Shows only the totals for the staged amounts for March of the current year.</td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">CYA3_WithUnpostedAndStaged</td>

<td class="confluenceTd" colspan="1">Shows the total of posted, unposted and staged amounts for March of the current year.</td>

</tr>

</tbody>

</table>

</div>

<span class="confluence-anchor-link" id="FinCube-TheFinancialCube-ACTCol"></span>

### ACT Column Notation

This notation is one step beyond CYA, since it can also be relative to a month and not just a year. ACT can make it easier to build and maintain monthly review reports because the columns specified are all relative to the month and year filter.

Since these notations are relative to a year and a period, it is important to specify the year and period in the parameters **Segment 9--Period** and **Segment 10--Year** and link them to a cell in the spreadsheet report. For the table below you can consider Mar 2017 the specified period.

<div class="table-wrap">

<table class="relative-table wrapped confluenceTable" style="width: 99.9206%;"><colgroup><col style="width: 33.7921%;"> <col style="width: 66.2079%;"></colgroup> 

<tbody>

<tr>

<th class="confluenceTh" colspan="2">ACT Notation (assuming Mar 2017 is the specified period)</th>

</tr>

<tr>

<td class="confluenceTd">Act</td>

<td class="confluenceTd">

The current-month actual for Mar 2017.

</td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">Bud</td>

<td class="confluenceTd" colspan="1">

The current-month budget for Mar 2017.

</td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">Proj3</td>

<td class="confluenceTd" colspan="1">The suffix for projection can be difficult to understand. Proj3 notes the projection for Mar 2017, when Mar was the third month of the projection period. This means the projection for Mar that was done in January.</td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">Proj2</td>

<td class="confluenceTd" colspan="1">The projection for Mar 2017 done in Feb 2017.</td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">Proj1</td>

<td class="confluenceTd" colspan="1">The projection for Mar 2017 done mid-month, Mar 2017.</td>

</tr>

<tr>

<td class="confluenceTd" colspan="2">*Projections may have several versions (sometimes called editions). Projections for Mar 2017 in the second week of Mar are the initial projection. Additional projection revisions may be in the 3rd and 4th week of Mar before the month closes. The notation below adds a suffix of Edition, which can be used in the report to specify a particular week's changes.*</td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">Proj1Edition1</td>

<td class="confluenceTd" colspan="1">Same as Proj1, the initial projection.</td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">Proj1Edition2</td>

<td class="confluenceTd" colspan="1">Shows the changes made in the 3rd week projections.</td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">Proj1Edition3</td>

<td class="confluenceTd" colspan="1">Shows the changes made in the 4th week projections.</td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">Proj1All</td>

<td class="confluenceTd" colspan="1">The summation of Proj1Edition1, Proj1Edition2 and Proj1Edition3.</td>

</tr>

<tr>

<td class="confluenceTd" colspan="2"><span>*Special Suffixes for Unposted Amounts: If configured, you may be able to use the _Unposted or _WithUnposted suffix to notations like ACT to see the unposted amounts in our journal entries.*</span></td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">Act_Unposted</td>

<td class="confluenceTd" colspan="1">Shows only the totals for the unposted amounts.</td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">Act_WithUnposted</td>

<td class="confluenceTd" colspan="1">Shows the total of posted and unposted amounts.</td>

</tr>

<tr>

<td class="confluenceTd" colspan="2"><span>*Special consideration for Staged journal entry Amounts: If configured, you may be able to show staged journal amounts that are not uploaded to the ERP yet. Below are examples.*</span></td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">Act_Staged</td>

<td class="confluenceTd" colspan="1">Shows only the totals for the staged amounts.</td>

</tr>

<tr>

<td class="confluenceTd" colspan="1">Act_WithUnpostedAndStaged</td>

<td class="confluenceTd" colspan="1">Shows the total of posted, unposted, and staged amounts.</td>

</tr>

</tbody>

</table>

</div>

<span class="confluence-anchor-link" id="FinCube-TheFinancialCube-JColDef"></span>

### jColumnDef() Column Notation

The [jColumnDef()](127965411.html) notation is the most recent addition to the column options and is the most flexible and intuitive in use. Instead of using a single text string to represent an amount, like CYA1 or Act, you can use the jColumnDef() function containing arguments for each of the 12 segments noted in the above DataPortal parameters. In this way, you can specify each component separately and more clearly. jColumnDef() arguments are essentially an additional filter level for each column you want to show.

It is important to emphasize that jColumnDef() goes beyond a source (Actual, Budget, fcast1 to fcast12), a year, and a period alone. These are the same segments (9, 10 and 12) that earlier notations (CTA and ACT) can only specify. jColumnDef also supports the remaining 12 segments and each can support the same filter options and groups noted above for DataPortal parameters explained in the [FinCube](FinCube---The-Financial-Cube_127796359.html) DataPortal page. The result is a highly flexible method to create columns.

The illustration below shows an example. In cells H2 and I2, the jColumnDef() function is entered into the column definition row instead of CYA1 or Act. The jColumnDef() function argument references the cells below it (rows 4 through 15) that notes all the segment options. In this example, the columns will return the Jan and Feb of 2017 actuals, since Period, Year and Source are the only segments used.

<span class="confluence-embedded-file-wrapper confluence-embedded-manual-size">![](attachments/127796359/127965319.png?height=250)</span> 

In the following example, you are using more of the segments. The columns were changed so both are for Jan 2017, but the first column is now specified to all revenue for district 2050\. the second column is specified to show EBITDA for the same district. Using segment groups provides multiple ways to define a column.

<span class="confluence-embedded-file-wrapper confluence-embedded-manual-size">![](attachments/127796359/127965946.png?height=250)</span> 


