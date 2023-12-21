---
title: "Doc Search"
tree: false
sitemap: false
keywords: search, interject, documentation, find
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
    #custom-top-hits {
        margin-left: 15px;
        margin-bottom: 10px;
    }
	#custom-advanced_button {
		display: none; /* Hide the div by default */
		text-align: right;
	}
	#advanced-search-options {
    }
	#custom-space {
		display: none;
	}
	#orderby_dropdown_container {
		display: none;
	}
	
</style>

<form id="custom-search-form">
  <input type="search" id="custom-search-input" placeholder="Enter your search query">
  <button type="submit" id="custom-search-button">Search</button>
</form>

<div class="orderby_dropdown_container" style="float: right;">
	<label for="dropdown">Sort:</label>
  <select id="orderby_dropdown" name="Sort" onchange="handleDropdownChange(this)">
    <option value="occurrence">Occurrence</option>
    <option value="alphabetic">Alphabetically</option>
    <option value="date">Date</option>
  </select>
  </div>

<div id="custom-advanced_button">
<button id="custom-advanced-search" style="float: right;" onclick="toggleOptions()">Advanced Search</button>
</div>

<div id="advanced-search-options">
  <input
    type="checkbox"
    id="custom-regex"
    title="Searches with Regex syntax"
	onclick="handleCustomRegex()"
  >
  <label for="custom-regex">Use Regex</label>
  <input
    type="checkbox"
    id="custom-all-hits"
    title="Displays all hits in the page(s)"
	onclick="handleCustomAllHits()"
  >
  <label for="custom-all-hits">Show all hits</label>
  <input
    type="checkbox"
    id="custom-top-hits"
    title="Displays hits in page title, url, keywords, and descriptions (Standard search only)"
	onclick="handleCustomTopHits()"
  >
  <label for="custom-top-hits">Display top hits</label>
</div>

<div id="custom-space">
	<br>
</div>

<div id="resultsContainer">
	<div id="top-hits-results"></div>
	<hr style="border: 1px solid #878896;">
	<div id="custom-search-results"></div>
</div>
