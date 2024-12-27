---
title: Regression Testing for Regressions
published: true
date: 2019-04-12T15:55:49.674Z
description: How do different samples, data cleaning methods, feature engineering and statistical algorithms change our estimates?
tags:
categories:
  - data
author: koren
canonical_url: https://dev.to/korenmiklos/regression-testing-for-regressions-5f9j
---

Ok, this is a confusing title. Both “regression” and “testing” have a formal definition in statistics. And “[regression testing](https://en.wikipedia.org/wiki/Regression_testing)” is a software engineering term for making sure that changes to your code did not introduce any unwanted change in its behavior.

As data scientists, we engage in regression testing all the time. Suppose I estimated that, in Hungarian manufacturing firms between 1992 and 2014, foreign managers improve firm productivity by 15 percent relative to domestic managers. Then the vendor sends an additional year’s worth of data. The first thing I want to check is how my estimate changes. Or we come up with a new algorithm to disambiguate manager names. How do the results change?

![](https://cdn-images-1.medium.com/max/1600/0*vxRjo5gLPQPcrmkY)
Photo by [五玄土 ORIENTO](https://unsplash.com/@oriento?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Given a statistical estimator (remember, [everything is a function](https://dev.to/korenmiklos/everything-is-a-function-4171))

```
estimate = function(data)
```

we often play around with different samples, data cleaning methods, feature engineering and statistical algorithms to see how our estimates change. We prefer robust findings to those that are very sensitive to small changes in our methods.

Some of this testing is formal, some of it is informal. Every course on statistics tells you how to calculate standard errors, confidence intervals, and how to conduct hypothesis tests. All of these test for one source of sensitivity in our analysis: random variation in sampling.

Suppose I conduct my study on a sample of 1,000 managers. My estimated performance premium of foreign managers is 15.0 percent, but it may be 14.8 percent in another sample of 1,000\. Or 16.1 percent in yet another sample. Standard errors (say, ±1.5 percent) and confidence intervals (say, 12.1–17.9 percent) tell me how my estimate is going to vary in different samples drawn at random. (The fact that we can calculate this from only one sample is the smartest trick of frequentist statistics. “The Lady Tasting Tea” gives a great overview of the history of statistical thought.)

[**The Lady Tasting Tea | David Salsburg | Macmillan**](https://us.macmillan.com/excerpt?isbn=9780805071344 "https://us.macmillan.com/excerpt?isbn=9780805071344")

But sampling variation is something we rarely worry about in most applications. In fact, my manager study uses data on the _universe_ of about 3 million Hungarian managers. I am more worried about robustness to different data cleaning procedures, different statistical methods. So, as everyone else, I engage in various ad-hoc robustness tests.

#### How can we make this testing more reproducible?

At the very least, we should document every step we did. I sometimes create new branches in my git repo with names like `experiment/narrow-sample`. These are often just a couple of commits in which I learn how my results would change if I used a narrower sample definition, for example. Then I go back to my `master` branch, leaving these short branches dangling. I leave a record of my tests, but I am not sure this is a proper use git branching.

We can also automate some of these tests. [Cross validation](https://en.wikipedia.org/wiki/Cross-validation_%28statistics%29) in machine learning is one example of such automated testing. We can add various assertions in simple [unit tests](https://en.wikipedia.org/wiki/Unit_testing). For example, if two Stata commands can be used to estimate the same model, I can

```
assert e(rmse) == old_mse
```

when I switch to the new command. This would check if the residual mean squared error is the same in two estimators. It is very unlikely (though not impossible) to hit the exact same MSE unless the regressions performed are the same.

But what do I do if I expect some changes, just not much? What if my point estimates are similar, but my standard errors have blown up? (An applied microeconomist’s nightmare.)

I think there is a strong need for formal characterizations of statistical estimates (a kind of “grammar of statistics”) and a framework to compare them, like so:

```
assert estimate1.coefficient.similar(estimate2.coefficient)  
assert estimate1.coefficient.significant() == estimate2.coefficient.significant()
```

What values should we test for? Point estimates, standard errors? p-values? How should we compare them? I realize I gave more questions than answers, but I feel strongly that this is something applied statistics (aka data science) can improve on.