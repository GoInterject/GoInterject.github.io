
$(document).ready(function(){    
    /* 
    Expands and collapses sections for streamlining documentation upon clicking the expand/collapse event button.
	The "collapsible-expanded" class is expanded by default
    */
    var collapse = document.getElementsByClassName("collapsible-expanded");
    var i;

    for (i = 0; i < collapse.length; i++) {
		var collapsible = collapse[i];
		var panel = collapsible.parentNode;
		
		panel.style.maxHeight = "100%";
		
		collapsible.addEventListener("click", function() {
            // toggle between adding and removing active so color changes when hovering over button.
            this.classList.toggle("clicked-expanded");
            
            // Toggle between hiding and showing text in the panel div
            while (panel) {
                if (panel.classList.contains('panel-expanded') ) {
                    // if panel is open, close. else open to max height
                    if (panel.style.maxHeight){
                        panel.style.maxHeight = null;
                    } else {
                        panel.style.maxHeight = panel.scrollHeight + "px";
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