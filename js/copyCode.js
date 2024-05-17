/*
This code enhances the user experience on a webpage by adding a "Copy" button 
to each code block displayed on the page. When a user clicks the "Copy" button, 
it automatically copies the content of the associated <code> element (assuming there's one) 
to their clipboard. This feature allows users to easily copy code snippets for later 
use without having to manually select and copy the text.
*/
// Select all <pre> elements in the document
var codeBlocks = document.querySelectorAll('pre');

// Iterate over each <pre> element
codeBlocks.forEach(function (codeBlock) {
  // Create a button element for copying the code
  var copyButton = document.createElement('button');
  copyButton.className = 'copy'; // Set class name for styling
  copyButton.type = 'button'; // Set button type
  copyButton.ariaLabel = 'Copy code to clipboard'; // Set aria label for accessibility
  copyButton.innerText = 'Copy'; // Set button text

  // Append the copy button to the code block
  codeBlock.append(copyButton);

  // Add an event listener to the copy button for click events
  copyButton.addEventListener('click', function () {
    // Get the text content of the <code> element within the code block and trim any leading/trailing whitespace
    var code = codeBlock.querySelector('code').innerText.trim();
    
    // Copy the code to the clipboard using the Clipboard API
    window.navigator.clipboard.writeText(code);

    // Change the button text to 'Copied' to indicate successful copy
    copyButton.innerText = 'Copied';
    
    // Define a timeout to revert the button text back to 'Copy' after 4 seconds
    var fourSeconds = 4000;
    setTimeout(function () {
      copyButton.innerText = 'Copy';
    }, fourSeconds);
  });
});
