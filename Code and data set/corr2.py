import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


import seaborn 
# Reading a dataset
givenDataset = pd.read_csv('c:/covid19cases_test2.csv')
# Assigning the list of columns from the dataset 
numericColumns = ['cases','deaths','total_tests','Year','positive_tests','reported_cases','reported_deaths']

# Creating a correlation matrix 
correlationMatrix  = givenDataset.loc[:,numericColumns].corr()
# Printing the correlation matrix.
print(round(correlationMatrix, 4))
# Displaying the correlation matrix

plt.figure(figsize=(16, 6))
seaborn.heatmap(correlationMatrix, annot=True)

plt.show()