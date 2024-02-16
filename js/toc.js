---
layout: null
---

// check the url of the webpage sitePath is defined in head of custom.html
// define the nav container variable
var docstoc

var docstocTesting = {{ site.data.testingtoc.testingtoc | jsonify }};
var docstocMain = {{ site.data.toc | jsonify }};
var docstocFinancials = {{ site.data.apptoc.financial | jsonify }};
var docstocTraining = {{ site.data.apptoc.InterjectTraining | jsonify }};
var docstocWIP = {{ site.data.apptoc.wip | jsonify }};

// check to see if this is part of the default nav
if (sitePath.startsWith("/wTesting") == true){
   docstoc = docstocTesting
}
else if (sitePath.startsWith("/w") == true){
   docstoc = docstocMain
}
 // if not part of the default nav check if it's an app
else if (sitePath.startsWith("/bApps/bFinancials") == true){
   docstoc = docstocFinancials
}
else if (sitePath.startsWith("/bApps/InterjectTraining/WIP") == true){
    docstoc = docstocWIP;
}
else if (sitePath.startsWith("/bApps/InterjectTraining") == true){
    docstoc = docstocTraining;
}
// if it is not an app nor a default page, then load the default nav
else {
   docstoc = docstocMain
}

// search page case and subcases
if (sitePath.startsWith("/schemas/custom_search") == true || sitePath.startsWith("/bApps/schemas/custom_search") == true){
    // now determine the referring (origination?) page to determine which docstoc to assign
    if (referringPage.includes("/wTesting") == true){
        docstoc = docstocTesting
    }
    else if (referringPage.includes("/w") == true){
        docstoc = docstocMain
    }
    else if (referringPage.includes("/bApps/bFinancials") == true){
        docstoc = docstocFinancials
    }
    else if (referringPage.includes("/bApps/InterjectTraining/WIP") == true){
        docstoc = docstocWIP
    }
    else if (referringPage.includes("/bApps/InterjectTraining") == true){
        docstoc = docstocTraining
    }
    else {
        docstoc = docstocMain
    }
}

renderNav(docstoc);