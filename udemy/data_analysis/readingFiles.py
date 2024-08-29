import pandas as pd
import numpy as np

url='https://www.fdic.gov/bank-failures/failed-bank-list'
data = pd.read_html(url)
print(data[0])