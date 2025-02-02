// ==============================================================
// TOP LEVEL VARIABLES
// ==============================================================
// Right nav highlighting
var sidebarObj = (document.getElementsByClassName("sidebar")[0]) ? document.getElementsByClassName("sidebar")[0] : document.getElementsByClassName("sidebar-home")[0]
var sidebarBottom = sidebarObj.getBoundingClientRect().bottom;
var footerTop = document.getElementsByClassName("footer")[0].getBoundingClientRect().top;
var headerOffset = document.getElementsByClassName("container-fluid")[0].getBoundingClientRect().bottom;

// ensure that the left nav visibly displays the current topic
var current = document.getElementsByClassName("active currentPage");
var body = document.getElementsByClassName("col-content content");

var outputHorzTabs = new Array();
var outputLetNav = new Array();
var totalTopics = 0;
var currentSection;
var sectionToHighlight;

var currentHeading = "";

// ==============================================================
// SCRIPT
// ==============================================================
// --------------------------------------------------------------
// RIGHT SIDE BAR
// --------------------------------------------------------------
if (current[0]) {
    if (sidebarObj) {
      current[0].scrollIntoView(true);
      body[0].scrollIntoView(true);
    }
    // library hack
    if (document.location.pathname.indexOf("/samples/") > -1){
      $(".currentPage").closest("ul").addClass("in");
    }
  }

$(window).scroll(function(){
  var headingPositions = new Array();
  $("h1, h2, h3, h4, h5, h6").each(function(){
    if (this.id == "") this.id="title";
    headingPositions[this.id]=this.getBoundingClientRect().top;
  });
  headingPositions.sort();
  // the headings have all been grabbed and sorted in order of their scroll
  // position (from the top of the page). First one is toppermost.
  for(var key in headingPositions)
  {
    if (headingPositions[key] > 0 && headingPositions[key] < 200)
    {
      if (currentHeading != key)
      {
        // a new heading has scrolled to within 200px of the top of the page.
        // highlight the right-nav entry and de-highlight the others.
        highlightRightNav(key);
        currentHeading = key;
      }
      break;
    }
  }
});

// --------------------------------------------------------------
// TOGGLE MENU
// --------------------------------------------------------------
$("#menu-toggle").click(function(e) {
        e.preventDefault();
        $(".wrapper").toggleClass("right-open");
        $(".col-toc").toggleClass("col-toc-hidden");
    });
$("#menu-toggle-left").click(function(e) {
        e.preventDefault();
        $(".col-nav").toggleClass("col-toc-hidden");
    });
$(".navbar-toggle").click(function(){
  $("#sidebar-nav").each(function(){
    $(this).toggleClass("hidden-sm");
    $(this).toggleClass("hidden-xs");
  });
});

var navHeight = $('.navbar').outerHeight(true) + 80;

$(document.body).scrollspy({
	target: '#leftCol',
	offset: navHeight
});

$(document).ready(function(){
  // Add smooth scrolling to all links
  // $( ".toc-nav a" ).addClass( "active" );
  $(".toc-nav a").on('click', function(event) {
    // $(this).addClass('active');
    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;
      loadHash(hash);

      // Add hash (#) to URL when done scrolling (default click behavior)
      window.location.hash = hash;

    } // End if
  });
  if (window.location.hash) loadHash(window.location.hash);
});

$(document).ready(function(){
  $(".sidebar").Stickyfill();

  // Add smooth scrolling to all links
  $(".nav-sidebar ul li a").on('click', function(event) {

    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top-80
      }, 800, function(){

        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });
});

// Make dropdown show on hover
$('ul.nav li.dropdown').hover(function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn(500);
}, function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut(500);
});

// Temp hack for side menu
$('.nav-sidebar ul li a').click(function() {
    $(this).addClass('collapse').siblings().toggleClass('in');
});

if($('.nav-sidebar ul a.active').length != 0)
{
  $('.nav-sidebar ul').click(function() {
      $(this).addClass('collapse in').siblings;
  });
}

// --------------------------------------------------------------
// COMPONENTS
// --------------------------------------------------------------
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

// Enable glossary link popovers
$('.glossLink').popover();

