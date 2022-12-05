---
title: Managing Settings Cache
layout: custom
---
* * *

##  **Overview**

Interject optimizes speed by caching company settings, such as Data Portals, Connections, and Report Library templates. This information is received on login and is stored in memory for as long as the Excel session is open. This is an important topic for new deployments where these settings may need to change often.  If there are any changes to these company settings, the Interject Excel add-in will check for changes at various actions. Opening the Report Library or the Report Builder automatically checks for setting changes. Other actions like Pull, Save, or Drill check only every two hours, since these actions occur quite often and could create excess communication. 

###  Forcing Cached Settings to Refresh 

There may be situations where deploying new Interject tools may be in a critical time when company settings require rapid updates. For example, a newly deployed report may need a change, as well as a new Data Portal parameter, to support a new filter that was requested by users. The stored procedure that is assigned to the Data Portal would be changed immediately in the database. The Data Portal will be updated with a new parameter, and a new version of the report is added to the Report Library. However, since users may not receive new cached settings for up to 2 hours, the users would continue to use the old report and outdated Data Portal information. Since the stored procedure change is immediate, the old report would error since it is not passing the new stored procedure’s new parameter value.  To remedy this situation, there are a couple options. 

Users could open the Report Library that checks to refresh the cached settings instead of waiting on the 2 hour cycle that automatically happens on every Interject pull. This is not ideal. 

The best solution is to change the refresh cache settings interval before the deployment. In the Interject Website Portal there is a setting that allows the 2 hour settings cache check-in to be temporarily made as frequent as every 5 minutes. After 2 days, the setting will revert back to 2 hours. Using this setting during critical deployments can help settings changes propagate much quicker and avoid confusion with users. 

###  Making the Middle Tier Forgiving 

Another technique that can make Data Portal changes easier to manage is to update the middle-tier, a stored procedure, or the website API, so that no error results if the new parameter is missing. You can go further and provide a message to the user saying they are using an older version of the report and ask them to open the new version from the Report Library. 
