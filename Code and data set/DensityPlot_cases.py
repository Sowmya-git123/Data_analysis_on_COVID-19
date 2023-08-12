import pandas as pd
import matplotlib.pyplot as plt

# Load data to DataFrame
dataFrame = pd.read_csv("covid19cases_test.csv")

# plot density plot
# attribute is "cases"
dataFrame.cases.plot.density(color='green')
plt.title('Density plot = Cases')
plt.show()