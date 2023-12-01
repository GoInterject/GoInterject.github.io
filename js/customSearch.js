// Get the query parameter from the URL
const queriedString = window.location.search;
const urlParams = new URLSearchParams(queriedString);

// Extract the parameters from the query string
const searchTermEncoded = urlParams.get('q');
const useRegex = urlParams.get('r');

// Decode the search term
const searchTermDecoded = decodeURIComponent(searchTermEncoded);

if(searchTermDecoded != 'undefined' && searchTermDecoded != "") {
  document.getElementById('custom-search-input').value = searchTermDecoded;
  }

document.getElementById('custom-search-input').focus(); // focus on search input

const query = searchTermDecoded.toLowerCase();
const resultsContainer = document.getElementById('custom-search-results');

if(useRegex === 'true') {
  document.getElementById('custom-regex').checked = true;
}

fetchAndDisplayResults();

// Search listener
document.getElementById('custom-search-form').addEventListener('submit', function (e) {
  e.preventDefault();
  loadPage("/schemas/custom_search?q=" + document.getElementById('custom-search-input').value + "&r=" + document.getElementById('custom-regex').checked);
});

// FUNCTIONS --------------------------------------------------------------
function fetchAndDisplayResultsRegex() {
  alert("regex")
}

function fetchAndDisplayResults() {
  fetch('../search_index.json')
    .then(response => response.json())
    .then(searchIndex => {
      var results;
      if(useRegex === 'true') {
        results = searchRegex(query, searchIndex);
      }
      else {
        results = search(query, searchIndex);
      }
      displayResults(results, resultsContainer, query);
    })
    .catch(error => {
      console.error('Error fetching search index:', error);
    });
}

function search(query, index) {
  // This searches through the content for the query
  return index.filter(page => page.content.toLowerCase().includes(query));
}

function searchRegex(query, searchIndex) {
  const regex = new RegExp(query, 'i'); // 'i' for case-insensitive, adjust flags as needed
  return searchIndex.filter(item => regex.test(item.content));
}

function displayResults(results, container, query) {
  container.innerHTML = '';

  if (results.length === 0) {
    container.innerHTML = '<p>No results found.</p>';
  } else {
    results.forEach(result => {
      const resultItem = document.createElement('div');
      if(useRegex === 'true') {
        resultItem.innerHTML = `
        <h5><a href="${result.url}" target="_blank">${result.title}</a></h5>
        <p>&emsp;${getSnippetRegex(result.content, query)}</p>
      `;
      }
      else {
      resultItem.innerHTML = `
        <h5><a href="${result.url}" target="_blank">${result.title}</a></h5>
        <p>&emsp;${getSnippet(result.content, query)}</p>
      `;
      }
      container.appendChild(resultItem);
    });
  }
}

function getSnippetRegex(content, query) {
  const snippetBefore = 50;
  const snippetAfter = 50;

  const regex = new RegExp(`.{0,${snippetBefore}}(${query}).{0,${snippetAfter}}`, 'ig');
  const match = regex.exec(content);

  if (match) {
    const start = match.index - snippetBefore;
    const end = match.index + match[0].length + snippetAfter;
    const snippet = content.substring(Math.max(0, start), end);

    // Highlight the matched part with a yellow background
    const highlightedSnippet = snippet.replace(new RegExp(query, 'ig'), match => `<span style="background-color: yellow;">${match}</span>`);

    return `...${highlightedSnippet}...`;
  } else {
    return content.substring(0, snippetBefore + snippetAfter) + '...';
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
