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

indicator_set = {
    "515":"GDP (constant 2010 US$)",
    "518":"GDP (current US$)",
    "522":"GDP per capita (constant 2010 US$)",
    "525":"GDP per capita (current US$)",
    "543":"GNI (constant 2010 US$)",
    "546":"GNI (current US$)",
    "548":"GNI per capita (constant 2010 US$)"}

#Reads the WDIData.csv, years 2010 and before are skipped.
left_df = pd.read_csv(FILE_PATH,
                usecols=['Country Name', 'Country Code', 'Indicator Name',
                         '2011','2012','2013','2014','2015','2016','2017','2018'])

#Function: get augments
def get_augs():
#Get a country group
    try:
        myGroup = input("""Input a Country group: g8, apt, aifta, tpp11 or cptpp")
        g8:    CAN, DEU, FRA, GBR, ITA, JPN, RUS, USA
        apt:   BRN, CHN, IDN, JPN, KHM, KOR, LAO, MMR, MYS, PHL, SGP, THA, VNM
        aifta: BRN, IDN, IND, KHM, LAO, MMR, MYS, PHL, SGP, THA, VNM
        tpp11: AUS, BRN, CAN, CHL, JPN, MEX, MYS, NZL, PER, SGP, VNM
        cptpp: AUS, CAN, JPN, MEX, NZL, SGP, VNM\n>> """)
    except Exception as exc_msg:
        print("Error!{}".format(exc_msg))
#Get an indicator number
    try:
        myIndicator_code = input("""Input an Indicagor Number:
        515: GDP (constant 2010 US$)
        518: GDP (current US$)
        522: GDP per capita (constant 2010 US$)
        525: GDP per capita (current US$)
        543: GNI (constant 2010 US$)
        546: GNI (current US$)
        548: GNI per capita (constant 2010 US$)\n>> """)
    except Exception as exc_msg:
        print("Error!{}".format(exc_msg))
    myIndicator = indicator_set[myIndicator_code]
#Confirm augments
    flag = True
    while flag:
        print("\nAre they OK?\n\tYour group:{}\n\t{}\n".format(myGroup, myIndicator))
        confirmation = input("(y/n/abort) >> ")

        if confirmation.lower() == "abort":
            os.sys.exit("Aborted!\n")
        elif not confirmation.lower() in {"y", "yes", "ok"}:
            get_augs()
        else: flag = False
#Confirmed augments
    outputFileName = myIndicator + "_" + myGroup + ".csv"
    return myGroup, myIndicator, outputFileName

#Set augments
myGroup, myIndicator, outputFileName = get_augs()

#Set right DataFrame with target country group and Indicator
right_df = pd.DataFrame(member_country_set[myGroup], columns=["Country Code"])
right_df["Indicator Name"] = myIndicator #Add a column for filtering.

#Merge (inner merge)
resultant_df = left_df.merge(right_df,
    left_on=["Country Code", "Indicator Name"], right_on=["Country Code", "Indicator Name"])

#Create an output file.
resultant_df.to_csv(os.path.join(MY_OUTPUT_PATH, outputFileName))
print("\n {}\n is available at {}\n".format(outputFileName, MY_OUTPUT_PATH))
