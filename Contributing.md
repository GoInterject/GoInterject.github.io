---
title: Contributing
filename: "Contributing.md"
layout: custom
sitemap: false
keywords: [best practices, standards, editing, changes, format, style, consistency]
headings: ["Overview", "Contributing Process Flow", "Screenshot Requirements", "Screenshot Software Requirements", "When to Include a Screenshot", "Click Action (Arrow)", "Highlighting & Emphasizing", "Multi-Step Actions in a Single Screenshot (Numbered Steps)", "Emphasizing Text or a Point in a Screenshot", "Note on Complex Screenshots", "Note on Popups in Screenshots", "Screenshots of Excel Content", "Tab Navigation in Screenshots", "Spacing Surrounding Screenshots", "Note for Content Reviewers", "Uploading and Saving Screenshots to the Documentation Site", "Adding Jekyll Headers to Page", "Headings", "Table of Contents", "Grammar/Spelling", "Referencing Buttons and Text", "Lists", "Tables", "Links", "Code Blocks", "Consistency", "Commit Message Standards"]
links: ["https://www.techsmith.com/screen-capture.html"]
image_dir: "Contributing"
images: [{file: "01", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "02", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "03", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "04", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "05", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "06", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "07", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "Documentation_process", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "08", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "09", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "10", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "11", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "12", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "13", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "14", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "15", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "16", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "17", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "18", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "19", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}, {file: "19", type: "png", site: "Addin", cat: "", sub: "", report: "", ribbon: "", config: ""}]
description: Hello and thank you for wanting to make a contribution to Interject. These are the guidelines that we use to make sure our documentation is the highest quality, and consistent. Included in this document is the documentation cycle from creation to approval.
---
* * *

## Overview

Hello and thank you for wanting to make a contribution to Interject. These are the guidelines that we use to make sure our documentation is the highest quality, and consistent. Included in this document is the documentation cycle from creation to approval.

### Contributing Process Flow

**Step 1:** Navigate to our Github repository at GoInterject/GoInterject.github.io.

![](/images/Contributing/01.png)
<br>

**Step 2:** Fork/Clone the repository.

**For editors:** Fork your own branch of the main master branch repository.

![](/images/Contributing/02.png)
<br>

**For content reviewers**: Clone the patch branch named “patch-x.x” (“x.x” in place of the current version number) on the main repository and host locally and make all your changes there before pushing to the origin (master) repository.

Switch to “patch-x.x” branch.

![](/images/Contributing/03.png)
<br>

![](/images/Contributing/04.png)
<br>

Clone the branch.

![](/images/Contributing/05.png)
<br>

![](/images/Contributing/06.png)
<br>

** Step 3:** Make your changes on your forked branch.

**Step 4:** Make a pull request to a branch that is titled "patch-x.x".

![](/images/Contributing/07.png)
<br>

**Step 5:** The changes will be reviewed in the patch branch.

**Step 6:** Once all changes are reviewed and approved, that patch branch will be merged into the master branch on a deployment schedule.

![](/images/Contributing/Documentation_process.png)
<br>

### Screenshot Requirements

Screenshots are used heavily in our documentation. Below are our conventions and our process of including screenshots in the documentation.

#### Screenshot Software Requirements

Screenshots for our website are made consistent by using a screen capture program called [Snagit](https://www.techsmith.com/screen-capture.html).

In order to keep screenshots consistent, make sure they are captured in the most current software (see above).

#### When to Include a Screenshot

Every step in a documentation page should be represented in a screenshot. Screenshots can contain multiple steps, but every step in the process of a lab or walkthrough should be shown somewhere in a screenshot. The user should be able to look at only the screenshots on a page and know exactly what to do.

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

1. To highlight click action areas on the screen if they are hard to see (you can use both an arrow and an outline):

![](/images/Contributing/10.png)
<br>

2. To emphasize a portion of a window.

![](/images/Contributing/11.png)
<br>

3. To emphasize a particular window within a screenshot,

4. To highlight “Next”, “Close” and “Ok” buttons (do not use an arrow for this).

![](/images/Contributing/12.png)
<br>

5. To highlight clickable data-entry (capture) fields (use after a click action indicated by an arrow, if a data entry field comes up) (do not use both an arrow and a red border for this).

![](/images/Contributing/13.png)
<br>

6. To highlight checkboxes.

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

#### Spacing Surrounding Screenshots

When including a screenshot in the markdown file, be sure to contain a space before the image and follow the image with a &lt;br&gt; and another space.

```
...content...

![](/images/Contributing/19.png)
<br>

...content...
```

### Note for Content Reviewers

When reviewing for publication, check that no assumptions are made regarding steps, major or minor, required in any process.

### Uploading and Saving Screenshots to the Documentation Site

Generally, upload your screenshot images to be the exact size as the original you had taken. Smaller images, such as in-window popups, should be 360px wide, unless an otherwise more appropriate size is needed.

Name your screenshots 01.png, 02.png, 03.png, etc. based on the order of their placement within the page.

When saving screenshots, place them in the following directory:

/images/[DirectoryToYourPageFolder]

If a folder for your page does not exist, please add one and place all images in that folder. This ensures the most simple naming conventions of 01, 02, 03 as the images are displayed on the website. 

### Adding Jekyll Headers to Page

All pages must have Jekyll headers added to the top of the page in order for our search function to show it correctly. The way to denote the Jekyll is by three hyphens "---" at the top and bottom of the header. (Note: The "#" denotes comments below).

``` markdown
---
title: Contributions #Name of Page
layout: custom #Keep as custom
keyword: #Whatever the document is about
description: #A short description
sitemap: True #Lets google know this needs to be indexed 
---
* * * #This inserts a horizontal line after the title
```

### Headings

Most pages should have the "Overview" heading as a h2 (##). Subsequent headings should be marked as h3 (###) or h4 (####).

Headings should be Title Case (following APA standards).

### Table of Contents

TOC entries should always have a default link. For example, if the parent category group does not have a landing page, it should link to the first sub catagory page.

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

Tables need not to have extra spaces as Jekyll will format the table and delete extra spaces. Only use extra spaces where it is necessary to visualize the table in the markdown file.

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

### Commit Message Standards

All commit messages should follow this general layout. This is to ensure consistency in determining what has been changed.

```
action(thingchanged): description of the change
```

|Actions      |When to use                                                                                                                 |
|-----------|--------------------------------------------------------------------------------------------------------------------------|
|update       | This should be used when content currently exists, and you are modifying. I.e. grammatical error fixes, or replacing images|
|add          | This action type should be used when you are creating a content page initially.                                            |
|remove       | This action type is to be used when you are removing a section or an entire page of documentation.                         |
|create       | This should be used when you are creating a new section to existing documentation.                                         |

The "thingchanged" should be a single word noun that describes as best as possible, the piece of UI that was changed.
The "description of the change" should be an accurate description as to what in more detail was changed.

Example:
```
update(screenshots): replaced old SS's with new ones to match UI changes
```
