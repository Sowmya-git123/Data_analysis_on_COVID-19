import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot  as plot
import pandas as pa
from scipy import stats

pd = pa.read_csv("covid19cases_test.csv")
X = pd["Year"]
Y = pd["deaths"]

slope, intercept, r, p, std_err = stats.linregress(X, Y)
def lineFunc(x):
  return 0.8248 * x - 1664.13
lineY = list(map(lineFunc, X))
print(lineY)

plot.scatter(X,Y, color='green')
plot.plot(X,lineY, color='orange')
plot.xlabel("Years")
plot.ylabel("Number of COVID-19 Deaths")
plot.title("Covid-19 Deaths")
plot.show()