# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 12:56:13 2020

@author: Cam
"""

import matplotlib.pyplot as plt

ENCUT = [400,440,480,520,560,600,640,680,720,760,800]

######################### Input for Neutral ###################################-0.52115463*10**2

# note: 3,4,5 tot energies incomplete
MASnI3_TOTAL_ENERGY = [-.52148150*10**2, -.52121700*10**2, -.52114287*10**2, -.52114619*10**2, -.52118913*10**2, -.52124353*10**2, -.52128662*10**2, -.52131580*10**2, -.52133008*10**2, -.52134118*10**2, -.52134745*10**2]
MASnI3_a = [6.1029881177602237,6.1271193416853951,6.1352214927051376, 6.1340927213732854, 6.1337465089525809, 6.1364450485062196,6.1371447517467850,6.1367651454657048,6.1331208291419985,6.1391699922416585,6.1412669744603408]
MASnI3_b = [6.1325522590384161,6.1629348258325312,6.1653998957504257, 6.1754563341847915, 6.1757997386930548, 6.1857740960672718,6.1915523765681071,6.1762930980609143,6.1803811350288225,6.1947654732365001, 6.1921093550976742]
MASnI3_c = [6.1959235377824378,6.2348682176917594,6.2568012671606086, 6.2668452040498641, 6.2677603818980669, 6.2709905383718194,6.2767181022919587,6.2814539969395593,6.2836607102121400,6.2823505143893836, 6.2877934154261403]

########################## Plotting for Neutral ####################################
fig, ax1 = plt.subplots(figsize = (7,5))

plt.title('ENCUT Convergence for MASnI3 Where EDIFFG = 10$^{-2}$')
plt.grid()

ax1.set_xlabel('ENCUT (eV)')
ax1.set_xlim(min(ENCUT), max(ENCUT))
ax1.set_ylabel('Total Energy (eV)')
ax1.set_ylim(-52.2, -52.1)
lns1 = ax1.plot(ENCUT, MASnI3_TOTAL_ENERGY, color = 'tab:orange')
ax1.tick_params(axis='y')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax2.set_ylim(6, 6.5)
ax2.set_ylabel('Lattice Paramter ($\AA$)')  # we already handled the x-label with ax1
lns2 = ax2.plot(ENCUT, MASnI3_a, color = 'tab:red')
lns3 = ax2.plot(ENCUT, MASnI3_b, color = 'tab:green')
lns4 = ax2.plot(ENCUT, MASnI3_c, color = 'tab:blue')
ax2.tick_params(axis='y')

lns = lns1+lns2+lns3+lns4
ax1.legend(lns, ('Total Energy', 'a Lattice Paramter', 'b Lattice Parameter', 'c Lattice Paramter'), loc=3)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
fig.savefig('ENCUT_MASnI3.pdf')
###############################################################################

########################### Input for 2+ ######################################
ENCUT2plus = [400,440]
MASnI3_2plus_TOTAL_ENERGY = [-0.60593479*10**2, -0.62198895*10**2, -0.62848004*10**2, -0.63786384*10**2, -0.63935233*10**2, -0.63935549*10**2, -0.63935650*10**2]
MASnI3_2plus_a = [5.2507393159294260, 5.2470979931810646, 5.0289372548025648, 5.9184718268107828, 5.8993105284783587, 5.8965812506066770, 5.8945432746386190]
MASnI3_2plus_b = [5.2402921648051812, 4.7213500618019308, 4.3222209219232566, 3.6372141113848908, 3.6198111955138477, 3.6223457776518848, 3.6239476637921522]
MASnI3_2plus_c = [5.2284739017202071, 5.2483685981823358, 5.6872947706338515, 5.8199161855757229, 5.8803671311507042, 5.8772931423376642, 5.8762554627156671]

########################## Plotting for 2+ ####################################
fig, ax1 = plt.subplots(figsize = (7,5))

plt.title('ENCUT Convergence for MASnI3 Where EDIFFG = 10$^{-2}$')
plt.grid()

ax1.set_xlabel('ENCUT (eV)')
ax1.set_xlim(min(ENCUT), max(ENCUT))
ax1.set_ylabel('Total Energy (eV)')
lns1 = ax1.plot(ENCUT2plus, MASnI3_2plus_TOTAL_ENERGY, color = 'tab:orange')
ax1.tick_params(axis='y')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax2.set_ylim(3,6)
ax2.set_ylabel('Lattice Paramter ($\AA$)')  # we already handled the x-label with ax1
lns2 = ax2.plot(ENCUT2plus, MASnI3_2plus_a, color = 'tab:red')
lns3 = ax2.plot(ENCUT2plus, MASnI3_2plus_b, color = 'tab:green')
lns4 = ax2.plot(ENCUT2plus, MASnI3_2plus_c, color = 'tab:blue')
ax2.tick_params(axis='y')

lns = lns1+lns2+lns3+lns4
ax1.legend(lns, ('Total Energy', 'a Lattice Paramter', 'b Lattice Parameter', 'c Lattice Paramter'), loc=3)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
fig.savefig('ENCUT_[MASnI3]2+.pdf')


###############################################################################

