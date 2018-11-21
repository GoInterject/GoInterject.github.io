

/* opens a image into a zoomed view for ease of viewing */
function zoom_img(x){
    // Get the modal
    var modal = document.getElementById('modal-main');
    var modalImg = document.getElementById("modal-img");

    console.log(x.src);
    // Get the image and insert it inside the modal 
    modal.style.display = "block";
    modalImg.src = x.src;

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close-modal")[0];

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() { 
        modal.style.display = "none";
    }
  }
