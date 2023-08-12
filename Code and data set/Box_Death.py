import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

# Load data into DataFrame:
dataFrame = pd.read_csv("covid19cases_test.csv")

# plot box plot
sb.boxplot( data = dataFrame['deaths'], orient="v", color='red')
plt.xlabel('deaths')
plt.title('deaths')
# display
plt.show()