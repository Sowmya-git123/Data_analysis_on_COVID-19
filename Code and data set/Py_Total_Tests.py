import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot  as plot
import pandas as pa
from scipy import stats

pd = pa.read_csv("covid19cases_test.csv")
X = pd["Year"]
Y = pd["total_tests"]

slope, intercept, r, p, std_err = stats.linregress(X, Y)
def lineFunc(x):
  return 5317.120793 * x -10736442.11
lineY = list(map(lineFunc, X))
print(lineY)

plot.scatter(X,Y, color='green')
plot.plot(X,lineY, color='orange')
plot.xlabel("Years")
plot.ylabel("Number of COVID-19 Dtotal_tests")
plot.title("Covid-19 total_tests")
plot.show()