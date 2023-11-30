var searchInput = document.getElementById('search-input');
var resultsContainer = document.getElementById('search-results');

searchInput.addEventListener('input', function () {
  
});

searchInput.addEventListener('keydown', function (event) {
  if (event.key === 'Enter') {
    performSearch();
  }
});

function performSearch() {
  var query = searchInput.value.toLowerCase();
  resultsContainer.innerHTML = '';

  if (query.length < 2) return;

  alert("you entered: " + searchInput.value)

  // Fetch the search data directly from the JSON file in the root folder
  fetch('../search_index.json') // Update the file path here
    .then(response => response.json())
    .then(data => {
      var results = data.filter(function (item) {
        return (
          item.title.toLowerCase().includes(query) ||
          item.content.toLowerCase().includes(query)
        );
      });

      alert("results = " + results.length)
      
      if (results.length === 0) {
        alert("results is 0")
        resultsContainer.innerHTML = '<p>No results found.</p>';
        return;
     }

      results.forEach(function (result) {
        var li = document.createElement('li');
        var a = document.createElement('a');
        a.href = result.url;
        a.textContent = result.title;
        li.appendChild(a);
        resultsContainer.appendChild(li);
      });
    })
    .catch(error => console.error('Error fetching search data:', error));
}
