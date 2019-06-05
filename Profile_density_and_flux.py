from matplotlib import pyplot as plt
from boutdata import collect
from boututils.showdata import showdata
from numpy import zeros


Nhc_wo_w = collect("Nh+",path='no_molecules_test_frecycle_0.99_Flux_4e23/')
Nhc_w_wo = collect("Nh+",path='with_molecules_test_frecycle_0.99/')
Nhc_w_w = collect("Nh+",path='with_molecules_test_lossrate_1e4_frecycle_0.99/')
#Nhc_wo_wo = collect("Nh+",path='Without_H2_c_without_radiation/')  ##[-1,0,1:-1,0]
Nhc_w_w_1e5 = collect("Nh+",path='with_molecules_test_lossrate_1e5_frecycle_0.99/')  ##[-1,0,1:-1,0]
Nhc_wo_w_1e5 = collect("Nh+",path='no_molecules_test_frecycle_0.99_Flux_4e23_loss_1e5')
Nhc_wo_wo = collect("Nh+",path='no_molecules_test/')
Nhc_w_w_1e5_elastic = collect("Nh+",path='lossrate_1e5_H2c_elastic')
Nhc_w_w_1e5_elastic_H2_pump = collect("Nh+",path='lossrate_1e5_H2c_elastic_H2_pumping')

Nh_wo_w = collect("Nh",path='no_molecules_test_frecycle_0.99_Flux_4e23/')
Nh_w_wo = collect("Nh",path='with_molecules_test_frecycle_0.99/')
Nh_w_w = collect("Nh",path='with_molecules_test_lossrate_1e4_frecycle_0.99/')
Nh_w_w_1e5 = collect("Nh",path='with_molecules_test_lossrate_1e5_frecycle_0.99/')  ##[-1,0,1:-1,0]
Nh_wo_w_1e5 = collect("Nh",path='no_molecules_test_frecycle_0.99_Flux_4e23_loss_1e5')
Nh_wo_wo = collect("Nh",path='no_molecules_test/')
Nh_w_w_1e5_elastic = collect("Nh",path='lossrate_1e5_H2c_elastic')
Nh_w_w_1e5_elastic_H2_pump = collect("Nh",path='lossrate_1e5_H2c_elastic_H2_pumping')


Nh2c_w_wo = collect("Nh2+",path='with_molecules_test_frecycle_0.99/')
Nh2c_w_w = collect("Nh2+",path='with_molecules_test_lossrate_1e4_frecycle_0.99/')
Nh2c_w_w_1e5 = collect("Nh2+",path='with_molecules_test_lossrate_1e5_frecycle_0.99/')
Nh2c_w_w_1e5_elastic = collect("Nh2+",path='lossrate_1e5_H2c_elastic')
Nh2c_w_w_1e5_elastic_H2_pump = collect("Nh2+",path='lossrate_1e5_H2c_elastic_H2_pumping')


#Nh2c_wo_w = collect("Nh+",path='no_molecules_test_frecycle_0.99_Flux_4e23/')
Nh2_w_wo = collect("Nh2",path='with_molecules_test_frecycle_0.99/')
Nh2_w_w = collect("Nh2",path='with_molecules_test_lossrate_1e4_frecycle_0.99/')
Nh2_w_w_1e5 = collect("Nh2",path='with_molecules_test_lossrate_1e5_frecycle_0.99/')
Nh2_w_w_1e5_elastic = collect("Nh2",path='lossrate_1e5_H2c_elastic')
Nh2_w_w_1e5_elastic_H2_pump = collect("Nh2",path='lossrate_1e5_H2c_elastic_H2_pumping')


NVhc_wo_w = collect("NVh+",path='no_molecules_test_frecycle_0.99_Flux_4e23/')
NVhc_w_wo = collect("NVh+",path='with_molecules_test_frecycle_0.99/')
NVhc_w_w = collect("NVh+",path='with_molecules_test_lossrate_1e4_frecycle_0.99/')
#NVhc_wo_wo = collect("NVh+",path='Without_H2_c_without_radiation/')
NVhc_w_w_1e5 = collect("NVh+",path='with_molecules_test_lossrate_1e5_frecycle_0.99/')  ##[-1,0,1:-1,0]
NVhc_wo_w_1e5 = collect("NVh+",path='no_molecules_test_frecycle_0.99_Flux_4e23_loss_1e5')
NVhc_wo_wo = collect("NVh+",path='no_molecules_test/')
NVhc_w_w_1e5_elastic = collect("NVh+",path='lossrate_1e5_H2c_elastic')
NVhc_w_w_1e5_elastic_H2_pump = collect("NVh+",path='lossrate_1e5_H2c_elastic_H2_pumping')

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

