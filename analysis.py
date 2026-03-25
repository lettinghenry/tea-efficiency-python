import pandas as pd
import numpy as np
import statsmodels.api as sm

data = pd.read_csv("tea_data.csv")

data["log_output"] = np.log(data["output"])
data["log_land"] = np.log(data["land"])
data["log_labor"] = np.log(data["labor"])
data["log_fertilizer"] = np.log(data["fertilizer"])

X = data[["log_land", "log_labor", "log_fertilizer"]]
X = sm.add_constant(X)
y = data["log_output"]

model = sm.OLS(y, X).fit()

print(model.summary())

data["efficiency"] = np.exp(model.resid)

print(data[["output", "efficiency"]])