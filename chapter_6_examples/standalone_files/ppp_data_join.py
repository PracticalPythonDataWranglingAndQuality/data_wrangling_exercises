# Quick script for creating new CSVs that each contain the first few rows of
# our larger data files

# importing the `pandas` library
import pandas as pd

# read the august data into a pandas DataFrame using its `read_csv()` method
august_ppp_data = pd.read_csv('public_150k_plus_080820.csv')

# read the recent data into a pandas DataFrame using its `read_csv()` method
recent_ppp_data = pd.read_csv('public_150k_plus_recent.csv')

# now that we have both files in memory, let's merge them!
merged_data = pd.merge(august_ppp_data,recent_ppp_data,how='outer',
 left_on=['BusinessName','Lender','DateApproved'],right_on=['BorrowerName',
 'ServicingLenderName','DateApproved'],indicator=True)

# `print()` the values in the "indicator" column,
# which has a default label of `_merge`
print(merged_data.value_counts('_merge'))

# merge the data again, removing the match on `DateApproved`
merged_data_no_date = pd.merge(august_ppp_data,recent_ppp_data,how='outer',
 left_on=['BusinessName','Lender'],right_on=['BorrowerName',
 'ServicingLenderName'],indicator=True)

# `print()` the values in the "indicator" column,
# which has a default label of `_merge`
print(merged_data_no_date.value_counts('_merge'))

# merge the data again, matching only on `BusinessName`/`BorrowerName`
merged_data_biz_only = pd.merge(august_ppp_data,recent_ppp_data,how='outer',
 left_on=['BusinessName'],right_on=['BorrowerName'],indicator=True)

# `print()` the values in the "indicator" column,
# which has a default label of `_merge`
print(merged_data_biz_only.value_counts('_merge'))
