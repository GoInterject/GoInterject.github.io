---
title: Reviewing Report Formulas
filename: "Report-Formula-Reviews.md"
layout: custom
keywords: [cell formula review, report formulas, function wizard]
headings: ["Overview", "Getting Started", "The Function Wizard", "Cell Formula Review"]
links: ["/wAbout/Customer-Aging.html", "https://support.microsoft.com/en-au/office/using-functions-and-nested-functions-in-excel-formulas-3f4cf298-ded7-4f91-bc80-607533b65f02", "/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#advanced-menu-items"]
image_dir: "FormulasReviews"
images: [{file: "InterjectCustomerCollections",type: "png",site: "Addin",cat: "Report Library",sub: "",report: "Interject Customer Collections",ribbon: "",config: ""},{file: "Unfreeze",type: "png",site: "Addin",cat: "Quick Tools",sub: "",report: "",ribbon: "Advanced",config: ""},{file: "SelectFX",type: "png",site: "Addin",cat: "Report",sub: "",report: "",ribbon: "",config: "Yes"},{file: "FunctionWizard",type: "png",site: "Excel",cat: "Function Wizard",sub: "",report: "",ribbon: "",config: ""},{file: "SelectCellFormulaReview",type: "png",site: "Addin",cat: "Ribbon",sub: "Validation Report",report: "",ribbon: "",config: ""},{file: "FormulaReviewWindow",type: "png",site: "Addin",cat: "Formula Review",sub: "",report: "",ribbon: "",config: ""},{file: "FormulaReviewOptions",type: "png",site: "Addin",cat: "Formula Review",sub: "",report: "",ribbon: "",config: ""},{file: "ShowReferences",type: "png",site: "Addin",cat: "Formula Review",sub: "",report: "",ribbon: "",config: ""},{file: "ShowParamNames",type: "png",site: "Addin",cat: "Formula Review",sub: "",report: "",ribbon: "",config: ""},{file: "IndentDataCellFunctions",type: "png",site: "Addin",cat: "Formula Review",sub: "",report: "",ribbon: "",config: ""},{file: "IndentAllOthers",type: "png",site: "Addin",cat: "Formula Review",sub: "",report: "",ribbon: "",config: ""}]
description: Reviewing the Interject report formulas for accuracy is a vital step in eliminating report errors. This page shows two tools that help with these formulas&#58; Excel's Function Wizard and Interject's Cell Formula Review.
---
* * *

## Overview

Reviewing the Interject report formulas for accuracy is a vital step in eliminating report errors. Sometimes when setting up a report formula, it can be difficult to enter everything correctly as there can be nested formulas each with their own set of parameters. Many times there are a number of parentheses, commas, and quotation marks that must be entered correctly. This page shows two tools that help with these formulas: Excel's Function Wizard and Interject's Cell Formula Review.

### Getting Started

This page will use the the Customer Collections report [previously](/wAbout/Customer-Aging.html) used in the Real World Walkthrough.

![](/images/FormulasReviews/InterjectCustomerCollections.png)
<br>

In order to access the report formulas, you need to first unfreeze the panes. From the Quick Tools, select **PANES: Freeze/UnFreeze Panes** and click **Run and Close**.

![](/images/FormulasReviews/Unfreeze.png)
<br>

### The Function Wizard

Excel's Function Wizard makes it easy to enter formulas inside the report and enter or modify parameters. First select the formula you want to edit and press the **fx** button to bring up the Function Wizard.

![](/images/FormulasReviews/SelectFX.png)
<br>

The Function Wizard window displays the currently selected formula and all its parameters. It also conveniently displays descriptions for the formula and all the parameters. In addition, the result of the formula is displayed (if there are errors in the formula, it will show the error).

![](/images/FormulasReviews/FunctionWizard.png)
<br>

For more about Excel's Function Wizard and entering formulas, see [Microsoft's documentation](https://support.microsoft.com/en-au/office/using-functions-and-nested-functions-in-excel-formulas-3f4cf298-ded7-4f91-bc80-607533b65f02){:target="_blank"}{:rel="noopener noreferrer"}.

### Cell Formula Review

The Function Wizard is good for entering and modifying formulas but it does not show detailed information concerning the Interject parameters. For this you can use Interject's Cell Formula Review. (This is found on the Interject [advanced](/wGetStarted/INTERJECT-Ribbon-Menu-Items.html#advanced-menu-items) menu).

First select the cell containing the formula you want to review. Then click **Validation Report** and then select **Cell Formula Review**.

![](/images/FormulasReviews/SelectCellFormulaReview.png)
<br>

This **Formula Review** window appears showing a convenient display of the formula and its parameters and values.

![](/images/FormulasReviews/FormulaReviewWindow.png)
<br>

This window has four different options to further customize the display:

* Show Formula References
* Show Param Names
* Indent Data Cell Functions
* Indent All Others

![](/images/FormulasReviews/FormulaReviewOptions.png)
<br>

The **Show Formula References** will display the references used in the parameters.

![](/images/FormulasReviews/ShowReferences.png)
<br>

**Show Param Names** displays the names of the parameters.

![](/images/FormulasReviews/ShowParamNames.png)
<br>

The **Indent Data Cell Functions** will include indentation before each entry.

![](/images/FormulasReviews/IndentDataCellFunctions.png)
<br>

Finally, the **Indent All Others** will provide newlines for each entry.

![](/images/FormulasReviews/IndentAllOthers.png)
<br>
