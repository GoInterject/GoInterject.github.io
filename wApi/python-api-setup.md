---
layout: custom
title:  "Python API Setup"
filename: "python-api-setup.md"
date:   2018-10-12 9:03:02 -0700
categories: API Developer
keywords: [data api, python, setup]
headings: ["Overview", "Requirements", "Get The Code", "Install The Python Package", "Linux additional requirements", "Install Package", "Setup API", "Get Template Config", "Setup Connection Strings", "Choose Controllers", "Custom Functions", "Running The API", "More Information"]
links: ["https://github.com/GoInterject/ids-python-api", "mailto:help@gointerject.com", "https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server", "/wApi/python-api-custom-functions.html", "https://github.com/GoInterject/ids-python-api"]
image_dir: ""
images: [
	{file: "temp_gitlab_download_repo", type: "png", site: "Github", cat: "ids-python-api", sub: "", report: "", ribbon: "", config: ""}
	]
description: Shows how to setup an Interject Python data api.
---


## Overview

This is an API built on top of Python and Flask for the Interject Excel Add-in. The API Allows execution of pass-through commands on a server/database and returning data to the Interject Excel Add-in. 

In this walkthrough we will setup a Python API locally which can be used to manage dataflow to and from an Interject Report. 

### Requirements

* [Python](https://www.python.org/downloads/){:target="_blank"}{:rel="noopener noreferrer"} >= 3.9

Once Python is installed the dependencies for the Interject API include:

* poetry (for build)
* typer
* fastapi
* uvicorn
* pydantic
* pyjwt
* pandas
* sqlalchemy
* pyodbc
* loguru
* requests
* pyOpenSSL (when running API with HTTPS)

<blockquote class=highlight_note>
<b>Note:</b> For the most current version requirements of the dependencies, see the <a href="https://github.com/GoInterject/ids-python-api/blob/master/pyproject.toml" target="_blank" rel="noopener noreferrer">repo</a>.
</blockquote>
<br>

### Get The Code

Start by cloning the repository to your system.

```git
git clone https://github.com/GoInterject/ids-python-api
```

<br>
<blockquote class=highlight_note>
<b>Note:</b> If this repo is private and you need access, please <a href="mailto:help@gointerject.com">contact us</a>. It will be public soon.
</blockquote>
<br>

If you do not have git installed or prefer a different method, simply download the source code from the repository website.

![](/images/PythonApiSetup/temp_gitlab_download_repo.png)
<br>

### Install The Python Package

After cloning the repository, install the package locally to the Python environment using one of the following commands.

#### Linux Additional Requirements

If you are using a linux system it will be important to install the additional 2 tools:

1. Install mysql_config (for mysqlclient/MySQL connections): 

    ```bash
    sudo apt-get install libmysqlclient-dev
    ```

2. Install [Microsofts ODBC driver](https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server){:target="_blank"}{:rel="noopener noreferrer"} (for pyodbc/MSSQL connections) 

#### Install Package

```python
python setup.py develop
``` 

or 

```python
python setup.py -e .
```

### Setup API

#### Get Template Config

To run the API, settings related to its functionality need to be set. These are located in the file named `appconfig.py`. By default the source code has an example config named `example_appconfig.py` but this must be renamed to `appconfig.py`.

#### Setup Connection Strings

Interject Data Connections contain an Api Connection String Name. In order to allow the API to connect to a Data Connection, it must be added to the `CONNECTIONSTRINGS` dictionary object following the format `'conn_string_name' : 'conn_string'`. As many connection strings as are desired to serve from the server can be added to this variable.

```python
# Interject Data Connection Strings available to the server
CONNECTIONSTRINGS = {
    'MongoDB_Demo': 'mongodb+srv://apiTestUser:randomhashstring.mongodb.net/demo||demo|Demo'
}
```

#### Choose Controllers

In the `appconfig.py` file the variable, `CONTROLLERS` is an dictionary object with the types of database handles to be loaded by the flask server. Any of these controllers can be set to false and then will not require their dependent packages to be installed. For example if a user only wanted to use the API with a MySQL database then the controllers could be configured like below, which would not require `pandas` or `pymongo` packages to be installed.

```python
# Controllers define what python packages should be imported 
CONTROLLERS = {
    'MySQL' : True,
    'OtherSQL' : False,
    'MongoDB' : False,
    'Pandas' : False
}
```

#### Custom Functions

If the `MongoDB` or `Pandas` controllers are being utilized, then it is possible to first pull data into a custom python module before sending it as a outgoing response from the server. This functionality utilizes the `Pandas` python package and more information can be found in the [Python Api Custom Functions](/wApi/python-api-custom-functions.html){:target="_blank"}{:rel="noopener noreferrer"} page.


### Running The API

Once settings have been configured, the server can be launched using the built-in flask server (`main.py`) or via the Twisted Web production ready server (`server.py`) using the following command:

```
python server.py
``` 

### More Information

For more information visit the source code and readme for the [project on GitHub](https://github.com/GoInterject/ids-python-api){:target="_blank"}{:rel="noopener noreferrer"}.
