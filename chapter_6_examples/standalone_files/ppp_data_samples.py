# Quick script for creating new CSVs that each contain the first few rows of
# our larger data files

# importing the `pandas` library
import pandas as pd

# read the august data into a pandas DataFrame using its `read_csv()` method
august_ppp_data = pd.read_csv('public_150k_plus_080820.csv')

# the `head()` method returns the DataFrame's column headers
# along with the first 5 rows of data
august_sample = august_ppp_data.head()

# write those first few rows to a CSV called `august_sample.csv`
# using the pandas `to_csv()` method
august_sample.to_csv('august_sample.csv', index=False)

# read the recent data into a pandas DataFrame using its `read_csv()` method
recent_ppp_data = pd.read_csv('public_150k_plus_recent.csv')

# the `head()` method returns the DataFrame's column headers
# along with the first 5 rows of data
recent_sample = recent_ppp_data.head()

# write those first few rows to a CSV called `recent_sample.csv`
recent_sample.to_csv('recent_sample.csv', index=False)
