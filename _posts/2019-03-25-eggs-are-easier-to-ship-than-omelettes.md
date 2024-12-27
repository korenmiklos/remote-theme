---
title: Eggs Are Easier To Ship Than Omelettes
published: true
date: 2019-03-25T09:17:34.352Z
description: I estimated the regression model we discussed last week and it didn’t work. Which regression model? What do you mean it didn’t work?
tags:
categories:
  - data
author: koren
canonical_url: https://dev.to/korenmiklos/eggs-are-easier-to-ship-than-omelettes-1g3g
---

> - I estimated the regression model we discussed last week and it didn’t work.  
> - Which regression model? What do you mean it didn’t work?

How often have you had this conversation in your research team? We have the tendency to assume that our coworkers’ minds are magically connected to ours. They’re not. In fact, there is a very **hard boundary** between my thoughts and yours. It always takes real effort to transcend this boundary, and this affects how we collaborate.

![Photo by [Jakub Kapusnak](https://unsplash.com/@foodiesfeed?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/1600/0*Z3lxEHR8vumzwAfV)
Photo by [Jakub Kapusnak](https://unsplash.com/@foodiesfeed?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)

I have recently introduced a simple template when sharing my work with coauthors. I answer the following four questions and I ask them to do the same.

1.  What deliverables have I completed?
2.  What did I learn?
3.  What actions do I need from you?
4.  What are my next steps?

For example,

1. Estimated a Poisson regression of post office counts on a bridge proximity indicator: see Table 2.  
2. After bridges are built, post offices become more frequent within 10km. The effect disappears beyond 20km.  
3. Review Table 2 and tell me what additional controls to include.  
4. Download data on river width to be used as an instrument for bridge location.

It is motivated by [daily scrum meetings](https://en.wikipedia.org/wiki/Scrum_%28software_development%29#Daily_Scrum), but I have adapted it to the explorative nature of research projects.

In the answer to Question 1, you should list **actual deliverables** (Table 2), not just vague concepts (regression model). You should format the tables and figures for publishing, including notes and labels. You will have to do this at some point anyway, you might as well help your coworker understand what precisely you did to generate Figure 3.

Research is an explorative process, and your insights are an essential input. In Question 2, you can share what you learned. What was **most surprising** to you? Do not just repeat what is in the table or the figure. You don’t want to insult your coworker’s intelligence. This is an opportunity to exercise your analytical judgement.

“_FYI_” and “_What do you think?_” don’t cut it. What **specific actions** do you need to go on with your work? If you are stuck somewhere, let them know. If you are unsure about some parts and would need more feedback, let them know.

Much as in scrum, sharing what you are planning next helps bring the team to a common understanding. You are the best positioned to decide on **next steps**, because you are the one who best understands the data and the model you are working with. (If not, request for feedback in Question 3.) So don’t be afraid to map out your work.

I sometimes just say to Question 4: “_Next steps: None. I am happy to answer clarification questions by email or Skype Monday afternoon._” It is better for your teammates to know what they can expect from you, even if it is “_nothing_.” This is especially important if you are not sharing an office. I have had way too many email ping-pongs about who did what, and if people are not in sync, this can easily take a week or more.

I certainly feel the benefits of this approach. I can catch up faster on my coauthors’ work. We need synchronous status meetings less often, and if we do, they are more productive.

This is just one example of how creating an analytics product with hard boundaries can make you more productive. You should also write [modular code](https://dev.to/korenmiklos/the-tupperware-approach-to-coding-1g74) that is [free of side effects](https://dev.to/korenmiklos/everything-is-a-function-4171). And assume (next to) nothing about your teammate’s computing environment. But more on this later.