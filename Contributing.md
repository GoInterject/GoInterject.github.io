---
title: Contributing
layout: custom
sitemap: false
---

### Overview

Hello and thank you for wanting to make a contribution to INTERJECT. These are the guidelines that we use to make sure our documentation is the highest quality, and consistent. Included in this document is the documentation cycle from creation to approval.

### Contributing Process Flow

Step 1: Fork your own branch of the main master branch repo unless you are a content reviewer, in which case, use a clone of the patch branch on the main repository and host locally and make all your changes there before pushing to the origin repository.

Step 2: Make your changes on your forked branch

Step 3: Make a pull request to a branch that is titled "patch-x.x"

Step 4: The changes will be reviewed in the patch branch

Step 5: Once all changes are reviewed and approved, that patch branch will be merged into the master branch on a deployment schedule.

![](/images/Documentation process.png)

### Screenshot Requirements

#### When to Include a Screenshot

Every step in a documentation page should be represented in a screenshot. Screenshots can contain multiple steps, but every step in the process of a lab or walkthrough should be shown somewhere in a screenshot. The user should be able to look at only the screenshots on a page and know exactly what to do.

Below, we will go through the screenshot creation conventions used for each type of action/step a user must take.

#### Screenshot Software Requirements

Screenshots for our website are made consistent by using a screen capture program called [Snagit](https://www.techsmith.com/screen-capture.html).

In order to keep screenshots consistent, make sure they are captured in the most current software (see above).

#### Click Action (Arrow)

If the instructions call for a click action, use a **solid, red arrow** pointing to the click location.

**Arrows** should be:
* red,
* 7px in thickness,
* below the item if possible,
* have a middle-centered shadow behind them.

No arrow is needed for "Next" or "Finish" actions, or when only a single button is used in a screenshot.

Arrows are not typically needed for buttons that are easy to see and emphasized on the screen. For these, go to “Highlighting Buttons...” For not very well defined buttons, add an arrow indicating to the user where to click.

Use an arrow in a screenshot:
* for click actions that are not buttons,
* to point to inconspicuous or not well-defined buttons,
* to point to tab navigation steps.

It is important to **place arrows where they are easily seen**, such as *below* the dark green menu of Excel 2016. 

#### Highlighting Buttons, Emphasizing a Portion of a Window, and Next and Close Button Press Steps (Outlining with a Rectangle)

When discussing a specific portion of a window, a window inside of the screenshot, or button press actions, use a **red outline/rectangle** that is 2px wide around the area/button to highlight it.

"Next" and "Close" button press actions should also be emphasized by enclosing them in a red rectangle.

Such **outlines/rectangles** should:
* be red,
* be 2px in thickness,
* be surrounding the button,
* have a middle-centered shadow behind them.

Limit these outlines to 3 per screenshot for clarity.

Use a red outline/rectangle to
* highlight buttons for button-press actions (use an arrow additionally, if the button is hard to see or not well-defined) (?),
* emphasize a portion of a window,
* emphasize a particular window within a screenshot,
* highlight “Next” and “Close” buttons (do not use an arrow for this),
* highlight clickable data-entry (capture) fields (use after a click action indicated by an arrow, if a data entry field comes up) (do not use both an arrow and a red border for this), (ADD SCREENSHOT)
* highlight checkboxes.

#### Multi-Step Actions in a Single Screenshot (Numbered Steps)

If multiple steps are contained in one image, **label the steps 1, 2, 3,** etc. in Snagit. This gives readers more direction when steps are complex.

When using arrows and numbers together, always connect the arrow to a number and ensure that the arrow is projecting from the center of the number circle.

**Number-labeled steps** should be:
* red,
* made using the numbering feature of Snagit,
* have a middle-centered shadow behind them, (?)
* large enough to read, (use Snagit’s default size)
* connected to any red arrows also used in the step.

For images containing multiple steps, **place steps in an ordered list below the image**, numbered correspondingly and tabbed in once. (Add screenshot)

#### Emphasizing Text or a Point in a Screenshot

When emphasizing a point, **underline** the particular point with a **2px red line**. Do not use this to highlight buttons within screenshots (instead use the red outline described above).

#### Note on Complex Screenshots

For complex screenshots, include more thorough text narration in the documentation..

If a procedure is extremely involved, use a GIF.

If a screenshot has multiple images, be sure to use an ordered list of steps within it.

#### Note on Popups in Screenshots

When screen capturing windows that contain popups, make sure the popup appears distinct from the page containing it. To do this, allow the popup to slightly overlap other content in the image. Do not line it up with any other lines on the page. Unless a screenshot of just the pop up is needed (for a special circumstance), make sure to take screenshots of popups with the windows in which they appear; it is important to show all images with as much context as possible. 

#### Screenshots of Excel Content

For screenshots of Excel content:

Include the Row and Column definitions in the spreadsheet to provide context, when appropriate.
Include the INTERJECT menu ribbon when it is being used. If the step depicted in the screenshot does not use the INTERJECT menu ribbon, do not include it in the screenshot (to save space).
Make sure that **no personal or confidential data is visible on the screen** when taking screenshots. Use mary@mycompany.com or joe@mycompany.com for masking report library and email data or remove all personal information using snagit to cover it. For login examples, use "dummy" login credentials. Use the dummy names consistently. If mary@mycompany.com is used once on a page, use it throughout that page.
With the exception of login boxes, **highlight all boxes from clicks to data entry** (use 2px red border). 
Remove the cursor from the page when the screen is being captured, unless the cursor is needed.
If an image is to appear truncated, manually **add a "ripped" black border**.

#### Tab Navigation in Screenshots

When directing tab navigation (and sheet navigation in Excel), point to it with an arrow. This is especially helpful for larger screenshots.

### Note for Content Reviewers

When reviewing for publication, check that no assumptions are made regarding steps–major or minor–required in any process.

### Uploading and Saving Screenshots to the Documentation Site

Generally, upload your screenshot images to be the exact size as the original you had taken. Smaller images, such as in-window popups, should be 360px wide, unless an otherwise more appropriate size is needed.

Name your screenshots 01.png, 02.png, 03.png, etc. based on the order of their placement within the page.

When saving screenshots, place them in the

/images/[DirectoryToYourPageFolder]

folder of the website. If a folder for your page does not exist, please add one and place all images in that folder. This ensures the most simple naming conventions of 01, 02, 03 as the images are displayed on the website. 


### Adding Jekyll Headers to Page

All pages must have Jekyll headers added to the top of the page in order for our search function to show it correctly. The way to denote the jekyll is by three hyphens "---" at the top and bottom of the text. “#” denotes comments below.

``` markdown
Example of Jekyll Header
---
title: Contributions #Name of Page
layout: custom #Keep as custom
keyword: #Whatever the document is about
description: #A short description
sitemap: True #Lets google know this needs to be indexed 
---
```

### Commit Message Standards

All commit messages should follow this general layout. This is to ensure consistency in determining what has been changed.

```
action(thingchanged): description of the change
```

|Actions      |When to use                                                                                                                 |
|:-----------:|:--------------------------------------------------------------------------------------------------------------------------:|
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

### Adding to the Navigation

When adding a new file to the navigation of the website, edit the TOC.yaml file, unless it is for an app branch of the website. When editing the TOC.yaml file, follow the current convention for all the other navigation links. ALL yaml files are located inside the _data folder of the website.

