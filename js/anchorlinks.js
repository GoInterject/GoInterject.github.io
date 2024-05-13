// This is an Immediately Invoked Function Expression (IIFE) that takes in the document object as a parameter.
(function(d) {
	"use strict"; // Enables strict mode to catch common coding mistakes and "unsafe" actions.

	// Select all H1, H2, and H3 elements within the element with the id "DocumentationText".
	var hs = d.getElementById("DocumentationText").querySelectorAll("H1, H2, H3"), h;

	// Loop through each found heading element.
	for (var i = 0; i < hs.length; i++) {
		h = hs[i];
		// Check if the heading element has an id attribute and it is not empty.
		if (h.id != null && h.id.length > 0) {
			// If the condition is met, insert an anchor link inside the heading element.
			// The anchor link will link to the current page URL followed by the heading's id.
			h.insertAdjacentHTML('beforeend', '<a href="' + window.location.href + '#' + h.id + '" class="anchorLink">¶</a>')
		}
	}

})(document); // Passes the document object to the IIFE.
