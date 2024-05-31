/*
This code is for the custom search feature of the website. 
*/
// --------------------------------------------------------------
// TOP LEVEL VARIABLES
// --------------------------------------------------------------
const snippetBefore = 50; // number of characters to display before the query
const snippetAfter = 50; // number of characters to display after the query

// Get the query parameter from the URL
const queriedString = window.location.search;
const urlParams = new URLSearchParams(queriedString);

/* 
Extract the parameters from the query string

Queries for search are formatted and added to the search URL. For example:
https://docs.gointerject.com/schemas/custom_search?q=sample%20&r=false&a=true&t=true
*/
const searchTerm = urlParams.get('q');
const useRegex = urlParams.get('r');
const allHits = urlParams.get('a');
const topHits = urlParams.get('t');

// Encode and decode the search term (e.g. converts %20 to spaces)
const searchTermEncoded = encodeURIComponent(searchTerm);
const searchTermDecoded = decodeURIComponent(searchTermEncoded);
const query = searchTermDecoded.toLowerCase(); // For case insensitive searching

// Containers
const resultsContainer = document.getElementById('custom-search-results');
const topHitsContainer = document.getElementById('top-hits-results');

// Results
var results = new Array();
var topHitsResults = new Array();

// Page
var currentPageUrl = window.location.href;

// --------------------------------------------------------------
// PAGE SCRIPT (Builds the page elements)
// --------------------------------------------------------------
// Populate the search form element with the search term
var searchInput = document.getElementById('custom-search-input');
if (searchInput) {
  if (searchTermDecoded !== 'undefined' && searchTermDecoded !== "") {
    searchInput.value = searchTermDecoded;
  }

  // Put the focus on the search form
  searchInput.focus();
}

// Mark the Regex checkbox if the query is a regex query
var regexCheckbox = document.getElementById('custom-regex');
if (regexCheckbox && useRegex === 'true') {
  regexCheckbox.checked = true;
}

// Mark the allHits checkbox if the query is an allHits query
var allHitsCheckbox = document.getElementById('custom-all-hits');
if (allHitsCheckbox && allHits === 'true') {
  allHitsCheckbox.checked = true;
}

// Mark the topHits checkbox if the query is an allHits query
var topHitsCheckbox = document.getElementById('custom-top-hits');
if (topHitsCheckbox && topHits === 'true') {
  topHitsCheckbox.checked = true;
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
else if (currentPageUrl.includes("custom_search")){
	if(topHits === 'true') {
    console.log("top hits is true: displaying top hits")
		fetchAndDisplayTopHitsResults();
	}
  console.log("displaying all results")
	fetchAndDisplayResults();
}

// --------------------------------------------------------------
// RELOAD PAGE (Called when something changes)
// --------------------------------------------------------------
// builds a url from the value in the search form and the options selected, 
// then navigates to the url
function reloadPage() {
  var pathPrefix = isAppsSite ? "/bApps" : "";
  var searchInput = encodeURIComponent(document.getElementById('custom-search-input').value);
  var regexChecked = document.getElementById('custom-regex').checked;
  var allHitsChecked = document.getElementById('custom-all-hits').checked;
  var topHitsChecked = document.getElementById('custom-top-hits').checked;

  var url = `${pathPrefix}/schemas/custom_search?q=${searchInput}&r=${regexChecked}&a=${allHitsChecked}&t=${topHitsChecked}`;

  loadPage(url);
}

// --------------------------------------------------------------
// LISTENERS
// --------------------------------------------------------------
var searchForm = document.getElementById('custom-search-form');

if (searchForm) {
	// Add the listener to the search form
	document.getElementById('custom-search-form').addEventListener('submit', function (e) {
		e.preventDefault();
		reloadPage();
	});
}

// --------------------------------------------------------------
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
// Gets the top hits and displays them
function fetchAndDisplayTopHitsResults() {
  topHitsResults = getTopHitsResults(query, isAppsSite); // Function in menu.js	
	displayTopHitsResults(topHitsResults, topHitsContainer);
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

			const onlyHeadingHits = findHeadingsWithQuery(String(pages[results[i].topic].headings).toLowerCase(), query);
      const headingsHighlight = insertHighlightAll(onlyHeadingHits, query);
			const hitHeadings = `<p style="margin-bottom: 0px; margin-top: 0px"><b>Headings: </b>${headingsHighlight}</p>`;

      const imageStrings = extractImageValues(JSON.stringify(pages[results[i].topic].images).toLowerCase())
      const imageHits = findHeadingsWithQuery(imageStrings, query)
      const imageHightlight = insertHighlightAll(imageHits, query)
      const hitImages = `<p style="margin-bottom: 0px; margin-top: 0px"><b>Images: </b>${imageHightlight}</p>`;

      const descriptionHighlight = insertHighlightAll(String(pages[results[i].topic].description).toLowerCase(), query);
			const hitDescription = `<p style="margin-bottom: 0px; margin-top: 0px"><b>Description: </b>${descriptionHighlight}</p>`;
			
			resultItem.innerHTML = `
				${titleLink}
				${hitURL}
				${hitKeywords}
        ${hitHeadings}
        ${hitImages}
				${hitDescription}
				`;

		container.appendChild(resultItem);
		}
	}
	
}

