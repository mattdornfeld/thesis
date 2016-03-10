from pylab import *
from scipy.special import struve, jv
plt.style.use('bmh')

def X(x):
	return struve(1, x) / x

def R(x):
	return 1 - jv(1, 2*x) / x

x = np.arange(0.0001, 100, 0.01)

fig, ax = subplots()
ax.loglog(x, X(x), label='X(ka)')
ax.loglog(x, R(x), label='R(ka)')
ax.set_xlabel('ka')