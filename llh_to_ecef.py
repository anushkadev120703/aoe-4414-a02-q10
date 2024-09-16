# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km
#  converts LLH vector components to ECEF
# Parameters:
#  lat_deg: LLH latitude in degrees
#  lon_deg: LLH longitude in degrees
#  hae_km: height above ellipsoid in kilometers
#
# Output:
#  Prints r_x, r_y and r_z in kilometers
#
# Written by Anushka Devarajan
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# "constants"
R_E_KM = 6378.1363
E_E    = 0.081819221456

# helper functions
lat_deg = float('nan') #LLH latitude in degrees
lon_deg = float('nan') #LLH longitude in degrees
hae_km = float('nan') # height above the ellipsoid in km

# parse script arguments
if len(sys.argv)==4:
  lat_deg = float(sys.argv[1])
  lon_deg = float(sys.argv[2])
  hae_km = float(sys.argv[3])
else:
  print(\
   'Usage: '\
   'python3 ecef_to_llh.py lat_deg lon_deg hae_km'\
  )
  exit()

lat_rad = lat_deg * math.pi/180
lon_rad = lon_deg *math.pi/180

c_E= R_E_KM/(math.sqrt(1-(E_E**2)*(math.sin(lat_rad))**2))
s_E= (R_E_KM*(1-E_E**2))/(math.sqrt(1-(E_E**2)*(math.sin(lat_rad))**2))
r_x_km = (c_E + hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
r_y_km = (c_E + hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
r_z_km = (s_E+ hae_km)*math.sin(lat_rad)

#print r_x, r_y and r_z in km
print(r_x_km)
print(r_y_km)
print(r_z_km)