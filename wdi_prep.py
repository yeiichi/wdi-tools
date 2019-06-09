#!/usr/bin/env python
#_*_ coding: utf-8 _*

import os
from six.moves import urllib
import shutil
import pandas as pd

#Data source: World Development Indicators
WDI_URL = "http://databank.worldbank.org/data/download/WDI_csv.zip"
#Setup
PROJECT_DIR = "."
MY_DATA_PATH = os.path.join(PROJECT_DIR, "myData")
if not os.path.isdir(MY_DATA_PATH):
    os.makedirs(MY_DATA_PATH)
ZIP_PATH = os.path.join(MY_DATA_PATH, WDI_URL.split("/")[-1])
FILE_PATH = os.path.join(MY_DATA_PATH, "WDIData.csv")

#Retrieve the target
if not os.path.isfile(ZIP_PATH):
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

df = pd.read_csv(FILE_PATH)
print("Country Name:\n", str(df["Country Name"].unique()))
print("Indicator Name:\n", str(df["Indicator Name"].unique()))
print("Years:\n", "from", df.columns[4], "to", df.columns[-2],)
