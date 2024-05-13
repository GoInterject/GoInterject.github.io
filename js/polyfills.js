/*
This code snippet polyfills the startsWith method for older browsers that do not support 
it natively. The method checks if a string starts with the characters of a specified string, 
returning true or false as appropriate.
 */
// Check if the String prototype does not already have a 'startsWith' method
if (!String.prototype.startsWith) {
    // Define the 'startsWith' method on the String prototype
    Object.defineProperty(String.prototype, 'startsWith', {
        // Set the value of the 'startsWith' method as a function
        value: function(search, pos) {
            // Set the position to start searching from:
            // If 'pos' is not provided or is negative, set it to 0; otherwise, convert it to a number
            pos = !pos || pos < 0 ? 0 : +pos;
            
            // Compare the substring of the string from 'pos' to 'pos + search.length' with the 'search' string
            return this.substring(pos, pos + search.length) === search;
        }
    });
}
