from find_n_ratios import e_m_df
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
'''
This script reference find_n_ratios, speciffically the dataframe finding expected number of electrons for each oildrop
This script plots the charge of the oil drop against number of electrons and fits a linear line to get a value of electron charge
Asked for at the end of lab script. commented code is if y - intecept is not set for 0
'''

def lin_model (x, a ,b):
    return x * a + b

def dir_propor (x, a):
    return x * a

cleaned_df = e_m_df.dropna()

charge_tup = list(cleaned_df.index)
n = np.array(cleaned_df.iloc[:,0])
charge_val = [i[0] for i in charge_tup]
charge_err = [i[1] for i in charge_tup]

'''
USED IF Y-INTERCEPT != 0
coeff, pcov = curve_fit(lin_model, n, charge_val, sigma = charge_err, absolute_sigma=True)

m, c = coeff
float(m)
float(c)
std_coeffs = np.sqrt(np.diag(pcov)) # standard deviations of parameters
std_error = std_coeffs / np.sqrt(len(n))
'''
coeff, pcov = curve_fit(dir_propor, n, charge_val, sigma = charge_err, absolute_sigma=True)

m = coeff

std_coeffs = np.sqrt(np.diag(pcov)) # standard deviations of parameters
std_error = std_coeffs / np.sqrt(len(n)) # standard error
print(f"The Gradient m = {m} ± {std_error[0]}")

'''print(f"The Y-Intercept c = {c} ± {std_error[1]}")'''


fig, ax = plt.subplots()
ax.errorbar(n, charge_val, yerr = charge_err, fmt = ".", label= "Measured Data", alpha = 0.5, capsize = 5)

'''ax.plot(n, lin_model(n, m, c), label= "Linear Fit (Charge = N * e + c)")'''

ax.plot(n, dir_propor(n, m), label= "Linear Fit (Charge = N * e)")
ax.legend()
ax.set_ylabel("Charge of oil drop (eV)")
ax.set_xlabel("Number of electrons, N")
plt.show()
