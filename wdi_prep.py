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
    print("\nFiles have been unpacked into", MY_DATA_PATH)
else:
    print("\nFiles are ready at", MY_DATA_PATH)
#List of the unpacked data
os.system("ls -lh " + MY_DATA_PATH)
