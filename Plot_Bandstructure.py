import matplotlib.pyplot as plt
import numpy as np

def file_len(fname):
    with fname as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def unlink_wrap(dat, lims=[-np.pi, np.pi], thresh = 0.99):
    """
    Iterate over contiguous regions of `dat` (i.e. where it does not
    jump from near one limit to the other).

    This function returns an iterator object that yields slice
    objects, which index the contiguous portions of `dat`.

    This function implicitly assumes that all points in `dat` fall
    within `lims`.

    """
    jump = np.nonzero(np.abs(np.diff(dat)) > ((lims[1] - lims[0]) * thresh))[0]
    lasti = 0
    for ind in jump:
        yield slice(lasti, ind + 1)
        lasti = ind + 1
    yield slice(lasti, len(dat))

# This first file is your data file outputted from p4vasp, edit the correct file name + location here
mapbi = open('MAPbI3.txt', 'r')
mapbi3 = open('MAPbI3_new.txt', 'w')
mapbi3.truncate()

# This cleans the file
with open('MAPbI3.txt','r') as f:
    for line in f:
        cleanedLine = line.split()
        if cleanedLine:
            mapbi3.write(cleanedLine[0] + ',' + cleanedLine[1] + '\n')

# This loads the data into x and y variables
x, y = np.loadtxt('MAPbI3_new.txt', delimiter=',', unpack=True)#

# This uses an external function from
# https://stackoverflow.com/questions/27138751/preventing-plot-joining-when-values-wrap-in-matplotlib-plots
lims = [0, max(x)]
x = (x % lims[1])
for slc in unlink_wrap(x, lims, 0.96):
    plt.plot(x[slc], y[slc], 'k', linewidth=1)

# XKCD style plot available below:

# with plt.xkcd():
#     lims = [0, max(x)]
#     x = (x % lims[1])
#     for slc in unlink_wrap(x, lims, 0.96):
#         plt.plot(x[slc], y[slc], 'k', linewidth=1)
#     plt.annotate(
#         'I went and did some physics',
#         xy = (1.3,3),
#         arrowprops=dict(arrowstyle='->'),
#         xytext=(0.4,-0.5)
#     )

plt.xlim(min(x), max(x))
plt.xlabel('Momentum space distance (k)')
plt.ylabel('Energy (eV)')
plt.title('Bandstructure of MAPbI$_3$')
plt.legend()
plt.show()

mapbi.close()
mapbi3.close()