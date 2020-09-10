""" 
dht22.py 
Temperature/Humidity monitor using Raspberry Pi and DHT22. 
Data is displayed on thingspeak.com
"""
import sys
from time import sleep 
import Adafruit_DHT as dht
import requests

# Reading from DHT22 and storing the temperature and humidity
def getSensorData():
    DHT_PIN = 4 #BCM numbering of the GPIO pins.
    DHT_SENSOR = dht.DHT22 #Sensor used
    
    #Get sensor data
    hmdty, temp = dht.read_retry(DHT_SENSOR, DHT_PIN)

    #Display sensor reading to terminal screen
    if hmdty is not None and temp is not None:
        print("Temp = {0:0.01f}*C Humidity={1:0.01f}%".format(temp, hmdty))
    else:
        print("Failed to retrieve data from DHT22 sensor")
    return (hmdty, temp)

def main():
    # Enter Your API key here
    myAPI = "0QLCT2JSC02AYONS"
    
    print("Starting...")
    #This is the URL used to send the sensor reading to ThingSpeak (Do not change)
    baseURL = "https://api.thingspeak.com/update?api_key=%s" % myAPI 
    while True:
        try:
            #Get sensor data
            hmdty, temp = getSensorData()
            # If reading is valid
            if isinstance(hmdty, float) and isinstance(temp, float):

                # Formatting to two decimal places
                hmdty = '%.2f' % hmdty                       
                temp = '%.2f' % temp

                # Sending the data to thingspeak
                conn = requests.get(baseURL + '&field1=%s&field2=%s' % (hmdty, temp))                
                conn.close() # Closing the connection
            else:
                print ('Error')
            # DHT22 requires 2 seconds to give a reading, so make sure to add delay of above 2 seconds.
            sleep(20)
            
        except:
            break
        
# call main 
if __name__ == '__main__': 
   main() 

