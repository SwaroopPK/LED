# LED

  Raspberry Pi commonly known as RPi is a powerful device and it uses softwares which are either free or open source. It provides direct accessible processor pins as GPIOs. So learning computer science from scratch in such a device is better. One can learn in PC also but implementation at hardware level is not feasible as PC does not provide much hardware details.Also the newer versions of RPis have internal WiFi and Bluetooth connectivity.
  
  Here the LED is controlled using the commands in the SSH terminal. The code is written using the Python IDLE which is built in the Raspbian OS initially (The usage of IDLE and knowledge of Python language are assumed to be known).The GPIO pin 11(according to the physical numbering of the pins) is being used to make the bulb ON or OFF. The circuit is connected as shown in the below diagram.
  
  <p align="center"><img src="raspberry-pi-circuit.jpg" alt="Circuit Diagram" width="400" height="350" /></p>
  
  
  The python code is pretty simple for the required functionality. The below code are of importace for the GPIO pins to be written on or to be read from them.
      
    import RPi.GPIO as GPIO
The above code imports the Raspberry Pi Input Output Library as GPIO.     



    GPIO.setmode(GPIO.BOARD)
And this statement sets the GPIO type to **BOARD** i.e physical numbering system and



      GPIO.cleanup()
cleans up all the ports used. But be very clear that this only affects the ports that have been set in the current program. The rest of the program seems to be self eplanatory with only if-else and print statements.
