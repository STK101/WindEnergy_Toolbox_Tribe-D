import utils
def print_ascii(fn):
    f= open(fn,'r')
    print(''.join([line for line in f]))

print_ascii('windtext.txt')
print(" For all the tasks from 1 to 5 except 4, windspeed is expected from an anemometer present near the wind-turbine or for approximation purposes at height 10 meter from the ground (if you're using wind-speed reports please note the height they've been reported at and use tool 4 i.e. windspeed convertor)")
print(" 1. WindEnergy Potential")
print(" 2. Rotational Speed of Windmill/turbine or Frequency of AC")
print(" 3. Voltage Output of Windmill/Turbine")
print(" 4. Windspeed Convertor")
print(" 5. Monthly Output")
x = input("Please input the index corresponding to task that you want to perform i.e. if you want to calculate Voltage output just type 3 ")
if (x == "1"):
  ws = float(input("Enter the windspeed (in m/s): "))
  print(str(utils.wind_energy_potential(ws)) + " Watt")
elif (x == "2"):
  ws = float(input("Enter the windspeed (in m/s): "))
  print(str(utils.omega_actual(ws)) + " hz")
elif (x == "3"):
  ws = float(input("Enter the windspeed (in m/s): "))
  print(str(utils.voltageout(ws)) + " V")
elif (x == "4"):
  ws = float(input("Enter the windspeed (in m/s): "))
  hei = float(input("Input the height at which the above speed was reported (in meter) - "))
  print("Based on the location of your windmill installation select and input the appropriate hellmann constant-")
  print_ascii("HellmannTable.txt")
  h = float(input("Enter the α value - "))
  print(str(utils.windspeed_from_data(ws,hei,h)))
elif (x == "5"):
  print("You will need to enter hourly wind-speed i.e. 24 entries each corresponding to avg speed during the respective hour of day")
  ls = []
  for i in range(0,24):
    entry = float(input("Enter speed for " + str(i) + "th hour - "))
    ls.append(entry)
  print(str(utils.monthly_output(ls)) + " units")
else: 
  print("Please input a valid index")

          
                  
                  
