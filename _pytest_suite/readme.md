---
title: Readme - Website Test Suite
filename: "readme.md"
keywords: []
headings: []
links: []
image_dir: ""
images: []
Description: Website Test Suite

This test suite utilizes pytest to verify that the website meets criteria for a passing stable site.


# Setup
Ensure pytest is installed:

```bash
pip install pytest
```


# Usage
In the root directory of the website (i.e. gointerject.github.io) run the following command to verify tests for the site are passing

```bash
pytest
```


To view tests with print statements for debugging run:

```bash
pytest -v --capture=sys
```