#!/usr/bin/env python
#_*_ coding: utf-8 _*

import os
from six.moves import urllib
import shutil
import pandas as pd

#Data source: World Development Indicators
WDI_URL = "http://databank.worldbank.org/data/download/WDI_csv.zip"
#Setup
PROJECT_DIR = os.path.join(".", "MyWDI")
if not os.path.isdir(PROJECT_DIR):
    os.makedirs(PROJECT_DIR)
MY_DATA_PATH = os.path.join(PROJECT_DIR, "MyData")
if not os.path.isdir(MY_DATA_PATH):
    os.makedirs(MY_DATA_PATH)
ZIP_PATH = os.path.join(MY_DATA_PATH, WDI_URL.split("/")[-1])
FILE_PATH = os.path.join(MY_DATA_PATH, "WDIData.csv")

#Retrieve the target
if not os.path.isfile(ZIP_PATH):
    print("Download started at")
    os.system("date")
    print("Downloading... This may take a few minutes.")
    urllib.request.urlretrieve(WDI_URL, ZIP_PATH)
    print(WDI_URL.split("/")[-1], "has been downloaded to", MY_DATA_PATH)
else:
    print(WDI_URL.split("/")[-1], "is ready at", MY_DATA_PATH)

#Unpack the downloaded zip
if not os.path.isfile(FILE_PATH):
    shutil.unpack_archive(ZIP_PATH, MY_DATA_PATH)
    print("Files have been unpacked into", MY_DATA_PATH)
else:
    print("Files are ready at", MY_DATA_PATH)

#Create Country list and Indicator list (csv)
df = pd.read_csv(FILE_PATH, usecols=['Country Name', 'Country Code', 'country_list.csv'])
country_df = df[['Country Name', 'Country Code']].drop_duplicates(subset=['Country Name'])
country_df.to_csv(os.path.join(MY_DATA_PATH,'country_list.csv'), header=True, index=False)
indicator_df = df['Indicator Name'].drop_duplicates()
indicator_df.to_csv(os.path.join(MY_DATA_PATH,'indicator_list.csv'), header=True, index=False)

#Available files in the MY_DATA_PATH
print("\nNow, following files are available at", MY_DATA_PATH)
os.system("ls -lh " + MY_DATA_PATH)
