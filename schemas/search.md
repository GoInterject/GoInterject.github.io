---
title: "Docs search"
filename: "search.md"
keywords: [Search, Interject, documentation, manual, guide, reference, api]
headings: []
links: []
image_dir: ""
images: []
description: Interject documentation search results
noratings: false
notoc: false
notags: false
tree: false
sitemaps: false
---

<style type='text/css'>
#my-cse1 { all: initial !important; all: default !important; }
#my-cse1 table, #my-cse1 table tr, #my-cse1 table tr th, #my-cse1 table tr td, .gs-bidi-start-align { border: 0px !important; padding: 0px !important; line-height: initial !important; margin: 0px !important; }
.gs-snippet { margin-top: 0px !important; margin-bottom: 0px !important; padding: 0px !important; color: #999}
.gs-webResult .gs-result .gs-no-results-result { padding: 10px !important; }
.gs-per-result-labels { display: none !important; }
.gsc-url-top, .gsc-thumbnail-inside, .gs-spelling { padding: 0px !important; }
.gcsc-branding { padding-right: 0px !important; }
.gsc-tabHeader.gsc-tabhActive, .gsc-tabsArea { border-color: #CCC !important; }
.gcs-input, #gsc-i-id1 { padding: 5px 5px 5px 5px !important; }
#gscb_a, .gscb_a { padding: 3px 0px 0px 0px !important;}
.gsc-control-cse, .gsc-control-cse-en { padding: 0px !important; }
.gsc-result-info { padding-bottom: 0px !important; }
.gsc-adBlock { display: none; }
</style>

<div id="glossaryMatch"></div>

{% comment %}
This block of code retrieves the search hits via the Google Programmable Search Engine API
To make changes in the way the Search engine performs or looks, log in to the control panel at:
https://programmablesearchengine.google.com/controlpanel/all
{% endcomment %}

<div id="my-cse1">
<script>
  (function() {
    var cx = '009083416940869700725:jddtu1heaf0';
    var gcse = document.createElement('script');
    gcse.type = 'text/javascript';
    gcse.async = true;
    gcse.src = 'https://cse.google.com/cse.js?cx=' + cx;
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(gcse, s);
  })();
  //console.log("googlecustomsearch completed");
</script>


{% comment %}
This block of code displays a search box on the page
{% endcomment %}

<div class="gcse-searchbox"></div>

{% comment %}
This block of code displays the search hits
{% endcomment %}

<div class="gcse-searchresults"></div>

{% comment %}
This block of code seems to change the title of the search page
{% endcomment %}

<script defer>
  //console.log("Begin setTimeout Function");
setTimeout(function(){
  $(document).ready(function() {
    let searchTerm = decodeURI(queryString().q);
    if(searchTerm != 'undefined' && searchTerm != "") {
      //console.log("begin undefined searchTerm");
      //console.log(searchTerm)
      $("#st-search-input").val(searchTerm);
      $("#st-search-input").focus();
      // Update heading with term user searched for
      //console.log("middle undefined searchTerm");
      let currHeading = $("h1").text();
      $("h1").text(currHeading + " results for: " + searchTerm);
      //console.log(currHeading);
    }
  //console.log("document load");
  });
}, 1);
</script>
