var metadata, glossary;
var autoCompleteShowing = false;
var displayingAutcompleteResults = new Array();
var autoCompleteShowingID = 0;
var lastSearch = "";
var autoCompleteResultLimit = 3;
var results = new Array();
var scoreForTitleMatch = 10;
var scoreForURLMatch = 5;
var scoreForKeywordHEAVYMatch = 5   // weight for 1st three keywords
var scoreForKeywordDEFAULTMatch = 3 // weight for rest of keywords
var scoreForHeadingsMatch = 2
var scoreForImagesMatch = 1
var scoreForDescriptionMatch = 1

var isAppsSite = false;

if (window.location.href.indexOf("bApps") !== -1) {
	isAppsSite = true;
}

function addResult(topic, results, matchesTitle, matchesDescription, matchesURL, matchesKeywords, matchesTopKeywords, matchesHeadings, matchesImages)
{
  var matchScore = (matchesTitle * scoreForTitleMatch) +
                  (matchesDescription * scoreForDescriptionMatch) +
                  (matchesURL * scoreForURLMatch) +
                  (matchesTopKeywords * scoreForKeywordHEAVYMatch) +
                  (matchesKeywords * scoreForKeywordDEFAULTMatch) +
                  (matchesImages * scoreForImagesMatch) +
                  (matchesHeadings * scoreForHeadingsMatch);
  if (matchScore > 0)
  {
    var resultIndex = results.length;
    results[resultIndex] = new Array();
    results[resultIndex].topic = topic;
    results[resultIndex].score = matchScore;
  }
}
function loadPage(url)
{
  window.location.replace(url);
  window.location.href = url;
}

$(document).on("keypress", function(event) {
    if (event.keyCode == 13) {
      if(autoCompleteShowing) event.preventDefault();
    }
});

