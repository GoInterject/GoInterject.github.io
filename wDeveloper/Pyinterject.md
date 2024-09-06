---
title: Pyinterject
filename: "pyinterject.md"
layout: custom
keywords: [python, platform, api, package, scripts, crud]
headings: ["Overview", "Requirements", "Get the Code", "Setup", "What Can Pyinterject Do", "Example Scripts"]
links: ["https://www.python.org/downloads/", "https://github.com/GoInterject/pyinterject/blob/master/pyproject.toml", "https://github.com/GoInterject/pyinterject.git", "mailto:help@gointerject.com"]
image_dir: ""
images: []
description: Pyinterject is a Python client package that allows access to the Interject platform directly. With Python scripts, you can perform CRUD operations on your organization's information (e.g. data portals, data connections, users, etc.). This makes it extremely more efficient to handle bulk operations and routine maintenance.
---
* * *

## Overview

Pyinterject is a Python client package that allows access to the Interject platform directly. With Python scripts, you can perform CRUD operations on your organization's information (e.g. data portals, data connections, users, etc.). This makes it extremely more efficient to handle bulk operations and routine maintenance.

### Requirements

* [Python](https://www.python.org/downloads/){:target="_blank"}{:rel="noopener noreferrer"} 3.10 - 3.12

Once Python is installed the dependencies for Pyinterject include:

* poetry (for build)
* requests
* pydantic
* typer
* rich
* loguru
* pyodbc
* pyyaml
* pandas
* click
* prompt-toolkit
* python-dotenv
* toml

<blockquote class=highlight_note>
<b>Note:</b> For the most current version requirements of the dependencies, see the <a href="https://github.com/GoInterject/pyinterject/blob/master/pyproject.toml" target="_blank" rel="noopener noreferrer">repo</a>.
</blockquote>
<br>

###  Get the Code

With Git, you can clone the repository directly to your system. Navigate to the desired directory and run the following command:

```git
git clone https://github.com/GoInterject/pyinterject.git
```

<br>
<blockquote class=highlight_note>
<b>Note:</b> If this repo is private and you need access, please <a href="mailto:help@gointerject.com">contact us</a>. It will be public soon.
</blockquote>
<br>

### Setup

The simplest way to install Pyinterject is with pip and git:

```
pip install <PACKAGE PATH (.tar.gz OR .whl)>
```

Example:

```
pip install pyinterject-0.1.3-pkg/pyinterject-0.1.3.tar.gz
```

### What Can Pyinterject Do

Pyinterject can retrieve reports and information from a client as well as perform certain CRUD operations on a number of elements:

* Clients
* Client roles
* Custom roles
* Users
* User roles
* Data Portals
* Data Connections

### Example Scripts

The repo contains extensive documentation with example scripts that you can use to perform platform operations. Here are just a few examples:

**Get a Data Portal:**

```python
from pyinterject import Interject
ids = Interject("interject.yaml").connect()
dp = ids.get_portal("MyDataportal")
params = dp.get_params()

# (optional) View the data portal and params
print(dp)
print(params)
```

**Create a Data Connection:**

```python
from pyinterject import Interject
ids = Interject("interject.yaml").connect()
dc = ids.create_data_connection(name="testDC",
                                conn_str="testCS",
                                type="database",
                                )

# (optional) View newly created data connection
print(dc)
```

**Update a user:**

```python
from pyinterject import Interject
from pyinterject.core.models.user import User
clientIdPublic: str = ids.client.ClientIdPublic

# Get the user
user = ids.get_user("aBcdeFGHiJ") # The public id of the user

# Make changes
user.FirstName = "New_Name"
user.Address1 = "123 n. nowhere"

# Update the user
resp = ids.update_user(client_id_public=clientIdPublic, 
                       user_id_public=user.UserIDPublic, 
                       user=user)
```
