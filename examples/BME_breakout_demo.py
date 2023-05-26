import time
from machine import I2C, Pin
import bme280

i2c = I2C(0,scl=Pin(21), sda=Pin(20), freq=40000) #all sensor connected through I2C

# create BME280 sensor class instance 
bme = bme280.BME280(i2c=i2c) 


while True:
     # To read temperature, pressure and Humidity
     temperature = bme.temperature 
     pressure = bme.pressure 
     humidity = bme.humidity
    
     #print the readings
     print("\nMeasurement Values are:")
     print("Prssure = ",pressure)
     print("Tempera = ",temperature)
     print("humidity = ",humidity)
     
     time.sleep(0.5) # wait for half second



