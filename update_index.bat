@echo off

REM Run this script before pushing to Github GoInterject.github.io repo
REM This script sets the use_github_pages to false and builds the site
REM The search_index.json file will be rebuilt after the build process
REM The script then sets the use_github_pages back to true

setlocal enabledelayedexpansion

set "config_file=Gemfile"
set "temp_file=%config_file%.tmp"

REM Set use_github_pages to false
(
for /f "tokens=* delims=" %%A in ('type "%config_file%"') do (
        set "line=%%A"
        set "line=!line:true=false!"
        echo !line!
    )) > %temp_file%

move /y %temp_file% %config_file% > nul

echo Set use_github_pages to false

echo Running Jekyll build...
call bundle exec jekyll build

REM Set use_github_pages to true
(
for /f "tokens=* delims=" %%A in ('type "%config_file%"') do (
        set "line=%%A"
        set "line=!line:false=true!"
        echo !line!
    )) > %temp_file%

move /y %temp_file% %config_file% > nul

echo Set use_github_pages back to true

pause