---
layout: null
---
// This script generates a JavaScript array containing information about each page in the Jekyll site.
// The page data includes URL, title, filename, links, image directory, images, description, keywords, and headings.

// Define an array named 'pages' to store page information
var pages = [{% assign firstPage = "yes" %}
  
  // Loop through each page in the 'site.pages' array
  {% for page in site.pages %}
  
    // Check if the page has a title and is not hidden from the sitemap
    {% if page.title and page.hide_from_sitemap != true %}
    
      // Determine if it's the first page in the loop to handle comma placement
      {% if firstPage == "no" %},{% else %}{% assign firstPage = "no" %}{% endif %}
      
      // Construct an object representing the page and its properties
      {
        // Extract and format the URL, title, filename, links, image directory, images, description, keywords, and headings
        "url":{{ page.url | jsonify }},
        "title":{{ page.title | jsonify }},
        "filename":{{ page.filename | jsonify }},
        "links":{{ page.links | jsonify }},
        "image_dir":{{ page.image_dir | jsonify }},
        "images":{{ page.images | jsonify }},
        "description":{{ page.description | jsonify }},
        "keywords":{{ page.keywords | jsonify }},
        "headings":{{ page.headings | jsonify }}
      }
    
    {% endif %} // End of condition for valid page with title and not hidden from sitemap
    
  {% endfor %} // End of page loop
];
