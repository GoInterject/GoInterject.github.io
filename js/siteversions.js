---
layout: null
---
// This file is used to determine the objects being loaded by the archive-list file
const rootUrl = 'https://docs.gointerject.com'

if (window.navigator.onLine ) {
  /* Get the json object, then extract the information. Once extracted, add html element tags to it */
  $.getJSON("/js/siteversions.json", function(result){
    var buttonCode = null;
    var listItems = new Array();
    $.each(result, function(i, field){ 
        var prettyName = 'Interject ' + field.name;
        var fullUrl = rootUrl + field.path;
        if ( buttonCode == null ) {
          // Get the button code
          buttonCode = '<button id="archive-menu" data-toggle="dropdown" class="btn dropdown-toggle" style="border: 1px solid #254356; background-color: #fff; color: #254356;">' + prettyName + '&nbsp;(current) &nbsp;<span class="caret"></span></button>';
          
          listItems.push('<li role="presentation"><a role="menuitem" tabindex="-1" href="'+ fullUrl + '">' + prettyName + '</a></li>');
        } else {
            listItems.push('<li role="presentation"><a role="menuitem" tabindex="-1" href="'+ fullUrl + '">' + prettyName + '</a></li>');
        }
      
    });
  });
};



