---
title: Spatial Relations
published: true
date: 2019-04-17T07:54:46.587Z
description: Start seeing the world in points, lines, and polygons.
tags:
categories:
  - data
author: korenmiklos
canonical_url: https://dev.to/korenmiklos/spatial-relations-5e5f
---

---
title: Spatial Relations
published: true
description: Start seeing the world in points, lines, and polygons.
tags: GIS
---

Measurements often have a spatial dimension. If [thinking about time intervals](https://dev.to/korenmiklos/spells-221a) feels complicated, welcome to [__spatial relations__](https://en.wikipedia.org/wiki/Spatial_relation). Where in time there are only points and intervals, there are many more different types of objects in space and many more different relations. An observation may be related to a point, such as a sensor, a line, such as a river or a highway, or an area (often called _polygon_ in spatial analysis) such as a city.

![Photo by Fleur Treurniet on Unsplash](https://cdn-images-1.medium.com/max/1600/0*AvKFJTeB8sPSxG5Q)

These spatial entities may have many relations to one another. A sensor may be inside a city. A highway may intersect a river at a certain point. A highway may intersect the city. A river may serve as the boundary of the city.

> ### Simple Features
> A __point__ is given by a pair of coordinates (x,y). (We ignore 3D and only deal with the surface of the Earth.) A __line__ is a list of connected points (x1,y1)--(x2,y2)--... An __area__ is a polygon surrounded by a closed line, (x1,y1)--(x2,y2)--...--(x1,y1).
> You can have a collection of each of these items. Countries are, often, a collection of exclaves.

![By Krauss - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=21299138](https://upload.wikimedia.org/wikipedia/commons/5/55/TopologicSpatialRelarions2.png)

The first business of understanding spatial relations is to understand the type of spatial observations you have. Cities are not points, though they certainly have midpoints or centers which come up when you enter the city name in Google Maps. Cities are areas. Indeed, very few entities are actual points, though some can be reasonably approximated as such. A precise street address including the street number can be safely be approximated with its geocoordinates. 

Getting from human-readable addresses to machine-readable GPS coordinates is called __geocoding__. We do this every day when we enter addresses in Google Maps. To do this in a scalable way for all the observations in your dataset, you need a geocoding service. Google Maps has an API, but only allows geocoding for the purposes of showing points on their maps. For bulk geocoding you should turn to other providers such as [Nominatim](https://nominatim.openstreetmap.org/), using OpenStreetMap data.

> ### Projections and Spatial Reference Systems
> Geocoding convert addresses to a pair of coordinates: latitude and longitude. But what do these coordinates mean? Since two numbers represent a plane, the problem is how to map points on the surface of the Earth (which, contrary to some claims, is not flat) to points on a flat plane. This mapping is called a __projection__. There are many projections, depending on what shapes they assume about the Earth, which is slighly different from a perfect sphere. Yes, there is a classification of projections, called the [Spatial Reference System Identifier](https://en.wikipedia.org/wiki/Spatial_reference_system). By far the most widely used is the [World Geodetic System](https://en.wikipedia.org/wiki/World_Geodetic_System#WGS84), WGS84, which has an SRID of 4326. This is what you see in Google Maps and in your GPS. (Mercator projection is what you see on old printed maps, where Greenland looks larger than Africa. Don't ever use Mercator in real data.)

If you regularly work with spatial data, you should invest in knowing more about __geographic information systems__ (GIS). There are specialized GIS software to map spatial data or do spatial analysis, such as ESRI ArcGIS, MapInfo, or the open source [Quantum GIS](https://www.qgis.org/en/site/). Many database management tools also implement spatial queries, so you can easily select "all gas stations within 10km of this road."

Whereas points in space can easily be represented by just two numbers, richer spatial features require their special file format. [Well-known text](https://en.wikipedia.org/wiki/Well-known_text) provides a simple text representation of spatial features, such as `LINESTRING (30 10, 10 30, 40 40)`. This is very intuitive, but not very helpful in practice, where lines and polygons have thousands of vertices. [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON) is an open standard extension of JSON. If you are used to working with web apps and JSON data, convert your spatial information to the GeoJSON standard. By now all major GIS packages can read and write GeoJSON. There is also the proprietary binary file format of ESRI Shapefiles. These are widely used because of the ubiquity of the ArcGIS software package. The US Bureau of the Census, for example, published the [boundaries of Census tracts](https://www.census.gov/geo/maps-data/data/tiger-line.html) in ESRI Shapefiles.  