function highlightMe(inputTxt,keyword)
{
  inputTxt = String(inputTxt);
  simpletext = new RegExp("(" + keyword + ")","gi");
  return inputTxt.replace(simpletext, "<span>$1</span>")
}
function matches(inputTxt,searchTxt)
{
  var subs = inputTxt.split(searchTxt);
  return subs.length - 1;
}
function hookupTOCEvents()
{
  // do after tree render
  $('.expand-menu').on('click', function(elem) {
//      menu = elem.currentTarget.nextElementSibling
    menu = elem.currentTarget.parentElement
    if (menu.classList.contains("menu-closed")) {
      menu.classList.remove("menu-closed")
      menu.classList.add("menu-open")
    } else {
      menu.classList.add("menu-closed")
      menu.classList.remove("menu-open")
    }
    return false;
  });
  $(".left-off-canvas-menu").css("display","block");
  // console.log(metadata);
  $("#st-search-input").on('keyup change', function(e) {
    e = e || window.event;
    if (autoCompleteShowing)
    {
      if (e.keyCode == '38') {
          // up arrow
          if (autoCompleteShowingID > -1)
          {
            // go up a result
            $("#autoCompleteResult" + autoCompleteShowingID).removeClass("autocompleteSelected");
            autoCompleteShowingID = autoCompleteShowingID - 1;
            $("#autoCompleteResult" + autoCompleteShowingID).addClass("autocompleteSelected");
            $("#autocompleteShowAll").removeClass("autocompleteSelected");
          } else {
            // de-selection auto-complete; reverting to raw search
            $("#autoCompleteResult0").removeClass("autocompleteSelected");
            autoCompleteShowingID = -1;
          }
      } else if (e.keyCode == '40') {
          // down arrow
          if (autoCompleteShowingID < (displayingAutcompleteResults.length - 1))
          {
            // go down to the next result
            $("#autoCompleteResult" + autoCompleteShowingID).removeClass("autocompleteSelected");
            autoCompleteShowingID = autoCompleteShowingID + 1;
            $("#autoCompleteResult" + autoCompleteShowingID).addClass("autocompleteSelected");
          } else {
            // select "See all results..." and go no further
            $("#autoCompleteResult" + autoCompleteShowingID).removeClass("autocompleteSelected");
            $("#autocompleteShowAll").addClass("autocompleteSelected");
            autoCompleteShowingID = autoCompleteResultLimit;
          }
      } else if (e.keyCode == '13') {
        // return key
        e.preventDefault();
        if (autoCompleteShowingID==autoCompleteResultLimit || autoCompleteShowingID == -1 || autoCompleteShowing == false)
        {
          // "see all" is selected or they don't have an autocomplete result selected
          //?q=
          if (isAppsSite) {
			loadPage("/bApps/schemas/custom_search?q=" + $("#st-search-input").val());
		  }
		  else {
			loadPage("/schemas/custom_search?q=" + $("#st-search-input").val());
		  }
        } else {
          // an autocomplete result is selected
          loadPage(pages[displayingAutcompleteResults[autoCompleteShowingID]].url);
        }
      }
      //console.log('autoCompleteShowingID:',autoCompleteShowingID,'displayingAutcompleteResults[id]:',displayingAutcompleteResults[autoCompleteShowingID],'pages[id].url:',pages[displayingAutcompleteResults[autoCompleteShowingID]].url);
    }
    var searchVal = $("#st-search-input").val();
    if (lastSearch != searchVal)
    {
      displayingAutcompleteResults = [];
      results = [];
      var uppercaseSearchVal = searchVal.toUpperCase();
      //console.log("input changed: ",$("#st-search-input").val());

      if (searchVal.length > 2) {
  			results = getTopHitsResults(searchVal, isAppsSite);
	    }
      
	autoCompleteShowingID = -1;
	var resultsShown = 0;
	var resultsOutput = new Array();
	resultsOutput.push("<div id='autoContainer'>")
	//console.log(results);
	for (i=0; i < autoCompleteResultLimit && i < results.length; i++)
	{
	  //console.log(i, "of", autoCompleteResultLimit, "is underway");
	  displayingAutcompleteResults.push(results[i].topic); //log results to global array
	  resultsOutput.push("<div class='autoCompleteResult' id='autoCompleteResult" + i + "' onclick='loadPage(\"" + pages[results[i].topic].url + "\")'>");
	  resultsOutput.push("<ul class='autocompleteList'>");
	  resultsOutput.push("<li id='autoTitle" + i + "' class='autocompleteTitle'>")
	  resultsOutput.push("<a href=" + pages[results[i].topic].url + ">" + highlightMe(pages[results[i].topic].title,searchVal) + "</a>");
	  resultsOutput.push("</li>");
	  resultsOutput.push("<li id='autoUrl" + i + "' class='autocompleteUrl'>")
	  resultsOutput.push(highlightMe(pages[results[i].topic].url,searchVal));
	  resultsOutput.push("</li>");
	  /*
	  resultsOutput.push("<li id='autoBreadcrumb" + i + "' class='autocompleteBreadcrumb'>")
	  resultsOutput.push("Breadcrumb: " + breadcrumbString(pages[results[i]].url));
	  resultsOutput.push("</li>");
	  */
	  if (pages[results[i].topic].keywords)
		  {
		  resultsOutput.push("<li id='autoKeywords" + i + "' class='autocompleteKeywords'>")
		  resultsOutput.push("<b>Keywords</b>: <i>" + highlightMe(pages[results[i].topic].keywords,searchVal) + "</i>");
		  resultsOutput.push("</li>");
		  }
		  
	  // Limit the character length of the description so that the drop down from the search
	  // does not flow to the bottom of the page
	  var descriptionCutString;

		if (pages[results[i].topic].description != null) {
		  descriptionCutString = pages[results[i].topic].description.substring(0, 75) + "...";
		} else {
		  descriptionCutString = "No description available";
		}
	  
	  if (pages[results[i].topic].description)
		  {
		  resultsOutput.push("<li id='autoDescription" + i + "' class='autocompleteDescription'>")
		  resultsOutput.push("<b>Description</b>: " + highlightMe(descriptionCutString,searchVal));
		  resultsOutput.push("</li>");
		  }
	  resultsOutput.push("</ul>");
	  resultsOutput.push("</div>")
	  resultsShown++;
	}
	
	var resultsShownText = (resultsShown > 1) ? resultsShown + " of " + results.length + " docs" : "doc";
	var sitePath = isAppsSite ? '/bApps' : '';
	var resultsOutputText = results.length === 0 ? "No top results" : "Showing top " + resultsShownText;
	var resultsOutputLink = `<a href='${sitePath}/schemas/custom_search?q=${searchVal}'><b>${resultsOutputText}. See all results...</b></a>`;

	resultsOutput.push(`<div id='autocompleteShowAll'><ul class='autocompleteList'><li class='autocompleteTitle' id='autoSeeAll'>${resultsOutputLink}</li></ul></div>`);
	resultsOutput.push("</div>");
	$("#autocompleteResults").css("display","block");
	$("#autocompleteResults").html(resultsOutput.join(""));
	autoCompleteShowing = true;
      
      lastSearch = searchVal;
    } // if searchVal != lastSearch
  });
}

