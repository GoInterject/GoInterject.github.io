const snippetBefore = 50; // number of characters to display before the query
const snippetAfter = 50; // number of characters to display after the query

// Get the query parameter from the URL
const queriedString = window.location.search;
const urlParams = new URLSearchParams(queriedString);

// Extract the parameters from the query string
const searchTerm = urlParams.get('q');
const useRegex = urlParams.get('r');
const allHits = urlParams.get('a');

// Encode and Decode the search term
const searchTermEncoded = encodeURIComponent(searchTerm);
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
if(allHits === 'true') {
  document.getElementById('custom-all-hits').checked = true;
}

if (useRegex === 'true' && !isValidRegex(query)) {
  resultsContainer.innerHTML = '<p>Not a valid Regex expression</p>';
}
else if (query.length < 2) {
  resultsContainer.innerHTML = '<p>Minimum 2 characters</p>';
}
else {
  fetchAndDisplayResults();
}

// Search listener
document.getElementById('custom-search-form').addEventListener('submit', function (e) {
  e.preventDefault();
  loadPage("/schemas/custom_search?q=" + encodeURIComponent(document.getElementById('custom-search-input').value) + "&r=" + document.getElementById('custom-regex').checked + "&a=" + document.getElementById('custom-all-hits').checked);
});

// --------------------------------------------------------------
// FUNCTIONS
// --------------------------------------------------------------
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

// --------------------------------------------------------------
function search(query, index) {
  return index.map(page => {
    const lowercaseContent = page.content.toLowerCase();
    const occurrences = countOccurrences(lowercaseContent, query);

    return {
      ...page,
      occurrences: occurrences
    };
  }).filter(page => page.occurrences > 0);
}

// --------------------------------------------------------------
function countOccurrences(content, query) {
  const lowercaseContent = content.toLowerCase();
  const occurrences = lowercaseContent.split(query.toLowerCase()).length - 1;
  return occurrences;
}

// --------------------------------------------------------------
function searchRegex(query, searchIndex) {
  const regex = new RegExp(query, 'ig'); // 'i' for case-insensitive, adjust flags as needed

  return searchIndex.map(item => {
    const matches = item.content.match(regex);
    const occurrences = matches ? matches.length : 0;

    return {
      ...item,
      occurrences: occurrences
    };
  }).filter(item => item.occurrences > 0);
}

// --------------------------------------------------------------
function displayResults(results, container, query) {
  container.innerHTML = '';

  if (results.length === 0) {
    container.innerHTML = '<p>No results found</p>';
  } 
  else {

    results.forEach(result => {
      const resultItem = document.createElement('div');
      const titleLink = `<h5 style="margin-bottom: 0px;"><a href="${result.url}" target="_blank">${result.title}</a></h5>`;
      const occurrencesContent = `<p style="margin-bottom: 0px; margin-top: 0px; font-size: 12px;">Occurrences: ${result.occurrences}</p>`;

      let snippetContent;
      if (useRegex === 'true') {
        snippetContent = allHits === 'true'
          ? getSnippetRegexAll(result.content, query)
          : getSnippetRegex(result.content, query);
      } else {
        snippetContent = allHits === 'true'
          ? getSnippetAll(result.content, query)
          : getSnippet(result.content, query);
      }

      resultItem.innerHTML = `
        ${titleLink}
        ${occurrencesContent}
        <p>&emsp;${snippetContent}</p>
      `;

      container.appendChild(resultItem);
    });
  }
}

// --------------------------------------------------------------
function getSnippetRegex(content, query) {
  const regex = new RegExp(`(${query})`, 'ig');
  const match = regex.exec(content);

  if (match) {
    const start = Math.max(0, match.index - snippetBefore);
    const end = Math.min(content.length, match.index + match[0].length + snippetAfter);
    const snippet = content.substring(start, end);

    // Highlight the matched part with a yellow background
    const highlightedSnippet = snippet.replace(new RegExp(query, 'ig'), match => `<span style="background-color: yellow;">${match}</span>`);

    return `&emsp;...${highlightedSnippet}...`;
  } else {
    return content.substring(0, snippetBefore + snippetAfter) + '...';
  }
}
// --------------------------------------------------------------

function getSnippetRegexAll(content, query) {
  const regex = new RegExp(`(${query})`, 'ig');
  let match;
  let snippets = [];
  
  while ((match = regex.exec(content)) !== null) {
    const start = Math.max(0, match.index - snippetBefore);
    const end = Math.min(content.length, match.index + match[0].length + snippetAfter);
    const currentSnippet = content.substring(start, end);

    // Highlight the matched part with a yellow background
    const highlightedSnippet = insertHighlight(currentSnippet, match.index - start, match[0].length);

    snippets.push(`&emsp;...${highlightedSnippet}...`);
  }

  // If there are no matches, return the original content
  if (snippets.length === 0) {
    return content.substring(0, snippetBefore + snippetAfter) + '...';
  }

  // Join the snippets with newline characters
  return snippets.join('<br>');
}

// --------------------------------------------------------------
function getSnippet(content, query) {
  const index = content.toLowerCase().indexOf(query);

  if (index !== -1) {
    const start = Math.max(0, index - snippetBefore); // index of the start of the snippet
    const end = Math.min(content.length, index + snippetAfter); // index of the end of the snippet
    const snippet = content.substring(start, end);

    // Wrap the matched query in a span with a yellow background
    const highlightedSnippet = snippet.replace(new RegExp(escapeString(query), 'ig'), match => `<span style="background-color: yellow;">${match}</span>`);

    return `&emsp;...${highlightedSnippet}...`;
  } else {
    // If query not found, return the beginning of the content
    return content.substring(0, snippetBefore + snippetAfter) + '...';
  }
}

// --------------------------------------------------------------
function getSnippetAll(content, query) {
  const regex = new RegExp(escapeString(query), 'ig');
  let match;
  let snippets = [];

  while ((match = regex.exec(content)) !== null) {
    const start = Math.max(0, match.index - snippetBefore);
    const end = Math.min(content.length, match.index + match[0].length + snippetAfter);
    const snippet = content.substring(start, end);

    // Wrap the matched query in a span with a yellow background
    const highlightedSnippet = insertHighlight(snippet, match.index - start, match[0].length);

    snippets.push(`&emsp;...${highlightedSnippet}...`);
  }

  // If there are no matches, return the beginning of the content
  if (snippets.length === 0) {
    return content.substring(0, snippetBefore + snippetAfter) + '...';
  }

  // Remove the leading whitespace from the first snippet
  snippets[0] = snippets[0].replace(/^&emsp;/, '');

  return snippets.join('<br>');
}

// --------------------------------------------------------------
// Highlights the matched middle section of a string yellow
function insertHighlight(originalString, indexStart, matchLength) {
  const s = originalString.substring(0, indexStart) +
    `<span style="background-color: yellow;">` + 
    originalString.substring(indexStart, indexStart + matchLength) + 
    `</span>` +
    originalString.substring(indexStart + matchLength, originalString.length);

    return s;
}

// --------------------------------------------------------------
// Highlights all matched strings with yellow
function insertHighlightAll(originalString, stringToHighlight) {
  return originalString.replace(new RegExp(escapeString(stringToHighlight), 'ig'), m => `<span style="background-color: yellow;">${m}</span>`);
}

// --------------------------------------------------------------
function escapeString(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

// --------------------------------------------------------------
function isValidRegex(str) {
  try {
    new RegExp(str);
    return true;
  } catch (e) {
    return false;
  }
}