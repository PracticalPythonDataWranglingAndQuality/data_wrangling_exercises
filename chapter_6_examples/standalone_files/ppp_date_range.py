# Quick script for finding the earliest and latest loan dates in the PPP loan
# data

# importing the `pandas` library
import pandas as pd

# read the recent data into a pandas DataFrame using its `read_csv()` method
ppp_data = pd.read_csv('public_150k_plus_recent.csv')

# convert the values in the `DateApproved` column to *actual* dates
ppp_data['DateApproved'] = pd.to_datetime(ppp_data['DateApproved'],
 format='%m/%d/%Y')

# print out the `min()` and `max()` values in the `DateApproved` column
print(ppp_data['DateApproved'].min())
print(ppp_data['DateApproved'].max())
