---
categories:
- julia
code: 'using Targets


  add(x, y) = x + y


  @target a = 1

  @target b = 2

  @target c = add(a, b)


  @get c'
date: 2024-08-15
description: Computational pipeline management for Julia
download_url: https://github.com/codedthinking/Targets.jl
language: julia
tags:
- macromanagers
title: Targets.jl
---
