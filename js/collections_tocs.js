---
layout: null
---
// The percentage signs in the code are part of Jekyll's templating syntax. 
// In Jekyll, these are used to denote control flow statements and other logic within templates.
// These percentage sign codes allow Jekyll to dynamically generate JavaScript code 
//based on the pages in the "samples" collection.

// Define an array named collectionsTOC.
var collectionsTOC = new Array()
// Populate the collectionsTOC array with entries for the "library" collection.
collectionsTOC["library"] = [
  // Loop through each page in the "samples" collection.
  {% for page in site.samples %}
  {
      // Add an object to the array with the path and title of the current page.
      "path": {{ page.url | jsonify }}, // Path of the current page, converted to JSON format.
      "title": {{ page.title | jsonify }} // Title of the current page, converted to JSON format.
    }
    // Add a comma if it's not the last page in the collection.
    {% unless forloop.last %},{% endunless %}
    {% endfor %}
  ]