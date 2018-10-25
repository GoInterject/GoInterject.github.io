---
layout: custom
title:  "Document new website"
date:   2018-03-03 9:03:02 -0700
categories: documentation
---

Portal site should be the go to area. Whether it is downloads or documentation or forms. However to make it more easy to follow we need to reduce the options we have in the site for most users.

## On bording new developers from start to finish. 
1. Email invitation new clients (simplify)
2. Download turorial package 
3. 


## Portal 
Minimize what standard user sees in the portals site. Remove/Move:
1. My Offerings - should be part of myApps
2. My Data - should not be available to standard users (only Client Admin, Editor, Developer)
3. Settings - The only setting that should be available for stander user is to update his/er profile. Currently standard user can modify company profile. The user should be managed from.
    1. Setting should be managed from the
4. Instead of having a vertical main menu we should have a horizontal menu.
5. Top bar should include links back to portal site. (screenshot 11)

### Rebuilding Portal site
1. Example site - [zapier]

![images12](/images/Image12.png){:class="img-responsive"}

### Workflow for app development.
Example site: https://zapier.com/ - Connecting application and automate workflow
1. Steps to create an application
    1. Individual steps before and app can be packaged
        1. Create connections
            1. Should have a way to test connection string inside website. This should be done with java-script since it has to tested form client end not server
        2. Create Portal
        3. Create Excel Template - in excel 
            1. (we will need to create a way to view and manage reports templates in the website)
    2. Package an application
        1. Create Name/description specify public private
            1. (optional) Need a way to link to  app documentation/ or add documentation
        2. Select excel templates
            1. need access to report library from web
            2. select the templates that we what to include.
            3. At this point we should be able to figure out the portals and connections needed. This should be defaulted but allow users to change and modify. 
        3. Select portals
        4. Select connection  
            1. will default based on the portals that are selected
            2. specify the connection that can be overwrite



![images10](/images/Image10.png){:class="img-responsive"} 

## Documentation
1. Native GitHub static website [pages.github]
2. Having 2 documentation location may cause issues with having to duplicate documentation. An alliterative is to display different documentation based on roles that a users has in Interject
    1. Basic documentation
        1. Mostly graphical
        2. Walk through
    2. Best practice
    3. Advance (Developer)
    4. Creating data portal
    5. Api - documenting parameter
    6. Store procedure -
3. Documentation site is separate from portals side but the link should be found on the portal side
4. Apple Design is something that we should incorporate into our documentation (screenshot 4) [image4]
5. include video here. How to make excel into an app video (screenshot 5)
6. For the documentation site we will use Jekyll as the patform. This will allow static pages to be edited and maintained in github with source control as the back end.
    1. This is what docker is using. Below are key areas we should include
    2. All issues to documentation can change requests can be done through github (screenshot 1)
    3. On the left they have a table of contains and on the right they have a page outline (screenshot 2,3)
    4. Top menu should be links to other websites such as Portal ,main and form sites.
7. One downside is that we will not be able setup multi level security for a statistic website. We can provide basic security to allow users access to the site but in my opinion we should hide link for standard user but if someone has a direct link to the documentation site they should have full access.

![images4](/images/Image4.png){:class="img-responsive"} 

![images5](/images/Image5.png){:class="img-responsive"} 

![images1](/images/Image1.png){:class="img-responsive"} 

![images2](/images/Image2.png){:class="img-responsive"} 

![images3](/images/Image3.png){:class="img-responsive"} 

## Forums 
Apple defiantly has the best organization for forums (screenshot 5,6). Microsoft and salesforse have some good elements.
1. Section
    1. Ideas
    2. Excel
    3. Data
    4. Interject portal
    5. add-in
    6. ides visual studio and SSMS
    7. others
2.  However simple maybe betters
3. Other elements -

![images5](/images/Image5.png){:class="img-responsive"}

![images6](/images/Image6.png){:class="img-responsive"}

### Discourse Platform
The best platform for a forum is [Discourse]

This is opensource software with many sites that will host and maintain it

![images11](/images/Image11.png){:class="img-responsive"}

https://flarum.org/ appears to  be another easy to use forum


Discussing the different type of forums - 
https://www.a2hosting.com/blog/5-outstanding-forum-platforms-set-online-community/


[zapier]: https://zapier.com
[pages.github]: https://help.github.com/articles/what-is-github-pages/
[Discourse]: https://www.discourse.org/


