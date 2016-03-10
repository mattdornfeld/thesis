from pylab import *
plt.style.use('bmh')

def calc_phi(x, kn):
	return sin(kn*x)

L = 10
a = 1

k = arange(0, 0.7, 0.001) 
n = arange(0, 5, 1)
kn_list = n*pi/(L+a/3/pi)/a
fig, ax = subplots()
ax.plot(k, tan(k*L/a)+2*k/3/pi, label='Characteristic equation ')
ax.plot(kn_list, zeros(len(n)), 'o', label='End correction resonance frequencies ')
ax.set_xlabel('ka')
ax.set_ylim(-10,10)
ax.set_xlim(-0.01,0.7)
ax.legend()

kn_list = n*pi/(L+a/3/pi)/2
x = np.arange(0, L, 0.1)
fig, ax = subplots()
for m, kn in enumerate(kn_list):
	phi = calc_phi(x, kn)
	ax.plot(x/L, phi, label='m='+str(m))

ax.set_title('Resonance Modes')
ax.set_xlabel('xL')
ax.legend(loc=3)



