import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

# Parameters
kB = 8.617333262e-5  # eV/K

# Dataset
X = pd.read_csv("RT_data.csv", sep=";")

# Resistance normalization
X["R1_n"] = X["Germanium (R1)"] / X["Germanium (R1)"].iloc[0]

# Heating phase only
i_min = X["Temperature (T)"].idxmin()
X = X.loc[i_min:].copy()

# Temperature ranges
X_low = X[(X["Temperature (T)"] >= 120) &
          (X["Temperature (T)"] <= 200)].copy()

X_high = X[X["Temperature (T)"] > 345].copy()

# Data
T = X["Temperature (T)"]
R_Ge = X["R1_n"]

T_low = X_low["Temperature (T)"]
R_low = X_low["R1_n"]

T_high = X_high["Temperature (T)"]
R_high = X_high["R1_n"]

# Linear fit function
def linear_fit(x, y):
    m, q = np.polyfit(x, y, 1)
    return m, q

def linear(x, m, q):
    return m * x + q


# EXTRINSIC REGION
x_ext = np.log(T_low)
y_ext = np.log(R_low)

alpha, q_ext = linear_fit(x_ext, y_ext)
"""
plt.figure()
plt.plot(np.log(T), np.log(R_Ge), ".", markersize=3)
plt.plot(x_ext, linear(x_ext, alpha, q_ext),
         label=f"Fit: α={alpha:.4f}, q={q_ext:.4f}")
plt.xlabel("ln(T)")
plt.ylabel(r"ln($R/R_0$)")
plt.title("Germanium - Extrinsic Region")
plt.legend()
plt.grid()
plt.show()
"""

# INTRINSIC REGION
x_int = 1 / (2 * kB * T_high)
y_int = np.log(R_high)

Eg, q_int = linear_fit(x_int, y_int)

"""
plt.figure()
plt.plot(1 / (2 * kB * T), np.log(R_Ge), ".", markersize=3)
plt.plot(x_int, linear(x_int, Eg, q_int),
         label=f"Fit: Eg={Eg:.4f} eV, q={q_int:.4f}")
plt.xlabel(r"$1/(2k_BT)$ (eV$^{-1}$)")
plt.ylabel(r"ln($R/R_0$)")
plt.title("Germanium - Intrinsic Region")
plt.legend()
plt.grid()
plt.show()
"""


y_pred = linear(x_int, Eg, q_int)

rmse = np.sqrt(mean_squared_error(y_int, y_pred))
r2 = r2_score(y_int, y_pred)

print(f"Eg = {Eg:.4f} eV")
print(f"RMSE = {rmse:.6f}")
print(f"R² = {r2:.6f}")