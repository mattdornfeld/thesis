import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def odefun(x, t):
	xdot = np.zeros(2)

	L = 0.014
	tau = 0.001
	ps = 10
	k = 3e3
	b = 1230
	m = 476

	a1 =  0.01 +  x[0] + tau * x[1]
	a2 = 0.01 + x[0] - tau * x[1]
	pg = ps * (1 - a2 / a1)
	print(a1)

	xdot[0] = x[1]
	xdot[1] = - k/m * x[0] - b/m * x[1] + pg

	return xdot

x0 = np.array([1, 1])
t = np.arange(0,1,0.001)
x = odeint(odefun, x0, t)
plot(x[:,0])
