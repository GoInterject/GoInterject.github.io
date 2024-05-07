// This file is used to determine the objects being loaded by the archive-list file

// Get the root URL of the current page
const rootUrl = window.location.href.split("/")[0];

// Check if the browser is online
if (window.navigator.onLine ) {
  /* Get the JSON object, then extract the information. Once extracted, add HTML element tags to it */
  $.getJSON("/js/siteversions.json", function(result){
    var buttonCode = null;
    var listItems = new Array();
    $.each(result, function(i, field){ 
        // Construct a pretty name for the version
        var prettyName = 'Interject ' + field.name;
        // Construct the full URL for the version
        var fullUrl = rootUrl + field.path;
        
        // If the button code is not yet generated, create it
        if ( buttonCode == null ) {
          // Generate the button code for the dropdown menu
          buttonCode = '<button id="archive-menu" data-toggle="dropdown" class="btn dropdown-toggle" style="border: 1px solid #254356; background-color: #fff; color: #254356;">' + prettyName + '&nbsp;(current) &nbsp;<span class="caret"></span></button>';
          
          // Add the first list item for the current version
          listItems.push('<li role="presentation"><a role="menuitem" tabindex="-1" href="'+ fullUrl + '">' + prettyName + '</a></li>');
        } else {
            // Add subsequent list items for other versions
            listItems.push('<li role="presentation"><a role="menuitem" tabindex="-1" href="'+ fullUrl + '">' + prettyName + '</a></li>');
        }
      
    });
  });
};
