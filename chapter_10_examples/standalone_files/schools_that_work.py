import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# import the school test data
school_data = pd.read_csv("apib12tx.csv")

# plot test scores against the percentage of students receiving meal support
sns.scatterplot(data=school_data, x="MEALS", y="API12B", alpha=0.6, linewidth=0)

# highlight a high-performing school
highlight_school = school_data[school_data['SNAME'] == "Chin (John Yehall) Elementary"]
plt.scatter(highlight_school['MEALS'], highlight_school['API12B'],
 color='orange', alpha=1.0)

# show the plot!
plt.show()
