import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# (abbreviated) list of countries
countries = ['Japan', 'Iceland', 'Switzerland', 'France', 'Ireland', 'Germany',
 'Italy', 'Belgium']

# difference in years between official and actual retirement age
retirement_gap = [9, 2, 2, -1, -2, -2, -7, -8]

# zip the two lists together, and specify the column names as we make the DataFrame
retirement_data = pd.DataFrame(list(zip(countries, retirement_gap)),
 columns =['country', 'retirement_gap'])

# in practice, we might prefer to write a function that generates this list,
# based on our data values
bar_colors = ['#d01c8b', '#d01c8b', '#d01c8b', '#4dac26','#4dac26','#4dac26',
 '#4dac26','#4dac26']

# pass our data and palette to the `seaborn` `barplot()` function
ax = sns.barplot(x="retirement_gap", y="country", data=retirement_data, palette=bar_colors)

# show the plot!
plt.show()
