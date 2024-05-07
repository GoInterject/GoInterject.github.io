/*
This code sets up an event handler to open images in a zoomed view when they are clicked. 
*/
$(document).ready(function(){

    /* opens a image into a zoomed view for ease of viewing */
    $('img').click(function() {
        // get current img
        var thisImg = $(this);
            // ensure that this is not the logo image
            if (!$(thisImg).hasClass('logo')) {
        
            // Get the modal
            var modal = document.getElementById('modal-main');
            var modalImg = document.getElementById("modal-img");
            
            // Get the image and insert it inside the modal 
            modal.style.display = "block";
            modalImg.src = thisImg.attr('src');
            
            // When the user clicks on the modal then close the modal
            modal.onclick = function() {
                modal.style.display = "none";
            }
        };
    });
});