// --------------------------------------------------------------
// Gets the search hits and displays them
function fetchAndDisplayResults() {
	var searchIndexPath;
	if(isAppsSite) {
		searchIndexPath = '../../search_index_financials.json'
	}
	else {
		searchIndexPath = '../search_index.json'
	}
  fetch(searchIndexPath)
    .then(response => response.json())
    .then(searchIndex => {

      if(useRegex === 'true') {
        results = searchRegex(query, searchIndex); // Gets the results with a Regex search
      }
      else {
        results = search(query, searchIndex); // Gets the results with a standard search
      }
	  sortResults(results);
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
      const myCurrentTab = findTheTabForThisPage(result.url).toUpperCase()
      // const currentTab = `<p style="margin-bottom: 0px; margin-top: 3px; display: inline-block;">&lt;${myCurrentTab}&gt; </p>`;
      const titleLink = `<h5 style="margin-bottom: 0px; margin-top: 3px; display: inline-block;"><a href="${result.url}" target="_blank">${myCurrentTab} : ${result.title}</a></h5>`;
      const occurrencesContent = `<p style="margin-bottom: 0px; margin-top: 3px; font-size: 12px; display: inline-block; padding-left: 10px;">(Occurrences: ${result.occurrences})</p>`;

      // const titleLink = `<h5 style="margin-bottom: 0px; margin-top: 3px; display: inline-block;"><a href="${myCurrentTab}" target="_blank">${myCurrentTab} : ${result.title}</a></h5>`;
      // const occurrencesContent = `<p style="margin-bottom: 0px; margin-top: 3px; font-size: 12px; display: inline-block; padding-left: 10px;">(Occurrences: ${result.occurrences})</p>`;

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
        <div style="margin-bottom: 0px;">
          ${titleLink} ${occurrencesContent}
        </div>
        <p>&emsp;${snippetContent}</p>
      `;

      container.appendChild(resultItem);
    });
  }
}

// --------------------------------------------------------------
// FUNCTIONS (SEARCH)
// --------------------------------------------------------------
// Searches through all pages for the query
function search(query, index) {
  // Map over each page in the index array
  return index.map(page => {
    // Convert the content of the current page to lowercase
    const lowercaseContent = page.content.toLowerCase();

    // Count the occurrences of the query within the lowercase content
    const occurrences = countOccurrences(lowercaseContent, query);

    // Return an object representing the page with the added 'occurrences' property
    return {
      ...page, // Spread operator to include all existing properties of the page
      occurrences: occurrences // Add a new property 'occurrences' with the count of query occurrences
    };
  })
  // Filter out pages with no occurrences of the query
  .filter(page => page.occurrences > 0);
}

// --------------------------------------------------------------
// Searches through all pages for the query (with regex)
function searchRegex(query, searchIndex) {
  // Create a regular expression object with 'query' as the pattern
  // 'ig' flags: 'i' for case-insensitive search, 'g' for global search
  const regex = new RegExp(query, 'ig');

  // Map over each item in the search index array
  return searchIndex.map(item => {
    // Use the regular expression to find all matches in the content of the current item
    const matches = item.content.match(regex);
    
    // Count the number of matches found, or set to 0 if no matches were found
    const occurrences = matches ? matches.length : 0;

    // Return an object representing the item with the added 'occurrences' property
    return {
      ...item, // Spread operator to include all existing properties of the item
      occurrences: occurrences // Add a new property 'occurrences' with the count of query occurrences
    };
  })
  // Filter out items with no occurrences of the query
  .filter(item => item.occurrences > 0);
}
// --------------------------------------------------------------
// FUNCTIONS (SORT)
// --------------------------------------------------------------
function sortResults(results) {
  // Sort results by occurrences in descending order
  results.sort((a, b) => b.occurrences - a.occurrences);
}

// --------------------------------------------------------------
// FUNCTIONS (SNIPPETS)
// --------------------------------------------------------------
// Gets the snippet for a regex search
function getSnippetRegex(content, query) {
  // Create a regular expression object with 'query' as the pattern
  // Wrap 'query' in parentheses to capture it as a group
  // 'ig' flags: 'i' for case-insensitive search, 'g' for global search
  const regex = new RegExp(`(${query})`, 'ig');
  
  // Execute the regular expression on the content to find the first match
  const match = regex.exec(content);

  // If a match is found
  if (match) {
    // Calculate the start and end positions of the snippet
    const start = Math.max(0, match.index - snippetBefore);
    const end = Math.min(content.length, match.index + match[0].length + snippetAfter);
    
    // Extract the snippet from the content based on the calculated start and end positions
    const snippet = content.substring(start, end);

    // Highlight the matched part of the snippet with a yellow background
    const highlightedSnippet = snippet.replace(new RegExp(query, 'ig'), match => `<span style="background-color: yellow;">${match}</span>`);

    // Return the highlighted snippet with ellipses on both ends
    return `&emsp;...${highlightedSnippet}...`;
  } else {
    // If no match is found, return a portion of the content with ellipses
    return content.substring(0, snippetBefore + snippetAfter) + '...';
  }
}

// --------------------------------------------------------------
// Gets the snippet for an all hits regex search
function getSnippetRegexAll(content, query) {
  // Create a regular expression object with 'query' as the pattern
  // Wrap 'query' in parentheses to capture it as a group
  // 'ig' flags: 'i' for case-insensitive search, 'g' for global search
  const regex = new RegExp(`(${query})`, 'ig');
  
  let match; // Declare a variable to store each match
  let snippets = []; // Declare an array to store snippets
  
  // Iterate through all matches found in the content using a while loop
  while ((match = regex.exec(content)) !== null) {
    // Calculate the start and end positions of the current snippet
    const start = Math.max(0, match.index - snippetBefore);
    const end = Math.min(content.length, match.index + match[0].length + snippetAfter);
    
    // Extract the current snippet from the content based on the calculated start and end positions
    const currentSnippet = content.substring(start, end);

    // Highlight the matched part of the snippet with a yellow background
    const highlightedSnippet = insertHighlight(currentSnippet, match.index - start, match[0].length);

    // Add the highlighted snippet to the snippets array with ellipses on both ends
    snippets.push(`&emsp;...${highlightedSnippet}...`);
  }

  // If there are no matches, return a portion of the original content with ellipses
  if (snippets.length === 0) {
    return content.substring(0, snippetBefore + snippetAfter) + '...';
  }

  // Join the snippets with newline characters and return as a single string
  return snippets.join('<br>');
}

// --------------------------------------------------------------
// Gets the snippet for a search
function getSnippet(content, query) {
  // Find the index of the first occurrence of the query in the content (case-insensitive)
  const index = content.toLowerCase().indexOf(query);

  // If the query is found within the content
  if (index !== -1) {
    // Calculate the start and end positions of the snippet
    const start = Math.max(0, index - snippetBefore); // index of the start of the snippet
    const end = Math.min(content.length, index + snippetAfter); // index of the end of the snippet
    
    // Extract the snippet from the content based on the calculated start and end positions
    const snippet = content.substring(start, end);

    // Highlight the matched part of the snippet with a yellow background
    const highlightedSnippet = snippet.replace(new RegExp(escapeString(query), 'ig'), match => `<span style="background-color: yellow;">${match}</span>`);

    // Return the highlighted snippet with ellipses on both ends
    return `&emsp;...${highlightedSnippet}...`;
  } else {
    // If query not found, return a portion of the beginning of the content with ellipses
    return content.substring(0, snippetBefore + snippetAfter) + '...';
  }
}

// --------------------------------------------------------------
// Gets the snippet for an all hits search
function getSnippetAll(content, query) {
  // Create a regular expression object with 'query' as the pattern
  // 'ig' flags: 'i' for case-insensitive search, 'g' for global search
  const regex = new RegExp(escapeString(query), 'ig');
  let match; // Declare a variable to store each match
  let snippets = []; // Declare an array to store snippets

  // Iterate through all matches found in the content using a while loop
  while ((match = regex.exec(content)) !== null) {
    // Calculate the start and end positions of the current snippet
    const start = Math.max(0, match.index - snippetBefore);
    const end = Math.min(content.length, match.index + match[0].length + snippetAfter);
    
    // Extract the current snippet from the content based on the calculated start and end positions
    const snippet = content.substring(start, end);

    // Wrap the matched query in a span with a yellow background
    const highlightedSnippet = insertHighlight(snippet, match.index - start, match[0].length);

    // Add the highlighted snippet to the snippets array with ellipses on both ends
    snippets.push(`&emsp;...${highlightedSnippet}...`);
  }

  // If there are no matches, return a portion of the beginning of the content with ellipses
  if (snippets.length === 0) {
    return content.substring(0, snippetBefore + snippetAfter) + '...';
  }

  // Remove the leading whitespace from the first snippet
  snippets[0] = snippets[0].replace(/^&emsp;/, '');

  // Join the snippets with newline characters and return as a single string
  return snippets.join('<br>');
}

// --------------------------------------------------------------
// FUNCTIONS (OTHER)
// --------------------------------------------------------------
// Extracts the values of the image json in the meta-data front matter of the md files
function extractImageValues(imagesString) {
  // Parse the JSON string 'imagesString' into an array of objects or an empty array if 'imagesString' is empty or undefined
  const images = JSON.parse(imagesString || '[]');

  // Declare an empty array to store the extracted values
  const values = [];

  // Iterate over each image object in the 'images' array
  images.forEach(image => {
    // Destructure the properties of the image object with default values
    const { file, type, site, cat, sub, report, ribbon, config } = image;

    // Construct a comma-separated string of image values, using empty string as default for missing properties
    values.push(`${file || ''},${type || ''},${site || ''},${cat || ''},${sub || ''},${report || ''},${ribbon || ''},${config || ''}`);
  });

  // Join the array of values with newline characters and return as a single string
  return values.join('\n');
}

// --------------------------------------------------------------
// Returns only the list of headings that the query is found in
// If query is not found in any heading, returns the first 3 headings
// Return is a comma separated list
function findHeadingsWithQuery(headingsString, query) {
  const headings = headingsString.split(',').map(heading => heading.trim());
  const matchedHeadings = [];

  for (let heading of headings) {
    if (heading.toLowerCase().includes(query)) {
      matchedHeadings.push(heading);
    }
  }

  if (matchedHeadings.length === 0) {
    return headings.slice(0, 3).join(', ');
  } else {
    return matchedHeadings.join(', ');
  }
}

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
// Converts the string by escaping invalid url characters
function escapeString(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

// --------------------------------------------------------------
// Returns true if the string is a valid regex expression
function isValidRegex(str) {
  try {
    new RegExp(str);
    return true;
  } catch (e) {
    return false;
  }
}

// --------------------------------------------------------------
// Gets a percentage rating of relevancy based on the score compared to the top score
function getRelevancy(score, topScore) {
	if(score === topScore) {
		return 100
	}
	const result = Math.ceil((score / topScore) * 100);
	return result.toString()
}

// --------------------------------------------------------------
// Returns the number of times the query appears in the content
function countOccurrences(content, query) {
  const lowercaseContent = content.toLowerCase();
  const occurrences = lowercaseContent.split(query.toLowerCase()).length - 1;
  return occurrences;
}

