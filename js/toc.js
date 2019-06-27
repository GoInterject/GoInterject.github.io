---
layout: null
---

// check the url of the webpage sitePath is defined in head of custom.html
// define the nav container variable
var docstoc

// check to see if this is part of the default nave
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

renderNav(docstoc);

