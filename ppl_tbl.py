#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
import pandas as pd

#Setup
PROJECT_DIR = os.path.join(".", "MyWDI")
if not os.path.isdir(PROJECT_DIR):
    os.makedirs(PROJECT_DIR)

MY_DATA_PATH = os.path.join(PROJECT_DIR, "MyData")
if not os.path.isdir(MY_DATA_PATH):
    os.makedirs(MY_DATA_PATH)

FILE_PATH = os.path.join(MY_DATA_PATH, "WDIData.csv")
if not os.path.isfile(FILE_PATH):
    os.sys.exit("\n*******************************************\n"+FILE_PATH+" was not found.\nPlease prepare the data file and try again.\n*******************************************")

MY_OUTPUT_PATH = os.path.join(PROJECT_DIR, "MyOutput")
if not os.path.isdir(MY_OUTPUT_PATH):
    os.makedirs(MY_OUTPUT_PATH)

#Filter generator
#Member country list
#g8 = ["CAN", "FRA", "DEU", "ITA", "JPN", "RUS", "GBR", "USA"]
#aifta = ["BRN", "KHM", "IND", "IDN", "LAO", "MYS", "MMR", "PHL", "SGP", "THA", "VNM"]

#Function
#def ctryFltr(ctry_group):
#    fltd_str = ""
#    for i in ctry_group:
#          fltd_str += r"(df['Country Code'] == '{}') | ".format(i)
#    return fltd_str

#Reads the WDIData.csv, years 2010 and before are skipped.
df = pd.read_csv(FILE_PATH,
                usecols=['Country Name', 'Country Code', 'Indicator Name',
                         '2011','2012','2013','2014','2015','2016','2017','2018'])

#GDP in the G8
if not os.path.isfile(os.path.join(MY_OUTPUT_PATH,'G8Ppl.csv')):
    df_G8Ppl = df[
        (
        (df['Country Code'] == 'CAN') |
        (df['Country Code'] == 'FRA') |
        (df['Country Code'] == 'DEU') |
        (df['Country Code'] == 'ITA') |
        (df['Country Code'] == 'JPN') |
        (df['Country Code'] == 'RUS') |
        (df['Country Code'] == 'GBR') |
        (df['Country Code'] == 'CHN') |
        (df['Country Code'] == 'USA')
        )
        &
        (df['Indicator Name'] == 'Population, total')]

    df_G8Ppl.to_csv(os.path.join(MY_OUTPUT_PATH,'G8Ppl.csv'))

#GDP in the AIFTA
if not os.path.isfile(os.path.join(MY_OUTPUT_PATH,'AiftaPpl')):
    df_AiftaPpl = df[
        (
        (df['Country Code'] == 'BRN') |
        (df['Country Code'] == 'KHM') |
        (df['Country Code'] == 'IND') |
        (df['Country Code'] == 'IDN') |
        (df['Country Code'] == 'LAO') |
        (df['Country Code'] == 'MYS') |
        (df['Country Code'] == 'MMR') |
        (df['Country Code'] == 'PHL') |
        (df['Country Code'] == 'SGP') |
        (df['Country Code'] == 'THA') |
        (df['Country Code'] == 'VNM')
        )
        &
        (df['Indicator Name'] == 'Population, total')]

    df_AiftaPpl.to_csv(os.path.join(MY_OUTPUT_PATH,'AiftaPpl.csv'))

print("\n*********************************\nG8Ppl.csv and AiftaPpl.csv\nare available at "+MY_OUTPUT_PATH+"\n*********************************")
