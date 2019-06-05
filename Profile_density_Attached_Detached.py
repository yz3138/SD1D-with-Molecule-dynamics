from matplotlib import pyplot as plt
from boutdata import collect
from boututils.showdata import showdata
from numpy import zeros


##########
Nhc_w_w_attached = collect("Nh+",path='lossrate_1e5_H2c_elastic_H2_pumping')
Nhc_wo_w_attached = collect("Nh+",path='lossrate_1e5_no_H2c_elastic')
Nhc_w_w_detached = collect("Nh+",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity7e19')
Nhc_wo_w_detached = collect("Nh+",path='lossrate_1e5_no_H2c_elastic_udensity7e19')

Nh_w_w_attached = collect("Nh",path='lossrate_1e5_H2c_elastic_H2_pumping')
Nh_wo_w_attached = collect("Nh",path='lossrate_1e5_no_H2c_elastic')
Nh_w_w_detached = collect("Nh",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity7e19')
Nh_wo_w_detached = collect("Nh",path='lossrate_1e5_no_H2c_elastic_udensity7e19')

Nh2_w_w_attached = collect("Nh2",path='lossrate_1e5_H2c_elastic_H2_pumping')
Nh2_w_w_detached = collect("Nh2",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity7e19')

Nh2C_w_w_attached = collect("Nh2+",path='lossrate_1e5_H2c_elastic_H2_pumping')
Nh2C_w_w_detached = collect("Nh2+",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity7e19')

#########

path = 'lossrate_1e5_H2c_elastic_H2_pumping_udensity7e19'
nnorm = collect("Nnorm", path=path)
tnorm = collect("Tnorm", path=path)
pnorm = nnorm*tnorm*1.602e-19 # Converts p to Pascals
cs0 = collect("Cs0", path=path)

t = -1

dy = collect("dy", path=path, yguards=True) [0,:]
n = len(Nh2C_w_w_detached[-1,0,:,0])
pos = zeros(n)

pos[0] = 0.5*dy[1]
#pos[1] = 0.5*dy[1]
for i in range(1,n):
    pos[i] = pos[i-1] + 0.5*dy[i-1] + 0.5*dy[i]

#def replace_guards(var):
    """
    This in-place replaces the points in the guard cells with the points on the boundary

    """
#    var[0] = 0.5*(var[0] + var[1])
 #   var[-1] = 0.5*(var[-1] + var[-2])

#replace_guards(pos)
#replace_guards(Te_wo_w)
#replace_guards(Te_w_wo)
#replace_guards(Te_w_w)
#replace_guards(Te_wo_wo)

#Te_wo_w[-1] = Te_wo_w[-2] # Zero-gradient Te
#Te_w_wo[-1] = Te_w_wo[-2]
#Te_w_w[-1] = Te_w_w[-2]
#Te_wo_wo[-1] = Te_wo_wo[-2]

#pos.shape
#Te_w_w.shape
print(pos[:])
print(n)

############detached and attached####
plt.plot(pos-0.53,Nhc_w_w_attached[t,0,:,0]*nnorm,'r',label='attached with molecules',linewidth=2)
plt.plot(pos-0.53,Nhc_wo_w_attached[t,0,:,0]*nnorm,'k',label='attached without molecules',linewidth=2)
plt.plot(pos-0.53,Nhc_w_w_detached[t,0,:,0]*nnorm,'r-.',label='detached with molecules',linewidth=2)
plt.plot(pos-0.53,Nhc_wo_w_detached[t,0,:,0]*nnorm,'k-.',label='detached without molecules',linewidth=2)

plt.legend(loc='upper left')

plt.grid(True)
plt.xlim([29.5,30])
plt.xlabel("Position [m]")
plt.ylabel(r'Plasma Density [m^-3]')
plt.savefig("Profile_PlasmaDensity_AttachedandDetached.pdf")
plt.show()
##############
plt.plot(pos-0.53,Nh_w_w_attached[t,0,:,0]*nnorm,'r',label='attached with molecules',linewidth=2)
plt.plot(pos-0.53,Nh_wo_w_attached[t,0,:,0]*nnorm,'k',label='attached without molecules',linewidth=2)
plt.plot(pos-0.53,Nh_w_w_detached[t,0,:,0]*nnorm,'r-.',label='detached with molecules',linewidth=2)
plt.plot(pos-0.53,Nh_wo_w_detached[t,0,:,0]*nnorm,'k-.',label='detached without molecules',linewidth=2)

plt.legend(loc='upper left')

plt.grid(True)
plt.xlim([29.5,30])
plt.xlabel("Position [m]")
plt.ylabel(r'Atom Density [m^-3]')
plt.savefig("Profile_AtomDensity_AttachedandDetached.pdf")
plt.show()
###############
plt.plot(pos-0.53,Nh2_w_w_attached[t,0,:,0]*nnorm,label='attached with molecules',linewidth=2)
plt.plot(pos-0.53,Nh2_w_w_detached[t,0,:,0]*nnorm,'-.',label='detached with molecules',linewidth=2)

plt.legend(loc='upper left')

plt.grid(True)
plt.xlim([29.5,30])
plt.xlabel("Position [m]")
plt.ylabel(r'Molecule Density [m^-3]')
plt.savefig("Profile_MoleculeDensity_AttachedandDetached.pdf")
plt.show()
###############
plt.plot(pos-0.53,Nh2C_w_w_attached[t,0,:,0]*nnorm,label='attached with molecules',linewidth=2)
plt.plot(pos-0.53,Nh2C_w_w_detached[t,0,:,0]*nnorm,'-.',label='detached with molecules',linewidth=2)

plt.legend(loc='upper left')

plt.grid(True)
plt.xlim([29.5,30])
plt.xlabel("Position [m]")
plt.ylabel(r'Charged Molecule Density [m^-3]')
plt.savefig("Profile_ChargedMoleculeDensity_AttachedandDetached.pdf")
plt.show()


