const snippetBefore = 50; // number of characters to display before the query
const snippetAfter = 50; // number of characters to display after the query

// Get the query parameter from the URL
const queriedString = window.location.search;
const urlParams = new URLSearchParams(queriedString);

// Extract the parameters from the query string
const searchTermEncoded = urlParams.get('q');
const useRegex = urlParams.get('r');
const allHits = urlParams.get('a');

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
if(allHits === 'true') {
  document.getElementById('custom-all-hits').checked = true;
}

fetchAndDisplayResults();

// Search listener
document.getElementById('custom-search-form').addEventListener('submit', function (e) {
  e.preventDefault();
  loadPage("/schemas/custom_search?q=" + document.getElementById('custom-search-input').value + "&r=" + document.getElementById('custom-regex').checked + "&a=" + document.getElementById('custom-all-hits').checked);
});

// --------------------------------------------------------------
// FUNCTIONS
// --------------------------------------------------------------
function fetchAndDisplayResultsRegex() {
  alert("regex")
}
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
  // This searches through the content for the query
  return index.filter(page => page.content.toLowerCase().includes(query));
}
// --------------------------------------------------------------

function searchRegex(query, searchIndex) {
  const regex = new RegExp(query, 'i'); // 'i' for case-insensitive, adjust flags as needed
  return searchIndex.filter(item => regex.test(item.content));
}
// --------------------------------------------------------------

function displayResults(results, container, query) {
  container.innerHTML = '';

  if (results.length === 0) {
    container.innerHTML = '<p>No results found.</p>';
  } else {
    results.forEach(result => {
      const resultItem = document.createElement('div');
      if(useRegex === 'true') {
        if(allHits === 'true') {
          resultItem.innerHTML = `
          <h5><a href="${result.url}" target="_blank">${result.title}</a></h5>
          <p>${getSnippetRegexAll(result.content, query)}</p>
        `;
        }
        else {
          resultItem.innerHTML = `
          <h5><a href="${result.url}" target="_blank">${result.title}</a></h5>
          <p>${getSnippetRegex(result.content, query)}</p>
        `;
        }
      }
      else {
        if(allHits === 'true') {
          resultItem.innerHTML = `
            <h5><a href="${result.url}" target="_blank">${result.title}</a></h5>
            <p>&emsp;${getSnippetAll(result.content, query)}</p>
          `;
        }
        else {
          resultItem.innerHTML = `
            <h5><a href="${result.url}" target="_blank">${result.title}</a></h5>
            <p>&emsp;${getSnippet(result.content, query)}</p>
          `;
        }
      }
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
    const matchLength = match[0].length
    const currentSnippet = content.substring(start, end);
    const matchStartInSnippet = match.index - start;

    // Highlight the matched part with a yellow background
    //const highlightedSnippet = currentSnippet.replace(new RegExp(query, 'ig'), m => `<span style="background-color: yellow;">${m}</span>`);
    const highlightedSnippet = insertHighlight(currentSnippet, snippetBefore, matchLength);

    snippets.push(`&emsp;...${highlightedSnippet}...`);
  }

  // If there are no matches, return the original content
  if (snippets.length === 0) {
    return content.substring(0, snippetBefore + snippetAfter) + '...';
  }

  // Append the remaining content after the last match
  //snippets.push(content.substring(lastIndex, lastIndex + snippetAfter));

  // Join the snippets with newline characters
  return snippets.join('<br>');
}

// --------------------------------------------------------------
function getSnippet(content, query) {
  const index = content.toLowerCase().indexOf(query);

  if (index !== -1) {
    const start = Math.max(0, index - snippetBefore); // index of the start of the snippet
    const end = Math.min(content.length, index + snippetAfter); // index of the end of the snippet
    
//    const snippet = content.substring(start, index) + content.substring(index, end);
    const snippet = content.substring(start, end);

    // Wrap the matched query in a span with a yellow background
    const highlightedSnippet = snippet.replace(new RegExp(query, 'ig'), match => `<span style="background-color: yellow;">${match}</span>`);

    return `&emsp;...${highlightedSnippet}...`;
  } else {
    // If query not found, return the beginning of the content
    return content.substring(0, snippetBefore + snippetAfter) + '...';
  }
}

// --------------------------------------------------------------
function getSnippetAll(content, query) {
  const regex = new RegExp(query, 'ig');
  let match;
  let snippets = [];
  let lastIndex = 0;

  while ((match = regex.exec(content)) !== null) {
    const start = Math.max(0, match.index - snippetBefore);
    const end = Math.min(content.length, match.index + match[0].length + snippetAfter);
    const snippet = content.substring(start, end);

    // Wrap the matched query in a span with a yellow background
    //const highlightedSnippet = snippet.replace(new RegExp(query, 'ig'), m => `<span style="background-color: yellow;">${m}</span>`);
    const highlightedSnippet = insertHighlight(snippet, match.index, match.index + match[0].length);

    snippets.push(`&emsp;...${highlightedSnippet}...`);

    // Set lastIndex to the end of the current match
    lastIndex = regex.lastIndex;
  }

  // If there are no matches, return the beginning of the content
  if (snippets.length === 0) {
    return content.substring(0, snippetBefore + snippetAfter) + '...';
  }

  // Remove the leading whitespace from the first snippet
  snippets[0] = snippets[0].replace(/^&emsp;/, '');

  // Append the remaining content after the last match
  snippets.push(content.substring(lastIndex, lastIndex + snippetAfter));

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
    console.log("indexStart = " + indexStart + "; indexEnd =" + matchLength + ",s = " + s);
    return s;
}