"""
Step 0: download the raw listings (about 18 MB) into data/raw/.
The file is not stored in this repo because it is not my data, see README.

run:  python src/get_data.py
"""
import os
import urllib.request

URL = "https://raw.githubusercontent.com/DataMentes/Job-Market-Insights-analysis/main/data/processed/saudi_arabia.csv"
OUT = "data/raw/saudi_arabia.csv"

os.makedirs("data/raw", exist_ok=True)
if os.path.exists(OUT):
    print("already downloaded:", OUT)
else:
    print("downloading...")
    urllib.request.urlretrieve(URL, OUT)
    print("saved", OUT)
