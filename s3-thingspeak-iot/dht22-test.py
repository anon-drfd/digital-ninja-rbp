""" 
dht22-test.py 
Temperature/Humidity monitor using Raspberry Pi and DHT22. 
Data is displayed on terminal
"""
import sys
from time import sleep 
import Adafruit_DHT as dht

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
       
    print("Starting...")

    while True:
        try:
            #Get sensor data
            hmdty, temp = getSensorData()
            # DHT22 requires 2 seconds to give a reading, 
            # so, make sure to add delay of above 2 seconds.
            sleep(20)
            
        except:
            break
        
# call main 
main() 

