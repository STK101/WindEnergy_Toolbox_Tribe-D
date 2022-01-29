import math
import numpy as np
def revolution_speed_limit(wind_speed, blade_length = 1):
  tsr = 5
  return wind_speed*tsr/(math.pi * 2 * blade_length)

def wind_energy_potential(wind_speed, blade_length = 1):
  density = 1.225
  Constant = 0.3
  return (1/2) * density * (math.pi * pow(blade_length,2)) * pow(wind_speed,3) * Constant

def omega_actual(wind_speed, blade_length = 1):
  omega_wind = revolution_speed_limit(wind_speed, blade_length)
  P_wind = wind_energy_potential(wind_speed, blade_length)
  omega_torcurve = 1.85
  omega_generator = pow(P_wind/86.1, 1/2)
  omega = min(omega_wind, omega_generator )
  if (omega <=  omega_torcurve):
    return omega
  else:
    return 0

def poweroutput(wind_speed, blade_length = 1):
  omega = omega_actual(wind_speed, blade_length)
  return 630 * omega * 0.9
# fails on speed > 8.5m/s due to change in the generator curve
# output of 0 indicates faliure
 # replace by windspeed to get poweroutput

def voltageout(wind_speed, blade_length = 1):
  omega = omega_actual(wind_speed, blade_length = 1)
  return 24*omega

def monthly_output(average_wind_speeds):
    hourly_energy = [(poweroutput(average_wind_speeds[i]) + poweroutput(average_wind_speeds[i+1])) / 2  for i in range(0,len(average_wind_speeds) - 1)]
    return 30 * sum(hourly_energy)/ 1000 # 30 * daily /1000 to get in units
'''
Hellmann Table
location 	                                    α
Unstable air above open water surface: 	    0.06
Neutral air above open water surface: 	    0.10
Unstable air above flat open coast: 	      0.11
Neutral air above flat open coast: 	        0.16
Stable air above open water surface: 	      0.27
Unstable air above human inhabited areas: 	0.27
Neutral air above human inhabited areas: 	  0.34
Stable air above flat open coast: 	        0.40
Stable air above human inhabited areas: 	  0.60 
'''
  
def windspeed_from_data(wind_speed_at_h, height_original, correct_hellmann, height_new = 10):
  return wind_speed_at_h/(pow((height_original/height_new),correct_hellmann ))

