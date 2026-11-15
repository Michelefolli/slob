import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

X = pd.read_csv("RT_data.csv", sep=";")

# re-normalizing the coulmn RR1 and RR3
X["RR1_n"] = X["RR1"] / X["RR1"].iloc[0]
X["RR3_n"] = X["RR3"] / X["RR3"].iloc[0]


T = X["Temperature (T)"]

R_Ge = X["RR1_n"]
R_Ni = X["RR2"]
R_Cu = X["RR3_n"]

# Germanium
plt.figure()
plt.plot(T, R_Ge, ".", markersize=3)
plt.xlabel("Temperature (K)")
plt.ylabel(r"$R/R_0$")
plt.title("Germanium")
plt.grid()
plt.show()

# Nickel
plt.figure()
plt.plot(T, R_Ni, ".", markersize=3)
plt.xlabel("Temperature (K)")
plt.ylabel(r"$R/R_0$")
plt.title("Nickel")
plt.grid()
plt.show()

# Copper
plt.figure()
plt.plot(T, R_Cu, ".", markersize=3)
plt.xlabel("Temperature (K)")
plt.ylabel(r"$R/R_0$")
plt.title("Copper")
plt.grid()
plt.show()


