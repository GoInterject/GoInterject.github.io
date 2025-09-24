---
title: Pyinterject
filename: "Pyinterject.md"
layout: custom
keywords: [python, platform, api, package, scripts, crud]
headings: ["Overview", "What Can Pyinterject Do", "Example Scripts", "Get the Code"]
links: ["mailto:help@gointerject.com"]
image_dir: ""
images: []
description: Pyinterject is a Python client package that allows access to the Interject platform directly. With Python scripts, you can perform CRUD operations on your organization's information (e.g. data portals, data connections, users, etc.). This makes it extremely more efficient to handle bulk operations and routine maintenance.
---
* * *

## Overview

Pyinterject is a Python client package that allows access to the Interject platform directly. With Python scripts, you can perform CRUD operations on your organization's information (e.g. data portals, data connections, users, etc.). This makes it extremely more efficient to handle bulk operations and routine maintenance.

### What Can Pyinterject Do

Pyinterject can retrieve reports and information from a client as well as perform certain CRUD operations on a number of elements:

* Clients
* Client custom roles
* Users
* User roles
* Data Portals and parameters
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
user = ids.get_user("aBcdeFGHiJ")  # The public id of the user

# Make changes
user.FirstName = "New_Name"
user.Address1 = "123 n. nowhere"

# Update the user
resp = ids.update_user(client_id_public=clientIdPublic,
                       user_id_public=user.UserIDPublic,
                       user=user)
```

### Get the Code

The code for Pyinterject will be released soon. If you are interested, [contact us](mailto:help@gointerject.com) to be a part of the Beta release program.
