# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 12:56:13 2020

@author: Cam
"""

import matplotlib.pyplot as plt

KPOINT = [1,2,3,4,5,6,7,8,9]

######################### Input for Neutral ###################################-0.52115463*10**2

# note: 3,4,5 tot energies incomplete
MASnI3_TOTAL_ENERGY = [-.55607901E+02, -.52816194E+02, -.52310533E+02, -.52185196E+02,-.52146937E+02,-.52133676E+02,-.52128624E+02,-.52126520E+02,-.52125597E+02]
MASnI3_a = [6.0074064097832478,6.0673289347246584,6.1031108200208566,6.1215159145638998,6.1288195018309954,6.1316849066574264,6.1330922341922891,6.1337059454833911,6.1340785829178639]
MASnI3_b = [6.0073700087221944,6.0688241977721971,6.1116342969815500,6.1336273598307978,6.1476341215162682,6.1563046863659201,6.1612725826633641,6.1635043327764798,6.1646544784982167]
MASnI3_c = [6.0073816990494358,6.1067449393072337,6.1833416719962164,6.2147823376684119,6.2351927601427013,6.2468086674163450,6.2520947206249717,6.2551794060772821,6.2566074139662975]

########################## Plotting for Neutral ####################################
fig, ax1 = plt.subplots(figsize = (7,5))

plt.title('KPOINT Convergence for MASnI3')
plt.grid()

ax1.set_xlabel('n x n x n KMESH')
ax1.set_xlim(1, len(KPOINT))
ax1.set_ylabel('Total Energy (eV)')
ax1.set_ylim(-56, -52)
lns1 = ax1.plot(KPOINT, MASnI3_TOTAL_ENERGY, color = 'tab:orange')
ax1.tick_params(axis='y')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax2.set_ylim(6, 6.5)
ax2.set_ylabel('Lattice Paramter ($\AA$)')  # we already handled the x-label with ax1
lns2 = ax2.plot(KPOINT, MASnI3_a, color = 'tab:red')
lns3 = ax2.plot(KPOINT, MASnI3_b, color = 'tab:green')
lns4 = ax2.plot(KPOINT, MASnI3_c, color = 'tab:blue')
ax2.tick_params(axis='y')

lns = lns1+lns2+lns3+lns4
ax1.legend(lns, ('Total Energy', 'a Lattice Paramter', 'b Lattice Parameter', 'c Lattice Paramter'), loc=4)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
fig.savefig('KPOINT_MASnI3.pdf')
###############################################################################

########################### Input for 2+ ######################################
KPOINT2plus = [1,2,3,4,5,6,7,8]
MASnI3_2plus_TOTAL_ENERGY = [-.73238382E+02,-.64268380E+02,-.63470133E+02,-.63935753E+02,-.63963651E+02,-.62969547E+02, -.63690244E+02, -.63937304E+02]
MASnI3_2plus_a = [5.1160170469312742, 6.1845502137936244, 5.4382876709927146, 5.9292283608136795, 5.9009214908364696, 5.0590676228843732, 5.7577317724533659, 5.8937209800939812]
MASnI3_2plus_b = [4.5005284194859181, 6.2050940835340009, 3.8518927979559758, 3.5970892984516918, 3.6267871379177956, 5.6957852286644117, 5.8125940126864890, 3.6279116264719726]
MASnI3_2plus_c = [4.6002899152872807, 3.5409372817384557, 6.0649644469942459, 5.8545773619153838, 5.8615875492212348, 4.2800795412821673, 3.8111889469688385, 5.8763765319394397] 

########################## Plotting for 2+ ####################################
fig, ax1 = plt.subplots(figsize = (7,5))

plt.title('KPOINT Convergence for [MASnI3]$^{2+}$')
plt.grid()

ax1.set_xlabel('n x n x n KMESH')
ax1.set_xlim(1, len(KPOINT2plus))
ax1.set_ylabel('Total Energy (eV)')
lns1 = ax1.plot(KPOINT2plus, MASnI3_2plus_TOTAL_ENERGY, color = 'tab:orange')
ax1.tick_params(axis='y')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

ax2.set_ylim(3,7)
ax2.set_ylabel('Lattice Paramter ($\AA$)')  # we already handled the x-label with ax1
lns2 = ax2.plot(KPOINT2plus, MASnI3_2plus_a, color = 'tab:red')
lns3 = ax2.plot(KPOINT2plus, MASnI3_2plus_b, color = 'tab:green')
lns4 = ax2.plot(KPOINT2plus, MASnI3_2plus_c, color = 'tab:blue')
ax2.tick_params(axis='y')

lns = lns1+lns2+lns3+lns4
ax1.legend(lns, ('Total Energy', 'a Lattice Paramter', 'b Lattice Parameter', 'c Lattice Paramter'), loc=4)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
fig.savefig('KPOINT_[MASnI3]2+.pdf')


###############################################################################

