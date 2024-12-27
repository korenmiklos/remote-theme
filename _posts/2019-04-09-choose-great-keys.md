---
title: Choose Great Keys
published: true
date: 2019-04-09T21:01:37.888Z
description: Keys should be human readable, not just machine readable.
tags:
categories:
  - data
author: koren
canonical_url: https://dev.to/korenmiklos/choose-great-keys-e2f
---

Keys are what we use to refer to entities in data tables. A primary key is the unique identifier of each observation in your table, a foreign key is pointing to other entities in another table.

But how do these keys look in real life? Are they consecutively numbering rows from 1? Can we use names of firms and people as keys? Should we use cryptographic hash functions to generate [universally unique identifiers](https://en.wikipedia.org/wiki/Universally_unique_identifier)? Often you will have this decided for you with keys already given in the data store in which you are loading your data. But sometimes you will face the distinct pleasure of choosing your own keys.

![Photo by [Tim Evans](https://unsplash.com/@tjevans?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/9478/0*_VYwP0-zFPcTmacT)*Photo by [Tim Evans](https://unsplash.com/@tjevans?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

### Names are not unique

Most importantly, keys should be *unique*, that is, no two different observations should receive the same key. This sounds obvious, but your design can make this requirement harder or easier to satisfy.

Suppose you decide to refer to users by their last name (an obviously silly idea). After the second “*smith*” and “*jones*,” you will have to change your system. Then you decide to add first names. You are safe until the second “*john_smith*” or “*charles_jones*.” You will end up with “*john_smith_02*,” which is just plain ugly. (And what if there are more than 99 John Smiths’s in your data?)

If you think you would never commit such silly mistakes, read Patrick McKenzie's [list of 40 falsehoods](https://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/) programmers often assume about names. I come from a country which uses the Eastern name order, uses many accented letters, and where wives’ married names often do not include their first names (as in “*Szabó Jánosné*” ~ “*Mrs John Smith*”). I have encountered people with only one name. How hard it is for them to enter their name into any web app or database?

It gets worse with companies and organizations. It is next to impossible to use their correct name more than once. The municipal government of the Budapest district where my university is located is officially called “*Belváros-Lipótváros Budapest Főváros V. kerület Polgármesteri Hivatal*.” How often do you think it is spelled correctly in real-world data? Moreover, there are 37 elementary schools in Hungary whose official name is simply “*elementary school*.”

No, names are not unique, and are a terrible choice for unique keys. This is why most web apps and databases opt for a user chosen alphanumeric userid, an email address, or a computer-generated numeric identifier.

### Verbose keys

Follow these four tips to create useful keys.

1. **If there is a well established identifier for the entity you are describing, use that**. People have Social Security Numbers, firms have Employer Identification Numbers, regions have NUTS or FIPS codes, countries have ISO 3166 codes. Do not invent your own key unless you absolutely have to.

1. **Your key should be human readable, not just machine readable**. A sequentially increasing integer ID is not very helpful. Nor is an SHA1 hash such as dc6e5923f968db05aee116d94d11792385a9fcca8. Depending on context, combining 2-3 letters and 8-10 digits works best.

1. **Keys for one type of entity should be easily distinguishable from keys for another type of entity**. When you look at a key, you should immediately see what entity it refers to. Everyone in the U.S. knows “*08540”* is a ZIP-code and “*770-10-2831”* is a Social Security Number.

1. **Use hyphens or other punctuation to denote hierarchy in keys**. The ZIP+4 code “*53075-1108”* clearly delineates the 5-digit ZIP code from the 4-digit routing number. URLs are the best example of hierarchical keys: “*medium.com/data-architect”* refers to this blog, but you can use this structure to generate keys for other blogs on Medium.
> For example, you could use *F-DE-01234567* to refer to a German firm. *F-HU-12345678* would be a Hungarian firm. (Note the use of 2-letter ISO-3166 country codes.) *P-1234567890* could be a person.

Depending on the type of entity you are modeling, look out for these existing unique identifiers.

* **companies**: tax identifier, Employer Identification Number (EIN), EU VAT identifier, Open Corporates ID

* **individuals**: Social Security Number, email address

* **regions**: FIPS, NUTS, ZIP-code (although a ZIP code does not refer to an *area*)

* **countries**: ISO 3166 standard, 2-letter, 3-letter or numeric identifier

Finding good looking keys is fun. Go out and have some.