path = 'with_molecules_test_lossrate_1e4_frecycle_0.99/'
nnorm = collect("Nnorm", path=path)
tnorm = collect("Tnorm", path=path)
pnorm = nnorm*tnorm*1.602e-19 # Converts p to Pascals
cs0 = collect("Cs0", path=path)

t = -1

dy = collect("dy", path=path, yguards=True) [0,:]
n = len(NVhc_w_w[-1,0,:,0])
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
plt.plot(pos-0.54,NVhc_w_wo[t,0,:,0]*cs0*nnorm,'r',label='H2+,no pumping')
plt.plot(pos-0.54,NVhc_w_w[t,0,:,0]*cs0*nnorm,label='H2+,pumping rate 1e4')
plt.plot(pos-0.54,NVhc_w_w_1e5[t,0,:,0]*cs0*nnorm,label='H2+,pumping rate 1e5')
#plt.plot(pos-0.54,NVhc_wo_wo[t,0,:,0]*cs0*nnorm,'--',label='no H2+,no pumping')
plt.plot(pos-0.54,NVhc_wo_w[t,0,:,0]*cs0*nnorm,'--',label='No H2,pumping rate 1e4')
plt.plot(pos-0.54,NVhc_wo_w_1e5[t,0,:,0]*cs0*nnorm,'--',label='No H2+,pumping rate 1e5')

#plt.plot(pos,Nhc_wo_wo[t,0,:,0]*NVhc_wo_wo[t,0,:,0]*cs0*nnorm,'--',label='w/o Rad, w/o H2+')

plt.legend(loc='upper left')

plt.grid(True)
plt.xlim([0,30])
plt.xlabel("Position [m]")
plt.ylabel(r'Plasma Flux [m^-2/s]')
plt.savefig("Profile_Flux.pdf")
plt.show()
##########
plt.plot(pos-0.54,NVhc_w_w_1e5[t,0,:,0]*nnorm,label='pumping H')
plt.plot(pos-0.54,NVhc_w_w_1e5_elastic[t,0,:,0]*nnorm,'r',label='pumping H,elastic')
plt.plot(pos-0.54,NVhc_w_w_1e5_elastic_H2_pump[t,0,:,0]*nnorm,label='pumping H and H2,elastic')
plt.legend(loc='upper left')

plt.grid(True)
plt.xlim([0,30])
plt.xlabel("Position [m]")
plt.ylabel(r'Plasma Flux [m^-2/s]')
plt.savefig("Profile_Flux.pdf")
plt.show()

#######################
plt.plot(pos-0.54,Nhc_w_wo[t,0,:,0]*nnorm,'r',label='H2+,no pumping')
plt.plot(pos-0.54,Nhc_w_w[t,0,:,0]*nnorm,label='H2+,pumping rate 1e4')
plt.plot(pos-0.54,Nhc_w_w_1e5[t,0,:,0]*nnorm,label='H2+,pumping rate 1e5')
#plt.plot(pos-0.54,Nhc_wo_wo[t,0,:,0]*nnorm,'--',label='no H2+,no pumping')
plt.plot(pos-0.54,Nhc_wo_w[t,0,:,0]*nnorm,'--',label='No H2,pumping rate 1e4')
plt.plot(pos-0.54,Nhc_wo_w_1e5[t,0,:,0]*nnorm,'--',label='No H2+,pumping rate 1e5')
#plt.plot(pos,Nhc_wo_wo[t,0,:,0]*nnorm,'--',label='w/o Rad, w/o H2+')

plt.legend(loc='upper left')

plt.grid(True)
plt.xlim([29,30])
plt.xlabel("Position [m]")
plt.ylabel(r'Plasma Density [m^-3]')
plt.savefig("Profile_PlasmaDensity.pdf")
plt.show()

#######################
plt.plot(pos-0.54,Nh_w_wo[t,0,:,0]*nnorm,'r',label='H2+,no pumping')
plt.plot(pos-0.54,Nh_w_w[t,0,:,0]*nnorm,label='H2+,pumping rate 1e4')
plt.plot(pos-0.54,Nh_w_w_1e5[t,0,:,0]*nnorm,label='H2+,pumping rate 1e5')
#plt.plot(pos-0.54,Nh_wo_wo[t,0,:,0]*nnorm,'--',label='no H2+,no pumping')
plt.plot(pos-0.54,Nh_wo_w[t,0,:,0]*nnorm,'--',label='No H2,pumping rate 1e4')
plt.plot(pos-0.54,Nh_wo_w_1e5[t,0,:,0]*nnorm,'--',label='No H2+,pumping rate 1e5')
#plt.plot(pos,Nhc_wo_wo[t,0,:,0]*nnorm,'--',label='w/o Rad, w/o H2+')

plt.legend(loc='upper left')

