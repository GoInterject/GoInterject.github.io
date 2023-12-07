source "https://rubygems.org"

# Hello! This is where you manage which Jekyll version is used to run.
# When you want to use a different version, change it below, save the
# file and run `bundle install`. Run Jekyll with `bundle exec`, like so:
#
#     bundle exec jekyll serve
#
# This will help ensure the proper Jekyll version is running.
# Happy Jekylling!

# You can build the site locally or for Github pages
# To build locally, use 'gem "jekyll", "~> 3.9.2"'
# To build for Github pages, use 'gem "github-pages", group: :jekyll_plugins'

# NOTE: Building for github-pages will not run custom scripts in _plugin folder
# NOTE: Using 'bundle exec jekyll serve' will auto build when a change is detected
#       Because of the build_index.rb script, this will create a file and trigger the
#       auto-build continuously in a loop. Be sure to only serve while building for Github pages.

#gem "jekyll", "~> 3.9.2" # To build locally
gem "github-pages", group: :jekyll_plugins # To build for Github pages (To upgrade this build, run `bundle update github-pages`)

# This is the default theme for new Jekyll sites. You may change this to anything you like.
gem "minima", "~> 2.0"

# If you have any plugins, put them here!
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.6"
  gem 'nokogiri'
end

gem "jekyll-redirect-from"
gem "jekyll-relative-links"
gem "jekyll-sitemap"
gem "kramdown-parser-gfm"

#gem "jekyll-responsive-image"
#gem "jekyll-srcset"

# gem "jekyll-paginate"
# gem "jekyll-sitemap"
# gem "jekyll-gist"
# gem "jemoji"
# gem "jekyll-archives"

# Windows does not include zoneinfo files, so bundle the tzinfo-data gem
gem "tzinfo-data", platforms: [:mingw, :mswin, :x64_mingw, :jruby]

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1" if Gem.win_platform?

gem "rake"
ruby "3.1.2"
gem "webrick", "~> 1.7"