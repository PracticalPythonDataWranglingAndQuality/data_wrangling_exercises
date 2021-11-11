# Quick script for reviewing the all the column names in the PPP data
# to see what we can infer about them from the data itself

# importing the `pandas` library
import pandas as pd

# read the recent data into a pandas DataFrame using its `read_csv()` method
ppp_data_sample = pd.read_csv('recent_sample.csv')

# convert all missing data entries to '<NA>' using the `convertdtypes()` method
converted_data_sample = ppp_data_sample.convert_dtypes()

# transpose the whole sample
transposed_ppp_data_sample = converted_data_sample.transpose()

# print out the results!
print(transposed_ppp_data_sample)
