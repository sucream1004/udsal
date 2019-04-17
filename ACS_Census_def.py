#!/usr/bin/env python
# coding: utf-8

import os
import sys

import numpy as np
import pandas as pd
import geopandas as gpd
from shapely import wkt

import matplotlib.pyplot as plt

var = sys.argv[1]
url = 'https://api.census.gov/data/2017/acs/acs5?get={},NAME&for=tract:*&in=state:36%20county:*'.format(var)
print('Loading {} data'.format(var))
dat = pd.read_json(url)
col_name = [n for n in dat.iloc[0]]
dat.columns = col_name
dat.drop(dat.head(1).index, inplace=True)

dat['cd'] = dat.state + dat.county + dat.tract

ct2010 = pd.read_csv('https://data.cityofnewyork.us/api/views/i69b-3rdj/rows.csv?accessType=api', dtype=str)

ct2010['county'] = None
ct2010['county'][ct2010['BoroName']=='Staten Island'] = '085'
ct2010['county'][ct2010['BoroName']=='Manhattan'] = '061'
ct2010['county'][ct2010['BoroName']=='Brooklyn'] = '047'
ct2010['county'][ct2010['BoroName']=='Bronx'] = '005'
ct2010['county'][ct2010['BoroName']=='Queens'] = '081'

ct2010['cd'] = '36' + ct2010['county'] + ct2010['CT2010']

gdf = gpd.GeoDataFrame(ct2010)
gdf['the_geom'] = gdf['the_geom'].apply(wkt.loads)
gdf = gpd.GeoDataFrame(gdf, geometry='the_geom')

gdf = gdf.merge(dat, on='cd')
print('Merging Data')
fig, ax = plt.subplots(figsize=(20,20))
gdf.plot(ax=ax, column=str(var), cmap='OrRd', edgecolor='black', scheme='quantiles', legend=True)
plt.show()

