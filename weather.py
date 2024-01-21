import requests
import json
import config
key = config.api_key
city = input("Enter city: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + key + "&q=" + city
response = requests.get(complete_url)
x = response.json()
if(x["cod"]!="404"):
    y = x["main"]
    curr_temp = y["temp"]
    curr_pres = y["pressure"]
    curr_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    print("Temperature (in kelvin unit) = " +
                    str(curr_temp) +
          "\nAtmospheric pressure (in hPa unit) = " +
                    str(curr_pres) +
          "\nHumidity (in percentage) = " +
                    str(curr_humidity) +
          "\nDescription = " +
                    str(weather_description))
 
else:
    print(" City Not Found")






