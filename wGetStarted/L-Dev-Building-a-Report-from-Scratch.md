Start with a blank Excel workbook:

![](/images/L-Dev-Report_from_Scratch/01.png)

### Setting the Freeze Panes

We will start off by setting the Freeze Panes at the correct location using jFreezePanes() [detailed here](https://docs.gointerject.com/wIndex/jFreezePanes.html#function-summary)

**Step 1:** To start, type “=jFreezePanes” in cell **F10**:

![](/images/L-Dev-Report_from_Scratch/02.png)
Click on the function builder(?):

![](/images/L-Dev-Report_from_Scratch/03.png)
**Step 2:** There are two parameters of jFreezePanes(), FreezePanesCell and AnchorViewCell. AnchorViewCell specifies the very top row that will be visible when the panes are frozen. The cells above AnchorViewCell will be hidden when the panes are frozen. The cells between AnchorViewCell and FreezePanesCell is the block that is frozen at the top of the sheet as you scroll down the sheet.

Set **FreezePanesCell = A26**  and **AnchorViewCell = A18**:

![](/images/L-Dev-Report_from_Scratch/04.png)
Now that we have our freeze pane set up, we can start with formatting the spreadsheet.

INTERJECT uses the hidden area of the frozen pane to define INTERJECT report functions and to set up the formatting of the report.

### Formatting the Behind the Scenes Section

We’ll start by setting up the titles of the sections that hold the different report functionality formulas. This formatting is standard to INTERJECT reports.

**Step 1:** Start by selecting row 1 and coloring it dark blue (#1F4E78). This is the color that INTERJECT uses for titles of report definition sections.

	1. First, click on the “1” that denotes row 1 to highlight the entire row.
	2. Click the paint bucket to fill the color.
	3. Choose the darkest blue (#1F4E78).

![](/images/L-Dev-Report_from_Scratch/05.png)
For this report, we will need 5 different titled sections. Now that you have the color selected in your paint bucket, simply click on every other row and then click on the paint bucket until you have 5 dark blue rows:

![]/images/L-Dev-Report_from_Scratch/06.png

Now let’s name the title sections. We will need names: “Column Definitions,” “Formatting Range,” “Report Formulas,” “Hidden Parameters and Notes,” and “Report Area Below.”  We will enter “Column Definitions” and make it **white** and **bold** as follows:

![](/images/L-Dev-Report_from_Scratch/07.png)
Now enter the names “Formatting Range,” “Report Formulas,” “Hidden Parameters and Notes,” and “Report Area Below” in the next 4 title rows. Don’t worry about the formatting of these 4 for now.

![](/images/L-Dev-Report_from_Scratch/08.png)
Now, we can use the format painter to copy the formatting of the first title to the remaining 4:

![](/images/L-Dev-Report_from_Scratch/09.png)
As you may have noticed, the jFreezePanes() is out of place. And our hidden freeze panes sections goes all the way down to row 17, so the space where our titles are laid out should occupy all of this space. Let’s insert some more empty rows under our titles to put more space for formula definitions and the like.

Copy two empty rows from somewhere in the sheet:

![](/images/L-Dev-Report_from_Scratch/10.png)
Paste them above row 2 by right clicking on row 2:

![](/images/L-Dev-Report_from_Scratch/11.png)
Now copy and paste 2 more rows under each title so that your report looks like this:

![](/images/L-Dev-Report_from_Scratch/12.png)
We can now see that the size of our report definitions area matches the size we set for jFreezePanes(), ending at row 17. Let’s move our jFreezePanes() definition back to cell F10. Cut and paste cell F18 to cell F10:

![](/images/L-Dev-Report_from_Scratch/13.png)
Now let’s add the standard light blue color to the titled sections:

	1. Select the 3 rows under Column Definitions.
	2. Click the paint bucket.
	3. Select the lightest blue color (#DDEBF7).

![](/images/L-Dev-Report_from_Scratch/14.png)
Repeat this step for the three other report definition areas so that your report looks as follows:

![](/images/L-Dev-Report_from_Scratch/15.png)
Now let’s format the report area. We’ll start by putting a report title in cell **B19** “Customer Orders:”

![](/images/L-Dev-Report_from_Scratch/16.png)
Next, let’s name the report filters for this report. The report filters act as a way to specify which data is being pulled into the report from the data portal by specifying a set of characters that the pulled in data must contain. In cells **B21, B22 and B23**, respectively, type in: **“Company Name:”**, **“Contact Name:”**, and **“Customer ID:”**

![](/images/L-Dev-Report_from_Scratch/17.png)
Now, let’s resize column A to be smaller, and extend column B by a bit:

![](/images/L-Dev-Report_from_Scratch/18.png)
Now let’s color the input fields for the report filters. Apply the lightest orange color () to cells **C21, C22 and C23**:

![](/images/L-Dev-Report_from_Scratch/19.png)
Let’s expand column C a little bit to give the user more space for their input:

![](/images/L-Dev-Report_from_Scratch/20.png)
Now that we’ve titled and styled our report filters, let’s make the spreadsheet look better by removing the gridlines in Excel.

Go to the **Files** tab in Excel:

![](/images/L-Dev-Report_from_Scratch/21.png)
Go to **Options**:

![](/images/L-Dev-Report_from_Scratch/22.png)
	1. Go to the **Advanced** tab.
	2. Scroll down until you see **“Display options for this worksheet”**.
	3. **Uncheck** the **“Show gridlines”** checkbox.

![](/images/L-Dev-Report_from_Scratch/23.png)
Name the current worksheet **“CustomerOrderHistory”** and delete any other worksheets you have in the workbook:

![](/images/L-Dev-Report_from_Scratch/24.png)
![](/images/L-Dev-Report_from_Scratch/25.png)
![](/images/L-Dev-Report_from_Scratch/26.png)

### Adding ReportRange() to the Report

**Step 1:** Let’s add our first INTERJECT report formula to the report. We’ll start with **ReportRange()**. ReportRange() is a report formula used to PULL data into a defined *range* of a report from the Data Portal. ReportRange() can be used with formatting to format the data returned from the Data Portal into the spreadsheet. Read more about ReportRange() [here](https://docs.gointerject.com/wIndex/ReportRange.html#function-summary).

Type **“=ReportRange()”** in cell **C10** then click on the function builder icon.

![](/images/L-Dev-Report_from_Scratch/27.png)
As you can see, DataPortal is the first parameter that will must provide ReportRange() so that it knows where to pull in the data from. Type **“NorthwindCustomerOrders_MyName”** into the DataPortal parameter box for now.

![](/images/L-Dev-Report_from_Scratch/28.png)
We will now switch to configuring an INTERJECT Data Connection, and a Data Portal that we can pull from using ReportRange().

### Setting Up the First Data Connection

In order to continue our work from here, we need to set up the back-end Data Portal that ReportRange() will be using. For now, we will pause working on the front-end Excel report to configure the Data Portal and Data Connection that ReportRange() will use in our report.

We’ll start with the Data Connection. INTERJECT Data Connections enable users to connect to a database in order to pull data out of that database based on criteria specified in stored procedures which are set up with Data Portals. An overview of Data Connections and Data Portals can be found [here](https://docs.gointerject.com/wPortal/The-INTERJECT-Website-Portal.html#overview).

**Step 1: Logging in** Start by navigating to the INTERJECT portal site ([here](https://portal.gointerject.com/)) and logging in.

![](/images/L-Dev-Report_from_Scratch/29.png)
**Step 2: Create the connection:** Create a new data connection by clicking the New Connection button.

![](/images/L-Dev-Report_from_Scratch/30.png)
Name you connection **NorthwindDB_MyName** (substitute for your name) and give it a quick description.

![](/images/L-Dev-Report_from_Scratch/31.png)
Select **”Database”** from the dropdown list for **Connection Type**.

![](/images/L-Dev-Report_from_Scratch/32.png)
For the connection string, you will need to have your own sample Northwind database to use. You can download a Northwind sample database from Microsoft [here](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/sql/linq/downloading-sample-databases).

Substitute in your server and database name in italicized parts of the following sample connection string: ”Server=*MyServerAddress*;Database=*MyDatabase*;Trusted_Connection=True;” Once you have your connection string entered, press Save to continue.

![](/images/L-Dev-Report_from_Scratch/33.png)
### Setting Up the First Data Portal

**Step 1: Create the Data Portal** Now, we will create the Data Portal that allows us to actually pull data from the Data Connection that we made above.

Data Portals are provided as a way to connect to specific stored procedures within the Data Connection to an existing database. It is a finer-grain level of control, and connects to a single stored procedure on the database you connect to through the provided Data Connection. You can have multiple Data Portals connected to one Data Connection, but not vice-versa. For more, see [the website portal documentation](https://docs.gointerject.com/wPortal/The-INTERJECT-Website-Portal.html#-data-connections-).

Navigate again to [the portal site](https://portal.gointerject.com/) and choose Data Portals.

![](/images/L-Dev-Report_from_Scratch/34.png)
Create a new data portal.

![](/images/L-Dev-Report_from_Scratch/35.png)
Start by naming your Data Portal **”NorthwindCustomerOrders_YourName”** (substitute in your name) and giving it a description.

![](/images/L-Dev-Report_from_Scratch/36.png)
For the **Connection**, we will use the Data Connection we created in the last section, **”NorthwindDB_YourName”**. It should appear in the dropdown list when clicked

![](/images/L-Dev-Report_from_Scratch/37.png)
Now we will specify the stored procedure that this data portal will be referencing. We will write the stored procedure itself shortly. Name your stored procedure **”[demo].[northwind_customer_orders_myname]”**.

![](/images/L-Dev-Report_from_Scratch/38.png)
For the **Category**, enter **Demo** and for the **Command Type**, choose **Stored Procedure Name** from the dropdown list.

![](/images/L-Dev-Report_from_Scratch/39.png)
Make sure **Data Portal Status** is set to **Enabled** and **Is Custom Command?** is set to **No**, then save the new Data Portal:

![](/images/L-Dev-Report_from_Scratch/40.png)
### Setting up ReportRange() with the Data Portal

Now, we have a Data Connection to a database, and a Data Portal which specifies a stored procedure to provide data to it; but we need to write the stored procedure in order to actually get anything back from our ReportRange() call in the report.

In order to show how the front-end Excel interface ties into the writing of the back-end stored procedure, let’s start by going back to the report and figuring out what data we want to display to the user.

**Step 1:** Go back to the report, click in cell **C10** and open the function builder.

![](/images/L-Dev-Report_from_Scratch/41.png)
Enter **2:4** into the **ColDefRange** to tell ReportRange() that all of its column definitions can be found in this range of rows. You can read more about ColDefRange here.

![](/images/L-Dev-Report_from_Scratch/42.png)
Now, we can specify the columns that we want to get back from our Data Portal via ReportRange in the Column Definitions section of our report.

Starting with row 2, type **CustomerID** into cell **B2**, **CompanyName** into cell **C2**, **ContactName** into cell **E2**, **OrderID** into cell **F2**, **OrderDate** into cell **G2**, **OrderAmount** into cell **H2**, **Freight** into cell **I2**, **TotalAmount** into cell **J2**.

![](/images/L-Dev-Report_from_Scratch/43.png)
In row 3, we just need **ShipVia** in cell **C3** and **ShippedDate** in cell **E3**.

![](/images/L-Dev-Report_from_Scratch/44.png)
Now, let’s add the other parameters. Open the function arguments for ReportRange() again.

![](/images/L-Dev-Report_from_Scratch/45.png)
ReportRange() works by inserting the result set returned from the Data Portal *in between* two or more rows. These rows are specified by the TargetDataRange argument. Input **27:28** for our **TargetDataRange**.

![](/images/L-Dev-Report_from_Scratch/46.png)
The Formatting Range is the part of the report definitions section that specifies how final output will be formatted when returned to the end user. Our formatting range occupies rows 6:8, so input **6:8** in **FormatRange**.

![](/images/L-Dev-Report_from_Scratch/47.png)
The **Parameters** parameter specifies which cells will be the “filter” cells whose values are sent to the Data Portal to filter results to the user’s specifications. The Param() function ([read more here](https://docs.gointerject.com/wIndex/Param.html)) is used here to capture the cells. Type **Param(C21,C22,C23)** into **Parameters**.

![](/images/L-Dev-Report_from_Scratch/48.png)
As a best practice, we recommend you set **UseEntireRow** to **TRUE** and **PutFieldNamesAtTop** to **FALSE**

Now that we know which pieces of data we need in our report, we can design the stored procedure.

Using a SQL editor like [SQL Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/sql-server-management-studio-ssms?view=sql-server-2017), copy and paste in the following code:

code

Here is the SELECT statement in the code. The columns returned from the SELECT statement are the ones that populate into the report.

select code

### Setting up ReportDefaults()

The ReportDefaults() function is used to capture values from one or a set of cells (or an independently specified value) and send the value/s to another cell or set of cells. Its execution is triggered based on another action/event happening in the report (for example a save or clear action. It is commonly used to clear the values in the filter list after results have been pulled in and then cleared, which is how it will be used herein. Read more about ReportDefaults() [here](https://docs.gointerject.com/wIndex/ReportDefaults.html#function-summary).


