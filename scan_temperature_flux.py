from matplotlib import pyplot as plt
from boutdata import collect
from boututils.plotdata import plotdata
from numpy import zeros
from numpy import array
Te_wo_9 = collect("Te",path='lossrate_1e5_no_H2c_elastic_udensity9e19/')
Te_wo_7 = collect("Te",path='lossrate_1e5_no_H2c_elastic_udensity7e19/')
Te_wo_5 = collect("Te",path='lossrate_1e5_no_H2c_elastic_udensity5e19/')
Te_wo_3 = collect("Te",path='lossrate_1e5_no_H2c_elastic_udensity3e19/')
Te_wo_25 = collect("Te",path='lossrate_1e5_no_H2c_elastic_udensity2.5e19/')
Te_wo_2 = collect("Te",path='lossrate_1e5_no_H2c_elastic')
Te_wo_1 = collect("Te",path='lossrate_1e5_no_H2c_elastic_udensity1e19/')
Te_wo_05 = collect("Te",path='lossrate_1e5_no_H2c_elastic_udensity0.5e19/')

NVhc_wo_9 = collect("NVh+",path='lossrate_1e5_no_H2c_elastic_udensity9e19/')
NVhc_wo_7 = collect("NVh+",path='lossrate_1e5_no_H2c_elastic_udensity7e19/')
NVhc_wo_5 = collect("NVh+",path='lossrate_1e5_no_H2c_elastic_udensity5e19/')
NVhc_wo_3 = collect("NVh+",path='lossrate_1e5_no_H2c_elastic_udensity3e19/')
NVhc_wo_25 = collect("NVh+",path='lossrate_1e5_no_H2c_elastic_udensity2.5e19/')
NVhc_wo_2 = collect("NVh+",path='lossrate_1e5_no_H2c_elastic')
NVhc_wo_1 = collect("NVh+",path='lossrate_1e5_no_H2c_elastic_udensity1e19/')
NVhc_wo_05 = collect("NVh+",path='lossrate_1e5_no_H2c_elastic_udensity0.5e19/')

Te_w_9 = collect("Te",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity9e19')
Te_w_7 = collect("Te",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity7e19')
Te_w_5 = collect("Te",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity5e19')
Te_w_3 = collect("Te",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity3e19')
Te_w_25 = collect("Te",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity2.5e19')
Te_w_2 = collect("Te",path='lossrate_1e5_H2c_elastic_H2_pumping')
Te_w_1 = collect("Te",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity1e19')
Te_w_05 = collect("Te",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity0.5e19')

NVhc_w_9 = collect("NVh+",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity9e19')
NVhc_w_7 = collect("NVh+",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity7e19')
NVhc_w_5 = collect("NVh+",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity5e19')
NVhc_w_3 = collect("NVh+",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity3e19')
NVhc_w_25 = collect("NVh+",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity2.5e19')
NVhc_w_2 = collect("NVh+",path='lossrate_1e5_H2c_elastic_H2_pumping')
NVhc_w_1 = collect("NVh+",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity1e19')
NVhc_w_05 = collect("NVh+",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity0.5e19')

Tnorm = collect("Tnorm",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity0.5e19')
cs0 = collect("Cs0",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity0.5e19')
Nnorm = collect("Nnorm",path='lossrate_1e5_H2c_elastic_H2_pumping_udensity0.5e19')

Nup_array=zeros(8)
Te_w_array=zeros(8)
Te_wo_array=zeros(8)
NVhc_w_array=zeros(8)
NVhc_wo_array=zeros(8)


Te_w_array[0]=Te_w_05[-1,0,-1,0]
Te_w_array[1]=Te_w_1[-1,0,-1,0]
Te_w_array[2]=Te_w_2[-1,0,-1,0]
Te_w_array[3]=Te_w_25[-1,0,-1,0]
Te_w_array[4]=Te_w_3[-1,0,-1,0]
Te_w_array[5]=Te_w_5[-1,0,-1,0]
Te_w_array[6]=Te_w_7[-1,0,-1,0]
Te_w_array[7]=Te_w_9[-1,0,-1,0]

NVhc_w_array[0]=NVhc_w_05[-1,0,-1,0]
NVhc_w_array[1]=NVhc_w_1[-1,0,-1,0]
NVhc_w_array[2]=NVhc_w_2[-1,0,-1,0]
NVhc_w_array[3]=NVhc_w_25[-1,0,-1,0]
NVhc_w_array[4]=NVhc_w_3[-1,0,-1,0]
NVhc_w_array[5]=NVhc_w_5[-1,0,-1,0]
NVhc_w_array[6]=NVhc_w_7[-1,0,-1,0]
NVhc_w_array[7]=NVhc_w_9[-1,0,-1,0]

Te_wo_array[0]=Te_wo_05[-1,0,-1,0]
Te_wo_array[1]=Te_wo_1[-1,0,-1,0]
Te_wo_array[2]=Te_wo_2[-1,0,-1,0]
Te_wo_array[3]=Te_wo_25[-1,0,-1,0]
Te_wo_array[4]=Te_wo_3[-1,0,-1,0]
Te_wo_array[5]=Te_wo_5[-1,0,-1,0]
Te_wo_array[6]=Te_wo_7[-1,0,-1,0]
Te_wo_array[7]=Te_wo_9[-1,0,-1,0]

NVhc_wo_array[0]=NVhc_wo_05[-1,0,-1,0]
NVhc_wo_array[1]=NVhc_wo_1[-1,0,-1,0]
NVhc_wo_array[2]=NVhc_wo_2[-1,0,-1,0]
NVhc_wo_array[3]=NVhc_wo_25[-1,0,-1,0]
NVhc_wo_array[4]=NVhc_wo_3[-1,0,-1,0]
NVhc_wo_array[5]=NVhc_wo_5[-1,0,-1,0]
NVhc_wo_array[6]=NVhc_wo_7[-1,0,-1,0]
NVhc_wo_array[7]=NVhc_wo_9[-1,0,-1,0]

Nup_array[0]=0.5e19
Nup_array[1]=1.0e19
Nup_array[2]=2.0e19
Nup_array[3]=2.5e19
Nup_array[4]=3.0e19
Nup_array[5]=5.0e19
Nup_array[6]=7.0e19
Nup_array[7]=9.0e19

plt.plot(Nup_array[:],Te_w_array[:]*Tnorm,label='with molecules')
plt.plot(Nup_array[:],Te_wo_array[:]*Tnorm,label='without molecules')

plt.legend(loc='upper right')

plt.grid(True)
plt.ylim([0,70])
plt.xlabel(r'Upstream density [m^-3]')
plt.ylabel("Target temperature [eV]")
plt.savefig("Scan_target_temperature.pdf")

plt.show()

####################

plt.plot(Nup_array[:],NVhc_w_array[:]*cs0*Nnorm,label='with molecules')
plt.plot(Nup_array[:],NVhc_wo_array[:]*cs0*Nnorm,label='without molecules')

plt.legend(loc='upper left')

plt.grid(True)
#plt.xlim([29,30])
plt.xlabel(r'Upstream density [m^-3]')
plt.ylabel("target flux [m-2/s]")
plt.savefig("Scan_target_flux.pdf")

plt.show()

