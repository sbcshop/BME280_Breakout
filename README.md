# BME280_Breakout

<img src="https://github.com/sbcshop/BME280_Breakout/blob/main/images/BME280.jpg" width="288" height="264">

The BME280 is a popular sensor module that combines temperature, humidity, and barometric pressure measurements in a single package. For a variety of uses, including interior and outdoor navigation, weather forecasting, home automation, and personal health monitoring, it offers precise readings.

Its compact size, low power consumption, and reliable performance make it a popular choice among developers and hobbyists. It is simple to incorporate into your designs and takes up little room because to its tiny form factor and integrated header. 

It features headers with pins spaced at 0.1", making it easy to attach to a breadboard for quick and convenient prototyping.

With its 3.3V compatibility and I2C interface, you can easily incorporate it into your projects with popular platforms like ESP32, RPi Pico, Raspberry Pi, Rock Pi, and other 3.3V compatible boards. This flexibility allows you to harness the power of the BME280 Breakout alongside your preferred microcontrollers, enabling precise measurements of barometric pressure, humidity, and temperature.

### Pinouts:
<img src="https://github.com/sbcshop/BME280_Breakout/blob/main/images/BME280%20PINOUT.jpg" width="492" height="161">

1)	Pitch 0.1” Header Breakout
2)	BME280 sensor


## Interfacing with RPi Pico/Pico W
Step 1: Download Thonny IDE from [link](https://thonny.org/) as per your OS and install it.

Step 2: Connect Pico with BME280 breakout as shown below.
<img src="https://github.com/sbcshop/BME280_Breakout/blob/main/images/picow-pinout.svg" width = "" height ="">

<img src="https://github.com/sbcshop/BME280_Breakout/blob/main/images/interfacing_pico_bme280.png" width = "538" height ="258">

**Interfacing Pins:**

| Pico Pins | BME280 Breakout |
|---|---|
3.3V      | 3.3V            |
GPIO21    | SCL             |
GPIO20    | SDA             |
GND       | GND             |


Step 3: Download code files from [examples](https://github.com/sbcshop/BME280_Breakout/tree/main/examples) folder, you will find [bme280.py](https://github.com/sbcshop/BME280_Breakout/blob/main/examples/bme280.py) library and [BME280_Pico_demo.py](https://github.com/sbcshop/BME280_Breakout/blob/main/examples/BME280_Pico_demo.py)

Step 4: Open both files in Thonny IDE, Connect Pico to laptop/PC and select device with suitable com port, 

<img src="https://github.com/sbcshop/BME280_Breakout/blob/main/images/scr1.png">

<img src="https://github.com/sbcshop/BME280_Breakout/blob/main/images/scr2.png">

Now Transfer the library file to RPi Pico 

<img src="https://github.com/sbcshop/BME280_Breakout/blob/main/images/scr3.png">

<img src="https://github.com/sbcshop/BME280_Breakout/blob/main/images/scr4.png">

<img src="https://github.com/sbcshop/BME280_Breakout/blob/main/images/scr5.png">

<img src="https://github.com/sbcshop/BME280_Breakout/blob/main/images/scr6.png">

With demo code open in Thonny Ide click on green button to run demo code 
<img src="https://github.com/sbcshop/BME280_Breakout/blob/main/images/scr7.png">

<img src="https://github.com/sbcshop/BME280_Breakout/blob/main/images/output.png">

To run standalone transfer demo code file as main.py inside Pico as shown below 
<img src="https://github.com/sbcshop/BME280_Breakout/blob/main/images/pico_folderview.png">

Step 1: Download Thonny IDE from [link](https://thonny.org/) as per your OS and install it.

Step 2: Connect Pico with BME280 breakout as shown below.
<img src="https://github.com/sbcshop/BME280_Breakout/blob/main/images/picow-pinout.svg" width = "" height ="">

<img src="https://github.com/sbcshop/BME280_Breakout/blob/main/images/interfacing_pico_bme280.png" width = "538" height ="258">

## Interfacing with Raspberry Pi
**Interfacing Pins:**

| Raspberry Pi Pins | BME280 Breakout |
|---|---|
3.3V     | 3.3V            |
GPIO3    | SCL             |
GPIO2    | SDA             |
GND      | GND             |


Step 3: Download code files [BME280_Pidemo.py](https://github.com/sbcshop/BME280_Breakout/blob/main/examples/BME280_Pidemo.py) from [examples](https://github.com/sbcshop/BME280_Breakout/tree/main/examples).  

Step 4: Run file using python IDE or Terminal shown as below 

<img src="https://github.com/sbcshop/BME280_Breakout/blob/main/images/python_ide_run.png">

OR

<img src="https://github.com/sbcshop/BME280_Breakout/blob/main/images/terminal_code_run.png">


### Repository Contents:
  - [/Design Data](https://github.com/sbcshop/BME280_Breakout/tree/main/Design%20Data) - This directory contains Schematic, Top and Bottom View
  - [/Mecahnical Data](https://github.com/sbcshop/BME280_Breakout/tree/main/Mechanical%20Data) - This directory contains Dimension, 3D and STEP files
  - [BME280 Datasheet](https://github.com/sbcshop/BME280_Breakout/blob/main/Documents/BME280-Datasheet.pdf)

## Related Products
  * [1.28" Round LCD Breakout](https://shop.sb-components.co.uk/products/1-28-round-lcd-breakout?_pos=2&_sid=aa1a4c610&_ss=r) 
   
     ![1.28" Round LCD Breakout](https://cdn.shopify.com/s/files/1/1217/2104/products/01_a58fb20c-7cc7-4908-bfca-549b28c721b6.png?v=1677234693&width=300)   

  * [1.3" LCD Breakout](https://shop.sb-components.co.uk/products/1-3-lcd-breakout?_pos=2&_sid=23eee937e&_ss=r) 
   
     ![1.3" LCD Breakout](https://cdn.shopify.com/s/files/1/1217/2104/products/01_1_a486ba53-c02b-4491-b110-a9b64736ad39.png?v=1677241189&width=300) 
  
  * [1.14" LCD Breakout](https://shop.sb-components.co.uk/products/1-14-inch-lcd-breakout?_pos=1&_sid=8dab247c9&_ss=r) 
   
     ![1.14" LCD Breakout](https://cdn.shopify.com/s/files/1/1217/2104/products/1.14InchLCDBreakout.png?v=1622801461&width=300) 

 
## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
