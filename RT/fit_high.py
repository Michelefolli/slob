import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# dataset
X = pd.read_csv("RT_data.csv", sep=";")

# re-normalizing the coulmn RR1 and RR3
X["RR1_n"] = X["RR1"] / X["RR1"].iloc[0]
X["RR3_n"] = X["RR3"] / X["RR3"].iloc[0]

# dataset with higest temperatures
i_min = X["Temperature (T)"].idxmin()

X_high = X.loc[i_min:]
X_high = X_high[X_high["Temperature (T)"] > 300].copy()


#array for graphs
T = X_high["Temperature (T)"]
R_Ge = X_high["RR1_n"]
R_Ni = X_high["RR2"]
R_Cu = X_high["RR3_n"]

#linear fit
m_Ni, q_Ni = np.polyfit(T, R_Ni, 1)
def fit_Ni(x) :
    return m_Ni*x + q_Ni

m_Cu, q_Cu = np.polyfit(T, R_Cu, 1)
def fit_Cu(x) :
    return m_Cu * x + q_Cu


#exponential fit
def exp(x, A, B, C) :
    return A * np.exp(-B*x) + C

popt, pcov = curve_fit(exp, T, R_Ge, p0=[1E4, 1E-2, 1E-2])
A_Ge, B_Ge, C_Ge = popt

def fit_Ge (x) :
    return exp(x, A_Ge, B_Ge, C_Ge)

# Germanium
plt.figure()
plt.plot(T, R_Ge, ".", markersize=3)
plt.plot(T, fit_Ge(T),
         label=f"Fit: A={A_Ge:.4f}, B={B_Ge:.4f}, C={C_Ge:.4f}")
plt.legend()
plt.xlabel("Temperature (K)")
plt.ylabel(r"$R/R_0$")
plt.title("Germanium")
plt.grid()
plt.show()

# Nickel
plt.figure()
plt.plot(T, R_Ni, ".", markersize=3)
plt.plot(T, fit_Ni(T),
         label=f"Fit: m={m_Ni:.5f}, q={q_Ni:.4f}")
plt.legend()
plt.xlabel("Temperature (K)")
plt.ylabel(r"$R/R_0$")
plt.title("Nickel")
plt.grid()
plt.show()

# Copper
plt.figure()
plt.plot(T, R_Cu, ".", markersize=3)
plt.plot(T, fit_Cu(T),
         label=f"Fit: m={m_Cu:.5f}, q={q_Cu:.4f}")
plt.legend()
plt.xlabel("Temperature (K)")
plt.ylabel(r"$R/R_0$")
plt.title("Copper")
plt.grid()
plt.show()

