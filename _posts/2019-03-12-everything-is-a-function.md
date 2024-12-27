---
title: Everything is a Function
published: true
date: 2019-03-12T17:40:06.875Z
description: Procedural programming comes natural to scientists, because it reads like a precise protocol for an experiment. But everything in data analysis is a function.
tags:
categories:
  - data
author: korenmiklos
canonical_url: https://dev.to/korenmiklos/everything-is-a-function-4171
---

---
title: Everything is a Function
published: true
description:  Procedural programming comes natural to scientists, because it reads like a precise protocol for an experiment. But everything in data analysis is a function.
tags: data science, functional
---

Most scientists start programming in a [procedural style](https://en.wikipedia.org/wiki/Procedural_programming). I certainly did. Procedural programming comes natural to scientists, because it reads like a precise [protocol](https://www.protocols.io/) for an experiment. _Do this_. _Then do that_.

![](https://cdn-images-1.medium.com/max/1600/1*5UdOie2kHbfcSgd51cZmoA.jpeg)

> Photo by [Hans Reniers](https://unsplash.com/photos/lQGJCMY5qcM?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/search/photos/lab-test?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

I haven’t seen anyone doing data analysis in [Clojure](https://clojure.org/), [Erlang](https://www.erlang.org/), [Haskell](https://www.haskell.org/) or another functional language.

```
output = function(inputs)
```

Strange, because if you think about it, **everything in data analysis is a function**. Data cleaning maps from messy data to tidy data. A statistical estimator maps from a sample to a real number. A visualization maps from data to a colorful bitmap. For data analysis, we almost exclusively write code that does not require user interaction and would be well suited to the functional paradigm.

The conventional definition of functional programming is “no side effects.” You only compute output from inputs. You cannot rely on any other information, and you cannot pass on any other information. This very tight discipline is super useful for science, as it easier to [**argue about correctness**](https://en.wikipedia.org/wiki/Referential_transparency). For example, the ordinary least squares estimator of multivariate regressions,

![](https://cdn-images-1.medium.com/max/1600/1*T4wr_Wr3xGLlFoZhvO7txg.png)

is a mathematical function which you can characterize using pencil and paper. The Julia equivalent,

```julia
function OLS(X, Y)  
    return inv(X' * X) * X' * Y  
end
```

works independently of what you have done somewhere else in the code. (By the way, `X\Y` is a better way to write this in Julia.)

Moreover, it is easier to **automate computations** as a chain of functions. If `f(X,Y)` is the estimator of multivariate coefficients and `g(b,X)` is a prediction rule, then `g(f(X,Y),X)` is your fitted machine learning model. Relying on pure functions makes the data science process more reproducible.

#### What are some existing implementations of the chain of functions approach?

You can chain small tools in a Unix-like shell [via the pipe operator](http://swcarpentry.github.io/shell-novice/04-pipefilter/index.html). The tool reads from STDIN and writes to STDOUT and (hopefully) does not touch anything else in between. As a data scientist, you can focus on implementing the function correctly, instead of worrying how you get the data and who does what with it. This is why I am a big fan of “[data science from the command line](https://medium.com/wunderlist-engineering/is-yelp-international-an-excuse-to-roll-data-with-the-command-line-415dc04499a3).”

An even better example is `%>%` piping in R. (Julia has a similar [pipe operator](https://docs.julialang.org/en/v1.1/base/base/#Base.:|%3E).) As I understand from my R colleagues, most idiomatic code now uses this syntax.

```R
x %>% log() %>% diff() %>% exp() %>% round(1)
```

At some level, even scripting languages such as Stata do-files can be thought of as a chain of functions. A strict limitation of Stata is that you can only carry out computations on a single dataframe at a time. This limitation has huge benefits, though. You can write functional code that maps from one state of your dataframe to the next. For example,

```stata
generate y = log(x)  
replace y = 0 if x < 0
```

is a chain of two functions. Easy to read, easy to debug. It does the same as the Pandas code

```python
df['y'] = math.log(df['x'])  
df['y'][df['x'] < 0] = 0
```

Er, what? This reads more complicated because of a vastly wider state we have to control. What log function do we want to use? Which dataframe are we selecting over? Which dataframe are we changing?

#### What is not functional?

Notebooks and other REPL are not and [Joel Spolsky](https://www.joelonsoftware.com/) [hates them with a passion](https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI/edit). When you move up and down between cells, saving all kinds of variables in your workspace, you confuse yourself about what is an input to your current computation. I sometimes play around in ipython notebooks, but I always feel guilty.

[Jenny Bryan](https://jennybryan.org/) from RStudio and tidyverse also has something to say about side effects.

{% twitter 940021008764846080 %}

#### A wish list (or New Year’s resolution) for better data science

1.  Implement pipe operator in Python. I know it’s hard, but can we just have _tidyverse_ for Python?
2.  Write purely functional Stata code. Separate out input/output and even model estimation, graphing from pure data manipulation code.
3.  Explore [data science libraries](https://www.datahaskell.org/index.html) for real functional languages. I know, SQL is functional, but it reads very complicated.
4.  More generally, keep an eye out for side effects. Do I need this global parameter? Do I need to write this to disk? Aim to write as pure functions as possible.