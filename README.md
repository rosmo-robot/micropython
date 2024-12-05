# micropython
Micropython code for Rosmo Robot

<h2>Very much a work in progress </h2>

Quick test:
copy the lot to your esp32 and then run this

```
from RosMo import RosMo
from time import sleep

rosmo = RosMo()
rosmo.car.forward(0.5)
sleep(1)
rosmo.car.stop()
```

<hr />

The web ui is NOT currently using encoders, because I can only get one encoder to accurately control speed at any given time. When I use all 4 the interrupts interact in some way and bollox the encoder readings

<hr />


To try encoder code with one motor  

```
from RosMo_N20enc import EncodedMotor, PID
# Create a motor object
m1 = EncodedMotor(21, 39, False, 14, 9)  # Motor(fwd pin, bkwd pin, Reversed, encA, encB, frequency) Default frequency is set at 50Hz

# Create a PID object  with desired PID values
p1 = PID(m1, 3, 0, 10, 1000)  # PID(Motor object, Propotional, Derivative, Integral, Max correction speed)

while(1):
  p1.setRPM(180)
```

<hr />


# Notes on installing micropython on the esp32-s3 using windows  

Open a cmd window and install esptool.  In this example it was already installed  

![1](https://github.com/user-attachments/assets/cd0698cb-f348-4cd0-8883-90637f77b934)

Look in device manager to find which comport the board is on  (which was COM7 in my case not 36 as in illustration)

![2](https://github.com/user-attachments/assets/b9e1e3fb-3391-48a1-88fb-442cf9125dfe)

Erase the flash memory

![3](https://github.com/user-attachments/assets/b88de9c5-35d1-47e6-9c31-81fb2152973e)

Downloaded the latest bin from the micropython site

https://micropython.org/download/ESP32_GENERIC_S3/

![4](https://github.com/user-attachments/assets/58428417-d75f-4f6d-8f8d-51ce1f2fe1b2)

Navigate to the directory containing the downloaded and run the command suggested in install instructions on the micropython site

![5](https://github.com/user-attachments/assets/d0ef67af-5e5b-4e63-8cd5-13b11e7770d5)

Open Thonny and select configure interpreter.

![6](https://github.com/user-attachments/assets/47f8f673-c79e-44a7-8464-be284b05aeb8)

Select MicroPython (ESP32)

<hr />


# Notes on installing micropython on the esp32-s3 using Ubuntu  

sudo apt install pipx thonny

pipx ensurepath

pipx install esptool

Remove the Esp32s3 from the robot and connect to your computer

sudo dmesg | grep tty (note the bit after tty and make the line below match that)

esptool.py --chip esp32s3 --port /dev/ttyUSB0 erase_flash

Get the latest .bin file: https://micropython.org/download/ESP32_GENERIC_S3/

cd /Downloads (or wherever your downloads end up)

ls (to remind yourself what the file is called)

Flash the latest bin file:
esptool.py --chip esp32s3 --port /dev/ttyUSB0 write_flash -z 0 [Name of the latest bin file]


