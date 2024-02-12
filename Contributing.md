---
title: Contributing
filename: "Contributing.md"
layout: custom
sitemap: false
keywords: [best practices, standards, editing, changes, format, style, consistency]
headings: ["Overview", "Setting Up A Local Environment", "Commit Messages", "Screenshots", "Screenshot Software Requirements", "When to Include a Screenshot", "Click Action (Arrow)", "Highlighting & Emphasizing", "Multi-Step Actions in a Single Screenshot (Numbered Steps)", "Emphasizing Text or a Point in a Screenshot", "Note on Complex Screenshots", "Note on Popups in Screenshots", "Screenshots of Excel Content", "Tab Navigation in Screenshots", "Screenshots Size", "Spacing Surrounding Screenshots", "Interject Company", "Hiding Credentials", "Uploading and Saving Screenshots to the Documentation Site", "Jekyll Front Matter", "Entries", "Images Entry", "Headings", "Table of Contents", "Grammar/Spelling", "Referencing Buttons and Text", "Lists", "Tables", "Links", "Code Blocks", "Consistency"]
links: ["https://app.clickup.com/8587490/v/dc/86272-35740/86272-32800", "https://github.com/GoInterject/GoInterject.github.io", "https://www.techsmith.com/screen-capture.html"]
image_dir: "Contributing"
images: [{file: "01", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "CloneCopyClick", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "CommandPromptNavigate", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "PullRequestClick", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "PullRequestChooseBranches", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "PullRequestReviewer", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "08", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "09", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "10", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "11", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "12", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "13", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "14", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "15", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "16", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "17", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "18", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "19", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "19", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "InterjectDevelopment", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "EmailBlurred", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "DummyEmailDisplayed", type: "png", site: "", cat: "", sub: "", report: "", ribbon: "", config: ""}]
description: Hello and thank you for wanting to make a contribution to Interject. These are the guidelines that we use to make sure our documentation is the highest quality, and consistent. Included in this document is the documentation cycle from creation to approval.
---
* * *

## Overview

Hello and thank you for wanting to make a contribution to Interject. These are the guidelines that we use to make sure our documentation is the highest quality, and consistent. Included in this document is the documentation cycle from creation to approval.

### Setting Up A Local Environment

