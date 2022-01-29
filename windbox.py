import utils
print("

 _    _ _           _______           
| |  | (_)         | | ___ \          
| |  | |_ _ __   __| | |_/ / _____  __
| |/\| | | '_ \ / _` | ___ \/ _ \ \/ /
\  /\  / | | | | (_| | |_/ / (_) >  < 
 \/  \/|_|_| |_|\__,_\____/ \___/_/\_\
                                                                           
")
print(" For all the tasks from 1 to 5 except 4, windspeed is expected from an anemometer present near the wind-turbine or for approximation purposes
      at height 10 meter from the ground (if you're using wind-speed reports please note the height they've been reported at and use tool 4 i.e. windspeed convertor)")
print(" 1. WindEnergy Potential")
print(" 2. Rotational Speed of Windmill/turbine or Frequency of AC")
print(" 3. Voltage Output of Windmill/Turbine")
print(" 4. Windspeed Convertor")
print(" 5. Monthly Output")
x = input(" Please input the index corresponding to task that you want to perform i.e. if you want to calculate Voltage output just type "3" (omitting the double quotes)"
if (x == "1"):
  ws = int(input("Enter the windspeed (in m/s): "))
  print(str(utils.wind_energy_potential(ws)))
elif (x == "2"):
  ws = int(input("Enter the windspeed (in m/s): "))
  print(str(utils.omega_actual(ws)))
elif (x == "3"):
  ws = int(input("Enter the windspeed (in m/s): "))
  print(str(utils.voltageout(ws)))
elif (x == "4"):
  ws = int(input("Enter the windspeed (in m/s): "))
  h = int(input("Enter 
  print("Based on the location of your windmill installation select and input the appropriate hellmann constant-")
  print("Hellmann Table -
location 	                                    α
Unstable air above open water surface: 	    0.06
Neutral air above open water surface: 	    0.10
Unstable air above flat open coast: 	      0.11
Neutral air above flat open coast: 	        0.16
Stable air above open water surface: 	      0.27
Unstable air above human inhabited areas: 	0.27
Neutral air above human inhabited areas: 	  0.34
Stable air above flat open coast: 	        0.40
Stable air above human inhabited areas: 	  0.60 ")
  h = int(input("Enter the α value - "))
  print(str(utils.voltageout(ws)))
elif (x == "5"):
  print("You will need to enter hourly wind-speed i.e. 24 entries each corresponding to avg speed during the respective hour of day")
  ls = []
  for i in range(0,24):
    entry = int(input("Enter speed for " + str(i) + "th hour - "))
    ls.append(entry)
  print(str(utils.monthly_output(ls)))
else: 
print("Please input a valid index")
          
                  
                  
