# Print a message indicating the script is running
puts "Setting hook: extract_metadata"

# Register a Jekyll hook for the `:post_write` event
Jekyll::Hooks.register :site, :post_write do |site|
  puts "Extracting metadata..."

  # Path to the Python script
  python_script_path = File.join('_python', 'extraction', 'extract_all.py')

  # puts "python_script_path = " + python_script_path

  # Execute the Python script
  success = system("python #{python_script_path}")
#   success = exec("python ")

  # Check if the Python script ran successfully
  if success
    puts "Metadata extraction completed successfully."
  else
    puts "Metadata extraction failed."
    # Optionally raise an error to halt further execution
    raise "Python script failed to execute."
  end
end
