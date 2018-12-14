---
title: PairGroup()
layout: custom
---
##  Function Summary 

Provides an easy method to string multiple [ Pair() ](Pair_81756188.html) functions together in a single string argument with each Pair() delimited by a comma. This function is used as a helper function for both [Formatting](Formatting-Functions-Landing.html) and [Data](Data-Functions-Landing.html) functions. It is used to consolidate multiple Pair() functions so that they can all be applied by the same INTERJECT function. To see the functions that PairGroup() can be embedded in, view the **Usable In These Functions** section of this page. This function does have a Pair() limit of 34 Pairs. There can only be one PairGroup() embed so you cannot embed a PairGroup() inside another PairGroup().

###  Function Arguments   

| Parameter Name | Description                                                                                        | Default | Optional |
|----------------|----------------------------------------------------------------------------------------------------|---------|----------|
| Pair1          | This parameter is meant to have a [Pair()](Pair_81756188.html) function embedded in it             |         | YES      |
| Pair2          | This parameter is meant to have another Pair() function embedded in it                             |         | YES      |
| ...            | ...                                                                                                |         | ...      |
| Pair34         | This is the limit to the Pair() functions that can be embedded into a single PairGroup() function. |         | YES      |

### Excel Formula Bar Example

```Excel
PairGroup(Pair(L12:N12,"DateBegin",TRUE),Pair(M21,"Segment2",TRUE),Pair(F26:F125,"Segment1",TRUE))
```

If you want to gain more context as to how this PairGroup() function works, it is sourced from [Lab Drill: Financial Report](/wGetStarted/L-Drill-FinancialReport_128409219.html). 

### Example Function Composition

| Argument Name | Example Mapping                | Explanation |
|---------------|--------------------------------|-------------|
| Function Name | `=PairGroup()`                   |This is the excel function name used to call the function. It is not meant to standalone and is meant to be embedded inside of a [ Formatting ](Formatting-Functions-Landing.html) or [Data](Data-Functions-Landing.html) function.             |
| Pair1         | Pair(L12:N12,"DateBegin",TRUE) |This is the first pair function that is executed in this example. To better understand a pair function click [Here](/wIndex/Pair_81756188.html)            |
| Pair2         | Pair(M21,"Segment2",True)      |This is the second pair function that is executed in this example.|
| Pair3         | Pair(F26:F125,"Segment1",TRUE) |This is the third pair function that is executed in this example. |

###  Usable In These Functions  

* [ReportDrill](ReportDrill_61702556.html)
* [ReportDefaults](ReportDefaults_61702546.html)
