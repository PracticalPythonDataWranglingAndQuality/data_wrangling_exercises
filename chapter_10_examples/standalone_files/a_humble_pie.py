import matplotlib.pyplot as plt

# matplotlib works counterclockwise, so we need to essentially reverse
# the order of our pie-value "slices"
candidate_names = ['Adams', 'Wiley', 'Garcia', 'Yang', 'Others']

candidate_names.reverse()

vote_pct = [30.8, 21.3, 19.6, 12.2, 16.1]

vote_pct.reverse()

colors = ['#006d2c','#006d2c', '#006d2c', '#31a354','#74c476']

colors.reverse()

fig1, ax1 = plt.subplots()

# by default, the starting axis is the x-axis; making this value 90 ensures
# that it is a vertical line instead
ax1.pie(vote_pct, labels=candidate_names, autopct='%.1f%%', startangle=90,
 colors=colors)

ax1.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.

# show the plot!
plt.show()
