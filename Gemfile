source "https://rubygems.org"
#
# Hello. This is where you manage which Jekyll version is used to run.
# When you want to use a different version, change it below, save the
# file and run `bundle install`. Run Jekyll with `bundle exec`, like so:
#
#     bundle exec jekyll serve
#
# This will help ensure the proper Jekyll version is running.
# Happy Jekylling.
#
# NOTE: This site is built and deployed using Github actions as of 12/15/2023
#    Therefore there is no need to use the gem "github-pages" as with pervious versions
#    Github actions will build the site and run custom scripts

gem "jekyll", "~> 3.9.2"

# This is the default theme for new Jekyll sites. You may change this to anything you like.
gem "minima", "~> 2.0"

# If you have any plugins, put them here.
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
ruby "~> 3.1.0"
gem "webrick", "~> 1.7"
