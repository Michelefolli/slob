import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataset
X = pd.read_csv("RT_data.csv", sep=";")

# Re-normalization
X["RR1_n"] = X["RR1"] / X["RR1"].iloc[0]
X["RR3_n"] = X["RR3"] / X["RR3"].iloc[0]

# Heating phase, 120-200 K
i_min = X["Temperature (T)"].idxmin()

X_low = X.loc[i_min:]
X_low = X_low[
    (X_low["Temperature (T)"] >= 120) &
    (X_low["Temperature (T)"] <= 240)
].copy()

# Data
T = X_low["Temperature (T)"]
R_Ge = X_low["RR1_n"]
R_Ni = X_low["RR2"]
R_Cu = X_low["RR3_n"]

# Linear fits
m_Ge, q_Ge = np.polyfit(T, R_Ge, 1)
m_Ni, q_Ni = np.polyfit(T, R_Ni, 1)
m_Cu, q_Cu = np.polyfit(T, R_Cu, 1)

# Germanium
plt.figure()
plt.plot(T, R_Ge, ".", markersize=3)
plt.plot(T, m_Ge*T + q_Ge, label=f"m={m_Ge:.5f}, q={q_Ge:.4f}")
plt.xlabel("Temperature (K)")
plt.ylabel(r"$R/R_0$")
plt.title("Germanium - Low Temperature")
plt.legend()
plt.grid()
plt.show()

# Nickel
plt.figure()
plt.plot(T, R_Ni, ".", markersize=3)
plt.plot(T, m_Ni*T + q_Ni, label=f"m={m_Ni:.5f}, q={q_Ni:.4f}")
plt.xlabel("Temperature (K)")
plt.ylabel(r"$R/R_0$")
plt.title("Nickel - Low Temperature")
plt.legend()
plt.grid()
plt.show()

# Copper
plt.figure()
plt.plot(T, R_Cu, ".", markersize=3)
plt.plot(T, m_Cu*T + q_Cu, label=f"m={m_Cu:.5f}, q={q_Cu:.4f}")
plt.xlabel("Temperature (K)")
plt.ylabel(r"$R/R_0$")
plt.title("Copper - Low Temperature")
plt.legend()
plt.grid()
plt.show()