import pandas as pd
import matplotlib.pyplot as plt

# Load data to DataFrame
dataFrame = pd.read_csv("covid19cases_test.csv")

# plot density plot
# attribute is "Deaths"
dataFrame.total_tests.plot.density(color='gold')
plt.title('Density plot = Total_Tests')
plt.show()