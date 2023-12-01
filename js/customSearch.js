// search.js

// Get the query parameter from the URL
const queriedString = window.location.search;

// Extract the 'q' parameter from the query string
const urlParams = new URLSearchParams(queriedString);
const searchTermEncoded = urlParams.get('q');

// Decode the search term
const searchTermDecoded = decodeURIComponent(searchTermEncoded);

//let searchTerm = decodeURI(queryString().q);
console.log(searchTermDecoded);

if(searchTermDecoded != 'undefined' && searchTermDecoded != "") {
  document.getElementById('custom-search-input').value = searchTermDecoded;
  document.getElementById('custom-search-input').focus();
  }

const query = searchTermDecoded.toLowerCase();
const resultsContainer = document.getElementById('custom-search-results');

fetchAndDisplayResults();

document.getElementById('custom-search-form').addEventListener('submit', function (e) {
  e.preventDefault();
  loadPage("/schemas/custom_search?q=" + document.getElementById('custom-search-input').value);
});

function fetchAndDisplayResults() {
  // Fetch the search index from the parent folder
  fetch('../search_index.json')
    .then(response => response.json())
    .then(searchIndex => {
      const results = search(query, searchIndex);
      displayResults(results, resultsContainer, query);
    })
    .catch(error => {
      console.error('Error fetching search index:', error);
    });
}

function search(query, index) {
  // Perform search logic on the index and return matching results
  // This example searches through the content for the query
  return index.filter(page => page.content.toLowerCase().includes(query));
}

function displayResults(results, container, query) {
  // Display the search results on the page
  // You can customize how the results are presented, e.g., as links to the matched pages

  container.innerHTML = '';

  if (results.length === 0) {
    container.innerHTML = '<p>No results found.</p>';
  } else {
    results.forEach(result => {
      const resultItem = document.createElement('div');
      resultItem.innerHTML = `
        <h5><a href="${result.url}" target="_blank">${result.title}</a></h5>
        <p>&emsp;${getSnippet(result.content, query)}</p>
      `;
      container.appendChild(resultItem);
    });
  }
}

function getSnippet(content, query) {
  // Extract a snippet of the content around the matched query with a newline limit
  const snippetBefore = 50; // number of characters to display before the query
  const snippetAfter = 50; // number of characters to display after the query

  const index = content.toLowerCase().indexOf(query);

  if (index !== -1) {
    const start = Math.max(0, index - snippetBefore); // index of the start of the snippet
    const end = Math.min(content.length, index + snippetAfter); // index of the end of the snippet
    
    const snippet = content.substring(start, index) + content.substring(index, end);

    // Wrap the matched query in a span with a yellow background
    const highlightedSnippet = snippet.replace(new RegExp(query, 'ig'), match => `<span style="background-color: yellow;">${match}</span>`);

    return `...${highlightedSnippet}...`;
  } else {
    // If query not found, return the beginning of the content
    return content.substring(0, snippetBefore + snippetAfter) + '...';
  }
}
