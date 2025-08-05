---
authors:
- koren
categories:
- duckdb
- cpp
code: "-- Load the extension\nLOAD stata_dta;\n\n-- Read Stata file directly into\
  \ DuckDB\nSELECT * FROM read_stata_dta('data/survey.dta');\n\n-- Query with SQL\
  \ operations\nSELECT region, AVG(income) \nFROM read_stata_dta('data/survey.dta')\
  \ \nGROUP BY region;"
date: 2025-07-29
description: High-performance DuckDB extension for reading Stata .dta files
download_url: https://github.com/codedthinking/stata-dta
language: cpp
tags:
- data
- stata
- duckdb
title: stata-dta
---
A high-performance DuckDB extension that enables direct reading of Stata `.dta` data files into DuckDB tables without intermediate conversion. Supports Stata file versions 105-119 with efficient streaming processing, automatic format detection, and full SQL integration.

Key features:
- Native SQL access to Stata datasets
- Support for multiple data types and missing values
- Memory-efficient chunked reading for large files
- Thread-safe stateless design
- Cross-platform compatibility with big/little-endian support