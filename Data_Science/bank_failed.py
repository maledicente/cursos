import pandas as pd
import numpy as np

# bank_list=pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')

bank_list = pd.read_csv('banklist.csv')

print(bank_list.index)
