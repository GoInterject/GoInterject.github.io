---
title: jCell/jCellN()
layout: custom
keywords: [jcell, function]
descriptions: jCell retrieves data based on the provided parameters. 
---

##  Function Summary 

jCell retrieves data based on the provided parameters. The first argument is typically a [ jAcct() ](/wIndex/jAcct.html) lookup when a company has more than one segment to filter. The retrieved data is always summarized into a single value. 


Filter text for up to six segments of a chart of accounts. Use the INTERJECT function [ jAcct() ](/wIndex/jAcct.html) when more than a single segment is used as a filter. 

###  Function Arguments   

| Parameter Name | Description                                                                                                                                                                | Default | Optional |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- |
| FullAccount    | Filter text for up to six segments of a chart of accounts. Use the INTERJECT function [ jAcct() ](/wIndex/jAcct.html) when more than a single segment is used as a filter. |         | NO       |
| Period         | The month or quarter to filter the retrieved data.                                                                                                                         |         | YES      |
| Year           | The year or range of years to filter the retrieved data.                                                                                                                   |         | YES      |
| Source         | A source filter that may include budget, actual, or forecast, depending on user's system.                                                                                  |         | YES      |
| Version        | Filters the retrieved data.                                                                                                                                                |         | YES      |
| Company        | Sub-grouping to retrieve data only from a specific company or district.                                                                                                    |         | YES      |
| Currency       |                                                                                                                                                                            |         | YES      |

###  Function Composition   
  
<table>  
<tr>  
<th>

Formula 
</th>  
<th>

Example 
</th>  
<th>

Explanation 
</th> </tr>  
<tr>  
<td>

=jCell( 

FullAccount 

,Period 

,Year 

,Source 

,Version 

,Company 

,Currency 

) 

</td>  
<td>

=jCell( 

) 

</td>  
<td>

</td> </tr> </table>

###  Function Example   

| From File      | Worksheet    |
| -------------- | ------------ |
| InterjectBasic | Drill_Orders |

