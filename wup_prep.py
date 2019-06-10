#!/usr/bin/env python
# coding: utf-8

import os
from six.moves import urllib
#import shutil
import pandas as pd

#Data source: World Urbanization Prospects 2018
SRC_URL = "https://population.un.org/wup/Download/Files/WUP2018-F13-Capital_Cities.xls"
#Setup
PROJECT_DIR = os.path.join(".", "MyWUP")
if not os.path.isdir(PROJECT_DIR):
    os.makedirs(PROJECT_DIR)
MY_DATA_PATH = os.path.join(PROJECT_DIR, "MyData")
if not os.path.isdir(MY_DATA_PATH):
    os.makedirs(MY_DATA_PATH)
#ZIP_PATH = os.path.join(MY_DATA_PATH, SRC_URL.split("/")[-1])
FILE_PATH = os.path.join(MY_DATA_PATH, SRC_URL.split("/")[-1])

#Retrieve the target
if not os.path.isfile(FILE_PATH):
    print("Download started at")
    os.system("date")
    #print("Downloading... This may take a few minutes.")
    urllib.request.urlretrieve(SRC_URL, FILE_PATH)
    print(SRC_URL.split("/")[-1], "has been downloaded to", MY_DATA_PATH)
else:
    print(SRC_URL.split("/")[-1], "is ready at", MY_DATA_PATH)

#Unpack the downloaded zip
#if not os.path.isfile(FILE_PATH):
#    shutil.unpack_archive(ZIP_PATH, MY_DATA_PATH)
#    print("Files have been unpacked into", MY_DATA_PATH)
#else:
#    print("Files are ready at", MY_DATA_PATH)

cap_LatLong_df = pd.read_excel(FILE_PATH, skiprows=16,
usecols=['Country or area', 'Capital City', 'Latitude', 'Longitude'])
cap_LatLong_df.to_csv(os.path.join(MY_DATA_PATH,'cap_LatLong.csv'), header=True, index=False)

#country_df = df[['Country Name', 'Country Code']].drop_duplicates(subset=['Country Name'])
#country_df.to_csv(os.path.join(MY_DATA_PATH,'country_list.csv'), header=True, index=False)
#indicator_df = df['Indicator Name'].drop_duplicates()
#indicator_df.to_csv(os.path.join(MY_DATA_PATH,'indicator_list.csv'), header=True, index=False)

#Available files in the MY_DATA_PATH
print("\nNow, following files are available at", MY_DATA_PATH)
os.system("ls -lh " + MY_DATA_PATH)
