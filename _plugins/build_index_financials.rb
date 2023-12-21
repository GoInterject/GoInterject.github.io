# This script creates and builds a json file that indexes doc pages on the website
# The json file is used for the custom search feature

require 'nokogiri'

puts "Running script build_index_financials"

Jekyll::Hooks.register :site, :post_write do |site|
  puts "Building index search_index_financials.json"

  # Build your index here
    index_finanacials_content = build_index_financials(site)
  
    # Specify the path and filename for the index file
    parent_folder = File.expand_path("..", site.dest)
    index_file_path = File.join(parent_folder, 'search_index_financials.json')
    site_index_file_path = File.join(site.dest, 'search_index_financials.json')
    
    # Write the index content to the file
    File.write(index_file_path, index_finanacials_content)
    File.write(site_index_file_path, index_finanacials_content)
  end
  
  def build_index_financials(site)
    # Build an array of hashes containing relevant data
    index_data = []
  
    # Iterate over all pages on the website
    site.pages.each do |page|

      # Include only documents from specific folders
      next unless finanacials_included_folder?(page)
      
      # Exclude pages from specific folders
      #next if excluded_folder?(page) || !page.url.end_with?('.html') || page.data['title'] == 404

      # Use Nokogiri to strip HTML tags from the content
      stripped_content = Nokogiri::HTML(page.content).text
      
      # Replace '\n' and '\t' characters with spaces
      cleaned_content = stripped_content.gsub(/[\n\t]/, ' ')

      # Remove the U+00a0 character
      cleaned_content = cleaned_content.gsub(/\u00a0/, '')

      # Replace multiple consecutive spaces with a single space
      cleaned_content = cleaned_content.gsub(/\s+/, ' ')

      index_data << {
        'title' => page.data['title'],
        'url' => page.url,
        'content' => cleaned_content
      }
    end
  
    # Convert the array to JSON
    index_json = JSON.generate(index_data)
  
    return index_json
  end
  
  def finanacials_included_folder?(page)
    included_folders = ['bApps']

    # Check if the page or document is in an included folder
    included_folders.any? do |folder|
      page.url.start_with?("/#{folder}/")
    end
  end

  def finanacials_excluded_folder?(page)
    excluded_folders = []
  
    # Check if the page or document is in an excluded folder
    excluded_folders.any? do |folder|
      page.url.start_with?("/#{folder}/")
    end
  end
