---
title: The Tupperware Approach to Coding
published: true
date: 2019-03-05T21:29:12.824Z
description: A tree structure is effective to organize the information you have to keep in your head if you optimize between small and few.
tags:
categories:
  - data
author: koren
canonical_url: https://dev.to/korenmiklos/the-tupperware-approach-to-coding-1g74
---

Coding is like ultra running. It is a huge, often daunting task. If you don’t want to go crazy, you have to break it into smaller chunks. _Before lunch, I will finish this function. At the next aid station, I have to refill my water bottles._

Dividing the problem into many small, manageable chunks is one way to deal with complex problems. But if you split the problem into too small chunks, you will end with too many of them. Again you will feel overwhelmed.

![](https://thepracticaldev.s3.amazonaws.com/i/iihvoky9de4s9m5uhnl9.jpeg)

A nested structure with multiple layers is often helpful. When running an ultra, I like to split the race into thirds, the thirds into sections between aid stations, and, indeed, I often just focus on single breaths. For coding, there are libraries, modules, classes, functions and single statements.

> A tree structure is effective to organize the information you have to keep in your head if you optimize between small and few.

Perhaps the best known example is how we think about time. Time is naturally modular. There are about 30 days in a month and 12 months in a year. (We are lucky with this arrangement. A Saturn year takes about 25,000 Saturn days.) This way, we can have both _small_ and _few_. I can plan for today. For this week. I can estimate how many weeks a project takes. I can select projects to work on next year.

Notice how I am moving up and down across multiple levels of abstraction. When I make plans for today, I do not pause to think about how these activities affect my goals for the year. (Maybe I should.) When I schedule different projects across the coming weeks, I do not pause to think about whether I will do them in the morning or the afternoon. I just assume that my daily plan will fall in line.

Another well known example is the folder structure on most operating systems. (The earliest mentions of folder hierarchies are from [1958](https://www.computer.org/csdl/proceedings/afips/1958/5053/00/50530059.pdf) and [1965](https://multicians.org/fjcc4.html).) I can put a folder inside another folder, down to an arbitrary depth. This way, I can look around in my current folder and have an understanding quickly. If I need more details, I dig deeper into a folder inside.

> Much as a structured calendar and a nice folder structure, a well structured program helps organize your thoughts.

I have written scripts, especially early in my career, that did everything at once. Thousands of lines of code, executing line by line. Looking through and trying to edit these scripts later is like an ultra runner’s nightmare.

![Some of the 4569 lines of code in a single script](https://thepracticaldev.s3.amazonaws.com/i/esvu89rv2awxynywh2uh.png)
Later on, I erred on the side of too many. In a research project I could easily have 20–30 do files with little organization. Looking back, this makes me nauseous.

![Some of 36 scripts.](https://thepracticaldev.s3.amazonaws.com/i/2pqr8sn84odob9vkvnj4.png)
So what is the right level of abstraction? What is small enough? How many are few enough?

> Each of your chunks should be small enough to keep in your head.

You should not look at another piece of code to find out what the current function does. Often, this means only a couple of lines of code per function and a couple of functions per module. Object oriented languages are modular by design, but you can split up even simple Stata scripts in many smaller pieces.

> And you should not refer to more than 6–8 other chunks in any one layer.

More than that and you will get lost. Having 10 or more scripts to look at and run is a good indication that you want to introduce additional layers. Can these scripts be differentiated by function? By how often they are called? By what inputs they need? Anything to make you more organized.

![This is much better. But I can still improve the organization of utils.](https://thepracticaldev.s3.amazonaws.com/i/tr2fw1l8yat1dsavbhwg.png)
Nurture your code with the same love you nurture your calendar.