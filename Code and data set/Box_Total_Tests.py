import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

# Load data into DataFrame:
dataFrame = pd.read_csv("covid19cases_test.csv")

# plot box plot
sb.boxplot( data = dataFrame['total_tests'], orient="v", color='red')
plt.xlabel('total_tests')
plt.title('total_tests')
# display
plt.show()