import pandas as pd
import matplotlib.pyplot as plt

# Load data to DataFrame
dataFrame = pd.read_csv("covid19cases_test.csv")

# plot density plot
# attribute is "Deaths"
dataFrame.deaths.plot.density(color='blue')
plt.title('Density plot = Deaths')
plt.show()