// sync tabs with the same data-group
window.onload = function() {
  $('.nav-tabs > li > a').click(function(e) {
    var group = $(this).attr('data-group');
    $('.nav-tabs > li > a[data-group="'+ group +'"]').tab('show');
  })
  $('.ctrl-right .btn-group').css("visibility","visible");
};

// ==============================================================
// FUNCTIONS
// ==============================================================
function addMyClass(classToAdd) {
  var classString = this.className; // returns the string of all the classes for myDiv
   // Adds the class "main__section" to the string (notice the leading space)
  this.className = newClass; // sets className to the new string
}

// --------------------------------------------------------------
// RIGHT SIDE BAR
// --------------------------------------------------------------
// Highlights the heading in the right side bar that the current scroll 
// position is on in the document page
function highlightRightNav(heading)
{
  if (document.location.pathname.indexOf("/glossary/")<0){
    if (heading == "title")
    {
      history.replaceState({},"Top of page on " + document.location.pathname,document.location.protocol +"//"+ document.location.hostname + (location.port ? ':'+location.port: '') + document.location.pathname);
      $("#my_toc a").each(function(){
        $(this).removeClass("active");
      });
      $("#sidebar-wrapper").animate({
        scrollTop: 0
      },800);
    } else {
      var targetAnchorHREF = document.location.protocol +"//"+ document.location.hostname + (location.port ? ':'+location.port: '') + document.location.pathname + "#" + heading;
      // make sure we aren't filtering out that heading level
      var noFilterFound = false;
      $("#my_toc a").each(function(){
        if (this.href==targetAnchorHREF) {
          noFilterFound = true;
        }
      });
      // now, highlight that heading
      if (noFilterFound)
      {
        $("#my_toc a").each(function(){
          //console.log("right-nav",this.href);
          if (this.href==targetAnchorHREF)
          {
            history.replaceState({},this.innerText,targetAnchorHREF);
            $(this).addClass("active");
            var sidebarOffset = (sidebarBottom > 200) ? 200 : headerOffset - 20;
            $("#sidebar-wrapper").animate({
              scrollTop: $("#sidebar-wrapper").scrollTop() + $(this).position().top - sidebarOffset
            },100);
            //document.getElementById("sidebar-wrapper").scrollTop = this.getBoundingClientRect().top - 200;
          } else {
            $(this).removeClass("active");
          }
        });
      }
    }
  }
}

// --------------------------------------------------------------
  // Using jQuery's animate() method to add smooth page scroll
  function loadHash(hashObj)
{
  // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
  $('html, body').animate({
    scrollTop: $(hashObj).offset().top-80
  }, 800);
}

// --------------------------------------------------------------
// TAB DISPLAYED IN CUSTOM SEARCH
// --------------------------------------------------------------
// Traverses through all the table of content files looking for the tab 
// that the page is contained in
// The docstoc variables are declared in toc.js
function findTheTabForThisPage(page) {
  var foundThisTab = ""
  foundThisTab = findTheTabInThisNode(docstocMain, page)
  if (foundThisTab !== "") {
    return foundThisTab
  }
  foundThisTab = findTheTabInThisNode(docstocFinancials, page)
  if (foundThisTab !== "") {
    return foundThisTab
  }
  foundThisTab = findTheTabInThisNode(docstocTraining, page)
  if (foundThisTab !== "") {
    return foundThisTab
  }
  foundThisTab = findTheTabInThisNode(docstocWIP, page)
  if (foundThisTab !== "") {
    return foundThisTab
  }
return foundThisTab
}

// --------------------------------------------------------------
// Traverses this tree/branch looking for the page, returns the tab it is found in
function findTheTabInThisTree(tree, page, currentTab) {
  // Recursive function
  function processBranch(branch){
    // check sub pages in section
    for (var k=0;k<branch.length;k++){
  
      // first check branch itself <NOTE> we need to do this because our header sections are links
      if (branch[k].path == page && !branch[k].nosync){
        foundTab = currentTab
        break;
      }
  
      if (branch[k].path == page && !branch[k].nosync){
        foundTab = currentTab
        break;
      }  else {
        // else recurse through branch
        if (branch[k].section) {
          processBranch(branch[k].section);
        } 
      }
      
    }
  }
    var foundTab = ""
    processBranch(tree);
  
    return foundTab;
}

