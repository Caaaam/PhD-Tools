import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# Sn Content Fraction
Sn_Content = [0, 0.25, 0.5, 0.75, 1] 

# Results from VASP using 4x4x1 PBE
BZA = [2.18, 1.86, 1.84, 1.82, 1.89]
HA = [2.05, 1.78, 1.76, 1.74, 1.67]
SMBA = [2.17, 1.97, 1.92, 1.92, 2.02]

Sn_Content2 = [0, 0.125, 0.25, 0.5]
PEA_Ge = [2.13, 2.09, 2.04, 1.95]
Sn_Content3 = [1]
PEA_Ge2 = [1.97]


# Uses non-linear least squares to fit, fixing both edges
def fit_func(x, a, b,c):
    return a*x**2 + b*x + c 

# Calls function to fit, Sigma weights different points, FIXING the x = 0 and 1 case 
# https://stackoverflow.com/questions/33539287/how-to-force-specific-points-in-curve-fitting
sigma = np.ones(len(Sn_Content))
sigma[[0, -1]] = 0.01
Fit_BZA, Covariance_No_Soc = curve_fit(fit_func, Sn_Content, BZA, p0=(0.1 ,1e-3, 0.1), sigma=sigma)
Fit_HA, Covariance_Soc = curve_fit(fit_func, Sn_Content, HA, p0=(0.1 ,1e-3, 0.1), sigma=sigma)
Fit_SMBA, Covariance_Soc = curve_fit(fit_func, Sn_Content, SMBA, p0=(0.1 ,1e-3, 0.1), sigma=sigma)

# Generates x values and makes a order 2 polynomial from Fit
x = np.linspace(0,1, num = 100)
BZA_Func = Fit_BZA[0]*x**2 + Fit_BZA[1]*x + Fit_BZA[2]
HA_Func = Fit_HA[0]*x**2 + Fit_HA[1]*x + Fit_HA[2]
SMBA_Func = Fit_SMBA[0]*x**2 + Fit_SMBA[1]*x + Fit_SMBA[2]

# Print statements
Fit_BZA_Text = "%.3f$x^2$ %.3fx + %.3f" % (Fit_BZA[0],Fit_BZA[1],Fit_BZA[2])
Fit_HA_Text = "%.3f$x^2$ %.3fx + %.3f" % (Fit_HA[0],Fit_HA[1],Fit_HA[2])
Fit_SMBA_Text = "%.3f$x^2$ %.3fx + %.3f" % (Fit_SMBA[0],Fit_SMBA[1],Fit_SMBA[2])

print("\nNo SoC funcion coefficients:") 
print(Fit_BZA_Text) 

print("\nSoC funcion coefficients:") 
print(Fit_HA_Text) 

# Plotting Set Up
plt.figure(figsize=(7,6))
#plt.title('Bandgap (eV) as a Function of Fraction of\nSn Content For A$_2$B1$_{1-x}$B2$_x$I$_4$')
plt.xlim(0,1)
plt.ylim(1.4,2.25)
plt.grid()

#SciPy curve fit
plt.plot(x, BZA_Func, linestyle = '--', label = 'Non-Linear Least Square Fit For BZA$_2$Pb$_{1-x}$Sn$_x$I$_4$ (Exp)')
plt.plot(x, HA_Func, linestyle = '--',label = 'Non-Linear Least Square Fit For HAPb$_{1-x}$Sn$_x$I$_4$ (Exp)')
plt.plot(x, SMBA_Func, linestyle = '--',label = 'Non-Linear Least Square Fit For (S-MBA)$_2$Pb$_{1-x}$Sn$_x$I$_4$ (DFT)')
plt.plot(np.unique(Sn_Content2),np.poly1d(np.polyfit(Sn_Content2, PEA_Ge, 1))(np.unique(Sn_Content2)), linestyle = '--', label = 'Linear Fit For PEA$_2$Ge$_{1-x}$Sn$_x$I4 (Exp)', color = 'red')
plt.text(0.6,1.85,Fit_BZA_Text)
plt.text(0.65,1.62,Fit_HA_Text)
plt.text(0.655,2.02,Fit_SMBA_Text)
plt.text(0.255,2.06, '-0.3634$x$ + 2.132')

#Scatter
plt.scatter(Sn_Content, BZA, s = 30)
plt.scatter(Sn_Content, HA, s = 30)
plt.scatter(Sn_Content, SMBA, s = 30)
plt.scatter(Sn_Content2, PEA_Ge, s = 30, color = 'red')
plt.scatter(Sn_Content3, PEA_Ge2, s = 30, color = 'red')

#Labels
plt.xticks([0,0.25,0.5,0.75,1],['0','0.25','0.5','0.75','1'])
plt.legend(loc=4)

plt.rcParams.update({'font.size': 14})
plt.ylabel('Bandgap Energy (eV)')
plt.xlabel('$x$')

# Save Fig
plt.savefig('Mixed_B_Site_Literature.pdf')
