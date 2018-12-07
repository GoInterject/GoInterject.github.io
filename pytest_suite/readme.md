# Website Test Suite
This test suite utilizes pytest to verify that the website meets criteria for a passing stable site.


# Setup
Ensure pytest is install:

```bash
> pip install pytest
```


# Usage
In the root directory of the website (i.e. gointerject.github.io) run the following command to verify tests for the site are passing

```bash
> pytest -v
```


To view tests with print statments for debugging run:

```bash
> pytest -v --capture=no
```