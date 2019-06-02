---
title: Contributions
layout: custom
sitemap: false
---

## Overview

Hello and thank you for wanting to make a contribution to the INTERJECT. These are the guidelines that we use to make sure our documentation is the highest quality, and consistent. Included in this document is the documentation cycle from creation to approval.

### Process Flow

Step 1: Fork your own branch of the main master branch repo unless you are a content reviewer, in which case, use a clone of the patch branch on the main repository and host locally and make all your changes there before pushing to the origin repository.

Step 2: Make your changes on your forked branch

Step 3: Make a pull request to a branch that is titled "patch-x.x"

Step 4: The changes will be reviewed in the patch branch

Step 5: Once all changes are reviewed and approved, that patch branch will be merged into the master branch on a deployment schedule.

![](/images/Documentation process.png)

### Screenshot Requirements

Screenshots for this website are made consistent by using a window capture program called [Snagit](https://www.techsmith.com/screen-capture.html).

In order to keep screenshots consistent, make sure they are captured in the most current software (see above).If the instructions call for a click action, use a solid, red arrow pointing to the click. Arrows should be 7px in thickness and below the item if possible. No arrow is needed for "Next" or "Finish" actions, or when only a single button is used in a screenshot."Next" and "Close" buttons should be outlined with a 2px red border.

When discussing a specific portion or window inside of an image, use a red rectangle that is 2px wide around the spot to highlight it. Limit these outlines to 3 per screenshot for clarity.

For complex screenshots, include more thorough text narration.

It is important to place arrows where they are easily seen, such as below the dark green menu of Excel 2016. When emphasizing a point, underline the particular point with a 2px red line. Highlight buttons within screenshots using the red square described in this section.

For not very well defined buttons, add an arrow indicating to the user where to click. When using boxes, arrows, and lines in the image, also use a centered shadow by clicking the middle box in the newest version of Snaggit. If multiple steps are contained in one image, label the steps 1, 2, 3, etc. in Snagit. This gives readers more direction when steps are complex. When using arrows and numbers together, always connect the arrow to a number and ensure that the arrow is projecting from the center of the number surrounding the circle.

For images containing multiple steps, place steps in an ordered list below the image, numbered correspondingly and tabbed in once.

Numbers within images should be large enough to read and of the default size.

If a procedure is extremely involved, use a GIF. If a screenshot has multiple images, be sure to use an ordered list within it. When screen capturing windows that contain popups, make sure the popup appears distinct from the page containing it. To do this, allow the popup to slightly overlap other content in the image. Do not line it up with any other lines on the page. Unless a screenshot of just the pop up is needed (for a special circumstance), make sure take screenshots of popups with the windows in which they appear; it is important to show all images with as much context as possible. 

For screenshots of Excel content, make sure the Row and Column definitions of the spreadsheet are visible, again to provide context. If the step depicted in those screenshots does not use the INTERJECT menu ribbon, do not include it in the screenshots (to save space). Make sure when screen-capturing that no personal or confidential data is visible on the screen. Use mary@mycompany.com or joe@mycompany.com for masking report library and email data or remove all personal information using snagit to cover it. For login examples, use "dummy" login credentials. With the exception of login boxes, highlight all boxes from clicks to data entry (use 2px red border). For clickable boxes (and check-boxes), do not use both an arrow and a red border. 

Use the above names consistently. If mary@mycompany.com is used once on a page, use it throughout that page.

Please remove the cursor from the page when the screen is being captured, unless the cursor is needed. If an image is to appear truncated, manually add a "ripped" black border. Always upload your image to be the exact size as the original you had taken. Smaller images, such as in-window popups, should be 360px wide, unless an otherwise more appropriate size is needed.

When directing tab navigation, point to it with an arrow. Do this especially for larger screenshots.

When reviewing for publication, check that no assumptions are made regarding steps–major or minor–required in any process.

### Saving Screenshots

When saving screenshots place them in the /images/[DirectoryToYourPageFolder] folder of the website. If a folder for your page does not exist, please add one and place all images in that folder. This ensures the most simple naming conventions of 01, 02, 03 as the images are displayed on the website. 

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