plt.grid(True)
plt.xlim([29,30])
plt.xlabel("Position [m]")
plt.ylabel(r'Atom Density [m^-3]')
plt.savefig("Profile_atomDensity.pdf")
plt.show()
#######################

plt.plot(pos-0.54,Nh2c_w_w[t,0,:,0]*nnorm,label='H2+,pumping')
plt.plot(pos-0.54,Nh2c_w_wo[t,0,:,0]*nnorm,'r',label='H2+,no pumping')
plt.plot(pos-0.54,Nh2c_w_w_1e5[t,0,:,0]*nnorm,label='H2+,pumping rate 1e5')
#plt.plot(pos-0.54,Nh2_c_wo_w[t,0,:,0]*nnorm,'--',label='No H2,pumping')
#plt.plot(pos,Nhc_wo_wo[t,0,:,0]*nnorm,'--',label='w/o Rad, w/o H2+')

plt.legend(loc='upper left')

plt.grid(True)
plt.xlim([29,30])
plt.xlabel("Position [m]")
plt.ylabel(r'Charged Molecule Density [m^-3]')
plt.savefig("Profile_ChargedMoleculeDensity.pdf")
plt.show()
#######################

plt.plot(pos-0.54,Nh2_w_w[t,0,:,0]*nnorm,label='H2+,pumping')
plt.plot(pos-0.54,Nh2_w_wo[t,0,:,0]*nnorm,'r',label='H2+,no pumping')
plt.plot(pos-0.54,Nh2_w_w_1e5[t,0,:,0]*nnorm,label='H2+,pumping rate 1e5')
#plt.plot(pos-0.54,Nh2_wo_w[t,0,:,0]*nnorm,'--',label='No H2,pumping')
#plt.plot(pos,Nhc_wo_wo[t,0,:,0]*nnorm,'--',label='w/o Rad, w/o H2+')

plt.legend(loc='upper left')

plt.grid(True)
plt.xlim([29,30])
plt.xlabel("Position [m]")
plt.ylabel(r'Molecule Density [m^-3]')
plt.savefig("Profile_MoleculeDensity.pdf")
plt.show()

############detached and attached####
plt.plot(pos-0.54,Nhc_w_w_attached[t,0,:,0]*nnorm,label='detached without molecules')
plt.plot(pos-0.54,Nhc_wo_w_attached[t,0,:,0]*nnorm,label='attached without molecules')
plt.plot(pos-0.54,Nhc_w_w_detached[t,0,:,0]*nnorm,'--',label='detached with molecules')
plt.plot(pos-0.54,Nhc_wo_w_detached[t,0,:,0]*nnorm,'--',label='detached without molecules')

plt.legend(loc='upper left')

plt.grid(True)
plt.xlim([29,30])
plt.xlabel("Position [m]")
plt.ylabel(r'Plasma Density [m^-3]')
plt.savefig("Profile_PlasmaDensity_AttachedandDetached.pdf")
plt.show()
##############
plt.plot(pos-0.54,Nh_w_w_attached[t,0,:,0]*nnorm,label='detached without molecules')
plt.plot(pos-0.54,Nh_wo_w_attached[t,0,:,0]*nnorm,label='attached without molecules')
plt.plot(pos-0.54,Nh_w_w_detached[t,0,:,0]*nnorm,'--',label='detached with molecules')
plt.plot(pos-0.54,Nh_wo_w_detached[t,0,:,0]*nnorm,'--',label='detached without molecules')

plt.legend(loc='upper left')

plt.grid(True)
plt.xlim([29,30])
plt.xlabel("Position [m]")
plt.ylabel(r'Atom Density [m^-3]')
plt.savefig("Profile_AtomDensity_AttachedandDetached.pdf")
plt.show()
###############
plt.plot(pos-0.54,Nh2_w_w_attached[t,0,:,0]*nnorm,label='detached without molecules')
plt.plot(pos-0.54,Nh2_w_w_detached[t,0,:,0]*nnorm,'--',label='detached with molecules')

plt.legend(loc='upper left')

plt.grid(True)
plt.xlim([29,30])
plt.xlabel("Position [m]")
plt.ylabel(r'Molecule Density [m^-3]')
plt.savefig("Profile_MoleculeDensity_AttachedandDetached.pdf")
plt.show()
###############
plt.plot(pos-0.54,Nh2C_w_w_attached[t,0,:,0]*nnorm,label='detached without molecules')
plt.plot(pos-0.54,Nh2C_w_w_detached[t,0,:,0]*nnorm,'--',label='detached with molecules')

plt.legend(loc='upper left')

plt.grid(True)
plt.xlim([29,30])
plt.xlabel("Position [m]")
plt.ylabel(r'Charged Molecule Density [m^-3]')
plt.savefig("Profile_ChargedMoleculeDensity_AttachedandDetached.pdf")
plt.show()


