// --------------------------------------------------------------
// TOP LEVEL VARIABLES
// --------------------------------------------------------------
const snippetBefore = 50; // number of characters to display before the query
const snippetAfter = 50; // number of characters to display after the query

// Get the query parameter from the URL
const queriedString = window.location.search;
const urlParams = new URLSearchParams(queriedString);

// Extract the parameters from the query string
const searchTerm = urlParams.get('q');
const useRegex = urlParams.get('r');
const allHits = urlParams.get('a');
const topHits = urlParams.get('t');

// Encode and decode the search term
const searchTermEncoded = encodeURIComponent(searchTerm);
const searchTermDecoded = decodeURIComponent(searchTermEncoded);
const query = searchTermDecoded.toLowerCase(); // For case insensitive searching

// Containers
const resultsContainer = document.getElementById('custom-search-results');
const topHitsContainer = document.getElementById('top-hits-results');

// --------------------------------------------------------------
// PAGE SCRIPT
// --------------------------------------------------------------
// Populate the search form with the search term
if(searchTermDecoded != 'undefined' && searchTermDecoded != "") {
	document.getElementById('custom-search-input').value = searchTermDecoded;
}

// Put the focus in the search form
document.getElementById('custom-search-input').focus(); // focus on search input

// Mark the Regex checkbox if the query is a regex query
if(useRegex === 'true') {
	document.getElementById('custom-regex').checked = true;
}

// Mark the allHits checkbox if the query is an allHits query
if(allHits === 'true') {
	document.getElementById('custom-all-hits').checked = true;
}

// Mark the topHits checkbox if the query is an allHits query
if(topHits === 'true') {
	document.getElementById('custom-top-hits').checked = true;
}

// Display the advanced search options if one is selected already
if(useRegex === 'true' || allHits === 'true' || topHits === 'true') {
	toggleOptions();
}

// Display message if the query is Regex and not valid
if (useRegex === 'true' && !isValidRegex(query)) {
	resultsContainer.innerHTML = '<p>Not a valid Regex expression</p>';
}

// Display message if the query is less than 2 characters
else if (query.length < 2) {
	resultsContainer.innerHTML = '<p>Minimum 2 characters</p>';
}
// Fetch and display the results
else {
	if(topHits === 'true') {
		fetchAndDisplayTopHitsResults();
	}
	fetchAndDisplayResults();
}

// --------------------------------------------------------------
// RELOAD PAGE
// --------------------------------------------------------------
// builds a url from the value in the search form and the options selected, then navigates to the url
function reloadPage() {
	loadPage("/schemas/custom_search?q=" + encodeURIComponent(document.getElementById('custom-search-input').value) + "&r=" + document.getElementById('custom-regex').checked + "&a=" + document.getElementById('custom-all-hits').checked + "&t=" + document.getElementById('custom-top-hits').checked);
}

// --------------------------------------------------------------
// LISTENERS
// --------------------------------------------------------------
// Add the listener to the search form
document.getElementById('custom-search-form').addEventListener('submit', function (e) {
	e.preventDefault();
	reloadPage();
});

function handleCustomAllHits() {
	reloadPage()
}

// --------------------------------------------------------------
function handleCustomTopHits() {
	reloadPage()
}

// --------------------------------------------------------------
function handleCustomRegex() {
	reloadPage()
}

// --------------------------------------------------------------
// FUNCTIONS (FETCH AND DISPLAY)
// --------------------------------------------------------------
function fetchAndDisplayTopHitsResults() {
	results = getTopHitsResults(query); // Function in menu.js
	displayTopHitsResults(results, topHitsContainer);
}

// --------------------------------------------------------------
function displayTopHitsResults(results, container) {

	var resultsContainer = document.getElementById("resultsContainer");
	var horizontalLine = document.createElement("hr");
	horizontalLine.style.border = "1px solid #878896";
	resultsContainer.insertBefore(horizontalLine, container);

	container.innerHTML = '';
	
	if(results.length === 0) {
		container.innerHTML = '<p>No top hits results found</p>';
	}
	else {
		const topScore = results[0].score;
		for (i=0; i < results.length; i++) {
			const resultItem = document.createElement('div');
			const titleLink = `<h5 style="margin-bottom: 0px;"><a href="${pages[results[i].topic].url}" target="_blank">${pages[results[i].topic].title}</a></h5>`;
			const relevancyScore = getRelevancy(results[i].score, topScore);
			const hitScore = `<p style="margin-bottom: 0px; margin-top: 0px; font-size: 12px;">Relevancy: ${relevancyScore}%</p>`;
			const urlHighlight = insertHighlightAll(String(pages[results[i].topic].url).toLowerCase(), query);
			const hitURL = `<p style="margin-bottom: 0px; margin-top: 0px">${urlHighlight}</p>`;
			const keywordsHighlight = insertHighlightAll(String(pages[results[i].topic].keywords).toLowerCase(), query);
			const hitKeywords = `<p style="margin-bottom: 0px; margin-top: 0px"><b>Keywords: </b>${keywordsHighlight}</p>`;
			const descriptionHighlight = insertHighlightAll(String(pages[results[i].topic].description).toLowerCase(), query);
			const hitDescription = `<p style="margin-bottom: 0px; margin-top: 0px"><b>Description: </b>${descriptionHighlight}</p>`;
			
			resultItem.innerHTML = `
				${titleLink}
				${hitURL}
				${hitKeywords}
				${hitDescription}
				`;

		container.appendChild(resultItem);
		}
	}
	
}

// --------------------------------------------------------------
function fetchAndDisplayResults() {
  fetch('../search_index.json')
    .then(response => response.json())
    .then(searchIndex => {
      var results;
      if(useRegex === 'true') {
        results = searchRegex(query, searchIndex); // Gets the results with a Regex search
      }
      else {
        results = search(query, searchIndex); // Gets the results with a standard search
      }
      displayResults(results, resultsContainer, query);
    })
    .catch(error => {
      console.error('Error fetching search index:', error);
    });
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
          ? getSnippetRegexAll(result.content, query) // Regex all hits
          : getSnippetRegex(result.content, query); // Regex
      } else {
        snippetContent = allHits === 'true'
          ? getSnippetAll(result.content, query) // Standard all hits
          : getSnippet(result.content, query); // Standard
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
// FUNCTIONS (SEARCH)
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
// FUNCTIONS (SNIPPETS)
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
// FUNCTIONS (OTHER)
// --------------------------------------------------------------
// Highlights a portion of the originalString yellow, from indexStart and extending matchLength number of characters
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

// --------------------------------------------------------------
function getRelevancy(score, topScore) {
	if(score === topScore) {
		return 100
	}
	const result = Math.ceil((score / topScore) * 100);
	return result.toString()
}

// --------------------------------------------------------------
function countOccurrences(content, query) {
  const lowercaseContent = content.toLowerCase();
  const occurrences = lowercaseContent.split(query.toLowerCase()).length - 1;
  return occurrences;
}

// --------------------------------------------------------------
function toggleOptions() {
    var optionsDiv = document.getElementById("advanced-search-options");
	spaceDiv = document.getElementById("custom-space");
    optionsDiv.style.display = (optionsDiv.style.display === "block") ? "none" : "block";
	spaceDiv.style.display = (optionsDiv.style.display === "block") ? "none" : "block";
  }
