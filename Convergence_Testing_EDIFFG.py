# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 12:56:13 2020

@author: Cam
"""

import matplotlib.pyplot as plt

EDIFFG = [1,2,3,4,5,6,7,8,9]

######################### Input for Neutral ###################################-0.52115463*10**2

# note: 3,4,5 tot energies incomplete
MASnI3_TOTAL_ENERGY = [-0.52114645*10**2, -0.52114651*10**2, 0, 0, 0, -0.52115463*10**2, -0.52115651*10**2, -0.52115658*10**2, -0.52115661*10**2]
MASnI3_a = [6.3233483996142974, 6.2848840041444944, 6.2064950009682098, 6.1685497843256529, 6.1337211977688373, 6.1351218751881973, 6.1353453410694927, 6.1355534997109809, 6.1353784632001922]
MASnI3_b = [6.3383302315327397, 6.2994652810778762, 6.2250206032474331, 6.1976045253522614, 6.1825965859135650, 6.1774163690868296, 6.1781643429305362, 6.1776851251138769, 6.1785808819693706]
MASnI3_c = [6.3336648439892205, 6.2971415739688226, 6.2273422688892142, 6.1992990104208721, 6.2642027873841242, 6.2712925979999463, 6.2752562624994859, 6.2753319580761957, 6.2758801179481534]

########################## Plotting for Neutral ####################################
fig, ax1 = plt.subplots(figsize = (7,5))

plt.title('EDIFFG Convergence for MASnI3')
plt.grid()

ax1.set_xlabel('n where EDIFFG = (1 x 10$^{-n}$)')
ax1.set_xlim(1, len(EDIFFG))
ax1.set_ylabel('Total Energy (eV)')
ax1.set_ylim(-52.12, -52.11)
lns1 = ax1.plot(EDIFFG[:2], MASnI3_TOTAL_ENERGY[:2], color = 'tab:orange')
lns1 = ax1.plot(EDIFFG[5:], MASnI3_TOTAL_ENERGY[5:], color = 'tab:orange')
ax1.tick_params(axis='y')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax2.set_ylim(6, 6.5)
ax2.set_ylabel('Lattice Paramter ($\AA$)')  # we already handled the x-label with ax1
lns2 = ax2.plot(EDIFFG, MASnI3_a, color = 'tab:red')
lns3 = ax2.plot(EDIFFG, MASnI3_b, color = 'tab:green')
lns4 = ax2.plot(EDIFFG, MASnI3_c, color = 'tab:blue')
ax2.tick_params(axis='y')

lns = lns1+lns2+lns3+lns4
ax1.legend(lns, ('Total Energy', 'a Lattice Paramter', 'b Lattice Parameter', 'c Lattice Paramter'), loc=3)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
fig.savefig('EDIFFG_MASnI3.pdf')
###############################################################################

########################### Input for 2+ ######################################
EDIFFG2plus = [1,2,3,4,5,6,7]
MASnI3_2plus_TOTAL_ENERGY = [-0.60593479*10**2, -0.62198895*10**2, -0.62848004*10**2, -0.63786384*10**2, -0.63935233*10**2, -0.63935549*10**2, -0.63935650*10**2]
MASnI3_2plus_a = [5.2507393159294260, 5.2470979931810646, 5.0289372548025648, 5.9184718268107828, 5.8993105284783587, 5.8965812506066770, 5.8945432746386190]
MASnI3_2plus_b = [5.2402921648051812, 4.7213500618019308, 4.3222209219232566, 3.6372141113848908, 3.6198111955138477, 3.6223457776518848, 3.6239476637921522]
MASnI3_2plus_c = [5.2284739017202071, 5.2483685981823358, 5.6872947706338515, 5.8199161855757229, 5.8803671311507042, 5.8772931423376642, 5.8762554627156671]

########################## Plotting for 2+ ####################################
fig, ax1 = plt.subplots(figsize = (7,5))

plt.title('EDIFFG Convergence for [MASnI3]$^{2+}$')
plt.grid()

ax1.set_xlabel('n where EDIFFG = (1 x 10$^{-n}$)')
ax1.set_xlim(1, len(EDIFFG2plus))
ax1.set_ylabel('Total Energy (eV)')
lns1 = ax1.plot(EDIFFG2plus, MASnI3_2plus_TOTAL_ENERGY, color = 'tab:orange')
ax1.tick_params(axis='y')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax2.set_ylim(3,6)
ax2.set_ylabel('Lattice Paramter ($\AA$)')  # we already handled the x-label with ax1
lns2 = ax2.plot(EDIFFG2plus, MASnI3_2plus_a, color = 'tab:red')
lns3 = ax2.plot(EDIFFG2plus, MASnI3_2plus_b, color = 'tab:green')
lns4 = ax2.plot(EDIFFG2plus, MASnI3_2plus_c, color = 'tab:blue')
ax2.tick_params(axis='y')

lns = lns1+lns2+lns3+lns4
ax1.legend(lns, ('Total Energy', 'a Lattice Paramter', 'b Lattice Parameter', 'c Lattice Paramter'), loc=3)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
fig.savefig('EDIFFG_[MASnI3]2+.pdf')


###############################################################################