function getTopHitsResults(searchVal, searchingAppSite) {
  var uppercaseSearchVal = searchVal.toUpperCase();
  var topHitsResults = [];

  for (var i = 0; i < pages.length; i++) {
    var thisPage = pages[i];

     var thisPageIsAppsSite = thisPage.url ? thisPage.url.toUpperCase().startsWith("/BAPPS") : false

     // Don't do search if these values are opposite (XOR)
     if (searchingAppSite ^ thisPageIsAppsSite) {
      continue;
    }

    var matchesTitle = thisPage.title ? matches(String(thisPage.title).toUpperCase(), uppercaseSearchVal) : 0;
    var matchesDescription = thisPage.description ? matches(String(thisPage.description).toUpperCase(), uppercaseSearchVal) : 0;
    var matchesURL = thisPage.url ? matches(String(thisPage.url).toUpperCase(), uppercaseSearchVal) : 0;
    var matchesKeywords = thisPage.keywords ? matches(String(thisPage.keywords.slice(2, thisPage.keywords.length)).toUpperCase(), uppercaseSearchVal) : 0;
    var matchesTopKeywords = thisPage.keywords ? matches(String(thisPage.keywords.slice(0, 3)).toUpperCase(), uppercaseSearchVal) : 0;
    var matchesHeadings = thisPage.url ? matches(String(thisPage.headings).toUpperCase(), uppercaseSearchVal) : 0;
    var matchesImages = thisPage.images ? matches(convertImagesObject(thisPage.images).toUpperCase(), uppercaseSearchVal) : 0;

    addResult(i, topHitsResults, matchesTitle, matchesDescription, matchesURL, matchesKeywords, matchesTopKeywords, matchesHeadings, matchesImages);
    }

  topHitsResults.sort(function(a, b) {
    return b.score - a.score;
  });

  return topHitsResults;
}

function convertImagesObject(images) {
  const jsImages = JSON.parse(JSON.stringify(images) || '[]'); // Parse JSON string into an array of objects
  const csvLines = [];

  jsImages.forEach(image => {
    // Convert each image object to a CSV line by stringify it
    csvLines.push(JSON.stringify(image));
  });

  return csvLines.join('\n');
}

function queryString()
{
    var vars = [], hash;
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for(var i = 0; i < hashes.length; i++)
    {
        hash = hashes[i].split('=');
        vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }
    return vars;
}

function renderTopicsByTagTable(tagToLookup,divID)
{
  var matchingPages = new Array();
  for (i=0;i<pages.length;i++)
  {
    thisPage = pages[i];
    if (thisPage.keywords)
    {
      var keywordArray = thisPage.keywords.toString().split(",");
      for (n=0;n<keywordArray.length;n++)
      {
        if (keywordArray[n].trim().toLowerCase()==tagToLookup.toLowerCase())
        {
          matchingPages.push(i); // log the id of the page w/matching keyword
        }
      }
    }
  }
  var pagesOutput = new Array();
  if (matchingPages.length > 0)
  {
    pagesOutput.push("<h2>Pages tagged with: " + tagToLookup + "</h2>");
    pagesOutput.push("<table><thead><tr><td>Page</td><td>Description</td></tr></thead><tbody>");
    for(i=0;i<matchingPages.length;i++) {
      thisPage = pages[matchingPages[i]];
      pagesOutput.push("<tr><td><a href='" + thisPage.url + "'>" + thisPage.title + "</a></td><td>" + thisPage.description + "</td></tr>");
    }
    pagesOutput.push("</tbody></table>");
  }
  $("#" + divID).html(pagesOutput.join(""));
}

var tagToLookup;
function renderTagsPage()
{
  if(window.location.pathname.indexOf("/glossary/")>-1 || window.location.pathname.indexOf("/schemas/custom_search")>-1)
  {
    if (window.location.pathname.indexOf("/glossary/")>-1)
    {
      // Get ?term=<value>
      tagToLookup = decodeURI(queryString().term);
      $("#keyword").html(tagToLookup);
    }
    else
    {
      // Get ?q=<value>
      tagToLookup = decodeURI(queryString().q);
    }
    // Get the term and definition
    for (i=0;i<glossary.length;i++)
    {
      if (glossary[i].term.toLowerCase()==tagToLookup.toLowerCase())
      {
        var glossaryOutput = glossary[i].def;
      }
    }
    if (glossaryOutput) {
      $("#glossaryMatch").html("<h2>Definition of: " + tagToLookup + "</h2>" + glossaryOutput);
    }
    renderTopicsByTagTable(tagToLookup,"topicMatch",true);
  }
}
