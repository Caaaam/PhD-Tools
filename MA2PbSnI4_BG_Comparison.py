import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

# Sn Content Fraction
Sn_Content = [0,0.25,0.25,0.25,0.25,0.5,0.5,0.5,0.5,0.5,0.5,0.75,0.75,0.75,0.75,1]

# Results from VASP using 2x2x1 PBE
No_SoC_BG = [2.24,1.97,1.99,1.99,1.98,1.81,1.75,1.77,1.84,1.85,1.85,1.66,1.66,1.66,1.66,1.55]
SoC_BG = [1.59,1.5,1.5,1.49,1.5,1.44,1.43,1.47,1.47,1.43,1.44,1.42,1.42,1.41,1.42,1.4]

# Uses non-linear least squares to fit, fixing both edges
def fit_func(x, a, b,c):
    return a*x**2 + b*x + c 

# Calls function to fit, Sigma weights different points, FIXING the x = 0 and 1 case 
# https://stackoverflow.com/questions/33539287/how-to-force-specific-points-in-curve-fitting
sigma = np.ones(len(Sn_Content))
sigma[[0, -1]] = 0.01
Fit_No_SoC, Covariance_No_Soc = curve_fit(fit_func, Sn_Content, No_SoC_BG, p0=(0.1 ,1e-3, 0.1), sigma=sigma)
Fit_SoC, Covariance_Soc = curve_fit(fit_func, Sn_Content, SoC_BG, p0=(0.1 ,1e-3, 0.1), sigma=sigma)

# Generates x values and makes a order 2 polynomial from Fit
x = np.linspace(0,1, num = 100)
No_SoC_Func = Fit_No_SoC[0]*x**2 + Fit_No_SoC[1]*x + Fit_No_SoC[2]
SoC_Func = Fit_SoC[0]*x**2 + Fit_SoC[1]*x + Fit_SoC[2]

# Print statements
Fit_No_SoC_Text = "%.3f$x^2$ %.3fx + %.3f" % (Fit_No_SoC[0],Fit_No_SoC[1],Fit_No_SoC[2])
Fit_SoC_Text = "%.3f$x^2$ %.3fx + %.3f" % (Fit_SoC[0],Fit_SoC[1],Fit_SoC[2])


print("\nNo SoC funcion coefficients:") 
print(Fit_No_SoC_Text) 

print("\nSoC funcion coefficients:") 
print(Fit_SoC_Text) 


# Plotting Set Up
plt.figure(figsize=(7,6))
plt.title('Bandgap (eV) as a Function of Fraction of Sn Content')
plt.ylabel('Bandgap Energy (eV)')
plt.xlabel('Sn Content Fraction')
plt.xlim(0,1)
plt.ylim(1.35,2.25)
plt.grid()

#SciPy curve fit
plt.plot(x, No_SoC_Func, linestyle = '--')
plt.plot(x, SoC_Func, linestyle = '--')
plt.text(0.65,1.72,Fit_No_SoC_Text)
plt.text(0.65,1.45,Fit_SoC_Text)

#Scatter
plt.scatter(Sn_Content, No_SoC_BG, s = 30)
plt.scatter(Sn_Content, SoC_BG, s = 30)

# Labels 4 dayz
plt.arrow(0.44,1.77,0.06,0.04, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.arrow(0.44,1.77,0.06,0.07, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.arrow(0.44,1.77,0.06,0.00, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.arrow(0.44,1.77,0.06,-0.02, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.text(0.304,1.762, "'Columns'")

plt.arrow(0.55,1.86,-0.05,-0.01, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.text(0.555,1.85, "'Battenberg'")

plt.arrow(0.44,1.42,0.06,0.02, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.arrow(0.44,1.42,0.06,0.01, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.text(0.304,1.412, "'Columns'")

plt.arrow(0.52,1.53,-0.02,-0.06, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')
plt.text(0.52,1.52, "'Battenberg'")

plt.arrow(0.44,1.42,0.06,0.02, width = 0.0000005, head_width = 0.0000000001, fc='k', ec='k')



#Labels
plt.xticks([0,0.25,0.5,0.75,1],['0','0.25','0.5','0.75','1'])
plt.legend(('Non-Linear Least Square Fit Without SoC','Non-Linear Least Square Fit With SoC', 'Without SoC', 'With SoC'))

# Save Fig
plt.savefig('BG_Function_Graph.pdf')
