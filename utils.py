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
