---
title: "Docs search"
tree: false
sitemap: false
keywords: search, interject, documentation, find
description: Interject documentation search results
---

<style>
    #custom-search-form {
        padding-bottom: 20px;
        background-color: white;
        display: flex; /* Use flexbox */
  }
    #custom-search-input {
        flex: 1; /* Let the input grow to fill available space */
  }

    #custom-search-button {
        margin-left: 10px;
  }

    #custom-search-results {
        /* Add styling for the results container as needed */
  }
</style>

<form id="custom-search-form">
  <input type="search" id="custom-search-input" placeholder="Enter your search query">
  <button type="submit" id="custom-search-button">Search</button>
</form>

<div id="custom-search-results"></div>

<script src="../js/customSearch.js"></script>
