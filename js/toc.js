---
layout: null
---

// check the url of the webpage sitePath is defined in head of custom.html
// define the nav container variable
var docstoc

// check to see if this is part of the default nav
if (sitePath.startsWith("/w") == true){
    docstoc = {{ site.data.toc | jsonify }};
} 
// if not part of the default nav check if it's an app
else if (sitePath.startsWith("/bApps/bFinancials") == true){
    docstoc = {{ site.data.apptoc.financial | jsonify }};
} 
else if (sitePath.startsWith("/bApps/InterjectTraining") == true){
    docstoc = {{ site.data.apptoc.InterjectTraining | jsonify }};
}
// if it is not an app nor a default page, then load the default nav
 else {
    docstoc = {{ site.data.toc | jsonify }};
}

// search page case and subcases
if (sitePath.startsWith("/schemas/search") == true){
    // now determine the referring (origination?) page to determine which docstoc to assign
    if (referringPage.includes("/w") == true){
        docstoc = {{ site.data.toc | jsonify }};
    }
    else if (referringPage.includes("/bApps/bFinancials") == true){
        docstoc = {{ site.data.apptoc.financial | jsonify }};
    }
    else if (referringPage.includes("/bApps/InterjectTraining") == true){
        docstoc = {{ site.data.apptoc.InterjectTraining | jsonify }};
    }
    else {
        docstoc = {{ site.data.toc | jsonify }};
    }
}

renderNav(docstoc);