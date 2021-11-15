import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.dates import DateFormatter
from datetime import datetime
import numpy as np

vaccine_data = pd.read_csv('owid-covid-data.csv')
vaccine_data['date']= pd.to_datetime(vaccine_data['date'])
country_and_month = vaccine_data.groupby('iso_code').resample('M', on='date').sum()
country_and_month_update = country_and_month.reset_index()
just_USA = country_and_month_update[country_and_month_update['iso_code']=='USA']

ax = sns.barplot(x="date", y="new_cases", palette=['grey'], data=just_USA)
plt.show()

def millions(val, pos):
    # the two arguments are the value and tick position
    modified_val = val*1e-6
    formatted_val = str(modified_val)
    if val == ax.get_ylim()[1]:
        formatted_val = formatted_val+'M'
    if val == 0:
        formatted_val = "0"
    return formatted_val
    #return '$%1.1fM' % (val*1e-6)

def custom_dates(val,pos):
    dates_list = just_USA.date.tolist()
    current_value = dates_list[pos]
    current_month = datetime.strftime(current_value, '%b')
    date_label = current_month
    if date_label == 'Jan':
        date_label = date_label + " '"+ datetime.strftime(current_value, '%y')
    return date_label

y_formatter = FuncFormatter(millions)
x_formatter = FuncFormatter(custom_dates)

# using a seaborn theme will make customization harder, so skip it
#sns.set_theme(style="whitegrid")
# make a barplot
ax = sns.barplot(x="date", y="new_cases", palette=['grey'], data=just_USA)

for i,bar in enumerate(ax.patches):
    if i == 6:
        bar.set_color('red')

ax.set_ylim(0,7000000)

# setting axis labels
plt.xlabel('Month')
plt.ylabel('New cases (M)')

# if you want to use rcParams, you need to use them *before* tick_params
# rcParams is the interactive version of a matplotlib stylesheet
# https://matplotlib.org/stable/tutorials/introductory/customizing.html

plt.rcParams['xtick.bottom'] = False

# manipulate the axis attributes
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html

ax.tick_params(direction='out', length=10, width=1, color='black', colors='black',pad=4, grid_color='black', grid_alpha=1, rotation=45)

# apply custom number formatter to y axis
ax.yaxis.set_major_formatter(y_formatter)
ax.xaxis.set_major_formatter(x_formatter)


# by default, this is in "data coordinates"; e.g. a value of 1 will left-align the start
# of the text with the center point of the first (in this case) column.
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html
# also, the "y" value is the bottom of the text, including multi-line text
ax.text(4,3000000, "Confirmed cases\noften lag infection\nby several weeks.");

bar_value = just_USA.new_cases.tolist()
ax.vlines( x = 6, color='black', linewidth=1, alpha=.7,
                         ymin = bar_value[6]+100000, ymax = 3000000-100000);

# ha! It uses LaTeX for text layout and mainpulation
# https://matplotlib.org/2.0.2/users/usetex.html
# plt.rc('text', usetex=True)
# plt.title(r"\textbf{Something}, but then also\\ something else")
# the following titles overwrite each other - seaborn uses matplotlib under the hood
plt.title("COVID-19 cases spike following relaxed restrictions\nin the spring of 2020", fontweight="bold")
# ax.set_title('COVID-19 cases spike following relaxed restrictions in the spring of 2020');

plt.show()
