---
title: Reproducible Data Wrangling
published: true
date: 2019-04-02T19:06:18.397Z
description: For the movements of "reproducible research" and "open data" to catch on, we need more tools to assist. 
tags:
categories:
  - data
author: koren
canonical_url: https://dev.to/korenmiklos/reproducible-data-wrangling-24eb
---

> “I spend more than half of my time integrating, cleansing and transforming data without doing any actual analysis.” (interviewee in the seminal Kandel, Paepcke, Hellerstein and Heer interview study of business analytics practices)

It is almost a *cliché* in data science that we spend the vast majority of our time getting, transforming, merging, or otherwise preparing data for the actual analysis.

![Photo by [Mr Cup / Fabien Barral](https://unsplash.com/@iammrcup?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)](https://cdn-images-1.medium.com/max/8576/0*9F8L8Wj47VUOvtWF)*Photo by [Mr Cup / Fabien Barral](https://unsplash.com/@iammrcup?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)*

This *data wrangling*, however, should also be reproducible. Journal referees, editors and readers have come to expect that if I make a theoretical statement, I offer a proof. If I make a statistical claim, I back it up by a discussion of the methodology and offer software code for replication. The reproducibility of wrangling, however, often hinges on author statements like “*we use the 2013 wave of the World Development Indicators*” or “*data comes from Penn World Tables *7.”

Most authors don’t make their data wrangling reproducible because reproducibility is hard. Very hard. Data comes in various formats, some of the files are huge, and most researchers don’t speak a general-purpose programming language that could be used to automate the data transformation process. In fact, most data transformation is still *ad hoc*, pointing and clicking in Excel, copying and pasting and doing a bunch of VLOOKUPs. (For the record, VLOOKUPs are great.)

Take the following example. For [recent study](http://miklos.koren.hu/papers/peer_reviewed_publications/administrative_barriers_to_trade/), I really wanted to take reproducibility seriously and do everything by the book. This has lead to a number of challenges.

* **Large datasets**. The originals of the datasets I use are dozens of GB in size. By the end of my wrangling, I end up with a few hundred MBs, but if I want to make the whole process transparent and reproducible, I also need to show the original data.

* **Inconsistent URLs and schema**. The Spanish *Agencia Tributaria* is very helpful in publishing *all* their trade online. There is a lot of structure in how they store the files and what they contain, but every year there are a few inconsistencies to make me cringe and debug for hours. (For example, find the odd one out among the [links here](https://www.agenciatributaria.es/AEAT.internet/Inicio/La_Agencia_Tributaria/Memorias_y_estadisticas_tributarias/Estadisticas/_Comercio_exterior_/Datos_estadisticos/Descarga_de_Datos_Estadisticos/Descarga_de_datos_mensuales_maxima_desagregacion_en_Euros__centimos_/2009/Enero/Enero.shtml).)

* **Country names**. This is a special case of inconsistent schema. Every single data source uses their own codebook for identifying countries. In the best case, you get the 3-letter ISO-3166 code of the country, like HUN and USA. These are great because they are a standard and quite human readable, right? Not so fast. Did you know that the 3-letter code changes when the country changes name? When Zaire became the Democratic Republic of the Congo, its [code changed from ZAR to COD](https://www.iso.org/obp/ui/#iso:code:3166:ZR). The best would be to use the [*numeric codes* of ISO-3166](http://en.wikipedia.org/wiki/ISO_3166-1_numeric), which are fairly stable over time, but almost nobody uses these.

* **Undocumented and unsupported data on websites**. The [Doing Business](http://doingbusiness.org/) project of the World Bank provides one of the greatest resources on cross-country data. But when they offer to “get all data,” they don’t actually mean it.

![](https://cdn-images-1.medium.com/max/2000/0*23yVozJ8i5uo3TPI.png)

They have much more detailed data on their website which you cannot download and is not archived. These are, for example, the detailed costs of importing in Afghanistan in 2014, but the website doesn’t publish this data for earlier years. Luckily, [web.archive.org](http://web.archive.org/web/20091003023159/http://www.doingbusiness.org/ExploreTopics/TradingAcrossBorders/Details.aspx?economyid=2) comes to the rescue.

![](https://cdn-images-1.medium.com/max/2000/0*0lGAN_KO3AuJYFMs.png)

* **Big boxes of data**. There is an 18MB .xls file I use from the 860MB .zip-file an author helpfully published on their website. The objective is laudable (like I said above, make everything available in the replication package), but I would prefer the option to download just what I need.

* **Undocumented vs illegal**. Most economics data sets I work with have no clear license terms attached. See this very helpful [NBER list](https://www.nber.org/data/), for example. For most data sets, I cannot figure out what I am allowed to do with them. Nobody likes to do something illegal, so better just leave them out from a replication package.

For the movements of “reproducible research” and “open data” to really catch on, we need more tools like the ones from [FrictionlessData](https://frictionlessdata.io/), [DataCite](https://datacite.org/), and data APIs that can be programmatically queried (like the [World Bank Data API](http://data.worldbank.org/developers/api-overview)).

And if you publish original data, please, please, follow the [World Bank](https://datacatalog.worldbank.org/search?sort_by=field_wbddh_modified_date&sort_order=DESC#), [OffeneRegister](https://offeneregister.de/daten/), [OpenTender](https://opentender.eu/start), and provide not just easy ways to download, but simple license terms such as [Creative Commons](https://creativecommons.org/) or [Open Database License](https://en.wikipedia.org/wiki/Open_Database_License).
