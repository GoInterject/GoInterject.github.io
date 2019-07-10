---
title: Review Date Detail Tab
layout: custom
keywords: [Training, Budget, Budget Change Query]
description: 
---

## Overview

**Purpose**: The ReviewDateDetail tab is used to show the budget amounts per account. Available filters allow the results to be restricted by Review Date Bucket, and many other options.

**Filter Options**:

* **Year** - *Optional*. Blank defaults to next Budget Year. Needs to be in YYYY format
* **District/Grouping** - *Optional*. Blank defaults to all districts you have rights to. Allows individual district, district ranges, or groupings
* **Account/Grouping** - *Optional*. Blank defaults to all accounts. Allows individual account, account ranges, or groupings
* [ **Review Type** ](#review-type-options) - *Required*. Drop-down list includes all Review Date options
* **Currency** - *Required*. Options are USD or CAD
* **Exclude IC** - *Required*. Drop-down options are FALSE or TRUE. If set to TRUE, then In-terCompany accounts are removed from the pull

![](/images/WCNTraining/Budget/BudChangeQuery_ReviewDateDetail_Fullview.png)

## Review Type Options

There are several *Review Type* drop-down options: **Corp Review Thru**, **Reg Review Thru**, **Reg Cutoff**, **Corp Cutoff**, **Corp After Cutoff**, **Corp All**, and **Reg All**.

![](/images/WCNTraining/Budget/BudChangeQuery_ReviewDateDetail_ReviewTypeDropDown.png)

Selecting a Review Date bucket shows all data up to that Review Date time stamp. Selecting *Corp After Cutoff* shows budget changes only after *Corp Cutoff*. Selecting *Corp All* shows *ALL* data, and *Reg All* shows all data up to the *Reg Cutoff* date time.