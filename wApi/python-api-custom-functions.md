---
layout: custom
title:  "Custom Functions With The Python Interject API"
date:   2018-10-12 9:03:02 -0700
categories: API Developer
---


## Setup

setup requires the following conditions be met:

- The Python Interject API is downloaded and all dependancies satisfied
- `appconfig.py` contains a name of a valid python script in the current directory for `CUSTOM_MODULE`
    - I.E. `CUSTOM_MODULE = 'etl'`
- the custom python function script contains a function that expects kwargs and returns a dataframe
- Interject Connection
    - name = user defined
    - connection type = "web api"
    - api root uri = url to your interject python server
    - api connection string name = Not Needed
    - authentication type = 10 

- Interject Dataportal 
    - connection = name of connection
    - command type = stored procedure name
    - Stored Procedure / Command = function name to run in CUSTOM_MODULE
    - Api Relative URI = `PandasDataframeRequest` or `MongoDBRequest`

    ```python
    ### etl.py ###
    import pandas as pd

    def interject_custom_func(**kwargs):
        """ Custom defined function which operates on pulled data from excel
            or a dataportal source before sending the data to its final destination
            
            Arguments:
                kwargs {dict} -- dictionary with options and input dataframe

            NOTE: - kwargs contains (dataframe, param_list)
                - expects return value to be a pandas DataFrame() 
        """

        d = {"column1":[1,2,3,4,5,6,7,8], "column2" : [5,4,3,2,1,5,43,7]}
        kwargs['dataframe'] = pd.DataFrame(d)
        kwargs['user_message'] = "user message to return"
        kwargs['param_list']['param1']['output_value'] = "output value"
        return kwargs

    ```

- server must be running for interject to pull data from. call using 

    ```
    > python main.py
    ```

    NOTE: the following files are required to exist in the local directory of the server
    - main.py
    - etl.py (arbitrary module name)
    - appconfig.py

## Output Options
Custom functions have the ability to utilize input and output parameters as well as return user messages to Interject.

Interject request information is passed to a custom function through the kwargs function argument.
<table>
<th>Parameters</th><th>Type</th><th>Description</th>
<tr>
    <td>`kwargs['dataframe']`</td>
    <td>pandas.DataFrame()</td>
    <td>Pandas dataframe</td>
</tr>
</table>

<!--
|Parameters|Type|Description|
|-|-|-|
| `kwargs['dataframe']` | pandas.DataFrame() | Pandas dataframe  |
| `kwargs['user_message']` |string | Interject User message (notices should contain "usernotice:", and errors should contain "usererror:")  |
| `kwargs['param_list'][<ParamName>]['name']` |string | the name of the formula parameter in the dataportal |
| `kwargs['param_list'][<ParamName>]['expects_output']` |bool |defines if the output_value should replace the value in the report |
| `kwargs['param_list'][<ParamName>]['in_formula']` |bool |determines whether the parameter is in the report formula or not (system params will be false) |
| `kwargs['param_list'][<ParamName>]['input_value']` |any |input parameter value from the user |
| `kwargs['param_list'][<ParamName>]['output_value']` |any |output parameter defined by the dataportal |
| `kwargs['param_list'][<ParamName>]['user_validation_msg']` |string |Not Currently Available|
-->