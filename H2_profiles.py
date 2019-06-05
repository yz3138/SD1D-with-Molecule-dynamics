from boututils.showdata import showdata
from boutdata import collect
import matplotlib.pyplot as plt
from numpy import zeros

##path='molecules_with_carbon/'
path='molecules/'

Nnorm= collect("Nnorm",path=path)
Cs0  = collect("Cs0",path=path)

Nh2_c= collect("Nh2+",path=path)
Nh2  = collect("Nh2",path=path)
Nh   = collect("Nh",path=path)
Nh_c = collect("Nh+",path=path)
Ne   = collect("Ne",path=path)

NVh2_c= collect("NVh2+",path=path)
NVh2  = collect("NVh2",path=path)
NVh= collect("NVh",path=path)
NVh_c= collect("NVh+",path=path)

V_h2_c=NVh2_c/Nh2_c
V_h2=NVh2/Nh2
V_h=NVh/Nh
V_h_c=NVh_c/Nh_c

####
t=52
####
dy = collect("dy", path='molecules/')[0,:]
n = len(dy)
pos = zeros(n)

# position at the centre of the grid cell
pos[0] = 0.5*dy[0]
##pos[1] = 0.5*dy[1]
for i in range(2,n):
    pos[i] = pos[i-1] + 0.5*dy[i-1] + 0.5*dy[i]


####    Density profiles
plt.plot(Nh[t,0,:,0]*Nnorm,label='H')
plt.plot(Nh2[t,0,:,0]*Nnorm,label='H2')
plt.plot(Nh2_c[t,0,:,0]*Nnorm,'--',label='H2+')
plt.plot(Nh_c[t,0,:,0]*Nnorm,'--',label='H+')

plt.yscale('log')
plt.legend(loc='lower left')  ##lower right###centre
plt.grid(True)
#plt.xlabel("distance from target [m]")
plt.ylabel(r'Density (m^-3)')
plt.ylim([1e10,3e19])
plt.savefig("DensityProfile_steady.pdf")
plt.show()

##########  Flux profiles

plt.plot(NVh[t,0,:,0]/Nh[t,0,:,0]*Cs0,label='Velocity_H')
plt.plot(NVh2[t,0,:,0]/Nh2[t,0,:,0]*Cs0,label='V_H2')
plt.plot(NVh2_c[t,0,:,0]/Nh2_c[t,0,:,0]*Cs0,'--',label='V_H2+')
plt.plot(NVh_c[t,0,:,0]/Nh_c[t,0,:,0]*Cs0,'--',label='V_H+')

##plt.yscale('log')
plt.legend(loc='lower left')  ##lower right###centre
plt.grid(True)
#plt.xlabel("distance from target [m]")
plt.ylabel(r'Flux (/sm^2)')
##plt.ylim([0,1e5])
plt.savefig("FluxProfile_steady.pdf")
plt.show()




