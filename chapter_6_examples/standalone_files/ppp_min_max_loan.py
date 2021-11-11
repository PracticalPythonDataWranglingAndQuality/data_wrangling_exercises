# Quick script for finding the minimum and maximum loans currently approved
# in our PPP loan data set

# importing the `pandas` library
import pandas as pd

# read the recent data into a pandas DataFrame
ppp_data = pd.read_csv('public_150k_plus_recent.csv')

# use the pandas `min()` and `max()` methods to retrieve the
# largest and smallest values, respectively
print(ppp_data['CurrentApprovalAmount'].min())
print(ppp_data['CurrentApprovalAmount'].max())