// --------------------------------------------------------------
// Traverses the root node of this toc looking for the page, returns the tab it is found in
function findTheTabInThisNode(rootnode, page){
  var myTab = ""

  for (i=0;i<rootnode.horizontalnav.length;i++)
  {
    // console.log("i = " + i)
    if (rootnode.horizontalnav[i].node != "glossary")
    {
      myTab = findTheTabInThisTree(rootnode[rootnode.horizontalnav[i].node], page, rootnode.horizontalnav[i].title);
      if (myTab !== "") {
        return myTab
      }
    }

  }
  return myTab
}

// --------------------------------------------------------------
// LEFT NAVIGATION MENU
// --------------------------------------------------------------
// Handles click action of a navigation item
function navClicked(sourceLink)
{
  var classString = document.getElementById('#item' + sourceLink).className;
  if (classString.indexOf(' in') > -1)
  {
    //collapse
    var newClass = classString.replace(' in','');
    document.getElementById('#item' + sourceLink).className = newClass;
  } else {
    //expand
    var newClass = classString.concat(' in');
    document.getElementById('#item' + sourceLink).className = newClass;
  }
}

// --------------------------------------------------------------
// Traverses the toc tree looking for the current item
function findMyTopic(tree){
  // Recursive function
  function processBranch(branch){

    // check sub pages in section
    for (var k=0;k<branch.length;k++){
  
      // first check branch itself <NOTE> we need to do this because our header sections are links
      if (branch[k].path == pageURL && !branch[k].nosync){
        thisIsIt = true;
        sectionToHighlight = currentSection;
        break;
      }
  
      if (branch[k].path == pageURL && !branch[k].nosync){
        // console.log(branch[k].path + ' was == ' + pageURL)
        thisIsIt = true;
        break;
      }  else {
        // else recurse through branch
        if (branch[k].section) {
          processBranch(branch[k].section);
        } 
      }
      
    }
  }

  var thisIsIt = false;

  processBranch(tree);

  return thisIsIt;
}

// --------------------------------------------------------------
// Walks through the toc json tree and builds a html toc contents
function walkTree(tree)
{
  for (var j=0;j<tree.length;j++)
  {
    totalTopics++;
    if (tree[j].section)
    {
        // Added parallel statements to build separate anchors for caret vs title for each section before appending them to output
        // One thing I noticed is that the "collapsed" class is set on build, but not altered during the navclick() operation
        // -TWS

        var sectionHasPath = findMyTopic(tree[j].section);

        if (tree[j].path && tree[j].path == pageURL){
          sectionHasPath = true;
        }

        var tempTitleNav = new Array();
        var tempCaretNav = new Array();

        outputLetNav.push('<li style="overflow-wrap: break-word; overflow:hidden;">');
        tempCaretNav.push('<a onclick="navClicked(' + totalTopics + ')" data-target="#item' + totalTopics + '" data-toggle="collapse" data-parent="#stacked-menu" style="float:right;"');
        
        // check if the page has a defined link
        //console.log('tree path:  ' + tree[j].path);
        if (tree[j].path != undefined){
          tempTitleNav.push('<a href="' + tree[j].path + '" style="float:left;width:60%;word-wrap: break-word;"');
        }
        else {
          tempTitleNav.push('<a style="float:left;width:60%;word-wrap: break-word;"');
        }

      if (sectionHasPath){
          tempCaretNav.push('aria-expanded="true"');
          tempTitleNav.push('class="nocaret active currentPage" aria-expanded="true"');
      } else {
          tempCaretNav.push('class="collapsed" aria-expanded="false"');
          tempTitleNav.push('class="nocaret" aria-expanded="false"');
      }
      tempCaretNav.push('><span class="caret arrow"></span></a>');
      tempTitleNav.push('>' + tree[j].sectiontitle + '</a><br style="clear:both;">');

      outputLetNav.push(tempCaretNav.join(''));
      outputLetNav.push(tempTitleNav.join(''));

      outputLetNav.push('<ul class="nav collapse');
      if (sectionHasPath) {
        outputLetNav.push(' in');
      }
      outputLetNav.push('" id="#item' + totalTopics + '" aria-expanded="');
      if (sectionHasPath){
        outputLetNav.push('true');
      } else {
        outputLetNav.push('false');
      }
      outputLetNav.push('">');
      var subTree = tree[j].section;
      walkTree(subTree);
      outputLetNav.push('</ul></li>');
    } else if (tree[j].generateTOC) {
      // auto-generate a TOC from a collection
      walkTree(collectionsTOC[tree[j].generateTOC]);
    } else {
      
      // just a regular old topic; this is a leaf, not a branch; render a link!
      outputLetNav.push('<li><a href="' + tree[j].path + '"');
      if (tree[j].path == pageURL && !tree[j].nosync)
      {
        sectionToHighlight = currentSection;
        outputLetNav.push('class="active currentPage nocaret" aria-expanded="true"');
      } else {
        outputLetNav.push('class="nocaret"');
      }
      outputLetNav.push('>'+tree[j].title+'</a></li>');
    }
  }
}