For editors of the documentation, it is necessary to set up a local environment where you can edit and preview changes before pushing them to the repository. The following lists the basics steps to do this. For detailed instructions on setting up a local environment for documentation editing, see our [Clickup page](https://app.clickup.com/8587490/v/dc/86272-35740/86272-32800){:target="_blank"}{:rel="noopener noreferrer"}

**Step 1:** Navigate to our [Github Repository](https://github.com/GoInterject/GoInterject.github.io){:target="_blank"}{:rel="noopener noreferrer"}.

![](/images/Contributing/01.png)
<br>

Click the clone button and then the copy to clipboard icon to copy the repository's URL.

![](/images/Contributing/CloneCopyClick.png)
<br>

**Step 2:** Navigate to a local folder where you want to clone the repository.

![](/images/Contributing/CommandPromptNavigate.png)
<br>

Execute the git clone command (be sure to paste the url you copied):

```bash
git clone https://github.com/GoInterject/GoInterject.github.io.git
```

**Step 3:** Make your changes locally to a local git branch.

**Step 4:** Push your changes to the repo using the git push command.

```bash
git push origin local_branch:remote_branch
```

**Step 5:** Make a pull request to merge the remote_branch you pushed the changes to into the develop branch.

Click **Pull requests** in the header and then **New pull request**.

![](/images/Contributing/PullRequestClick.png)
<br>

Ensure you are requesting to merge your branch into the develop branch. Click **Create pull request**.

![](/images/Contributing/PullRequestChooseBranches.png)
<br>

Write a description and then click the Reviewers settings button to choose a reviewer. Finally click **Create pull request**.

![](/images/Contributing/PullRequestReviewer.png)
<br>

### Commit Messages

All commit messages should follow this general layout. This is to ensure consistency in determining what has been changed.

```
action(thingchanged): description of the change
```

|Actions |When to Use | 
|---|---|
|update | This should be used when content currently exists, and you are modifying. I.e. grammatical error fixes, or replacing images|
|add | This action type should be used when you are creating a content page initially. |
|remove | This action type is to be used when you are removing a section or an entire page of documentation. |
|create | This should be used when you are creating a new section to existing documentation. |

The "thingchanged" should be a single word noun that describes as best as possible, the piece of UI that was changed.
The "description of the change" should be an accurate description as to what in more detail was changed.

Example:

```
update(screenshots): replaced old SS's with new ones to match UI changes
```

### Screenshots

Screenshots are used heavily in our documentation. Below are our conventions and our process of including screenshots in the documentation.

#### Screenshot Software Requirements

Screenshots for our website are made consistent by using a screen capture program called [Snagit](https://www.techsmith.com/screen-capture.html){:target="_blank"}{:rel="noopener noreferrer"}.

In order to keep screenshots consistent, make sure they are captured in the most current version.

#### When to Include a Screenshot

Every major step in a documentation page should be represented in a screenshot. Screenshots can contain multiple steps, but every step in the process of a lab or walkthrough should be shown somewhere in a screenshot. The user should be able to look at only the screenshots on a page and know exactly what to do.

The following is a simple walkthrough of the recommended screenshot procedure. It is organized by the type of action/step the user is being instructed to take in a given screenshot. There will also be example use cases for some of the screenshot techniques in each section.

#### Click Action (Arrow)

If the instructions call for a click action, use a **solid, red arrow** pointing to the click location.

**Arrows** should be:
* red,
* 7px in thickness,
* below the item if possible,
* have a middle-centered shadow behind them.

No arrow is needed for "Next", "Finish" or "Ok" actions, or when only a single button is used in a screenshot.

When to use an arrow in a screenshot.

1. For click actions:

![](/images/Contributing/08.png)
<br>

2. To point to tab navigation steps.

![](/images/Contributing/09.png)
<br>

It is important to **place arrows where they are easily seen**, such as *below* the dark green menu of Excel 2016.

#### Highlighting & Emphasizing

When discussing a specific portion of a window, a window inside of the screenshot, or button press actions, use a **red outline/rectangle** that is 2px wide around the area/button to highlight it.

"Next" and "Close" button press actions should also be emphasized by enclosing them in a red rectangle.

Such **outlines/rectangles** should:
* be red,
* be 2px in thickness,
* be surrounding the button,
* have a middle-centered shadow behind them.

Limit these outlines to 3 per screenshot for clarity.

When to use outline/rectangle.

1\. To highlight click action areas on the screen if they are hard to see (you can use both an arrow and an outline):

![](/images/Contributing/10.png)
<br>

2\. To emphasize a portion of a window.

![](/images/Contributing/11.png)
<br>

3\. To emphasize a particular window within a screenshot,

4\. To highlight “Next”, “Close” and “Ok” buttons (do not use an arrow for this).

![](/images/Contributing/12.png)
<br>

5\. To highlight clickable data-entry (capture) fields (use after a click action indicated by an arrow, if a data entry field comes up) (do not use both an arrow and a red border for this).

![](/images/Contributing/13.png)
<br>

6\. To highlight checkboxes.

#### Multi-Step Actions in a Single Screenshot (Numbered Steps)

If multiple steps are contained in one image, **label the steps 1, 2, 3,** etc. in Snagit. This gives readers more direction when steps are complex.

When using arrows and numbers together, always connect the arrow to a number and ensure that the arrow is projecting from the center of the number circle.

**Number-labeled steps** should be:
* red,
* made using the numbering feature of Snagit,
* have a middle-centered shadow behind them,
* large enough to read (use Snagit’s default size),
* connected to any red arrows also used in the step.

For more complex screenshots containing multiple steps, **place steps in an ordered list above the image**, numbered correspondingly and tabbed in once.

![](/images/Contributing/14.png)
<br>

#### Emphasizing Text or a Point in a Screenshot

When emphasizing a point, **underline** the particular point with a **2px red line**. Do not use this to highlight buttons within screenshots (instead use the red outline described above).

![](/images/Contributing/15.png)
<br>

#### Note on Complex Screenshots

For complex screenshots, include more thorough text narration in the documentation.

If a procedure is extremely involved, use a GIF.

If a screenshot has multiple images, be sure to use an ordered list of steps within it.

#### Note on Popups in Screenshots

When screen capturing windows that contain popups, make sure the popup appears distinct from the page containing it. To do this, allow the popup to slightly overlap other content in the image. Do not line it up with any other lines on the page. Unless a screenshot of just the pop up is needed (for a special circumstance), make sure to take screenshots of popups with the windows in which they appear; it is important to show all images with as much context as possible.

![](/images/Contributing/16.png)
<br>

#### Screenshots of Excel Content

For screenshots of Excel content:

* Include the Row and Column definitions in the spreadsheet to provide context, when appropriate.
* Include the Interject menu ribbon when it is being used. If the step depicted in the screenshot does not use the Interject menu ribbon, do not include it in the screenshot (to save space).
* Make sure that **no personal or confidential data is visible on the screen** when taking screenshots. Use mary@mycompany.com or joe@mycompany.com for masking report library and email data or remove all personal information using snagit to cover it. For login examples, use "dummy" login credentials. Use the dummy names consistently. If mary@mycompany.com is used once on a page, use it throughout that page.
* With the exception of login boxes, **highlight all boxes from clicks to data entry** (use 2px red border). 
* Remove the cursor from the page when the screen is being captured, unless the cursor is needed.
* If an image is to appear truncated, manually **add a "ripped" black border**.

Here is an example using a dummy credential.

![](/images/Contributing/17.png)
<br>

Here is an example using a ripped border (see left hand side).

![](/images/Contributing/18.png)
<br>

#### Tab Navigation in Screenshots

When directing tab navigation (and sheet navigation in Excel), point to it with an arrow. This is especially helpful for larger screenshots.

![](/images/Contributing/19.png)
<br>

#### Screenshots Size

Ensure the screenshots are big enough to be displayed properly. In most cases, the original screen capture size will suffice. However, be sure to check if the image is displayed properly and easily read.

#### Spacing Surrounding Screenshots

When including a screenshot in the markdown file, be sure to contain a space before the image and follow the image with a &lt;br&gt; and another space.

```
...content...

![](/images/Contributing/19.png)
<br>

...content...
```

#### Interject Company

Whenever possible, the company that should be displayed in the screenshot should be the "Interject Development" company. The times where this should not be the case is where a specific company should be used in order to correctly proceed with the walkthrough or the example.

![](/images/Contributing/InterjectDevelopment.png)
<br>

#### Hiding Credentials

All employee emails and passwords should be hidden from the screenshot. This can be accomplished by blanking it out or using the Snagit blur tool:

![](/images/Contributing/EmailBlurred.png)
<br>

A dummy email or password may be displayed instead:

![](/images/Contributing/DummyEmailDisplayed.png)
<br>

#### Uploading and Saving Screenshots to the Documentation Site

Generally, upload your screenshot images to be the exact size as the original you had taken. Smaller images, such as in-window popups, should be 360px wide, unless an otherwise more appropriate size is needed.

Name your screenshots appropriately to describe the content of the image. For example, PullDataClick or SaveDataClick. PNG images are preferred but JPG works as well.

When saving screenshots, place them in the following directory:

/images/[DirectoryToYourPageFolder]

If a folder for your page does not exist, please add one and place all images in that folder. Every page should have its own image folder. Do not combine pages. 

### Jekyll Front Matter

The Jekyll front matter is a list of meta data at the top of the md file. It is important that this front matter is accurate, complete, and formatted correctly.

#### Entries

The following are the entries and their descriptions for the front matter:

``` markdown
---
title: Name of Page
filename: The filename
layout: custom (only use custom)
keywords: Keywords that describe the page content
headings: The headings in the page
links: The links referenced in the page (both internal and external)
image_dir: The name of the image directory for this page
images: A nested list of images with their description (see next section below)
description: A short description (typically the first paragraph in the overview)
---
* * *
```

#### Images Entry

The images entry for the front matter contain a nested json list of images with keys that describe the content of the image:

- file: Name of the image file (without the extension)
- type: The type of file (e.g. png or jpg or gif)
- site: The site origin of the image (e.g. Addin, Portal, Windows)
- cat: The main category of the image (e.g. pull data, save data, report library)
- sub: The subcatetory of the image (e.g. more details of the category of the image)
- report: If a report title, Excel tab, or file is displayed or referenced list the name here
- ribbon: If simple or advanced ribbon is shown in the image
- config: If the Interject configuration area is shown in the image

Blank entries are an empty string ("").

Here is an example of a images entry:

```
images: [{file: "NewDataPortal", type: "png", site: "Portal", cat: "Data Portals", sub: "", report: "", ribbon: "", config: ""}, {file: "DataPortalDetails", type: "png", site: "Portal", cat: "Data Portals", sub: "Details", report: "", ribbon: "", config: ""}, {file: "AddSystemParameter", type: "png", site: "Portal", cat: "Data Portals", sub: "Details", report: "", ribbon: "", config: ""}, {file: "ChangeReportSaveFunction", type: "png", site: "Addin", cat: "Report", sub: "", report: "Customer Aging Summary", ribbon: "", config: ""}, {file: "SPCurrentDate", type: "png", site: "SSMS", cat: "Code", sub: "", report: "", ribbon: "", config: ""}]
```

For more specific examples of what to put in the cat and sub entries, see existing pages.

### Headings

Most pages should have the "Overview" heading as a h2 (##). Subsequent headings should be marked as h3 (###) or h4 (####).

Headings should be Title Case (following APA standards).

Headings should not be in bold as they are formatted already with their heading formatting.

Include one line space before and after all headings.

### Table of Contents

TOC entries should always have a default link. For example, if the parent category group does not have a landing page, it should link to the first sub category page.

### Grammar/Spelling

Ensure all extra lines are removed.

Ensure all extra spaces are removed.

Ensure spelling is correct.

Ensure consistency is maintained for the spelling and capitalization of certain words (e.g. Data Portal, Walkthrough).

### Referencing Buttons and Text

Whenever a button or menu item is referenced, mark the item as bold (\*\*). Whenever instruction to enter text is given, the text in question should be bold.

Whenever quotation marks are to be entered in the instructions, they should be escaped. For example:

```
Select cell E4 and enter **=ReportRange(\"NorthwindCustomers\")**
```

### Lists

Lists should be explicitly numbered to ensure it displays correctly across multiple platforms. For example:

```
1. Item 1
2. Item 2
3. Item 3
```

Not:

```
1. Item 1
1. Item 2
1. Item 3
```

### Tables

Tables should follow Jekyll/Markdown format for consistency wherever possible:

```
| Item | Description |
|-----|-----|
| Item1 | This is the description to Item1 |
| Item2 | This is the description to Item2 |
| Item3 | This is the description to Item3 |
```

Tables do not need to have extra spaces as Jekyll will format the table and delete extra spaces. Only use extra spaces where it is necessary to visualize the table in the markdown file.

When not possible, standard html table format should reflect the same standard table appearance for consistency.

### Links

Ensure all links work. Links to external websites should be followed by:

```
{:target="_blank"}{:rel="noopener noreferrer"}
```

### Code Blocks

Code blocks are preceded by \`\`\` to mark them as code. Generally, code should be be separated from the main content of the page.

### Consistency

Wherever possible, maintain the same formatting standards and usage as used in other pages. You can inspect other pages for examples.

