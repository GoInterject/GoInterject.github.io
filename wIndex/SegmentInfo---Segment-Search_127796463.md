---
title: Interject Documentation > SegmentInfo - Segment Search
layout: custom
keywords: [segmentinfo, segment search, function]
description: Segments is a dataportal which allows you to filter for every segment within your chart of accounts and allows you to use your groupings within your filter choices. 
---

##  **Overview**

Segments is a dataportal which allows you to filter for every segment within your chart of accounts and allows you to use your groupings within your filter choices. For example, if you are looking for accounts in **Revenue** , simply search for Revenue. If there is a segment that represents your business unit (such as Location or District) and security is enabled, it can be used to create dynamic reports that list the business units you or your team have rights to. 

To search segment groups, there is a related dataportal **GroupInfo** that provides all the groups an individual segment code may be a part of. 

###  Segments Parameters:   
  
<table>  
<tr>  
<th>

Parameter Name 
</th>  
<th>

Description 
</th>  
<th>

Default 
</th>  
<th>

Optional 
</th> </tr>  
<tr>  
<td>



SegmentNum 


</td>  
<td>

The segment number to be searched. This can be from 1 to 8. 1 is typically account, but it depends on your implementation. 
</td>  
<td>

  

</td>  
<td>



False 


</td> </tr>  
<tr>  
<td>

SegmentCode 
</td>  
<td>



Use a filter to search for the segment. Groups may be used as well as advanced filters such as <b>Revenue,!38000,52</b>

Leave blank to search all segments within your security rights. 


</td>  
<td>

  

</td>  
<td>

True 
</td> </tr>  
<tr>  
<td>

SegmentName 
</td>  
<td>

Filter on the name of the segment. This filter assumes a <b>contains</b> search. As a result, searching on <b>cash</b> will return <b>Restricted Cash</b> , <b>Petty Cash</b> , and so on. 
</td>  
<td>

  

</td>  
<td>

True 
</td> </tr> </table>

###  Available Columns:   
  
<table>  
<tr>  
<th>

Column Name 
</th>  
<th>

Description 
</th> </tr>  
<tr>  
<td>

SegmentCode 
</td>  
<td>



The segment code such as 52120 for Account or 2000 with a business unit. 


</td> </tr>  
<tr>  
<td>

SegmentName 
</td>  
<td>

The name for the segment, such as <b>Wages and Salaries</b>. 
</td> </tr>  
<tr>  
<td>

IsCredit 
</td>  
<td>

If the segment relates to Accounts, this field notes whether the account is a credit account, which is stored as a credit by default. 
</td> </tr>  
<tr>  
<td>

Inactive 
</td>  
<td>

Specifies if the segment is considered inactive 
</td> </tr> </table>
