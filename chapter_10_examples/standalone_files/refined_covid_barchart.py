# `pandas` for data loading; `seaborn` and `matplotlib` for visuals
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# `FuncFormatter` to format axis labels
from matplotlib.ticker import FuncFormatter

# `datetime` to interpret and customize dates
from datetime import datetime

# load the data
vaccine_data = pd.read_csv('owid-covid-data.csv')

# convert the `date` column to a "real" date
vaccine_data['date']= pd.to_datetime(vaccine_data['date'])

# group the data by country and month
country_and_month = vaccine_data.groupby('iso_code').resample('M',
 on='date').sum()

# use `reset_index()` to "flatten" the DataFrame headers
country_and_month_update = country_and_month.reset_index()

# select just the United States' data
just_USA = country_and_month_update[country_and_month_update['iso_code']=='USA']

# make the foundational barplot with `seaborn`
ax = sns.barplot(x="date", y="new_cases", palette=['#bababa'], data=just_USA)

# loop through the bars rectangles and set the color for the July, 2020
# bar to red
for i, bar in enumerate(ax.patches):
    if i == 6:
        bar.set_color('#ca0020')

# set the maximum y-axis value to 7M
ax.set_ylim(0,7000000)

# setting the axis labels
plt.xlabel('Month')
plt.ylabel('New cases (M)')

# modify the color, placement and orientation of the "tick labels"
ax.tick_params(direction='out', length=5, width=1, color='#404040',
 colors='#404040',pad=4, grid_color='#404040', grid_alpha=1,
 rotation=45)

# functions for formatting the axis "tick labels"
# `millions()` will convert the scientific notation to millions of cases
def millions(val, pos):
    modified_val = val*1e-6
    formatted_val = str(modified_val)
    if val == ax.get_ylim()[1]:
        formatted_val = formatted_val+'M'
    if val == 0:
        formatted_val = "0"
    return formatted_val


# `custom_dates()` will abbreviate the dates to be more readable
def custom_dates(val, pos):
    dates_list = just_USA.date.tolist()
    date_label = ""
    if pos is not None:
        current_value = dates_list[pos]
        current_month = datetime.strftime(current_value, '%b')
        date_label = current_month
        if date_label == 'Jan':
            date_label = date_label + " '"+ datetime.strftime(current_value,
             '%y')
    return date_label


# assign formatter functions
y_formatter = FuncFormatter(millions)
x_formatter = FuncFormatter(custom_dates)

# apply the formatter functions to the appropriate axis
ax.yaxis.set_major_formatter(y_formatter)
ax.xaxis.set_major_formatter(x_formatter)

# create and position the annotation text
ax.text(4, 3000000, "Confirmed cases\noften lag infection\nby several weeks.")

# get the value of all bars as a list
bar_value = just_USA.new_cases.tolist()

# create the leader line
ax.vlines( x = 6, color='#404040', linewidth=1, alpha=.7,
 ymin = bar_value[6]+100000, ymax = 3000000-100000)

# set the title of the chart
plt.title("COVID-19 cases spike following relaxed restrictions\n" + \
 "in the spring of 2020", fontweight="bold")

# show the chart!
plt.show()
