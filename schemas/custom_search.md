---
title: "Docs search"
tree: false
sitemap: false
keywords: [search, interject, documentation, find]
description: Interject documentation search results
---

<style>
    #custom-search-form {
        margin-bottom: 10px;
        background-color: white;
        display: flex; /* Use flexbox */
    }
    #custom-search-input {
        flex: 1; /* Let the input grow to fill available space */
    }
    #custom-search-button {
        margin-left: 10px;
        margin-right: 10px;
    }
    #custom-search-results {
  }
    #custom-regex {
        margin-right: 5px;
        margin-bottom: 10px;
    }
    #custom-all-hits {
        margin-left: 15px;
        margin-bottom: 10px;
    }

</style>

<form id="custom-search-form">
  <input type="search" id="custom-search-input" placeholder="Enter your search query">
  <button type="submit" id="custom-search-button">Search</button>
</form>

<div>
  <input type="checkbox" id="custom-regex">
  <label for="custom-regex">Use Regex</label>
  <input type="checkbox" id="custom-all-hits">
  <label for="custom-all-hits">Show all hits</label>
</div>

<div id="custom-search-results"></div>

<script src="../js/customSearch.js"></script>
