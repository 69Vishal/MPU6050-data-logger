# MPU6050-data-logger
Simple data logger for MPU6050 and Arduino

## Getting started 

Hey there, this is a simple data-logger for MPU6050 made for logging MPU6050 data to a `CSV` file for further processing. For this project you will need a Arduino nano and a MPU 6050. Connect the MPU6050 pin to arduino in the following way:
* `VCC -> 5V`
* `GND -> GND`
* `A4 -> SDA`
* `A5 -> SCL`

and you are done with harware part

## Software part
After connecting all pins, now connect you arduino to your computer with usb/serial interface. Now open Arduino IDE, and copy the code form `ARDUINO.CPP` to a new file and upload it to your computer, if you get error regarding missing library or something like that, this is because you have not installed Adafruit's MPU 6050 library, install it through library manager in tools tab and you will be fine.

Now open the `Data-log.py` and changer your serial interface where COM4 is written and run the program it will automatically create a file name `data.csv` and start recording data to it

That's it for today. Have a nice days.

# Donate
* PayPal -> balharav3@gmail.com
* UPI -> 19vishalindustries-1@okhdfcbank

Thank You
