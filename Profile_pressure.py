from matplotlib import pyplot as plt
from boutdata import collect
from boututils.showdata import showdata
from numpy import zeros

###############
Phc_wo_w = collect("Ph+",path='no_molecules_test_frecycle_0.99_Flux_4e23/')
Phc_w_wo = collect("Ph+",path='with_molecules_test_lossrate_1e4/')
Phc_w_w = collect("Ph+",path='with_molecules_test_lossrate_1e4_frecycle_0.99/')
#Phc_wo_wo = collect("Ph+",path='Without_H2_c_without_radiation/')  ##[-1,0,1:-1,0]
Phc_w_w_1e5 = collect("Ph+",path='with_molecules_test_lossrate_1e5_frecycle_0.99/')  ##[-1,0,1:-1,0]
Phc_wo_w_1e5 = collect("Ph+",path='no_molecules_test_frecycle_0.99_Flux_4e23_loss_1e5')
Phc_wo_wo = collect("Ph+",path='no_molecules_test/')

Phc_w_w_1e5_elastic = collect("Ph+",path='lossrate_1e5_H2c_elastic')
Phc_w_w_1e5_elastic_H2_pump = collect("Ph+",path='lossrate_1e5_H2c_elastic_H2_pumping')


Phc_w_w_attached = collect("Ph+",path='lossrate_1e5_H2c_elastic_H2_pumping')
Phc_wo_w_attached = collect("Ph+",path='lossrate_1e5_no_H2c_elastic')
Phc_w_w_detached = collect("Ph+",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity7e19')
Phc_wo_w_detached = collect("Ph+",path='lossrate_1e5_no_H2c_elastic_udensity7e19')
###############

Ph_wo_w = collect("Ph",path='no_molecules_test_frecycle_0.99_Flux_4e23/')
Ph_w_wo = collect("Ph",path='with_molecules_test_lossrate_1e4/')
Ph_w_w = collect("Ph",path='with_molecules_test_lossrate_1e4_frecycle_0.99/')
Ph_w_w_1e5 = collect("Ph",path='with_molecules_test_lossrate_1e5_frecycle_0.99/')  ##[-1,0,1:-1,0]
Ph_wo_w_1e5 = collect("Ph",path='no_molecules_test_frecycle_0.99_Flux_4e23_loss_1e5')
Ph_wo_wo = collect("Ph",path='no_molecules_test/')
Ph_w_w_1e5_elastic = collect("Ph",path='lossrate_1e5_H2c_elastic')
Ph_w_w_1e5_elastic_H2_pump = collect("Ph",path='lossrate_1e5_H2c_elastic_H2_pumping')

Ph_w_w_attached = collect("Ph",path='lossrate_1e5_H2c_elastic_H2_pumping')
Ph_wo_w_attached = collect("Ph",path='lossrate_1e5_no_H2c_elastic')
Ph_w_w_detached = collect("Ph",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity7e19')
Ph_wo_w_detached = collect("Ph",path='lossrate_1e5_no_H2c_elastic_udensity7e19')
#Ph_wo_wo = collect("Ph",path='Without_H2_c_without_radiation/')
##############
Ph2_w_wo = collect("Ph2",path='with_molecules_test_lossrate_1e4/')
Ph2_w_w = collect("Ph2",path='with_molecules_test_lossrate_1e4_frecycle_0.99/')
Ph2_w_w_1e5 = collect("Ph2",path='with_molecules_test_lossrate_1e5_frecycle_0.99/')
Ph2_w_w_1e5_elastic = collect("Ph2",path='lossrate_1e5_H2c_elastic')
Ph2_w_w_1e5_elastic_H2_pump = collect("Ph2",path='lossrate_1e5_H2c_elastic_H2_pumping')

Ph2_w_w_attached = collect("Ph2",path='lossrate_1e5_H2c_elastic_H2_pumping')
#Ph2_wo_w_attached = collect("Ph2",path='lossrate_1e5_no_H2c_elastic')
Ph2_w_w_detached = collect("Ph2",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity7e19')
#Ph2_wo_w_detached = collect("Ph2",path='lossrate_1e5_no_H2c_elastic_udensity7e19')
##############
Ph2c_w_wo = collect("Ph2+",path='with_molecules_test_lossrate_1e4/')
Ph2c_w_w = collect("Ph2+",path='with_molecules_test_lossrate_1e4_frecycle_0.99/')
Ph2c_w_w_1e5 = collect("Ph2+",path='with_molecules_test_lossrate_1e5_frecycle_0.99/')
Ph2c_w_w_1e5_elastic = collect("Ph2+",path='lossrate_1e5_H2c_elastic')
Ph2c_w_w_1e5_elastic_H2_pump = collect("Ph2+",path='lossrate_1e5_H2c_elastic_H2_pumping')

Ph2c_w_w_attached = collect("Ph2+",path='lossrate_1e5_H2c_elastic_H2_pumping')
#Ph2c_wo_w_attached = collect("Ph2+",path='lossrate_1e5_no_H2c_elastic')
Ph2c_w_w_detached = collect("Ph2+",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity7e19')
#Ph2c_wo_w_detached = collect("Ph2+",path='lossrate_1e5_no_H2c_elastic_udensity7e19')
#Ne_wo_w = collect("Ne",path='Include_H2_c_reaction_woH2c_wRad/')
#Ne_w_wo = collect("Ne",path='Include_H2_c_reaction_woRad/')
#Ne_w_w = collect("Ne",path='Include_H2_c_reaction_wRad/')

#Te_wo_w = collect("Te",path='Include_H2_c_reaction_woH2c_wRad/')
#Te_w_wo = collect("Te",path='Include_H2_c_reaction_woRad/')
#Te_w_w = collect("Te",path='Include_H2_c_reaction_wRad/')

path = 'with_molecules_test_lossrate_1e4_frecycle_0.99/'
nnorm = collect("Nnorm", path=path)
tnorm = collect("Tnorm", path=path)
pnorm = nnorm*tnorm*1.602e-19 # Converts p to Pascals
cs0 = collect("Cs0", path=path)

t = -1

dy = collect("dy", path=path, yguards=True) [0,:]
n = len(Phc_w_w[-1,0,:,0])
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
#plt.plot(pos,(Phc_w_w[t,0,:,0]+Ph_w_w[t,0,:,0]+Ph2_w_w[t,0,:,0]+Ph2c_w_w[t,0,:,0])*pnorm,'r',label='H2+, Rad')
plt.plot(pos-0.54,(2*Phc_w_w[t,0,:,0]+Ph_w_w[t,0,:,0]+Ph2_w_w[t,0,:,0]+2*Ph2c_w_w[t,0,:,0])*pnorm,label='H2+,pumping rate 1e4')
plt.plot(pos-0.54,(2*Phc_w_w_1e5[t,0,:,0]+Ph_w_w_1e5[t,0,:,0]+Ph2_w_w_1e5[t,0,:,0]+2*Ph2c_w_w_1e5[t,0,:,0])*pnorm,label='H2+,pumping rate 1e5')
plt.plot(pos-0.54,(2*Phc_w_wo[t,0,:,0]+Ph_w_wo[t,0,:,0]+Ph2_w_wo[t,0,:,0]+2*Ph2c_w_wo[t,0,:,0])*pnorm,'r',label='H2+,no pumping')


plt.plot(pos-0.54,(2*Phc_wo_w[t,0,:,0]+Ph_wo_w[t,0,:,0])*pnorm,'--',label='No H2,pumping rate 1e4')
plt.plot(pos-0.54,(2*Phc_wo_w_1e5[t,0,:,0]+Ph_wo_w_1e5[t,0,:,0])*pnorm,'--',label='No H2,pumping rate 1e5')


#plt.plot(pos,(Phc_wo_wo[t,0,:,0]+Ph_wo_wo[t,0,:,0]+Ph2_wo_wo[t,0,:,0])*pnorm,'--',label='w/o Rad, w/o H2+')

plt.legend(loc='lower left')

plt.grid(True)
plt.xlim([28,30])
plt.ylim([0,400])
plt.xlabel("Position [m]")
plt.ylabel(r'Total Pressure [Pa]')
plt.savefig("Profile_TotalPressure_pump.pdf")
plt.show()

#########
plt.plot(pos-0.54,(2*Phc_w_w_1e5[t,0,:,0]+Ph_w_w_1e5[t,0,:,0]+Ph2_w_w_1e5[t,0,:,0]+2*Ph2c_w_w_1e5[t,0,:,0])*pnorm,label='pumping H')
plt.plot(pos-0.54,(2*Phc_w_w_1e5_elastic[t,0,:,0]+Ph_w_w_1e5_elastic[t,0,:,0]+Ph2_w_w_1e5_elastic[t,0,:,0]+2*Ph2c_w_w_1e5_elastic[t,0,:,0])*pnorm,label='pumping H,elastic')
plt.plot(pos-0.54,(2*Phc_w_w_1e5_elastic_H2_pump[t,0,:,0]+Ph_w_w_1e5_elastic_H2_pump[t,0,:,0]+Ph2_w_w_1e5_elastic_H2_pump[t,0,:,0]+Ph2c_w_w_1e5_elastic_H2_pump[t,0,:,0])*pnorm,'r',label='pumping H and H2,elastic')
plt.legend(loc='lower left')

plt.grid(True)
plt.xlim([28,30])
plt.ylim([0,400])
plt.xlabel("Position [m]")
plt.ylabel(r'Total Pressure [Pa]')
plt.savefig("Profile_TotalPressure_elastic.pdf")
plt.show()
###########

plt.plot(pos-0.54,(2*Phc_w_w_attached[t,0,:,0]+Ph_w_w_attached[t,0,:,0]+Ph2_w_w_attached[t,0,:,0]+2*Ph2c_w_w_attached[t,0,:,0])*pnorm,label='with H2')
plt.plot(pos-0.54,(2*Phc_wo_w_attached[t,0,:,0]+Ph_wo_w_attached[t,0,:,0])*pnorm,label='without H2')

plt.legend(loc='lower left')

plt.grid(True)
plt.xlim([28,30])
plt.ylim([0,400])
plt.xlabel("Position [m]")
plt.ylabel(r'Total Pressure [Pa]')
plt.savefig("Profile_TotalPressure_attached.pdf")
plt.show()
############
plt.plot(pos-0.54,(2*Phc_w_w_detached[t,0,:,0]+Ph_w_w_detached[t,0,:,0]+Ph2_w_w_detached[t,0,:,0]+2*Ph2c_w_w_detached[t,0,:,0])*pnorm,label='with H2')
plt.plot(pos-0.54,(2*Phc_wo_w_detached[t,0,:,0]+Ph_wo_w_detached[t,0,:,0])*pnorm,label='without H2')

plt.legend(loc='lower left')

plt.grid(True)
plt.xlim([28,30])
#plt.ylim([0,400])
plt.xlabel("Position [m]")
plt.ylabel(r'Total Pressure [Pa]')
plt.savefig("Profile_TotalPressure_detached.pdf")
plt.show()

