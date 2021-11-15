import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# each individual array is a row of data
FDI = np.array([[0.8, 0.7], [0.3, 0.6]])

fdi_data = pd.DataFrame(data=FDI,
 columns=['Developed', 'Developing'])

ax = sns.lineplot(data=fdi_data)

# show the plot!
plt.show()
