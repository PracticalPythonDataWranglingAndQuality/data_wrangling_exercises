# Quick script for determining whether there are typos &c. in any of the PPP
# loan data's bank names

# importing the `pandas` library. The `as` keyword let's us essentially create
# a nickname for the library so that we can refer to it in fewer characters
import pandas as pd

# importing the `fingerprints` library, which will help us generate normalized
# labels for each of the bank names in our data set
import fingerprints

# read the recent data sample into a pandas DataFrame using the library's
# `read_csv()` method
ppp_data = pd.read_csv('public_150k_plus_recent.csv')

# use the pandas DataFrame `unique()` function to create a list of unique
# bank names in our data's `OriginatingLender` column
unique_names = ppp_data['OriginatingLender'].unique()

# confirm how many unique names there are
print(len(unique_names))

# create an empty list to hold the fingerprint of each of the unique names
fingerprint_list = []

# iterate through each name in the list of unique names
for name in unique_names:

    # for each name, generate its fingerprint
    # and append it to the end of the list
    fingerprint_list.append(fingerprints.generate(name))


# use the built-in `set()` method on our fingerprint_list, which will
# remove duplicates (and sort it)
fingerprint_set = set(fingerprint_list)

# check the length of the fingerprint_set
print(len(fingerprint_set))
