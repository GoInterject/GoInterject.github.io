---
title: SegmentInfo - Segment Search
layout: custom
keywords: [segmentinfo, segment search, code, function, columns]
description: Segments is a Data Portal which allows you to filter for every segment within your chart of accounts and allows you to use your groupings within your filter choices. 
---
* * *

##  Overview

Segments is a Data Portal which allows you to filter for every segment within your chart of accounts and allows you to use your groupings within your filter choices. For example, if you are looking for accounts in **Revenue** , simply search for Revenue. If there is a segment that represents your business unit (such as Location or District) and security is enabled, it can be used to create dynamic reports that list the business units you or your team have rights to. 
To search segment groups, there is a related Data Portal **GroupInfo** that provides all the groups an individual segment code may be a part of. 

###  Segments Parameters

| Parameter Name | Description | Default | Optional |
| --- | --- | --- | --- |
| SegmentNum | The segment number to be searched. This can be from 1 to 8. 1 is typically account, but it depends on your implementation. | | FALSE |
| SegmentCode | Use a filter to search for the segment. Groups may be used as well as advanced filters such as **Revenue,!38000,52**. Leave blank to search all segments within your security rights. | | TRUE |
| SegmentName | Filter on the name of the segment. This filter assumes a **contains** search. As a result, searching on **cash** will return **Restricted Cash**, **Petty Cash**, and so on. | 

### Available Columns

| Column Name | Description |
|-----|-----|
| SegmentCode | The segment code such as **52120** for Account or **2000** with a business unit. |
| SegmentName | The name for the segment, such as **Wages and Salaries**. |
| IsCredit | If the segment relates to Accounts, this field notes whether the account is a credit account, which is stored as a credit by default. |
| Inactive | Specifies if the segment is considered inactive |