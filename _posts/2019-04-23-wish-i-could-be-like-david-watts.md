---
title: Wish I Could Be Like David Watts
published: true
date: 2019-04-23T19:30:31.286Z
description: How do we know that _this_ David Watts is the same as _that_ David Watts?
tags:
categories:
  - data
author: koren
canonical_url: https://dev.to/korenmiklos/wish-i-could-be-like-david-watts-2edp
---

![](https://thepracticaldev.s3.amazonaws.com/i/ejv1y7jycmflj7isa14k.png)

Which David Watts? Names are not unique and we want to [use keys instead](https://medium.com/data-architect/choose-great-keys-d9ebe0485ec5). But how does David Watts become `P-12345678`? More importantly, how do we know that _this_ David Watts is the same as _that_ David Watts?

This problem is known as __entity resolution__ (ER), a.k.a. record linkage, deduplication, or fuzzy matching. (It is different from _named entity recognition_, where you have to recognize entities in flow text.) It is as complicated as it looks. Names and other fields are misspelled, so if you are too strict, you fail to link two related observations. If you are too fuzzy, you mistakenly link unrelated observations.

![](https://thepracticaldev.s3.amazonaws.com/i/uc422l830k173bp7omq0.jpg)
Photo by Steve Harvey on Unsplash

The first guiding principle of entity resolution is to embrace the imperfections. There is no perfect method, you are just balancing two types of error. _False positives_ occur when you link two observations that, in reality, refer to two different entities. _False negatives_ occur when you fail to link two observations that, in reality, represent the same entity. You can always decrease one type of error at the expense of the other by selecting a more or less stringent matching method.

The second guiding principle is to appreciate the computational complexity. If you are unsure about your data, you have to compare every observation with every other, making `N(N-1)/2` comparisons in a dataset with `N` observations. (See box on why it is sufficient to make _pairwise_ comparisons.) In a large dataset this becomes prohibitively many comparisons. For example, if you want to deduplicate users from a dataset with 100,000 observations (a small dataset), you have to make 10 _billion_ comparisons. Throughout the ER process, you should be looking for ways to reduce the number of necessary comparisons.

> ## Methods aside
> An entity resolution defines groups of observations that belong to the same entity: `e = {o1,o2,o3,...}`. Maybe surprisingly, it is sufficient to define when a _pair of observations_ denote the same entity, when `e(o1) = e(o2)`. Because equality is _transitive_, we can propagate the pairwise relation to the entire dataset: if `e(o1) = e(o2)` and `e(o2) = e(o3)` then `e(o1) = e(o3)` and `e = {o1,o2,o3}`.
>
> With fuzzy matching, we cannot tell precisely whether the entities behind two observations are _equal_. We can just calculate a _distance_ between the two observations, `d(o1,o2) ≥ 0`. The problem with this is that distances are not transitive: if `o1` and `o2` are "very close" and so are `o2` and `o3`, that does not make `o1` and `o3` "very close." We have the _triangle inequality_, `d(o1,o2) + d(o2,o3) ≥ d(o1,o3)`, but this is much weaker than transitivity. 
>
> The goal of fuzzy matching is to transform a distance into an equality relation. For example, `e(o1) = e(o2)` whenever `d(o1,o2) ≤ D` is a simple formula to use. But beware of being too fuzzy: when `D` is too big, you can end up linking observations that are very different. For example, if you allow for a _Levenshtein distance_ of 2 between a pair of words, you will find that
`book` `=` `back` `=` `hack` `=` `hacker`. I bet you didn't believe `book` `=` `hacker`.

The three steps to efficient ER are to Normalize, Match, and Merge.

First you __normalize__ your data by eliminating typos, alternative spellings, to bring the data to a more structured, more comparable format. For example, a name "Dr David George Watts III" may be normalized to "watts, david." Normalization can give you a lot of efficiency because your comparisons in the next step will be much easier. However, this is also where you can loose the most information if you are over-normalizing. 

Normalization (a.k.a. standardization) is a function that maps your observation to a simpler (often text) representation. During a normalization, you only use one observation and do not compare it to any other observation. That comes later. You can compare to (short) _white lists_, though. For example, if your observations represent cities, it is useful to compare the `city_name` field to a list of known cities and correct typos. You can also convert text fields to lower case, drop punctuation and _stop words_, round or bin numerical values.

If there is a canonical way to represent the information in your observations, use that. For example, the US Postal Services standardizes US addresses (see figure) and [provides an API](https://www.usps.com/business/web-tools-apis/address-information-api.htm) to do that. 

![](https://thepracticaldev.s3.amazonaws.com/i/dy4d171gkjmql3lltxr4.png)

Then you __match__ pairs of observations which are close enough according to your metric. The metric can allow for typos, such as a _Levenshtein distance_. It can rely on multiple fields such as name, address, phone number, date of birth. You can assign weights to each of these fields: matching on phone number may carry a large weight than matching on name. You can also opt for a _decision tree_: only check the date of birth and phone number for very common names, for example.

To minimize the number of comparisons, you typically only evaluate _potential matches_. This is where normalization can be helpful, as you only need to compare observations with normalized names of "watts, david," or those within the same city, for example.

Once you matched related observations, you have to __merge__ the information they provide about the entity they represent. For example, if you are matching "Dr David Watts" and "David Watts," you have to decide whether the person is indeed a "Dr" and whether you are keeping that information. The merge step involves aggregating information from the individual observations with whatever aggregation function you feel appropriate. You can fill in missing fields (if, say, you find the phone number for David Watts in one observation, use it throughout), use the most complete text representation (such as "Dr David George Watts III"), or simply keep all the variants of a field (by creating a _set_ of name variants, for example, {"David Watts", "Dr David Watts", "Dr David George Watts III"}). 

Follow through with all three steps to avoid mistakes later.