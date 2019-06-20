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
member_country_set = {
    "g8":["CAN", "DEU", "FRA", "GBR", "ITA", "JPN", "RUS", "USA"],
    "apt":["BRN", "CHN", "IDN", "JPN", "KHM", "KOR", "LAO", "MMR", "MYS", "PHL", "SGP", "THA", "VNM"],
    "aifta":["BRN", "IDN", "IND", "KHM", "LAO", "MMR", "MYS", "PHL", "SGP", "THA", "VNM"],
    "tpp11":["AUS", "BRN", "CAN", "CHL", "JPN", "MEX", "MYS", "NZL", "PER", "SGP", "VNM"],
    "cptpp":["AUS", "CAN", "JPN", "MEX", "NZL", "SGP", "VNM"]}

#Reads the WDIData.csv, years 2010 and before are skipped.
left_df = pd.read_csv(FILE_PATH,
                usecols=['Country Name', 'Country Code', 'Indicator Name',
                         '2011','2012','2013','2014','2015','2016','2017','2018'])

#Setting augments
try:
    myGroup = input("Input a Country group: g8, apt, aifta, tpp11, cptpp >> ")
except Exception as exc_msg:
    print("Error!{}".format(exc_msg))
myIndicator = "GDP (constant 2010 US$)"
outputFileName = myIndicator + "_" + myGroup + ".csv"

#Set right DataFrame with target country group and Indicator
right_df = pd.DataFrame(member_country_set[myGroup], columns=["Country Code"])
right_df["Indicator Name"] = myIndicator #Add a column for filtering.

#Merge (inner merge)
resultant_df = left_df.merge(right_df,
    left_on=["Country Code", "Indicator Name"], right_on=["Country Code", "Indicator Name"])

#Create an output file.
resultant_df.to_csv(os.path.join(MY_OUTPUT_PATH, outputFileName))
print("\n********************************\n" +
      outputFileName+"\nis available at "+ MY_OUTPUT_PATH +
      "\n********************************")
