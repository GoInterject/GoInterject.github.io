# _plugins/build_index.rb

puts "Setting build index for hook post_write"

Jekyll::Hooks.register :site, :post_write do |site|
  puts "Building index search_index.json"

  # Build your index here
    index_content = build_index(site)
  
    # Specify the path and filename for the index file
    parent_folder = File.expand_path("..", site.dest)
    index_file_path = File.join(parent_folder, 'search_index.json')
  
    # Write the index content to the file
    File.write(index_file_path, index_content)
  end
  
  def build_index(site)
    # Implement your logic to build the index
    # This can include collecting metadata from pages, posts, etc.
  
    # Build an array of hashes containing relevant data
    index_data = []
  
    # Iterate over all pages on the website
    site.pages.each do |page|
      # Exclude pages from specific folders
      next if excluded_folder?(page)
  
      index_data << {
        'title' => page.data['title'],
        'url' => page.url,
        'content' => page.content
      }
    end
  
    # Iterate over all documents in collections
    site.collections.each do |collection_name, collection|
      collection.docs.each do |document|
        # Exclude documents from specific folders
        next if excluded_folder?(document)
  
        index_data << {
          'title' => document.data['title'],
          'url' => document.url,
          #'content' => document.content
        }
      end
    end
  
    # Convert the array to JSON
    index_json = JSON.generate(index_data)
  
    return index_json
  end
  
  def excluded_folder?(page_or_document)
    excluded_folders = ['bApps', 'fonts', 'schemas']
  
    # Check if the page or document is in an excluded folder
    excluded_folders.any? do |folder|
      page_or_document.url.start_with?("/#{folder}/") ||
      page_or_document.url.include?("/#{folder}/")
    end
  end
  