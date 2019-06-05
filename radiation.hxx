

#ifndef __RADIATION_H__
#define __RADIATION_H__

#include "field3d.hxx"
#include "bout_types.hxx"
#include "bout/generic_factory.hxx"

#include <vector>
#include <cmath>

class RadiatedPower {
public:
  const Field3D power(const Field3D &Te, const Field3D &Ne, const Field3D &Ni);
  
  virtual BoutReal power(BoutReal Te, BoutReal ne, BoutReal ni) = 0;
  
private:
};

class InterpRadiatedPower : public RadiatedPower {
public:
  InterpRadiatedPower(const std::string &file);
  
  BoutReal power(BoutReal Te, BoutReal ne, BoutReal ni);
  
private:
  std::vector<BoutReal> te_array;  // Te in eV
  std::vector<BoutReal> p_array;   // Radiative loss rate in Watts m^3
};


/// Rates supplied by Eva Havlicova
class HydrogenRadiatedPower : public RadiatedPower {
public:
  BoutReal power(BoutReal Te, BoutReal ne, BoutReal ni);
  
  // Collision rate coefficient <sigma*v> [m3/s]
  BoutReal ionisation(BoutReal Te);
  
  //<sigma*v> [m3/s]
  BoutReal recombination(BoutReal n, BoutReal Te);
  
  // <sigma*v> [m3/s]
  BoutReal chargeExchange(BoutReal Te);
  
  // <sigma*v> [m3/s]
  BoutReal excitation(BoutReal Te);
  
private:
  
};

/*!
 * Hydrogen rates, fitted by Hannah Willett May 2015
 * University of York
 */
class UpdatedRadiatedPower : public RadiatedPower {
public:
  BoutReal power(BoutReal Te, BoutReal ne, BoutReal ni);  

  // Ionisation rate coefficient <sigma*v> [m3/s]
  BoutReal ionisation(BoutReal T); 
  
  // Recombination rate coefficient <sigma*v> [m3/s]
  BoutReal recombination(BoutReal n, BoutReal T);
  
  // Charge exchange rate coefficient <sigma*v> [m3/s]
  BoutReal chargeExchange(BoutReal Te);
  
  BoutReal excitation(BoutReal Te);
  BoutReal dissociation_ion(BoutReal T);
  BoutReal Diss_H_H2(BoutReal T);
  BoutReal Ion_H2(BoutReal T);
  BoutReal Ion_charged_H2(BoutReal T);
  BoutReal Ion_charged_H2_1(BoutReal T);
  BoutReal Diss_1(BoutReal T);
  BoutReal Diss_2(BoutReal T);
  BoutReal zhwang(BoutReal T);

private:
  
};


/// Carbon in coronal equilibrium 
/// From I.H.Hutchinson Nucl. Fusion 34 (10) 1337 - 1348 (1994)
class HutchinsonCarbonRadiation : public RadiatedPower {
  BoutReal power(BoutReal Te, BoutReal ne, BoutReal ni) {
    return ne * ni * 2e-31*pow(Te/10., 3) / (1. + pow(Te/10., 4.5));
  }
};



#endif // __RADIATION_H__
