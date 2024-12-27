---
title: Automate Your Data Work With Make
published: true
date: 2021-11-25T15:41:43.407Z
description: I like to think that you can remain productive over 40. Make is 43 this year and it is still my tool...
tags:
categories:
  - data
author: koren
canonical_url: https://dev.to/korenmiklos/automate-your-data-work-with-make-5eha
---

I like to think that you can remain productive over 40. [Make](https://en.wikipedia.org/wiki/Make_(software)) is 43 this year and it is still my tool of choice to automate my data cleaning or data analysis. It is versatile and beautifully simple. (At first.) Yet, [in a recent survey](https://gist.github.com/csokaimola/219911140de94e01851cc621f50ea794), we found that less than 5 percent of data savvy economists use Make regularly.

## What is Make?
Most build systems are meant to, well, build things. Compile code in Java, C, and the like. Make is supposed to do that, too, and most tutorials and StackOverflow questions will feature examples about how to build C code.

But at its very basic, Make is indeed beautifully simple. I create a text file called `Makefile` in my folder with the following content.
```make
clean_data.csv: raw_data.csv data_cleaner.py
    python data_cleaner.py
```
Then I say `make` in the shell and Make creates `clean_data.csv` from `raw_data.csv`.

In other words, I need to specify
```make
target: source
    recipe
```
and Make will run the recipe for me.

This information is something I want to note for my documentation anyway. What does my script need and what does it produce? I might as well put it in a Makefile.

This way, I can link up a chain of data work,
```make
visualization.pdf: clean_data.csv visualize.py
    python visualize.py
clean_data.csv: raw_data.csv data_cleaner.py
    python data_cleaner.py
```
When I enter `make` in the shell, I get my `visualization.pdf` recreated right from raw data.

> Order matters here. Typing `make` without any arguments recreates the *first* target found in the file called `Makefile`. I can also type `make clean_data.csv` if I want to recreate a specific target.

## Only do what is needed
Suppose I don't like the color in my graph and decide to edit `visualize.py`. But data cleaning takes a lot of time! If `clean_data.csv` is already up to date (relative to the time stamps of `raw_data.csv` and `data_cleaner.py`), Make will skip that step and only redo the visualization recipe. 

You don't have to rerun everything. Lazy is good. One more reason why you want to write [modular code](https://dev.to/korenmiklos/the-tupperware-approach-to-coding-1g74).

## Variables and functions
As soon as you feel the power of your first few simple Makefiles, you will crave for more. Can I do this? Can I do that? The answer is *yes, you can, but it will take a lot of searching on StackOverflow*.

One feature I use regularly is *automatic variables*. If I don't want to hard code file names into my neat Python script (you'll see shortly why), I can pass the names of target and source as variables.
```make
clean_data.csv: raw_data.csv data_cleaner.py
    python data_cleaner.py < $< > $@
```
This passes `raw_data.csv` (the variable `$<` refers to the first source file) to the STDIN of `data_cleaner.py` and saves the output on STDOUT to `clean_data.csv` (the variable `$@` denotes the target). 

Why these symbols? Don't ask me. They don't look pretty but they get the job done.

I can also use [functions](https://www.gnu.org/software/make/manual/html_node/Functions.html#Functions) like
```make
clean_data.csv: input/complicated-path/raw_data.csv data_cleaner.py
    python data_cleaner.py $(basename $(notdir $@)) 
```
and many more.

## Parallel execution
And now for the best part. Make can execute my jobs in parallel. On a nicely equipped AWS server, I gladly launch `make -j60` to do the tasks on 60 threads. Make serves as a job scheduler. Because it knows what depends on what, I will not run into a race condition.

> - Knock, knock.
> - Race condition.
> - Who's there?

Parallel execution doesn't help if I have a linear chain of recipe as above. But if I can split my dependency graph in parallel branches, they will be executed in the correct order.

So suppose my data is split into two (or many more). The following code would allow for parallel execution of the data cleaning recipe.
```make
visualization.pdf: merged_data.csv visualize.py
    python visualize.py
merged_data.csv: clean_data_1.csv clean_data_2.csv merge_data.py
    python merge_data.py
clean_data_%.csv: raw_data_%.csv data_cleaner.py
    python data_cleaner.py < $< > $@
```
I have used the *pattern matching* character `%` to match both `clean_data_1.csv` and `clean_data_2.csv`. 

Invoking make with the option `j`, `make -j2` will start two processes to clean the data. When *both* finished, the merge data recipe runs, then the visualization. (These will be single threaded.)

I regularly use parallel execution to do Monte Carlo simulations or draw bootstrap samples. Even if I have 500 parallel tasks and only 40 processors, `make -j40` will patiently grind away at those tasks. And if I kill my jobs to let someone run Matlab for the weekend (why would they do that?), I can simply restart on Monday with only 460 tasks to go.

- [Simple real-world Makefile](https://github.com/korenmiklos/per-shipment-costs-replication/blob/master/Makefile) with variables and for loops.
- [Not-so simple Makefile](https://github.com/korenmiklos/imported-inputs-and-productivity-replication/blob/master/code/Makefile) with variables, for loops, functions and pattern matching.

Those who still don't like Make? `$< $@` them.

Originally posted on [Medium](https://medium.com/data-architect/a-love-letter-to-make-933de68bb816).