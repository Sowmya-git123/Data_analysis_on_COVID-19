import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot  as plot
import pandas as pa
from scipy import stats

pd = pa.read_csv("covid19cases_test.csv")
X = pd["Year"]
Y = pd["cases"]

slope, intercept, r, p, std_err = stats.linregress(X, Y)
def lineFunc(x):
  return 41.19773546 * x - 83050.19578
lineY = list(map(lineFunc, X))
print(lineY)

plot.scatter(X,Y, color='green')
plot.plot(X,lineY, color='red')
plot.xlabel("Years")
plot.ylabel("Number of COVID-19 Cases")
plot.title("Covid-19 Cases")
plot.show()