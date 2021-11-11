# Quick script for finding a business within our data set by (partial) name

# importing the `pandas` library
import pandas as pd

# read the recent data sample into a pandas DataFrame
ppp_data = pd.read_csv('public_150k_plus_recent.csv')

# create a DataFrame without any missing `BorrowerName` values
ppp_data_named_borrowers = ppp_data[ppp_data['BorrowerName'].notna()]

# because precise matching can be tricky,
# we'll use the pandas `str.contains()` method
bankruptcy_example = ppp_data_named_borrowers[ppp_data_named_borrowers['BorrowerName']
 .str.contains('WATERFORD RECEPTIONS')]

# transposing the result so it's easier to read
print(bankruptcy_example.transpose())
