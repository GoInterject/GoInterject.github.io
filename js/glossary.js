// This script generates a JavaScript array containing glossary terms and their definitions.
// The glossary data is sourced from the Jekyll site's YAML data file.

// Define an array named 'glossary' to store glossary terms and their definitions
var glossary = [
    // Loop through each entry in the 'site.data.glossary' array
    {% for entry in site.data.glossary %}
    {
      // Extract the term from the current entry and format it as JSON
      "term": {{ entry[0] | jsonify }},
      // Extract the definition from the current entry, apply Markdown formatting, and replace internal links with custom URLs
      "def": {{ entry[1] | markdownify | replace:'href="#','href="/glossary/?term=' | jsonify }}
    }{% unless forloop.last %},{% endunless %} // Add a comma if not the last entry
    {% endfor %}
  ];
  