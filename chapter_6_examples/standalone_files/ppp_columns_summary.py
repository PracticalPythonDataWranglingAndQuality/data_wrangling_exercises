# Quick script for reviewing all the column names in the PPP data
# to see what we can infer about them from the data itself

# importing the `pandas` library
import pandas as pd

# read the recent data sample into a pandas DataFrame
ppp_data = pd.read_csv('public_150k_plus_recent.csv')

# print the summary of values that appear in the `LoanStats` column
print(ppp_data.value_counts('LoanStatus'))

# print the total number of entries in the `LoanStatus` column
print(sum(ppp_data.value_counts('LoanStatus')))

# print the summary of values that appear in the `Gender` column
print(ppp_data.value_counts('Gender'))

# print the total number of entries in the `Gender` column
print(sum(ppp_data.value_counts('Gender')))

# print how many rows do not list a value for `BorrowerAddress`
print(ppp_data['BorrowerAddress'].isna().sum())