// --------------------------------------------------------------
// Builds the left side vertical navigation toc and the 
// top horizontal navigation for the page
function renderNav(docstoc) {
  for (i=0;i<docstoc.horizontalnav.length;i++)
  {
    if (docstoc.horizontalnav[i].node != "glossary")
    {
      currentSection = docstoc.horizontalnav[i].node;
      // Build vertical navigation
      var itsHere = findMyTopic(docstoc[docstoc.horizontalnav[i].node]);
      if (itsHere || docstoc.horizontalnav[i].path == pageURL)
      {
        walkTree(docstoc[docstoc.horizontalnav[i].node]);
      }
    }
    // Build Horizontal navigation
    outputHorzTabs.push('<li id="' + docstoc.horizontalnav[i].node + '"');
    if (docstoc.horizontalnav[i].path==pageURL || docstoc.horizontalnav[i].node==sectionToHighlight)
    {
      outputHorzTabs.push(' class="active"');
    }
    outputHorzTabs.push('><a href="'+docstoc.horizontalnav[i].path+'">'+docstoc.horizontalnav[i].title+'</a></li>\n');
  }
  if (outputLetNav.length==0)
  {
    // Didn't find the current topic in the standard TOC; maybe it's a collection;
    for (var key in collectionsTOC)
    {
      var itsHere = findMyTopic(collectionsTOC[key]);
      if (itsHere) {
        walkTree(collectionsTOC[key]);
        break;
      }
    }
    // either glossary was true or no left nav has been built; default to glossary
    // show pages tagged with term and highlight term in left nav if applicable
    renderTagsPage();
    for (var i=0;i<glossary.length;i++){
      var highlightGloss = '';
      if (tagToLookup) highlightGloss = (glossary[i].term.toLowerCase()==tagToLookup.toLowerCase()) ? ' class="active currentPage"' : '';
      outputLetNav.push('<li><a'+highlightGloss+' href="/glossary/?term=' + glossary[i].term + '">'+glossary[i].term+'</a></li>');
    }
  }
  document.getElementById('jsTOCHorizontal').innerHTML = outputHorzTabs.join('');
  document.getElementById('jsTOCLeftNav').innerHTML = outputLetNav.join('');
}

// --------------------------------------------------------------
// COOKIES
// --------------------------------------------------------------
// This function creates a new cookie with the specified name, value, and expiration days.
function createCookie(name, value, days) {
  var expires = "";
  if (days) {
      var date = new Date();
      date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
      expires = "; expires=" + date.toUTCString();
  }
  // Set the cookie with the provided name, value, expiration, and path
  document.cookie = name + "=" + value + expires + "; path=/";
}

// --------------------------------------------------------------
// This function reads the value of the cookie with the specified name.
function readCookie(name) {
  var nameEQ = name + "=";
  var ca = document.cookie.split(';');
  for (var i = 0; i < ca.length; i++) {
      var c = ca[i];
      // Trim any leading whitespace from the cookie string
      while (c.charAt(0) == ' ') c = c.substring(1, c.length);
      // If the cookie name matches, return the cookie value
      if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
  }
  // If the cookie is not found, return null
  return null;
}

// --------------------------------------------------------------
// This function erases (deletes) the cookie with the specified name.
function eraseCookie(name) {
  // Call createCookie function with an expiration date in the past to delete the cookie
  createCookie(name, "", -1);
}
