/*
This script is for expanding and collapsing buttons/sections
These classes are expanded by default
*/
$(document).ready(function(){	
	/* 
	Expands and collapses sections for streamlining documentation upon clicking the expand/collapse event button.
	The "collapsible-expanded" and "panel-expanded" classes are expanded by default
	*/
	var collapse = document.getElementsByClassName("collapsible-expanded");
	var i;

	for (i = 0; i < collapse.length; i++) {
		collapse[i].addEventListener("click", function() {
			// toggle between adding and removing active so color changes when hovering over button.
			this.classList.toggle("clicked-expanded");
			
            // Toggle between hiding and showing text in the panel div
			var panel = this.parentNode;
			while (panel) {
				if (panel.classList.contains('panel-expanded') ) {
					// If panel is at 0, then expand it
					if (panel.style.maxHeight === "0px"){
						panel.style.maxHeight = panel.scrollHeight + "px";
					}
					// Panel is at max so collapse it
					else {
						panel.style.maxHeight = "0px";
					}
					// Once panel is found and acted on, break loop.
					break;
				}
				// go to next sibling and restart loop
				panel = panel.nextElementSibling;
			}
		});
	
	}
	
});